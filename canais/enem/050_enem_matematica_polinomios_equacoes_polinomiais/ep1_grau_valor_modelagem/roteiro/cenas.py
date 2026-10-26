# Roteiro — Polinômios e Equações Polinomiais, Episódio 1 de 5: polinômio, grau, valor numérico e modelagem
# Base: Estudos/Enem/estudos/01-matematica/35-polinomios-equacoes-polinomiais.html — seções 02 e 03 + Questões 1 e 8.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O PRÉDIO: o grau é o andar mais alto — o maior expoente que tem coeficiente diferente de zero.
#   O RAIO X: trocar x por 1 apaga as letras e deixa só a soma dos coeficientes; trocar por 0 apaga tudo o que tem x.
#   AS NOTAS FISCAIS: polinômios idênticos se conferem item por item, coeficiente com coeficiente.
#   A CAIXA DE PAPELÃO: três medidas de 1º grau multiplicadas dão um polinômio de grau 3.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: termos semelhantes e distributiva "todos com todos" e (−2)² = 4 (série de Expressões algébricas);
#   1 elevado a qualquer número dá 1 (série de Potenciação).
# Blocos = seções 02 e 03, com os exemplos do material. Exemplo NOSSO (marcado): no bloco b, a raiz usa
#   x² − 5x + 6 (P(2) = 0; P(4) = 2), porque o material não traz exemplo de raiz nesse trecho.
# Ressalva sobre o prompt: o gancho do usuário (mantido igual) já diz que a soma dos coeficientes de (x² − 3x + 3)^20
#   é 1, e o bloco d dá o grau 40 — os dois são a Questão 8 ("você faz"). Mantidos (desenho do usuário); na Q8 o novo é
#   fazer a conta sozinho e entender as quatro alternativas erradas.
# CORREÇÃO ao prompt/material (marcada): a conferência com x = 1 da Questão 1 dá 286 também nas alternativas B
#   (4x² − 78x + 360) e E (4x³ − 78x² + 360). O vídeo faz a conferência com x = 1 (como o prompt pede), avisa que ela
#   não basta e confere com x = 2: a caixa mede 20 × 11 × 2 = 440; D dá 440, B dá 220, E dá 80. Atalho verde nosso:
#   "confira com dois números".
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "soma dos coeficientes? troque x por 1 · termo independente?
#   troque x por 0"; cena verde "organize do maior para o menor expoente antes de ler o grau".
# QUESTÃO 1 (eu faço): V = x(24 − 2x)(15 − 2x) = 4x³ − 78x² + 360x (D). Erradas = material (A tira x uma vez só de cada
#   lado; B é só o fundo; C erra o sinal do meio; E não multiplica o 360 por x).
# QUESTÃO 8 (você faz): P(1) = (1 − 3 + 3)^20 = 1 (A). B 40 é o grau; C 3^20 é P(0); D 4^20 soma só os positivos de
#   dentro; E 7^20 é P(−1) (ignora os sinais).
# Nós fazemos (prompt): x³ − 4x² + 2x + 5 → P(0) = 5; P(1) = 4; P(−1) = −2.
# Frases-chave (meio e fim, idênticas): 1. Grau é o maior expoente que sobrevive.
#   2. P(1) soma os coeficientes; P(0) dá o termo independente. 3. Idênticos: coeficiente com coeficiente.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Polinômio do zero: grau, valor numérico e o truque do P(1) | Polinômios Ep. 1"
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
        "{a}*x ao quadrado menos três x mais três,* [p=0.2] elevado a *vinte,* [p=0.2] desenvolvido, [p=0.2] tem "
        "*dezenas de termos.* [p=0.4] {b}Quanto dá a soma de *todos os coeficientes?* [p=0.5] {c}Uma linha de conta: "
        "[p=0.3] *um.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Polinômios.* [p=0.4] {a}Ao final, [p=0.2] você vai *reconhecer um "
        "polinômio,* [p=0.2] {b}dizer o *grau* dele, [p=0.2] {c}calcular valores numéricos *de graça* [p=0.2] {d}e "
        "montar o polinômio do *volume de uma caixa.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Expressões algébricas: [p=0.2] juntar *termos semelhantes* "
        "[p=0.2] e a distributiva *todos com todos.* [p=0.4] {b}Ao trocar a letra por um negativo, [p=0.2] *parênteses:* "
        "[p=0.2] menos dois, ao quadrado, [p=0.2] dá *quatro.* [p=0.4] {c}E da Potenciação: [p=0.2] *um* elevado a "
        "qualquer número [p=0.2] dá *um.*"),

    # ================= CONCRETO: A CAIXA =================
    dict(id="04", block="caixa", text=
        "{t}Pegue uma folha de *papelão* retangular. [p=0.4] {a}Recorte um quadradinho em *cada canto.* [p=0.3] O lado "
        "do recorte é *x.* [p=0.4] {b}Dobre as abas: [p=0.2] vira uma *caixa sem tampa.* [p=0.4] {c}O volume *depende do x.* "
        "[p=0.3] {d}E a conta que dá esse volume [p=0.2] tem nome: [p=0.2] *polinômio.*"),

    # ================= BLOCO A: O QUE É POLINÔMIO =================
    dict(id="05", block="definicao", text=
        "{t}Mas o que é *polinômio?* [p=0.4] {a}*Polinômio:* [p=0.2] uma soma de termos com *x elevado a números "
        "naturais:* [p=0.2] zero, um, dois, três... [p=0.4] {b}*Coeficiente:* [p=0.2] o número que multiplica cada "
        "potência de x. [p=0.4] {c}*Termo independente:* [p=0.2] o número *sozinho,* sem x. [p=0.4] {d}E o "
        "*coeficiente dominante* [p=0.2] é o que acompanha a *maior* potência."),
    dict(id="06", block="grau", text=
        "{t}E o *grau?* [p=0.4] {a}Pense num *prédio:* [p=0.2] cada potência é um andar. [p=0.4] {b}*Grau:* "
        "[p=0.2] o *andar mais alto,* [p=0.2] o maior expoente com coeficiente *diferente de zero.* [p=0.4] {c}Quatro x "
        "ao cubo, menos setenta e oito x ao quadrado, mais trezentos e sessenta x: [p=0.2] *grau três.* [p=0.4] "
        "{d}E se o andar de cima for *m menos dois,* [p=0.2] vezes x ao quadrado? [p=0.3] Com m diferente de dois, "
        "[p=0.2] *grau dois.* [p=0.3] Com m igual a dois, [p=0.2] o andar *some:* [p=0.2] *grau um.*"),
    dict(id="07", block="nao_poli", text=
        "{t}E o que *não* é polinômio? [p=0.4] {a}x ao quadrado mais *um sobre x:* [p=0.2] um sobre x é x elevado a "
        "*menos um.* [p=0.2] Negativo não vale. [p=0.4] {b}*Raiz de x* mais três: [p=0.2] raiz é x elevado a *um "
        "meio.* [p=0.2] Fração também não vale. [p=0.4] {c}Expoente só *natural.*"),
    dict(id="08", block="atalho_ordem", text=
        "{t}Atalho. [p=0.4] {a}Antes de ler o grau e os coeficientes, [p=0.2] *organize:* [p=0.2] do *maior* para o "
        "*menor* expoente. [p=0.4] {b}O andar mais alto fica *na frente.*"),

    # ================= BLOCO B: VALOR NUMÉRICO E RAIZ =================
    dict(id="09", block="valor", text=
        "{t}E quanto *vale* um polinômio? [p=0.4] {a}*Valor numérico:* [p=0.2] P de a é o resultado de *trocar x por "
        "a.* [p=0.4] {b}Em x ao quadrado menos cinco x mais seis, [p=0.2] P de quatro é: [p=0.2] dezesseis, menos "
        "vinte, mais seis: [p=0.2] *dois.* [p=0.4] {c}E P de dois: [p=0.2] quatro, menos dez, mais seis: [p=0.2] "
        "*zero.* [p=0.4] {d}*Raiz:* [p=0.2] o número que faz o polinômio *dar zero.* [p=0.2] Dois é raiz."),

    # ================= BLOCO C: O RAIO X =================
    dict(id="10", block="raiox", text=
        "{t}Agora, *dois valores de graça.* [p=0.4] {a}Pegue dois x ao cubo, menos cinco x ao quadrado, mais x, mais "
        "sete. [p=0.4] {b}Troque x por *um.* [p=0.2] Um elevado a qualquer coisa é um: [p=0.2] as letras *somem.* "
        "[p=0.4] {c}Sobra dois, menos cinco, mais um, mais sete: [p=0.2] *cinco.* [p=0.2] É a *soma dos "
        "coeficientes.* [p=0.4] {d}É o *raio X:* [p=0.2] P de um mostra só os coeficientes. [p=0.4] {e}E P de *zero?* "
        "[p=0.2] Tudo o que tem x vira zero. [p=0.2] Sobra o *sete:* [p=0.2] o termo independente."),
    dict(id="11", block="raiox_pot", text=
        "{t}E para que serve isso? [p=0.4] {a}A soma dos coeficientes de *três x menos dois,* [p=0.2] elevado a *dez.* "
        "[p=0.4] {b}Sem desenvolver nada. [p=0.3] {c}Troque x por um: [p=0.2] três menos dois, [p=0.2] "
        "*um,* [p=0.2] elevado a dez: [p=0.2] *um.*"),
    dict(id="12", block="atalho_raiox", text=
        "{t}Atalho. [p=0.4] {a}Pediu a *soma dos coeficientes?* [p=0.2] Troque x por *um.* [p=0.4] {b}Pediu o *termo "
        "independente?* [p=0.2] Troque x por *zero.* [p=0.4] {c}Sem desenvolver nada."),

    # ================= BLOCO D: O GRAU NAS OPERAÇÕES =================
    dict(id="13", block="operacoes", text=
        "{t}E o grau, [p=0.2] quando a gente faz conta? [p=0.4] {a}No *produto,* [p=0.2] os graus *se somam:* "
        "[p=0.2] grau três vezes grau dois [p=0.2] dá *grau cinco.* [p=0.4] {b}Na *soma,* [p=0.2] o grau pode *cair:* "
        "[p=0.2] x ao quadrado mais um, [p=0.2] mais menos x ao quadrado mais três x: [p=0.2] os x ao quadrado se "
        "anulam. [p=0.2] Sobra *três x mais um.* [p=0.4] {c}E na *potência,* [p=0.2] o grau *multiplica:* [p=0.2] o "
        "polinômio do gancho [p=0.2] tem grau dois vezes vinte: [p=0.2] *quarenta.*"),

    # ================= BLOCO E: POLINÔMIOS IDÊNTICOS =================
    dict(id="14", block="identidade", text=
        "{t}Quando dois polinômios são *o mesmo?* [p=0.4] {a}*Polinômios idênticos:* [p=0.2] iguais para *todo x.* "
        "[p=0.2] Eles se conferem como duas *notas fiscais:* [p=0.2] item por item. [p=0.4] {b}a x ao quadrado, mais b "
        "menos um vezes x, mais três [p=0.2] contra dois x ao quadrado, mais cinco x, mais c. [p=0.4] {c}Andar de x ao "
        "quadrado: [p=0.2] *a é dois.* [p=0.3] Andar de x: [p=0.2] b menos um é cinco: [p=0.2] *b é seis.* [p=0.3] Sem "
        "x: [p=0.2] *c é três.* [p=0.4] {d}E o *polinômio nulo* [p=0.2] tem *todos* os coeficientes iguais a zero."),

    # ================= BLOCO F: MODELAR =================
    dict(id="15", block="modelar", text=
        "{t}E a caixa do começo? [p=0.4] {a}Comprimento, [p=0.2] largura [p=0.2] e altura: [p=0.2] cada medida é de "
        "*primeiro grau* em x. [p=0.4] {b}Volume é *comprimento vezes largura vezes altura.* [p=0.4] {c}Três graus um "
        "multiplicados: [p=0.2] um mais um mais um. [p=0.2] *Grau três.* [p=0.3] O volume da caixa é um polinômio do "
        "*terceiro grau.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}No polinômio *x ao cubo, menos quatro x ao quadrado, mais dois x, mais cinco,* [p=0.3] "
        "{b}calcule *P de zero,* [p=0.2] *P de um* [p=0.2] e *P de menos um.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}P de zero: [p=0.2] sobra o termo independente, [p=0.2] *cinco.* [p=0.4] {b}P de "
        "um: [p=0.2] a soma dos coeficientes: [p=0.2] um, menos quatro, mais dois, mais cinco: [p=0.2] *quatro.* "
        "[p=0.4] {c}P de menos um, [p=0.2] com parênteses: [p=0.2] menos um, menos quatro, menos dois, mais cinco: "
        "[p=0.2] *menos dois.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] grau é o maior expoente que sobrevive. [p=0.5] "
        "{b}Dois: [p=0.2] P de um soma os coeficientes; [p=0.2] P de zero dá o termo independente. [p=0.5] {c}Três: "
        "[p=0.2] idênticos: [p=0.2] coeficiente com coeficiente."),

    # ================= ERRO CLÁSSICO =================
    dict(id="19", block="erros", text=
        "{t}Agora, o erro clássico. [p=0.4] {a}Achar que a soma dos coeficientes é *P de zero.* [p=0.2] Em dois x ao "
        "cubo, menos cinco x ao quadrado, mais x, mais sete, [p=0.2] a pessoa responde *sete.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o zero *some com tudo.* [p=0.4] {c}Mas some com os *coeficientes* também. "
        "[p=0.2] Quem os *guarda* é o *um:* [p=0.2] a soma é *cinco.*"),

    # ================= QUESTÃO 1: EU FAÇO =================
    dict(id="20", block="q1", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}De uma folha de *vinte e quatro* por *quinze* "
        "centímetros, [p=0.2] recortam-se quatro quadrados de lado x, [p=0.2] e dobram-se as abas. [p=0.4] {b}O volume "
        "da caixa é dado por qual polinômio? [p=0.3] {qa}A começa com *x ao cubo.* [p=0.3] {qb}A B é de *grau dois.* "
        "[p=0.3] {qc}A C, [p=0.2] {qd}a D [p=0.2] {qe}e a E [p=0.2] são quase iguais: [p=0.2] mudam um *sinal* "
        "[p=0.2] ou um *x* no fim. [p=0.3] Repare bem na tela."),
    dict(id="21", block="q1", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Cada recorte tira x de *cada ponta.* [p=0.2] O comprimento fica "
        "*vinte e quatro menos dois x;* [p=0.2] a largura, *quinze menos dois x;* [p=0.2] a altura é *x.* [p=0.4] "
        "{b}O fundo é revisão: [p=0.2] todos com todos, [p=0.2] *trezentos e sessenta, menos setenta e oito x, mais "
        "quatro x ao quadrado.* [p=0.4] {c}O novo é multiplicar pela *altura x:* [p=0.2] cada expoente sobe um. "
        "[p=0.4] {d}*Quatro x ao cubo, menos setenta e oito x ao quadrado, mais trezentos e sessenta x.* [p=0.3] "
        "{ok}*Letra D!*"),
    dict(id="22", block="q1", text=
        "{t}Confiro com *x igual a um.* [p=0.4] {a}A caixa mede vinte e dois, por treze, por um: [p=0.2] *duzentos e "
        "oitenta e seis.* [p=0.3] E quatro, menos setenta e oito, mais trezentos e sessenta: [p=0.2] *duzentos e "
        "oitenta e seis.* [p=0.4] {b}Mas cuidado: [p=0.2] a B e a E *também* dão duzentos e oitenta e seis com x igual "
        "a um. [p=0.4] {c}Confiro com *dois:* [p=0.2] vinte, por onze, por dois: [p=0.2] *quatrocentos e quarenta.* "
        "[p=0.2] Só a D dá quatrocentos e quarenta."),
    dict(id="23", block="atalho_dois", text=
        "{t}Atalho. [p=0.4] {a}Para conferir um polinômio, [p=0.2] teste *dois números* pequenos. [p=0.4] {b}Um só "
        "pode coincidir *por acaso.*"),
    dict(id="24", block="q1", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A tira x *uma vez só* de cada lado. [p=0.4] {xb}A B é só o *fundo,* "
        "[p=0.2] grau dois: [p=0.2] área, não volume. [p=0.4] {xc}A C erra o *sinal* do termo do meio: "
        "[p=0.2] menos com mais dá *menos.* [p=0.4] {xe}E a E esquece de multiplicar o *trezentos e sessenta* pelo x."),

    # ================= QUESTÃO 8: VOCÊ FAZ =================
    dict(id="25", block="q8", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}O polinômio *x ao quadrado menos três x mais três,* [p=0.2] elevado a "
        "vinte, [p=0.2] tem muitos termos. [p=0.2] A soma de todos os seus coeficientes é: [p=0.3] {qa}A: um. [p=0.2] "
        "{qb}B: quarenta. [p=0.2] {qc}C: três elevado a vinte. [p=0.2] {qd}D: quatro elevado a vinte. [p=0.2] {qe}E: "
        "sete elevado a vinte. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q8", text=
        "{t}Vamos conferir. [p=0.3] {a}Soma dos coeficientes: [p=0.2] *P de um.* [p=0.3] Um, menos três, mais três: "
        "[p=0.2] *um.* [p=0.2] Um elevado a vinte: [p=0.2] *um.* [p=0.3] {ok}*Letra A!* [p=0.4] {xb}A B é o *grau.* "
        "[p=0.3] {xc}A C é *P de zero,* [p=0.2] o termo independente. [p=0.3] {xd}A D soma só os *positivos* de "
        "dentro. [p=0.3] {xe}E a E *ignora os sinais:* [p=0.2] é P de menos um."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] grau é o maior expoente que sobrevive. [p=0.5] "
        "{b}Dois: [p=0.2] P de um soma os coeficientes; [p=0.2] P de zero dá o termo independente. [p=0.5] {c}Três: "
        "[p=0.2] idênticos: [p=0.2] coeficiente com coeficiente."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Como saber o *resto* da divisão de *dois x ao cubo, menos x, mais cinco,* [p=0.2] por *x mais um,* [p=0.2] "
        "*sem fazer a divisão?* [p=0.5] {b}Trocando x por *um único número.* [p=0.4] {c}*Próximo episódio.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha ouvido falar no truque do P de um? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
