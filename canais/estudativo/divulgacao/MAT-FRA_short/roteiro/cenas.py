# Short-convite da trilha Frações e Decimais (MAT-FRA-001 a 021, publicadas) — vertical 1080x1920, ~35 s.
# Mesmo arquivo para Shorts, Reels e TikTok. Retenção: desafio no 1º quadro com contagem regressiva (laço aberto),
# o erro clássico 2/5 riscado + o macete da borboleta (MAT-FRA-008), virada "só se soma pedaço do mesmo tamanho",
# as capas reais das 21 aulas e o convite para a playlist "Frações e Decimais do Zero".
# Fatos: 1/2 + 1/3 = (1·3 + 2·1)/(2·3) = 5/6; 1/2 = 3/6 e 1/3 = 2/6.
# Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Quanto é 1/2 + 1/3? Você tem 3 segundos"

VOZ = dict(
    tags=["animada", "confiante", "curiosa"],
    prompt=("Narre um vídeo curto de redes sociais para estudantes: voz de professor jovem, carismático e MUITO "
            "envolvente, falando direto com o aluno. Energia alta já na primeira palavra, sem introdução. Tom de desafio "
            "no começo, de revelação no macete, acolhedor na virada e entusiasmado no convite final. Ritmo ágil mas claro, "
            "com ênfase nas palavras-chave. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular "
            "nem repetir nada."),
)

RITMO = dict(gap_bloco=0.0, pad_inicio=0.0, pad_fim=1.2)

SCENES = [
    dict(id="s01", block="desafio", text=
        "{a}Quanto é *um meio* mais *um terço?* [p=0.15] {b}Você tem *três segundos.* [p=1.6]"),
    dict(id="s02", block="macete", text=
        "{a}Se você pensou *dois quintos,* [p=0.1] {b}*errou!* [p=0.15] {c}O macete é a *borboleta.* [p=0.1] "
        "{d}Em cima: um vezes três, *mais* dois vezes um, *cinco.* [p=0.1] {e}Embaixo: dois vezes três, *seis.* [p=0.1] "
        "{f}*Cinco sextos!*"),
    dict(id="s03", block="virada", text=
        "{a}Fração não é *difícil.* [p=0.15] {b}A regra é uma só: [p=0.05] {c}só se soma pedaço do *mesmo tamanho.*"),
    dict(id="s04", block="trilha", text=
        "{a}Por isso eu montei *vinte e uma aulas,* do *zero:* [p=0.1] {b}o que é fração, [p=0.05] {c}somar e "
        "subtrair, [p=0.05] {d}multiplicar e dividir, [p=0.05] {e}números decimais [p=0.05] {f}e dízimas."),
    dict(id="s05", block="cta", text=
        "{a}Procure *Estudativo* no YouTube [p=0.1] {b}e assista à playlist *Frações e Decimais do Zero.* [p=0.2] "
        "{c}Bons estudos!"),
]
