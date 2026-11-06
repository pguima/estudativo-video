"""Valida o catálogo do Estudativo. Sai com código 1 se houver erro."""
import argparse
import math
import sys
from collections import Counter

import catalogo_lib as lib


def regra_valida(playlist):
    """Devolve os filtros se tipo e regra são válidos; senão None."""
    if playlist.get("tipo") not in lib.TIPOS_PLAYLIST:
        return None
    filtros = lib.parsear_regra(playlist.get("regra") or "")
    if not filtros or set(filtros) - set(lib.CHAVES_REGRA):
        return None
    return filtros


def rotulo(item):
    """O id do item; sem id, 'linha N' (número da linha no CSV)."""
    valor = (item.get("id") or "").strip()
    if valor:
        return valor
    linha = item.get("_linha")
    return f"linha {linha}" if linha else "(sem id)"


def erro_de_extra(item, quem):
    """Erro para valores além do cabeçalho (em geral, vírgula sem aspas dentro de um campo)."""
    linha = item.get("_linha", "?")
    onde = f"linha {linha}" if quem.startswith("linha ") else f"{quem}: linha {linha}"
    return f"{onde}: colunas a mais {item['_extra']}; campo com vírgula precisa de aspas"


def checar_campos(cat):
    erros = []
    vistos = set()
    ultima_ordem = {}
    for aula in cat.aulas:
        aid = rotulo(aula)
        if aula.get("_extra"):
            erros.append(erro_de_extra(aula, aid))
        if aula.get("id", ""):
            if aula["id"] in vistos:
                erros.append(f"id repetido: {aula['id']}")
            vistos.add(aula["id"])
        for campo in lib.CAMPOS_AULA:
            if campo == "prereqs":
                continue
            valor = aula.get(campo) or ""
            vazio = not lib.lista(valor) if campo == "provas" else not valor.strip()
            if vazio:
                erros.append(f"{aid}: campo vazio: {campo}")
        if aula.get("camada") not in lib.CAMADAS:
            erros.append(f"{aid}: camada inválida: {aula.get('camada')}")
        if aula.get("tipo") not in lib.TIPOS_AULA:
            erros.append(f"{aid}: tipo inválido: {aula.get('tipo')}")
        if aula.get("prioridade") not in lib.PRIORIDADES:
            erros.append(f"{aid}: prioridade inválida: {aula.get('prioridade')}")
        provas = lib.lista(aula.get("provas") or "")
        for prova in provas:
            if prova not in lib.PROVAS:
                erros.append(f"{aid}: provas: valor inválido: {prova}")
        for prova in dict.fromkeys(p for p in provas if provas.count(p) > 1):
            erros.append(f"{aid}: provas: valor repetido: {prova}")
        modulo = (aula.get("materia"), aula.get("trilha"), aula.get("modulo"))
        try:
            ordem = int(aula.get("ordem") or "")
        except ValueError:
            erros.append(f"{aid}: ordem não numérica: {aula.get('ordem')}")
            continue
        if modulo in ultima_ordem and ordem <= ultima_ordem[modulo]:
            erros.append(f"{aid}: ordem deve crescer dentro do módulo")
        ultima_ordem[modulo] = ordem
    return erros


def checar_campos_playlists(cat):
    erros = []
    vistos = set()
    for playlist in cat.playlists:
        pid = rotulo(playlist)
        if playlist.get("_extra"):
            erros.append(erro_de_extra(playlist, pid))
        if playlist.get("id", ""):
            if playlist["id"] in vistos:
                erros.append(f"{pid}: id de playlist repetido")
            vistos.add(playlist["id"])
        for campo in lib.CAMPOS_PLAYLIST:
            if not (playlist.get(campo) or "").strip():
                erros.append(f"{pid}: campo vazio: {campo}")
    return erros


def checar_prereqs(cat):
    erros = []
    posicao = {aula["id"]: i for i, aula in enumerate(cat.aulas)}
    for i, aula in enumerate(cat.aulas):
        for prereq in lib.lista(aula["prereqs"]):
            if prereq not in posicao:
                erros.append(f"{rotulo(aula)}: pré-requisito inexistente: {prereq}")
            elif posicao[prereq] >= i:
                erros.append(f"{rotulo(aula)}: pré-requisito vem depois ou forma círculo: {prereq}")
    return erros


