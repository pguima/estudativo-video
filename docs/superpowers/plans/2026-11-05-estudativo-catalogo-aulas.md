# Estudativo: catálogo de aulas e playlists (Etapa 1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Montar o catálogo de aulas e playlists do novo Estudativo, validado por script, em três entregas com aprovação do usuário entre elas.

**Architecture:** `aulas.csv` é a fonte única; a ordem das linhas é a ordem do curso. `playlists.csv` define filtros, e a lista de aulas de cada playlist é derivada deles. Uma biblioteca lê os dados, `validar_catalogo.py` aplica as regras da spec e `gerar_planilha.py` produz o `.xlsx` de revisão.

**Tech Stack:** Python 3.14 (comando `py` no Windows; `python` não está no PATH do Git Bash), biblioteca padrão com `unittest` (pytest não está instalado), `openpyxl` para a planilha.

**Spec:** `docs/superpowers/specs/2026-11-05-estudativo-catalogo-aulas-design.md`

**Commits:** nenhuma tarefa faz commit. O usuário não pediu, e o repositório tem alterações alheias pendentes (`.gitignore`, `canais/survive_the_headline/`). Se pedir, adicionar apenas `docs/` e `canais/estudativo/`.

**Portões de aprovação:** as Tasks 7, 8 e 9 terminam parando para o usuário revisar. Não avançar sem a aprovação.

---

## Estrutura de arquivos

Todos os caminhos partem de `canais/estudativo/catalogo/`:

| Arquivo | Responsabilidade |
|---|---|
| `catalogo_lib.py` | Constantes, leitura dos CSV, filtro de playlists |
| `validar_catalogo.py` | Regras de validação e linha de comando |
| `gerar_planilha.py` | Planilha de revisão |
| `iniciar_cobertura.py` | Cria a `cobertura.csv` com os 559 assuntos (uso único) |
| `aulas.csv`, `playlists.csv`, `cobertura.csv` | Dados do catálogo |
| `mapa_geral.csv` | Matérias, trilhas e módulos da Entrega 1 |
| `fontes/cronograma-enem.csv` | Cópia do cronograma |
| `fontes/provas.md`, `fontes/pesos_enem.md` | Pesquisa do que cai e do peso dos temas |
| `fontes/playlists_planejadas.csv` | Playlists de matérias que ainda não têm aulas |
| `tests/test_catalogo.py` | Testes |
| `revisao_catalogo.xlsx` | Planilha gerada |

Formato dos CSV: UTF-8 com BOM, separador vírgula. Listas dentro de um campo usam `;`.

Aula: `id,titulo,materia,trilha,modulo,ordem,habilidade,camada,tipo,prereqs,provas,prioridade,termo_busca`
Playlist: `id,titulo,tipo,materia,regra,descricao,termo_busca`
Cobertura: `area,assunto,aulas,justificativa`
Mapa: `materia,trilha,modulo,camada,aulas_estimadas,provas,observacao`

A regra da playlist usa `chave=valor`, com `;` entre filtros e `|` entre valores. Chaves: `materia`, `trilha`, `camada`, `prova`, `tipo`. Exemplos:

- Trilha: `materia=Matemática;trilha=Frações`
- Matéria: `materia=Matemática;camada=nivelamento|nucleo`
- Comece Aqui: `materia=Matemática;camada=nivelamento`
- Prova: `materia=Matemática;prova=fuvest;tipo=aula`

---

### Task 1: Biblioteca do catálogo

**Files:**
- Create: `canais/estudativo/catalogo/catalogo_lib.py`
- Create: `canais/estudativo/catalogo/aulas.csv`, `playlists.csv`, `cobertura.csv`
- Create: `canais/estudativo/catalogo/fontes/cronograma-enem.csv` (cópia)
- Test: `canais/estudativo/catalogo/tests/test_catalogo.py`

- [ ] **Step 1: Criar pastas, cópia do cronograma e CSVs só com cabeçalho**

```bash
cd /c/Users/Paulo/Documents/Claude/videos_canal/canais
mkdir -p estudativo/catalogo/fontes estudativo/catalogo/tests
cp /c/Users/Paulo/Documents/Claude/Projetos/Estudos/Enem/cronograma-enem.csv estudativo/catalogo/fontes/
cd estudativo/catalogo
printf '\xef\xbb\xbfid,titulo,materia,trilha,modulo,ordem,habilidade,camada,tipo,prereqs,provas,prioridade,termo_busca\n' > aulas.csv
printf '\xef\xbb\xbfid,titulo,tipo,materia,regra,descricao,termo_busca\n' > playlists.csv
printf '\xef\xbb\xbfarea,assunto,aulas,justificativa\n' > cobertura.csv
```

