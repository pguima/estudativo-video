# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 3 de 6: o caminho de volta (f(x) = k) e as funções por partes
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seção 05 ("O caminho de volta" e
#   "Funções definidas por partes") + Questões 9 e 2 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   IDA × VOLTA: dão o x → calcule f(x) (caminho de ida); dão o y → monte f(x) = k (caminho de volta). A MÁQUINA do ep. 1
#     rodando ao contrário: a saída R$ 30 entra pela bandeja e a máquina "rebobina" até mostrar a entrada 10 km.
#   AS GAVETAS: na função por partes a regra muda conforme a faixa; antes de calcular, descubra em que gaveta o x está.
#   O RELÓGIO DO ESTACIONAMENTO: "ou fração" = começou a hora, pagou a hora inteira.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos:
#   Bloco a usa o próprio táxi da Q9 (que é "eu faço", por desenho do usuário: gancho e seção 05 são a mesma conta).
#   Bloco d: 2 h 15 min → 10 + 2 · 4 = R$ 18,00 (seção 05). A Q2 (3 h 20 min → R$ 22,00) é a "você faz" e só aparece no fim.
#   Nós fazemos (prompt): academia C(m) = 50 + 80m, pagou 530 → 80m = 480 → m = 6.
#   ERROS 2, 3 e 4 com número NOSSO (1 h 30 min), para não entregar a Q2 e não repetir o 22 como valor errado:
#     certo 10 + 1 · 4 = 14 · ignorar a fração: 10 · proporcional: 10 + 4 · 0,5 = 12 · 1ª hora como adicional: 10 + 4 · 2 = 18.
# QUESTÃO 9 (eu faço): 5 + 2,5d = 30 → 2,5d = 25 → d = 10 → B. Material: E = P(30) = 80; C = 30 ÷ 2,5 = 12 (esquece o fixo);
#   D = (30 + 5) ÷ 2,5 = 14 (soma o fixo); A = 30 ÷ 5 = 6 (divide pela tarifa fixa). Conferência: 5 + 2,5 · 10 = 30.
# QUESTÃO 2 (você faz): depois da 1ª hora restam 2 h 20 min = 2 adicionais + 1 fração = 3 → 10 + 3 · 4 = 22 → D. Material:
#   A 18 ignora a fração; B 18,80 = 10 + 4 · 2,2 (lê 3 h 20 como 3,2 h); C 19,33 = 10 + 4 · 2,33 (proporcional);
#   E 26 = 10 + 4 · 4 (1ª hora também como adicional).
# Atalhos (verde): caminho de volta = desfazer de trás para frente (tira o fixo, divide pela tarifa) e conferir substituindo ·
#   estacionamento: tire a 1ª hora, ARREDONDE O RESTO PARA CIMA, multiplique pela tarifa adicional e some a 1ª hora.
# Frases-chave (meio e fim, idênticas): 1. Dão o x: calcule. Dão o y: resolva a equação. 2. Em função por partes, primeiro ache
#   a faixa. 3. Hora ou fração: começou a hora, paga a hora.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Pagou R$ 30 de táxi: andou quantos km? O caminho de volta · Matemática ENEM, Conceito de função, episódio 3"

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
        "{a}O táxi cobra *P de d* [p=0.2] igual a cinco [p=0.2] mais dois e meio vezes d. [p=0.4] {b}Você pagou *trinta "
        "reais.* [p=0.4] {c}Quem calcula *P de trinta* [p=0.2] acha *oitenta reais,* [p=0.2] o preço de uma corrida de "
        "trinta quilômetros, [p=0.3] {d}e marca a alternativa errada. [p=0.5] {e}A pergunta era outra: [p=0.3] *quantos "
        "quilômetros custam trinta reais?*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber quando *calcular* f de x [p=0.3] {b}e quando *resolver* f de x "
        "igual a k, [p=0.4] {c}e vai calcular qualquer tarifa por faixa [p=0.2] sem cair no *ou fração.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] *f de x* é a saída quando a entrada é x. "
        "[p=0.4] {b}E, da série de equações: [p=0.2] em cinco mais dois e meio d igual a trinta, [p=0.3] {c}tire cinco "
        "dos dois lados: [p=0.2] vinte e cinco. [p=0.3] {d}Divida por dois e meio: [p=0.2] *d igual a dez.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em duas cenas do dia a dia. [p=0.3] {a}Primeira: [p=0.2] você pega um táxi, [p=0.2] guarda o *recibo* "
        "[p=0.2] e só sabe *quanto pagou.* [p=0.2] Quer descobrir *quanto andou.* [p=0.5] {b}Segunda: [p=0.2] a placa "
        "de um estacionamento. [p=0.2] Primeira hora, [p=0.2] *dez reais.* [p=0.2] Hora adicional *ou fração,* [p=0.2] "
        "*quatro reais.* [p=0.4] {c}As duas escondem uma pegadinha."),

    # ================= BLOCO A: IDA × VOLTA =================
    dict(id="05", block="ida", text=
        "{t}Qual é a diferença entre ir e voltar numa função? [p=0.4] {a}O *caminho de ida* [p=0.2] é quando o enunciado "
        "*dá o x* [p=0.2] e pede o resultado. [p=0.4] {b}Andei dez quilômetros. [p=0.2] Quanto paguei? [p=0.3] {c}P de "
        "dez: [p=0.2] cinco mais dois e meio vezes dez, [p=0.2] cinco mais vinte e cinco, [p=0.2] *trinta reais.* "
        "[p=0.4] {d}A máquina do episódio um, normal: [p=0.2] entra dez, [p=0.2] sai trinta."),
    dict(id="06", block="volta", text=
        "{t}E quando o enunciado dá a *saída?* [p=0.4] {a}Esse é o *caminho de volta:* [p=0.2] dão o y [p=0.2] e pedem "
        "o x que produziu esse y. [p=0.4] {b}Aí você monta uma equação, [p=0.2] a *equação f de x igual a k:* [p=0.2] a "
        "fórmula igualada ao valor dado. [p=0.4] {c}Paguei trinta: [p=0.2] *cinco mais "
        "dois e meio d igual a trinta.* [p=0.4] {d}É a máquina *rebobinando:* [p=0.2] o trinta entra pela saída "
        "[p=0.2] e ela devolve a entrada: [p=0.2] *dez quilômetros.*"),
    dict(id="07", block="atalho_volta", text=
        "{t}Tem um jeito rápido de fazer a volta? [p=0.4] {a}Tem. [p=0.2] *Desfaça de trás para frente.* [p=0.3] A "
        "fórmula multiplica por dois e meio e depois soma cinco. [p=0.4] {b}Na volta, [p=0.2] ao contrário: [p=0.2] *tira o cinco,* [p=0.2] sobra vinte e cinco. [p=0.2] *Divide por dois e meio,* [p=0.2] "
        "dá dez. [p=0.4] {c}E confira substituindo: [p=0.2] P de dez [p=0.2] dá trinta? [p=0.2] Dá."),

    # ================= BLOCO B: POR QUE 80 ENGANA =================
    dict(id="08", block="oitenta", text=
        "{t}Então de onde saiu o oitenta do começo? [p=0.4] {a}Quem calcula *P de trinta* [p=0.2] colocou o trinta *no "
        "lugar do d.* [p=0.3] Cinco mais setenta e cinco, [p=0.2] oitenta. [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "trinta está no enunciado [p=0.2] e calcular é o que a gente mais treina. [p=0.4] {c}Só que "
        "oitenta reais é o preço de uma corrida de *trinta quilômetros.* [p=0.4] {d}Por isso, [p=0.2] antes de qualquer conta, [p=0.2] escreva na margem: "
        "[p=0.2] *dão o x* [p=0.2] ou *dão o y.*"),

    # ================= BLOCO C: FUNÇÃO POR PARTES =================
    dict(id="09", block="partes", text=
        "{t}E se a regra da função *mudar no meio do caminho?* [p=0.4] {a}Isso é uma *função definida por partes:* "
        "[p=0.2] a regra de cálculo muda [p=0.2] conforme a *faixa* em que o x está. [p=0.4] {b}*Faixa* é um intervalo de "
        "valores: [p=0.2] até uma hora, [p=0.2] de uma a duas, [p=0.2] e assim por diante. [p=0.4] {c}Pense num armário "
        "de *gavetas:* [p=0.2] cada gaveta guarda uma regra. [p=0.3] {d}Antes de calcular, [p=0.2] descubra *em que "
        "gaveta o x está.*"),

    # ================= BLOCO D: O ESTACIONAMENTO =================
    dict(id="10", block="fracao", text=
        "{t}E o que quer dizer *hora ou fração?* [p=0.4] {a}*Fração* de hora é um pedaço de hora: [p=0.2] cinco minutos, "
        "[p=0.2] quinze, [p=0.2] quarenta. [p=0.4] {b}A regra diz: [p=0.2] cada hora adicional, [p=0.2] *ou qualquer "
        "pedaço dela,* [p=0.2] custa quatro reais. [p=0.4] {c}É o relógio do estacionamento: [p=0.2] *começou a hora, "
        "[p=0.2] pagou a hora inteira.*"),
    dict(id="11", block="estac", text=
        "{t}Quanto paga quem fica *duas horas e quinze minutos?* [p=0.4] {a}Primeiro, [p=0.2] a primeira hora: [p=0.2] "
        "*dez reais.* [p=0.4] {b}Depois dela, [p=0.2] sobra uma hora e quinze. [p=0.2] Uma hora adicional *completa,* "
        "[p=0.2] quatro reais. [p=0.4] {c}E os quinze minutos? [p=0.2] São uma *fração:* [p=0.2] a hora começou, [p=0.2] "
        "então conta como hora. [p=0.2] Mais quatro reais. [p=0.4] {d}Dez mais duas vezes quatro: [p=0.2] *dezoito "
        "reais.*"),
    dict(id="12", block="atalho_estac", text=
        "{t}O atalho em três passos. [p=0.3] {a}Primeiro: [p=0.2] *tire a primeira hora.* [p=0.3] "
        "{b}Segundo: [p=0.2] o tempo que sobrou, [p=0.2] *arredonde para cima,* [p=0.2] para a hora inteira seguinte. "
        "[p=0.2] Uma hora e quinze vira *duas.* [p=0.3] {c}Terceiro: [p=0.2] multiplique pela tarifa adicional [p=0.2] e "
        "some a primeira hora. [p=0.2] Dez mais duas vezes quatro, [p=0.2] dezoito."),

    # ================= BLOCO E: OUTRAS FUNÇÕES POR PARTES =================
    dict(id="13", block="outras", text=
        "{t}Onde mais aparece função por partes? [p=0.4] {a}Na *conta de água:* [p=0.2] cada faixa de consumo "
        "tem um preço. [p=0.3] {b}Na *conta de energia,* [p=0.2] também por faixa. "
        "[p=0.3] {c}E no *imposto,* [p=0.2] em que a alíquota, [p=0.2] a porcentagem cobrada, [p=0.2] muda conforme a "
        "renda. [p=0.4] {d}Série própria mais adiante. [p=0.2] Por enquanto: [p=0.2] *ache a gaveta.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma academia cobra *cinquenta reais* de matrícula [p=0.2] mais *oitenta reais* por mês. "
        "[p=0.2] C de m [p=0.2] igual a cinquenta mais oitenta m. [p=0.4] {b}Uma pessoa pagou *quinhentos e trinta reais* "
        "no total. [p=0.2] Quantos meses? [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Deram o total, [p=0.2] a *saída.* [p=0.2] Na margem: [p=0.2] *dão o y.* [p=0.2] "
        "Caminho de volta. [p=0.4] {b}Cinquenta mais oitenta m [p=0.2] igual a quinhentos e trinta. [p=0.3] Tira a "
        "matrícula: [p=0.2] oitenta m [p=0.2] igual a *quatrocentos e oitenta.* [p=0.4] {c}Divide por oitenta: [p=0.2] "
        "*m igual a seis meses.* [p=0.4] {d}Conferindo: [p=0.2] oitenta vezes seis, [p=0.2] quatrocentos e oitenta, "
        "[p=0.2] mais cinquenta, [p=0.2] quinhentos e trinta. [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dão o x: [p=0.2] calcule. [p=0.2] Dão o y: [p=0.2] "
        "resolva a equação. [p=0.5] {b}Dois: [p=0.2] em função por partes, [p=0.2] primeiro ache a faixa. [p=0.5] "
        "{c}Três: [p=0.2] hora ou fração: [p=0.2] começou a hora, [p=0.2] paga a hora."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] calcular *f de trinta* [p=0.2] quando o "
        "enunciado dá *f de x igual a trinta.* [p=0.4] {b}Parece certo, [p=0.2] porque o trinta está ali, pronto."
        " [p=0.4] {c}Mas o trinta é a *saída.* [p=0.2] Monte a equação [p=0.2] e resolva."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] *ignorar a fração.* [p=0.2] Quem fica uma hora e meia [p=0.2] paga só os dez reais da "
        "primeira hora. [p=0.4] {b}Parece certo, [p=0.2] porque meia hora não chega a ser uma hora. [p=0.4] {c}Mas a "
        "regra diz *ou fração:* [p=0.2] a segunda hora começou. [p=0.2] Dez mais quatro, [p=0.2] *catorze reais.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] cobrar a fração *proporcionalmente.* [p=0.2] Meia hora, [p=0.2] metade de quatro, [p=0.2] "
        "dois reais: [p=0.2] total de doze. [p=0.4] {b}Parece certo, [p=0.2] porque parece justo."
        " [p=0.4] {c}Mas *ou fração* quer dizer hora inteira. [p=0.2] Continua *catorze.*"),
    dict(id="20", block="erros", text=
        "{a}Quarto: [p=0.2] cobrar a *primeira hora* como se fosse adicional. [p=0.2] Uma hora e meia vira duas horas "
        "de quatro reais, [p=0.2] mais os dez: [p=0.2] dezoito. [p=0.4] {b}Parece certo, [p=0.2] porque são duas horas "
        "começadas. [p=0.4] {c}Mas a primeira hora já está paga nos dez reais. "
        "[p=0.2] *Tire a primeira hora antes de contar.*"),

    # ================= QUESTÃO 9 (EU FAÇO) =================
    dict(id="21", block="q9", text=
        "{t}Uma questão do material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}O "
        "preço de uma corrida de táxi é *P de d* [p=0.2] igual a cinco mais dois e meio d, [p=0.2] d em "
        "quilômetros. [p=0.2] Um passageiro pagou *trinta reais.* [p=0.2] A distância percorrida foi de: [p=0.4] {qa}A: "
        "[p=0.2] seis. [p=0.3] {qb}B: [p=0.2] dez. [p=0.3] {qc}C: [p=0.2] doze. [p=0.3] {qd}D: [p=0.2] catorze. [p=0.3] "
        "{qe}E: [p=0.2] oitenta quilômetros. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q9", text=
        "{t}Primeiro, [p=0.2] a margem: [p=0.2] deram o preço, [p=0.2] a saída. [p=0.2] *Dão o y.* [p=0.4] {a}Cinco mais "
        "dois e meio d [p=0.2] igual a trinta. [p=0.2] Tira o cinco: [p=0.2] dois e meio d [p=0.2] igual a vinte e "
        "cinco. [p=0.3] {b}Divide por dois e meio: [p=0.2] *d igual a dez.* [p=0.4] {c}Conferindo: [p=0.2] P de dez, "
        "trinta. [p=0.3] {ok}*Letra B!*"),
    dict(id="23", block="q9", text=
        "{t}E as outras? [p=0.3] {xe}A E, [p=0.2] oitenta, [p=0.2] calculou *P de trinta:* [p=0.2] a pegadinha do "
        "começo. [p=0.4] {xc}A C dividiu trinta por dois e meio [p=0.2] e *esqueceu* os cinco fixos. [p=0.4] {xd}A D "
        "*somou* os cinco [p=0.2] em vez de tirar. [p=0.4] {xa}E a A [p=0.2] dividiu trinta pela tarifa fixa, [p=0.2] "
        "o cinco."),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="24", block="q2", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um estacionamento cobra *dez reais* pela primeira hora [p=0.2] e *quatro reais* "
        "por hora adicional ou fração de hora. [p=0.2] Um cliente deixou o carro por *três horas e vinte minutos.* "
        "[p=0.2] Ele pagou: [p=0.4] {qa}A: [p=0.2] dezoito reais. [p=0.3] {qb}B: [p=0.2] dezoito e oitenta. [p=0.3] "
        "{qc}C: [p=0.2] dezenove e trinta e três. [p=0.3] {qd}D: [p=0.2] vinte e dois. [p=0.3] {qe}E: [p=0.2] vinte e "
        "seis reais. [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="25", block="q2", text=
        "{t}Conferindo. [p=0.2] Dão o x, [p=0.2] o tempo: [p=0.2] é só calcular, [p=0.2] na gaveta certa. [p=0.4] "
        "{a}Tira a primeira hora: [p=0.2] dez reais. [p=0.2] Sobram *duas horas e vinte.* [p=0.4] {b}Duas horas "
        "completas [p=0.2] e uma fração, [p=0.2] que conta como hora: [p=0.2] *três horas adicionais.* [p=0.4] {c}Dez "
        "mais três vezes quatro: [p=0.2] *vinte e dois reais.* [p=0.3] {ok}*Letra D!*"),
    dict(id="26", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A, [p=0.2] dezoito, [p=0.2] *ignorou* os vinte minutos. [p=0.4] {xb}A B leu três "
        "horas e vinte [p=0.2] como *três vírgula dois* [p=0.2] e cobrou proporcional. [p=0.4] {xc}A C cobrou "
        "proporcional as duas horas e vinte. [p=0.4] {xe}E a E [p=0.2] cobrou a *primeira hora* também como "
        "adicional: [p=0.2] quatro horas de quatro reais [p=0.2] mais os dez."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dão o x: [p=0.2] calcule. [p=0.2] Dão o y: "
        "[p=0.2] resolva a equação. [p=0.5] {b}Dois: [p=0.2] em função por partes, [p=0.2] primeiro ache a faixa. "
        "[p=0.5] {c}Três: [p=0.2] hora ou fração: [p=0.2] começou a hora, [p=0.2] paga a hora."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Uma circunferência desenhada no papel [p=0.2] é gráfico de função? [p=0.5] {b}Existe um teste de *um "
        "segundo,* [p=0.2] feito com uma régua em pé. [p=0.5] {c}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já pagou hora cheia por poucos minutos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
