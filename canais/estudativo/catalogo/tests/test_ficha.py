import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import catalogo_lib as lib
import ficha_aula as fi


def aula(id, prereqs="", **campos):
    base = dict(id=id, titulo=f"Aula {id}", materia="Matemática", trilha="Frações", modulo="Somar", ordem="1",
                habilidade="Ao final, você consegue", camada="nucleo", tipo="aula", prereqs=prereqs, provas="enem",
                prioridade="1", termo_busca="busca")
    base.update(campos)
    return base


def catalogo():
    aulas = [aula("A"), aula("B", "A"), aula("C", "B"), aula("X", trilha="Outra"), aula("D", "C;X")]
    playlists = [dict(id="P", titulo="Frações", tipo="trilha", materia="Matemática", regra="materia=Matemática;trilha=Frações")]
    return lib.Catalogo(aulas=aulas, playlists=playlists, cobertura=[], assuntos=[])


class Ficha(unittest.TestCase):
    def test_cadeia_inclui_indiretos_na_ordem_do_curso(self):
        f = fi.montar_ficha(catalogo(), "D")
        self.assertEqual([a["id"] for a in f["cadeia"]], ["A", "B", "C", "X"])
        self.assertEqual([a["id"] for a in f["diretos"]], ["C", "X"])

    def test_vizinhas_ficam_na_mesma_trilha(self):
        f = fi.montar_ficha(catalogo(), "C")
        self.assertEqual(f["anterior"]["id"], "B")
        self.assertEqual(f["proxima"]["id"], "D")

    def test_ponta_da_trilha_nao_tem_vizinha(self):
        self.assertIsNone(fi.montar_ficha(catalogo(), "A")["anterior"])
        self.assertIsNone(fi.montar_ficha(catalogo(), "D")["proxima"])

    def test_playlist_traz_a_posicao(self):
        self.assertEqual(fi.montar_ficha(catalogo(), "C")["playlists"], [dict(titulo="Frações", tipo="trilha", posicao=3, total=4)])

    def test_id_desconhecido_avisa(self):
        with self.assertRaises(KeyError):
            fi.montar_ficha(catalogo(), "Z")

    def test_texto_mostra_situacao_do_prerequisito(self):
        texto = fi.texto_ficha(fi.montar_ficha(catalogo(), "C", {"B": "publicado"}))
        self.assertIn("B [publicado]", texto)
        self.assertIn("D [não gravada]", texto)

    def test_ficha_da_aula_real(self):
        f = fi.montar_ficha(lib.carregar(), "MAT-FRA-008")
        self.assertEqual(f["proxima"]["id"], "MAT-FRA-009")
        self.assertIn("MAT-DIV-005", [a["id"] for a in f["cadeia"]])


class Producao(unittest.TestCase):
    def test_marca_e_atualiza(self):
        with tempfile.TemporaryDirectory() as pasta:
            arq = Path(pasta) / "producao.csv"
            self.assertEqual(fi.ler_producao(arq), {})
            fi.marcar("A", "roteiro", arq, "2026-11-05")
            fi.marcar("B", "voz", arq, "2026-11-05")
            fi.marcar("A", "pronto", arq, "2026-11-06")
            self.assertEqual(fi.ler_producao(arq), {"A": "pronto", "B": "voz"})

    def test_estado_invalido(self):
        with tempfile.TemporaryDirectory() as pasta:
            with self.assertRaises(ValueError):
                fi.marcar("A", "feito", Path(pasta) / "p.csv")


if __name__ == "__main__":
    unittest.main()