- [ ] **Step 2: Escrever o teste que falha**

`tests/test_catalogo.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import catalogo_lib as lib


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

    def test_carregar_le_os_559_assuntos(self):
        cat = lib.carregar()
        self.assertEqual(len(cat.assuntos), 559)
        self.assertEqual(cat.assuntos[0]["area"], "Matemática")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Rodar e confirmar a falha**

Run: `cd /c/Users/Paulo/Documents/Claude/videos_canal/canais/estudativo/catalogo && py -m unittest discover -s tests`
Expected: FAIL com `ModuleNotFoundError: No module named 'catalogo_lib'`

- [ ] **Step 4: Implementar `catalogo_lib.py`**

```python
"""Leitura do catálogo do Estudativo e resolução das playlists."""
import csv
from dataclasses import dataclass
from pathlib import Path

PASTA = Path(__file__).resolve().parent

CAMPOS_AULA = (
    "id", "titulo", "materia", "trilha", "modulo", "ordem", "habilidade",
    "camada", "tipo", "prereqs", "provas", "prioridade", "termo_busca",
)
CAMPOS_PLAYLIST = ("id", "titulo", "tipo", "materia", "regra", "descricao", "termo_busca")
PROVAS = ("enem", "fuvest", "unicamp", "unesp", "uerj")
CAMADAS = ("nivelamento", "nucleo", "extensao")
TIPOS_AULA = ("aula", "pratica")
PRIORIDADES = ("1", "2", "3")
TIPOS_PLAYLIST = ("trilha", "materia", "comece_aqui", "prova")
CHAVES_REGRA = ("materia", "trilha", "camada", "prova")
MIN_AULAS_PROVA = 10


@dataclass
class Catalogo:
    aulas: list
    playlists: list
    cobertura: list
    assuntos: list


def lista(texto):
    return [parte.strip() for parte in texto.split(";") if parte.strip()]


def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def carregar(pasta=PASTA):
    pasta = Path(pasta)
    cronograma = ler_csv(pasta / "fontes" / "cronograma-enem.csv")
    return Catalogo(
        aulas=ler_csv(pasta / "aulas.csv"),
        playlists=ler_csv(pasta / "playlists.csv"),
        cobertura=ler_csv(pasta / "cobertura.csv"),
        assuntos=[{"area": l["Área"], "assunto": l["Assunto"]} for l in cronograma],
    )


def parsear_regra(regra):
    filtros = {}
    for parte in lista(regra):
        chave, _, valor = parte.partition("=")
        filtros[chave.strip()] = [v.strip() for v in valor.split("|") if v.strip()]
    return filtros


def aulas_da_playlist(playlist, aulas):
    filtros = parsear_regra(playlist["regra"])

    def entra(aula):
        for chave, valores in filtros.items():
            if chave == "prova":
                if not set(valores) & set(lista(aula["provas"])):
                    return False
            elif aula.get(chave) not in valores:
                return False
        return True

    return [aula for aula in aulas if entra(aula)]
```

- [ ] **Step 5: Rodar e confirmar que passa**

Run: `py -m unittest discover -s tests`
Expected: `Ran 5 tests` e `OK`

---

### Task 2: Validar campos e pré-requisitos

**Files:**
- Create: `canais/estudativo/catalogo/validar_catalogo.py`
- Modify: `canais/estudativo/catalogo/tests/test_catalogo.py`

- [ ] **Step 1: Acrescentar os testes que falham**

Em `tests/test_catalogo.py`, depois de `import catalogo_lib as lib`, acrescentar `import validar_catalogo as val`. Antes de `if __name__`, acrescentar:

```python
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


class TestPrereqs(unittest.TestCase):
    def test_prereq_inexistente(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="Z")]))
        self.assertTrue(any("inexistente" in e for e in erros))

    def test_prereq_depois_da_aula(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="B"), aula("B")]))
        self.assertTrue(any("depois" in e for e in erros))

    def test_circulo_e_detectado(self):
        erros = val.checar_prereqs(catalogo([aula("A", prereqs="B"), aula("B", prereqs="A")]))
        self.assertTrue(erros)

    def test_aula_nao_depende_de_si_mesma(self):
        self.assertTrue(val.checar_prereqs(catalogo([aula("A", prereqs="A")])))

    def test_ordem_correta_passa(self):
        self.assertEqual(val.checar_prereqs(catalogo([aula("A"), aula("B", prereqs="A")])), [])
