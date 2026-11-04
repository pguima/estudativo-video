# Divulgação da série Leitura da Proposta (Redação ENEM) em outras redes — SHORT vertical 1080x1920, ~35 s.
# Mesmo arquivo para Shorts, Reels e TikTok. Alta retenção: gancho no 1º quadro (zero com texto perfeito), placar,
# laço aberto (teste rápido com o tema de 2016), as 6 capas reais e o convite para a playlist.
# Fatos da série: fuga = zero; tangenciar limita C2, C3 e C5 a 40 (até 480 pontos a menos); 2016 = "Caminhos para
# combater a intolerância religiosa no Brasil" — falar só do assunto amplo tangencia.
# Visual em ../divulgacao_visual.py (compartilhado com o horizontal). Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Dá pra tirar ZERO na redação do ENEM com um texto perfeito"

VOZ = dict(
    tags=["animada", "confiante", "curiosa"],
    prompt=("Narre um vídeo curto de redes sociais para estudantes do ENEM: voz de professor jovem, carismático e "
            "MUITO envolvente, falando direto com o aluno. Energia alta já na primeira palavra, sem introdução. "
            "Tom de revelação no gancho, suspense no teste, entusiasmo no convite final. Ritmo ágil mas claro, com "
            "ênfase nas palavras-chave. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular "
            "nem repetir nada."),
)

PRONUNCIA = {"ENEM": "Enem"}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.0, pad_fim=1.2)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Dá pra tirar *zero* na redação do ENEM [p=0.15] {b}com um texto *perfeito.*"),
    dict(id="02", block="placar", text=
        "{a}É só *fugir do tema.* [p=0.2] {b}E quem só *tangencia* o tema [p=0.1] {c}perde até "
        "*quatrocentos e oitenta pontos.*"),
    dict(id="03", block="causa", text=
        "{a}E o erro nasce *antes da primeira linha:* [p=0.15] {b}na *leitura da proposta.*"),
    dict(id="04", block="teste", text=
        "{a}Olha esse tema: [p=0.1] {b}*Caminhos para combater a intolerância religiosa no Brasil.* [p=0.2] "
        "{c}Se o seu texto fala só de *intolerância religiosa,* [p=0.15] {d}você *tangenciou.*"),
    dict(id="05", block="serie", text=
        "{a}Por isso eu montei *seis aulas,* do *zero,* [p=0.1] {b}pra você nunca mais cair nessa."),
    dict(id="06", block="cta", text=
        "{a}Procure *Estudativo* no YouTube [p=0.1] {b}e assista à playlist *Redação: Leitura da Proposta.* [p=0.2] "
        "{c}Bons estudos!"),
]
