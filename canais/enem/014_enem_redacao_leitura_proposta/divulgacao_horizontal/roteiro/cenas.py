# Divulgação da série Leitura da Proposta (Redação ENEM) em outras redes — HORIZONTAL 1920x1080, ~70 s.
# Para YouTube (feed), Facebook, LinkedIn e X. Mesmo gancho do Short + um bloco curto por episódio (com a capa real)
# e convite para as duas playlists: "Redação: Leitura da Proposta" (a série) e "Redação ENEM do Zero" (a trilha).
# Visual em ../divulgacao_visual.py (compartilhado com o Short). Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Dá pra tirar ZERO na redação do ENEM com um texto perfeito: a série Leitura da Proposta"

VOZ = dict(
    tags=["animada", "confiante", "curiosa"],
    prompt=("Narre um vídeo curto de divulgação para estudantes do ENEM: voz de professor jovem, carismático e "
            "MUITO envolvente, falando direto com o aluno. Energia alta já na primeira palavra, sem introdução. "
            "Tom de revelação no gancho, suspense no teste, ritmo de lista animada nos episódios e entusiasmo no "
            "convite final. Ritmo ágil mas claro, com ênfase nas palavras-chave. Leia apenas o texto, exatamente "
            "como está escrito, sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {"ENEM": "Enem"}

RITMO = dict(gap_bloco=0.15, pad_inicio=0.0, pad_fim=1.5)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Dá pra tirar *zero* na redação do ENEM [p=0.15] {b}com um texto *perfeito.*"),
    dict(id="02", block="placar", text=
        "{a}É só *fugir do tema.* [p=0.2] {b}E quem só *tangencia* o tema [p=0.1] {c}perde até "
        "*quatrocentos e oitenta pontos.*"),
    dict(id="03", block="causa", text=
        "{a}O pior: [p=0.1] quase ninguém percebe. [p=0.2] {b}O erro nasce *antes da primeira linha,* [p=0.1] "
        "{c}na *leitura da proposta.*"),
    dict(id="04", block="teste", text=
        "{a}Olha esse tema: [p=0.1] {b}*Caminhos para combater a intolerância religiosa no Brasil.* [p=0.2] "
        "{c}Se o seu texto fala só de *intolerância religiosa,* [p=0.15] {d}você *tangenciou:* [p=0.1] "
        "{e}faltou *combater* e faltou *o Brasil.*"),
    dict(id="05", block="intro", text=
        "{a}Na série *Leitura da Proposta,* [p=0.1] {b}você aprende, do *zero:*"),
    dict(id="06", block="eps", text="{a}o que a prova pede, *antes de escrever;*"),
    dict(id="07", block="eps", text="{a}a desmontar a *frase temática* em blocos;"),
    dict(id="08", block="eps", text="{a}a usar os *textos motivadores* sem copiar;"),
    dict(id="09", block="eps", text="{a}a diferença entre *tangenciar* e *fugir* do tema;"),
    dict(id="10", block="eps", text="{a}o caminho do tema até a *tese,* em seis passos;"),
    dict(id="11", block="eps", text="{a}e um desafio com *dez pegadinhas* e *cinco temas reais* do ENEM."),
    dict(id="12", block="cta", text=
        "{a}As seis aulas estão no canal *Estudativo,* no YouTube, [p=0.1] {b}na playlist *Redação: Leitura da Proposta.* "
        "[p=0.2] {c}E, para a redação completa, [p=0.1] siga a playlist *Redação ENEM do Zero.* [p=0.2] "
        "{d}Te vejo na primeira aula!"),
]