```

- [ ] **Step 2: Rodar e confirmar a falha**

Run: `py -m unittest discover -s tests`
Expected: FAIL com `ModuleNotFoundError: No module named 'validar_catalogo'`

- [ ] **Step 3: Implementar a primeira parte de `validar_catalogo.py`**

```python
"""Valida o catálogo do Estudativo. Sai com código 1 se houver erro."""
import argparse
import sys

import catalogo_lib as lib


def checar_campos(cat):
    erros = []
    vistos = set()
    ultima_ordem = {}
    for aula in cat.aulas:
        aid = aula["id"]
        if aid in vistos:
            erros.append(f"id repetido: {aid}")
        vistos.add(aid)
        for campo in lib.CAMPOS_AULA:
            if campo != "prereqs" and not (aula.get(campo) or "").strip():
                erros.append(f"{aid}: campo vazio: {campo}")
        if aula["camada"] not in lib.CAMADAS:
            erros.append(f"{aid}: camada inválida: {aula['camada']}")
        if aula["tipo"] not in lib.TIPOS_AULA:
            erros.append(f"{aid}: tipo inválido: {aula['tipo']}")
        if aula["prioridade"] not in lib.PRIORIDADES:
            erros.append(f"{aid}: prioridade inválida: {aula['prioridade']}")
        for prova in lib.lista(aula["provas"]):
            if prova not in lib.PROVAS:
                erros.append(f"{aid}: provas: valor inválido: {prova}")
        modulo = (aula["materia"], aula["trilha"], aula["modulo"])
        try:
            ordem = int(aula["ordem"])
        except ValueError:
            erros.append(f"{aid}: ordem não numérica: {aula['ordem']}")
            continue
        if modulo in ultima_ordem and ordem <= ultima_ordem[modulo]:
            erros.append(f"{aid}: ordem deve crescer dentro do módulo")
        ultima_ordem[modulo] = ordem
    return erros


def checar_prereqs(cat):
    erros = []
    posicao = {aula["id"]: i for i, aula in enumerate(cat.aulas)}
    for i, aula in enumerate(cat.aulas):
        for prereq in lib.lista(aula["prereqs"]):
            if prereq not in posicao:
                erros.append(f"{aula['id']}: pré-requisito inexistente: {prereq}")
            elif posicao[prereq] >= i:
                erros.append(f"{aula['id']}: pré-requisito vem depois ou forma círculo: {prereq}")
    return erros
```

Exigir que todo pré-requisito venha antes na ordem do curso já impede círculos, porque em um círculo ao menos uma aula aponta para frente.

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `py -m unittest discover -s tests`
Expected: `Ran 15 tests` e `OK`

---

### Task 3: Validar camadas, módulos e cobertura

**Files:**
- Modify: `canais/estudativo/catalogo/validar_catalogo.py`
- Modify: `canais/estudativo/catalogo/tests/test_catalogo.py`

- [ ] **Step 1: Acrescentar os testes que falham**

Antes de `if __name__`:

```python
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


class TestModulos(unittest.TestCase):
    def test_modulo_sem_pratica(self):
        self.assertTrue(val.checar_modulos(catalogo([aula("A")])))

    def test_pratica_deve_ser_a_ultima(self):
        cat = catalogo([aula("A", tipo="pratica", ordem="1"), aula("B", ordem="2")])
        self.assertTrue(val.checar_modulos(cat))

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
```

- [ ] **Step 2: Rodar e confirmar a falha**

Run: `py -m unittest discover -s tests`
Expected: FAIL com `AttributeError: ... has no attribute 'checar_camadas'`

- [ ] **Step 3: Acrescentar a `validar_catalogo.py`**

```python
def checar_camadas(cat):
    erros = []
    por_id = {aula["id"]: aula for aula in cat.aulas}
    usadas = set()
    for aula in cat.aulas:
        for prereq in lib.lista(aula["prereqs"]):
            usadas.add(prereq)
            alvo = por_id.get(prereq)
            if alvo and alvo["camada"] == "extensao" and aula["camada"] != "extensao":
                erros.append(f"{aula['id']}: depende da Extensão: {prereq}")
    for aula in cat.aulas:
        if aula["camada"] == "nivelamento" and aula["id"] not in usadas:
            erros.append(f"{aula['id']}: aula de Nivelamento sem dependente")
    return erros


