# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 4 de 7: MMC — quando as coisas voltam a coincidir (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seção 08 + Questões 1 e 5 da seção 12.
#   MDC NÃO é ensinado aqui (próximo episódio).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: MMC é o próximo REENCONTRO — cada coisa anda no seu ritmo, as tabuadas vão crescendo, e o MMC é o
#   primeiro número em que as tabuadas se encontram (linha do tempo com marcas coloridas que acendem juntas).
# Lidos EXATAMENTE como no material: definição (cena 07), regra da fatoração (09), palavras-chave (14), checagem (15),
#   enunciados e alternativas das Questões 1 e 5.
# Erros das alternativas (não estão todos no material): Q1 A = 7h = somar os intervalos (12 + 18 + 30 = 60 min);
#   Q5 E = 60 = parou no MMC (material); Q5 A = 6 = dividir 60 por 10 sem converter minutos em segundos.
# Frases-chave (meio e fim, idênticas):
#   1. Coisas que se repetem e se reencontram: MMC.
#   2. Todos os fatores, maior expoente.
#   3. Pediram "quantas vezes"? Ainda falta dividir.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "MMC: quando as coisas voltam a coincidir — Matemática ENEM, Divisibilidade episódio 4"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Nas contas, fale devagar e com clareza, como quem raciocina junto com o aluno. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "MMC": "M M C",
    "MDC": "M D C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Ônibus, [p=0.2] {b}lâmpadas, [p=0.2] {c}engrenagens, [p=0.2] {d}remédios: [p=0.3] quando a questão do ENEM fala de "
        "coisas que se repetem [p=0.2] e voltam a acontecer *juntas,* [p=0.3] {e}a resposta é sempre a mesma ferramenta. [p=0.4] "
        "{f}E ela vale ponto quase todo ano."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular o MMC de *três jeitos* [p=0.4] {b}e não vai cair na pegadinha do "
        "*quantas vezes.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, duas lembranças rápidas. [p=0.3] {a}*Múltiplo* é a tabuada: [p=0.2] os múltiplos de seis são seis, doze, "
        "dezoito, vinte e quatro, [p=0.2] e não acabam. [p=0.4] {b}E *fatorar* é achar a receita do número: [p=0.2] quais "
        "primos, os tijolos, [p=0.2] e quantos de cada. [p=0.3] {c}Doze, por exemplo, [p=0.2] é dois ao quadrado vezes três."),

    # ================= BLOCO A: A LINHA DO TEMPO =================
    dict(id="04", block="remedios", text=
        "{t}Agora, uma pergunta. [p=0.3] {a}Uma pessoa toma um remédio de *seis em seis* horas [p=0.2] {b}e outro de *oito em "
        "oito* horas. [p=0.4] {c}Ela tomou os dois juntos agora. [p=0.3] Quando vai tomar os dois juntos de novo? [p=0.5] "
        "{d}O tempo entre uma dose e a próxima [p=0.2] se chama *intervalo.*"),
    dict(id="05", block="remedios", text=
        "{t}Vamos marcar na linha do tempo. [p=0.3] {a}O primeiro remédio: [p=0.2] seis, [p=0.2] doze, [p=0.2] dezoito, "
        "[p=0.2] vinte e quatro horas. [p=0.4] {b}O segundo: [p=0.2] oito, [p=0.2] dezesseis, [p=0.2] vinte e quatro. "
        "[p=0.4] {c}Olha aí! [p=0.3] As duas tabuadas se encontram no *vinte e quatro.* [p=0.4] {d}Daqui a vinte e quatro "
        "horas, [p=0.2] os dois remédios voltam a ser tomados juntos."),
    dict(id="06", block="remedios", text=
        "{t}E depois? [p=0.3] {a}Elas se encontram de novo no quarenta e oito, [p=0.2] no setenta e dois... [p=0.4] "
        "{b}Esses números que aparecem nas duas tabuadas [p=0.2] são os *múltiplos comuns.* [p=0.4] {c}E o primeiro deles, "
        "[p=0.2] o vinte e quatro, [p=0.2] é o *reencontro.*"),

    dict(id="06b", block="luzes", text=
        "{t}Funciona com qualquer coisa que se repete. [p=0.3] {a}Duas luzes de Natal: [p=0.2] uma pisca a cada *dois* "
        "segundos, [p=0.2] {b}a outra a cada *três.* [p=0.4] {c}A primeira: [p=0.2] dois, quatro, seis. [p=0.3] {d}A "
        "segunda: [p=0.2] três, seis. [p=0.4] {e}No *seis,* [p=0.2] as duas acendem juntas. [p=0.3] Cada uma no seu ritmo, "
        "[p=0.2] e o reencontro chega."),

    # ================= BLOCO B: DEFINIÇÃO =================
    dict(id="07", block="definicao", text=
        "{t}Esse primeiro reencontro tem nome: [p=0.2] *MMC,* [p=0.2] mínimo múltiplo comum. [p=0.4] {a}Mínimo quer dizer *o "
        "menor.* [p=0.3] {b}Múltiplo comum, [p=0.2] o que está na tabuada de todos. [p=0.4] {c}A definição: [p=0.2] o menor "
        "número, [p=0.2] diferente de zero, [p=0.2] que é múltiplo de todos os dados ao mesmo tempo."),
    dict(id="08", block="definicao", text=
        "{t}E por que diferente de zero? [p=0.4] {a}Porque o zero está em todas as tabuadas: [p=0.2] é o momento da largada. "
        "[p=0.4] {b}O que interessa é o *próximo* encontro. [p=0.4] {c}Então: [p=0.2] MMC de seis e oito [p=0.2] é *vinte e "
        "quatro.*"),

    # ================= BLOCO C: PELA FATORAÇÃO =================
    dict(id="09", block="fatoracao", text=
        "{t}Mas listar tabuadas com números grandes [p=0.2] demora. [p=0.3] Tem atalho? [p=0.4] {a}Tem: [p=0.2] a receita. "
        "[p=0.3] {b}A regra é: [p=0.2] *todos os fatores, com o maior expoente.* [p=0.4] {c}Por quê? [p=0.2] O múltiplo comum "
        "precisa *conter* cada número inteiro. [p=0.3] {d}Então nenhum tijolo pode faltar."),
    dict(id="10", block="fatoracao", text=
        "{t}Testando com o seis e o oito. [p=0.3] {a}Seis é dois vezes três. [p=0.3] {b}Oito é dois ao cubo. [p=0.4] "
        "{c}Todos os fatores: [p=0.2] o dois e o três. [p=0.3] {d}Do dois, o maior expoente é o três: [p=0.2] dois ao cubo. "
        "[p=0.3] {e}Dois ao cubo, oito, [p=0.2] vezes três, [p=0.2] *vinte e quatro.* [p=0.3] {f}O mesmo reencontro da linha "
        "do tempo!"),
    dict(id="11", block="fatoracao", text=
        "{t}Agora eu faço um maior: [p=0.2] setenta e dois e cento e vinte. [p=0.4] {a}Setenta e dois é dois ao cubo vezes "
        "três ao quadrado. [p=0.3] {b}Cento e vinte é dois ao cubo vezes três vezes cinco. [p=0.4] {c}Todos os fatores: "
        "[p=0.2] dois, [p=0.2] três [p=0.2] e cinco. [p=0.3] {d}Maiores expoentes: [p=0.2] dois ao cubo, [p=0.2] três ao "
        "quadrado [p=0.2] e cinco."),
    dict(id="12", block="fatoracao", text=
        "{a}Oito vezes nove, [p=0.2] setenta e dois. [p=0.3] Vezes cinco, [p=0.2] {b}*trezentos e sessenta.* [p=0.4] "
        "{c}Conferindo: [p=0.2] trezentos e sessenta dividido por setenta e dois [p=0.2] dá cinco, [p=0.2] sem sobrar. "
        "[p=0.3] {d}Dividido por cento e vinte, [p=0.2] dá três. [p=0.3] {e}Os dois cabem dentro dele. [p=0.2] É o "
        "reencontro."),

    dict(id="12b", block="nosfazemos", text=
        "{t}Sua vez. [p=0.3] {a}Calcule o MMC de *quatro* e *dez.* [p=0.3] {p}Pause e tente. [p=2.0] {b}Quatro é dois ao "
        "quadrado. [p=0.2] Dez é dois vezes cinco. [p=0.4] {c}Todos os fatores, maior expoente: [p=0.2] dois ao quadrado, "
        "quatro, [p=0.2] vezes cinco: [p=0.2] *vinte.* [p=0.4] {d}Confere na tabuada: [p=0.2] quatro, oito, doze, dezesseis, "
        "*vinte.* [p=0.2] Dez, *vinte.* [p=0.2] Reencontro!"),

    # ================= BLOCO D: DECOMPOSIÇÃO SIMULTÂNEA =================
    dict(id="13", block="varal", text=
        "{t}E com três números? [p=0.3] {a}Aí o mais rápido é a *decomposição simultânea:* [p=0.2] fatorar todos ao mesmo "
        "tempo, [p=0.2] no mesmo varal. [p=0.4] {b}Doze, dezoito e trinta, lado a lado. [p=0.3] {c}Divido pelo dois: "
        "[p=0.2] seis, nove e quinze. [p=0.4] {d}Agora pelo três: [p=0.2] dois, três e cinco."),
    dict(id="14", block="varal", text=
        "{a}Pelo dois de novo: [p=0.2] só o dois é divisível. [p=0.3] {b}Ele vira um, [p=0.2] e quem não divide *desce "
        "igual:* [p=0.2] um, três e cinco. [p=0.4] {c}Pelo três: [p=0.2] um, um e cinco. [p=0.3] {d}Pelo cinco: [p=0.2] "
        "um, um e um. [p=0.2] Acabou. [p=0.4] {e}Multiplico a coluna da direita: [p=0.2] dois vezes três vezes dois vezes "
        "três vezes cinco, [p=0.3] {f}*cento e oitenta.*"),

    # ================= BLOCO E: COMO RECONHECER =================
    dict(id="15", block="reconhecer", text=
        "{t}E como saber que a questão é de MMC? [p=0.4] {a}Repare nas palavras: [p=0.2] voltarão a coincidir, [p=0.2] "
        "{b}ao mesmo tempo novamente, [p=0.2] {c}juntos de novo, [p=0.2] {d}de quanto em quanto tempo se encontram. "
        "[p=0.4] {e}Coisa que se repete e se reencontra: [p=0.2] *MMC.*"),

    # ================= BLOCO F: CHECAGEM DE SANIDADE =================
    dict(id="16", block="sanidade", text=
        "{t}Fez a conta. [p=0.2] Como saber se está certa? [p=0.4] {a}Checagem rápida: [p=0.2] o MMC *nunca* é menor que o "
        "maior dos números dados. [p=0.4] {b}Faz sentido: [p=0.2] o reencontro não pode vir antes da volta mais lenta. "
        "[p=0.4] {c}Cento e oitenta é maior que trinta? [p=0.2] É. [p=0.2] Passou. [p=0.3] {d}E trezentos e sessenta é maior "
        "que cento e vinte? [p=0.2] Também. [p=0.2] Passou."),

    # ================= BLOCO G: QUANDO × QUANTAS VEZES =================
    dict(id="17", block="quantas", text=
        "{t}E agora, a pegadinha mais famosa. [p=0.4] {a}*Quando* os remédios coincidem? [p=0.2] Isso é o MMC: [p=0.2] a "
        "cada vinte e quatro horas. [p=0.4] {b}Mas *quantas vezes* eles coincidem em três dias? [p=0.3] {c}Três dias são "
        "setenta e duas horas. [p=0.3] {d}Setenta e dois dividido por vinte e quatro: [p=0.2] *três vezes.* [p=0.4] "
        "{f}No vinte e quatro, [p=0.2] no quarenta e oito [p=0.2] e no setenta e dois. [p=0.3] A largada, no zero, [p=0.2] "
        "não conta: [p=0.2] a pergunta é quantas vezes *voltam* a coincidir. [p=0.4] {e}O MMC é só o meio do caminho: "
        "[p=0.2] ainda falta *dividir.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] coisas que se repetem e se reencontram: [p=0.2] MMC. "
        "[p=0.5] {b}Dois: [p=0.2] todos os fatores, [p=0.2] maior expoente. [p=0.5] {c}Três: [p=0.2] pediram quantas vezes? "
        "[p=0.2] Ainda falta dividir."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar só os fatores *comuns.* [p=0.3] Com setenta "
        "e dois e cento e vinte, [p=0.2] dá vinte e quatro. [p=0.4] {b}Parece certo, [p=0.2] porque a palavra comum está no "
        "nome. [p=0.4] {c}Mas vinte e quatro é menor que cento e vinte: [p=0.2] a checagem denuncia. [p=0.2] Use *todos* os "
        "fatores."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] achar o MMC e *parar.* [p=0.4] {b}Parece certo, [p=0.2] porque a conta difícil já foi feita. "
        "[p=0.4] {c}Mas se pediram quantas vezes, [p=0.2] ainda falta dividir o intervalo pelo MMC."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] esquecer de *converter* as unidades. [p=0.4] {b}Parece certo, [p=0.2] porque os números "
        "estão todos ali. [p=0.4] {c}Mas minuto com hora, [p=0.2] ou minuto com segundo, [p=0.2] não se misturam. [p=0.2] "
        "Cento e oitenta minutos são *três horas.*"),

    # ================= QUESTÃO 1 =================
    dict(id="22", block="q1", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}Três linhas de ônibus partem do mesmo terminal. [p=0.3] {b}A linha "
        "A parte a cada doze minutos, [p=0.2] a linha B a cada dezoito minutos [p=0.2] e a linha C a cada trinta minutos. "
        "[p=0.4] {c}Se as três partiram juntas às seis horas, [p=0.2] a que horas voltarão a partir juntas pela primeira vez? "
        "[p=0.4] {d}A: [p=0.2] sete horas. [p=0.3] {e}B: [p=0.2] oito horas. [p=0.3] {f}C: [p=0.2] nove horas. [p=0.3] "
        "{g}D: [p=0.2] dez horas. [p=0.3] {h}E: [p=0.2] doze horas. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="23", block="q1", text=
        "{t}Vamos lá. [p=0.3] {a}Voltar a partir juntas: [p=0.2] coisas que se repetem e se reencontram. [p=0.2] *MMC.* "
        "[p=0.4] {b}E esses são os mesmos números do varal: [p=0.2] doze, dezoito e trinta. [p=0.3] {f}Pela fatoração: [p=0.2] doze é dois ao "
        "quadrado vezes três; [p=0.2] dezoito, dois vezes três ao quadrado; [p=0.2] trinta, dois vezes três vezes cinco. "
        "[p=0.4] {g}Maiores expoentes: [p=0.2] dois ao quadrado, [p=0.2] três ao quadrado [p=0.2] e cinco. [p=0.3] Quatro "
        "vezes nove vezes cinco: [p=0.2] {c}*cento e oitenta minutos.* [p=0.4] {d}Agora a unidade: [p=0.2] cento e oitenta minutos [p=0.2] são *três horas.*"),
    dict(id="24", block="q1", text=
        "{a}Seis horas mais três horas: [p=0.2] *nove horas.* [p=0.4] {b}Checagem: [p=0.2] cento e oitenta é maior que trinta. "
        "[p=0.2] Passou. [p=0.3] {ok}*Letra C!* [p=0.5] {x}E as sete horas? [p=0.3] É de quem *somou* os intervalos: [p=0.2] "
        "doze mais dezoito mais trinta, [p=0.2] sessenta minutos. [p=0.3] Somar não acha reencontro."),

    # ================= QUESTÃO 5 =================
    dict(id="25", block="q5", text=
        "{t}Próxima. [p=0.3] {a}Três lâmpadas de um painel piscam em intervalos regulares: [p=0.3] {b}a primeira a cada "
        "quatro segundos, [p=0.2] a segunda a cada seis segundos [p=0.2] e a terceira a cada dez segundos. [p=0.4] {c}Num "
        "certo instante as três piscam juntas. [p=0.3] {d}Nos dez minutos seguintes, [p=0.2] quantas vezes elas voltam a "
        "piscar simultaneamente?"),
    dict(id="26", block="q5", text=
        "{a}A: [p=0.2] seis. [p=0.3] {b}B: [p=0.2] dez. [p=0.3] {c}C: [p=0.2] doze. [p=0.3] {d}D: [p=0.2] quinze. [p=0.3] "
        "{e}E: [p=0.2] sessenta. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{t}Primeiro, o MMC. [p=0.3] {a}Quatro é dois ao quadrado. [p=0.2] {b}Seis é dois vezes três. [p=0.2] {c}Dez é dois "
        "vezes cinco. [p=0.4] {d}Todos os fatores, maior expoente: [p=0.2] dois ao quadrado, [p=0.2] vezes três, [p=0.2] "
        "vezes cinco: [p=0.3] {e}*sessenta segundos.* [p=0.4] {f}Elas piscam juntas a cada sessenta segundos. [p=0.3] {g}Checagem: [p=0.2] sessenta é "
        "maior que dez, [p=0.2] o maior intervalo. [p=0.2] Passou."),
    dict(id="28", block="q5", text=
        "{t}Mas a pergunta é *quantas vezes.* [p=0.4] {a}Converte: [p=0.2] dez minutos são seiscentos segundos. [p=0.4] "
        "{b}Seiscentos dividido por sessenta: [p=0.2] *dez vezes.* [p=0.4] {c}Aos sessenta, [p=0.2] cento e vinte, [p=0.2] "
        "cento e oitenta... [p=0.2] até seiscentos. [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q5", text=
        "{x}E a armadilha? [p=0.3] Quem achou o MMC e *parou* [p=0.2] marca sessenta: [p=0.2] a letra E. [p=0.4] {y}E quem "
        "dividiu sessenta por dez [p=0.2] sem converter os minutos [p=0.2] cai no seis: [p=0.2] a letra A."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] coisas que se repetem e se reencontram: [p=0.2] MMC. "
        "[p=0.5] {b}Dois: [p=0.2] todos os fatores, [p=0.2] maior expoente. [p=0.5] {c}Três: [p=0.2] pediram quantas vezes? "
        "[p=0.2] Ainda falta dividir."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}E quando, em vez de coisas que se repetem, [p=0.2] você precisa *cortar* tábuas [p=0.2] {b}ou formar grupos "
        "iguais, [p=0.2] do maior tamanho possível? [p=0.4] {c}Aí a ferramenta é outra. [p=0.3] {d}Próximo episódio: "
        "[p=0.2] *MDC.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha do quantas vezes? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
