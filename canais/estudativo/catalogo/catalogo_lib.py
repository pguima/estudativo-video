"""Leitura do catálogo do Estudativo e resolução das playlists."""
import csv
import sys
from dataclasses import dataclass, field
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
TIPOS_PLAYLIST = ("trilha", "materia", "comece_aqui", "prova", "especial")
COLUNAS_COBERTURA = ("area", "assunto", "aulas", "justificativa")
COLUNAS_CRONOGRAMA = ("Área", "Assunto")
CHAVES_REGRA = ("materia", "trilha", "modulo", "camada", "prova", "tipo")
MIN_AULAS_PROVA = 10
MIN_AULAS_PRATICA_PROPRIA = 4
MAX_EXCESSO_TRILHA = 1.4


@dataclass
class Catalogo:
    aulas: list
    playlists: list
    cobertura: list
    assuntos: list
    mapa: list = field(default_factory=list)


def lista(texto):
    return [parte.strip() for parte in texto.split(";") if parte.strip()]


class ErroDeFormato(Exception):
    """CSV com cabeçalho, separador ou codificação fora do combinado."""


def usar_utf8():
    """Faz o terminal do Windows imprimir acentos."""
    reconfigurar = getattr(sys.stdout, "reconfigure", None)
    if reconfigurar:
        reconfigurar(encoding="utf-8")


def ler_csv(caminho, colunas=()):
    """Lê o CSV em dicts. `_linha` = número da linha no arquivo; `_extra` = valores além do cabeçalho."""
    caminho = Path(caminho)
    try:
        with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
            return _ler_linhas(caminho.name, csv.reader(arquivo), colunas)
    except UnicodeDecodeError as erro:
        raise ErroDeFormato(f"{caminho.name}: não está em UTF-8 ({erro.reason}); salve como CSV UTF-8") from erro


def _ler_linhas(nome, leitor, colunas):
    cabecalho = [c.strip() for c in next(leitor, [])]
    faltam = [c for c in colunas if c not in cabecalho]
    if faltam:
        dica = ""
        if any(";" in c for c in cabecalho):
            dica = " (o arquivo parece separado por ';'; salve como CSV com vírgula)"
        raise ErroDeFormato(f"{nome}: faltam colunas {faltam}{dica}")
    linhas = []
    while True:
        inicio = leitor.line_num + 1
        try:
            valores = next(leitor)
        except StopIteration:
            return linhas
        linha = {}
        extra = []
        for i, valor in enumerate(valores):
            if i < len(cabecalho) and cabecalho[i]:
                linha[cabecalho[i]] = valor
            else:
                extra.append(valor)
        if not any(v.strip() for v in valores):
            continue
        for coluna in cabecalho:
            linha.setdefault(coluna, "")
        linha["_linha"] = inicio
        if any(v.strip() for v in extra):
            linha["_extra"] = extra
        linhas.append(linha)


def carregar(pasta=PASTA):
    pasta = Path(pasta)
    cronograma = ler_csv(pasta / "fontes" / "cronograma-enem.csv", COLUNAS_CRONOGRAMA)
    arquivo_mapa = pasta / "mapa_geral.csv"
    mapa = ler_csv(arquivo_mapa) if arquivo_mapa.exists() else []
    return Catalogo(
        mapa=mapa,
        aulas=ler_csv(pasta / "aulas.csv", CAMPOS_AULA),
        playlists=ler_csv(pasta / "playlists.csv", CAMPOS_PLAYLIST),
        cobertura=ler_csv(pasta / "cobertura.csv", COLUNAS_COBERTURA),
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
