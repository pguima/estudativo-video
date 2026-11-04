# Estudativo · Questão 010 — ENEM 2025, 2º dia, caderno amarelo, questão 136: lagoa circular de raio 1 km com ciclovia;
# um ponto está protegido se houver um policial a no máximo 200 m dele, sobre a ciclovia; π ≈ 3.
# Número mínimo de policiais? → 15 (alternativa C). Enunciado: enunciado/questao.png.
# Aula horizontal 1920x1080 (~5 min), explicada passo a passo.
# Caminho: COMPRIMENTO DA CIRCUNFERÊNCIA (raio, diâmetro, π = volta ÷ diâmetro, C = 2πr, exemplo da roda) →
# passo 1: unidades (1 km = 1000 m) → passo 2: a volta (2·3·1000 = 6000 m) → a ideia: cada policial cobre 200 m
# para cada lado = 400 m; a pegadinha (6000 ÷ 200 = 30, alternativa D) → passo 3: 6000 ÷ 400 = 15 (C) →
# por que é o mínimo (14 × 400 = 5600: faltam 400 m) + conferência → divisão não exata: arredonda para cima
# (raio 1,1 km → 16,5 → 17) + desafio (raio 2 km, 250 m) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: quantos policiais protegem a ciclovia da lagoa? (comprimento da circunferência)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. 'Pi' é a letra grega (leia "
            "'pí'). Faça as perguntas com curiosidade genuína, mostre surpresa na resposta e comemore o resultado. "
            "Respeite as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, "
            "resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e trinta e seis do ENEM dois mil e vinte e cinco. [p=0.2] Em volta de uma lagoa circular, "
        "[p=0.1] com raio de *um quilômetro,* [p=0.1] existe uma *ciclovia.* [p=0.3] {b}A prefeitura quer colocar "
        "policiais na ciclovia [p=0.1] para deixá-la *totalmente protegida.* [p=0.3] {c}Um ponto está protegido [p=0.1] "
        "se houver um policial a, no máximo, *duzentos metros* dele, [p=0.1] em cima da ciclovia. [p=0.3] {d}E a questão "
        "manda usar *três* como aproximação para pi. [p=0.3] {e}Qual é o *número mínimo* de policiais? [p=0.3] Nessa "
        "aula, você vai resolver passo a passo, [p=0.1] usando o *comprimento da circunferência* [p=0.1] e uma ideia "
        "simples: [p=0.1] *quanto cada policial protege.*"),
    dict(id="02", block="circunferencia", text=
        "{a}Primeiro, a ferramenta: [p=0.1] o *comprimento da circunferência.* [p=0.2] É a medida da volta inteira, "
        "[p=0.1] como se a gente cortasse o círculo [p=0.1] e esticasse a linha. [p=0.3] {b}Dois nomes importantes: "
        "[p=0.1] o *raio* vai do centro até a borda, [p=0.1] e o *diâmetro* atravessa o círculo de lado a lado. [p=0.2] "
        "O diâmetro vale *dois raios.* [p=0.3] {c}E tem um fato curioso: [p=0.1] em *qualquer* círculo, [p=0.1] a volta "
        "dividida pelo diâmetro [p=0.1] dá sempre o mesmo número, [p=0.1] um pouco mais que três. [p=0.2] Esse número é o "
        "*pi:* [p=0.1] três vírgula um quatro, e continua. [p=0.3] {d}Então a volta é pi vezes o diâmetro, [p=0.1] ou "
        "seja, [p=0.1] *C é igual a dois vezes pi vezes r.* [p=0.3] {e}Um exemplo: [p=0.1] uma roda com raio de trinta "
        "centímetros. [p=0.2] Usando pi igual a três, [p=0.1] a volta é dois vezes três vezes trinta: [p=0.1] *cento e "
        "oitenta centímetros.*"),
    dict(id="03", block="unidades", text=
        "{a}Passo um: [p=0.1] colocar tudo na *mesma unidade.* [p=0.2] O raio está em quilômetros, [p=0.1] e a distância "
        "de proteção está em metros. [p=0.3] {b}Um quilômetro são *mil metros.* [p=0.2] Então o raio da lagoa é *mil "
        "metros.*"),
    dict(id="04", block="volta", text=
        "{a}Passo dois: [p=0.1] o tamanho da ciclovia. [p=0.2] Ela contorna a lagoa, [p=0.1] e a questão manda "
        "desconsiderar a largura da pista. [p=0.2] Então o comprimento da ciclovia [p=0.1] é o comprimento da "
        "circunferência. [p=0.3] {b}C é igual a dois vezes pi vezes r. [p=0.2] Dois, vezes três, vezes mil: [p=0.1] "
        "*seis mil metros.* [p=0.3] {c}Se a gente esticasse a ciclovia, [p=0.1] ela seria uma linha reta de *seis "
        "quilômetros.*"),
    dict(id="05", block="cobertura", text=
        "{a}Agora, a ideia principal: [p=0.1] quanto da ciclovia *um policial* protege? [p=0.3] {b}Olhe a figura do "
        "enunciado. [p=0.2] O ponto P está protegido [p=0.1] se houver um policial até duzentos metros *para um lado* "
        "[p=0.1] ou até duzentos metros *para o outro.* [p=0.3] {c}Agora inverta o olhar: [p=0.1] um policial parado "
        "protege duzentos metros *à frente* [p=0.1] e duzentos metros *atrás.* [p=0.2] No total, [p=0.1] *quatrocentos "
        "metros* de ciclovia. [p=0.3] {d}E aqui mora a *pegadinha.* [p=0.2] Quem esquece um dos lados [p=0.1] divide "
        "seis mil por duzentos [p=0.1] e encontra trinta. [p=0.2] Alternativa D. [p=0.2] *Errado:* [p=0.1] cada policial "
        "protege o *dobro* disso."),
    dict(id="06", block="divisao", text=
        "{a}Passo três: [p=0.1] dividir a volta em trechos de quatrocentos metros. [p=0.3] {b}Seis mil dividido por "
        "quatrocentos. [p=0.2] Cortando dois zeros, [p=0.1] fica sessenta dividido por quatro: [p=0.1] *quinze.* [p=0.3] "
        "{c}Basta colocar um policial no meio de cada trecho. [p=0.2] Os quinze trechos fecham a volta inteira, [p=0.1] "
        "sem buraco e sem sobra. [p=0.3] {d}*Quinze policiais.* [p=0.2] Alternativa *C.*"),
    dict(id="07", block="minimo", text=
        "{a}Mas por que não dá com menos? [p=0.2] Vamos testar com *quatorze.* [p=0.3] {b}Quatorze vezes quatrocentos "
        "[p=0.1] dá cinco mil e seiscentos metros. [p=0.3] {c}Sobram *quatrocentos metros* [p=0.1] sem nenhum policial "
        "por perto. [p=0.2] A ciclovia não fica totalmente protegida. [p=0.3] {d}Com quinze: [p=0.1] quinze vezes "
        "quatrocentos, [p=0.1] *seis mil metros.* [p=0.2] Cobre exatamente a volta. [p=0.2] Confere!"),
    dict(id="08", block="generaliza", text=
        "{a}E se a divisão não desse exata? [p=0.2] Imagine que o raio fosse *um vírgula um quilômetro.* [p=0.3] {b}A "
        "volta seria dois vezes três vezes mil e cem: [p=0.1] *seis mil e seiscentos metros.* [p=0.2] Dividido por "
        "quatrocentos, [p=0.1] dá *dezesseis vírgula cinco.* [p=0.3] {c}Não existe meio policial. [p=0.2] Com dezesseis, "
        "[p=0.1] sobra um pedaço sem proteção. [p=0.2] Então a gente *arredonda para cima:* [p=0.1] *dezessete.* "
        "[p=0.3] {d}Agora é com você: [p=0.1] e se a lagoa tivesse raio de *dois quilômetros,* [p=0.1] e cada policial "
        "protegesse *duzentos e cinquenta metros* para cada lado? [p=0.2] Quantos policiais, no mínimo? [p=0.2] Deixe sua "
        "resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, passamos o raio para metros: [p=0.1] mil metros. [p=0.2] "
        "{c}Depois, calculamos a volta: [p=0.1] dois vezes três vezes mil, [p=0.1] seis mil metros. [p=0.2] {d}Cada "
        "policial protege duzentos metros para cada lado: [p=0.1] quatrocentos metros. [p=0.2] {e}E seis mil dividido "
        "por quatrocentos [p=0.1] dá quinze policiais."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*comprimento da circunferência,* [p=0.2] {c}*unidades e conversões* [p=0.2] {d}e *divisibilidade.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