def checar_modulos(cat):
    modulos = {}
    for aula in cat.aulas:
        chave = (aula["materia"], aula["trilha"], aula["modulo"])
        modulos.setdefault(chave, []).append(aula)
    erros = []
    for (materia, trilha, modulo), aulas in modulos.items():
        if aulas[-1]["tipo"] != "pratica":
            erros.append(f"{materia} > {trilha} > {modulo}: não termina em prática")
    return erros


def checar_cobertura(cat, areas=None):
    erros = []
    ids = {aula["id"] for aula in cat.aulas}
    no_cronograma = {(a["area"], a["assunto"]) for a in cat.assuntos}
    linhas = {(c["area"], c["assunto"]): c for c in cat.cobertura}
    for area, assunto in sorted(no_cronograma):
        if areas and area not in areas:
            continue
        linha = linhas.get((area, assunto))
        if linha is None:
            erros.append(f"cobertura: assunto ausente: {area} > {assunto}")
            continue
        aulas = lib.lista(linha["aulas"])
        if not aulas and not linha["justificativa"].strip():
            erros.append(f"cobertura: sem aula e sem justificativa: {area} > {assunto}")
        for aid in aulas:
            if aid not in ids:
                erros.append(f"cobertura: aula inexistente: {assunto} > {aid}")
    for chave in linhas:
        if chave not in no_cronograma:
            erros.append(f"cobertura: assunto fora do cronograma: {chave[0]} > {chave[1]}")
    return erros
```

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `py -m unittest discover -s tests`
Expected: `Ran 27 tests` e `OK`

---

### Task 4: Validar playlists e criar a linha de comando

**Files:**
- Modify: `canais/estudativo/catalogo/validar_catalogo.py`
- Modify: `canais/estudativo/catalogo/tests/test_catalogo.py`

- [ ] **Step 1: Acrescentar os testes que falham**

Antes de `if __name__`:

```python
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

    def test_aula_sem_trilha(self):
        self.assertTrue(val.checar_playlists(catalogo([aula("A")], [MATERIA])))

    def test_aula_em_duas_trilhas(self):
        dupla = playlist("P3")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), dupla, MATERIA]))
        self.assertTrue(any("Trilha" in e for e in erros))

    def test_aula_fora_da_materia(self):
        self.assertTrue(val.checar_playlists(catalogo([aula("A")], [playlist()])))

    def test_extensao_nao_precisa_da_materia(self):
        cat = catalogo([aula("A", camada="extensao")], [playlist()])
        self.assertEqual(val.checar_playlists(cat), [])

    def test_prova_exige_minimo_de_aulas(self):
        prova = playlist("P3", "prova", "materia=Matemática;prova=enem")
        erros = val.checar_playlists(catalogo([aula("A")], [playlist(), MATERIA, prova]))
        self.assertTrue(any("mínimo" in e for e in erros))

    def test_titulo_repetido(self):
        p1 = playlist("P1", titulo="Igual")
        p2 = playlist("P2", "materia", MATERIA["regra"], titulo="Igual")
        erros = val.checar_playlists(catalogo([aula("A")], [p1, p2]))
        self.assertTrue(any("título repetido" in e for e in erros))


class TestAvisos(unittest.TestCase):
    def test_titulo_com_e_gera_aviso_e_nao_erro(self):
        cat = catalogo([aula("A", titulo="Mediana e moda", ordem="1"), aula("B", tipo="pratica", ordem="2")],
                       [playlist(), MATERIA])
        erros, avisos = val.validar(cat)
        self.assertEqual(erros, [])
        self.assertEqual(len(avisos), 1)
