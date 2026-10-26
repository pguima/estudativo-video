# Roteiro — Matrizes e Operações, Episódio 2 de 5: operações casa a casa (igualdade, soma e número vezes matriz)
# Base: Estudos/Enem/estudos/01-matematica/33-matrizes-operacoes.html — seção 04 + Questão 8 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   AS FOLHAS TRANSPARENTES: somar matrizes é sobrepor duas folhas da mesma planilha; cada casa só conversa com a de baixo.
#   O AUMENTO GERAL: número vezes matriz atinge TODO mundo, não só a primeira linha (o carimbo ×3 em cada casa).
#   O SISTEMA DISFARÇADO: igualdade de matrizes vira uma equação por casa.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: o endereço a_ij (ep. 1), o método da adição (série de Sistemas: x + y = 7 e x − y = 1), 0,4 · 5 = 2.
# Blocos = seção 04 (igualdade → x = 4, y = 3; (1 4 / 2 0) + (3 −1 / 5 2) = (4 3 / 7 2); 3 · (1 4 / 2 0) = (3 12 / 6 0)).
# Exemplos NOSSOS (marcados), para não adiantar as casas da Questão 8:
#   bloco d: um aluno com notas 5 e 8, pesos 0,4 e 0,6 → 2 + 4,8 = 6,8 (o par 5/8 não existe na Q8);
#   bloco e: 2X + A = B com A = (1 4 / 2 0) e B = (5 6 / 8 2) → B − A = (4 2 / 6 2) → X = (2 1 / 3 1).
# Nós fazemos (prompt): 2A − B com A = (2 5 / 1 3), B = (4 1 / 3 7) → 2A = (4 10 / 2 6) → (0 9 / −1 −1).
# Acréscimos NOSSOS (marcados): duas cenas verdes de ATALHO — "antes de qualquer conta, confira a ordem; na igualdade,
#   some as duas equações e o y some" (cena 09) e "a média ponderada sempre fica ENTRE as duas notas, mais perto da nota
#   de peso maior" (cena 11, usada como conferência na Q8). Definições em uma frase: mesma ordem, elementos
#   correspondentes, igualdade de matrizes, matriz nula / elemento neutro, matriz oposta, média ponderada.
# QUESTÃO 8 em três tempos: eu faço m11 = 2 + 4,2 = 6,2; nós fazemos m12 = 6,2 e m21 = 5,8; você faz (pausa)
#   m22 = 6,4, m31 = 6,0 e m32 = 5,4. São 4 médias ≥ 6,0 (o 6,0 conta): letra D. Erradas = material (A conta os alunos
#   aprovados nas duas disciplinas, só o aluno 1; B conta as médias abaixo de 6, que são 2; C troca os pesos e chega a 3;
#   E usa a média simples e chega a 5).
# Frases-chave (meio e fim, idênticas): 1. Soma e igualdade: casa com casa, na mesma ordem.
#   2. Número vezes matriz atinge todas as casas. 3. Igualdade de matrizes vira um sistema.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Somar matrizes e multiplicar por número: casa com casa | Matrizes Ep. 2"
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
        "{a}Três alunos, [p=0.2] duas disciplinas, [p=0.2] duas provas: [p=0.3] são *seis médias ponderadas.* [p=0.5] "
        "{b}Com matrizes, [p=0.2] você escreve *uma conta só,* [p=0.2] zero vírgula quatro A mais zero vírgula seis B, "
        "[p=0.4] {c}e ainda escapa da pegadinha [p=0.2] de que *seis vírgula zero* [p=0.2] *também aprova.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Matrizes.* [p=0.4] {a}Ao final, [p=0.2] você vai *somar matrizes,* "
        "[p=0.2] *multiplicar por número* [p=0.4] {b}e resolver *igualdades de matrizes* [p=0.2] sem errar uma casa."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes. [p=0.3] {a}Do episódio um: [p=0.2] *a, i, j* [p=0.2] é o endereço: [p=0.2] linha i, "
        "coluna j. [p=0.4] {b}Da série de Sistemas: [p=0.2] x mais y igual a sete [p=0.2] e x menos y igual a um. "
        "[p=0.2] *Somando* as duas, [p=0.2] o y some: [p=0.2] dois x igual a oito. [p=0.4] {c}E zero vírgula quatro "
        "vezes cinco [p=0.2] dá *dois.*"),

    # ================= CONCRETO =================
    dict(id="04", block="planilhas", text=
        "{t}Imagine *duas planilhas* de notas: [p=0.4] {a}a da *prova um* [p=0.2] e a da *prova dois.* [p=0.4] {b}Os mesmos alunos nas linhas, [p=0.2] as mesmas disciplinas "
        "nas colunas. [p=0.4] {c}Quer juntar as duas? [p=0.2] *Sobreponha as folhas:* [p=0.2] cada casa só conversa "
        "[p=0.2] com a casa que está *embaixo dela.*"),
    dict(id="05", block="definicoes", text=
        "{t}Isso tem dois nomes. [p=0.4] {a}*Mesma ordem:* [p=0.2] o mesmo número de linhas [p=0.2] e de colunas. "
        "[p=0.4] {b}*Elementos correspondentes:* [p=0.2] os que moram no *mesmo endereço,* [p=0.2] um em cada matriz."),

    # ================= BLOCO A: IGUALDADE =================
    dict(id="06", block="igualdade", text=
        "{t}Quando duas matrizes são *iguais?* [p=0.4] {a}*Igualdade de matrizes:* [p=0.2] mesma ordem [p=0.2] e casa "
        "por casa igual. [p=0.4] {b}Olhe esta: [p=0.2] x mais y, três, dois, x menos y [p=0.2] igual a sete, três, "
        "dois, um. [p=0.4] {c}Cada casa vira uma equação: [p=0.2] é um *sistema disfarçado.* [p=0.4] {d}Somando: [p=0.2] *x igual a quatro.* [p=0.2] E *y igual a "
        "três.*"),

    # ================= BLOCO B: SOMA E SUBTRAÇÃO =================
    dict(id="07", block="soma", text=
        "{t}E como se *soma?* [p=0.4] {a}Uma folha sobre a outra. [p=0.2] Um, quatro, dois, zero [p=0.2] mais três, "
        "menos um, cinco, dois. [p=0.4] {b}Primeira casa: [p=0.2] um mais três, *quatro.* [p=0.3] Depois quatro menos "
        "um, *três.* [p=0.3] {c}Dois mais cinco, *sete.* [p=0.2] Zero mais dois, *dois.* [p=0.4] {d}Subtração: "
        "[p=0.2] casa menos casa. [p=0.2] Sempre na *mesma ordem.*"),

    # ================= BLOCO C: NÚMERO VEZES MATRIZ =================
    dict(id="08", block="numero", text=
        "{t}E *três vezes* uma matriz? [p=0.4] {a}É um *aumento geral:* [p=0.2] *todo mundo* recebe. [p=0.4] {b}Três "
        "vezes um, *três.* [p=0.2] Três vezes quatro, *doze.* [p=0.3] {c}Três vezes dois, *seis.* [p=0.2] Três vezes "
        "zero, *zero.* [p=0.4] {d}O carimbo bate em *todas as casas,* [p=0.2] até a última."),
    dict(id="09", block="atalho_ordem", text=
        "{t}Atalho. [p=0.4] {a}Antes de qualquer conta, [p=0.2] *confira a ordem:* [p=0.2] se as matrizes têm tamanhos "
        "diferentes, [p=0.2] a soma nem existe. [p=0.4] {b}E na igualdade, [p=0.2] *some as duas equações:* [p=0.2] o y "
        "some na hora."),

    # ================= BLOCO D: MÉDIA PONDERADA =================
    dict(id="10", block="media", text=
        "{t}E as duas planilhas? [p=0.4] {a}*Média ponderada:* [p=0.2] a média em que cada nota tem um *peso.* "
        "[p=0.4] {b}Com pesos zero vírgula quatro e zero vírgula seis: [p=0.2] *M igual a zero vírgula quatro A mais "
        "zero vírgula seis B.* [p=0.4] {c}Um aluno tirou *cinco* na prova um [p=0.2] e *oito* na prova dois. [p=0.4] "
        "{d}Zero vírgula quatro vezes cinco, *dois.* [p=0.2] Zero vírgula seis vezes oito, *quatro vírgula oito.* "
        "[p=0.3] Média: [p=0.2] *seis vírgula oito.* [p=0.4] {e}Na matriz, [p=0.2] essa conta é feita *posição por "
        "posição.*"),
    dict(id="11", block="atalho_media", text=
        "{t}Atalho para conferir. [p=0.4] {a}A média ponderada fica sempre *entre* as duas notas. [p=0.4] {b}E mais "
        "perto da nota de *peso maior.* [p=0.3] Entre cinco e oito, [p=0.2] perto do oito: [p=0.2] seis vírgula oito "
        "*confere.*"),

    # ================= BLOCO E: PROPRIEDADES =================
    dict(id="12", block="propriedades", text=
        "{t}E as regras dos números? [p=0.4] {a}Na soma, [p=0.2] a ordem *não importa.* [p=0.4] {b}A *matriz nula,* "
        "[p=0.2] toda de zeros, [p=0.2] é o *elemento neutro:* [p=0.2] não muda nada. [p=0.3] E a *oposta,* menos A, "
        "[p=0.2] troca o sinal de cada casa. [p=0.4] {c}Por isso, "
        "[p=0.2] dois X mais A igual a B [p=0.2] se resolve como no *primeiro grau:* [p=0.2] *X igual a B menos A, "
        "dividido por dois.* [p=0.4] {d}Com A um, quatro, dois, zero [p=0.2] e B cinco, seis, oito, dois: [p=0.2] B "
        "menos A dá quatro, dois, seis, dois. [p=0.3] Dividindo: [p=0.2] *dois, um, três, um.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}A é dois, cinco, um, três. [p=0.2] B é quatro, um, três, sete. [p=0.4] {b}Quanto é "
        "*dois A menos B?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Primeiro o carimbo, [p=0.2] em todas as casas: [p=0.2] dois A é *quatro, dez, "
        "dois, seis.* [p=0.4] {b}Agora casa menos casa: [p=0.2] quatro menos quatro, *zero.* [p=0.2] Dez menos um, "
        "*nove.* [p=0.3] {c}Dois menos três, *menos um.* [p=0.2] Seis menos sete, *menos um.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] soma e igualdade: [p=0.2] casa com casa, [p=0.2] na "
        "mesma ordem. [p=0.5] {b}Dois: [p=0.2] número vezes matriz [p=0.2] atinge todas as casas. [p=0.5] {c}Três: "
        "[p=0.2] igualdade de matrizes [p=0.2] vira um sistema."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] em três vezes A, [p=0.2] multiplicar *só a "
        "primeira linha.* [p=0.4] {b}Parece certo, [p=0.2] porque na conta de números [p=0.2] o três aparece uma vez "
        "só. [p=0.4] {c}Mas é aumento geral: [p=0.2] o carimbo vai em *todas as casas.*"),
    dict(id="17", block="erros", text=
        "{a}Segundo: [p=0.2] somar matrizes de *ordens diferentes.* [p=0.4] {b}Parece certo, [p=0.2] porque sempre dá "
        "para somar *números.* [p=0.4] {c}Mas uma casa sem par [p=0.2] não tem com quem somar: [p=0.2] a soma *não "
        "existe.*"),

    # ================= QUESTÃO 8 EM TRÊS TEMPOS =================
    dict(id="18", block="q8", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}Três alunos nas linhas, [p=0.2] duas disciplinas "
        "nas colunas. [p=0.2] *A* tem as notas da prova um, [p=0.2] *B* as da prova dois. [p=0.4] {b}A média é M igual a "
        "zero vírgula quatro A mais zero vírgula seis B, [p=0.2] e aprova quem tem *seis vírgula zero ou mais.* "
        "[p=0.4] {c}Quantos dos seis elementos de M [p=0.2] são *maiores ou iguais a seis vírgula zero?* [p=0.3] "
        "{qa}A: um. [p=0.2] {qb}B: dois. [p=0.2] {qc}C: três. [p=0.2] {qd}D: quatro. [p=0.2] {qe}E: cinco."),
    dict(id="19", block="q8", text=
        "{t}A primeira casa, [p=0.2] *eu faço.* [p=0.4] {a}Linha um, coluna um: [p=0.2] *cinco* em A [p=0.2] e *sete* "
        "em B. [p=0.4] {b}Zero vírgula quatro vezes cinco, *dois.* [p=0.2] Zero vírgula seis vezes sete, *quatro "
        "vírgula dois.* [p=0.4] {c}M um um: [p=0.2] *seis vírgula dois.* [p=0.2] Entre cinco e sete, [p=0.2] perto do "
        "sete: [p=0.2] confere."),
    dict(id="20", block="q8", text=
        "{t}As próximas duas, [p=0.2] *nós fazemos.* [p=0.4] {a}M um dois: [p=0.2] oito e cinco. [p=0.2] Três "
        "vírgula dois mais três: [p=0.2] *seis vírgula dois.* [p=0.4] {b}M dois um: [p=0.2] sete e cinco. [p=0.2] Dois "
        "vírgula oito mais três: [p=0.2] *cinco vírgula oito.*"),
    dict(id="21", block="q8", text=
        "{t}As últimas três, [p=0.2] *você faz.* [p=0.4] {a}M dois dois, [p=0.2] M três um [p=0.2] e M três dois. "
        "[p=0.3] Depois, [p=0.2] conte. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q8", text=
        "{t}Vamos conferir. [p=0.3] {a}Quatro e oito: [p=0.2] um vírgula seis mais quatro vírgula oito, [p=0.2] *seis "
        "vírgula quatro.* [p=0.4] {b}Seis e seis: [p=0.2] *seis vírgula zero.* [p=0.3] {c}Seis e cinco: [p=0.2] *cinco "
        "vírgula quatro.* [p=0.4] {d}Agora a contagem. [p=0.2] O seis vírgula zero *conta:* [p=0.2] o critério é "
        "*maior ou igual.* [p=0.4] {e}São *quatro* médias. [p=0.3] {ok}*Letra D!*"),
    dict(id="23", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A conta *alunos* aprovados nas duas disciplinas, [p=0.2] só o primeiro, "
        "[p=0.2] e não as médias. [p=0.4] {xb}A B conta as médias *abaixo* de seis. [p=0.4] {xc}A C *troca os pesos.* "
        "[p=0.4] {xe}E a E usa a *média simples,* [p=0.2] que deixa só um valor abaixo de seis."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="24", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] soma e igualdade: [p=0.2] casa com casa, "
        "[p=0.2] na mesma ordem. [p=0.5] {b}Dois: [p=0.2] número vezes matriz [p=0.2] atinge todas as casas. [p=0.5] "
        "{c}Três: [p=0.2] igualdade de matrizes [p=0.2] vira um sistema."),

    # ================= PONTE E CTA =================
    dict(id="25", block="ponte", text=
        "{a}Uma filial compra *dez quilos de arroz,* [p=0.2] *cinco quilos de feijão* [p=0.2] e *quatro litros de "
        "óleo;* [p=0.3] o fornecedor cobra *cinco,* *nove* e *oito reais.* [p=0.4] {b}Como fazer essa conta [p=0.2] "
        "para várias filiais e vários fornecedores *de uma vez?* [p=0.4] {c}Multiplicando matrizes, [p=0.2] e essa "
        "conta *não* é casa com casa. [p=0.3] Próximo episódio."),
    dict(id="26", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você contaria o seis vírgula zero como aprovado? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
