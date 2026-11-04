# Short — Tecnativo 020: a Microsoft oferece dinheiro para 60 mil funcionários irem embora (por causa da IA)
# Base: original/fonte_microsoft_saida_voluntaria.md (SiliconANGLE, Yahoo Finance, Tom's Hardware, CNBC, 26–27/10/2026).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso (viram algarismos na legenda,
# ver NUMEROS no visual.py)

TITULO = "A Microsoft quer pagar 60 mil funcionários para irem embora (e a culpa é da IA)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia: voz masculina adulta, grave, enérgica e empolgada, como quem conta para "
            "um amigo uma notícia que acabou de estourar. Ritmo rápido e energia alta desde a primeira palavra, sem "
            "introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. Tom "
            "provocador na pergunta final. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}A Microsoft ofereceu dinheiro [p=0.1] para *sessenta mil funcionários* irem embora. [p=0.2] "
        "{b}É quase *um quarto* da empresa."),
    dict(id="02", block="quem", text=
        "{a}A oferta vale nos Estados Unidos, [p=0.1] Canadá, [p=0.1] Índia [p=0.1] e Reino Unido. [p=0.2] "
        "{b}E chega até *vice-presidente.*"),
    dict(id="03", block="pacote", text=
        "{a}O pacote, segundo o Business Insider: [p=0.1] uma ou duas *semanas de salário* [p=0.1] para cada seis "
        "meses de casa, [p=0.1] {b}mais ações [p=0.1] e plano de saúde por um tempo."),
    dict(id="04", block="motivo", text=
        "{a}E o motivo? [p=0.1] *Inteligência artificial.* [p=0.2] {b}A Microsoft planeja investir mais de *cento e "
        "setenta bilhões de dólares* este ano, [p=0.1] {c}boa parte em *data centers* de IA."),
    dict(id="05", block="maio", text=
        "{a}Em maio, [p=0.1] ela já tinha feito uma oferta assim, [p=0.1] para cerca de *nove mil* pessoas. [p=0.2] "
        "{b}Agora é quase *sete vezes* mais."),
    dict(id="06", block="memo", text=
        "{a}Quem aceitar tem até o *começo de dezembro.* [p=0.2] {b}E a chefe de pessoas da Microsoft escreveu: "
        "[p=0.1] {c}*isso é novo para nós.* [p=0.1] *Vamos aprender.*"),
    dict(id="07", block="final", text=
        "{a}E aí: [p=0.1] se te oferecessem dinheiro para sair, [p=0.1] você *aceitava?* [p=0.2] {b}Ou acha que a IA "
        "vai chegar no seu emprego *de qualquer jeito?*"),
]
