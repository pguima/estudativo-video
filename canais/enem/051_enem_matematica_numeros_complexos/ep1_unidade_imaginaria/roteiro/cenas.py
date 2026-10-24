# Roteiro — Números Complexos, Episódio 1 de 5: a unidade imaginária, delta negativo e as potências de i
# Base: Estudos/Enem/estudos/01-matematica/36-numeros-complexos.html — seções 02 e 03 + Questões 8 e 1.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O SUPERPODER: i é uma letra comum com um superpoder — ao quadrado, vira −1.
#   O RELÓGIO DE QUATRO HORAS: 1, i, −1, −i e volta ao começo; para qualquer expoente, só importa o resto por 4.
#   AS GÊMEAS ESPELHADAS: raízes conjugadas têm a mesma parte real e a parte imaginária com o sinal trocado.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: Δ = b² − 4ac, Bhaskara e "Δ < 0 → nenhuma raiz real" (série de Equação do 2º grau); "√−4 não existe
#   nos reais" e as propriedades de potência (série de Potenciação); divisão com resto.
# Blocos = seções 02 e 03, com os exemplos do material e do prompt (x² + 2x + 5 = 0, √−36, √−4 · √−9, i^103, a soma
#   i + i² + … + i^100).
# Troca NOSSA (marcada), regra de exemplos: o prompt usa i^2026 no bloco e e na animação principal (506 voltas), mas
#   i^2026 é metade da Questão 1 ("você faz", com pausa). No bloco e uso i^2025 (2025 = 4 · 506 + 1 → i): o ponteiro dá
#   as mesmas 506 voltas e para na casa 1. O i^2026 e o i^2027 só aparecem na resolução da Questão 1. A promessa do
#   usuário ("até i elevado a 2026") ficou igual.
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO — "raiz de negativo: tire o menos, tire a raiz, cole o i";
#   "achou uma raiz complexa, a outra é a gêmea espelhada; confira por soma e produto"; "o resto por 4 sai dos dois
#   últimos algarismos" (o do prompt); e o erro 1 com (3i)² = −9, número nosso.
# QUESTÃO 8 (nós fazemos, logo depois do bloco c): Δ = 16 − 52 = −36, √−36 = 6i, x = (4 ± 6i) ÷ 2 = 2 ± 3i (A).
#   Erradas = material: B usa b em vez de −b; C divide só a parte real por 2; D não divide por 2a; E vale só nos reais.
# QUESTÃO 1 (você faz): i^2026 = i² = −1 e i^2027 = i³ = −i → −1 − i (C). Erradas = material: A usa i² = 1 e i³ = i;
#   B erra só o i³; D erra só o i²; E acha que duas seguidas se anulam (só quatro seguidas somam zero).
# Nós fazemos (prompt): i^35 → 35 = 4 · 8 + 3 → −i; i^48 → 48 = 4 · 12 → 1.
# Frases-chave (meio e fim, idênticas): 1. i ao quadrado é −1. 2. Delta negativo: nenhuma raiz real, mas duas raízes
#   complexas conjugadas. 3. Potência de i: só importa o resto por 4.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Número complexo do zero: i² = −1, delta negativo e i elevado a 2026 · Matemática ENEM, Complexos episódio 1"

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
        "{a}Na série de Bhaskara, [p=0.2] *x ao quadrado mais dois x mais cinco igual a zero* [p=0.2] deu delta *menos "
        "dezesseis,* [p=0.2] e a resposta foi: [p=0.2] *nenhuma raiz real.* [p=0.5] {b}Repare na palavra *real.* "
        "[p=0.5] {c}Hoje essa equação ganha *duas raízes:* [p=0.3] *menos um mais dois i* [p=0.2] e *menos um menos "
        "dois i.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Números complexos.* [p=0.4] {a}Ao final, [p=0.2] você vai "
        "*resolver equações do segundo grau com delta negativo* [p=0.3] {b}e calcular *qualquer potência de i,* "
        "[p=0.2] até *i elevado a dois mil e vinte e seis,* [p=0.2] *de cabeça.*"),
    dict(id="03", block="prereq", text=
        "{t}Quatro lembretes rápidos. [p=0.3] {a}Da série de Bhaskara: [p=0.2] *delta é b ao quadrado menos quatro a "
        "c,* [p=0.2] e x é *menos b, mais ou menos raiz de delta, sobre dois a.* [p=0.4] {b}Delta negativo: [p=0.2] "
        "*nenhuma raiz real.* [p=0.4] {c}Da Potenciação: [p=0.2] raiz de *menos quatro* não existe nos reais, "
        "[p=0.2] e nas potências de mesma base, [p=0.2] *os expoentes se somam.* [p=0.4] {d}E a divisão com resto: "
        "[p=0.2] dois mil e vinte e seis é *quatro vezes quinhentos e seis,* [p=0.2] *mais dois.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Antes da conta, [p=0.2] uma história. [p=0.4] {a}Para quem só sabia *contar,* [p=0.2] *menos cinco* não "
        "existia. [p=0.3] Como ter menos cinco laranjas? [p=0.4] {b}Até que veio o *termômetro:* [p=0.2] *menos cinco "
        "graus* existe, sim. [p=0.4] {c}Agora digite *raiz de menos trinta e seis* na calculadora do celular. "
        "[p=0.3] {d}*Erro.* [p=0.4] {e}Hoje esse erro vira *um número.*"),

    # ================= BLOCO A: A DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E que número é esse? [p=0.4] {a}*Unidade imaginária:* [p=0.2] o número *i,* [p=0.2] que, ao quadrado, "
        "dá *menos um.* [p=0.4] {b}Pense no i como uma *letra comum com um superpoder:* [p=0.2] quando aparece *ao "
        "quadrado,* [p=0.2] *vira menos um.* [p=0.4] {c}Com ele, [p=0.2] raiz de menos trinta e seis é *seis i.* "
        "[p=0.3] {d}Confira: [p=0.2] seis i, ao quadrado, [p=0.2] é trinta e seis vezes *i ao quadrado.* [p=0.3] "
        "{e}Pare a conta: [p=0.2] *i ao quadrado é menos um.* [p=0.2] Dá *menos trinta e seis.*"),
    dict(id="06", block="atalho_raiz", text=
        "{t}Atalho. [p=0.4] {a}Raiz de um número negativo? [p=0.2] *Tire o menos,* [p=0.3] {b}*tire a raiz* do "
        "número, [p=0.3] {c}e *cole o i.* [p=0.4] {d}Raiz de menos dezesseis: [p=0.2] *quatro i.* [p=0.3] Raiz de "
        "menos nove: [p=0.2] *três i.*"),

    # ================= BLOCO B: A FORMA ALGÉBRICA =================
    dict(id="07", block="forma", text=
        "{t}E como se escreve um número desses? [p=0.4] {a}*Número complexo:* [p=0.2] todo número da forma *a mais b "
        "i,* [p=0.2] com a e b reais. [p=0.2] Essa é a *forma algébrica.* [p=0.4] {b}*Parte real:* [p=0.2] o *a.* "
        "[p=0.4] {c}*Parte imaginária:* [p=0.2] o *b,* [p=0.2] o número que multiplica o i, [p=0.2] *sem o i.* "
        "[p=0.4] {d}Em dois menos três i, [p=0.2] a parte real é *dois* [p=0.2] e a parte imaginária é *menos três.*"),
    dict(id="08", block="tabela", text=
        "{t}E os nomes? [p=0.4] {a}Se a parte imaginária é *zero,* [p=0.2] o número é *real:* [p=0.2] menos sete é "
        "menos sete mais zero i. [p=0.4] {b}Se a parte real é zero, [p=0.2] e a imaginária não, [p=0.2] é "
        "*imaginário puro:* [p=0.2] cinco i. [p=0.4] {c}Com parte imaginária diferente de zero, [p=0.2] é *não real:* "
        "[p=0.2] dois menos três i. [p=0.4] {d}E o *conjunto dos complexos,* [p=0.2] o *C,* [p=0.2] *contém os "
        "reais.* [p=0.2] Todo real é um complexo [p=0.2] com o b igual a zero."),

    # ================= BLOCO C: DELTA NEGATIVO =================
    dict(id="09", block="delta", text=
        "{t}E a equação do gancho? [p=0.4] {a}*x ao quadrado mais dois x mais cinco igual a zero.* [p=0.3] "
        "*Discriminante,* [p=0.2] o delta: [p=0.2] quatro menos vinte, [p=0.2] *menos dezesseis.* [p=0.4] {b}Raiz de "
        "menos dezesseis: [p=0.2] *quatro i.* [p=0.4] {c}x é menos dois, mais ou menos quatro i, [p=0.2] sobre dois. "
        "[p=0.3] Divida *as duas partes* por dois: [p=0.2] {d}*menos um mais dois i* [p=0.2] e *menos um menos dois "
        "i.*"),
    dict(id="10", block="gemeas", text=
        "{t}Repare nas duas. [p=0.4] {a}Mesma parte real, [p=0.2] *menos um.* [p=0.2] Parte imaginária com o *sinal "
        "trocado.* [p=0.4] {b}São *raízes conjugadas:* [p=0.2] *gêmeas espelhadas.* [p=0.4] {c}E dá para conferir. "
        "[p=0.2] A soma: [p=0.2] os i se anulam, [p=0.2] *menos dois,* [p=0.2] que é *menos b sobre a.* [p=0.4] {d}O "
        "produto: [p=0.2] um, menos quatro *i ao quadrado.* [p=0.2] Pare: [p=0.2] i ao quadrado é menos um. [p=0.2] "
        "Um mais quatro, [p=0.2] *cinco,* [p=0.2] que é *c sobre a.*"),
    dict(id="11", block="atalho_gemea", text=
        "{t}Atalho. [p=0.4] {a}Achou *uma* raiz complexa? [p=0.2] A outra é a *gêmea espelhada:* [p=0.2] troque só o "
        "sinal do i. [p=0.4] {b}E confira por *soma e produto:* [p=0.2] *dez segundos* de conta."),

    # ================= QUESTÃO 8: NÓS FAZEMOS =================
    dict(id="12", block="q8", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM, [p=0.2] e *nós fazemos juntos.* [p=0.4] {a}Resolvendo *x "
        "ao quadrado menos quatro x mais treze igual a zero* [p=0.2] nos complexos, [p=0.2] as raízes são: [p=0.3] "
        "{qa}A: [p=0.2] dois mais ou menos três i. [p=0.2] {qb}B: [p=0.2] menos dois mais ou menos três i. [p=0.2] "
        "{qc}C: [p=0.2] dois mais ou menos seis i. [p=0.2] {qd}D: [p=0.2] quatro mais ou menos seis i. [p=0.2] {qe}E: "
        "[p=0.2] inexistentes, pois o discriminante é negativo. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="13", block="q8", text=
        "{t}Vamos juntos. [p=0.3] {a}Delta: [p=0.2] dezesseis menos cinquenta e dois, [p=0.2] *menos trinta e seis.* "
        "[p=0.3] Raiz: [p=0.2] *seis i.* [p=0.4] {b}x é quatro, mais ou menos seis i, sobre dois: [p=0.2] *dois mais "
        "ou menos três i.* [p=0.3] {ok}*Letra A!* [p=0.4] {c}Confiro: [p=0.2] soma *quatro;* [p=0.2] produto, quatro "
        "mais nove, [p=0.2] *treze.* [p=0.2] Bate. [p=0.4] {xb}A B usa *b* no lugar de *menos b.* [p=0.3] {xc}A C "
        "divide *só a parte real* por dois. [p=0.3] {xd}A D *não divide* por dois a. [p=0.3] {xe}E a E vale *só nos "
        "reais.*"),

    # ================= BLOCO D: O CUIDADO =================
    dict(id="14", block="cuidado", text=
        "{t}Agora, [p=0.2] uma pegadinha. [p=0.4] {a}Raiz de menos quatro *vezes* raiz de menos nove. [p=0.3] Dá para "
        "juntar tudo numa raiz só? [p=0.4] {b}Muita gente faz: [p=0.2] menos quatro vezes menos nove, [p=0.2] trinta e "
        "seis, [p=0.2] raiz, *seis.* [p=0.4] {c}*Não.* [p=0.2] Escreva com i *primeiro:* [p=0.2] *dois i vezes três "
        "i.* [p=0.3] {d}Seis i ao quadrado. [p=0.2] Pare: [p=0.2] i ao quadrado é menos um. [p=0.2] *Menos seis.*"),

    # ================= BLOCO E: O RELÓGIO =================
    dict(id="15", block="relogio", text=
        "{t}E as potências de i? [p=0.4] {a}i elevado a zero: [p=0.2] *um.* [p=0.2] {b}A um: [p=0.2] *i.* [p=0.2] "
        "{c}Ao quadrado: [p=0.2] *menos um.* [p=0.3] {d}Ao cubo: [p=0.2] i ao quadrado vezes i, [p=0.2] *menos i.* "
        "[p=0.3] {e}À quarta: [p=0.2] i ao quadrado, ao quadrado, [p=0.2] menos um ao quadrado: [p=0.2] *um* de novo. "
        "[p=0.4] {f}É um *relógio de quatro horas:* [p=0.2] cada vez que você multiplica por i, [p=0.2] o ponteiro "
        "*anda uma casa.*"),
    dict(id="16", block="resto", text=
        "{t}E um expoente enorme? [p=0.4] {a}Cada *quatro* casas, [p=0.2] o ponteiro dá *uma volta completa* e para "
        "no mesmo lugar. [p=0.3] {b}Então *só importa o resto da divisão por quatro.* [p=0.4] {c}i elevado a dois mil "
        "e vinte e cinco: [p=0.2] dois mil e vinte e cinco é quatro vezes quinhentos e seis, [p=0.2] *mais um.* "
        "[p=0.3] {d}Quinhentas e seis voltas, [p=0.2] e o ponteiro para na casa *um:* [p=0.2] *i.* [p=0.4] {e}i "
        "elevado a cento e três: [p=0.2] resto *três:* [p=0.2] *menos i.*"),
    dict(id="17", block="atalho_resto", text=
        "{t}Atalho. [p=0.4] {a}Para achar o resto por quatro, [p=0.2] olhe só os *dois últimos algarismos.* [p=0.4] "
        "{b}Cem é múltiplo de quatro, [p=0.2] então o resto *mora no fim do número.* [p=0.4] {c}Dois mil e vinte e "
        "cinco: [p=0.2] *vinte e cinco,* [p=0.2] resto um. [p=0.3] Cento e três: [p=0.2] *zero três,* [p=0.2] resto "
        "três."),

    # ================= BLOCO F: QUATRO SEGUIDAS =================
    dict(id="18", block="soma4", text=
        "{t}E uma *soma* de potências? [p=0.4] {a}Some uma volta inteira do relógio: [p=0.2] um, mais i, menos um, "
        "menos i. [p=0.4] {b}*Zero.* [p=0.2] Quatro potências seguidas somam *zero.* [p=0.4] {c}Então i, mais i ao "
        "quadrado, e assim por diante, até i elevado a cem: [p=0.2] cem termos, [p=0.2] *vinte e cinco grupos de "
        "quatro.* [p=0.3] {d}Soma: [p=0.2] *zero.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto valem *i elevado a trinta e cinco* [p=0.2] e *i elevado a quarenta e oito?* "
        "[p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Trinta e cinco é quatro vezes oito, [p=0.2] *mais três.* [p=0.2] Casa três: "
        "[p=0.2] *menos i.* [p=0.4] {b}Quarenta e oito é quatro vezes doze, [p=0.2] *resto zero.* [p=0.2] Volta "
        "certinha: [p=0.2] o ponteiro para no *um.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] i ao quadrado é menos um. [p=0.5] {b}Dois: [p=0.2] "
        "delta negativo: [p=0.2] nenhuma raiz real, [p=0.2] mas duas raízes complexas conjugadas. [p=0.5] {c}Três: "
        "[p=0.2] potência de i: [p=0.2] só importa o resto por quatro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *i ao quadrado igual a um.* [p=0.2] Aí três i, ao "
        "quadrado, vira *nove.* [p=0.4] {b}Parece certo, [p=0.2] porque *todo quadrado* que você conhecia dava "
        "positivo. [p=0.4] {c}Mas o i tem o superpoder: [p=0.2] *i ao quadrado é menos um.* [p=0.2] Três i, ao "
        "quadrado, é *menos nove.*"),
    dict(id="23", block="erros", text=
        "{t}Segundo. [p=0.4] {a}Dizer que a parte imaginária de *três menos quatro i* [p=0.2] é *menos quatro i.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o i *mora* nessa parte. [p=0.4] {c}Mas a parte imaginária é só o "
        "*número* que multiplica o i: [p=0.2] *menos quatro.*"),
    dict(id="24", block="erros", text=
        "{t}Terceiro. [p=0.4] {a}Raiz de menos quatro vezes raiz de menos nove, [p=0.2] igual a *seis.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque nos positivos [p=0.2] *raiz vezes raiz é a raiz do produto.* [p=0.4] {c}Com "
        "negativo, essa regra *não vale.* [p=0.2] Escreva com i primeiro: [p=0.2] *menos seis.*"),
    dict(id="25", block="erros", text=
        "{t}Quarto. [p=0.4] {a}Delta negativo: [p=0.2] *não há raízes.* [p=0.4] {b}Parece certo, [p=0.2] porque era "
        "*exatamente* o que você aprendeu na série de Bhaskara. [p=0.4] {c}Faltava uma palavra: [p=0.2] não há raízes "
        "*reais.* [p=0.2] Nos complexos, [p=0.2] há *duas.*"),

    # ================= QUESTÃO 1: VOCÊ FAZ =================
    dict(id="26", block="q1", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um professor pediu para simplificar *i elevado a dois mil e vinte e "
        "seis,* [p=0.2] *mais i elevado a dois mil e vinte e sete.* [p=0.3] O resultado é: [p=0.3] {qa}A: [p=0.2] um "
        "mais i. [p=0.2] {qb}B: [p=0.2] menos um mais i. [p=0.2] {qc}C: [p=0.2] menos um menos i. [p=0.2] {qd}D: "
        "[p=0.2] um menos i. [p=0.2] {qe}E: [p=0.2] zero. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {a}Dois mil e vinte e seis: [p=0.2] *vinte e seis,* [p=0.2] resto *dois.* "
        "[p=0.2] i ao quadrado, [p=0.2] *menos um.* [p=0.4] {b}Dois mil e vinte e sete: [p=0.2] resto *três.* "
        "[p=0.2] i ao cubo, [p=0.2] *menos i.* [p=0.4] {c}Soma: [p=0.2] *menos um menos i.* [p=0.3] {ok}*Letra C!* "
        "[p=0.4] {xa}A A usa i ao quadrado igual a um *e* i ao cubo igual a i. [p=0.3] {xb}A B erra *só o i ao "
        "cubo.* [p=0.3] {xd}A D erra *só o i ao quadrado.* [p=0.3] {xe}E a E acha que *duas* potências seguidas se "
        "anulam. [p=0.2] Só *quatro* seguidas somam zero."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] i ao quadrado é menos um. [p=0.5] {b}Dois: "
        "[p=0.2] delta negativo: [p=0.2] nenhuma raiz real, [p=0.2] mas duas raízes complexas conjugadas. [p=0.5] "
        "{c}Três: [p=0.2] potência de i: [p=0.2] só importa o resto por quatro."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}*Dois mais três i,* [p=0.2] vezes *um menos i:* [p=0.3] no meio da conta [p=0.2] aparece um *menos três i "
        "ao quadrado.* [p=0.5] {b}O que fazer com ele [p=0.2] decide se você marca *a certa* ou *a pegadinha.* "
        "[p=0.4] {c}*Próximo episódio.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto vale i elevado a dois mil e trinta? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
