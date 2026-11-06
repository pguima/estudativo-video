import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import catalogo_lib as lib
import validar_catalogo as val
import tempfile
import openpyxl
import gerar_planilha as pla


def aula(id="MAT-FRA-001", **campos):
    base = {
        "id": id, "titulo": "Somar frações", "materia": "Matemática",
        "trilha": "Frações", "modulo": "Somar", "ordem": "1",
        "habilidade": "Ao final, você consegue somar frações",
        "camada": "nucleo", "tipo": "aula", "prereqs": "",
        "provas": "enem", "prioridade": "1", "termo_busca": "somar frações",
    }
    base.update(campos)
    return base


class TestLib(unittest.TestCase):
    def test_lista_ignora_vazios_e_espacos(self):
        self.assertEqual(lib.lista(" a; b;;"), ["a", "b"])

    def test_parsear_regra(self):
        self.assertEqual(
            lib.parsear_regra("materia=Matemática;camada=nivelamento|nucleo"),
            {"materia": ["Matemática"], "camada": ["nivelamento", "nucleo"]},
        )

    def test_playlist_filtra_e_mantem_ordem_do_curso(self):
        aulas = [
            aula("A", camada="nivelamento"),
            aula("B", camada="extensao"),
            aula("C", camada="nucleo"),
        ]
        playlist = {"regra": "materia=Matemática;camada=nivelamento|nucleo"}
        ids = [a["id"] for a in lib.aulas_da_playlist(playlist, aulas)]
        self.assertEqual(ids, ["A", "C"])

    def test_playlist_de_prova_olha_a_lista_de_provas(self):
        aulas = [aula("A", provas="enem;fuvest"), aula("B", provas="enem")]
        playlist = {"regra": "prova=fuvest"}
        ids = [a["id"] for a in lib.aulas_da_playlist(playlist, aulas)]
        self.assertEqual(ids, ["A"])

    def test_constantes_da_spec(self):
        self.assertEqual(lib.MIN_AULAS_PROVA, 10)
        self.assertEqual(lib.PROVAS, ("enem", "fuvest", "unicamp", "unesp", "uerj"))
        self.assertEqual(lib.CAMADAS, ("nivelamento", "nucleo", "extensao"))
        self.assertEqual(lib.TIPOS_AULA, ("aula", "pratica"))
        self.assertEqual(lib.TIPOS_PLAYLIST, ("trilha", "materia", "comece_aqui", "prova", "especial"))
        self.assertEqual(lib.CAMPOS_AULA, (
            "id", "titulo", "materia", "trilha", "modulo", "ordem", "habilidade",
            "camada", "tipo", "prereqs", "provas", "prioridade", "termo_busca",
        ))
        self.assertIn("tipo", lib.CHAVES_REGRA)

    def test_ler_csv_linha_curta_vira_campo_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "x.csv"
            caminho.write_text("a,b,c\n1\n1,2,3,4\n", encoding="utf-8")
            linhas = lib.ler_csv(caminho)
        self.assertEqual(linhas[0], {"a": "1", "b": "", "c": "", "_linha": 2})
        self.assertEqual(linhas[1], {"a": "1", "b": "2", "c": "3", "_linha": 3, "_extra": ["4"]})

    def test_carregar_le_os_559_assuntos(self):
        cat = lib.carregar()
        self.assertEqual(len(cat.assuntos), 559)
        self.assertEqual(cat.assuntos[0]["area"], "Matemática")


def tem(teste, erros, trecho):
    teste.assertTrue(any(trecho in e for e in erros), f"{trecho!r} não está em {erros}")


def catalogo(aulas=(), playlists=(), cobertura=(), assuntos=()):
    return lib.Catalogo(list(aulas), list(playlists), list(cobertura), list(assuntos))


class TestCampos(unittest.TestCase):
    def test_id_repetido(self):
        erros = val.checar_campos(catalogo([aula("A"), aula("A")]))
        self.assertTrue(any("repetido" in e for e in erros))

    def test_campo_vazio(self):
        erros = val.checar_campos(catalogo([aula("A", habilidade="")]))
        self.assertTrue(any("habilidade" in e for e in erros))

    def test_prereqs_podem_ser_vazios(self):
        self.assertEqual(val.checar_campos(catalogo([aula("A", prereqs="")])), [])

    def test_valores_fora_da_lista(self):
        for campo, valor in (("camada", "x"), ("tipo", "x"), ("prioridade", "9"), ("provas", "enem;ufpr")):
            erros = val.checar_campos(catalogo([aula("A", **{campo: valor})]))
            self.assertTrue(any(campo in e for e in erros), campo)

    def test_ordem_deve_crescer_dentro_do_modulo(self):
        erros = val.checar_campos(catalogo([aula("A", ordem="2"), aula("B", ordem="1")]))
        self.assertTrue(any("ordem" in e for e in erros))


class TestCamposNovos(unittest.TestCase):
    def test_provas_so_com_separador_e_vazio(self):
        erros = val.checar_campos(catalogo([aula("A", provas=";")]))
        self.assertTrue(any("campo vazio: provas" in e for e in erros))

    def test_ordem_nao_numerica(self):
        erros = val.checar_campos(catalogo([aula("A", ordem="x")]))
        self.assertTrue(any("ordem não numérica" in e for e in erros))

    def test_linha_curta_vira_erro_e_nao_traceback(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "aulas.csv"
            caminho.write_text(",".join(lib.CAMPOS_AULA) + "\nA,Titulo\n", encoding="utf-8")
            linhas = lib.ler_csv(caminho)
        erros = val.checar_campos(catalogo(linhas))
        self.assertTrue(any("campo vazio: habilidade" in e for e in erros))


class TestPrereqs(unittest.TestCase):
    def test_prereq_inexistente(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="Z")]))
        self.assertTrue(any("inexistente" in e for e in erros))

    def test_prereq_depois_da_aula(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="B"), aula("B")]))
        self.assertTrue(any("depois" in e for e in erros))

    def test_circulo_e_detectado(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="B"), aula("B", prereqs="A")]))
        tem(self, erros, "A: pré-requisito vem depois ou forma círculo: B")

    def test_aula_nao_depende_de_si_mesma(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="A")]))
        tem(self, erros, "A: pré-requisito vem depois ou forma círculo: A")

    def test_ordem_correta_passa(self):
        self.assertEqual(val.checar_prereqs(catalogo([aula("A"), aula("B", prereqs="A")])), [])