```

- [ ] **Step 2: Rodar e confirmar a falha**

Run: `py -m unittest discover -s tests`
Expected: FAIL com `AttributeError: ... has no attribute 'checar_playlists'`

- [ ] **Step 3: Acrescentar a `validar_catalogo.py`**

```python
def checar_playlists(cat):
    erros = []
    titulos = set()
    trilhas_por_aula = {aula["id"]: 0 for aula in cat.aulas}
    em_playlist_de_materia = set()
    for playlist in cat.playlists:
        pid = playlist["id"]
        if playlist["titulo"] in titulos:
            erros.append(f"{pid}: título repetido: {playlist['titulo']}")
        titulos.add(playlist["titulo"])
        if playlist["tipo"] not in lib.TIPOS_PLAYLIST:
            erros.append(f"{pid}: tipo inválido: {playlist['tipo']}")
        filtros = lib.parsear_regra(playlist["regra"])
        desconhecidas = set(filtros) - set(lib.CHAVES_REGRA)
        if not filtros or desconhecidas:
            erros.append(f"{pid}: regra inválida: {playlist['regra']}")
            continue
        aulas = lib.aulas_da_playlist(playlist, cat.aulas)
        if not aulas:
            erros.append(f"{pid}: playlist vazia")
        for aula in aulas:
            if playlist["tipo"] == "trilha":
                trilhas_por_aula[aula["id"]] += 1
            elif playlist["tipo"] == "materia":
                em_playlist_de_materia.add(aula["id"])
        if playlist["tipo"] == "prova" and len(aulas) < lib.MIN_AULAS_PROVA:
            erros.append(f"{pid}: abaixo do mínimo de {lib.MIN_AULAS_PROVA} aulas")
    for aula in cat.aulas:
        aid = aula["id"]
        if trilhas_por_aula[aid] != 1:
            erros.append(f"{aid}: está em {trilhas_por_aula[aid]} playlists de Trilha")
        if aula["camada"] != "extensao" and aid not in em_playlist_de_materia:
            erros.append(f"{aid}: fora da playlist da sua Matéria")
    return erros


def avisos_de_titulo(cat):
    return [
        f"{aula['id']}: confira se é uma habilidade só: {aula['titulo']}"
        for aula in cat.aulas
        if " e " in aula["titulo"]
    ]


def validar(cat, areas=None):
    erros = (
        checar_campos(cat) + checar_prereqs(cat) + checar_camadas(cat)
        + checar_modulos(cat) + checar_cobertura(cat, areas) + checar_playlists(cat)
    )
    return erros, avisos_de_titulo(cat)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--area", action="append", help="limita a cobertura a esta área do cronograma")
    args = parser.parse_args()
    cat = lib.carregar()
    erros, avisos = validar(cat, args.area)
    for aviso in avisos:
        print(f"AVISO {aviso}")
    for erro in erros:
        print(f"ERRO  {erro}")
    print(f"{len(cat.aulas)} aulas, {len(cat.playlists)} playlists, {len(erros)} erros, {len(avisos)} avisos")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `py -m unittest discover -s tests`
Expected: `Ran 39 tests` e `OK`

---

### Task 5: Cobertura inicial e planilha de revisão

**Files:**
- Create: `canais/estudativo/catalogo/iniciar_cobertura.py`
- Create: `canais/estudativo/catalogo/gerar_planilha.py`
- Modify: `canais/estudativo/catalogo/tests/test_catalogo.py`

- [ ] **Step 1: Criar e rodar `iniciar_cobertura.py`**

```python
"""Uso único: cria cobertura.csv com todos os assuntos do cronograma."""
import csv

import catalogo_lib as lib

cat = lib.carregar()
if cat.cobertura:
    raise SystemExit("cobertura.csv já tem dados; nada foi alterado.")
with open(lib.PASTA / "cobertura.csv", "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["area", "assunto", "aulas", "justificativa"])
    for item in cat.assuntos:
        escritor.writerow([item["area"], item["assunto"], "", ""])
print(f"{len(cat.assuntos)} assuntos gravados.")
```

Run: `py iniciar_cobertura.py`
Expected: `559 assuntos gravados.`

- [ ] **Step 2: Instalar o openpyxl, se faltar**

Run: `py -c "import openpyxl" || py -m pip install openpyxl`
Expected: sem erro

- [ ] **Step 3: Acrescentar o teste que falha**

Depois de `import validar_catalogo as val`, acrescentar `import tempfile`, `import openpyxl` e `import gerar_planilha as pla`. Antes de `if __name__`:

```python
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
```

- [ ] **Step 4: Rodar e confirmar a falha**

Run: `py -m unittest discover -s tests`
Expected: FAIL com `ModuleNotFoundError: No module named 'gerar_planilha'`

- [ ] **Step 5: Implementar `gerar_planilha.py`**

