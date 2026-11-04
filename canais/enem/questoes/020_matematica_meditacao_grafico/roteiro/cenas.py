# Estudativo · Questão 020 — ENEM 2025, 2º dia, caderno amarelo, questão 142: gráfico da frequência respiratória (rpm)
# de um praticante avançado de meditação em função do tempo (min). Antes de t1 a frequência é f1 (constante); a partir de
# t1 (início da meditação) ela diminui até t2 e, a partir de t2, fica constante em f2 → alternativa D.
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: ler um gráfico (eixos, cada ponto = um instante e um valor; sobe / desce / reta deitada) →
# A FERRAMENTA 2: diretamente proporcional (y = k · x, reta que passa pela origem: dobra um, dobra o outro) e
# inversamente proporcional (x · y = k: dobra um, o outro cai pela metade; curva que nunca fica deitada) → passo 1: o que
# a questão pede (a partir de t1) → passo 2: de t1 a t2, desce → passo 3: depois de t2, reta deitada (constante) → D →
# pegadinhas (A, B, C, E) → generaliza (café esfriando até a temperatura da sala) + desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: o gráfico da respiração na meditação (leitura de gráfico e proporcionalidade)"

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
        "{a}Questão cento e quarenta e dois do ENEM dois mil e vinte e cinco. [p=0.2] O gráfico mostra a *frequência "
        "respiratória* de quem medita há muito tempo: [p=0.1] quantas vezes a pessoa respira por minuto, [p=0.1] ao "
        "longo do tempo. [p=0.3] {b}No instante *tê um,* [p=0.1] a meditação começa. [p=0.2] E no instante *tê dois,* "
        "[p=0.1] a respiração se estabiliza. [p=0.3] {c}A pergunta: [p=0.1] a partir de tê um, [p=0.1] como a "
        "frequência se comporta? [p=0.3] {d}Nessa aula, você vai aprender a ler o gráfico trecho por trecho, [p=0.1] e "
        "a desmontar as palavras difíceis das alternativas."),
    dict(id="02", block="leitura", text=
        "{a}Primeiro, [p=0.1] como se lê um gráfico. [p=0.3] {b}No eixo deitado fica o *tempo,* [p=0.1] em minutos. "
        "[p=0.2] No eixo em pé, [p=0.1] a *frequência,* [p=0.1] em respirações por minuto. [p=0.3] {c}Cada ponto da "
        "linha junta as duas coisas: [p=0.1] um instante [p=0.1] e o valor naquele instante. [p=0.3] {d}Andando da "
        "esquerda para a direita, [p=0.1] se a linha *sobe,* [p=0.1] o valor aumenta. [p=0.2] Se *desce,* [p=0.1] "
        "diminui. [p=0.2] {e}E se fica *deitada,* [p=0.1] reta e na mesma altura, [p=0.1] o valor não muda: [p=0.1] é "
        "*constante.*"),
    dict(id="03", block="proporcao", text=
        "{a}Agora, [p=0.1] as palavras difíceis das alternativas. [p=0.3] {b}*Diretamente proporcional:* [p=0.1] quando "
        "uma grandeza dobra, [p=0.1] a outra também dobra. [p=0.2] Dois minutos, dez; [p=0.1] quatro minutos, vinte. "
        "[p=0.2] O gráfico é uma *reta que sobe* [p=0.1] e passa pelo zero. [p=0.3] {c}*Inversamente proporcional:* "
        "[p=0.1] quando uma dobra, [p=0.1] a outra cai pela *metade.* [p=0.2] Dois, seis; [p=0.1] quatro, três. "
        "[p=0.2] {d}O gráfico é uma curva que desce cada vez mais devagar, [p=0.1] mas *nunca fica deitada.*"),
    dict(id="04", block="trecho1", text=
        "{a}Passo um: [p=0.1] olhar só o pedaço que a pergunta pede. [p=0.3] {b}Antes de tê um, [p=0.1] a pessoa "
        "ainda não está meditando, [p=0.1] e a linha fica deitada em *efe um.* [p=0.3] {c}Mas a pergunta diz: [p=0.1] "
        "*a partir de tê um.* [p=0.2] Então, [p=0.1] esse começo fica de fora."),
    dict(id="05", block="trecho2", text=
        "{a}Passo dois: [p=0.1] de tê um até tê dois. [p=0.3] {b}A linha *desce:* [p=0.1] sai de efe um [p=0.1] e chega "
        "em efe dois, [p=0.1] que é mais baixo. [p=0.3] {c}Então, [p=0.1] nesse trecho, [p=0.1] a frequência "
        "respiratória *diminui.* [p=0.2] A pessoa passa a respirar menos vezes por minuto."),
    dict(id="06", block="trecho3", text=
        "{a}Passo três: [p=0.1] depois de tê dois. [p=0.3] {b}O tempo continua passando, [p=0.1] mas a linha fica "
        "deitada em efe dois. [p=0.2] O valor não muda mais: [p=0.1] é *constante.* [p=0.3] {c}Juntando os dois "
        "trechos: [p=0.1] diminui até tê dois, [p=0.1] e a partir daí fica constante. [p=0.3] {d}Alternativa *D.*"),
    dict(id="07", block="pegadinhas", text=
        "{a}Agora, [p=0.1] por que as outras estão erradas. [p=0.3] {b}Letra A, [p=0.1] *mantém-se constante:* [p=0.1] só vale "
        "depois de tê dois. [p=0.2] Entre tê um e tê dois, [p=0.1] a linha desce. [p=0.3] {c}Letra B, [p=0.1] *diretamente "
        "proporcional:* [p=0.1] o tempo aumenta [p=0.1] e a frequência diminui. [p=0.2] Diretamente proporcional "
        "teria que subir junto. [p=0.3] {d}Letra C, [p=0.1] *inversamente proporcional:* [p=0.1] parece, [p=0.1] porque desce, "
        "[p=0.1] mas a curva inversa nunca fica deitada. [p=0.2] Aqui, [p=0.1] depois de tê dois, [p=0.1] ela fica. "
        "[p=0.3] {e}E a letra E, [p=0.1] *diminui o tempo todo:* [p=0.1] depois de tê dois, [p=0.1] ela não diminui mais."),
    dict(id="08", block="generaliza", text=
        "{a}Esse desenho, [p=0.1] que desce e depois deita, [p=0.1] aparece em muito lugar. [p=0.3] {b}Um café quente "
        "na mesa [p=0.1] esfria rápido no começo, [p=0.1] depois mais devagar, [p=0.1] até ficar na temperatura da "
        "sala. [p=0.2] Daí em diante, [p=0.1] constante. [p=0.3] {c}Agora é com você: [p=0.1] e um copo de suco gelado "
        "na mesma mesa? [p=0.2] Como seria o gráfico da temperatura? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="09", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Primeiro, [p=0.1] veja o que cada eixo mostra. [p=0.2] {c}Depois, [p=0.1] "
        "separe só o trecho que a pergunta pede. [p=0.2] {d}Em cada trecho, [p=0.1] veja se a linha sobe, desce ou "
        "fica deitada. [p=0.2] {e}E só use proporcional quando o gráfico tiver a forma certa."),
    dict(id="10", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*leitura de gráficos,* [p=0.2] {c}*funções crescentes, decrescentes e constantes* [p=0.2] {d}e *grandezas "
        "diretamente e inversamente proporcionais.* [p=0.3] {e}Se quiser aprender cada assunto desde o começo, [p=0.1] "
        "procure essas aulas aqui no canal. [p=0.4] {f}E se essa questão te ajudou, [p=0.1] inscreva-se no "
        "*Estudativo* [p=0.1] para não perder a próxima questão."),
]
