# Roteiro — Expressões Algébricas e Produtos Notáveis, Episódio 1 de 5: linguagem algébrica, valor numérico e operações
# com polinômios.
# Base: Estudos/Enem/estudos/01-matematica/19-expressoes-algebricas-produtos-notaveis.html — seções 02 e 03 + Questões 1 e 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A letra é uma CAIXINHA com um número dentro: troque a caixinha pelo número, SEMPRE dentro de parênteses.
#   Termos semelhantes são FRUTAS iguais: 3 maçãs + 2 maçãs = 5 maçãs; maçã com banana não vira uma fruta só.
#   A distributiva é um APERTO DE MÃO: cada termo de um parêntese cumprimenta cada termo do outro (2 × 2 = 4 apertos).
#   O menos antes do parêntese é um ESPELHO: vira o sinal de TODOS os termos de dentro.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula".
# Exemplos: os blocos usam os números do prompt (seções 02 e 03). Os erros clássicos usam os números do prompt.
# Nós fazemos (prompt): (x + 2)(3x − 1) = 3x² − x + 6x − 2 = 3x² + 5x − 2.
# QUESTÃO 1 (eu faço, texto idêntico): 2 · 6 + 2,5 · (x + x + 3) = 12 + 5x + 7,5 = 5x + 19,5 → C. Conferência x = 2: 11 + 18,5 = 29,5.
#   Erradas (do material, conferidas): A = 6 + 2,5(x + 3) = 2,5x + 13,5 (só a 2ª corrida); B = uma tarifa só (5x + 13,5);
#   D = esqueceu 3 km × 2,50 (5x + 15); E = (6 + 2,5)(2x + 3) = 17x + 25,5.
# QUESTÃO 6 (você faz, texto idêntico): (30 − 2x)(20 − 2x) = 600 − 60x − 40x + 4x² = 4x² − 100x + 600 → E. Conferência x = 1:
#   28 · 18 = 504 = 4 − 100 + 600. Erradas (do material): A = folha menos os 4 quadrados (inclui as abas); C = (30 − x)(20 − x);
#   B = esqueceu (−2x)(−2x); D = fez esse produto com o sinal errado.
# Acréscimos nossos (verde): "teste com um número" para a tradução; "negativo de parênteses" no valor numérico;
#   "teste com x = 1" depois da distributiva ((2x + 3)(x − 4) → 5 · (−3) = −15 = 2 − 5 − 12). Fórmula usada na Q6 explicada:
#   área do retângulo = comprimento × largura.
# Frases-chave (meio e fim, idênticas): 1. Negativo entra na conta sempre de parênteses. 2. Só se somam termos semelhantes.
#   3. Na distributiva, todos cumprimentam todos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Álgebra do zero: traduzir frases, valor numérico e distributiva | Produtos Notáveis Ep. 1"
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
        "{a}*O dobro de um número, aumentado de três* [p=0.3] {b}e *o dobro da soma de um número com três* [p=0.3] "
        "parecem a mesma frase. [p=0.4] {c}Com o número cinco, [p=0.2] a primeira dá *treze* [p=0.2] e a segunda dá "
        "*dezesseis.* [p=0.4] {d}No ENEM, [p=0.2] as duas estão nas alternativas."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *traduzir frases em expressões,* [p=0.3] {b}calcular o valor delas "
        "*sem errar sinal* [p=0.3] {c}e multiplicar polinômios *sem perder termo.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Operações: [p=0.2] menos com menos dá mais. [p=0.2] "
        "E *menos três ao quadrado,* sem parênteses, [p=0.2] é *menos nove;* [p=0.2] com parênteses, [p=0.2] *nove.* "
        "[p=0.4] {b}E da série de Potenciação: [p=0.2] x ao quadrado vezes x ao cubo [p=0.2] é *x à quinta;* [p=0.2] e "
        "*três x, tudo ao quadrado,* [p=0.2] é *nove x ao quadrado.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Abra um aplicativo de transporte. [p=0.3] {a}Ele mostra: [p=0.2] *seis reais fixos* [p=0.2] mais *dois e "
        "cinquenta por quilômetro.* [p=0.4] {b}Corrida de dois quilômetros: [p=0.2] *onze reais.* [p=0.2] De dez "
        "quilômetros: [p=0.2] *trinta e um.* [p=0.4] {c}A regra é a mesma; [p=0.2] só muda a distância. [p=0.4] "
        "{d}Então escrevemos: [p=0.2] *seis mais dois vírgula cinco x.* [p=0.2] A letra *x* guarda *qualquer "
        "distância.*"),

    # ================= BLOCO A: VOCABULÁRIO =================
    dict(id="05", block="vocab", text=
        "{t}E como se chama cada pedaço disso? [p=0.4] {a}A letra que guarda um número que pode mudar [p=0.2] é a "
        "*variável.* [p=0.4] {b}Uma conta com números, letras e operações [p=0.2] é uma *expressão algébrica.* [p=0.4] "
        "{c}E cada pedaço separado por mais ou por menos [p=0.2] é um *termo.* [p=0.2] Seis mais dois vírgula cinco x "
        "[p=0.2] tem *dois termos.*"),
    dict(id="06", block="vocab", text=
        "{t}Agora, um termo por dentro. [p=0.3] {a}Pegue *menos cinco x ao quadrado.* [p=0.4] {b}O número da frente, "
        "[p=0.2] com o sinal, [p=0.2] é o *coeficiente:* [p=0.2] *menos cinco.* [p=0.4] {c}A parte com letra [p=0.2] é a "
        "*parte literal:* [p=0.2] *x ao quadrado.* "),

    # ================= BLOCO B: TRADUÇÃO =================
    dict(id="07", block="traducao", text=
        "{t}Como transformar uma frase em expressão? [p=0.4] {a}*O dobro de um número, aumentado de três:* [p=0.2] "
        "primeiro dobra, [p=0.2] depois soma. [p=0.2] *Dois x mais três.* [p=0.4] {b}*O dobro da soma de um número com "
        "três:* [p=0.2] aqui a soma vem antes. [p=0.2] E o que vem antes [p=0.2] vai entre *parênteses:* [p=0.2] *dois "
        "vezes, abre parênteses, x mais três.* [p=0.4] {c}Frases parecidas, [p=0.2] contas diferentes."),
    dict(id="08", block="traducao", text=
        "{t}Mais traduções. [p=0.3] {a}*O quadrado de um número, menos um:* [p=0.2] x ao quadrado menos "
        "um. [p=0.2] Não é *x menos um, tudo ao quadrado.* [p=0.4] {b}*A metade de um número somada a seu "
        "triplo:* [p=0.2] x sobre dois, [p=0.2] mais três x. [p=0.4] {c}*Dois números consecutivos,* [p=0.2] um logo "
        "depois do outro: [p=0.2] *n* [p=0.2] e *n mais um.* [p=0.2] Dois pares consecutivos: [p=0.2] *dois n* [p=0.2] e "
        "*dois n mais dois.* [p=0.4] {d}E a corrida: [p=0.2] *parte fixa* [p=0.2] mais *parte que varia.*"),
    dict(id="09", block="traducao", text=
        "{t}E como saber se a tradução está certa? [p=0.4] {a}Atalho: [p=0.2] *teste com um número.* [p=0.2] Faça a "
        "frase com cinco, em palavras: [p=0.2] o dobro de cinco, aumentado de três, [p=0.2] treze. [p=0.4] {b}Depois, "
        "ponha cinco na expressão. [p=0.2] Deu o mesmo? [p=0.2] *Tradução certa.*"),

    # ================= BLOCO C: VALOR NUMÉRICO =================
    dict(id="10", block="valor", text=
        "{t}E o que é o *valor* de uma expressão? [p=0.4] {a}*Valor numérico* é o resultado [p=0.2] quando você troca a "
        "letra por um número. [p=0.4] {b}Pense na letra como uma *caixinha* com um número dentro. [p=0.2] Abra a caixinha [p=0.2] e coloque o "
        "número [p=0.2] *sempre dentro de parênteses.* [p=0.4] "
        "{c}Exemplo: [p=0.2] *três x ao quadrado, menos dois x, mais um,* [p=0.2] com x igual a *menos dois.*"),
    dict(id="11", block="valor", text=
        "{t}Um termo de cada vez. [p=0.3] {a}Primeiro: [p=0.2] três vezes, [p=0.2] *menos dois entre parênteses, ao "
        "quadrado.* [p=0.2] Isso dá *mais quatro.* [p=0.2] Três vezes quatro, [p=0.2] "
        "*doze.* [p=0.4] {b}Segundo: [p=0.2] menos dois vezes *menos dois.* [p=0.2] Menos com menos, [p=0.2] *mais "
        "quatro.* [p=0.4] {c}Terceiro: [p=0.2] *mais um.* [p=0.4] {d}Doze mais quatro mais um: [p=0.2] *dezessete.*"),
    dict(id="12", block="valor", text=
        "{t}E se esquecer os parênteses? [p=0.3] {a}Fica *três vezes menos dois ao quadrado.* [p=0.2] Aí o quadrado "
        "pega só o dois: [p=0.2] *menos quatro.* [p=0.2] Três vezes menos quatro, [p=0.2] *menos doze.* [p=0.4] {b}A "
        "conta termina em *menos sete,* [p=0.2] e não em dezessete. [p=0.4] {c}Atalho de segurança: [p=0.2] abriu a "
        "caixinha com um negativo, [p=0.2] *escreva os parênteses primeiro* [p=0.2] e só depois o número."),

    # ================= BLOCO D: TERMOS SEMELHANTES =================
    dict(id="13", block="semelhantes", text=
        "{t}Dá para juntar tudo? [p=0.4] {a}Pense em frutas. [p=0.2] Três maçãs mais duas maçãs: [p=0.2] "
        "*cinco maçãs.* [p=0.2] Mas maçã com banana [p=0.2] não vira uma fruta só. [p=0.4] {b}Na álgebra, [p=0.2] a "
        "fruta é a parte literal. [p=0.2] *Termos semelhantes* [p=0.2] são os que têm a *mesma parte literal.* [p=0.2] "
        "Só eles se juntam."),
    dict(id="14", block="semelhantes", text=
        "{a}Três x ao quadrado, [p=0.2] mais dois x, [p=0.2] menos x ao quadrado, [p=0.2] mais cinco x. [p=0.4] {b}Os x "
        "ao quadrado: [p=0.2] três menos um, [p=0.2] *dois x ao quadrado.* [p=0.2] Os x: [p=0.2] dois mais cinco, "
        "[p=0.2] *sete x.* [p=0.4] {c}Resposta: [p=0.2] *dois x ao quadrado mais sete x.* [p=0.4] "
        "{d}Não vira nove x ao cubo: [p=0.2] são frutas diferentes."),

    # ================= BLOCO E: O ESPELHO =================
    dict(id="15", block="espelho", text=
        "{t}E quando aparece um *menos* antes do parêntese? [p=0.4] {a}Cinco, [p=0.2] menos, [p=0.2] abre parênteses, "
        "[p=0.2] x menos três. [p=0.4] {b}Esse menos é um *espelho:* [p=0.2] ele vira o sinal de *todos* os termos de "
        "dentro. [p=0.2] O x vira *menos x.* [p=0.2] O menos três vira *mais três.* [p=0.4] {c}Fica cinco menos x mais "
        "três: [p=0.2] *oito menos x.*"),

    # ================= BLOCO F: DISTRIBUTIVA =================
    dict(id="16", block="distributiva", text=
        "{t}E como se multiplicam dois parênteses? [p=0.4] {a}Antes, um nome: [p=0.2] *polinômio* é uma soma de termos "
        "[p=0.2] como dois x mais três. [p=0.4] {b}Para multiplicar, [p=0.2] usa-se a *propriedade distributiva:* [p=0.2] cada termo de um parêntese [p=0.2] multiplica "
        "cada termo do outro. [p=0.4] {c}Pense num *aperto de mão:* [p=0.2] todos cumprimentam todos. [p=0.2] Dois termos "
        "de cada lado: [p=0.2] *quatro apertos de mão.*"),
    dict(id="17", block="distributiva", text=
        "{t}Dois x mais três, [p=0.2] vezes x menos quatro. [p=0.3] {a}Primeiro aperto: [p=0.2] dois x vezes x, [p=0.2] "
        "*dois x ao quadrado.* [p=0.3] {b}Segundo: [p=0.2] dois x vezes menos quatro, [p=0.2] *menos oito x.* [p=0.3] "
        "{c}Terceiro: [p=0.2] três vezes x, [p=0.2] *mais três x.* [p=0.3] {d}Quarto: [p=0.2] três vezes menos quatro, "
        "[p=0.2] *menos doze.* [p=0.4] {e}Frutas iguais: [p=0.2] *menos cinco x.* [p=0.2] Resultado: [p=0.2] *dois x ao quadrado, menos cinco x, menos doze.*"),
    dict(id="18", block="distributiva", text=
        "{t}Esqueceu algum aperto? [p=0.4] {a}Atalho: [p=0.2] *teste com x igual a um.* "
        "[p=0.2] No começo: [p=0.2] dois mais três é cinco; [p=0.2] um menos quatro é menos três. [p=0.2] Cinco "
        "vezes menos três: [p=0.2] *menos quinze.* [p=0.4] {b}No resultado: [p=0.2] dois, menos cinco, menos doze: "
        "[p=0.2] *menos quinze.* [p=0.2] Bateu. [p=0.4] {c}Não bateu? [p=0.2] Sumiu um aperto [p=0.2] ou virou um sinal."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Desenvolva: [p=0.2] *x mais dois, vezes três x menos um.* [p=0.4] {b}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}x vezes três x: [p=0.2] *três x ao quadrado.* "
        "[p=0.2] x vezes menos um: [p=0.2] *menos x.* [p=0.3] {b}Dois vezes três x: [p=0.2] *mais seis x.* [p=0.2] Dois "
        "vezes menos um: [p=0.2] *menos dois.* [p=0.4] {c}Frutas iguais: [p=0.2] *cinco x.* "
        "[p=0.2] Resposta: [p=0.2] *três x ao quadrado, mais cinco x, menos dois.* [p=0.4] {d}Teste com x igual a um: "
        "[p=0.2] seis dos dois lados. [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] negativo entra na conta sempre de parênteses. [p=0.5] "
        "{b}Dois: [p=0.2] só se somam termos semelhantes. [p=0.5] {c}Três: [p=0.2] na distributiva, todos cumprimentam "
        "todos."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os cinco erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *menos dois ao quadrado* [p=0.2] é "
        "*mais quatro.* [p=0.4] {b}Parece certo, [p=0.2] porque menos com menos dá mais. [p=0.4] {c}Mas, sem "
        "parênteses, [p=0.2] o quadrado pega só o dois: [p=0.2] *menos quatro.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] trocar só o primeiro sinal: [p=0.2] *cinco menos x menos três.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o menos parece grudado só no primeiro termo. [p=0.4] {c}Mas o espelho vira "
        "*todos* os sinais: [p=0.2] cinco menos x *mais* três, [p=0.2] oito menos x."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] dois x mais três x ao quadrado [p=0.2] virar *cinco x ao cubo.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque dois mais três é cinco. [p=0.4] {c}Mas não são semelhantes: "
        "[p=0.2] maçã com banana. [p=0.2] *Fica como está.*"),
    dict(id="25", block="erros", text=
        "{a}Quarto: [p=0.2] *três x, tudo ao quadrado,* [p=0.2] virar *três x ao quadrado.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o quadrado está colado no x. [p=0.4] {c}Mas ele está do lado de fora do parêntese: [p=0.2] eleva "
        "o três também. [p=0.2] *Nove x ao quadrado.*"),
    dict(id="26", block="erros", text=
        "{a}Quinto: [p=0.2] escrever *o dobro da soma* [p=0.2] como *dois x mais três.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque as palavras aparecem nessa ordem. [p=0.4] {c}Mas a soma acontece primeiro: [p=0.2] *dois vezes, abre "
        "parênteses, x mais três.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="27", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com "
        "você. [p=0.4] {a}Um aplicativo de transporte cobra, por corrida, [p=0.2] uma tarifa fixa de *seis reais* [p=0.2] "
        "mais *dois e cinquenta por quilômetro* rodado. [p=0.2] Em um dia, uma pessoa fez duas corridas: [p=0.2] a "
        "primeira de *x quilômetros* [p=0.2] e a segunda *três quilômetros mais longa* que a primeira. [p=0.2] A "
        "expressão que dá o valor total pago pelas duas corridas, em reais, é: [p=0.4] {qa}A: [p=0.2] dois vírgula cinco "
        "x mais treze vírgula cinco. [p=0.3] {qb}B: [p=0.2] cinco x mais treze vírgula cinco. [p=0.3] {qc}C: [p=0.2] "
        "cinco x mais dezenove vírgula cinco. [p=0.3] {qd}D: [p=0.2] cinco x mais quinze. [p=0.3] {qe}E: [p=0.2] "
        "dezessete x mais vinte e cinco vírgula cinco. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q1", text=
        "{t}Uma informação de cada vez. [p=0.3] {a}Tarifas fixas: [p=0.2] duas corridas, [p=0.2] *doze reais.* [p=0.4] "
        "{b}Quilômetros: [p=0.2] x, [p=0.2] mais x mais três: [p=0.2] *dois x mais três.* [p=0.4] {c}Custo dos "
        "quilômetros: [p=0.2] dois e cinquenta vezes dois x mais três. [p=0.2] Aperto de mão: [p=0.2] *cinco x mais "
        "sete e cinquenta.* [p=0.4] {d}Total: [p=0.2] doze mais cinco x mais sete e cinquenta: [p=0.2] *cinco x mais "
        "dezenove e cinquenta.* [p=0.4] {e}Teste com x igual a dois: [p=0.2] corridas de onze "
        "e de dezoito e cinquenta, [p=0.2] *vinte e nove e cinquenta.* [p=0.2] A expressão dá o mesmo. [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A cobrou *só a segunda corrida.* [p=0.4] {xb}A B cobrou a tarifa fixa "
        "*uma vez só.* [p=0.4] {xd}A D esqueceu de multiplicar os três quilômetros extras [p=0.2] por dois e cinquenta. "
        "[p=0.4] {xe}E a E cobrou os seis reais *por quilômetro* também."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="30", block="q6", text=
        "{t}E esta é *sua.* [p=0.3] {a}De uma folha retangular de papelão de *trinta por vinte centímetros,* [p=0.2] "
        "recortam-se quatro quadrados de lado *x* centímetros, [p=0.2] um em cada canto. [p=0.2] Dobrando as abas, "
        "[p=0.2] obtém-se uma caixa sem tampa. [p=0.2] A área do fundo dessa caixa, em centímetros quadrados, é: [p=0.4] "
        "{qa}A: [p=0.2] seiscentos menos quatro x ao quadrado. [p=0.3] {qb}B: [p=0.2] seiscentos menos cem x. [p=0.3] "
        "{qc}C: [p=0.2] x ao quadrado, menos cinquenta x, mais seiscentos. [p=0.3] {qd}D: [p=0.2] seiscentos, menos cem "
        "x, menos quatro x ao quadrado. [p=0.3] {qe}E: [p=0.2] quatro x ao quadrado, menos cem x, mais seiscentos. "
        "[p=0.4] {p}Lembre: [p=0.2] a área de um retângulo é *comprimento vezes largura.* [p=0.2] *Pause o vídeo e "
        "resolva.* [p=2.0]"),
    dict(id="31", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}Cada lado da folha perde x *nas duas pontas.* [p=0.2] O fundo mede *trinta menos dois "
        "x* [p=0.2] por *vinte menos dois x.* [p=0.4] {b}Comprimento vezes largura: [p=0.2] quatro apertos de mão. "
        "[p=0.2] Seiscentos, [p=0.2] menos sessenta x, "
        "[p=0.2] menos quarenta x. [p=0.4] {c}E o aperto que decide a questão: [p=0.2] "
        "menos dois x vezes menos dois x. [p=0.2] Menos com menos: [p=0.2] *mais quatro x ao quadrado.* [p=0.4] "
        "{d}Juntando: [p=0.2] *quatro x ao quadrado, menos cem x, mais seiscentos.* [p=0.4] {e}Teste com x igual a um: "
        "[p=0.2] vinte e oito vezes dezoito, [p=0.2] quinhentos e quatro, [p=0.2] e a expressão também. [p=0.3] {ok}*Letra E!*"),
    dict(id="32", block="q6", text=
        "{t}E as outras? [p=0.3] {xa}A A é a folha menos os quatro quadradinhos: [p=0.2] inclui as abas. [p=0.4] {xc}A C tirou x de cada lado *uma vez só.* [p=0.4] {xb}A B esqueceu o quarto aperto de mão, "
        "[p=0.2] o *mais quatro x ao quadrado.* [p=0.4] {xd}E a D fez esse aperto *com o sinal errado.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] negativo entra na conta sempre de parênteses. "
        "[p=0.5] {b}Dois: [p=0.2] só se somam termos semelhantes. [p=0.5] {c}Três: [p=0.2] na distributiva, todos "
        "cumprimentam todos."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Um quadrado de lado *três mais quatro* [p=0.2] tem quantos quadradinhos? [p=0.5] {b}Se você respondeu três ao "
        "quadrado mais quatro ao quadrado, [p=0.2] *vinte e cinco,* [p=0.2] faltaram *vinte e quatro.* [p=0.5] "
        "{c}Próximo episódio: [p=0.2] o erro mais famoso da álgebra."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses cinco erros você já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
