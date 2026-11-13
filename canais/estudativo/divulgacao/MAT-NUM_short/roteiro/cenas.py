# Short-convite da trilha Números e Contas (MAT-NUM-001 a 019, já publicadas) — vertical 1080x1920, ~35 s.
# Mesmo arquivo para Shorts, Reels e TikTok. Retenção: desafio no 1º quadro com contagem regressiva (laço aberto),
# resposta + macete em 5 s (entrega rápida), virada para a dor ("não é falta de cabeça, é base"), as capas reais das
# 19 aulas e o convite para a playlist "Números e Contas do Zero".
# Fatos: 48 × 5 = 480 ÷ 2 = 240 (macete da MAT-NUM-012); 99 × 7 = 700 − 7 = 693.
# Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Quanto é 48 × 5? Você tem 3 segundos"

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
        "{a}Quanto é *quarenta e oito vezes cinco?* [p=0.15] {b}Você tem *três segundos.* [p=1.6]"),
    dict(id="s02", block="macete", text=
        "{a}*Duzentos e quarenta.* [p=0.15] {b}O macete: vezes cinco é *vezes dez,* [p=0.05] {c}dividido por *dois.* "
        "[p=0.1] {d}Quatrocentos e oitenta, [p=0.05] {e}metade, [p=0.05] {f}duzentos e quarenta."),
    dict(id="s03", block="virada", text=
        "{a}Se conta ainda te trava, [p=0.1] {b}não é falta de cabeça. [p=0.15] {c}É *base* que ninguém te ensinou."),
    dict(id="s04", block="trilha", text=
        "{a}Por isso eu montei *dezenove aulas,* do *zero:* [p=0.1] {b}tabuada com macetes, [p=0.05] {c}conta armada, "
        "[p=0.05] {d}divisão, [p=0.05] {e}ordem das operações [p=0.05] {f}e números negativos."),
    dict(id="s05", block="cta", text=
        "{a}Procure *Estudativo* no YouTube [p=0.1] {b}e assista à playlist *Números e Contas do Zero.* [p=0.2] "
        "{c}Bons estudos!"),
]
