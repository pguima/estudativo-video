# Short — Tecnativo 017: o Reddit vai virar um site só para quem tem login (e a culpa é da IA do Google)
# Base: original/fonte_reddit_login.md (CNBC + 9to5Google, 29/10/2026). Marcas: {cue} animação · *texto* destaque ·
# [p=0.2] pausa · números por extenso (viram algarismos na legenda, ver NUMEROS no visual.py)

TITULO = "O Reddit vai exigir login para ler (e a culpa é da IA do Google)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia: voz masculina adulta, grave, enérgica e empolgada, como quem conta para "
            "um amigo uma notícia que vai mudar a internet. Ritmo rápido e energia alta desde a primeira palavra, sem "
            "introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. Tom "
            "provocador na pergunta final. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Sabe quando você pesquisa no Google [p=0.1] e a melhor resposta está no *Reddit?* [p=0.2] "
        "{b}Em breve, [p=0.1] vai precisar de *login* para ler."),
    dict(id="02", block="anuncio", text=
        "{a}O CEO do Reddit, *Steve Huffman,* anunciou nesta quinta: [p=0.1] "
        "{b}o site vai virar *só para quem tem conta.*"),
    dict(id="03", block="culpado", text=
        "{a}E o motivo [p=0.1] é o próprio *Google.* [p=0.2] {b}Com as *respostas de IA* na busca, [p=0.1] "
        "{c}a pessoa lê o resumo [p=0.1] e *não clica* mais no Reddit."),
    dict(id="04", block="numeros", text=
        "{a}As visitas vindas do Google caíram *mais de um milhão* por semana. [p=0.1] "
        "{b}E as ações do Reddit despencaram *mais de quinze por cento.*"),
    dict(id="05", block="robos", text=
        "{a}Tem outro alvo: [p=0.1] *robôs* que copiam o Reddit [p=0.1] para treinar IA. [p=0.2] "
        "{b}Segundo ele, [p=0.1] quase todo acesso não autorizado [p=0.1] vem de quem *não está logado.*"),
    dict(id="06", block="quando", text=
        "{a}Os testes começam *ainda este ano,* [p=0.1] em países *fora dos Estados Unidos.* [p=0.2] "
        "{b}Huffman disse que segurou isso o quanto pôde, [p=0.1] e chamou de *sinal dos tempos.*"),
    dict(id="07", block="final", text=
        "{a}E aí: [p=0.1] você criaria uma conta [p=0.1] só para ler o Reddit? [p=0.2] {b}Ou a internet aberta *acabou?*"),
]