class TestCamadas(unittest.TestCase):
    def test_nucleo_nao_depende_de_extensao(self):
        cat = catalogo([aula("A", camada="extensao"), aula("B", camada="nucleo", prereqs="A")])
        self.assertTrue(any("Extensão" in e for e in val.checar_camadas(cat)))

    def test_nivelamento_sem_dependente(self):
        cat = catalogo([aula("A", camada="nivelamento")])
        self.assertTrue(any("Nivelamento" in e for e in val.checar_camadas(cat)))

    def test_nivelamento_com_dependente_passa(self):
        cat = catalogo([aula("A", camada="nivelamento"), aula("B", prereqs="A")])
        self.assertEqual(val.checar_camadas(cat), [])

    def test_nivelamento_usado_so_por_extensao(self):
        cat = catalogo([aula("A", camada="nivelamento"), aula("B", camada="extensao", prereqs="A")])
        self.assertTrue(any("Nivelamento" in e for e in val.checar_camadas(cat)))

    def test_nivelamento_encadeado_passa(self):
        cat = catalogo([
            aula("A", camada="nivelamento"),
            aula("B", camada="nivelamento", prereqs="A"),
            aula("C", prereqs="B"),
        ])
        self.assertEqual(val.checar_camadas(cat), [])

    def test_pratica_de_nivelamento_sem_dependente_passa(self):
        cat = catalogo([
            aula("A", camada="nivelamento"),
            aula("B", prereqs="A"),
            aula("C", camada="nivelamento", tipo="pratica", ordem="2"),
        ])
        self.assertEqual(val.checar_camadas(cat), [])


class TestModulos(unittest.TestCase):
    def test_modulo_sem_pratica(self):
        tem(self, val.checar_modulos(catalogo([aula("A")])), "não termina em prática")

    def test_pratica_deve_ser_a_ultima(self):
        cat = catalogo([aula("A", tipo="pratica", ordem="1"), aula("B", ordem="2")])
        tem(self, val.checar_modulos(cat), "não termina em prática")

    def test_modulo_correto_passa(self):
        cat = catalogo([aula("A", ordem="1"), aula("B", tipo="pratica", ordem="2")])
        self.assertEqual(val.checar_modulos(cat), [])


class TestCobertura(unittest.TestCase):
    ASSUNTOS = [
        {"area": "Matemática", "assunto": "Frações"},
        {"area": "Humanas", "assunto": "Vargas"},
    ]

    def test_assunto_fora_da_cobertura(self):
        erros = val.checar_cobertura(catalogo(assuntos=self.ASSUNTOS))
        self.assertEqual(len(erros), 2)

    def test_filtro_por_area(self):
        erros = val.checar_cobertura(catalogo(assuntos=self.ASSUNTOS), ["Matemática"])
        self.assertEqual(len(erros), 1)

    def test_linha_sem_aula_e_sem_justificativa(self):
        linha = {"area": "Matemática", "assunto": "Frações", "aulas": "", "justificativa": ""}
        erros = val.checar_cobertura(catalogo(cobertura=[linha], assuntos=self.ASSUNTOS[:1]))
        self.assertTrue(any("justificativa" in e for e in erros))

    def test_aula_inexistente(self):
        linha = {"area": "Matemática", "assunto": "Frações", "aulas": "Z", "justificativa": ""}
        erros = val.checar_cobertura(catalogo(cobertura=[linha], assuntos=self.ASSUNTOS[:1]))
        self.assertTrue(any("inexistente" in e for e in erros))

    def test_justificativa_basta(self):
        linha = {"area": "Matemática", "assunto": "Frações", "aulas": "", "justificativa": "Unida a outro"}
        erros = val.checar_cobertura(catalogo(cobertura=[linha], assuntos=self.ASSUNTOS[:1]))
        self.assertEqual(erros, [])

    def test_assunto_que_nao_esta_no_cronograma(self):
        linha = {"area": "Matemática", "assunto": "Outro", "aulas": "", "justificativa": "x"}
        erros = val.checar_cobertura(catalogo(cobertura=[linha], assuntos=self.ASSUNTOS[:1]))
        self.assertTrue(any("fora do cronograma" in e for e in erros))


def playlist(id="P1", tipo="trilha", regra="materia=Matemática;trilha=Frações", **campos):
    base = {
        "id": id, "titulo": f"Playlist {id}", "tipo": tipo, "materia": "Matemática",
        "regra": regra, "descricao": "Descrição", "termo_busca": "frações",
    }
    base.update(campos)
    return base


MATERIA = playlist("P2", "materia", "materia=Matemática;camada=nivelamento|nucleo")


class TestPlaylists(unittest.TestCase):
    def test_catalogo_correto_passa(self):
        self.assertEqual(val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA])), [])

    def test_playlist_vazia(self):
        vazia = playlist("P3", regra="materia=Física")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, vazia]))
        self.assertTrue(any("vazia" in e for e in erros))

    def test_chave_de_regra_desconhecida(self):
        ruim = playlist("P3", regra="serie=1")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, ruim]))
        self.assertTrue(any("regra" in e for e in erros))

    def test_regra_vazia(self):
        ruim = playlist("P3", regra="")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, ruim]))
        self.assertTrue(any("regra" in e for e in erros))

    def test_tipo_invalido(self):
        ruim = playlist("P3", tipo="outro")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, ruim]))
        self.assertTrue(any("tipo" in e for e in erros))

    def test_checar_playlists_nao_conta_trilhas(self):
        self.assertEqual(val.checar_playlists(catalogo([aula("A")], [MATERIA])), [])
        self.assertEqual(
            val.checar_playlists(catalogo([aula("A")], [playlist(), playlist("P3"), MATERIA])), [])

    def test_tipo_invalido_nao_vira_regra_invalida(self):
        ruim = playlist("P3", tipo="outro")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, ruim]))
        tem(self, erros, "P3: tipo inválido: outro")
        self.assertFalse(any("regra inválida" in e for e in erros), erros)

    def test_extensao_fora_da_materia_passa(self):
        cat = catalogo([aula("A", camada="extensao")], [playlist()])
        self.assertEqual(val.checar_playlists(cat), [])

    def test_titulo_repetido(self):
        p1 = playlist("P1", titulo="Igual")
        p2 = playlist("P2", "materia", MATERIA["regra"], titulo="Igual")
        erros = val.checar_playlists(catalogo([aula("A")], [p1, p2]))
        self.assertTrue(any("título repetido" in e for e in erros))


def playlist_prova(id="P3", prova="fuvest", **campos):
    return playlist(id, "prova", f"materia=Matemática;prova={prova};tipo=aula", **campos)


def aulas_de_prova(n, prova="fuvest", praticas=0):
    aulas = [aula(f"A{i}", ordem=str(i), provas=prova) for i in range(1, n + 1)]
    aulas += [
        aula(f"P{i}", tipo="pratica", ordem=str(n + i), provas=prova)
        for i in range(1, praticas + 1)
    ]
    return aulas


