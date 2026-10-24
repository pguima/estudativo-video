# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 2 de 6: multiplicar, dividir, elevar e tirar raiz (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seção 04 (+ Questões 2, 3 e 8 da
# seção 12 e a questão extra das bactérias, enviada no prompt).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   DUAS PISTAS: os coeficientes correm numa pista, os expoentes na outra.
#   A GANGORRA: coeficiente sobe 10 vezes, expoente desce 1 → mesmo valor (40 · 10⁶ = 4 · 10⁷). Serve para renormalizar e para
#   deixar o expoente PAR antes da raiz.
# Exemplos dos blocos (TROCADOS de propósito, para não entregar as questões "você faz"):
#   o prompt usava no bloco c) (2·10⁻²) ÷ (5·10⁻⁵) = 0,4·10³ (é a Questão 3) e no bloco e) √(1,6·10⁻⁵) (é a Questão 8).
#   Aqui: multiplicar 3·10⁴ fotos × 2·10⁶ bytes = 6·10¹⁰ · dividir 6·10³ L ÷ 2·10⁻¹ L = 3·10⁴ copos (3 − (−1) = 4) ·
#   renormalizar 40·10⁶ → 4·10⁷ (gangorra do prompt) e (3·10⁻⁴) ÷ (6·10⁻⁸) = 0,5·10⁴ → 5·10³ · potência (2·10⁻²)³ = 8·10⁻⁶ ·
#   raiz √(4,9·10⁻⁵) = √(49·10⁻⁶) = 7·10⁻³.
# Nós fazemos: (6·10³)·(5·10⁻⁷) = 30·10⁻⁴ → 3·10⁻³.
# QUESTÃO EXTRA (eu faço) — bactérias: (2·3)·10^(−12+8) = 6·10⁻⁴ g → B. Análise EXATAMENTE como no prompt:
#   A (6·10⁻²⁰): −12 − 8 = −20 · C (5·10⁻⁴): somou 2 + 3 · D (6·10⁴): perdeu o sinal do −12 (12 − 8 = 4) ·
#   E (6·10⁹⁶): multiplicou os expoentes (12 · 8 = 96).
# QUESTÃO 2 do material (nós fazemos) — data center: 40·10⁶ → 4·10⁷ → C. Material: D = parou um passo antes; A = somou 8 + 5.
#   NOSSAS: B (4·10⁶) tirou o zero do 40 sem subir o expoente · E (4·10⁸) subiu o expoente duas vezes.
# QUESTÃO 3 do material (você faz) — impressora 3D: 0,4·10^(−2−(−5)) = 0,4·10³ → 4·10² = 400 → D.
#   ATENÇÃO, erro do material: ele diz que errar o sinal (−2 − 5 = −7) leva à A (25). Não leva: dá 0,4·10⁻⁷, nem está nas
#   alternativas. No vídeo: esse erro dá um número de camadas menor que um, absurdo. NOSSAS: A (25) e C (250) trazem o 2,5 de
#   quem dividiu ao contrário (5 ÷ 2) · B (40) e E (4 000) erraram a gangorra (o expoente desceu dois / não desceu).
# QUESTÃO 8 do material (você faz) — placa quadrada: 1,6·10⁻⁵ = 16·10⁻⁶ → √ = 4·10⁻³ → A. Material: B = dividiu o expoente
#   ímpar por 2. NOSSAS: C (1,26·10⁻³) tirou a raiz do 1,6 e arredondou o expoente · D (8·10⁻³) dividiu o 16 por 2 em vez de
#   tirar a raiz · E (4·10⁻⁶) tirou a raiz do 16 e esqueceu a do 10⁻⁶.
# Frases-chave (meio e fim, idênticas):
#   1. Multiplicou: soma expoentes. Dividiu: subtrai.
#   2. Fez a conta? Renormalize.
#   3. Raiz quadrada só com expoente par.
# Atalhos (verde): "números com números, potências com potências" · "menos com menos vira mais" · "o que um lado da gangorra
#   ganha, o outro perde" · "o de fora entra nos dois" · "deixe o expoente par com a gangorra" · "confira elevando ao quadrado".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Notação científica: multiplicar, dividir, elevar e tirar raiz (sem cair no 40 · 10⁶) · Matemática ENEM, episódio 2"

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
        "{a}Você multiplica, [p=0.2] chega em *quarenta vezes dez elevado a seis,* [p=0.3] {b}encontra essa resposta nas "
        "alternativas [p=0.2] e marca. [p=0.5] {c}*Errou.* [p=0.5] {d}O número está certo; [p=0.2] a *escrita,* não. [p=0.4] "
        "{e}A prova coloca essa armadilha *de propósito.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai fazer as quatro operações: [p=0.2] *multiplicar, dividir, elevar e tirar "
        "raiz.* [p=0.4] {b}E sem esquecer *o último passo,* [p=0.2] aquele que a prova adora cobrar."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Na notação científica, [p=0.2] o número da frente se chama "
        "*coeficiente,* [p=0.2] e ele precisa ter *um único algarismo, diferente de zero, antes da vírgula.* [p=0.4] "
        "{b}Multiplicar potências de dez soma os expoentes: [p=0.2] dez ao cubo vezes dez ao quadrado, [p=0.2] dez elevado a "
        "cinco. [p=0.4] {c}E dividir subtrai: [p=0.2] dez elevado a cinco dividido por dez ao quadrado, [p=0.2] dez ao cubo."),

    # ================= BLOCO A: MULTIPLICAR — AS DUAS PISTAS =================
    dict(id="04", block="multiplicar", text=
        "{t}Pergunta: [p=0.2] um celular guarda *três vezes dez elevado a quatro* fotos, [p=0.2] e cada foto tem *dois vezes "
        "dez elevado a seis* bytes. [p=0.4] Quantos bytes ao todo? [p=0.5] {a}É uma multiplicação. [p=0.3] {b}E o segredo é "
        "imaginar *duas pistas separadas.* [p=0.3] {c}Os coeficientes correm numa pista; [p=0.2] {d}os expoentes, na outra."),
    dict(id="05", block="multiplicar", text=
        "{t}Pista de cima: [p=0.2] três vezes dois, [p=0.2] *seis.* [p=0.4] {a}Pista de baixo: [p=0.2] dez elevado a quatro "
        "vezes dez elevado a seis. [p=0.2] Mesma base, [p=0.2] então *soma* os expoentes: [p=0.2] quatro mais seis, [p=0.2] "
        "*dez.* [p=0.4] {b}Resultado: [p=0.2] *seis vezes dez elevado a dez* bytes. [p=0.4] {c}Atalho: [p=0.2] *números com "
        "números, [p=0.2] potências com potências.*"),

    # ================= BLOCO B: DIVIDIR — ATENÇÃO AOS SINAIS =================
    dict(id="06", block="dividir", text=
        "{t}E para dividir? [p=0.3] Uma caixa d'água tem *seis vezes dez ao cubo* litros, [p=0.2] e um copo tem *dois vezes "
        "dez elevado a menos um* litro, [p=0.2] que é zero vírgula dois. [p=0.4] Quantos copos? [p=0.4] {a}Pista de cima: "
        "[p=0.2] seis dividido por dois, [p=0.2] *três.* [p=0.4] {b}Pista de baixo: [p=0.2] divisão de mesma base *subtrai* "
        "os expoentes: [p=0.2] três *menos* menos um."),
    dict(id="07", block="dividir", text=
        "{t}Devagar, [p=0.2] porque é aqui que mora o erro. [p=0.4] {a}Três, [p=0.3] menos, [p=0.3] *menos um.* [p=0.5] "
        "{b}Dois sinais de menos juntos [p=0.2] viram *mais:* [p=0.3] {c}três *mais* um, [p=0.3] *quatro.* [p=0.4] "
        "{d}Resultado: [p=0.2] *três vezes dez elevado a quatro* copos, [p=0.2] trinta mil. [p=0.4] {e}Atalho: [p=0.2] "
        "subtraiu um expoente negativo? [p=0.2] *Menos com menos vira mais.*"),

    # ================= BLOCO C: RENORMALIZAR — A GANGORRA =================
    dict(id="08", block="gangorra", text=
        "{t}Agora, o passo que quase todo mundo esquece. [p=0.3] {a}Às vezes a conta termina com um coeficiente *fora do "
        "padrão,* [p=0.2] como o quarenta do começo da aula: [p=0.2] quarenta vezes dez elevado a seis. [p=0.4] {b}Quarenta "
        "tem *dois* algarismos antes da vírgula. [p=0.3] Ainda não é notação científica. [p=0.4] {c}Consertar isso tem nome: "
        "[p=0.2] *renormalizar,* [p=0.2] que é reescrever o número no padrão, [p=0.2] sem mudar o valor."),
    dict(id="09", block="gangorra", text=
        "{t}E para isso, [p=0.2] uma *gangorra.* [p=0.3] {a}De um lado, o coeficiente. [p=0.2] Do outro, o expoente. "
        "[p=0.4] {b}Quarenta vira *quatro:* [p=0.2] o coeficiente ficou dez vezes menor. [p=0.4] {c}Para compensar, [p=0.2] "
        "o expoente *sobe um:* [p=0.2] de seis para *sete.* [p=0.4] {d}Quatro vezes dez elevado a sete. [p=0.3] {e}*Mesmo "
        "valor,* [p=0.2] agora na escrita certa."),
    dict(id="10", block="gangorra", text=
        "{t}E a gangorra funciona para os dois lados. [p=0.3] {a}Três vezes dez elevado a menos quatro, [p=0.2] dividido por "
        "seis vezes dez elevado a menos oito. [p=0.4] {b}Três dividido por seis: [p=0.2] *zero vírgula cinco.* [p=0.3] "
        "{c}Menos quatro, menos menos oito: [p=0.2] menos quatro *mais* oito, [p=0.2] *quatro.* [p=0.4] {d}Zero vírgula "
        "cinco é *pequeno demais:* [p=0.2] nenhum algarismo diferente de zero antes da vírgula. [p=0.4] {e}O coeficiente "
        "sobe para *cinco,* [p=0.2] e o expoente desce para *três.* [p=0.4] {f}Atalho: [p=0.2] *o que um lado da gangorra "
        "ganha, [p=0.2] o outro perde.*"),

    # ================= BLOCO D: POTÊNCIA =================
    dict(id="11", block="potencia", text=
        "{t}E para elevar a uma potência? [p=0.3] Revisão rápida da série anterior. [p=0.4] {a}Dois vezes dez elevado a "
        "menos dois, [p=0.2] tudo ao cubo. [p=0.4] {b}O expoente de fora *entra nos dois fatores.* [p=0.3] {c}Dois ao cubo, "
        "[p=0.2] *oito.* [p=0.3] {d}Dez elevado a menos dois, [p=0.2] ao cubo: [p=0.2] potência de potência *multiplica,* "
        "[p=0.2] menos dois vezes três, [p=0.2] *menos seis.* [p=0.4] {e}*Oito vezes dez elevado a menos seis.*"),

    # ================= BLOCO E: RAIZ — EXPOENTE PAR =================
    dict(id="12", block="raiz", text=
        "{t}E a raiz quadrada? [p=0.3] Aqui tem um truque. [p=0.4] {a}Raiz de quatro vírgula nove vezes dez elevado a "
        "menos cinco. [p=0.4] {b}A raiz quadrada de uma potência *divide o expoente por dois.* [p=0.3] {c}Mas menos cinco é "
        "*ímpar:* [p=0.2] ímpar é o número que não se divide por dois em partes inteiras. [p=0.4] {d}Dividir dá menos dois e "
        "meio, [p=0.2] um expoente *quebrado,* [p=0.2] que não serve em notação científica."),
    dict(id="13", block="raiz", text=
        "{t}A saída é a gangorra! [p=0.3] {a}O coeficiente sobe dez vezes: [p=0.2] quatro vírgula nove vira *quarenta e "
        "nove.* [p=0.3] {b}O expoente desce um: [p=0.2] menos cinco vira *menos seis,* [p=0.2] que é *par.* [p=0.4] {c}Agora "
        "sim: [p=0.2] raiz de quarenta e nove, [p=0.2] *sete.* [p=0.3] {d}Menos seis dividido por dois, [p=0.2] *menos três.* "
        "[p=0.4] {e}Sete vezes dez elevado a menos três. [p=0.4] {f}Atalho: [p=0.2] *antes da raiz, [p=0.2] deixe o expoente "
        "par com a gangorra.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Seis vezes dez ao cubo, [p=0.2] vezes cinco vezes dez elevado a menos sete. [p=0.3] {b}Faça "
        "a conta [p=0.2] e *renormalize.* [p=0.4] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Pista de cima: [p=0.2] seis vezes cinco, [p=0.2] *trinta.* [p=0.3] {b}Pista de "
        "baixo: [p=0.2] três mais menos sete, [p=0.2] *menos quatro.* [p=0.4] {c}Trinta vezes dez elevado a menos quatro. "
        "[p=0.3] Parou aqui? [p=0.2] *Ainda não!* [p=0.4] {d}Trinta vira três, [p=0.2] e o expoente sobe um: [p=0.2] de menos "
        "quatro para *menos três.* [p=0.4] {e}*Três vezes dez elevado a menos três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] multiplicou, [p=0.2] soma expoentes. [p=0.2] Dividiu, "
        "[p=0.2] subtrai. [p=0.5] {b}Dois: [p=0.2] fez a conta? [p=0.2] Renormalize. [p=0.5] {c}Três: [p=0.2] raiz "
        "quadrada só com expoente par."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] parar em *quarenta vezes dez elevado a seis.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o valor está correto [p=0.2] e a resposta está lá nas alternativas. [p=0.4] "
        "{c}Mas o coeficiente passou de dez: [p=0.2] *renormalize* para quatro vezes dez elevado a sete."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] errar o sinal ao subtrair um expoente negativo. [p=0.4] {b}Parece certo, [p=0.2] porque são "
        "dois sinais de menos, [p=0.2] e a pressa junta tudo num menos só. [p=0.4] {c}Mas *menos com menos vira mais:* "
        "[p=0.2] três menos menos um é *quatro.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] *multiplicar* os expoentes num produto. [p=0.4] {b}Parece certo, [p=0.2] porque os "
        "coeficientes foram multiplicados, [p=0.2] e dá vontade de fazer igual. [p=0.4] {c}Mas são duas pistas com regras "
        "diferentes: [p=0.2] em cima multiplica, [p=0.2] embaixo *soma.*"),
    dict(id="20", block="erros", text=
        "{a}Quarto: [p=0.2] tirar a raiz com o expoente *ímpar.* [p=0.4] {b}Parece certo, [p=0.2] porque é só dividir o "
        "expoente por dois. [p=0.4] {c}Mas o resultado sai quebrado. [p=0.2] Use a gangorra antes: [p=0.2] expoente *par,* "
        "[p=0.2] e só então a raiz."),

    # ================= QUESTÃO EXTRA (EU FAÇO) =================
    dict(id="21", block="q_bact", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.3] Esta primeira, eu faço com você assistindo. [p=0.4] {a}Uma bactéria "
        "tem massa aproximada de *dois vezes dez elevado a menos doze* gramas. [p=0.3] Uma colônia contém cerca de *três "
        "vezes dez elevado a oito* bactérias. [p=0.3] A massa total da colônia, em gramas, é de aproximadamente: [p=0.4] "
        "{qa}A: [p=0.2] seis vezes dez elevado a menos vinte. [p=0.3] {qb}B: [p=0.2] seis vezes dez elevado a menos quatro. "
        "[p=0.3] {qc}C: [p=0.2] cinco vezes dez elevado a menos quatro. [p=0.3] {qd}D: [p=0.2] seis vezes dez elevado a "
        "quatro. [p=0.3] {qe}E: [p=0.2] seis vezes dez elevado a noventa e seis."),
    dict(id="22", block="q_bact", text=
        "{t}Massa total é a massa de uma, [p=0.2] *vezes* o número de bactérias. [p=0.4] {a}Pista de cima: [p=0.2] dois "
        "vezes três, [p=0.2] *seis.* [p=0.3] {b}Pista de baixo: [p=0.2] *soma* os expoentes: [p=0.2] menos doze mais oito, "
        "[p=0.2] *menos quatro.* [p=0.4] {c}Seis vezes dez elevado a menos quatro grama: [p=0.2] zero vírgula zero zero zero "
        "seis. [p=0.2] Já está no padrão. [p=0.3] {ok}*Letra B!*"),
    dict(id="23", block="q_bact", text=
        "{t}E cada alternativa errada tem dono. [p=0.3] {xa}A A fez menos doze *menos* oito, [p=0.2] menos vinte: [p=0.2] "
        "errou o sinal ao somar os expoentes. [p=0.4] {xc}A C *somou* os coeficientes, [p=0.2] dois mais três. [p=0.4] "
        "{xd}A D perdeu o sinal do menos doze: [p=0.2] doze menos oito, [p=0.2] quatro. [p=0.4] {xe}E a E *multiplicou* "
        "os expoentes, [p=0.2] doze vezes oito, [p=0.2] noventa e seis: [p=0.2] usou a regra da potência de potência num "
        "produto."),

    # ================= QUESTÃO 2 DO MATERIAL (NÓS FAZEMOS) =================
    dict(id="24", block="q_data", text=
        "{t}Agora, uma do nosso material de estudo, [p=0.2] e essa a gente faz *junto.* [p=0.4] {a}Um data center possui "
        "*oito vezes dez elevado a quatro* servidores, [p=0.2] e cada servidor consome, em média, [p=0.2] *cinco vezes dez "
        "ao quadrado* watts. [p=0.3] A potência total consumida, em watts, é: [p=0.4] {qa}A: [p=0.2] um vírgula três vezes "
        "dez elevado a sete. [p=0.3] {qb}B: [p=0.2] quatro vezes dez elevado a seis. [p=0.3] {qc}C: [p=0.2] quatro vezes dez "
        "elevado a sete. [p=0.3] {qd}D: [p=0.2] quarenta vezes dez elevado a seis. [p=0.3] {qe}E: [p=0.2] quatro vezes dez "
        "elevado a oito. [p=0.4] {p}Tente o primeiro passo comigo. [p=1.2]"),
    dict(id="25", block="q_data", text=
        "{t}Pista de cima: [p=0.2] oito vezes cinco, [p=0.2] *quarenta.* [p=0.3] {a}Pista de baixo: [p=0.2] quatro mais "
        "dois, [p=0.2] *seis.* [p=0.3] {b}Quarenta vezes dez elevado a seis. [p=0.3] Conhece esse número? [p=0.2] É o do "
        "começo da aula! [p=0.4] {c}Gangorra: [p=0.2] quarenta vira quatro, [p=0.2] o expoente sobe para sete. [p=0.3] "
        "{ok}*Letra C.*"),
    dict(id="26", block="q_data", text=
        "{xd}A D é a armadilha de quem parou *um passo antes.* [p=0.4] {xa}A A somou oito mais cinco. [p=0.4] {xb}A B "
        "cortou o zero do quarenta [p=0.2] e esqueceu de subir o expoente. [p=0.4] {xe}E a E subiu o expoente *duas* vezes."),

    # ================= QUESTÃO 3 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="27", block="q_imp", text=
        "{t}Agora é com você. [p=0.3] {a}Uma impressora 3D deposita material em camadas de *cinco vezes dez elevado a menos "
        "cinco* metro de espessura. [p=0.3] Para produzir uma peça com *dois vezes dez elevado a menos dois* metro de altura, "
        "[p=0.2] o número de camadas necessárias é: [p=0.4] {qa}A: [p=0.2] vinte e cinco. [p=0.3] {qb}B: [p=0.2] quarenta. "
        "[p=0.3] {qc}C: [p=0.2] duzentos e cinquenta. [p=0.3] {qd}D: [p=0.2] quatrocentos. [p=0.3] {qe}E: [p=0.2] quatro "
        "mil. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q_imp", text=
        "{t}Quantas camadas cabem na altura? [p=0.2] É *divisão:* [p=0.2] altura dividida pela espessura. [p=0.4] {a}Pista "
        "de cima: [p=0.2] dois dividido por cinco, [p=0.2] *zero vírgula quatro.* [p=0.4] {b}Pista de baixo, [p=0.2] em "
        "câmera lenta: [p=0.3] menos dois, [p=0.3] menos, [p=0.3] menos cinco. [p=0.5] {c}Menos com menos vira mais: "
        "[p=0.3] menos dois *mais* cinco, [p=0.3] *mais três.* [p=0.4] {d}Zero vírgula quatro vezes dez ao cubo. [p=0.3] "
        "Gangorra: [p=0.2] quatro vezes dez ao quadrado, [p=0.2] *quatrocentas* camadas. [p=0.3] {ok}*Letra D.*"),
    dict(id="29", block="q_imp", text=
        "{t}E repare: [p=0.2] quem errou o sinal [p=0.2] e fez menos dois menos cinco, [p=0.2] menos sete, [p=0.2] chega a "
        "*menos de uma* camada. [p=0.3] Absurdo! [p=0.4] {xa}A A e a C trazem o dois e meio [p=0.2] de quem dividiu ao "
        "contrário, [p=0.2] cinco por dois. [p=0.4] {xb}E a B e a E erraram a gangorra: [p=0.2] o expoente desceu demais, "
        "[p=0.2] ou não desceu."),

    # ================= QUESTÃO 8 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="30", block="q_placa", text=
        "{t}A última. [p=0.3] {a}Uma placa quadrada tem área de *um vírgula seis vezes dez elevado a menos cinco* metro "
        "quadrado. [p=0.3] A medida do lado dessa placa, em metros, é: [p=0.4] {qa}A: [p=0.2] quatro vezes dez elevado a "
        "menos três. [p=0.3] {qb}B: [p=0.2] quatro vezes dez elevado a menos dois vírgula cinco. [p=0.3] {qc}C: [p=0.2] um "
        "vírgula vinte e seis vezes dez elevado a menos três. [p=0.3] {qd}D: [p=0.2] oito vezes dez elevado a menos três. "
        "[p=0.3] {qe}E: [p=0.2] quatro vezes dez elevado a menos seis. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="31", block="q_placa", text=
        "{t}O lado do quadrado é a *raiz* da área. [p=0.3] {a}Mas o expoente, [p=0.2] menos cinco, [p=0.2] é ímpar. "
        "[p=0.4] {b}Gangorra: [p=0.2] o coeficiente sobe para *dezesseis,* [p=0.2] o expoente desce para *menos seis.* "
        "[p=0.4] {c}Raiz de dezesseis, [p=0.2] *quatro.* [p=0.2] Menos seis dividido por dois, [p=0.2] *menos três.* "
        "[p=0.3] {ok}*Letra A.* [p=0.4] {d}Confira elevando ao quadrado: [p=0.2] quatro ao quadrado, dezesseis; [p=0.2] "
        "menos três vezes dois, menos seis. [p=0.2] Voltou certinho."),
    dict(id="32", block="q_placa", text=
        "{xb}A B dividiu o expoente ímpar por dois: [p=0.2] expoente quebrado. [p=0.4] {xc}A C tirou a raiz do um vírgula "
        "seis [p=0.2] e arredondou o expoente. [p=0.4] {xd}A D dividiu o dezesseis por dois, [p=0.2] em vez de tirar a raiz. "
        "[p=0.4] {xe}E a E tirou a raiz do dezesseis, [p=0.2] mas esqueceu a raiz da potência de dez."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] multiplicou, [p=0.2] soma expoentes. [p=0.2] "
        "Dividiu, [p=0.2] subtrai. [p=0.5] {b}Dois: [p=0.2] fez a conta? [p=0.2] Renormalize. [p=0.5] {c}Três: [p=0.2] "
        "raiz quadrada só com expoente par."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Multiplicar e dividir funcionam com expoentes *diferentes.* [p=0.4] {b}Somar e subtrair, [p=0.2] *não.* [p=0.4] "
        "{c}É a operação que mais derruba. [p=0.3] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha parado no quarenta vezes dez elevado a seis? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
