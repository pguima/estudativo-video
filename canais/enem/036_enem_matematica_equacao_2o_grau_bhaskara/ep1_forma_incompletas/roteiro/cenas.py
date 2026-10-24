# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 1 de 6: forma geral, coeficientes com sinal e incompletas.
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seções 02 e 03 + Questão 5.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A equação do 2º grau só CONVERSA DEPOIS DE ARRUMADA: tudo de um lado, zero do outro, na ordem x², x, número.
#   O sinal é parte do coeficiente, como o SOBRENOME faz parte do nome: em x² − 7x + 10, o b se chama −7.
#   PRODUTO NULO: se uma multiplicação deu zero, alguém ali é zero (as duas caixinhas com a placa "= 0").
#   NUNCA DIVIDA POR x: dividir por x é jogar fora, sem perceber, a raiz zero.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Tabela da seção 02: 2x² − 7x + 3 = 0 (2, −7, 3) · 3x − x² = 2 → −x² + 3x − 2 = 0 (−1, 3, −2) · x² = 5x → x² − 5x = 0
#   (1, −5, 0) · (x + 1)² = 9 → x² + 2x + 1 = 9 → x² + 2x − 8 = 0 (1, 2, −8). Vezes −1: x² − 3x + 2 = 0 (raízes 1 e 2 nas
#   duas formas). b = 0: 2x² − 50 = 0 → ±5 · x² + 9 = 0 sem raiz real · fatorada (x − 2)(x + 7) = 0 → 2 e −7.
#   DESVIO DO PROMPT: o bloco c (c = 0) e o erro 2 pediam 3x² − 12x / 3x² = 12x, que é exatamente a Questão 5 ("você faz").
#   Para não entregar a questão, usam 2x² − 10x = 0 → 2x(x − 5) = 0 → 0 e 5 (2·25 − 10·5 = 0) e 2x² = 10x. O gancho
#   (3x² = 12x) fica igual e só é respondido na Questão 5.
# Nós fazemos (prompt): x² − 49 = 0 → ±7 · 2x² + 6x = 0 → 2x(x + 3) = 0 → 0 e −3 (2·9 − 18 = 0).
# QUESTÃO 5 (você faz, texto idêntico): 3x² − 12x = 0 → 3x(x − 4) = 0 → 0 ou 4 → incompleta, faltou o 0 → E.
#   Erradas (do material e do prompt): A ignora a raiz perdida; B resolve 3x² = 12 (x² = 4 → ±2), esquecendo o x da direita;
#   C e D aplicam o ± das incompletas com b = 0, mas aqui quem é zero é o c: −4 não satisfaz (3·16 = 48 ≠ 12·(−4) = −48).
# Acréscimos nossos (verde): "vezes −1 quando o a é negativo"; c = 0 → raízes 0 e −b/a; b = 0 → isole x² e use ±;
#   "já veio fatorada? leia as raízes com o sinal trocado"; o quadrado de 25 m² (lado 5 m, o −5 descartado pelo contexto).
# Frases-chave (meio e fim, idênticas): 1. Primeiro arrume: tudo de um lado, zero do outro. 2. O sinal faz parte do
#   coeficiente. 3. Nunca divida por x: coloque x em evidência.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação do 2º grau do zero: coeficientes com sinal e incompletas sem fórmula · Matemática ENEM, 2º grau episódio 1"

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
        "{a}Para resolver *três x ao quadrado igual a doze x,* [p=0.3] {b}um estudante dividiu tudo por x [p=0.2] e achou "
        "*x igual a quatro.* [p=0.4] {c}Está certo, [p=0.2] mas está *incompleto:* [p=0.3] {d}ele jogou fora uma resposta "
        "sem perceber. [p=0.4] {e}*Qual?*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai *arrumar* qualquer equação do segundo grau, [p=0.3] {b}ler os *coeficientes* sem "
        "errar o sinal [p=0.3] {c}e resolver as *incompletas* sem fórmula."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Expressões Algébricas: [p=0.2] o *fator comum.* "
        "[p=0.2] Cinco x mais dez [p=0.2] é *cinco vezes, x mais dois.* [p=0.3] {b}E *x mais um, ao quadrado,* [p=0.2] é x "
        "ao quadrado, mais dois x, mais um. [p=0.4] {c}Da série de Equações: [p=0.2] a *balança.* [p=0.2] O que se faz de "
        "um lado, [p=0.2] se faz do outro."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Um terreno quadrado tem *vinte e cinco metros quadrados.* [p=0.3] Quanto mede o lado? [p=0.6] {a}*Cinco "
        "metros:* [p=0.2] cinco vezes cinco, vinte e cinco. [p=0.4] {b}Agora sem terreno: [p=0.2] *que número, ao quadrado, "
        "dá vinte e cinco?* [p=0.5] {c}O cinco, [p=0.2] e também o *menos cinco.* [p=0.2] Menos com menos dá mais. [p=0.4] "
        "{d}Em matemática: [p=0.2] *x ao quadrado igual a vinte e cinco.* [p=0.2] Duas respostas. [p=0.2] No terreno, o "
        "menos cinco sai: [p=0.2] lado não é negativo."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E o que é uma equação do segundo grau? [p=0.4] {a}É a equação que pode ser escrita assim: [p=0.2] *a x ao "
        "quadrado, mais b x, mais c, igual a zero.* [p=0.4] {b}a, b e c são os *coeficientes,* [p=0.2] os números da "
        "equação. [p=0.2] O *a* acompanha o x ao quadrado, [p=0.2] o *b* acompanha o x, [p=0.2] e o *c* fica sozinho: "
        "[p=0.2] é o *termo independente.* [p=0.4] {c}Os valores de x que resolvem a equação [p=0.2] são as *raízes.*"),
    dict(id="06", block="definicao", text=
        "{t}E por que o *a* não pode ser zero? [p=0.4] {a}Porque aí o x ao quadrado *some,* [p=0.2] e sobra algo como "
        "*três x menos seis.* [p=0.3] {b}Isso já é do *primeiro grau.* [p=0.2] A regra: [p=0.2] *a diferente de zero.*"),

    # ================= BLOCO B: ARRUMAR E LER =================
    dict(id="07", block="arrumar", text=
        "{t}Em *três x menos x ao quadrado igual a dois,* [p=0.2] quanto vale o a? [p=0.5] {a}Calma. [p=0.2] A equação do "
        "segundo grau *só conversa depois de arrumada.* [p=0.4] {b}Tudo de um lado, [p=0.2] *zero do outro,* [p=0.2] na "
        "ordem: [p=0.2] x ao quadrado, x, número. [p=0.4] {c}O dois passa subtraindo, [p=0.2] e fica: [p=0.2] *menos x ao "
        "quadrado, mais três x, menos dois, igual a zero.*"),
    dict(id="08", block="arrumar", text=
        "{t}Agora, a tabelinha. [p=0.3] {a}O a é *menos um.* [p=0.3] {b}O b é *três.* [p=0.3] {c}O c é *menos dois.* "
        "[p=0.4] {d}O sinal faz parte do coeficiente, [p=0.2] como o *sobrenome* faz parte do nome. [p=0.2] O c não se "
        "chama dois: [p=0.2] se chama *menos dois.*"),
    dict(id="09", block="arrumar", text=
        "{t}Mais três para treinar o olho. [p=0.3] {a}*Dois x ao quadrado, menos sete x, mais três:* [p=0.2] já arrumada. "
        "[p=0.2] *Dois, menos sete, três.* [p=0.4] {b}*x ao quadrado igual a cinco x:* [p=0.2] o cinco x passa subtraindo. "
        "[p=0.2] *Um, menos cinco, zero.* [p=0.4] {c}*x mais um, ao quadrado, igual a nove:* [p=0.2] desenvolva e tire o "
        "nove. [p=0.2] x ao quadrado, mais dois x, menos oito: [p=0.2] *um, dois, menos oito.*"),
    dict(id="10", block="arrumar", text=
        "{t}E esse *a negativo* incomoda? [p=0.4] {a}Multiplique tudo por *menos um:* [p=0.2] os sinais viram. [p=0.3] "
        "{b}Fica *x ao quadrado, menos três x, mais dois.* [p=0.4] {c}E as raízes *não mudam:* [p=0.2] zero vezes menos um "
        "continua zero."),

    # ================= BLOCO C: PRODUTO NULO E c = 0 =================
    dict(id="11", block="nulo", text=
        "{t}E quando falta um pedaço? [p=0.4] {a}Se o b ou o c for *zero,* [p=0.2] a equação é *incompleta,* [p=0.2] e "
        "tem um caminho curto. [p=0.4] {b}A chave é o *produto nulo:* [p=0.2] se uma multiplicação deu zero, [p=0.2] "
        "*alguém ali é zero.* [p=0.4] {c}Não tem outro jeito de uma multiplicação dar zero."),
    dict(id="12", block="nulo", text=
        "{t}Com o *c igual a zero.* [p=0.3] {a}*Dois x ao quadrado, menos dez x, igual a zero.* [p=0.4] {b}O dois x está "
        "nos dois termos. [p=0.2] Em evidência: [p=0.2] *dois x, vezes, x menos cinco, igual a zero.* [p=0.4] {c}Duas "
        "caixinhas dando zero. [p=0.2] Ou dois x é zero: [p=0.2] *x igual a zero.* [p=0.4] {d}Ou x menos cinco é zero: "
        "[p=0.2] *x igual a cinco.* [p=0.4] {e}Confira: [p=0.2] dois vezes vinte e cinco, cinquenta, [p=0.2] menos "
        "cinquenta: [p=0.2] *zero.*"),
    dict(id="13", block="nulo", text=
        "{t}Atalho para o c igual a zero. [p=0.3] {a}Uma raiz é *sempre zero.* [p=0.3] {b}A outra é *menos b sobre a.* "
        "[p=0.3] Aqui: [p=0.2] menos, menos dez, sobre dois: [p=0.2] *cinco.*"),

    # ================= BLOCO D: NUNCA DIVIDA POR x =================
    dict(id="14", block="dividir", text=
        "{t}E o caminho rápido? [p=0.4] {a}*Dois x ao quadrado igual a dez x.* [p=0.2] Divide por x: [p=0.2] *x igual a "
        "cinco.* [p=0.4] {b}Cadê o *zero?* [p=0.4] {c}Dividir por x supõe que x *não* é zero. [p=0.4] {d}*Nunca divida por "
        "x:* [p=0.2] dividir por x é jogar fora, sem perceber, a raiz zero. [p=0.3] Arrume [p=0.2] e coloque o x *em "
        "evidência.*"),

    # ================= BLOCO E: b = 0 =================
    dict(id="15", block="bzero", text=
        "{t}E quando o *b* é zero? [p=0.4] {a}*Dois x ao quadrado, menos cinquenta, igual a zero.* [p=0.4] {b}Isole o x ao "
        "quadrado: [p=0.2] soma cinquenta, [p=0.2] divide por dois: [p=0.2] *x ao quadrado igual a vinte e cinco.* [p=0.4] "
        "{c}O terreno do começo: [p=0.2] *cinco ou menos cinco.* [p=0.4] {d}Raízes *simétricas:* [p=0.2] o mesmo número, "
        "[p=0.2] com sinais trocados."),
    dict(id="16", block="bzero", text=
        "{t}E *x ao quadrado mais nove igual a zero?* [p=0.4] {a}Isolando: [p=0.2] *x ao quadrado igual a menos nove.* "
        "[p=0.4] {b}Que número ao quadrado dá negativo? [p=0.3] Nenhum. [p=0.4] {c}*Não tem raiz real.* [p=0.4] {d}Atalho "
        "para o b igual a zero: [p=0.2] isole o x ao quadrado [p=0.2] e use o *mais ou menos.* [p=0.2] Deu negativo? [p=0.2] "
        "*Sem raiz real.*"),

    # ================= BLOCO F: JÁ VEM FATORADA =================
    dict(id="17", block="fatorada", text=
        "{t}E se já vier *multiplicada?* [p=0.4] {a}*x menos dois, vezes, x mais sete, igual a zero.* [p=0.4] {b}Produto "
        "nulo: [p=0.2] x menos dois é zero, [p=0.2] *x igual a dois.* [p=0.2] x mais sete é zero, [p=0.2] *x igual a menos "
        "sete.* [p=0.4] {c}Sem conta nenhuma. [p=0.3] {d}Atalho: [p=0.2] leia cada parêntese com o *sinal trocado.* [p=0.2] "
        "Desenvolver é trabalho jogado fora."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva duas: [p=0.2] *x ao quadrado menos quarenta e nove igual a zero,* [p=0.3] {b}e "
        "*dois x ao quadrado mais seis x igual a zero.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Na primeira, o b é zero: [p=0.2] x ao quadrado igual a quarenta e nove, [p=0.2] *sete "
        "ou menos sete.* [p=0.4] {b}Na segunda, o c é zero: [p=0.2] *dois x, vezes, x mais três, igual a zero.* [p=0.4] "
        "{c}*x igual a zero* [p=0.2] ou *x igual a menos três.* [p=0.4] {d}Confira o menos três: [p=0.2] dois vezes nove, "
        "dezoito, [p=0.2] mais seis vezes menos três, menos dezoito: [p=0.2] *zero.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primeiro arrume: tudo de um lado, zero do outro. [p=0.5] "
        "{b}Dois: [p=0.2] o sinal faz parte do coeficiente. [p=0.5] {c}Três: [p=0.2] nunca divida por x: coloque x em "
        "evidência."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] em *x ao quadrado, menos sete x, mais dez,* "
        "[p=0.2] ler o b como *sete.* [p=0.4] {b}Parece certo, [p=0.2] porque o número que aparece escrito é o sete. "
        "[p=0.4] {c}Mas o sinal faz parte do coeficiente: [p=0.2] o b é *menos sete.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] em *dois x ao quadrado igual a dez x,* [p=0.2] dividir por x [p=0.2] e responder *só cinco.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o cinco *funciona* na equação. [p=0.4] {c}Mas ao dividir por x, [p=0.2] "
        "o *zero* desapareceu. [p=0.2] Arrume e coloque x em evidência: [p=0.2] *zero e cinco.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] *x ao quadrado igual a vinte e cinco* [p=0.2] dar *só cinco.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a raiz de vinte e cinco é cinco. [p=0.4] {c}Mas são *duas* respostas: [p=0.2] *cinco e menos "
        "cinco.* [p=0.2] Só descarte o menos cinco [p=0.2] se o *contexto* pedir."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="24", block="q5", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] *Você faz.* [p=0.4] {a}Para resolver a "
        "equação *três x ao quadrado igual a doze x,* [p=0.2] um estudante dividiu os dois lados por *três x* [p=0.2] e "
        "concluiu que a solução é *x igual a quatro.* [p=0.2] Sobre essa resolução, é correto afirmar que ela: [p=0.4] "
        "{qa}A: [p=0.2] está correta, pois a única solução é quatro. [p=0.3] {qb}B: [p=0.2] está errada, pois as soluções "
        "são dois e menos dois. [p=0.3] {qc}C: [p=0.2] está errada, pois as soluções são quatro e menos quatro. [p=0.3] "
        "{qd}D: [p=0.2] está incompleta, pois faltou a solução menos quatro. [p=0.3] {qe}E: [p=0.2] está incompleta, pois "
        "faltou a solução zero. [p=0.4] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="25", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}Arrume: [p=0.2] *três x ao quadrado, menos doze x, igual a zero.* [p=0.2] O c é "
        "zero. [p=0.4] {b}Três x em evidência: [p=0.2] *três x, vezes, x menos quatro, igual a zero.* [p=0.4] {c}*x igual "
        "a zero* [p=0.2] ou *x igual a quatro.* [p=0.4] {d}O quatro está certo, [p=0.2] mas ao dividir por três x [p=0.2] o "
        "estudante jogou fora o *zero.* [p=0.2] É a resposta do começo da aula. [p=0.3] {ok}*Letra E!*"),
    dict(id="26", block="q5", text=
        "{t}E as erradas? [p=0.3] {xa}A A *ignora* a raiz perdida. [p=0.4] {xb}A B resolve *três x ao quadrado igual a "
        "doze,* [p=0.2] esquecendo o x da direita. [p=0.4] {xc}A C e a D usam o *mais ou menos* de quando o b é zero. "
        "[p=0.2] {xd}Mas aqui o zero é o *c.* [p=0.3] {f}E o menos quatro não serve: [p=0.2] três vezes dezesseis, "
        "*quarenta e oito;* [p=0.2] doze vezes menos quatro, *menos quarenta e oito.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro arrume: tudo de um lado, zero do outro. "
        "[p=0.5] {b}Dois: [p=0.2] o sinal faz parte do coeficiente. [p=0.5] {c}Três: [p=0.2] nunca divida por x: coloque "
        "x em evidência."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}E quando a equação vem *completa,* [p=0.2] como *dois x ao quadrado, menos sete x, mais três, igual a zero,* "
        "[p=0.2] sem fator comum à vista? [p=0.5] {b}Existe uma *fórmula* que resolve todas. [p=0.5] {c}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha dividido por x alguma vez? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
