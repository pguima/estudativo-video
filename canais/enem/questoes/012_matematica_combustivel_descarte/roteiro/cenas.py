# Estudativo · Questão 012 — ENEM 2025, 2º dia, caderno amarelo, questão 138: caminhões-tanque de 30.000 L; em todo
# transporte um mesmo volume é descartado (independe da quantidade). Pedido de 10.000 L: enviou 10.200, chegaram 9.900.
# Novo pedido: o dobro do encomendado, no mesmo caminhão. Volume mínimo a enviar? → 20.300 L (alternativa C).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080 (~4–5 min), explicada passo a passo.
# Caminho: A FERRAMENTA: parte fixa × parte proporcional (taxa de entrega da pizza; é a ideia da função afim) →
# passo 1: o descarte (10.200 − 9.900 = 300 L; a distribuidora contou 200 e faltaram 100) → a ideia: o descarte é a
# parte fixa (não dobra) → passo 2: o novo pedido (2 × 10.000 = 20.000, o dobro do ENCOMENDADO) → passo 3: enviar =
# 20.000 + 300 = 20.300 (C), cabe no caminhão → conferir as alternativas (A e B não chegam; D e E chegam mas não são
# o mínimo; D dobra o envio, E dobra o descarte) → regra geral + desafio (pedido triplo: 30.300 > 30.000) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: quanto combustível a distribuidora deve enviar? (parte fixa × parte proporcional)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e trinta e oito do ENEM dois mil e vinte e cinco. [p=0.2] Uma distribuidora tem "
        "caminhões-tanque [p=0.1] de *trinta mil litros.* [p=0.3] {b}Em todo transporte, [p=0.1] um *mesmo volume* de "
        "combustível é descartado, [p=0.1] e esse volume *não depende* da quantidade transportada. [p=0.3] {c}Um posto "
        "encomendou *dez mil litros.* [p=0.2] A distribuidora enviou *dez mil e duzentos,* [p=0.1] mas chegaram só "
        "*nove mil e novecentos.* [p=0.3] {d}Agora o posto quer *o dobro* do que encomendou, [p=0.1] no mesmo caminhão. "
        "[p=0.2] {e}Qual é o *volume mínimo* que a distribuidora deve enviar? [p=0.3] Nessa aula, você vai resolver "
        "passo a passo, [p=0.1] separando o que é *fixo* [p=0.1] do que é *proporcional.*"),
    dict(id="02", block="ferramenta", text=
        "{a}Primeiro, a ferramenta: [p=0.1] *parte fixa* e *parte proporcional.* [p=0.3] {b}Pense numa pizzaria. "
        "[p=0.2] Cada pizza custa *quarenta reais,* [p=0.1] e a entrega custa *seis reais.* [p=0.2] Uma pizza: "
        "[p=0.1] quarenta mais seis, [p=0.1] *quarenta e seis reais.* [p=0.3] {c}E com duas pizzas? [p=0.2] O preço das "
        "pizzas dobra: [p=0.1] oitenta. [p=0.2] Mas a entrega continua *seis.* [p=0.2] Total: [p=0.1] *oitenta e seis,* "
        "[p=0.1] e não noventa e dois. [p=0.3] {d}A parte proporcional *dobra* junto com a quantidade. [p=0.2] A parte "
        "fixa *fica igual.* [p=0.3] {e}Uma parte que varia mais uma parte fixa: [p=0.1] essa é a ideia da *função "
        "afim.*"),
    dict(id="03", block="descarte", text=
        "{a}Passo um: [p=0.1] descobrir *quanto* é descartado. [p=0.3] {b}O que chega é o que foi enviado, [p=0.1] "
        "*menos* o descarte. [p=0.3] {c}Foram enviados dez mil e duzentos litros, [p=0.1] e chegaram nove mil e "
        "novecentos. [p=0.2] Dez mil e duzentos menos nove mil e novecentos: [p=0.1] *trezentos litros.* [p=0.3] {d}Repare: "
        "[p=0.1] a distribuidora mandou duzentos a mais, [p=0.1] mas o descarte era de trezentos. [p=0.2] Por isso "
        "faltaram *cem litros* no posto."),
    dict(id="04", block="fixo", text=
        "{a}Agora, a ideia principal. [p=0.2] O enunciado diz que o descarte *não depende* da quantidade "
        "transportada. [p=0.3] {b}Então o descarte é a *parte fixa,* [p=0.1] como a taxa de entrega da pizza. "
        "[p=0.3] {c}Transportando dez mil ou vinte mil litros, [p=0.1] o caminhão descarta *trezentos litros.* [p=0.2] "
        "Nem mais, nem menos. [p=0.3] {d}E é por isso que a questão fala em usar o *mesmo caminhão:* [p=0.1] assim, "
        "o descarte continuou o mesmo."),
    dict(id="05", block="pedido", text=
        "{a}Passo dois: [p=0.1] quanto o posto quer receber? [p=0.3] {b}O dobro do volume *encomendado* no pedido "
        "anterior. [p=0.2] O encomendado foi dez mil litros. [p=0.2] Então: [p=0.1] duas vezes dez mil, [p=0.1] *vinte "
        "mil litros.* [p=0.3] {c}Cuidado: [p=0.1] não é o dobro do que foi *enviado,* [p=0.1] nem do que *chegou.* "
        "[p=0.2] É o dobro do que foi *pedido.*"),
    dict(id="06", block="envio", text=
        "{a}Passo três: [p=0.1] quanto enviar. [p=0.3] {b}Para chegar em vinte mil litros, [p=0.1] a distribuidora "
        "precisa mandar os vinte mil, [p=0.1] *mais* os trezentos que vão ser descartados. [p=0.3] {c}Vinte mil mais "
        "trezentos: [p=0.1] *vinte mil e trezentos litros.* [p=0.3] {d}E cabe no caminhão? [p=0.2] Sim: [p=0.1] vinte "
        "mil e trezentos é menos que trinta mil. [p=0.3] {e}*Vinte mil e trezentos litros.* [p=0.2] Alternativa *C.*"),
    dict(id="07", block="alternativas", text=
        "{a}Vamos conferir todas as alternativas: [p=0.1] de cada envio, [p=0.1] tiramos os trezentos do descarte. "
        "[p=0.3] {b}Com vinte mil e cem, [p=0.1] chegam dezenove mil e oitocentos. [p=0.2] Com vinte mil e duzentos, "
        "[p=0.1] dezenove mil e novecentos. [p=0.2] As duas *não chegam* aos vinte mil. [p=0.3] {c}Com vinte mil e "
        "trezentos, [p=0.1] chegam *exatamente* vinte mil. [p=0.3] {d}As alternativas D e E também entregam vinte mil, "
        "[p=0.1] mas mandam combustível *a mais.* [p=0.2] A D dobra o envio anterior, [p=0.1] e a E dobra o descarte. "
        "[p=0.2] Nenhuma das duas é o *mínimo.*"),
    dict(id="08", block="generaliza", text=
        "{a}O mesmo raciocínio serve para qualquer pedido: [p=0.1] *enviar é igual ao pedido mais trezentos.* [p=0.3] "
        "{b}Se o posto pedisse quinze mil litros, [p=0.1] a distribuidora mandaria *quinze mil e trezentos.* [p=0.3] "
        "{c}Agora é com você: [p=0.1] e se o novo pedido fosse *o triplo* do primeiro? [p=0.2] Um caminhão só daria "
        "conta? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, o descarte: [p=0.1] dez mil e duzentos menos nove mil e "
        "novecentos, [p=0.1] trezentos litros. [p=0.2] {c}O descarte é fixo: [p=0.1] não dobra. [p=0.2] {d}O novo "
        "pedido é o dobro de dez mil: [p=0.1] vinte mil litros. [p=0.2] {e}E o envio mínimo é vinte mil mais trezentos: "
        "[p=0.1] vinte mil e trezentos litros."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*grandezas proporcionais,* [p=0.2] {c}*função afim* [p=0.2] {d}e *equações do primeiro grau.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
