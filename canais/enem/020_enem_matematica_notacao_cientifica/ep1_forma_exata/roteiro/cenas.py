# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 1 de 6: a forma exata, converter qualquer número e
# algarismos significativos (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seções 02, 03 e 09 (+ Questão 1 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PLACA DE CARRO: só existe UM jeito certo de escrever cada número: um único algarismo (diferente de zero) antes da vírgula.
#   CONTADOR DE CASAS: o expoente conta quantas casas a vírgula andou (liga ao "contador de zeros" da série de Potenciação).
#   CADEIRAS VAZIAS: zeros à esquerda só guardam lugar; não contam como significativos.
# CORREÇÃO do gancho: prompt e material dizem "quatro áreas", mas Matemática, Física, Química, Biologia e Humanas são TRÊS das
#   quatro áreas do ENEM (Linguagens fica fora). A fala diz "Matemática, Ciências da Natureza (Física, Química e Biologia) e até Humanas".
# Desvio: a massa da Terra aparece no gancho (contar zeros é difícil) e é convertida só na Questão 1, para não entregar a resposta
#   no bloco d); os exemplos do bloco d) são 384 400 000 e 0,000 000 42.
# Nós fazemos: 72 000 = 7,2·10⁴ · 0,0035 = 3,5·10⁻³ · 45·10² = 4,5·10³.
# Arredondamento (exemplos nossos): 3,844 com 2 significativos → 3,8 (o seguinte é 4) · 5,97 com 2 significativos → 6,0 (o seguinte é 7).
# QUESTÃO 1 do material (texto idêntico na tela): 5 970 000 000 000 000 000 000 000 kg = 5,97·10²⁴ → C.
#   B (59,7·10²³) e E (0,597·10²⁵) têm o valor certo fora da forma exata; D (5,97·10⁻²⁴) inverteu o sinal (explicações do material).
#   Explicação NOSSA (o material não explica a A): A (5,97·10²¹) contou só os sete grupos de "000" e esqueceu o 9, o 7 e o 0
#   do primeiro grupo.
# Frases-chave (meio e fim, idênticas):
#   1. Um único algarismo, diferente de zero, antes da vírgula.
#   2. Número grande: expoente positivo. Pequeno: negativo.
#   3. Expoente negativo não deixa o número negativo.
# Atalhos (verde): "conte os algarismos depois do primeiro" (número grande) · "conte os zeros da frente, inclusive o de antes da
#   vírgula" (número pequeno) · "maior que 1 → +, menor que 1 → −" · "escreva em notação científica e conte o coeficiente".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Notação científica do zero: a forma exata, a vírgula que anda e os algarismos significativos · Matemática ENEM, ep. 1"

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
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Este assunto aparece em quase toda a prova do ENEM. [p=0.4] {b}Em *Matemática.* [p=0.3] {c}Em *Ciências da "
        "Natureza:* [p=0.2] Física, [p=0.2] Química [p=0.2] e Biologia. [p=0.4] {d}E até em *Humanas.* [p=0.5] {e}Sempre "
        "que surge um número *gigante* [p=0.2] ou *minúsculo,* [p=0.2] ele está lá."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai escrever *qualquer número* em notação científica. [p=0.4] {b}E vai "
        "perceber na hora [p=0.2] quando uma alternativa está escrita *do jeito errado.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido da série de Potenciação. [p=0.3] {a}Dez elevado a três [p=0.2] é *um seguido de três "
        "zeros:* [p=0.2] mil. [p=0.4] {b}E dez elevado a *menos* três [p=0.2] é zero vírgula zero zero um: [p=0.2] três casas "
        "depois da vírgula, [p=0.2] com o um na última. [p=0.4] {c}Um número *pequeno,* [p=0.2] mas positivo."),

    # ================= CONCRETO: NÚMEROS ENORMES E MINÚSCULOS =================
    dict(id="04", block="zeros", text=
        "{t}Agora olhe este número: [p=0.3] a massa da Terra, [p=0.2] em quilos. [p=0.4] {a}Cinco, nove, sete, [p=0.2] e "
        "depois *zeros.* [p=0.2] Muitos zeros. [p=0.5] {b}Quantos? [p=0.4] Você teria que contar um por um, [p=0.2] e é aí que "
        "a gente erra. [p=0.5] {c}No outro extremo, [p=0.2] o tamanho de um vírus, [p=0.2] em metros: [p=0.2] zero vírgula, "
        "[p=0.2] e uma fila de zeros antes do um. [p=0.5] {d}Contar zeros [p=0.2] é o jeito mais fácil de errar uma conta."),

    # ================= BLOCO A: A FORMA EXATA =================
    dict(id="05", block="forma", text=
        "{t}Para não contar zero nenhum, [p=0.2] existe a *notação científica:* [p=0.3] um jeito padronizado de escrever "
        "números muito grandes ou muito pequenos. [p=0.5] {a}A forma é sempre esta: [p=0.2] *a vezes dez elevado a n.* "
        "[p=0.4] {b}O *a* se chama *coeficiente:* [p=0.2] é o número da frente. [p=0.4] {c}O *n* é o *expoente:* [p=0.2] o "
        "numerozinho no alto do dez, [p=0.2] e ele tem que ser um número *inteiro,* [p=0.2] sem vírgula."),
    dict(id="06", block="forma", text=
        "{t}E o coeficiente tem uma regra rígida. [p=0.3] {a}Ele fica entre um e dez: [p=0.2] *pode* ser um, [p=0.2] mas "
        "*não pode* chegar a dez. [p=0.4] {b}As barrinhas em volta do *a* [p=0.2] querem dizer: [p=0.2] olhe o número sem o "
        "sinal. [p=0.4] {c}Na prática, [p=0.2] isso significa *um único algarismo,* [p=0.2] diferente de zero, [p=0.2] antes "
        "da vírgula."),
    dict(id="07", block="placa", text=
        "{t}Pense numa *placa de carro.* [p=0.3] {a}Ela tem um formato fixo: [p=0.2] letras e números, [p=0.2] sempre na "
        "mesma ordem. [p=0.4] {b}Por isso cada carro tem *um só* jeito certo de ser escrito. [p=0.4] {c}A notação científica "
        "é igual: [p=0.2] cada número tem *uma única* escrita certa. [p=0.4] {d}Um algarismo antes da vírgula, [p=0.2] "
        "nem menos, [p=0.2] nem mais."),

    # ================= BLOCO B: POR QUE A RESTRIÇÃO EXISTE =================
    dict(id="08", block="tabela", text=
        "{t}Mas por que tanta regra? [p=0.3] {a}Porque sem ela, [p=0.2] o mesmo número teria várias escritas, [p=0.2] e a "
        "prova *cobra* justamente a certa. [p=0.5] {b}Três vírgula oitenta e quatro vezes dez elevado a oito? [p=0.2] Um "
        "algarismo antes da vírgula: [p=0.2] *é* notação científica. [p=0.4] {c}Vinte e cinco vezes dez elevado a três? "
        "[p=0.2] *Não:* [p=0.2] o vinte e cinco passou de dez. [p=0.4] {d}Zero vírgula cinco vezes dez elevado a quatro? "
        "[p=0.2] *Também não:* [p=0.2] o coeficiente ficou abaixo de um. [p=0.4] {e}E um vezes dez elevado a menos seis? "
        "[p=0.2] *É:* [p=0.2] o um é permitido."),
    dict(id="09", block="tabela", text=
        "{t}E como consertar as erradas? [p=0.3] {a}Isso se chama *renormalizar:* [p=0.2] arrumar o número para a forma "
        "exata, [p=0.2] sem mudar o valor. [p=0.5] {b}Vinte e cinco vira dois vírgula cinco: [p=0.2] o coeficiente ficou dez "
        "vezes *menor,* [p=0.2] então o expoente *sobe* um. [p=0.3] {c}Dois vírgula cinco vezes dez elevado a quatro. [p=0.5] "
        "{d}Zero vírgula cinco vira cinco: [p=0.2] ficou dez vezes *maior,* [p=0.2] então o expoente *desce* um. [p=0.3] "
        "{e}Cinco vezes dez elevado a três."),

    # ================= BLOCO C: EXPOENTE NEGATIVO, NÚMERO POSITIVO =================
    dict(id="10", block="negativo", text=
        "{t}E quando o expoente é negativo, [p=0.2] o número fica negativo? [p=0.5] {a}*Não.* [p=0.3] Dez elevado a menos "
        "três [p=0.2] é zero vírgula zero zero um. [p=0.3] {b}Pequeno, [p=0.2] mas *positivo.* [p=0.4] {c}O sinal do expoente "
        "não fala do sinal do número. [p=0.3] {d}Ele diz *para que lado a vírgula anda.*"),

    # ================= BLOCO D: A REGRA ÚNICA DE CONVERSÃO =================
    dict(id="11", block="virgula", text=
        "{t}E como transformar qualquer número? [p=0.3] {a}Existe uma regra só: [p=0.2] *ande com a vírgula* até sobrar "
        "um algarismo antes dela. [p=0.4] {b}O expoente é o *contador de casas* que a vírgula andou. [p=0.5] {c}A distância "
        "da Terra à Lua, [p=0.2] em metros: [p=0.2] trezentos e oitenta e quatro milhões e quatrocentos mil. [p=0.4] {d}A "
        "vírgula está escondida no fim. [p=0.3] {e}Ela anda para a *esquerda,* [p=0.2] casa por casa, [p=0.2] até parar "
        "depois do três: [p=0.3] {f}*oito* casas. [p=0.4] {g}Três vírgula oito quatro quatro vezes dez elevado a *oito.*"),
    dict(id="12", block="virgula", text=
        "{t}Agora um número pequeno: [p=0.2] zero vírgula, [p=0.2] seis zeros, [p=0.2] quarenta e dois. [p=0.4] {a}A vírgula "
        "anda para a *direita,* [p=0.2] até passar o quatro: [p=0.3] {b}*sete* casas. [p=0.4] {c}Quatro vírgula dois vezes "
        "dez elevado a *menos* sete. [p=0.5] {d}Viu a regra do sinal? [p=0.3] Vírgula para a esquerda, [p=0.2] número "
        "grande, [p=0.2] expoente *positivo.* [p=0.3] {e}Vírgula para a direita, [p=0.2] número pequeno, [p=0.2] expoente "
        "*negativo.*"),
    dict(id="13", block="atalho_conta", text=
        "{t}E dois atalhos para contar mais rápido. [p=0.4] {a}Número grande: [p=0.2] conte os algarismos *depois do "
        "primeiro.* [p=0.3] Trezentos e oitenta e quatro milhões e quatrocentos mil tem nove algarismos: [p=0.2] tirando o "
        "primeiro, [p=0.2] *oito.* [p=0.5] {b}Número pequeno: [p=0.2] conte os zeros *da frente,* [p=0.2] incluindo o zero "
        "antes da vírgula. [p=0.3] {c}No zero vírgula zero zero zero zero zero zero quarenta e dois, [p=0.2] são *sete.*"),

    # ================= BLOCO E: A CONFERÊNCIA DE DOIS SEGUNDOS =================
    dict(id="14", block="conferencia", text=
        "{t}E antes de seguir, [p=0.2] a conferência de *dois segundos.* [p=0.4] {a}Olhe o número original. [p=0.3] {b}Ele é "
        "*maior* que um? [p=0.2] O expoente tem que ser *positivo.* [p=0.4] {c}É *menor* que um? [p=0.2] O expoente tem que "
        "ser *negativo.* [p=0.4] {d}Isso pega o erro de sinal na hora, [p=0.2] sem recontar casa nenhuma."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Escreva em notação científica: [p=0.2] setenta e dois mil. [p=0.3] {b}Depois, [p=0.2] zero "
        "vírgula zero zero trinta e cinco. [p=0.3] {c}E corrija esta escrita: [p=0.2] quarenta e cinco vezes dez elevado a "
        "dois. [p=0.4] {d}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Setenta e dois mil: [p=0.2] a vírgula anda quatro casas para a esquerda. [p=0.2] "
        "*Sete vírgula dois vezes dez elevado a quatro.* [p=0.4] {b}Zero vírgula zero zero trinta e cinco: [p=0.2] três "
        "casas para a direita. [p=0.2] *Três vírgula cinco vezes dez elevado a menos três.* [p=0.4] {c}Quarenta e cinco "
        "passou de dez: [p=0.2] vira quatro vírgula cinco, [p=0.2] e o expoente sobe um. [p=0.2] *Quatro vírgula cinco vezes "
        "dez elevado a três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] um único algarismo, [p=0.2] diferente de zero, [p=0.2] "
        "antes da vírgula. [p=0.5] {b}Dois: [p=0.2] número grande, [p=0.2] expoente positivo. [p=0.2] Pequeno, [p=0.2] "
        "negativo. [p=0.5] {c}Três: [p=0.2] expoente negativo não deixa o número negativo."),

    # ================= BLOCO F: ALGARISMOS SIGNIFICATIVOS =================
    dict(id="18", block="signif", text=
        "{t}E agora, uma ideia que cai muito em Física e Química: [p=0.3] *algarismos significativos.* [p=0.4] {a}São os "
        "algarismos que *carregam informação* de uma medida: [p=0.2] os que contam de verdade. [p=0.5] {b}Regra um: [p=0.2] "
        "todo algarismo *diferente de zero* conta. [p=0.4] {c}Regra dois: [p=0.2] zero *entre* algarismos que contam, "
        "[p=0.2] também conta. [p=0.4] {d}Regra três: [p=0.2] zero *à esquerda* não conta. [p=0.4] {e}Regra quatro: [p=0.2] "
        "zero *à direita,* [p=0.2] depois da vírgula, [p=0.2] conta."),
    dict(id="19", block="signif", text=
        "{t}Pense nos zeros à esquerda como *cadeiras vazias:* [p=0.3] eles só guardam lugar. [p=0.4] {a}Zero vírgula zero "
        "zero quatrocentos e vinte. [p=0.3] {b}Os três zeros da frente são cadeiras vazias: [p=0.2] não contam. [p=0.4] {c}O "
        "quatro e o dois contam, [p=0.2] {d}e o zero do final também, [p=0.2] porque está depois da vírgula. [p=0.3] *Três* "
        "significativos. [p=0.5] {e}Já mil e dois: [p=0.2] os dois zeros estão *no meio,* [p=0.2] então contam. [p=0.3] "
        "*Quatro* significativos."),

    # ================= BLOCO G: A VANTAGEM ESCONDIDA =================
    dict(id="20", block="vantagem", text=
        "{t}E a notação científica tem uma vantagem escondida. [p=0.4] {a}Quatro mil e duzentos: [p=0.2] quantos "
        "significativos? [p=0.3] Pode ser dois, [p=0.2] três [p=0.2] ou quatro. [p=0.2] Não dá para saber. [p=0.4] {b}Mas "
        "quatro vírgula vinte vezes dez elevado a três [p=0.2] tem exatamente *três,* [p=0.2] sem discussão. [p=0.4] "
        "{c}No coeficiente, [p=0.2] *todos* os algarismos contam. [p=0.4] {d}Atalho: [p=0.2] na dúvida, [p=0.2] escreva "
        "em notação científica [p=0.2] e conte o coeficiente."),

    # ================= BLOCO H: ARREDONDAMENTO =================
    dict(id="21", block="arredondar", text=
        "{t}E quando a questão pede menos algarismos? [p=0.3] {a}Aí você *arredonda:* [p=0.2] corta os algarismos que "
        "sobram e ajusta o último que fica. [p=0.4] {b}A regra é olhar o algarismo *seguinte.* [p=0.2] Menor que cinco, "
        "[p=0.2] *mantém.* [p=0.2] Cinco ou mais, [p=0.2] *soma um.* [p=0.5] {c}Três vírgula oito quatro quatro, [p=0.2] com "
        "dois significativos: [p=0.2] o seguinte é quatro, [p=0.2] fica *três vírgula oito.* [p=0.4] {d}Cinco vírgula noventa "
        "e sete: [p=0.2] o seguinte é sete, [p=0.2] o nove vira dez [p=0.2] e fica *seis vírgula zero.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] aceitar vinte e cinco vezes dez elevado a três "
        "[p=0.2] como notação científica. [p=0.4] {b}Parece certo, [p=0.2] porque o número está certo. [p=0.4] {c}Mas a "
        "*escrita* não: [p=0.2] dois vírgula cinco vezes dez elevado a quatro."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] errar o *sinal* do expoente. [p=0.4] {b}Parece certo, [p=0.2] porque você contou as casas "
        "direitinho. [p=0.4] {c}Mas faça a conferência de dois segundos: [p=0.2] maior que um, [p=0.2] *positivo.*"),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que dez elevado a menos três [p=0.2] é um número *negativo.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o sinal de menos está ali. [p=0.4] {c}Mas é zero vírgula zero zero um: [p=0.2] *positivo.*"),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] contar os zeros à esquerda [p=0.2] como significativos. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "eles estão escritos ali. [p=0.4] {c}Mas são cadeiras vazias: [p=0.2] *não contam.*"),

    # ================= QUESTÃO 1 DO MATERIAL =================
    dict(id="26", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}A massa da Terra é de "
        "aproximadamente [p=0.2] cinco, nove, sete, [p=0.2] seguido de vinte e dois zeros, [p=0.2] em quilos. [p=0.3] Em "
        "notação científica, [p=0.2] esse valor é: [p=0.4] {qa}A: [p=0.2] cinco vírgula noventa e sete vezes dez elevado a "
        "vinte e um. [p=0.3] {qb}B: [p=0.2] cinquenta e nove vírgula sete vezes dez elevado a vinte e três. [p=0.3] {qc}C: "
        "[p=0.2] cinco vírgula noventa e sete vezes dez elevado a vinte e quatro. [p=0.3] {qd}D: [p=0.2] cinco vírgula noventa "
        "e sete vezes dez elevado a *menos* vinte e quatro. [p=0.3] {qe}E: [p=0.2] zero vírgula quinhentos e noventa e sete "
        "vezes dez elevado a vinte e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="questao", text=
        "{t}Vamos resolver. [p=0.3] {a}A vírgula está escondida no fim do número, [p=0.2] e precisa parar *depois do cinco.* "
        "[p=0.4] {b}Pelo atalho, [p=0.2] conte os algarismos depois do primeiro: [p=0.2] o nove, [p=0.2] o sete [p=0.2] e os "
        "vinte e dois zeros. [p=0.3] {c}*Vinte e quatro* casas. [p=0.4] {d}A Terra é enorme, [p=0.2] então o expoente é "
        "*positivo:* [p=0.2] cinco vírgula noventa e sete vezes dez elevado a vinte e quatro. [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="questao", text=
        "{t}E as outras? [p=0.3] {xb}A B e a E [p=0.2] têm o valor *certo,* [p=0.2] mas não estão na forma exata: "
        "[p=0.2] cinquenta e nove vírgula sete passou de dez, [p=0.2] e zero vírgula quinhentos e noventa e sete ficou abaixo "
        "de um. [p=0.4] {xd}A D inverteu o sinal: [p=0.2] a Terra pesaria quase nada. [p=0.4] {xa}E a A contou só os grupos "
        "de três zeros, [p=0.2] e esqueceu o nove, [p=0.2] o sete [p=0.2] e o zero do primeiro grupo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] um único algarismo, [p=0.2] diferente de zero, "
        "[p=0.2] antes da vírgula. [p=0.5] {b}Dois: [p=0.2] número grande, [p=0.2] expoente positivo. [p=0.2] Pequeno, "
        "[p=0.2] negativo. [p=0.5] {c}Três: [p=0.2] expoente negativo não deixa o número negativo."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}E para fazer *contas?* [p=0.4] {b}Multiplicar e dividir em notação científica é fácil, [p=0.3] {c}mas tem um "
        "passo que quase todo mundo *esquece.* [p=0.4] {d}Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantos zeros você contou na massa da Terra? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