class TestEstruturaPlaylists(unittest.TestCase):
    def erros(self, aulas, playlists):
        return val.checar_estrutura_playlists(catalogo(aulas, playlists))

    def tem(self, erros, trecho):
        self.assertTrue(any(trecho in e for e in erros), erros)

    def test_playlists_esperadas_puras(self):
        aulas = [
            aula("A", camada="nivelamento", provas="enem"),
            aula("B", ordem="2", provas="enem"),
            aula("C", camada="extensao", ordem="3", provas="enem"),
            aula("D", tipo="pratica", ordem="4", provas="enem"),
        ]
        self.assertEqual(val.playlists_esperadas(aulas), {
            ("trilha", "Matemática", "Frações"): ["A", "B", "C", "D"],
            ("materia", "Matemática", ""): ["A", "B", "D"],
            ("comece_aqui", "Matemática", ""): ["A"],
        })

    def test_prova_so_com_minimo_de_aulas_sem_praticas(self):
        esperadas = val.playlists_esperadas(aulas_de_prova(10, "fuvest", praticas=1))
        self.assertEqual(len(esperadas[("prova", "Matemática", "fuvest")]), 10)
        esperadas = val.playlists_esperadas(aulas_de_prova(9, "fuvest", praticas=1))
        self.assertNotIn(("prova", "Matemática", "fuvest"), esperadas)

    def test_catalogo_correto_passa(self):
        self.assertEqual(self.erros([aula("A")], [playlist(), MATERIA]), [])

    def test_aula_fora_da_playlist_de_materia(self):
        self.tem(self.erros([aula("A")], [playlist()]), "falta")

    def test_extensao_dentro_da_playlist_de_materia(self):
        aulas = [aula("A"), aula("B", camada="extensao", ordem="2")]
        larga = playlist("P2", "materia", "materia=Matemática")
        self.tem(self.erros(aulas, [playlist(), larga]), "ids diferentes")

    def test_aula_de_fisica_coberta_so_por_playlist_de_matematica(self):
        aulas = [aula("A"), aula("F", materia="Física", trilha="Cinemática", modulo="MRU")]
        playlists = [
            playlist(), MATERIA,
            playlist("P3", regra="materia=Física;trilha=Cinemática", materia="Física"),
        ]
        self.tem(self.erros(aulas, playlists), "falta")

    def test_materia_da_playlist_divergente_do_filtro(self):
        # coluna materia=Física, filtro de Matemática: chave real ("materia","Física") não é a esperada
        divergente = playlist("P2", "materia", MATERIA["regra"], materia="Física")
        erros = self.erros([aula("A")], [playlist(), divergente])
        self.tem(erros, "falta")

    def test_materia_divergente_cai_em_ids_diferentes(self):
        aulas = [aula("A"), aula("F", materia="Física", trilha="Cinemática", modulo="MRU")]
        materia_fis = playlist("P3", "materia", "materia=Matemática;camada=nivelamento|nucleo", materia="Física")
        playlists = [
            playlist(), MATERIA, materia_fis,
            playlist("P4", regra="materia=Física;trilha=Cinemática", materia="Física"),
        ]
        self.tem(self.erros(aulas, playlists), "ids diferentes")

    def test_duas_trilhas_da_mesma_trilha(self):
        aulas = [aula("A", camada="nivelamento"), aula("B", ordem="2")]
        p1 = playlist("P1", regra="materia=Matemática;trilha=Frações;camada=nivelamento")
        p2 = playlist("P3", regra="materia=Matemática;trilha=Frações;camada=nucleo")
        self.tem(self.erros(aulas, [p1, p2, MATERIA]), "mesma chave")

    def test_trilha_abrangendo_duas_trilhas(self):
        aulas = [aula("A"), aula("B", trilha="Decimais", modulo="Ler")]
        larga = playlist("P1", regra="materia=Matemática;trilha=Frações|Decimais")
        decimais = playlist("P3", regra="materia=Matemática;trilha=Decimais")
        self.tem(self.erros(aulas, [larga, decimais, MATERIA]), "ids diferentes")

    def test_duas_playlists_de_materia(self):
        outra = playlist("P3", "materia", MATERIA["regra"])
        self.tem(self.erros([aula("A")], [playlist(), MATERIA, outra]), "mesma chave")

    def test_nivelamento_sem_comece_aqui(self):
        aulas = [aula("A", camada="nivelamento"), aula("B", ordem="2")]
        self.tem(self.erros(aulas, [playlist(), MATERIA]), "falta")

    def test_comece_aqui_contendo_nucleo(self):
        aulas = [aula("A", camada="nivelamento"), aula("B", ordem="2")]
        comece = playlist("P3", "comece_aqui", "materia=Matemática;camada=nivelamento|nucleo")
        self.tem(self.erros(aulas, [playlist(), MATERIA, comece]), "ids diferentes")

    def test_comece_aqui_correto_passa(self):
        aulas = [aula("A", camada="nivelamento"), aula("B", ordem="2")]
        comece = playlist("P3", "comece_aqui", "materia=Matemática;camada=nivelamento")
        self.assertEqual(self.erros(aulas, [playlist(), MATERIA, comece]), [])

    def test_prova_sem_chave_prova_na_regra(self):
        sem = playlist("P3", "prova", "materia=Matemática;tipo=aula")
        erros = self.erros(aulas_de_prova(10), [playlist(), MATERIA, sem])
        self.tem(erros, "mínimo")
        self.tem(erros, "falta")

    def test_regra_de_prova_sem_materia(self):
        aulas = aulas_de_prova(10) + [
            aula("F1", materia="Física", trilha="Cinemática", modulo="MRU", provas="fuvest")
        ]
        sem = playlist("P3", "prova", "prova=fuvest;tipo=aula")
        playlists = [
            playlist(), MATERIA, sem,
            playlist("P4", regra="materia=Física;trilha=Cinemática", materia="Física"),
            playlist("P5", "materia", "materia=Física;camada=nivelamento|nucleo", materia="Física"),
        ]
        self.tem(self.erros(aulas, playlists), "ids diferentes")

    def test_dez_aulas_da_fuvest_sem_playlist_de_prova(self):
        self.tem(self.erros(aulas_de_prova(10), [playlist(), MATERIA]), "falta")

    def test_dez_aulas_com_playlist_de_prova_passa(self):
        self.assertEqual(
            self.erros(aulas_de_prova(10), [playlist(), MATERIA, playlist_prova()]), [])

    def test_nove_aulas_com_playlist_de_prova_e_erro(self):
        erros = self.erros(aulas_de_prova(9), [playlist(), MATERIA, playlist_prova()])
        self.tem(erros, "mínimo")

    def test_pratica_nao_conta_no_minimo(self):
        erros = self.erros(aulas_de_prova(9, praticas=1), [playlist(), MATERIA, playlist_prova()])
        self.tem(erros, "mínimo")

    def test_prova_sem_tipo_aula_na_regra_inclui_praticas(self):
        sem_tipo = playlist("P3", "prova", "materia=Matemática;prova=fuvest")
        erros = self.erros(aulas_de_prova(10, praticas=1), [playlist(), MATERIA, sem_tipo])
        self.tem(erros, "ids diferentes")

    def test_playlists_invalidas_sao_puladas(self):
        ruim = playlist("P3", "outro")
        sem_regra = playlist("P4", regra="serie=1")
        self.assertEqual(self.erros([aula("A")], [playlist(), MATERIA, ruim, sem_regra]), [])