```python
"""Gera a planilha de revisão do catálogo do Estudativo."""
from collections import Counter

from openpyxl import Workbook
from openpyxl.styles import Font

import catalogo_lib as lib

CAMPOS_MAPA = ("materia", "trilha", "modulo", "camada", "aulas_estimadas", "provas", "observacao")


def _aba(livro, titulo, cabecalho, linhas):
    aba = livro.create_sheet(titulo)
    aba.append(list(cabecalho))
    for celula in aba[1]:
        celula.font = Font(bold=True)
    for linha in linhas:
        aba.append(list(linha))
    aba.freeze_panes = "A2"
    return aba


def _resumo(cat):
    linhas = [("Aulas", len(cat.aulas)), ("Playlists", len(cat.playlists))]
    for camada, total in sorted(Counter(a["camada"] for a in cat.aulas).items()):
        linhas.append((f"Aulas: {camada}", total))
    for materia, total in sorted(Counter(a["materia"] for a in cat.aulas).items()):
        linhas.append((f"Aulas: {materia}", total))
    for tipo, total in sorted(Counter(p["tipo"] for p in cat.playlists).items()):
        linhas.append((f"Playlists: {tipo}", total))
    return linhas


def _ordem_das_playlists(cat):
    for playlist in cat.playlists:
        for posicao, aula in enumerate(lib.aulas_da_playlist(playlist, cat.aulas), 1):
            yield playlist["titulo"], posicao, aula["id"], aula["titulo"]


def gerar(cat, destino, mapa):
    livro = Workbook()
    livro.remove(livro.active)
    _aba(livro, "Resumo", ("Item", "Total"), _resumo(cat))
    _aba(livro, "Mapa geral", CAMPOS_MAPA, ([m[c] for c in CAMPOS_MAPA] for m in mapa))
    _aba(livro, "Aulas", lib.CAMPOS_AULA, ([a[c] for c in lib.CAMPOS_AULA] for a in cat.aulas))
    _aba(livro, "Playlists", lib.CAMPOS_PLAYLIST, ([p[c] for c in lib.CAMPOS_PLAYLIST] for p in cat.playlists))
    _aba(livro, "Ordem das playlists", ("Playlist", "Posição", "ID", "Aula"), _ordem_das_playlists(cat))
    _aba(
        livro, "Cobertura", ("Área", "Assunto", "Aulas", "Justificativa"),
        ((c["area"], c["assunto"], c["aulas"], c["justificativa"]) for c in cat.cobertura),
    )
    livro.save(destino)


def main():
    arquivo_mapa = lib.PASTA / "mapa_geral.csv"
    mapa = lib.ler_csv(arquivo_mapa) if arquivo_mapa.exists() else []
    destino = lib.PASTA / "revisao_catalogo.xlsx"
    gerar(lib.carregar(), destino, mapa)
    print(destino)


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Rodar e confirmar que passa**

Run: `py -m unittest discover -s tests`
Expected: `Ran 40 tests` e `OK`

Run: `py validar_catalogo.py --area Nenhuma`
Expected: `0 aulas, 0 playlists, 0 erros, 0 avisos`

---

### Task 6: Levantar o que cai em cada prova

**Files:**
- Create: `canais/estudativo/catalogo/fontes/provas.md`
- Create: `canais/estudativo/catalogo/fontes/pesos_enem.md`

- [ ] **Step 1: Baixar as fontes oficiais em pasta própria**

Baixar para o scratchpad da sessão, cada arquivo em pasta nova, e não para o repositório (`*.pdf` está no `.gitignore`). Ponto de partida do ENEM: `https://download.inep.gov.br/download/enem/matriz_referencia.pdf`. Depois, localizar nos sites oficiais o edital ou manual mais recente de Fuvest, Unicamp, Unesp e UERJ. Se o site de uma prova não trouxer o programa por matéria, registrar a falta em `provas.md`, em vez de inferir de sites de cursinho.

- [ ] **Step 2: Escrever `fontes/provas.md`**

Para cada prova, registrar: edição do documento, URL, data de acesso, data da prova mais recente e o programa por matéria, com os conteúdos listados pela própria fonte. Acrescentar uma seção "Só em vestibulares tradicionais" com o que aparece em alguma prova e não na matriz do Inep. Confirmar aqui se números complexos entram nesse grupo.

Se Espanhol, Literatura ou leituras obrigatórias variarem por prova, indicar isso. Leituras obrigatórias mudam todo ano: anotar a edição a que se referem.

- [ ] **Step 3: Escrever `fontes/pesos_enem.md`**

Reunir ao menos três rankings públicos de assuntos mais cobrados, com fonte, período e metodologia. Para cada matéria, listar os temas em três faixas (alta, média, baixa), que viram a `prioridade` 1, 2 e 3. Quando as fontes discordarem, registrar a divergência e usar a faixa mais frequente entre elas. Sem dado para um tema, usar prioridade 2 e anotar "sem dado".

---

### Task 7: Entrega 1, mapa geral

**Files:**
- Create: `canais/estudativo/catalogo/mapa_geral.csv`

- [ ] **Step 1: Ler os assuntos e montar o mapa**

