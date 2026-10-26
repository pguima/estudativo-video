# Roteiro — Equações e Inequações do 1º Grau, Episódio 1 de 5: a equação como balança e o roteiro de resolução.
# Base: Estudos/Enem/estudos/01-matematica/20-equacoes-inequacoes-1o-grau.html — seções 02, 03 e 04 + Questão 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A equação é uma BALANÇA equilibrada: continua equilibrada se você fizer a MESMA coisa nos dois pratos.
#   "Passar para o outro lado" é só um APELIDO: o que soma passa subtraindo; o que multiplica passa dividindo, LEVANDO o
#   próprio sinal.
#   O traço da fração é um PARÊNTESE DISFARÇADO: o menos na frente dela atinge o numerador inteiro.
#   A conferência é a PROVA REAL: substitua e veja se a balança fecha.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos: os blocos usam os números do prompt (seções 02, 03 e 04), todos conferidos em Python:
#   3x + 4 = 19 → x = 5 (3·5 + 4 = 19) · −2x = 10 → x = −5 (−2·(−5) = 10) · 5(x − 2) − 3(x − 4) = 18 → x = 8
#   (5·6 − 3·4 = 18); erro −3x − 12 → x = 20 (5·18 − 3·16 = 42) · x/2 − (x − 4)/3 = 3 → x = 10 (5 − 2 = 3); erro → x = 26
#   (13 − 22/3 ≈ 5,67) · 2(x + 3) = 2x + 5 → 0x = −1 · 3(x − 2) = 3x − 6 → 0x = 0.
#   Bloco a (nosso): 3x − 15 = 0 → x = −(−15)/3 = 5, a mesma balança escrita como ax + b = 0.
# Nós fazemos (prompt): 4(x − 1) − 2(x − 5) = 12 → 2x + 6 = 12 → x = 3; conferência 4·2 − 2·(−2) = 12.
# QUESTÃO 6 (eu faço e você confere, texto idêntico): 40 + 3x = 3x + 36 → 0x = −4 → nunca se igualam; B sempre R$ 4,00 mais
#   barata → D. Erradas (do material e do prompt): A toma o 12 do parêntese como solução; B transforma R$ 4,00 em 4 km;
#   C inverte quem é mais barata; E supõe que os preços se cruzam. Conferência nossa: 10 km → A 70, B 66; 100 km → 340 e 336.
# Acréscimos nossos (verde): o "apelido" como atalho de 2 regras; "confira na equação ORIGINAL" (a prova real);
#   "MMC de 2 e 3 = 6" lembrado na hora; "x sumiu? leia o que sobrou" (número = número falso → nenhuma; 0 = 0 → infinitas).
# Frases-chave (meio e fim, idênticas): 1. O que se faz num prato se faz no outro. 2. O que multiplica passa dividindo, com
#   o próprio sinal. 3. O traço da fração é um parêntese disfarçado.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação do 1º grau do zero: a balança e o roteiro de 5 passos | Equações do 1º Grau Ep. 1"
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
    "MMC": "eme eme cê",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Em *cinco vezes x menos dois, menos três vezes x menos quatro, igual a dezoito,* [p=0.3] {b}a resposta é "
        "*oito.* [p=0.4] {c}Quem erra um único sinal [p=0.2] chega a *vinte,* [p=0.2] e o vinte está nas alternativas. "
        "[p=0.4] {d}Hoje você aprende um *roteiro em cinco passos* [p=0.2] que não deixa o sinal escapar."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai resolver *qualquer equação do primeiro grau,* [p=0.2] {b}com *parênteses* e "
        "*frações,* [p=0.3] {c}e saber quando ela *não tem solução* [p=0.2] ou tem *infinitas.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes de trinta segundos. [p=0.3] {a}Da série de Expressões Algébricas: [p=0.2] o *menos* "
        "antes do parêntese é um *espelho.* [p=0.2] Ele vira o sinal de *todos* os termos de dentro. [p=0.2] Menos, abre "
        "parênteses, x menos quatro: [p=0.2] *menos x mais quatro.* [p=0.4] {b}E da série de Frações: [p=0.2] o *MMC* "
        "é o *menor número* que é múltiplo dos denominadores. [p=0.2] O MMC de dois e três [p=0.2] é *seis.*"),

    # ================= CONCRETO: A BALANÇA =================
    dict(id="04", block="balanca", text=
        "{t}Imagine uma balança de feira, [p=0.2] equilibrada. [p=0.3] {a}Num prato, [p=0.2] *três sacos iguais* "
        "[p=0.2] e *quatro pesinhos* de um quilo. [p=0.3] {b}No outro, [p=0.2] *dezenove quilos.* [p=0.4] {c}Quanto "
        "pesa cada saco? [p=0.6] {d}Tire os quatro pesinhos [p=0.2] *dos dois pratos ao mesmo tempo.* [p=0.2] Sobram três "
        "sacos [p=0.2] contra *quinze quilos.* [p=0.4] {e}Agora divida *cada prato* em três partes iguais: [p=0.2] um saco "
        "[p=0.2] contra *cinco quilos.* [p=0.4] {f}E o ponteiro? [p=0.2] Continuou no meio o tempo todo."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E onde está a matemática nisso? [p=0.4] {a}Chame o peso do saco de *x.* [p=0.2] A balança vira [p=0.2] "
        "*três x mais quatro igual a dezenove.* [p=0.4] {b}Isso é uma *equação:* [p=0.2] uma igualdade com um valor "
        "escondido. [p=0.4] {c}O valor escondido [p=0.2] é a *incógnita.* [p=0.4] {d}E o número que deixa a igualdade "
        "verdadeira [p=0.2] é a *raiz,* [p=0.2] ou *solução.* [p=0.2] Aqui, [p=0.2] *cinco.*"),
    dict(id="06", block="definicao", text=
        "{t}E o que faz ela ser *do primeiro grau?* [p=0.4] {a}O x aparece sozinho, [p=0.2] sem estar ao quadrado. "
        "[p=0.2] Toda equação assim [p=0.2] pode ser escrita como *a x mais b igual a zero,* [p=0.2] com *a diferente de "
        "zero.* [p=0.4] {b}A raiz é sempre [p=0.2] *x igual a menos b sobre a.* [p=0.4] {c}A nossa balança: [p=0.2] três x "
        "menos quinze igual a zero. [p=0.2] Menos, menos quinze, sobre três: [p=0.2] *cinco.* [p=0.2] O mesmo saco."),

    # ================= BLOCO B: A BALANÇA NA CONTA =================
    dict(id="07", block="naconta", text=
        "{t}Como a balança fica escrita, linha por linha? [p=0.4] {a}*Três x mais quatro igual a dezenove.* [p=0.4] {b}Tira "
        "quatro dos dois lados: [p=0.2] *três x igual a quinze.* [p=0.4] {c}Divide os dois lados por três: [p=0.2] *x igual "
        "a cinco.* [p=0.4] {d}E a *prova real:* [p=0.2] substitua. [p=0.2] Três vezes cinco, quinze, [p=0.2] mais quatro, "
        "[p=0.2] *dezenove.* [p=0.2] A balança fecha."),

    # ================= BLOCO C: OS DOIS PRINCÍPIOS =================
    dict(id="08", block="principios", text=
        "{t}Que operações são permitidas na balança? [p=0.4] {a}O *princípio aditivo:* [p=0.2] somar ou subtrair *o mesmo "
        "número* dos dois lados. [p=0.4] {b}O *princípio multiplicativo:* [p=0.2] multiplicar ou dividir os dois lados "
        "*pelo mesmo número,* [p=0.2] desde que *não seja zero.* [p=0.4] {c}Só isso. [p=0.2] Tudo o resto [p=0.2] é apelido "
        "dessas duas regras."),
    dict(id="09", block="principios", text=
        "{t}E aquele *passar para o outro lado?* [p=0.4] {a}É só um apelido. [p=0.2] O que *soma* passa *subtraindo.* "
        "[p=0.2] O que *multiplica* passa *dividindo.* [p=0.4] {b}Mas atenção: [p=0.2] quem passa dividindo [p=0.2] *leva o "
        "próprio sinal.* [p=0.4] {c}Menos dois x igual a dez. [p=0.2] O menos dois passa dividindo [p=0.2] *com o "
        "menos:* [p=0.2] dez sobre menos dois, [p=0.2] *menos cinco.* [p=0.4] {d}Prova real: [p=0.2] menos dois vezes "
        "menos cinco, [p=0.2] *dez.* [p=0.2] Fecha."),

    # ================= BLOCO D: O ROTEIRO =================
    dict(id="10", block="roteiro", text=
        "{t}E quando a equação é grande? [p=0.4] Siga sempre a mesma ordem. [p=0.3] {a}Um: [p=0.2] tire os "
        "*denominadores.* [p=0.3] {b}Dois: [p=0.2] tire os *parênteses.* [p=0.3] {c}Três: [p=0.2] *separe:* [p=0.2] x de "
        "um lado, números do outro. [p=0.3] {d}Quatro: [p=0.2] *reduza e divida.* [p=0.3] {e}Cinco: [p=0.2] *confira* "
        "[p=0.2] na equação do começo."),

    # ================= BLOCO E: COM PARÊNTESES =================
    dict(id="11", block="parenteses", text=
        "{t}Vamos à equação do começo. [p=0.3] {a}Cinco vezes x menos dois, [p=0.2] menos três vezes x menos quatro, "
        "[p=0.2] igual a dezoito. [p=0.4] {b}Passo dois, os parênteses. [p=0.2] Cinco vezes x: [p=0.2] *cinco x.* [p=0.2] "
        "Cinco vezes menos dois: [p=0.2] *menos dez.* [p=0.4] {c}Agora o perigo. [p=0.2] Menos três vezes x: [p=0.2] *menos "
        "três x.* [p=0.2] Menos três vezes menos quatro: [p=0.2] menos com menos, [p=0.2] *mais doze.* [p=0.4] {d}Juntando: "
        "[p=0.2] *dois x mais dois igual a dezoito.* [p=0.2] Tira dois: [p=0.2] dois x igual a dezesseis. [p=0.2] Divide "
        "por dois: [p=0.2] *x igual a oito.*"),
    dict(id="12", block="parenteses", text=
        "{t}Confira. [p=0.3] {a}Oito menos dois, seis; [p=0.2] cinco vezes seis, *trinta.* [p=0.2] Oito menos quatro, "
        "quatro; [p=0.2] três vezes quatro, *doze.* [p=0.2] Trinta menos doze: [p=0.2] *dezoito.* [p=0.2] Fecha. [p=0.4] "
        "{b}E quem escreveu *menos três x menos doze?* [p=0.2] Chega a dois x menos vinte e dois igual a dezoito, [p=0.2] e "
        "a *x igual a vinte.* [p=0.4] {c}A prova real denuncia: [p=0.2] cinco vezes dezoito, [p=0.2] menos três vezes "
        "dezesseis: [p=0.2] *quarenta e dois.* [p=0.2] Não é dezoito. [p=0.2] *A balança não fecha.*"),

    # ================= BLOCO F: COM FRAÇÕES =================
    dict(id="13", block="fracoes", text=
        "{t}E com frações? [p=0.4] {a}*x sobre dois, menos x menos quatro sobre três, igual a três.* [p=0.4] {b}Passo um: "
        "[p=0.2] o MMC de dois e três é *seis.* [p=0.2] Multiplique *tudo* por seis. [p=0.4] {c}Seis vezes x sobre dois: "
        "[p=0.2] *três x.* [p=0.2] Seis vezes três: [p=0.2] *dezoito.* [p=0.4] {d}E a fração com o menos? [p=0.2] Aqui está "
        "o truque: [p=0.2] o traço da fração [p=0.2] é um *parêntese disfarçado.* [p=0.2] Ela vira [p=0.2] *menos dois, "
        "abre parênteses, x menos quatro.*"),
    dict(id="14", block="fracoes", text=
        "{t}Agora é o espelho. [p=0.3] {a}Menos dois vezes x: [p=0.2] *menos dois x.* [p=0.2] Menos dois vezes menos quatro: "
        "[p=0.2] *mais oito.* [p=0.4] {b}Três x menos dois x mais oito [p=0.2] igual a dezoito. [p=0.2] *x mais oito igual "
        "a dezoito.* [p=0.2] *x igual a dez.* [p=0.4] {c}Prova real: [p=0.2] dez sobre dois, cinco; [p=0.2] seis sobre "
        "três, dois. [p=0.2] Cinco menos dois: [p=0.2] *três.* [p=0.2] Fecha. [p=0.4] {d}Quem esquece o parêntese [p=0.2] "
        "escreve *menos oito,* [p=0.2] e chega a *vinte e seis.*"),

    # ================= BLOCO G: QUANDO O X SOME =================
    dict(id="15", block="xsome", text=
        "{t}E se o x *sumir* no meio da conta? [p=0.4] {a}Dois vezes x mais três [p=0.2] igual a dois x mais cinco. "
        "[p=0.2] Dois x mais seis [p=0.2] igual a dois x mais cinco. [p=0.4] {b}Tira dois x dos dois lados: [p=0.2] "
        "*zero x igual a menos um.* [p=0.2] Ou seja, [p=0.2] *seis igual a cinco.* [p=0.4] {c}Isso é falso [p=0.2] para "
        "*qualquer* x. [p=0.2] A balança nunca fecha: [p=0.2] *nenhuma solução.*"),
    dict(id="16", block="xsome", text=
        "{t}Agora o contrário. [p=0.3] {a}Três vezes x menos dois [p=0.2] igual a três x menos seis. [p=0.2] Três x menos "
        "seis igual a três x menos seis. [p=0.4] {b}Tira três x: [p=0.2] *zero x igual a zero.* [p=0.2] Isso é verdade "
        "[p=0.2] para *qualquer* x. [p=0.4] {c}*Infinitas soluções.* [p=0.2] Esse tipo de igualdade se chama "
        "*identidade.* [p=0.4] {d}Atalho: [p=0.2] o x sumiu? [p=0.2] Leia o que sobrou. [p=0.2] Ficou falso, *nenhuma.* "
        "[p=0.2] Ficou zero igual a zero, *infinitas.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva: [p=0.2] *quatro vezes x menos um, menos dois vezes x menos cinco, igual a "
        "doze.* [p=0.4] {b}*Pause e tente,* [p=0.2] com o roteiro. [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Parênteses: [p=0.2] *quatro x menos quatro.* [p=0.2] E o espelho no segundo: [p=0.2] "
        "*menos dois x mais dez.* [p=0.4] {b}Juntando: [p=0.2] *dois x mais seis igual a doze.* [p=0.2] Dois x igual a seis. "
        "[p=0.2] *x igual a três.* [p=0.4] {c}Prova real: [p=0.2] quatro vezes dois, oito. [p=0.2] Menos dois vezes menos "
        "dois, [p=0.2] mais quatro. [p=0.2] Oito mais quatro: [p=0.2] *doze.* [p=0.2] Fecha."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o que se faz num prato se faz no outro. [p=0.5] {b}Dois: "
        "[p=0.2] o que multiplica passa dividindo, com o próprio sinal. [p=0.5] {c}Três: [p=0.2] o traço da fração é um "
        "parêntese disfarçado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *menos três vezes x menos quatro* [p=0.2] virar "
        "*menos três x menos doze.* [p=0.4] {b}Parece certo, [p=0.2] porque o menos quatro já tinha sinal de menos. [p=0.4] "
        "{c}Mas menos vezes menos [p=0.2] dá *mais:* [p=0.2] *menos três x mais doze.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] no *menos x menos quatro sobre três,* [p=0.2] deixar o menos quatro *intacto.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o menos parece encostado só no x. [p=0.4] {c}Mas o traço é um parêntese "
        "disfarçado: [p=0.2] o menos atinge *o numerador inteiro.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] *menos dois x igual a dez* [p=0.2] dar *x igual a cinco.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque passar para o outro lado parece sempre trocar o sinal. [p=0.4] {c}Mas trocar sinal [p=0.2] é só para quem "
        "soma ou subtrai. [p=0.2] Quem multiplica passa dividindo *com o próprio sinal:* [p=0.2] *menos cinco.*"),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] *um terço mais um quarto* [p=0.2] dar *dois sétimos.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque é só somar em cima e somar embaixo. [p=0.4] {c}Mas fração se soma pelo MMC: [p=0.2] quatro doze avos "
        "mais três doze avos, [p=0.2] *sete doze avos.*"),

    # ================= QUESTÃO 6 (EU FAÇO E VOCÊ CONFERE) =================
    dict(id="24", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Eu resolvo, [p=0.2] e você confere. "
        "[p=0.4] {a}Duas empresas de frete calculam o preço, em reais, [p=0.2] de uma entrega de *x quilômetros.* [p=0.2] "
        "A empresa A cobra *quarenta mais três x;* [p=0.2] a empresa B cobra *três vezes, abre parênteses, x mais "
        "doze.* [p=0.2] Comparando as duas, conclui-se que: [p=0.4] {qa}A: [p=0.2] os preços se igualam em uma entrega de "
        "doze quilômetros. [p=0.3] {qb}B: [p=0.2] os preços se igualam em uma entrega de quatro quilômetros. [p=0.3] "
        "{qc}C: [p=0.2] A é mais barata em qualquer entrega, por quatro reais. [p=0.3] {qd}D: [p=0.2] B é mais barata em "
        "qualquer entrega, por quatro reais. [p=0.3] {qe}E: [p=0.2] B é mais barata só nas entregas de até doze "
        "quilômetros. [p=0.4] {p}*Pause e tente* antes de mim. [p=2.0]"),
    dict(id="25", block="q6", text=
        "{t}Primeiro, os parênteses de B. [p=0.3] {a}Três vezes x mais três vezes doze: [p=0.2] *três x mais trinta e "
        "seis.* [p=0.4] {b}Quando os preços se igualam? [p=0.2] Quarenta mais três x [p=0.2] igual a três x mais trinta e "
        "seis. [p=0.4] {c}Tira três x dos dois lados: [p=0.2] *zero x igual a menos quatro.* [p=0.2] O x sumiu, [p=0.2] e "
        "sobrou algo falso: [p=0.2] *nunca se igualam.* [p=0.4] {d}E a diferença? [p=0.2] Quarenta contra trinta e seis: "
        "[p=0.2] B sempre *quatro reais mais barata.* [p=0.4] {e}Confira: [p=0.2] dez quilômetros, [p=0.2] setenta contra "
        "sessenta e seis. [p=0.2] Cem quilômetros, [p=0.2] trezentos e quarenta contra trezentos e trinta e seis. [p=0.3] "
        "{ok}*Letra D!*"),
    dict(id="26", block="q6", text=
        "{t}E as erradas? [p=0.3] {xa}A A pegou o *doze do parêntese* [p=0.2] como se fosse a solução. [p=0.4] {xb}A B "
        "transformou os *quatro reais* [p=0.2] em *quatro quilômetros.* [p=0.4] {xc}A C *inverteu* quem é mais barata. "
        "[p=0.4] {xe}E a E supôs que os preços *se cruzam.* [p=0.2] Não se cruzam: [p=0.2] os dois cobram os mesmos três "
        "reais por quilômetro. [p=0.4] {f}Essa situação volta na série de Sistemas Lineares, [p=0.2] com o nome de "
        "*retas paralelas.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o que se faz num prato se faz no outro. [p=0.5] "
        "{b}Dois: [p=0.2] o que multiplica passa dividindo, com o próprio sinal. [p=0.5] {c}Três: [p=0.2] o traço da "
        "fração é um parêntese disfarçado."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Resolver é a parte fácil. [p=0.4] {b}O difícil é transformar [p=0.2] *daqui a quatro anos, o pai terá o "
        "triplo da idade do filho* [p=0.2] numa equação. [p=0.5] {c}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses quatro erros você já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