class TestCamposPlaylists(unittest.TestCase):
    def test_id_repetido(self):
        cat = catalogo(playlists=[playlist("P1"), playlist("P1", titulo="Outro")])
        self.assertTrue(any("repetido" in e for e in val.checar_campos_playlists(cat)))

    def test_campo_vazio_em_qualquer_campo(self):
        for campo in lib.CAMPOS_PLAYLIST:
            linha = playlist("P1")
            linha[campo] = " "
            erros = val.checar_campos_playlists(catalogo(playlists=[linha]))
            self.assertTrue(any(f"campo vazio: {campo}" in e for e in erros), campo)

    def test_playlist_correta_passa(self):
        self.assertEqual(val.checar_campos_playlists(catalogo(playlists=[playlist()])), [])


class TestValidarChamaTudo(unittest.TestCase):
    def test_uma_falha_de_cada_familia(self):
        aulas = [
            aula("A", habilidade="", prereqs="Z"),
            aula("B", camada="nivelamento", ordem="2"),
        ]
        playlists = [
            playlist("P1", titulo="Igual", descricao=""),
            playlist("P2", "materia", MATERIA["regra"], titulo="Igual"),
        ]
        cat = catalogo(aulas, playlists, assuntos=[{"area": "Matemática", "assunto": "Frações"}])
        erros, _ = val.validar(cat)
        for trecho in (
            "A: campo vazio: habilidade",
            "P1: campo vazio: descricao",
            "pré-requisito inexistente: Z",
            "aula de Nivelamento",
            "não termina em prática",
            "cobertura: assunto ausente",
            "título repetido",
            "falta a playlist",
        ):
            self.assertTrue(any(trecho in e for e in erros), trecho)


class TestMain(unittest.TestCase):
    def rodar(self, cat):
        saida = io.StringIO()
        with mock.patch("catalogo_lib.carregar", return_value=cat), \
                mock.patch.object(sys, "argv", ["validar_catalogo.py"]), \
                contextlib.redirect_stdout(saida):
            codigo = val.main()
        return codigo, saida.getvalue()

    def test_devolve_1_com_erro(self):
        codigo, saida = self.rodar(catalogo([aula("A")]))
        self.assertEqual(codigo, 1)
        self.assertIn("ERRO", saida)

    def test_devolve_0_sem_erro(self):
        cat = catalogo([aula("A", ordem="1"), aula("B", tipo="pratica", ordem="2")], [playlist(), MATERIA])
        codigo, saida = self.rodar(cat)
        self.assertEqual(codigo, 0, saida)


class TestAvisos(unittest.TestCase):
    def test_titulo_com_e_gera_aviso_e_nao_erro(self):
        cat = catalogo([aula("A", titulo="Mediana e moda", ordem="1"), aula("B", tipo="pratica", ordem="2")],
                       [playlist(), MATERIA])
        erros, avisos = val.validar(cat)
        self.assertEqual(erros, [])
        self.assertEqual(len(avisos), 1)


class TestPlanilha(unittest.TestCase):
    def test_abas_e_ordem_das_playlists(self):
        cat = catalogo([aula("A"), aula("B", ordem="2")], [playlist()])
        with tempfile.TemporaryDirectory() as pasta:
            destino = Path(pasta) / "revisao.xlsx"
            pla.gerar(cat, destino, [])
            livro = openpyxl.load_workbook(destino)
            self.assertEqual(
                livro.sheetnames,
                ["Resumo", "Mapa geral", "Aulas", "Playlists", "Ordem das playlists", "Cobertura"],
            )
            ordem = livro["Ordem das playlists"]
            self.assertEqual(ordem.cell(3, 3).value, "B")
            self.assertEqual(ordem.cell(3, 2).value, 2)
            livro.close()


# ---------------------------------------------------------------- cenário completo

def _A(id, trilha, modulo, ordem, camada="nucleo", tipo="aula", prereqs="", provas="enem;fuvest",
       materia="Matemática"):
    return aula(id, titulo=f"Aula {id}", materia=materia, trilha=trilha, modulo=modulo,
                ordem=str(ordem), camada=camada, tipo=tipo, prereqs=prereqs, provas=provas)


def _P(id, titulo, tipo, regra):
    return playlist(id, tipo, regra, titulo=titulo)


def catalogo_completo():
    """Matemática inteira (nivelamento, núcleo, extensão, 3 trilhas, 2 provas) + cronograma real."""
    aulas = [
        _A("MAT-BAS-001", "Bases", "Tabuada", 1, "nivelamento", provas="enem"),
        _A("MAT-BAS-002", "Bases", "Tabuada", 2, "nivelamento", prereqs="MAT-BAS-001", provas="enem"),
        _A("MAT-BAS-003", "Bases", "Tabuada", 3, "nivelamento", "pratica", "MAT-BAS-002", provas="enem"),
        _A("MAT-FRA-001", "Frações", "Somar", 1, prereqs="MAT-BAS-002"),
    ]
    for i in range(2, 11):
        aulas.append(_A(f"MAT-FRA-{i:03}", "Frações", "Somar", i, prereqs=f"MAT-FRA-{i-1:03}"))
    aulas.append(_A("MAT-FRA-011", "Frações", "Somar", 11, tipo="pratica", prereqs="MAT-FRA-010"))
    aulas += [
        _A("MAT-CPX-001", "Complexos", "Intro", 1, "extensao", prereqs="MAT-FRA-010", provas="fuvest"),
        _A("MAT-CPX-002", "Complexos", "Intro", 2, "extensao", "pratica", "MAT-CPX-001", provas="fuvest"),
    ]
    playlists = [
        _P("T1", "Bases do Zero", "trilha", "materia=Matemática;trilha=Bases"),
        _P("T2", "Frações do Zero", "trilha", "materia=Matemática;trilha=Frações"),
        _P("T3", "Complexos", "trilha", "materia=Matemática;trilha=Complexos"),
        _P("M1", "Matemática do Zero", "materia", "materia=Matemática;camada=nivelamento|nucleo"),
        _P("C1", "Comece Aqui", "comece_aqui", "materia=Matemática;camada=nivelamento"),
        _P("PF", "Matemática para a Fuvest", "prova", "materia=Matemática;prova=fuvest;tipo=aula"),
        _P("PE", "Matemática para o ENEM", "prova", "materia=Matemática;prova=enem;tipo=aula"),
    ]
    cronograma = lib.ler_csv(lib.PASTA / "fontes" / "cronograma-enem.csv")
    assuntos = [{"area": l["Área"], "assunto": l["Assunto"]} for l in cronograma]
    cobertura = [
        {"area": a["area"], "assunto": a["assunto"],
         "aulas": "MAT-FRA-001" if a["area"] == "Matemática" else "", "justificativa": ""}
        for a in assuntos
    ]
    return lib.Catalogo(aulas, playlists, cobertura, assuntos)


