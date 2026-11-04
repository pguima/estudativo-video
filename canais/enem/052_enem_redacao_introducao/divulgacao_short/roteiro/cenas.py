# Divulgação da série Introdução da Redação (Redação ENEM) em outras redes — SHORT vertical 1080x1920, ~35 s.
# Mesmo arquivo para Shorts, Reels, TikTok, Instagram, Facebook (Reels) e X. Retenção nos 5 primeiros segundos:
# o 1º quadro já mostra a folha com "Desde os primórdios da humanidade..." + "SUA REDAÇÃO COMEÇA ASSIM?" (funciona
# sem som); em ~1,5 s o carimbo PARE! bate e risca o clichê; aos ~3 s o mesmo começo aparece em 3 temas (genérico).
# Depois: as 3 perguntas da introdução (ep. 1), as 7 capas, a série anterior (Leitura da Proposta) e o convite.
# Sem religião nos exemplos (temas do ENEM 2018, 2019, 2021). Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Sua redação começa com \"Desde os primórdios\"? Pare agora"

VOZ = dict(
    tags=["animada", "confiante", "curiosa"],
    prompt=("Narre um vídeo curto de redes sociais para estudantes do ENEM: voz de professor jovem, carismático e "
            "MUITO envolvente, falando direto com o aluno. Energia alta já na primeira palavra, sem introdução. "
            "Tom de alerta no gancho, de revelação nas três perguntas e entusiasmo no convite final. Ritmo ágil mas "
            "claro, com ênfase nas palavras-chave. Leia apenas o texto, exatamente como está escrito, sem acrescentar, "
            "pular nem repetir nada."),
)

PRONUNCIA = {"ENEM": "Enem"}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.0, pad_fim=1.2)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Se a sua redação começa assim, [p=0.1] {b}*pare agora.*"),
    dict(id="02", block="generico", text=
        "{a}*Desde os primórdios* serve pra *qualquer tema.* [p=0.15] {b}Por isso, não diz *nada* sobre o seu."),
    dict(id="03", block="perguntas", text=
        "{a}Uma boa introdução responde *três perguntas:* [p=0.1] {b}de onde parte a discussão, [p=0.1] "
        "{c}o que você defende [p=0.1] {d}e por quais caminhos vai provar."),
    dict(id="04", block="serie", text=
        "{a}Na série *Introdução da Redação,* [p=0.1] {b}são *sete aulas,* do zero, [p=0.1] {c}da primeira frase até a *tese.*"),
    dict(id="05", block="anteriores", text=
        "{a}E se você ainda não viu, [p=0.1] {b}comece pela série *Leitura da Proposta.*"),
    dict(id="06", block="cta", text=
        "{a}Procure *Estudativo* no YouTube [p=0.1] {b}e assista à playlist *Redação: Introdução.* [p=0.2] "
        "{c}Bons estudos!"),
]
