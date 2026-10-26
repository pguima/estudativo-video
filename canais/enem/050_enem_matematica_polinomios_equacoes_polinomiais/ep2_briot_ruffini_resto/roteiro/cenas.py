# Roteiro — Polinômios e Equações Polinomiais, Episódio 2 de 5: divisão, Briot-Ruffini e o teorema do resto
# Base: Estudos/Enem/estudos/01-matematica/35-polinomios-equacoes-polinomiais.html — seções 04 e 05 + Questões 2 e 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A ESTEIRA: Briot-Ruffini — desce o primeiro, multiplica pela raiz, soma com o próximo, e repete.
#   O PEDÁGIO: o teorema do resto — em vez de percorrer a divisão inteira, substitua a raiz do divisor e pague só o resto.
#   O LADO OPOSTO: a raiz do divisor mora do lado oposto — x − 2 mora em 2; x + 3 mora em −3.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: dividendo = divisor × quociente + resto, resto menor que o divisor (série de Divisibilidade);
#   valor numérico (episódio 1); resolver um sistema 2 × 2 (série de Sistemas lineares).
# Blocos = seções 04 e 05, com os exemplos do material (bloco b: 2x³ − 3x² − 5x + 6 por x − 2 → 2, 1, −3, resto 0;
#   bloco d: o gancho; bloco e: x³ + kx − 4 por x − 2 → k = −2).
# Exemplos NOSSOS (marcados):
#   - bloco d: a conferência do gancho pela esteira (2, 0, −1, 5 com −1 → 2, −2, 1, resto 4);
#   - bloco f: restos 5 por x − 1 e 7 por x − 2 → m + n = 5 e 2m + n = 7 → resto 2x + 3 (a Q9 é "você faz";
#     o material só descreve o método);
#   - erro 1: x³ − 4x + 1 por x − 2 (sem o zero dá −3; certo 1 = P(2)). Com x − 1 o erro daria −2 por coincidência;
#   - erro 2: x² + 2x − 5 por x + 3 (certo P(−3) = −2; errado P(3) = 10);
#   - erro 3: x² − 3x + 4 por x − 2 (certo P(2) = 2; errado P(−2) = 14).
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO "antes da esteira: todos os coeficientes e a raiz do lado
#   oposto", "pediu só o resto? calcule P(a)" e "no sistema, subtraia as equações: o n some".
# QUESTÃO 2 (eu faço): P(3) = 0 → 27 − 18 + 3k + 6 = 0 → 3k = −15 → k = −5 (C). Erradas = material (A para em 3k = −15;
#   B usa P(−3): −39 − 3k = 0 → −13; D erra o sinal no fim → 5; E combina os dois → 13). Conferência: P(3) = 0 com k = −5.
# QUESTÃO 9 (você faz, com a dica do prompt antes da pausa): R = mx + n; m + n = 3 e −2m + n = −6 → m = 3, n = 0 →
#   resto 3x (B). Erradas = material (A soma os restos; C multiplica; D toma o segundo resto como termo independente;
#   E troca as raízes: R(1) = −6 e R(−2) = 3 → −3x − 3).
# Nós fazemos (prompt): x³ − 4x + 1 por x − 1 → 1, 0, −4, 1 → 1, 1, −3, resto −2; P(1) = −2.
# Frases-chave (meio e fim, idênticas): 1. O resto por x − a é P(a). 2. Desce, multiplica pela raiz, soma.
#   3. Não pule o zero; x + 3 usa −3.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Briot-Ruffini e o teorema do resto: o resto sem dividir | Polinômios Ep. 2"
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
        "{a}Resto da divisão de *dois x ao cubo, menos x, mais cinco,* [p=0.2] por *x mais um?* [p=0.5] {b}Sem armar a "
        "conta: [p=0.2] troque x por *menos um.* [p=0.4] {c}Dá menos dois, mais um, mais cinco [p=0.2] igual a "
        "*quatro.* [p=0.4] {d}*Pronto.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Polinômios.* [p=0.4] {a}Ao final, [p=0.2] você vai *dividir por x "
        "menos a em uma linha,* [p=0.3] {b}achar *restos sem dividir* [p=0.3] {c}e descobrir o *valor de k* que deixa "
        "um polinômio *divisível.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Divisibilidade: [p=0.2] *dividendo é divisor vezes "
        "quociente, mais resto,* [p=0.2] e o resto é *menor* que o divisor. [p=0.4] {b}Do episódio um: [p=0.2] *P de "
        "a* é trocar x por a. [p=0.4] {c}E da série de Sistemas: [p=0.2] resolver *duas equações* com *duas "
        "incógnitas.*"),

    # ================= CONCRETO: AS BALAS =================
    dict(id="04", block="balas", text=
        "{t}Comece pelos números. [p=0.3] {a}*Dezessete balas* para *cinco crianças.* [p=0.4] {b}Cada uma ganha *três,* "
        "[p=0.2] e sobram *duas.* [p=0.4] {c}Dezessete é igual a cinco vezes três, mais dois. [p=0.4] {d}*Dividendo:* "
        "[p=0.2] o que se divide, dezessete. [p=0.2] *Divisor:* [p=0.2] por quanto, cinco. [p=0.2] *Quociente:* "
        "[p=0.2] quanto cada um ganha, três. [p=0.2] *Resto:* [p=0.2] o que sobra, dois. [p=0.4] {e}E *divisível* "
        "[p=0.2] quer dizer: [p=0.2] *resto zero.*"),

    # ================= BLOCO A: A RELAÇÃO =================
    dict(id="05", block="relacao", text=
        "{t}E com polinômios? [p=0.4] {a}A mesma conta: [p=0.2] *P é igual a D vezes Q, mais R.* [p=0.4] {b}O resto "
        "tem grau *menor* que o divisor. [p=0.4] {c}E o grau do quociente [p=0.2] é o grau de P *menos* o grau de D: "
        "[p=0.2] grau três dividido por grau um [p=0.2] dá quociente de *grau dois.*"),
    dict(id="06", block="grau_resto", text=
        "{t}E que cara tem o resto? [p=0.4] {a}Divisor de *grau um:* [p=0.2] o resto tem grau zero. [p=0.2] É um "
        "*número.* [p=0.4] {b}Divisor de *grau dois:* [p=0.2] o resto tem no máximo grau um. [p=0.2] Ele tem a cara "
        "*a x mais b.*"),

    # ================= BLOCO B: A ESTEIRA =================
    dict(id="07", block="esteira_def", text=
        "{t}E como dividir *rápido* por x menos um número? [p=0.4] {a}*Dispositivo de Briot-Ruffini:* [p=0.2] uma "
        "tabelinha que faz essa divisão *em uma linha.* [p=0.4] {b}À esquerda vai a *raiz do divisor:* [p=0.2] o "
        "número que zera o divisor. [p=0.4] {c}Ela mora do *lado oposto:* [p=0.2] x menos dois mora em *dois;* "
        "[p=0.2] x mais três mora em *menos três.*"),
    dict(id="08", block="esteira", text=
        "{t}Vamos dividir *dois x ao cubo, menos três x ao quadrado, menos cinco x, mais seis,* [p=0.2] por *x menos "
        "dois.* [p=0.4] {a}Pense numa *esteira.* [p=0.2] O primeiro coeficiente *desce:* [p=0.2] *dois.* [p=0.4] {b}Multiplica "
        "pela raiz e soma com o próximo: [p=0.2] dois vezes dois, quatro, [p=0.2] menos três: [p=0.2] *um.* [p=0.4] "
        "{c}De novo: [p=0.2] dois vezes um, dois, [p=0.2] menos cinco: [p=0.2] *menos três.* [p=0.4] {d}E o último: "
        "[p=0.2] dois vezes menos três, menos seis, [p=0.2] mais seis: [p=0.2] *zero.*"),
    dict(id="09", block="esteira", text=
        "{t}E como se lê a esteira? [p=0.4] {a}Os primeiros números são o *quociente,* [p=0.2] com *um grau a menos:* "
        "[p=0.2] *dois x ao quadrado, mais x, menos três.* [p=0.4] {b}O último é o *resto:* [p=0.2] *zero.* [p=0.4] "
        "{c}Resto zero quer dizer que *dois é raiz* do polinômio."),
    dict(id="10", block="atalho_esteira", text=
        "{t}Atalho. [p=0.4] {a}Antes de ligar a esteira, [p=0.2] escreva *todos* os coeficientes, [p=0.2] do maior para o "
        "menor expoente. [p=0.4] {b}E ponha à esquerda a raiz do *lado oposto.* [p=0.4] {c}Depois é só repetir: "
        "[p=0.2] *desce, multiplica pela raiz, soma.*"),

    # ================= BLOCO C: AS DUAS ARMADILHAS DA ESTEIRA =================
    dict(id="11", block="armadilhas", text=
        "{t}E onde a esteira *trava?* [p=0.4] {a}Em *x ao cubo, menos quatro x, mais um,* [p=0.2] *falta* o x ao "
        "quadrado. [p=0.4] {b}Ele entra com *zero:* [p=0.2] os coeficientes são *um, zero, menos quatro, um.* [p=0.2] "
        "Sem o zero, a conta inteira *escorrega* uma casa. [p=0.4] {c}E para dividir por *x mais três,* [p=0.2] a raiz "
        "do lado oposto: [p=0.2] *menos três.*"),

    # ================= BLOCO D: O TEOREMA DO RESTO =================
    dict(id="12", block="resto", text=
        "{t}E se a questão quiser *só o resto?* [p=0.4] {a}*Teorema do resto:* [p=0.2] o resto da divisão por x menos "
        "a [p=0.2] é *P de a.* [p=0.4] {b}Por quê? [p=0.2] Troque x por a em P igual a x menos a, vezes Q, mais R. "
        "[p=0.3] O x menos a vira *zero* [p=0.2] e leva o Q junto. [p=0.2] Sobra *só o R.* [p=0.4] {c}É o *pedágio:* "
        "[p=0.2] em vez de percorrer a divisão inteira, [p=0.2] você substitui a raiz [p=0.2] e paga *só o resto.*"),
    dict(id="13", block="resto_ex", text=
        "{t}Volte ao gancho. [p=0.4] {a}Dois x ao cubo, menos x, mais cinco, [p=0.2] por x mais um. [p=0.3] A raiz do "
        "divisor é *menos um.* [p=0.4] {b}P de menos um: [p=0.2] menos dois, mais um, mais cinco: [p=0.2] *quatro.* "
        "[p=0.4] {c}Na esteira, com o zero do x ao quadrado: [p=0.2] dois, menos dois, um... [p=0.2] {c2}e o resto, "
        "*quatro.* [p=0.3] Os dois caminhos *batem.*"),
    dict(id="14", block="atalho_resto", text=
        "{t}Atalho. [p=0.4] {a}Pediu *só o resto* da divisão por x menos a? [p=0.2] *Não divida:* [p=0.2] calcule *P de "
        "a.* [p=0.4] {b}Pediu o *quociente?* [p=0.2] Aí, sim, *esteira.*"),

    # ================= BLOCO E: D'ALEMBERT =================
    dict(id="15", block="dalembert", text=
        "{t}E quando a divisão é *exata?* [p=0.4] {a}*Teorema de D'Alembert:* [p=0.2] P é divisível por x menos a "
        "[p=0.2] *se, e só se,* [p=0.2] *P de a é zero.* [p=0.2] Ou seja, a é raiz. [p=0.4] {b}Quanto vale k para *x ao "
        "cubo, mais k x, menos quatro* [p=0.2] ser divisível por *x menos dois?* [p=0.4] {c}P de dois igual a zero: "
        "[p=0.2] oito, mais dois k, menos quatro, igual a zero. [p=0.3] Dois k é menos quatro: [p=0.2] *k é menos "
        "dois.*"),

    # ================= BLOCO F: RESTO POR GRAU 2 =================
    dict(id="16", block="grau2", text=
        "{t}E se o divisor for de *grau dois?* [p=0.4] {a}Por exemplo, x menos um, vezes x menos dois. [p=0.3] O resto "
        "tem a cara *m x mais n.* [p=0.4] {b}Nas raízes do divisor, [p=0.2] P e o resto *dão o mesmo valor.* [p=0.4] "
        "{c}Se o resto por x menos um é *cinco,* [p=0.2] m mais n é cinco. [p=0.3] Se o resto por x menos dois é *sete,* "
        "[p=0.2] dois m mais n é sete. [p=0.4] {d}Um sistema dois por dois: [p=0.2] m é *dois,* n é *três.* [p=0.2] "
        "Resto: *dois x mais três.*"),
    dict(id="17", block="atalho_sistema", text=
        "{t}Atalho. [p=0.4] {a}No sistema, [p=0.2] *subtraia* uma equação da outra: [p=0.2] o *n some* [p=0.2] e o m "
        "aparece sozinho. [p=0.4] {b}Depois, confira: [p=0.2] o resto tem de dar os *dois* valores do enunciado."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Divida *x ao cubo, menos quatro x, mais um,* [p=0.2] por *x menos um,* [p=0.2] com a "
        "esteira. [p=0.4] {b}E confira o resto pelo *teorema.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Coeficientes, *com o zero:* [p=0.2] um, zero, menos quatro, um. [p=0.2] Raiz: *um.* "
        "[p=0.4] {b}Desce *um.* [p=0.2] {b2}Um mais zero: [p=0.2] *um.* [p=0.2] {b3}Um menos quatro: [p=0.2] *menos três.* "
        "[p=0.2] {b4}Menos três mais um: [p=0.2] *menos dois.* [p=0.4] {c}Quociente: [p=0.2] *x ao quadrado, mais x, menos "
        "três.* [p=0.2] Resto: [p=0.2] *menos dois.* [p=0.4] {d}E P de um: [p=0.2] um, menos quatro, mais um: [p=0.2] "
        "*menos dois.* [p=0.2] Bateu!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o resto por x menos a é P de a. [p=0.5] {b}Dois: "
        "[p=0.2] desce, multiplica pela raiz, soma. [p=0.5] {c}Três: [p=0.2] não pule o zero; [p=0.2] x mais três usa "
        "menos três."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] esteira *sem o zero.* [p=0.2] Em x ao cubo, menos "
        "quatro x, mais um, por x menos dois, [p=0.2] a pessoa usa um, menos quatro, um, [p=0.2] e o resto sai *menos "
        "três.* [p=0.4] {b}Parece certo, [p=0.2] porque o zero *não aparece* no polinômio. [p=0.4] {c}Mas a casa do x "
        "ao quadrado existe. [p=0.2] Com o zero, o resto é *um.* [p=0.2] E P de dois confirma: [p=0.2] *um.*"),
    dict(id="22", block="erros", text=
        "{t}Segundo: [p=0.2] dividir por *x mais três* usando *três.* [p=0.4] {a}Em x ao quadrado, mais dois x, menos "
        "cinco, [p=0.2] a pessoa calcula P de três: [p=0.2] *dez.* [p=0.4] {b}Parece certo, [p=0.2] porque o três *está "
        "escrito* ali. [p=0.4] {c}Mas a raiz mora do lado oposto: [p=0.2] P de *menos três* [p=0.2] dá *menos dois.*"),
    dict(id="23", block="erros", text=
        "{t}Terceiro: [p=0.2] achar que o resto por x menos a [p=0.2] é *P de menos a.* [p=0.4] {a}Em x ao quadrado, "
        "menos três x, mais quatro, [p=0.2] por x menos dois, [p=0.2] a pessoa calcula P de menos dois: [p=0.2] "
        "*catorze.* [p=0.4] {b}Parece certo, [p=0.2] porque a pessoa decorou que *o sinal troca.* [p=0.4] {c}E troca "
        "mesmo: [p=0.2] x *menos* dois vira *mais* dois. [p=0.2] O resto é *P de dois:* [p=0.2] *dois.*"),

    # ================= QUESTÃO 2: EU FAÇO =================
    dict(id="24", block="q2", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}O polinômio *x ao cubo, menos dois x ao quadrado, "
        "mais k x, mais seis* [p=0.2] é divisível por *x menos três.* [p=0.2] O valor de k é: [p=0.3] {qa}A: menos "
        "quinze. [p=0.2] {qb}B: menos treze. [p=0.2] {qc}C: menos cinco. [p=0.2] {qd}D: cinco. [p=0.2] {qe}E: treze."),
    dict(id="25", block="q2", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Divisível por x menos três: [p=0.2] raiz do divisor, *três.* [p=0.2] "
        "D'Alembert: [p=0.2] *P de três é zero.* [p=0.4] {b}Vinte e sete, menos dezoito, mais três k, mais seis, "
        "[p=0.2] igual a zero. [p=0.3] Quinze mais três k é zero: [p=0.2] três k é *menos quinze.* [p=0.4] {c}Divide "
        "por três: [p=0.2] *k é menos cinco.* [p=0.3] {ok}*Letra C!* [p=0.4] {d}Confiro: [p=0.2] com k igual a menos "
        "cinco, [p=0.2] vinte e sete, menos dezoito, menos quinze, mais seis: [p=0.2] *zero.*"),
    dict(id="26", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *para* em três k igual a menos quinze, [p=0.2] sem dividir por três. "
        "[p=0.4] {xb}A B usa *P de menos três,* [p=0.2] a raiz com o sinal trocado: [p=0.2] dá menos treze. [p=0.4] "
        "{xd}A D erra o *sinal* na última passagem. [p=0.4] {xe}E a E *junta os dois erros:* [p=0.2] P de menos três "
        "e o sinal trocado."),

    # ================= QUESTÃO 9: VOCÊ FAZ =================
    dict(id="27", block="q9", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um polinômio P, dividido por *x menos um,* [p=0.2] deixa resto *três;* "
        "[p=0.3] dividido por *x mais dois,* [p=0.2] deixa resto *menos seis.* [p=0.3] O resto da divisão de P por x "
        "menos um, vezes x mais dois, é: [p=0.3] {qa}A: menos três. [p=0.2] {qb}B: três x. [p=0.2] {qc}C: menos dezoito. "
        "[p=0.2] {qd}D: três x menos seis. [p=0.2] {qe}E: menos três x, menos três. [p=0.4] {dica}Uma dica: [p=0.2] o "
        "resto tem grau no máximo um: [p=0.2] *m x mais n.* [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}Vamos conferir. [p=0.3] {a}As raízes do divisor: [p=0.2] *um* e *menos dois.* [p=0.4] {b}P de um é três: "
        "[p=0.2] *m mais n é três.* [p=0.3] P de menos dois é menos seis: [p=0.2] *menos dois m, mais n, é menos seis.* "
        "[p=0.4] {c}Subtraia: [p=0.2] *três m é nove,* [p=0.2] m é *três.* [p=0.2] E n é *zero.* [p=0.4] {d}Resto: "
        "[p=0.2] *três x.* [p=0.3] {ok}*Letra B!* [p=0.3] Confere: [p=0.2] três vezes um, três; [p=0.2] três vezes menos "
        "dois, menos seis."),
    dict(id="29", block="q9", text=
        "{t}E as erradas? [p=0.3] {xa}A A *soma* os dois restos. [p=0.4] {xc}A C *multiplica* os dois restos. [p=0.4] "
        "{xd}A D acerta o m, [p=0.2] mas usa o segundo resto como *termo independente.* [p=0.4] {xe}E a E *troca as "
        "raízes:* [p=0.2] põe o menos seis no um, [p=0.2] e o três no menos dois."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o resto por x menos a é P de a. [p=0.5] {b}Dois: "
        "[p=0.2] desce, multiplica pela raiz, soma. [p=0.5] {c}Três: [p=0.2] não pule o zero; [p=0.2] x mais três usa "
        "menos três."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O lucro de uma fábrica é *x ao cubo, menos seis x ao quadrado, mais onze x, menos seis,* [p=0.3] e você sabe "
        "que ele *zera em x igual a um.* [p=0.4] {b}Como achar os *outros dois valores* que zeram o lucro? [p=0.4] "
        "{c}Com a *esteira de hoje.* [p=0.3] {d}*Próximo episódio.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha usado o teorema do resto? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