def checar_camadas(cat):
    erros = []
    por_id = {aula["id"]: aula for aula in cat.aulas}
    for aula in cat.aulas:
        for prereq in lib.lista(aula["prereqs"]):
            alvo = por_id.get(prereq)
            if alvo and alvo["camada"] == "extensao" and aula["camada"] != "extensao":
                erros.append(f"{rotulo(aula)}: depende da Extensão: {prereq}")
    alcancadas = set()
    pendentes = [aula["id"] for aula in cat.aulas
                 if aula["camada"] == "nucleo" and aula["tipo"] == "aula"]
    while pendentes:
        aula = por_id.get(pendentes.pop())
        if aula is None:
            continue
        for prereq in lib.lista(aula["prereqs"]):
            if prereq not in alcancadas:
                alcancadas.add(prereq)
                pendentes.append(prereq)
    for aula in cat.aulas:
        if (aula["camada"] == "nivelamento" and aula["tipo"] == "aula"
                and aula["id"] not in alcancadas):
            erros.append(f"{rotulo(aula)}: aula de Nivelamento que não leva ao Núcleo")
    return erros


def checar_modulos(cat):
    trilhas = {}
    for aula in cat.aulas:
        modulos = trilhas.setdefault((aula["materia"], aula["trilha"]), {})
        modulos.setdefault(aula["modulo"], []).append(aula)
    erros = []
    for (materia, trilha), modulos in trilhas.items():
        sequencia = list(modulos.items())
        for i, (modulo, aulas) in enumerate(sequencia):
            nome = f"{materia} > {trilha} > {modulo}"
            if any(a["tipo"] == "pratica" for a in aulas[:-1]):
                erros.append(f"{nome}: prática fora do fim do módulo")
            if aulas[-1]["tipo"] == "pratica":
                continue
            seguinte = sequencia[i + 1][1] if i + 1 < len(sequencia) else None
            if len(aulas) >= lib.MIN_AULAS_PRATICA_PROPRIA:
                erros.append(f"{nome}: não termina em prática (módulo com 4 aulas ou mais)")
            elif seguinte is None:
                erros.append(f"{nome}: não termina em prática (último módulo da trilha)")
            elif seguinte[-1]["tipo"] != "pratica":
                erros.append(f"{nome}: não termina em prática e o módulo seguinte também não")
            elif seguinte[-1]["camada"] == "extensao" and aulas[-1]["camada"] != "extensao":
                erros.append(f"{nome}: prática conjunta caiu na Extensão, camada diferente")
    return erros


def checar_cobertura(cat, areas=None):
    erros = []
    ids = {aula["id"] for aula in cat.aulas}
    no_cronograma = {(a["area"], a["assunto"]) for a in cat.assuntos}
    validas = sorted({area for area, _ in no_cronograma})
    for area in areas or []:
        if area not in validas:
            erros.append(f"cobertura: área inexistente: {area}; áreas válidas: {validas}")
    linhas = {}
    for c in cat.cobertura:
        chave = (c["area"], c["assunto"])
        if areas and c["area"] not in areas:
            continue
        nome = f"{c['area']} > {c['assunto']}" if any(chave) else f"linha {c.get('_linha', '?')}"
        if c.get("_extra"):
            erros.append(f"cobertura: {erro_de_extra(c, 'linha ' + str(c.get('_linha', '?')))} [{nome}]")
        if chave in linhas:
            onde = [str(x["_linha"]) for x in (linhas[chave], c) if x.get("_linha")]
            sufixo = f" (linhas {' e '.join(onde)})" if len(onde) == 2 else ""
            erros.append(f"cobertura: linha duplicada: {nome}{sufixo}")
        else:
            linhas[chave] = c
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


def checar_playlists(cat):
    erros = []
    titulos = set()
    for playlist in cat.playlists:
        pid = rotulo(playlist)
        if playlist["titulo"] in titulos:
            erros.append(f"{pid}: título repetido: {playlist['titulo']}")
        titulos.add(playlist["titulo"])
        if playlist["tipo"] not in lib.TIPOS_PLAYLIST:
            erros.append(f"{pid}: tipo inválido: {playlist['tipo']}")
            continue
        if regra_valida(playlist) is None:
            erros.append(f"{pid}: regra inválida: {playlist['regra']}")
            continue
        if not lib.aulas_da_playlist(playlist, cat.aulas):
            erros.append(f"{pid}: playlist vazia")
    return erros


