# Roteiro — Potenciação e Radiciação, Episódio 1 de 7: O que é potência e os casos especiais (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seção 02 (+ Questão 3 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PAPEL DOBRADO: cada dobra multiplica as camadas por 2; três dobras = 2 · 2 · 2 = 8 camadas, não 6.
#   (apoio) CORRENTE DE WHATSAPP: cada pessoa manda para 2 → na 5ª rodada, 2⁵ = 32 pessoas.
#   ESCADA QUE DESCE DIVIDINDO: 2³ = 8, 2² = 4, 2¹ = 2; cada degrau para baixo ÷ 2 → 2⁰ = 1, 2⁻¹ = 1/2, 2⁻² = 1/4, 2⁻³ = 1/8.
# Revisão relâmpago (série de Operações): (−2)⁴ = 16, (−2)³ = −8, −3² = −9, (−3)² = 9.
# Nós fazemos: 5⁰ = 1 · 3⁻² = 1/9 · (1/2)⁻¹ = 2 · (−1)⁷ = −1.
# QUESTÃO 3 do material (texto idêntico na tela): (2/3)⁻² + (1/2)⁻³ = 9/4 + 8 = 41/4 → D.
#   A (−41/4): achou que expoente negativo deixa o resultado negativo (explicação do material).
#   Explicações NOSSAS (o material só explica a A): C (25/4) = 9/4 + 4 → fez 2³ como 2 · 2 (um fator a menos);
#   E (12) = 4 + 8 → na primeira parte elevou só o 2, sem inverter a fração; B (17/36) é menor que 1, impossível
#   (só a segunda parte já dá 8).
# Frases-chave (meio e fim, idênticas):
#   1. Potência é multiplicar a base por ela mesma.
#   2. Qualquer número, menos o zero, elevado a zero dá 1.
#   3. Expoente negativo inverte; não deixa negativo.
# Atalhos (verde): "vá dobrando o resultado" (2, 4, 8, 16, 32) · "expoente zero → 1, sem conta" ·
#   "expoente negativo: inverta a base e tire o menos" · "fração: vire de cabeça para baixo" · "par de sinais de menos vira mais".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Potência do zero: por que 2⁰ = 1 e expoente negativo NÃO dá negativo | Potenciação Ep. 1"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "pH": "pê agá",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Potência quase nunca é o *tema* de uma questão do ENEM. [p=0.5] {b}Mas ela é a *língua* em que estão escritas "
        "as questões de [p=0.2] {c}juros, [p=0.2] Pitágoras, [p=0.2] áreas, [p=0.2] meia-vida [p=0.2] e pH. [p=0.5] "
        "{d}Quem não lê essa língua [p=0.2] *trava antes de começar.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber *o que é uma potência,* [p=0.3] {b}e por que qualquer número "
        "elevado a zero *dá um.* [p=0.4] {c}E nunca mais vai achar que expoente negativo [p=0.2] dá resultado *negativo.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Multiplicar é somar parcelas iguais: [p=0.2] três vezes dois é dois "
        "mais dois mais dois, [p=0.2] seis. [p=0.4] {b}E *inverter* um número é virar ele de cabeça para baixo. [p=0.3] "
        "{c}O inverso de dois, [p=0.2] que é dois sobre um, [p=0.2] é *um meio.* [p=0.3] {d}O inverso de dois terços [p=0.2] "
        "é *três meios.*"),

    # ================= BLOCO A: O PAPEL DOBRADO =================
    dict(id="04", block="papel", text=
        "{t}Pegue uma folha de papel [p=0.2] e dobre ao meio. [p=0.3] Quantas camadas? [p=0.5] {a}*Duas.* [p=0.3] {b}Dobre "
        "de novo: [p=0.2] *quatro.* [p=0.3] {c}Mais uma vez: [p=0.2] *oito.* [p=0.4] {d}Cada dobra *multiplica* as camadas "
        "por dois. [p=0.3] {e}Três dobras: [p=0.2] dois vezes dois vezes dois, [p=0.2] oito camadas."),
    dict(id="05", block="papel", text=
        "{t}Essa conta tem um jeito curto de escrever: [p=0.2] *dois elevado a três.* [p=0.4] {a}Isso é uma *potência:* "
        "[p=0.2] uma multiplicação de números iguais. [p=0.4] {b}O número que se repete é a *base:* [p=0.2] o dois. [p=0.3] "
        "{c}O numerozinho no alto é o *expoente:* [p=0.2] ele conta quantas vezes a base aparece. [p=0.4] {d}E cada dois "
        "dessa conta se chama *fator,* [p=0.2] que é cada número de uma multiplicação."),
    dict(id="06", block="papel", text=
        "{t}No geral, [p=0.2] a matemática escreve assim: [p=0.2] *a elevado a n.* [p=0.3] {a}O *a* é qualquer número, "
        "[p=0.2] e o *n* diz quantos fatores *a* você multiplica. [p=0.5] {b}Um exemplo do celular: [p=0.2] uma corrente "
        "de WhatsApp em que cada pessoa manda para *duas.* [p=0.4] {c}Na quinta rodada, [p=0.2] quantas pessoas recebem? "
        "[p=0.4] {d}Dois elevado a cinco: [p=0.2] dois, [p=0.2] vezes dois, [p=0.2] vezes dois, [p=0.2] vezes dois, "
        "[p=0.2] vezes dois. [p=0.3] {e}*Trinta e duas.*"),
    dict(id="07", block="papel", text=
        "{t}E um atalho para não se perder nos fatores: [p=0.3] {a}*vá dobrando o resultado.* [p=0.3] {b}Dois, [p=0.2] "
        "quatro, [p=0.2] oito, [p=0.2] dezesseis, [p=0.2] trinta e dois. [p=0.4] {c}Cada passo é o anterior vezes a base. "
        "[p=0.3] {d}Contou cinco passos? [p=0.2] É dois elevado a cinco."),

    # ================= BLOCO B: O ERRO DE PARTIDA =================
    dict(id="08", block="erro_partida", text=
        "{t}Agora, uma pergunta rápida: [p=0.2] quanto é dois elevado a três? [p=0.5] {a}Muita gente responde *seis.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o dois e o três estão ali, [p=0.2] e dois vezes três dá seis. [p=0.4] "
        "{c}Mas lembre da folha: [p=0.2] três dobras deram *oito* camadas, [p=0.2] não seis. [p=0.4] {d}Potência multiplica "
        "a base *por ela mesma,* [p=0.2] não pelo expoente."),

    # ================= BLOCO C: EXPOENTE 1 E BASE 1 =================
    dict(id="09", block="um", text=
        "{t}E se o expoente for *um?* [p=0.3] {a}Uma dobra só. [p=0.2] Um fator só. [p=0.4] {b}Então *a elevado a um* é o "
        "próprio *a.* [p=0.3] {c}Sete elevado a um? [p=0.2] *Sete.*"),
    dict(id="10", block="um", text=
        "{t}E se a *base* for o um? [p=0.3] {a}Um vezes um, [p=0.2] vezes um, [p=0.2] vezes um... [p=0.3] {b}não sai do "
        "lugar. [p=0.4] {c}Um elevado a *quinhentos* [p=0.2] continua sendo *um.*"),

    # ================= BLOCO D: A ESCADA E O EXPOENTE ZERO =================
    dict(id="11", block="escada", text=
        "{t}Agora, a pergunta que derruba muita gente: [p=0.3] quanto é *dois elevado a zero?* [p=0.4] {a}Zero fatores? "
        "[p=0.2] Parece que devia dar zero. [p=0.5] {b}Em vez de decorar, [p=0.2] vamos *descobrir,* [p=0.2] com uma escada."),
    dict(id="12", block="escada", text=
        "{t}No degrau de cima, [p=0.2] dois elevado a três, [p=0.2] *oito.* [p=0.4] {a}Desça um degrau: [p=0.2] dois "
        "elevado a dois, [p=0.2] *quatro.* [p=0.3] {b}Mais um: [p=0.2] dois elevado a um, [p=0.2] *dois.* [p=0.4] {c}Repare "
        "no padrão: [p=0.2] cada degrau para baixo *divide por dois.* [p=0.3] {d}Oito, [p=0.2] quatro, [p=0.2] dois."),
    dict(id="13", block="escada", text=
        "{t}Então o próximo degrau é fácil: [p=0.3] {a}dois dividido por dois, [p=0.2] *um.* [p=0.4] {b}Dois elevado a zero "
        "*é um.* [p=0.4] {c}E vale para qualquer base, [p=0.2] menos o zero: [p=0.2] noventa e nove elevado a zero, [p=0.2] "
        "*um.* [p=0.4] {d}O zero fica de fora [p=0.2] porque a escada dele teria que dividir por zero, [p=0.2] e isso não existe. "
        "[p=0.4] {e}Atalho: [p=0.2] viu expoente zero, [p=0.2] com base diferente de zero? [p=0.2] A resposta é *um,* "
        "[p=0.2] sem conta."),

    # ================= BLOCO E: CONTINUANDO A ESCADA — EXPOENTE NEGATIVO =================
    dict(id="14", block="escada", text=
        "{t}E se a escada continuar *descendo?* [p=0.4] {a}Depois do zero, [p=0.2] vem o *menos um.* [p=0.3] {b}Um dividido "
        "por dois: [p=0.2] *um meio.* [p=0.4] {c}Menos dois: [p=0.2] um meio dividido por dois, [p=0.2] *um quarto.* [p=0.4] "
        "{d}Menos três: [p=0.2] *um oitavo.*"),
    dict(id="15", block="negativo", text=
        "{t}Agora, olhe dois degraus lado a lado. [p=0.3] {a}Dois elevado a três é oito. [p=0.2] Dois elevado a menos três "
        "é *um oitavo.* [p=0.4] {b}É o *inverso* do oito! [p=0.4] {c}Essa é a regra: [p=0.2] *a elevado a menos n* [p=0.2] "
        "é *um sobre a elevado a n.* [p=0.4] {d}O sinal de menos no expoente [p=0.2] manda *inverter.* [p=0.4] {e}Atalho: "
        "[p=0.2] inverta a base [p=0.2] e tire o sinal de menos do expoente."),

    # ================= BLOCO F: FRAÇÃO COM EXPOENTE NEGATIVO =================
    dict(id="16", block="fracao", text=
        "{t}E quando a base já é uma fração? [p=0.3] Por exemplo, [p=0.2] *dois terços elevado a menos dois.* [p=0.4] "
        "{a}Inverter uma fração é virar de cabeça para baixo: [p=0.2] dois terços vira *três meios,* [p=0.3] {b}e o expoente "
        "perde o sinal. [p=0.4] {c}Elevar a dois tem apelido: [p=0.2] *ao quadrado,* [p=0.2] que é vezes ela mesma. [p=0.4] "
        "{d}Três vezes três em cima, [p=0.2] *nove.* [p=0.2] Dois vezes dois embaixo, [p=0.2] *quatro.* [p=0.3] {e}*Nove quartos.*"),

    # ================= BLOCO G: NEGATIVO NÃO DEIXA NEGATIVO =================
    dict(id="17", block="nao_negativo", text=
        "{t}E repare numa coisa: [p=0.2] em nenhum degrau da escada apareceu número negativo. [p=0.4] {a}Dois elevado a "
        "menos três [p=0.2] é *um oitavo,* [p=0.2] um número *positivo,* [p=0.2] pequenininho. [p=0.4] {b}Não é menos oito. "
        "[p=0.4] {c}O menos do expoente *não mexe no sinal da resposta.* [p=0.3] {d}Ele só manda inverter."),

    # ================= BLOCO H: REVISÃO RELÂMPAGO DO SINAL =================
    dict(id="18", block="sinal", text=
        "{t}E quando a resposta fica negativa? [p=0.3] Revisão relâmpago da série de Operações. [p=0.4] {a}Base negativa "
        "com expoente *par* dá positivo: [p=0.2] menos dois elevado a quatro, [p=0.2] *dezesseis.* [p=0.4] {b}Com expoente "
        "*ímpar,* [p=0.2] dá negativo: [p=0.2] menos dois elevado a três, [p=0.2] que tem o apelido de *ao cubo,* [p=0.2] "
        "*menos oito.* [p=0.4] {c}Atalho: [p=0.2] os sinais de menos se cancelam em pares. [p=0.4] {d}E o parêntese manda: "
        "[p=0.2] menos três ao quadrado, sem parêntese, [p=0.2] é *menos nove.* [p=0.3] {e}Com parêntese, [p=0.2] *nove.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Quatro contas. [p=0.3] {a}Cinco elevado a zero. [p=0.3] {b}Três elevado a menos dois. [p=0.3] "
        "{c}Um meio elevado a menos um. [p=0.3] {d}E menos um elevado a sete. [p=0.4] {e}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Cinco elevado a zero: [p=0.2] expoente zero, [p=0.2] *um.* [p=0.4] {b}Três elevado a "
        "menos dois: [p=0.2] inverte e tira o menos, [p=0.2] um sobre três ao quadrado, [p=0.2] *um nono.* [p=0.4] {c}Um meio "
        "elevado a menos um: [p=0.2] de cabeça para baixo, [p=0.2] dois sobre um, [p=0.2] *dois.* [p=0.4] {d}Menos um elevado "
        "a sete: [p=0.2] base negativa, [p=0.2] expoente ímpar, [p=0.2] *menos um.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] potência é multiplicar a base por ela mesma. [p=0.5] "
        "{b}Dois: [p=0.2] qualquer número, [p=0.2] menos o zero, [p=0.2] elevado a zero dá um. [p=0.5] {c}Três: [p=0.2] "
        "expoente negativo inverte; [p=0.2] não deixa negativo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dois elevado a três igual a *seis.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque dois vezes três dá seis. [p=0.4] {c}Mas são três dobras: [p=0.2] dois vezes dois "
        "vezes dois, [p=0.2] *oito.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] *a elevado a zero igual a zero.* [p=0.4] {b}Parece certo, [p=0.2] porque o zero costuma zerar "
        "tudo. [p=0.4] {c}Mas a escada mostra: [p=0.2] um degrau abaixo do dois, [p=0.2] vem o *um.*"),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que dois elevado a menos três é *menos oito,* [p=0.2] ou qualquer número negativo. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o sinal de menos está ali, [p=0.2] bem à vista. [p=0.4] {c}Mas o menos do "
        "expoente só manda inverter: [p=0.2] *um oitavo,* [p=0.2] positivo."),

    # ================= QUESTÃO 3 DO MATERIAL =================
    dict(id="25", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}O valor da expressão "
        "[p=0.2] dois terços elevado a menos dois, [p=0.2] *mais* um meio elevado a menos três, [p=0.2] é: [p=0.4] {qa}A: "
        "[p=0.2] menos quarenta e um quartos. [p=0.3] {qb}B: [p=0.2] dezessete trinta e seis avos. [p=0.3] {qc}C: [p=0.2] "
        "vinte e cinco quartos. [p=0.3] {qd}D: [p=0.2] quarenta e um quartos. [p=0.3] {qe}E: [p=0.2] doze. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="questao", text=
        "{t}Vamos resolver, [p=0.2] uma parte de cada vez. [p=0.4] {a}Dois terços elevado a menos dois: [p=0.2] vira de "
        "cabeça para baixo, [p=0.2] três meios ao quadrado, [p=0.2] *nove quartos.* [p=0.4] {b}Um meio elevado a menos três: "
        "[p=0.2] vira dois sobre um, [p=0.2] que é dois, [p=0.2] ao cubo: [p=0.2] *oito.* [p=0.4] {c}Agora a soma. [p=0.2] "
        "Para somar com quartos, [p=0.2] o oito vira trinta e dois quartos, [p=0.2] porque oito vezes quatro é trinta e dois. "
        "[p=0.4] {d}Nove quartos mais trinta e dois quartos: [p=0.2] *quarenta e um quartos.* [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="questao", text=
        "{t}E as outras? [p=0.3] {xa}A A é a armadilha da aula: [p=0.2] o resultado certo com sinal de menos, [p=0.2] de quem "
        "achou que o expoente negativo [p=0.2] deixa o resultado negativo. [p=0.4] {xc}A C acertou os nove quartos, [p=0.2] "
        "mas fez dois ao cubo como dois vezes dois: [p=0.2] um fator a menos. [p=0.4] {xe}A E elevou só o dois, [p=0.2] "
        "sem inverter a fração. [p=0.4] {xb}E a B é menor que um: [p=0.2] impossível, [p=0.2] se só a segunda parte já dá oito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] potência é multiplicar a base por ela mesma. [p=0.5] "
        "{b}Dois: [p=0.2] qualquer número, [p=0.2] menos o zero, [p=0.2] elevado a zero dá um. [p=0.5] {c}Três: [p=0.2] "
        "expoente negativo inverte; [p=0.2] não deixa negativo."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}E quando a expressão mistura várias potências, [p=0.2] como *dois elevado a cinco, [p=0.2] vezes quatro elevado "
        "a três, [p=0.2] dividido por oito ao quadrado?* [p=0.4] {b}Existem *sete regras* que resolvem qualquer uma. "
        "[p=0.4] {c}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que dois elevado a zero dava zero? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
