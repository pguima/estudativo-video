# Roteiro — Função Composta e Função Inversa, Episódio 3 de 5: função inversa (desfazer o caminho)
# Base: Estudos/Enem/estudos/01-matematica/30-funcao-composta-inversa.html — seção 06 (definição, f⁻¹(f(x)) = x e o quadro
#   "f⁻¹ não é 1/f"), seção 07 (receita, exemplo com fração, inversa da afim), seção 08 (só as conversões) + Questões 3 e 8.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   CAMINHO DE VOLTA: a inversa troca entrada e saída.
#   SAPATO ANTES DA MEIA: desfaça na ordem contrária (retoma "meia e sapato" do ep. 1).
#   O ⁻¹ NÃO É EXPOENTE: f⁻¹ desfaz; 1/f vira de cabeça para baixo.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Narração: "f⁻¹" é lido "f inversa"; "1/f" é lido "um sobre f".
# Material corrigido (roteiros.md, "Erros encontrados"): o material diz que x/2 e 1/(2x) "parecem próximas". O vídeo NÃO usa
#   a frase: com x = 4, x/2 = 2 e 1/(2x) = 0,125; uma é reta, a outra é curva.
# DESVIO DO PROMPT (regra de exemplos): o bloco f pedia inverter f(x) = (2x + 1)/(x − 3), que é EXATAMENTE a Questão 8
#   ("você faz", com pausa). O bloco usa um exemplo nosso: f(x) = (3x + 2)/(x − 4) → x(y − 3) = 4y + 2 →
#   f⁻¹(x) = (4x + 2)/(x − 3); teste f(5) = 17 e f⁻¹(17) = 70/14 = 5. A (2x + 1)/(x − 3) aparece só na Questão 8.
# Bloco e: Celsius–Fahrenheit completo (98,6 °F → 37 °C); o táxi só é anunciado e fica para a Questão 3 ("eu faço").
# Nós fazemos (prompt): f(x) = 3x − 6 → f⁻¹(x) = (x + 6)/3; teste f(4) = 6 e f⁻¹(6) = 4.
# QUESTÃO 3 ("eu faço"): x = (P − 4,5)/2,5 → A; R$ 37,00 → 13 km; 4,5 + 2,5 · 13 = 37. Erradas como no material (B divide
#   antes de subtrair; C soma o 4,5; D troca as letras sem isolar; E "um sobre"). Os valores com P = 37 (10,3 · 16,6 · 97 ·
#   ≈ 0,01) são acréscimo nosso, conferidos em trabalho/conferir_contas.py.
# QUESTÃO 8 ("você faz", com pausa): f⁻¹(x) = (3x + 1)/(x − 2) → A; conferência f(4) = 9 e 28/7 = 4. Erradas como no material
#   (B = 1/f; C sinal do 2; D sinal do 1; E a própria f). O teste com 9 elimina todas (B 6/19, C 28/11, D 26/7, E 19/6):
#   acréscimo nosso, conferido em Python.
# Atalhos (verde): "teste com um ponto" · afim: "(x − b)/a: o que foi somado por último sai primeiro" · conversão: "leia a
#   fórmula de trás para frente" · fração: "junte os x de um lado e ponha x em evidência".
# Frases-chave (meio e fim, idênticas): 1. A inversa troca entrada e saída. 2. Desfaça na ordem contrária: primeiro o último
#   passo. 3. f⁻¹ desfaz; 1/f só vira de cabeça para baixo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função inversa do zero: desfazer o caminho sem cair no 1/f · Matemática ENEM, Composta e Inversa ep. 3"

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
        "{a}Em Nova York, [p=0.2] o termômetro marca *noventa e oito vírgula seis graus Fahrenheit.* [p=0.4] {b}Você "
        "está com febre? [p=0.4] {c}Não: [p=0.2] são exatamente *trinta e sete graus Celsius.* [p=0.4] {d}Para saber, "
        "[p=0.2] você precisa da fórmula que faz o *caminho de volta.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular a *inversa* de qualquer função afim, [p=0.3] {b}inverter uma "
        "*fração* [p=0.3] {c}e nunca mais confundir *f inversa* com *um sobre f.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}*Isolar* o x é deixá-lo sozinho de um lado: [p=0.2] em dois x "
        "mais um igual a sete, [p=0.2] tira o um, divide por dois: [p=0.2] *x igual a três.* [p=0.4] {b}Da Função "
        "Afim: [p=0.2] *F igual a um vírgula oito C, mais trinta e dois.* [p=0.4] {c}E do episódio um: [p=0.2] *meia "
        "e sapato:* [p=0.2] a ordem muda o resultado."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em quem chega da rua. [p=0.3] {a}De manhã: [p=0.2] *meia,* depois *sapato.* [p=0.4] {b}À noite, "
        "para desfazer: [p=0.2] primeiro o *sapato,* depois a meia. [p=0.2] O último passo é o primeiro a ser "
        "desfeito. [p=0.4] {c}E um termômetro de viagem que só mostra *Fahrenheit:* [p=0.2] você quer o caminho de "
        "volta, para Celsius."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E o que é uma função inversa? [p=0.4] {a}Toda função tem uma *entrada,* o número que você põe, [p=0.2] e "
        "uma *saída,* o número que ela devolve. [p=0.4] {b}A *função inversa* é o *caminho de volta:* [p=0.2] a saída "
        "vira entrada, e a entrada vira saída. [p=0.4] {c}Escreve-se *f com um menos um pequeno,* [p=0.2] e lê-se *f "
        "inversa.* [p=0.4] {d}Se f leva *a* em *b,* [p=0.2] a f inversa leva *b* de volta em *a.*"),
    dict(id="06", block="definicao", text=
        "{t}E se eu fizer a ida e a volta? [p=0.4] {a}Aplico f, [p=0.2] depois a f inversa: [p=0.4] {b}volto ao *x.* "
        "[p=0.3] *f inversa de f de x é igual a x.* [p=0.4] {c}*Ida e volta [p=0.2] é ficar parado.*"),

    # ================= BLOCO B: NÃO É 1/f =================
    dict(id="07", block="umsobre", text=
        "{t}Esse menos um é um expoente? [p=0.4] {a}*Não.* [p=0.2] Aqui ele quer dizer *desfazer.* [p=0.4] {b}f de x "
        "igual a *x mais três:* [p=0.2] para desfazer, tira três. [p=0.2] A inversa é *x menos três.* [p=0.4] {c}*Um "
        "sobre x mais três* é outra coisa. [p=0.2] Com x igual a um: [p=0.2] a inversa dá *menos dois;* [p=0.2] o um "
        "sobre dá *zero vírgula vinte e cinco.*"),
    dict(id="08", block="umsobre", text=
        "{t}E com f de x igual a *dois x?* [p=0.4] {a}Desfazer dobrar é dividir por dois: [p=0.2] a inversa é *x "
        "sobre dois.* [p=0.4] {b}Com x igual a quatro: [p=0.2] x sobre dois dá *dois;* [p=0.2] um sobre dois x dá "
        "*zero vírgula cento e vinte e cinco.* [p=0.4] {c}Nem perto. [p=0.2] Uma é *reta,* a outra é *curva:* [p=0.2] "
        "funções diferentes."),

    # ================= BLOCO C: A RECEITA =================
    dict(id="09", block="esteira", text=
        "{t}E como achar a inversa de *dois x mais um?* [p=0.4] {a}Pense numa esteira: [p=0.2] o número é "
        "*multiplicado por dois* [p=0.2] e depois *soma um.* [p=0.2] Entra um, sai três. [p=0.4] {b}Para voltar, a "
        "esteira roda ao contrário: [p=0.2] *primeiro tira um,* [p=0.2] *depois divide por dois.* [p=0.4] {c}O três "
        "volta a ser um."),
    dict(id="10", block="receita", text=
        "{t}No papel, isso vira uma *receita de três passos.* [p=0.4] {a}Um: [p=0.2] escreva *y igual a dois x mais "
        "um.* [p=0.4] {b}Dois: [p=0.2] *isole o x.* [p=0.2] Passe o um para o outro lado, [p=0.2] e divida por dois: "
        "[p=0.2] *x igual a y menos um, sobre dois.* [p=0.4] {c}Três: [p=0.2] *troque os nomes:* [p=0.2] x vira y, y "
        "vira x. [p=0.4] {d}*f inversa de x igual a x menos um, sobre dois.*"),
    dict(id="11", block="teste", text=
        "{t}E como saber se está certa? [p=0.4] {a}Atalho: [p=0.2] *teste com um ponto.* [p=0.4] {b}f de um é *três.* "
        "[p=0.4] {c}Então a inversa precisa levar o três de volta no um: [p=0.2] três menos um, dividido por dois: "
        "[p=0.2] *um.* [p=0.3] Bateu."),

    # ================= BLOCO D: A INVERSA DA AFIM =================
    dict(id="12", block="afim", text=
        "{t}E vale para *qualquer* função afim? [p=0.4] {a}Vale. [p=0.2] Em *a x mais b,* [p=0.2] o x foi "
        "multiplicado por *a,* [p=0.2] depois somado com *b.* [p=0.4] {b}Na volta: [p=0.2] *tira o b,* [p=0.2] "
        "*depois divide pelo a.* [p=0.2] *x menos b, sobre a.* [p=0.4] {c}E se f *cresce,* [p=0.2] a inversa também "
        "cresce."),
    dict(id="13", block="afim", text=
        "{t}Isso vira atalho de prova. [p=0.4] {a}*O que foi somado por último sai primeiro;* [p=0.2] depois divida "
        "pelo número do x. [p=0.4] {b}Cinco x mais quatro? [p=0.2] *x menos quatro, sobre cinco.* [p=0.4] {c}Sem "
        "montar equação."),

    # ================= BLOCO E: CONVERSÕES =================
    dict(id="14", block="conversao", text=
        "{t}E o termômetro de Nova York? [p=0.4] {a}*F igual a um vírgula oito C, mais trinta e dois.* [p=0.4] {b}Na "
        "volta: [p=0.2] tira o trinta e dois, [p=0.2] depois divide por um vírgula oito. [p=0.2] *C igual a F menos "
        "trinta e dois, sobre um vírgula oito.* [p=0.4] {c}Noventa e oito vírgula seis menos trinta e dois: [p=0.2] "
        "*sessenta e seis vírgula seis.* [p=0.2] Dividido por um vírgula oito: [p=0.2] *trinta e sete graus.* [p=0.3] "
        "Sem febre."),
    dict(id="15", block="conversao", text=
        "{t}E toda conversão tem inversa? [p=0.4] {a}Tem. [p=0.2] Atalho: [p=0.2] *leia a fórmula de trás para "
        "frente,* [p=0.2] com a conta oposta. [p=0.4] {b}O preço do táxi pela distância [p=0.2] vira a *distância "
        "pelo preço:* [p=0.2] é a nossa primeira questão."),

    # ================= BLOCO F: INVERSA COM FRAÇÃO =================
    dict(id="16", block="fracao", text=
        "{t}E se a função for uma *fração,* [p=0.2] com x em cima e embaixo? [p=0.4] {a}Pegue *três x mais dois, "
        "sobre x menos quatro,* [p=0.2] com x diferente de quatro. [p=0.4] {b}*Multiplique cruzado:* [p=0.2] y vezes "
        "x menos quatro, [p=0.2] igual a três x mais dois. [p=0.4] {c}Distribua o y: [p=0.2] *x y menos quatro y.*"),
    dict(id="17", block="fracao", text=
        "{t}Agora o x aparece duas vezes. [p=0.4] {a}Junte os termos com x de um lado: [p=0.2] x y menos três x "
        "[p=0.2] igual a quatro y mais dois. [p=0.4] {b}*Ponha o x em evidência,* [p=0.2] isto é, para fora, "
        "multiplicando: [p=0.2] *x vezes y menos três.* [p=0.4] {c}Divida e troque os nomes: [p=0.2] *quatro x mais "
        "dois, sobre x menos três.* [p=0.4] {d}Teste: [p=0.2] f de cinco é dezessete, [p=0.2] e a inversa de "
        "dezessete dá setenta sobre catorze: [p=0.2] *cinco.* [p=0.3] Bateu."),
    dict(id="18", block="fracao", text=
        "{t}O truque da fração, em uma linha. [p=0.4] {a}Atalho: [p=0.2] *junte os x de um lado [p=0.2] e ponha o x "
        "em evidência.* [p=0.4] {b}É assim que o x fica sozinho."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Calcule a inversa de *f de x igual a três x menos seis* [p=0.2] e teste com um ponto. "
        "[p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O último passo foi tirar seis; [p=0.2] então, primeiro *soma seis:* [p=0.2] y "
        "mais seis igual a três x. [p=0.4] {b}Divide por três [p=0.2] e troca os nomes: [p=0.2] *f inversa igual a x "
        "mais seis, sobre três.* [p=0.4] {c}Teste: [p=0.2] f de quatro é doze menos seis, [p=0.2] *seis.* [p=0.2] "
        "Inversa de seis: [p=0.2] doze dividido por três, [p=0.2] *quatro.* [p=0.3] Voltou."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a inversa troca entrada e saída. [p=0.5] {b}Dois: "
        "[p=0.2] desfaça na ordem contrária: [p=0.2] primeiro o último passo. [p=0.5] {c}Três: [p=0.2] f inversa desfaz; "
        "[p=0.2] um sobre f só vira de cabeça para baixo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *f inversa é um sobre f.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque em números, [p=0.2] dois elevado a menos um é mesmo um meio. [p=0.4] {c}Mas "
        "no f, o menos um *quer dizer desfazer:* [p=0.2] a inversa de x mais três é x menos três."),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] na inversa de dois x mais um, [p=0.2] *somar um* em vez de tirar, [p=0.2] ou *dividir "
        "antes* de tirar o um. [p=0.4] {b}Parece certo, [p=0.2] porque as contas são as da ida. [p=0.4] {c}Mas "
        "desfazer é *conta oposta, ordem contrária.* [p=0.2] Teste com três: [p=0.2] nenhuma das duas volta ao um."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] *trocar as letras sem isolar nada:* [p=0.2] x igual a dois y mais um, e para por aí. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque trocar os nomes é um dos passos. [p=0.4] {c}Mas é o *último.* "
        "[p=0.2] Sem isolar, [p=0.2] você só reescreveu a própria f."),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="25", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. "
        "[p=0.4] {a}Em uma cidade, [p=0.2] o preço *P,* em reais, [p=0.2] de uma corrida de táxi de *x quilômetros* "
        "[p=0.2] é *P igual a quatro vírgula cinco, mais dois vírgula cinco x.* [p=0.2] Um aplicativo quer mostrar "
        "[p=0.2] quantos quilômetros o passageiro pode percorrer com um valor P disponível. [p=0.2] A expressão que "
        "fornece x em função de P é: [p=0.4] {qa}A: [p=0.2] P menos quatro vírgula cinco, sobre dois vírgula cinco. "
        "[p=0.3] {qb}B: [p=0.2] P sobre dois vírgula cinco, menos quatro vírgula cinco. [p=0.3] {qc}C: [p=0.2] P mais "
        "quatro vírgula cinco, sobre dois vírgula cinco. [p=0.3] {qd}D: [p=0.2] dois vírgula cinco P, mais quatro vírgula "
        "cinco. [p=0.3] {qe}E: [p=0.2] um sobre quatro vírgula cinco mais dois vírgula cinco P. [p=0.5] {p}*Pause o "
        "vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{t}O preço é a saída; [p=0.2] a pergunta quer a *volta.* [p=0.4] {a}A ida: [p=0.2] vezes dois vírgula cinco, "
        "[p=0.2] mais quatro vírgula cinco. [p=0.2] A volta: [p=0.2] *tira quatro vírgula cinco,* [p=0.2] *depois "
        "divide por dois vírgula cinco.* [p=0.4] {b}x igual a P menos quatro vírgula cinco, sobre dois vírgula cinco. "
        "[p=0.4] {c}Teste com trinta e sete reais: [p=0.2] trinta e dois e meio, dividido por dois e meio: [p=0.2] "
        "*treze quilômetros.* [p=0.2] E na ida, [p=0.2] quatro e meio mais dois e meio vezes treze: [p=0.2] *trinta e "
        "sete.* [p=0.3] {ok}*Letra A!*"),
    dict(id="27", block="q3", text=
        "{t}E as erradas? [p=0.4] {xb}A B [p=0.2] *divide antes de subtrair.* [p=0.3] {xc}A C [p=0.2] *soma* o quatro "
        "e meio. [p=0.3] {xd}A D [p=0.2] *troca as letras sem isolar.* [p=0.3] {xe}E a E [p=0.2] confunde a inversa "
        "com *um sobre* a função. [p=0.4] {a}Com trinta e sete reais, [p=0.2] nenhuma dá treze."),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="28", block="q8", text=
        "{t}E a última é *sua.* [p=0.4] {a}A função *f de x igual a dois x mais um, sobre x menos três,* [p=0.2] "
        "definida para x diferente de três, [p=0.2] é usada para converter um índice x em uma nota f de x [p=0.2] e "
        "admite inversa no conjunto adequado. [p=0.2] A lei de f inversa é: [p=0.4] {qa}A: [p=0.2] três x mais um, sobre "
        "x menos dois. [p=0.3] {qb}B: [p=0.2] x menos três, sobre dois x mais um. [p=0.3] {qc}C: [p=0.2] três x mais um, "
        "sobre x mais dois. [p=0.3] {qd}D: [p=0.2] três x menos um, sobre x menos dois. [p=0.3] {qe}E: [p=0.2] dois x "
        "mais um, sobre x menos três. [p=0.5] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="29", block="q8", text=
        "{t}Conferindo. [p=0.3] {a}Multiplique cruzado: [p=0.2] *x y menos três y* [p=0.2] igual a dois x mais um. "
        "[p=0.4] {b}Junte os x: [p=0.2] x y menos dois x [p=0.2] igual a três y mais um. [p=0.2] Ponha o x em evidência: "
        "[p=0.2] *x vezes y menos dois* [p=0.2] igual a três y mais um. [p=0.4] {c}Divida e troque os nomes: [p=0.2] *três "
        "x mais um, sobre x menos dois.* [p=0.3] {ok}*Letra A!*"),
    dict(id="30", block="q8", text=
        "{t}Teste com um ponto. [p=0.4] {a}f de quatro: [p=0.2] nove sobre um, [p=0.2] *nove.* [p=0.2] Na inversa: "
        "[p=0.2] vinte e oito sobre sete, [p=0.2] *quatro.* [p=0.3] Voltou. [p=0.4] {xb}A B é o *um sobre f.* [p=0.3] "
        "{xc}A C erra o sinal do *dois* na evidência. [p=0.3] {xd}A D erra o sinal do *um.* [p=0.3] {xe}E a E é a "
        "*própria f.* [p=0.4] {b}Com o nove, [p=0.2] só a A devolve o quatro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a inversa troca entrada e saída. [p=0.5] "
        "{b}Dois: [p=0.2] desfaça na ordem contrária: [p=0.2] primeiro o último passo. [p=0.5] {c}Três: [p=0.2] f "
        "inversa desfaz; [p=0.2] um sobre f só vira de cabeça para baixo."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}*f de x igual a x ao quadrado* [p=0.2] leva três em nove [p=0.2] e menos três em nove. [p=0.4] {b}Se eu te "
        "disser que a saída foi nove, [p=0.2] de onde veio? [p=0.4] {c}Nem toda função pode ser desfeita. [p=0.4] "
        "{d}Próximo episódio: [p=0.2] quem tem inversa, [p=0.2] e o espelho que desenha o gráfico dela."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que conversão do seu dia a dia [p=0.2] você já fez de trás para "
        "frente? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