def playlists_esperadas(aulas):
    """{(tipo, materia, detalhe): [ids]} exigido pelo catálogo, na ordem do curso."""
    esperadas = {}
    for aula in aulas:
        materia = aula["materia"]
        esperadas.setdefault(("trilha", materia, aula["trilha"]), []).append(aula["id"])
        if aula["camada"] in ("nivelamento", "nucleo"):
            esperadas.setdefault(("materia", materia, ""), []).append(aula["id"])
        if aula["camada"] == "nivelamento":
            esperadas.setdefault(("comece_aqui", materia, ""), []).append(aula["id"])
    provas = {}
    for aula in aulas:
        if aula["tipo"] != "aula":
            continue
        for prova in dict.fromkeys(lib.lista(aula["provas"])):
            if prova in lib.PROVAS:
                provas.setdefault(("prova", aula["materia"], prova), []).append(aula["id"])
    for chave, ids in provas.items():
        if len(ids) >= lib.MIN_AULAS_PROVA:
            esperadas[chave] = ids
    return esperadas


def descrever_diferenca(ids, esperado):
    faltam = [i for i in esperado if i not in ids]
    sobram = [i for i in ids if i not in esperado]
    if not faltam and not sobram:
        return "ordem diferente"
    return f"faltam: {faltam}; sobram: {sobram}"


def chave_da_playlist(playlist, filtros):
    detalhe = ""
    if playlist["tipo"] in ("trilha", "prova"):
        detalhe = (filtros.get(playlist["tipo"]) or [""])[0]
    return (playlist["tipo"], playlist["materia"], detalhe)


def checar_estrutura_playlists(cat):
    erros = []
    esperadas = playlists_esperadas(cat.aulas)
    reais = {}
    for playlist in cat.playlists:
        filtros = regra_valida(playlist)
        if filtros is None or playlist["tipo"] == "especial":
            continue
        chave = chave_da_playlist(playlist, filtros)
        pid = playlist["id"]
        if chave not in esperadas:
            if playlist["tipo"] == "prova":
                erros.append(
                    f"{pid}: playlist de prova inesperada {chave}: abaixo do mínimo de "
                    f"{lib.MIN_AULAS_PROVA} aulas, ou regra sem a prova")
            else:
                erros.append(f"{pid}: playlist inesperada {chave}")
            continue
        reais.setdefault(chave, []).append(pid)
        ids = [a["id"] for a in lib.aulas_da_playlist(playlist, cat.aulas)]
        if ids != esperadas[chave]:
            diferenca = descrever_diferenca(ids, esperadas[chave])
            if diferenca == "ordem diferente":
                erros.append(f"{pid}: ordem diferente do esperado para {chave}; regra: {playlist['regra']}")
            else:
                erros.append(f"{pid}: ids diferentes do esperado para {chave}; {diferenca}; "
                             f"regra: {playlist['regra']}")
    for chave, pids in reais.items():
        if len(pids) > 1:
            erros.append(f"{', '.join(pids)}: mesma chave {chave}")
    for chave in esperadas:
        if chave not in reais:
            erros.append(f"falta a playlist {chave}")
    return erros


def avisos_de_titulo(cat):
    return [
        f"{rotulo(aula)}: confira se é uma habilidade só: {aula['titulo']}"
        for aula in cat.aulas
        if " e " in aula["titulo"]
    ]


def checar_orcamento(aulas, mapa):
    if not mapa:
        return []
    previsto = Counter()
    for linha in mapa:
        previsto[(linha["materia"], linha["trilha"])] += int(linha["aulas_estimadas"])
    reais = Counter((aula["materia"], aula["trilha"]) for aula in aulas)
    erros = []
    for (materia, trilha), total in reais.items():
        if (materia, trilha) not in previsto:
            erros.append(f"{materia} > {trilha}: trilha fora do mapa")
            continue
        teto = math.floor(previsto[(materia, trilha)] * lib.MAX_EXCESSO_TRILHA + 1e-9)
        if total > teto:
            erros.append(f"{materia} > {trilha}: {total} vídeos, acima do teto de {teto}")
    return erros


def validar(cat, areas=None):
    erros = (
        checar_orcamento(cat.aulas, cat.mapa) +
        checar_campos(cat) + checar_campos_playlists(cat) + checar_prereqs(cat)
        + checar_camadas(cat) + checar_modulos(cat) + checar_cobertura(cat, areas)
        + checar_playlists(cat) + checar_estrutura_playlists(cat)
    )
    return erros, avisos_de_titulo(cat)


def main():
    lib.usar_utf8()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--area", action="append", help="limita a cobertura a esta área do cronograma")
    args = parser.parse_args()
    try:
        cat = lib.carregar()
    except lib.ErroDeFormato as erro:
        print(erro)
        return 1
    erros, avisos = validar(cat, args.area)
    for aviso in avisos:
        print(f"AVISO {aviso}")
    for erro in erros:
        print(f"ERRO  {erro}")
    print(f"{len(cat.aulas)} aulas, {len(cat.playlists)} playlists, {len(erros)} erros, {len(avisos)} avisos")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