def _saida_ascii():
    """stdout que quebra com acento se main() não o reconfigurar para utf-8."""
    return io.TextIOWrapper(io.BytesIO(), encoding="ascii", write_through=True)


def _texto(saida):
    return saida.buffer.getvalue().decode("utf-8")


def rodar_main(modulo, cat, argv=()):
    saida = _saida_ascii()
    with mock.patch("catalogo_lib.carregar", return_value=cat), \
            mock.patch.object(sys, "argv", ["x.py", *argv]), \
            contextlib.redirect_stdout(saida):
        codigo = modulo.main()
    return codigo, _texto(saida), saida


class TestCenarioCompleto(unittest.TestCase):
    def test_matematica_completa_da_zero_erros(self):
        erros, avisos = val.validar(catalogo_completo(), ["Matemática"])
        self.assertEqual(erros, [])
        self.assertEqual(avisos, [])

    def test_main_respeita_area(self):
        cat = catalogo_completo()
        codigo, saida, _ = rodar_main(val, cat, ["--area", "Matemática"])
        self.assertEqual(codigo, 0, saida)
        codigo, saida, _ = rodar_main(val, cat)
        self.assertEqual(codigo, 1)
        self.assertIn("cobertura: sem aula e sem justificativa", saida)

    def test_trilha_sem_playlist_gera_um_erro_so(self):
        cat = catalogo_completo()
        cat.playlists = [p for p in cat.playlists if p["id"] != "T2"]
        erros, _ = val.validar(cat, ["Matemática"])
        self.assertEqual(len(erros), 1, erros)
        tem(self, erros, "falta a playlist")

    def test_aula_em_duas_trilhas_e_detectada(self):
        cat = catalogo_completo()
        cat.playlists.append(_P("T9", "Outra de Frações", "trilha", "materia=Matemática;trilha=Frações"))
        erros, _ = val.validar(cat, ["Matemática"])
        tem(self, erros, "T2, T9: mesma chave")

    def test_aula_em_nenhuma_trilha_e_detectada(self):
        cat = catalogo_completo()
        cat.aulas[4]["trilha"] = "Fracoes"
        erros = val.checar_estrutura_playlists(cat)
        tem(self, erros, "falta a playlist ('trilha', 'Matemática', 'Fracoes')")


class TestAreaInvalida(unittest.TestCase):
    ASSUNTOS = [{"area": "Matemática", "assunto": "Frações"}, {"area": "Humanas", "assunto": "Vargas"}]

    def test_area_inexistente_gera_erro_com_as_validas(self):
        for area in ("Matematica", "Física"):
            erros = val.checar_cobertura(catalogo(assuntos=self.ASSUNTOS), [area])
            tem(self, erros, f"área inexistente: {area}")
            tem(self, erros, "['Humanas', 'Matemática']")

    def test_area_valida_junto_de_invalida_continua_checando(self):
        erros = val.checar_cobertura(catalogo(assuntos=self.ASSUNTOS), ["Matemática", "Nada"])
        tem(self, erros, "área inexistente: Nada")
        tem(self, erros, "assunto ausente: Matemática > Frações")

    def test_main_com_area_invalida_devolve_1(self):
        codigo, saida, _ = rodar_main(val, catalogo_completo(), ["--area", "Nenhuma"])
        self.assertEqual(codigo, 1)
        self.assertIn("área inexistente: Nenhuma", saida)


