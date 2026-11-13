# Short-convite da trilha Divisibilidade, MMC e MDC (MAT-DIV-001 a 008, publicadas) — vertical 1080x1920, ~35 s.
# Mesmo arquivo para Shorts, Reels e TikTok. Retenção: desafio no 1º quadro com contagem regressiva (laço aberto),
# resposta + macete dos noves fora (MAT-DIV-002), virada "não é decoreba: é saber qual usar e quando", as capas
# reais das 8 aulas e o convite para a playlist "Divisibilidade, MMC e MDC do Zero".
# Fatos: 4 + 5 + 7 + 2 = 18; 18 ÷ 9 = 2; 4572 ÷ 9 = 508.
# Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "4.572 se divide por 9? Você tem 3 segundos"

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
        "{a}*Quatro mil quinhentos e setenta e dois* se divide por *nove?* [p=0.15] {b}Você tem *três segundos.* [p=1.6]"),
    dict(id="s02", block="macete", text=
        "{a}*Sim!* [p=0.15] {b}O macete: *some os algarismos.* [p=0.1] {c}Quatro mais cinco, mais sete, mais dois: "
        "[p=0.05] {d}*dezoito.* [p=0.1] {e}Dezoito se divide por *nove,* [p=0.05] {f}então o número também se divide."),
    dict(id="s03", block="virada", text=
        "{a}MMC e MDC parecem *decoreba.* [p=0.15] {b}Mas a prova só quer saber [p=0.05] {c}*qual usar,* e *quando.*"),
    dict(id="s04", block="trilha", text=
        "{a}Por isso eu montei *oito aulas,* do *zero:* [p=0.1] {b}múltiplos e divisores, [p=0.05] {c}regras de "
        "divisibilidade, [p=0.05] {d}números primos, [p=0.05] {e}MMC e MDC [p=0.05] {f}e os problemas de prova."),
    dict(id="s05", block="cta", text=
        "{a}Procure *Estudativo* no YouTube [p=0.1] {b}e assista à playlist *Divisibilidade, MMC e MDC do Zero.* [p=0.2] "
        "{c}Bons estudos!"),
]
