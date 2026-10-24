# Short promocional — Seguridade Social, Módulo 1 (Fundamentos) no canal Estudativo. Vertical 1080x1920, 25–30 s.
# Narração literal do pedido do usuário (24/10/2026). Módulo 1 = Temporada 1 do PLANO_DE_VIDEOS.md (aulas 001 a 009).
# Sem estatísticas, depoimentos ou promessa de aprovação. Cenas ilustrativas desenhadas no motor; único material real:
# a capa da Aula 1 (001_conceito_e_tripe/youtube/capa_A_tripe.jpg).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa

TITULO = "Vai estudar Seguridade Social para concurso? Comece pelo Módulo 1"

VOZ = dict(
    tags=["confiante", "animada"],
    prompt=("Narre um Short de YouTube para estudantes de concurso: voz masculina adulta, natural, clara, firme e "
            "envolvente, como um professor que fala direto com o aluno. Energia alta já na primeira palavra, sem "
            "introdução. Ritmo ágil mas compreensível, com ênfase nas palavras-chave. Tom acolhedor e convidativo no "
            "final. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.0, pad_fim=1.0)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Vai estudar *Seguridade Social* para *concurso?* [p=0.3] {b}Então, comece *por aqui!*"),
    dict(id="02", block="decorar", text=
        "{a}Antes de *decorar* conceitos [p=0.1] e resolver *questões,* [p=0.2] {b}é importante entender os "
        "*fundamentos* da matéria."),
    dict(id="03", block="modulo", text=
        "{a}No canal *Estudativo,* [p=0.2] {b}você encontra o *primeiro módulo* do curso de Seguridade Social: "
        "[p=0.2] {c}*Fundamentos.*"),
    dict(id="04", block="base", text=
        "{a}Dê o *primeiro passo* [p=0.1] {b}para construir uma *base sólida* nessa matéria."),
    dict(id="05", block="cta", text=
        "{a}Acesse o canal *Estudativo* [p=0.1] e comece agora pelo *Módulo 1.* [p=0.2] {b}Te espero lá!"),
]