class TestFormatoCsv(unittest.TestCase):
    def escrever(self, pasta, nome, texto, encoding="utf-8"):
        caminho = Path(pasta) / nome
        caminho.write_bytes(texto.encode(encoding))
        return caminho

    def test_coluna_faltando(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = self.escrever(pasta, "aulas.csv", "a,c\n1,2\n")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.ler_csv(caminho, ("a", "b", "c"))
        self.assertTrue(str(ctx.exception).startswith("aulas.csv: faltam colunas ['b']"), ctx.exception)

    def test_separador_ponto_e_virgula(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = self.escrever(pasta, "aulas.csv", ";".join(lib.CAMPOS_AULA) + "\n" + "x;" * 12 + "x\n")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.ler_csv(caminho, lib.CAMPOS_AULA)
        self.assertIn("aulas.csv: faltam colunas", str(ctx.exception))
        self.assertIn("';'", str(ctx.exception))

    def test_arquivo_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = self.escrever(pasta, "aulas.csv", "")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.ler_csv(caminho, ("a",))
        self.assertIn("aulas.csv: faltam colunas ['a']", str(ctx.exception))

    def test_coluna_renomeada_em_carregar(self):
        with tempfile.TemporaryDirectory() as pasta:
            pasta = Path(pasta)
            (pasta / "fontes").mkdir()
            (pasta / "fontes" / "cronograma-enem.csv").write_text("Área,Assunto\nM,x\n", encoding="utf-8-sig")
            cabecalho = ",".join(lib.CAMPOS_AULA).replace("habilidade", "skill")
            (pasta / "aulas.csv").write_text(cabecalho + "\n", encoding="utf-8-sig")
            (pasta / "playlists.csv").write_text(",".join(lib.CAMPOS_PLAYLIST) + "\n", encoding="utf-8-sig")
            (pasta / "cobertura.csv").write_text("area,assunto,aulas,justificativa\n", encoding="utf-8-sig")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.carregar(pasta)
            self.assertIn("aulas.csv: faltam colunas ['habilidade']", str(ctx.exception))
            (pasta / "aulas.csv").write_text(",".join(lib.CAMPOS_AULA) + "\n", encoding="utf-8-sig")
            cat = lib.carregar(pasta)
            self.assertEqual(cat.assuntos, [{"area": "M", "assunto": "x"}])

    def test_cobertura_sem_coluna(self):
        with tempfile.TemporaryDirectory() as pasta:
            pasta = Path(pasta)
            (pasta / "fontes").mkdir()
            (pasta / "fontes" / "cronograma-enem.csv").write_text("Área,Assunto\nM,x\n", encoding="utf-8")
            (pasta / "aulas.csv").write_text(",".join(lib.CAMPOS_AULA) + "\n", encoding="utf-8")
            (pasta / "playlists.csv").write_text(",".join(lib.CAMPOS_PLAYLIST) + "\n", encoding="utf-8")
            (pasta / "cobertura.csv").write_text("area,assunto,aulas\n", encoding="utf-8")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.carregar(pasta)
            self.assertIn("cobertura.csv: faltam colunas ['justificativa']", str(ctx.exception))

    def test_cronograma_sem_coluna_assunto(self):
        with tempfile.TemporaryDirectory() as pasta:
            pasta = Path(pasta)
            (pasta / "fontes").mkdir()
            (pasta / "fontes" / "cronograma-enem.csv").write_text("Área,Tema\nM,x\n", encoding="utf-8")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.carregar(pasta)
            self.assertIn("cronograma-enem.csv: faltam colunas ['Assunto']", str(ctx.exception))

    def test_nao_utf8_cita_o_arquivo(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = self.escrever(pasta, "aulas.csv", "a\nação\n", encoding="cp1252")
            with self.assertRaises(lib.ErroDeFormato) as ctx:
                lib.ler_csv(caminho)
        self.assertIn("aulas.csv", str(ctx.exception))
        self.assertIn("UTF-8", str(ctx.exception))

    def test_bom_nao_vaza_para_o_nome_da_coluna(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = self.escrever(pasta, "x.csv", "﻿id,t\n1,2\n")
            linhas = lib.ler_csv(caminho, ("id", "t"))
        self.assertEqual(linhas, [{"id": "1", "t": "2", "_linha": 2}])

    def test_cabecalho_real_do_cronograma(self):
        linhas = lib.ler_csv(lib.PASTA / "fontes" / "cronograma-enem.csv", lib.COLUNAS_CRONOGRAMA)
        self.assertEqual(len(linhas), 559)

    def test_main_imprime_a_mensagem_e_devolve_1(self):
        saida = _saida_ascii()
        erro = lib.ErroDeFormato("aulas.csv: faltam colunas ['id']")
        with mock.patch("catalogo_lib.carregar", side_effect=erro), \
                mock.patch.object(sys, "argv", ["x.py"]), contextlib.redirect_stdout(saida):
            codigo = val.main()
        self.assertEqual(codigo, 1)
        self.assertIn("aulas.csv: faltam colunas ['id']", _texto(saida))


class TestLinhasDoCsv(unittest.TestCase):
    def ler(self, texto):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "x.csv"
            caminho.write_bytes(texto.encode("utf-8"))
            return lib.ler_csv(caminho)

    def test_numero_da_linha_do_arquivo(self):
        linhas = self.ler("a,b\n1,2\n3,4\n")
        self.assertEqual([l["_linha"] for l in linhas], [2, 3])

    def test_linhas_vazias_sao_ignoradas_sem_perder_a_numeracao(self):
        linhas = self.ler("a,b\n1,2\n\n,\n  , \n3,4\n")
        self.assertEqual([(l["a"], l["_linha"]) for l in linhas], [("1", 2), ("3", 6)])

    def test_campo_com_quebra_de_linha_conta_a_linha_inicial(self):
        linhas = self.ler('a,b\n"x\ny",2\n3,4\n')
        self.assertEqual([l["_linha"] for l in linhas], [2, 4])

    def test_valor_a_mais_vai_para_extra_e_virgula_final_nao(self):
        linhas = self.ler("a,b\n1,2,3,4\n5,6,\n")
        self.assertEqual(linhas[0]["_extra"], ["3", "4"])
        self.assertNotIn("_extra", linhas[1])
        self.assertNotIn(None, linhas[0])

    def test_id_vazio_usa_linha_na_mensagem(self):
        cat = catalogo([aula("", _linha=7)])
        tem(self, val.checar_campos(cat), "linha 7: campo vazio: id")
        cat = catalogo([aula("", _linha=7), aula("", ordem="2", _linha=8)])
        erros = val.checar_campos(cat)
        self.assertFalse(any("id repetido" in e for e in erros), erros)

    def test_linha_aparece_nas_outras_mensagens_de_aula(self):
        cat = catalogo([aula("", prereqs="Z", _linha=9)])
        tem(self, val.checar_prereqs(cat), "linha 9: pré-requisito inexistente: Z")

    def test_extra_vira_erro_em_aulas_playlists_e_cobertura(self):
        cat = catalogo(
            [aula("A", _linha=2, _extra=["z"])],
            [playlist("P1", _linha=5, _extra=["y"])],
            [{"area": "M", "assunto": "F", "aulas": "", "justificativa": "j", "_linha": 3, "_extra": ["w"]}],
            [{"area": "M", "assunto": "F"}],
        )
        tem(self, val.checar_campos(cat), "A: linha 2: colunas a mais")
        tem(self, val.checar_campos_playlists(cat), "P1: linha 5: colunas a mais")
        tem(self, val.checar_cobertura(cat), "cobertura: linha 3: colunas a mais")

    def test_linha_nao_vaza_para_a_planilha(self):
        cat = catalogo([aula("A", _linha=99, _extra=["z"])], [playlist(_linha=98)],
                       [{"area": "M", "assunto": "F", "aulas": "", "justificativa": "", "_linha": 97}])
        mapa = [{**{c: "x" for c in pla.CAMPOS_MAPA}, "_linha": 96}]
        with tempfile.TemporaryDirectory() as pasta:
            destino = Path(pasta) / "r.xlsx"
            pla.gerar(cat, destino, mapa)
            livro = openpyxl.load_workbook(destino)
            for aba in livro:
                valores = {c.value for linha in aba.iter_rows() for c in linha}
                self.assertFalse(valores & {99, 98, 97, 96, "_linha", "_extra", "z"}, aba.title)
            self.assertEqual(livro["Aulas"].max_column, len(lib.CAMPOS_AULA))
            self.assertEqual(livro["Mapa geral"].max_column, len(pla.CAMPOS_MAPA))
            livro.close()


class TestIdsDiferentes(unittest.TestCase):
    def test_mostra_so_faltam_e_sobram(self):
        self.assertEqual(val.descrever_diferenca(["A", "C"], ["A", "B"]), "faltam: ['B']; sobram: ['C']")

    def test_mesmos_ids_em_outra_ordem(self):
        self.assertEqual(val.descrever_diferenca(["B", "A"], ["A", "B"]), "ordem diferente")

    def test_mensagem_completa_traz_regra_e_nao_as_listas(self):
        aulas = [aula("A"), aula("B", camada="extensao", ordem="2")]
        larga = playlist("P2", "materia", "materia=Matemática")
        erros = val.checar_estrutura_playlists(catalogo(aulas, [playlist(), larga]))
        tem(self, erros, "P2: ids diferentes")
        tem(self, erros, "faltam: []; sobram: ['B']")
        tem(self, erros, "regra: materia=Matemática")
        self.assertFalse(any("esperado [" in e or "tem [" in e for e in erros), erros)


class TestOrdemDoModulo(unittest.TestCase):
    def test_ordem_reinicia_em_outro_modulo_da_mesma_materia(self):
        aulas = [
            aula("A", ordem="1"), aula("B", ordem="2"),
            aula("C", trilha="Frações", modulo="Subtrair", ordem="1"),
            aula("D", trilha="Decimais", modulo="Somar", ordem="1"),
            aula("E", materia="Física", trilha="Frações", modulo="Somar", ordem="1"),
        ]
        self.assertEqual(val.checar_campos(catalogo(aulas)), [])

    def test_ordem_repetida_no_mesmo_modulo_e_erro(self):
        erros = val.checar_campos(catalogo([aula("A", ordem="2"), aula("B", ordem="2")]))
        tem(self, erros, "B: ordem deve crescer dentro do módulo")


class TestRegrasDeCamadas(unittest.TestCase):
    def test_extensao_depender_de_extensao_passa(self):
        cat = catalogo([aula("A", camada="extensao"), aula("B", camada="extensao", prereqs="A", ordem="2")])
        self.assertEqual(val.checar_camadas(cat), [])

    def test_nivelamento_usado_so_por_pratica_do_nucleo_e_erro(self):
        cat = catalogo([
            aula("A", camada="nivelamento"),
            aula("B", tipo="pratica", prereqs="A", ordem="2"),
        ])
        tem(self, val.checar_camadas(cat), "A: aula de Nivelamento que não leva ao Núcleo")

    def test_nivelamento_usado_por_aula_do_nucleo_passa(self):
        cat = catalogo([aula("A", camada="nivelamento"), aula("B", prereqs="A", ordem="2")])
        self.assertEqual(val.checar_camadas(cat), [])


class TestProvas(unittest.TestCase):
    def test_prova_repetida_na_aula_e_erro(self):
        erros = val.checar_campos(catalogo([aula("A", provas="enem;fuvest;fuvest")]))
        tem(self, erros, "A: provas: valor repetido: fuvest")

    def test_prova_repetida_nao_conta_duas_vezes(self):
        aulas = aulas_de_prova(9)
        aulas[0]["provas"] = "fuvest;fuvest"
        self.assertNotIn(("prova", "Matemática", "fuvest"), val.playlists_esperadas(aulas))
        aulas = aulas_de_prova(10)
        aulas[0]["provas"] = "fuvest;fuvest"
        self.assertEqual(len(val.playlists_esperadas(aulas)[("prova", "Matemática", "fuvest")]), 10)

    def test_prova_invalida_nao_entra_em_playlists_esperadas(self):
        aulas = [aula(f"A{i}", ordem=str(i), provas="enem;ufpr") for i in range(1, 11)]
        chaves = val.playlists_esperadas(aulas)
        self.assertNotIn(("prova", "Matemática", "ufpr"), chaves)
        self.assertIn(("prova", "Matemática", "enem"), chaves)


class TestCoberturaDuplicada(unittest.TestCase):
    def test_linha_duplicada_e_erro(self):
        linha = {"area": "Matemática", "assunto": "Frações", "aulas": "", "justificativa": "x"}
        cat = catalogo(cobertura=[linha, dict(linha, aulas="Z")],
                       assuntos=[{"area": "Matemática", "assunto": "Frações"}])
        tem(self, val.checar_cobertura(cat), "cobertura: linha duplicada: Matemática > Frações")


class TestBomEmCsv(unittest.TestCase):
    def test_utf8_sig_le_a_primeira_coluna(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "aulas.csv"
            caminho.write_bytes(
                b"\xef\xbb\xbf" + ",".join(lib.CAMPOS_AULA).encode() + b"\n" + b"A" + b"," * 12 + b"\n")
            linhas = lib.ler_csv(caminho, lib.CAMPOS_AULA)
        self.assertEqual(linhas[0]["id"], "A")


class TestSaidaDoMain(unittest.TestCase):
    def test_aviso_e_impresso(self):
        cat = catalogo([aula("A", titulo="Mediana e moda", ordem="1"), aula("B", tipo="pratica", ordem="2")],
                       [playlist(), MATERIA])
        codigo, saida, _ = rodar_main(val, cat)
        self.assertEqual(codigo, 0, saida)
        self.assertIn("AVISO A: confira se é uma habilidade só: Mediana e moda", saida)
        self.assertIn("1 avisos", saida)

    def test_main_troca_stdout_para_utf8(self):
        _, saida, stream = rodar_main(val, catalogo([aula("A", titulo="Média")]))
        self.assertEqual(stream.encoding, "utf-8")
        self.assertIn("ERRO", saida)


class TestPlanilhaConteudo(unittest.TestCase):
    def gerar(self, cat, mapa=()):
        pasta = tempfile.TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        destino = Path(pasta.name) / "r.xlsx"
        pla.gerar(cat, destino, list(mapa))
        livro = openpyxl.load_workbook(destino)
        self.addCleanup(livro.close)
        return livro

    def test_abas_cobertura_e_resumo_tem_conteudo(self):
        cat = catalogo(
            [aula("A"), aula("B", ordem="2", camada="nivelamento")], [playlist()],
            [{"area": "Matemática", "assunto": "Frações", "aulas": "A", "justificativa": "j"}],
        )
        livro = self.gerar(cat)
        cob = livro["Cobertura"]
        self.assertEqual([c.value for c in cob[1]], ["Área", "Assunto", "Aulas", "Justificativa"])
        self.assertEqual([c.value for c in cob[2]], ["Matemática", "Frações", "A", "j"])
        resumo = {r[0].value: r[1].value for r in livro["Resumo"].iter_rows(min_row=2)}
        self.assertEqual(resumo["Aulas"], 2)
        self.assertEqual(resumo["Playlists"], 1)
        self.assertEqual(resumo["Aulas: nucleo"], 1)
        self.assertEqual(resumo["Aulas: nivelamento"], 1)
        self.assertEqual(resumo["Aulas: Matemática"], 2)
        self.assertEqual(resumo["Playlists: trilha"], 1)

    def test_texto_comecado_por_igual_fica_texto(self):
        cat = catalogo([aula("A", titulo="=1+1")], [playlist(titulo="=SOMA(A1)")])
        livro = self.gerar(cat)
        celula = livro["Aulas"].cell(2, 2)
        self.assertEqual((celula.value, celula.data_type), ("=1+1", "s"))
        celula = livro["Playlists"].cell(2, 2)
        self.assertEqual((celula.value, celula.data_type), ("=SOMA(A1)", "s"))
        celula = livro["Ordem das playlists"].cell(2, 1)
        self.assertEqual((celula.value, celula.data_type), ("=SOMA(A1)", "s"))

    def test_numeros_continuam_numeros(self):
        livro = self.gerar(catalogo([aula("A")], [playlist()]))
        self.assertEqual(livro["Resumo"].cell(2, 2).data_type, "n")

    def test_playlist_com_regra_invalida_fica_fora_da_ordem(self):
        sem_regra = playlist("P9", regra="")
        ruim = playlist("P8", regra="serie=1")
        livro = self.gerar(catalogo([aula("A")], [sem_regra, ruim, playlist()]))
        nomes = {r[0].value for r in livro["Ordem das playlists"].iter_rows(min_row=2)}
        self.assertEqual(nomes, {"Playlist P1"})

    def test_main_avisa_quando_o_catalogo_tem_erros(self):
        cat = catalogo([aula("A")])
        with tempfile.TemporaryDirectory() as pasta, \
                mock.patch("catalogo_lib.carregar", return_value=cat), \
                mock.patch("catalogo_lib.PASTA", Path(pasta)):
            saida = _saida_ascii()
            with contextlib.redirect_stdout(saida):
                pla.main()
            texto = _texto(saida)
            self.assertTrue((Path(pasta) / "revisao_catalogo.xlsx").exists())
        self.assertRegex(texto, r"ATENÇÃO: catálogo com \d+ erros")
        self.assertIn("revisao_catalogo.xlsx", texto)
        self.assertEqual(saida.encoding, "utf-8")

    def test_main_sem_erros_nao_avisa(self):
        cat = catalogo_completo()
        cat.assuntos = []
        cat.cobertura = []
        with tempfile.TemporaryDirectory() as pasta, \
                mock.patch("catalogo_lib.carregar", return_value=cat), \
                mock.patch("catalogo_lib.PASTA", Path(pasta)):
            saida = _saida_ascii()
            with contextlib.redirect_stdout(saida):
                pla.main()
        self.assertNotIn("ATENÇÃO", _texto(saida))


class TestPraticaConjunta(unittest.TestCase):
    @staticmethod
    def modulo(nome, n, pratica, inicio=1, trilha="Frações"):
        aulas = [
            aula(f"{trilha}-{nome}-{i}", modulo=nome, ordem=str(i), trilha=trilha)
            for i in range(inicio, inicio + n)
        ]
        if pratica:
            aulas.append(aula(f"{trilha}-{nome}-P", modulo=nome, ordem=str(inicio + n), tipo="pratica", trilha=trilha))
        return aulas

    def erros(self, *modulos):
        return val.checar_modulos(catalogo([a for m in modulos for a in m]))

    def test_constante(self):
        self.assertEqual(lib.MIN_AULAS_PRATICA_PROPRIA, 4)

    def test_modulo_pequeno_divide_com_o_seguinte(self):
        self.assertEqual(self.erros(self.modulo("A", 2, False), self.modulo("B", 2, True)), [])

    def test_modulo_grande_precisa_de_pratica_propria(self):
        erros = self.erros(self.modulo("A", 4, False), self.modulo("B", 2, True))
        tem(self, erros, "4 aulas ou mais")

    def test_modulo_com_3_aulas_pode_dividir(self):
        self.assertEqual(self.erros(self.modulo("A", 3, False), self.modulo("B", 5, True)), [])

    def test_dois_seguidos_sem_pratica(self):
        erros = self.erros(self.modulo("A", 2, False), self.modulo("B", 2, False), self.modulo("C", 2, True))
        tem(self, erros, "módulo seguinte também não")

    def test_ultimo_da_trilha_precisa_de_pratica(self):
        erros = self.erros(self.modulo("A", 2, True), self.modulo("B", 2, False))
        tem(self, erros, "último módulo da trilha")

    def test_modulo_seguinte_de_outra_trilha_nao_vale(self):
        erros = self.erros(self.modulo("A", 2, False), self.modulo("B", 2, True, trilha="Outra"))
        tem(self, erros, "último módulo da trilha")

    def test_pratica_conjunta_nao_cruza_camadas(self):
        pequeno = [aula("A", modulo="A", ordem="1", camada="nucleo")]
        seguinte = [
            aula("B", modulo="B", ordem="1", camada="extensao"),
            aula("C", modulo="B", ordem="2", camada="extensao", tipo="pratica"),
        ]
        tem(self, self.erros(pequeno, seguinte), "camada diferente")

    def test_pratica_no_meio_do_modulo(self):
        aulas = [aula("A", ordem="1"), aula("B", tipo="pratica", ordem="2"), aula("C", ordem="3"),
                 aula("D", tipo="pratica", ordem="4")]
        tem(self, val.checar_modulos(catalogo(aulas)), "prática fora do fim")


class TestOrcamento(unittest.TestCase):
    MAPA = [
        {"materia": "Matemática", "trilha": "Frações", "aulas_estimadas": "6"},
        {"materia": "Matemática", "trilha": "Frações", "aulas_estimadas": "4"},
    ]

    def aulas(self, n):
        return [aula(f"A{i}", ordem=str(i)) for i in range(1, n + 1)]

    def test_constante(self):
        self.assertEqual(lib.MAX_EXCESSO_TRILHA, 1.4)

    def test_no_teto_passa(self):
        self.assertEqual(val.checar_orcamento(self.aulas(14), self.MAPA), [])

    def test_acima_do_teto(self):
        tem(self, val.checar_orcamento(self.aulas(15), self.MAPA), "teto de 14")

    def test_trilha_fora_do_mapa(self):
        tem(self, val.checar_orcamento([aula("A", trilha="Nova")], self.MAPA), "fora do mapa")

    def test_validar_aplica_o_orcamento(self):
        cat = catalogo(self.aulas(15))
        cat.mapa = self.MAPA
        erros, _ = val.validar(cat)
        tem(self, erros, "teto de 14")


class TestPlaylistEspecial(unittest.TestCase):
    ESPECIAL = {
        "id": "PL-X", "titulo": "Somar do Zero", "tipo": "especial", "materia": "Matemática",
        "regra": "materia=Matemática;modulo=Somar", "descricao": "d", "termo_busca": "t",
    }

    def test_especial_nao_e_esperada_e_passa(self):
        cat = catalogo([aula("A")], [playlist(), MATERIA, self.ESPECIAL])
        self.assertEqual(val.checar_playlists(cat) + val.checar_estrutura_playlists(cat), [])

    def test_especial_filtra_por_modulo(self):
        aulas = [aula("A"), aula("B", modulo="Outro")]
        self.assertEqual([a["id"] for a in lib.aulas_da_playlist(self.ESPECIAL, aulas)], ["A"])

    def test_especial_vazia_e_erro(self):
        vazia = dict(self.ESPECIAL, regra="materia=Matemática;modulo=Nada")
        tem(self, val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, vazia])), "vazia")


if __name__ == "__main__":
    unittest.main()