Para cada uma das 35 matérias do cronograma, agrupar os assuntos em trilhas e módulos, seguindo a ordem dos pré-requisitos, e não a do cronograma. O nome da matéria no catálogo é o nome escolar, por exemplo "Matemática", "Física" e "Biologia". As 35 matérias do cronograma são reagrupadas em 14 matérias escolares: Matemática, Física, Química, Biologia, História, Geografia, Filosofia, Sociologia, Língua Portuguesa e Interpretação, Literatura, Redação, Inglês, Espanhol, e Artes e Educação Física.

Exemplo de linha:

```csv
materia,trilha,modulo,camada,aulas_estimadas,provas,observacao
Matemática,Frações,Somar frações,nucleo,5,enem;fuvest;unicamp;unesp;uerj,Depende de MMC
```

Regras:
- Cada módulo tem de 3 a 8 aulas, incluindo a prática. Fora disso, dividir ou juntar.
- `aulas_estimadas` conta a prática.
- `provas` vem de `fontes/provas.md`.
- Nivelamento entra como módulo próprio, com a estimativa do que os módulos seguintes vão pedir.

- [ ] **Step 2: Criar as playlists de Matéria e Comece Aqui**

Em `fontes/playlists_planejadas.csv`, com as mesmas colunas de `playlists.csv`, uma linha `materia` por matéria e uma `comece_aqui` por matéria com Nivelamento. Elas ficam nesse arquivo porque a validação recusa playlist vazia, e ainda não há aulas. Exemplo:

```csv
PL-MAT,Matemática do Zero,materia,Matemática,materia=Matemática;camada=nivelamento|nucleo,Toda a Matemática do ensino médio em ordem. Para ENEM e vestibulares.,matemática do zero
PL-MAT-BASE,Comece Aqui: Bases de Matemática,comece_aqui,Matemática,materia=Matemática;camada=nivelamento,As bases de Matemática para quem está há muito tempo sem estudar.,matemática básica do zero
```

Nesta entrega não rodar `validar_catalogo.py`: ainda não há aulas. Mostrar a lista ao usuário no Step 4.

- [ ] **Step 3: Gerar a planilha e somar as estimativas**

Run: `py gerar_planilha.py`
Expected: imprime o caminho de `revisao_catalogo.xlsx`

Somar `aulas_estimadas` por camada e matéria, e comparar o total com a estimativa de cerca de 1.000 aulas da spec.

- [ ] **Step 4: Parar para aprovação**

Mostrar ao usuário os totais por camada e matéria, a lista de trilhas e os pontos de decisão. Não começar a Task 8 sem aprovação.

---

### Task 8: Entrega 2, Matemática aula por aula

**Files:**
- Modify: `canais/estudativo/catalogo/aulas.csv`, `playlists.csv`, `cobertura.csv`

- [ ] **Step 1: Escrever as aulas do Núcleo, trilha por trilha**

Para cada trilha do mapa, ler os assuntos correspondentes em `Projetos/Estudos/Enem/estudos/01-matematica/*.html`, usando `py _ferramentas/extrair_material.py <html> <txt>` a partir da raiz do repositório. O material serve de consulta sobre o conteúdo; não copiar a divisão de seções nem os episódios antigos.

Formato do id: `MAT-<TRILHA>-<NNN>`, com a sigla da trilha em 3 letras e numeração sequencial por trilha. Exemplo de linhas em `aulas.csv`:

```csv
MAT-FRA-010,Encontrar o denominador comum,Matemática,Frações,Somar frações,1,"Ao final, você consegue reescrever 1/2 e 1/3 com o mesmo denominador",nucleo,aula,MAT-MMC-004;MAT-FRA-006,enem;fuvest;unicamp;unesp;uerj,1,denominador comum
MAT-FRA-011,Somar frações com denominadores diferentes,Matemática,Frações,Somar frações,2,"Ao final, você consegue somar 1/2 + 1/3",nucleo,aula,MAT-FRA-010,enem;fuvest;unicamp;unesp;uerj,1,como somar frações com denominadores diferentes
```

Em cada aula, conferir:
- A habilidade é algo que a pessoa consegue **fazer**, com um exemplo concreto.
- Cabe em 5 a 8 minutos, cerca de 800 a 1.250 palavras a 2,6 palavras por segundo.
- Todo conteúdo que a aula usa está em `prereqs` ou é aviso de passagem.
- `prereqs` lista só dependências diretas.
- `termo_busca` é o que um aluno digitaria no YouTube.
- Módulo com 4 aulas ou mais termina em `pratica`. Módulo com até 3 aulas pode dividir a prática com o seguinte da mesma trilha; nesse caso, os `prereqs` da prática incluem aulas dos dois módulos.

