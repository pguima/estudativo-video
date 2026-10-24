# Roteiro — Frações, Decimais e Dízimas, Episódio 5 de 8: Operações com decimais sem calculadora (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seção 07 + Questão 5 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   DINHEIRO: decimal é dinheiro; a vírgula separa reais de centavos.
#   MOEDAS: dividir 4,80 por 0,12 é perguntar quantas moedas de 12 centavos cabem em R$ 4,80 → 40. Por isso o resultado cresce.
# Números do material (seção 07): 2,5 + 0,75 = 2,50 + 0,75 = 3,25 · 0,3 · 0,04 = 0,012 (1 + 2 = 3 casas; 3/10 · 4/100 = 12/1000) ·
#   4,8 ÷ 0,12 = 480 ÷ 12 = 40 · 3,47 · 100 = 347 · 3,47 ÷ 100 = 0,0347.
#   Exemplo próprio da subtração: R$ 5,00 − R$ 2,75 = R$ 2,25. Encolher: 10 · 0,5 = 5 (metade).
# Exercício: 1,2 · 0,5 = 0,6 e 2,4 ÷ 0,6 = 4.
# Questão 5 (seção 12) lida exatamente como no material · gabarito B (40). E = 576 é de quem multiplicou (4,8 · 0,12 = 0,576).
#   As outras são descartadas "conferindo de volta" (× 0,12): A 4 → 0,48 · C 57 → 6,84 · D 400 → 48 · E 576 → 69,12.
# Frases-chave (meio e fim, idênticas):
#   1. Somar: vírgula embaixo de vírgula.
#   2. Multiplicar: some as casas decimais.
#   3. Dividir por menos de 1 faz o número crescer.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Dividi 4,8 por 0,12 e deu 40: decimais sem calculadora · Matemática ENEM, episódio 5"

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
        "{a}Dividi *quatro vírgula oito* por *zero vírgula doze,* [p=0.2] e deu *quarenta.* [p=0.5] {b}O resultado ficou *maior* "
        "que o número que eu dividi. [p=0.4] {c}Errei? [p=0.4] {d}*Não.* [p=0.3] {e}E entender isso salva questões inteiras do ENEM."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *somar,* [p=0.2] *multiplicar* e *dividir* decimais sem calculadora, [p=0.4] "
        "{b}e sem medo do resultado. [p=0.4] {c}E o segredo vai estar no seu bolso: [p=0.2] *dinheiro.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="dinheiro", text=
        "{t}Pense em dois reais e cinquenta centavos. [p=0.3] {a}Você escreve assim: [p=0.2] dois, [p=0.2] vírgula, [p=0.2] "
        "cinquenta. [p=0.4] {b}Isso é um *número decimal:* [p=0.2] um número com vírgula. [p=0.4] {c}E a *vírgula* separa o "
        "inteiro dos pedaços menores. [p=0.3] {d}No dinheiro, [p=0.2] ela separa *reais* de *centavos.*"),
    dict(id="04", block="casas", text=
        "{t}Cada algarismo depois da vírgula ocupa uma *casa decimal.* [p=0.4] {a}A primeira casa é o *décimo:* [p=0.2] zero "
        "vírgula um, [p=0.2] que é dez centavos, [p=0.2] um décimo do real. [p=0.4] {b}A segunda é o *centésimo:* [p=0.2] zero "
        "vírgula zero um, [p=0.2] um centavo. [p=0.4] {c}E a terceira é o *milésimo:* [p=0.2] zero vírgula zero zero um, [p=0.2] "
        "que é um décimo de centavo. [p=0.2] Moeda disso não existe, [p=0.2] mas na conta aparece."),

    # ================= BLOCO A: SOMAR E SUBTRAIR =================
    dict(id="05", block="somar", text=
        "{t}Primeira pergunta: [p=0.2] você tem *dois reais e cinquenta* [p=0.2] e ganha *setenta e cinco centavos.* [p=0.3] "
        "Com quanto fica? [p=0.5] {a}Os centavos juntos: [p=0.2] cinquenta mais setenta e cinco, [p=0.2] cento e vinte e cinco "
        "centavos. [p=0.3] {b}Isso é um real e vinte e cinco. [p=0.4] {c}Mais os dois reais: [p=0.2] *três reais e vinte e cinco.*"),
    dict(id="06", block="somar", text=
        "{t}No caderno, a regra é esta: [p=0.3] {a}*alinhe as vírgulas,* [p=0.2] uma embaixo da outra. [p=0.4] {b}Se uma tiver "
        "menos casas, [p=0.2] complete com *zero:* [p=0.2] dois vírgula cinco vira dois vírgula cinquenta. [p=0.4] {c}Aí some "
        "como sempre, [p=0.2] da direita para a esquerda, [p=0.3] {d}e desça a vírgula no mesmo lugar: [p=0.2] *três vírgula vinte "
        "e cinco.*"),
    dict(id="07", block="somar", text=
        "{t}E por que alinhar? [p=0.3] {a}Porque assim você soma *reais com reais* [p=0.2] e *centavos com centavos.* [p=0.4] "
        "{b}A subtração é igual: [p=0.2] cinco reais menos dois e setenta e cinco. [p=0.3] {c}Escreva cinco como cinco vírgula "
        "zero zero, [p=0.2] alinhe, [p=0.2] e subtraia: [p=0.2] *dois e vinte e cinco.*"),

    # ================= BLOCO B: MULTIPLICAR =================
    dict(id="08", block="multiplicar", text=
        "{t}Agora, uma que confunde muita gente: [p=0.2] *zero vírgula três vezes zero vírgula zero quatro.* [p=0.4] {a}Primeiro "
        "passo: [p=0.2] esqueça as vírgulas, [p=0.2] e multiplique como se fossem inteiros. [p=0.3] Três vezes quatro, [p=0.2] "
        "*doze.* [p=0.4] {b}Segundo passo: [p=0.2] *conte as casas decimais.* [p=0.3] O zero vírgula três tem *uma.* [p=0.2] "
        "O zero vírgula zero quatro tem *duas.* [p=0.3] {c}Uma mais duas: [p=0.2] *três casas* no resultado."),
    dict(id="09", block="multiplicar", text=
        "{t}Então o doze precisa de três casas depois da vírgula. [p=0.4] {a}Só tem dois algarismos? [p=0.2] Complete com zero "
        "na frente: [p=0.3] {b}*zero vírgula zero doze.* [p=0.5] {c}E por que contar casas funciona? [p=0.3] {d}Zero vírgula três "
        "é *três décimos.* [p=0.2] Zero vírgula zero quatro é *quatro centésimos.* [p=0.3] {e}Multiplicando, [p=0.2] três vezes "
        "quatro em cima, [p=0.2] dez vezes cem embaixo: [p=0.2] *doze milésimos.*"),
    dict(id="10", block="multiplicar", text=
        "{t}O atalho, então: [p=0.2] {a}multiplique sem vírgula, [p=0.3] {b}some as casas dos dois números, [p=0.3] {c}e conte "
        "essas casas *da direita para a esquerda* para pôr a vírgula. [p=0.4] {d}Faltou algarismo? [p=0.2] Zero na frente."),

    # ================= BLOCO C: DIVIDIR =================
    dict(id="11", block="dividir", text=
        "{t}E a divisão do começo? [p=0.3] {a}Quatro vírgula oito dividido por zero vírgula doze [p=0.2] é a mesma pergunta que: "
        "[p=0.3] {b}*quantas moedas de doze centavos cabem em quatro reais e oitenta?* [p=0.4] {c}Doze centavos é pouquinho. "
        "[p=0.3] Então cabem *muitas* moedas: [p=0.2] *quarenta.* [p=0.4] {d}Por isso o resultado cresce."),
    dict(id="12", block="dividir", text=
        "{t}E como fazer a conta sem calculadora? [p=0.3] {a}*Iguale as casas decimais:* [p=0.2] quatro vírgula oito vira quatro "
        "vírgula oitenta, [p=0.2] com duas casas, [p=0.2] igual ao zero vírgula doze. [p=0.4] {b}Agora *tire as vírgulas* dos dois: "
        "[p=0.3] quatrocentos e oitenta dividido por doze. [p=0.4] {c}Tirar a vírgula, aqui, [p=0.2] é passar tudo para "
        "*centavos:* [p=0.2] quatrocentos e oitenta centavos, [p=0.2] em moedas de doze centavos."),
    dict(id="13", block="dividir", text=
        "{t}E a divisão ficou inteira. [p=0.3] {a}Quatrocentos e oitenta dividido por doze: [p=0.3] {b}doze cabe *quatro* vezes no "
        "quarenta e oito, [p=0.2] porque doze vezes quatro é quarenta e oito. [p=0.4] {c}Sobra zero, [p=0.2] e desce o zero: "
        "[p=0.3] {d}resultado, [p=0.2] *quarenta.*"),

    # ================= BLOCO D: POR 10, 100, 1000 =================
    dict(id="14", block="vezes100", text=
        "{t}E multiplicar por dez, [p=0.2] cem, [p=0.2] mil? [p=0.3] Aí é quase mágica. [p=0.4] {a}Três vírgula quarenta e sete "
        "vezes cem. [p=0.3] {b}O cem tem *dois zeros:* [p=0.2] então a vírgula anda *duas casas para a direita.* [p=0.4] "
        "{c}Resultado: [p=0.2] *trezentos e quarenta e sete.* [p=0.4] {d}Faz sentido: [p=0.2] cem pacotes de três reais e "
        "quarenta e sete custam trezentos e quarenta e sete reais."),
    dict(id="15", block="vezes100", text=
        "{t}E dividir por cem é o caminho de volta: [p=0.3] {a}a vírgula anda *duas casas para a esquerda.* [p=0.4] {b}Três "
        "vírgula quarenta e sete dividido por cem: [p=0.2] faltou casa? [p=0.2] Complete com zero. [p=0.3] {c}*Zero vírgula zero "
        "trezentos e quarenta e sete.* [p=0.4] {d}O atalho: [p=0.2] *cada zero é uma casa.* [p=0.2] Vezes, direita. [p=0.2] "
        "Dividido, esquerda."),

    # ================= BLOCO E: O RESULTADO QUE ASSUSTA =================
    dict(id="16", block="assusta", text=
        "{t}E agora, o resultado que assusta [p=0.2] e está certo. [p=0.4] {a}*Dividir* por um número *menor que um* [p=0.2] "
        "faz o resultado *crescer.* [p=0.3] Quarenta moedas, [p=0.2] lembra? [p=0.4] {b}E *multiplicar* por um número menor que "
        "um [p=0.2] faz o resultado *encolher:* [p=0.3] dez vezes zero vírgula cinco é cinco, [p=0.2] a metade. [p=0.4] {c}Ficou "
        "na dúvida? [p=0.2] *Confira multiplicando de volta:* [p=0.3] {d}quarenta vezes zero vírgula doze [p=0.2] dá quatro "
        "vírgula oito. [p=0.3] *Está certo.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas contas. [p=0.4] {a}Primeira: [p=0.2] *um vírgula dois vezes zero vírgula cinco.* [p=0.4] "
        "{b}Segunda: [p=0.2] *dois vírgula quatro dividido por zero vírgula seis.* [p=0.4] {c}Pause o vídeo e calcule. [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Doze vezes cinco, [p=0.2] sessenta. [p=0.3] Uma casa mais uma casa, [p=0.2] duas casas: "
        "[p=0.2] zero vírgula sessenta, [p=0.2] ou seja, [p=0.2] *zero vírgula seis.* [p=0.5] {b}Na divisão, as casas já são "
        "iguais. [p=0.3] Tira as vírgulas: [p=0.2] vinte e quatro dividido por seis, [p=0.2] *quatro.* [p=0.4] {c}E conferindo: "
        "[p=0.2] quatro vezes zero vírgula seis, [p=0.2] dois vírgula quatro."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] somar: [p=0.2] vírgula embaixo de vírgula. [p=0.5] {b}Dois: "
        "[p=0.2] multiplicar: [p=0.2] some as casas decimais. [p=0.5] {c}Três: [p=0.2] dividir por menos de um [p=0.2] faz o "
        "número crescer."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer que zero vírgula três vezes zero vírgula zero "
        "quatro [p=0.2] é *zero vírgula doze.* [p=0.4] {b}Parece certo, [p=0.2] porque três vezes quatro é mesmo doze. [p=0.4] "
        "{c}Mas faltou contar as casas: [p=0.2] uma mais duas, [p=0.2] três. [p=0.2] *Zero vírgula zero doze.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *errou* porque a divisão deu um número maior. [p=0.4] {b}Parece certo, [p=0.2] porque na "
        "escola dividir sempre diminuía. [p=0.4] {c}Mas dividir por menos de um *aumenta.* [p=0.2] Confira multiplicando de volta."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] somar decimais *sem alinhar as vírgulas.* [p=0.4] {b}Parece certo, [p=0.2] porque você alinha os "
        "números pela direita, [p=0.2] como nos inteiros. [p=0.4] {c}Mas aí você soma centavos com reais. [p=0.2] *Vírgula embaixo "
        "de vírgula.*"),

    # ================= QUESTÃO 5 =================
    dict(id="23", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Uma fita de *quatro vírgula oito metros* [p=0.2] será cortada em "
        "pedaços de *zero vírgula doze metro* cada. [p=0.4] {b}Quantos pedaços serão obtidos?"),
    dict(id="24", block="questao", text=
        "{a}A: [p=0.2] quatro. [p=0.4] {b}B: [p=0.2] quarenta. [p=0.4] {c}C: [p=0.2] cinquenta e sete. [p=0.4] {d}D: [p=0.2] "
        "quatrocentos. [p=0.4] {e}E: [p=0.2] quinhentos e setenta e seis. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="questao", text=
        "{t}Vamos resolver. [p=0.3] {a}Quantos pedaços cabem na fita: [p=0.2] é divisão. [p=0.3] Quatro vírgula oito dividido por "
        "zero vírgula doze. [p=0.4] {b}Iguala as casas: [p=0.2] quatro vírgula oitenta. [p=0.3] Tira as vírgulas: [p=0.2] "
        "quatrocentos e oitenta dividido por doze, [p=0.2] *quarenta.* [p=0.4] {c}Conferindo de volta: [p=0.2] quarenta vezes zero "
        "vírgula doze, [p=0.2] quatro vírgula oito. [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="questao", text=
        "{t}E as outras? [p=0.3] {xe}A E é de quem *multiplicou* em vez de dividir: [p=0.2] quatro vírgula oito vezes zero vírgula "
        "doze dá zero vírgula quinhentos e setenta e seis, [p=0.2] e a pessoa sumiu com a vírgula. [p=0.5] {xa}As outras você "
        "descarta conferindo de volta. [p=0.3] Quatro pedaços dariam só quarenta e oito centímetros. [p=0.4] {xd}Quatrocentos "
        "dariam quarenta e oito metros. [p=0.4] {xc}E cinquenta e sete passariam da fita."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] somar: [p=0.2] vírgula embaixo de vírgula. [p=0.5] "
        "{b}Dois: [p=0.2] multiplicar: [p=0.2] some as casas decimais. [p=0.5] {c}Três: [p=0.2] dividir por menos de um [p=0.2] "
        "faz o número crescer."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Por que *um quarto* vira zero vírgula vinte e cinco [p=0.2] e acaba, [p=0.3] {b}mas *um terço* vira zero vírgula três "
        "três três [p=0.2] e *nunca* acaba? [p=0.4] {c}Dá para saber *antes* de dividir. [p=0.4] {d}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha levado um susto com uma divisão que cresceu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