- [ ] **Step 2: Escrever a Extensão e o Nivelamento**

Extensão: temas que `fontes/provas.md` marca como só de vestibulares tradicionais, com `provas` sem `enem` e sem serem pré-requisito do Núcleo.

Nivelamento: percorrer os `prereqs` do Núcleo e criar aulas só para bases do fundamental que o Núcleo usa. Essas aulas ficam **antes** das que dependem delas em `aulas.csv`. A validação recusa aula de Nivelamento que não leve a uma aula do Núcleo.

- [ ] **Step 3: Criar as playlists de Trilha e de Prova**

Em `playlists.csv`, uma linha `trilha` por trilha e uma `prova` por prova com pelo menos 10 aulas de Matemática:

```csv
PL-MAT-FRA,Frações do Zero,trilha,Matemática,materia=Matemática;trilha=Frações,"Frações do zero, uma habilidade por aula.",frações do zero
PL-MAT-FUVEST,Matemática para a Fuvest,prova,Matemática,materia=Matemática;prova=fuvest;tipo=aula,Todas as aulas de Matemática que caem na Fuvest.,matemática fuvest
```

Mover também as linhas de Matemática de `fontes/playlists_planejadas.csv` para `playlists.csv`. As das outras matérias só passam para lá na Task 9, junto com as aulas de cada uma.

- [ ] **Step 4: Preencher a cobertura de Matemática**

Em `cobertura.csv`, cada um dos 93 assuntos de `Matemática` recebe os ids das suas aulas ou uma justificativa.

- [ ] **Step 5: Validar**

Run: `py validar_catalogo.py --area Matemática`
Expected: `0 erros`. Revisar cada aviso de título e dividir a aula, se ela tiver duas habilidades.

- [ ] **Step 6: Revisão independente de ordem**

Pedir a um subagente, sem contar a conclusão, que leia `aulas.csv` de Matemática como aluno iniciante e aponte aulas que pareçam usar algo ainda não ensinado, ou com duas habilidades. Corrigir o que for confirmado e repetir o Step 5.

- [ ] **Step 7: Gerar a planilha e parar para aprovação**

Run: `py gerar_planilha.py`

Mostrar ao usuário o total por camada, as trilhas, as playlists, exemplos de aulas e os assuntos cortados com justificativa. Não começar a Task 9 sem aprovação. Se o usuário mudar o modelo, corrigir Matemática antes de seguir.

---

### Task 9: Entrega 3, demais matérias

**Files:**
- Modify: `canais/estudativo/catalogo/aulas.csv`, `playlists.csv`, `cobertura.csv`

Só começa com a Entrega 2 aprovada, aplicando os ajustes do usuário.

- [ ] **Step 1: Repetir os Steps 1 a 6 da Task 8 para cada matéria**

Em cada matéria, mover suas linhas de `fontes/playlists_planejadas.csv` para `playlists.csv`.

Ordem: Língua Portuguesa e Interpretação, Redação, Literatura, Física, Química, Biologia, História, Geografia, Filosofia, Sociologia, Inglês, Espanhol, e Artes e Educação Física. As pastas do material são `05-linguagens`, `06-redacao`, `07-artes`, `03-fisica`, `02-quimica`, `11-biologia`, `08-historia`, `04-geografia`, `09-filosofia` e `10-sociologia`, em `Projetos/Estudos/Enem/estudos/`. Física e Química usam a Matemática como pré-requisito, então seus `prereqs` podem apontar para ids `MAT-*`, e essas aulas vêm antes em `aulas.csv`.

Validar ao fim de cada matéria com `--area`, conforme a área do cronograma. Áreas com várias matérias (Natureza, Humanas, Linguagens) só zeram a cobertura quando todas as suas matérias estiverem prontas; até lá, os erros restantes de cobertura devem ser apenas dessas matérias pendentes.

- [ ] **Step 2: Validar o catálogo inteiro**

Run: `py validar_catalogo.py`
Expected: `0 erros`, com os 559 assuntos cobertos

- [ ] **Step 3: Gerar a planilha e entregar**

Run: `py gerar_planilha.py`

Mostrar ao usuário os totais finais, comparados à estimativa da spec, e a lista completa de playlists. Depois, atualizar a memória do projeto com o novo padrão do Estudativo e oferecer a spec da Etapa 2.
