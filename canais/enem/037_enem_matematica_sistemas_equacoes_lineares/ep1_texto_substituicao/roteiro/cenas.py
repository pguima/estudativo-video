# Roteiro — Sistemas de Equações Lineares, Episódio 1 de 5: o que é um sistema, do texto ao sistema e a substituição.
# Base: Estudos/Enem/estudos/01-matematica/22-sistemas-equacoes-lineares.html — seções 02, 03 e 04 + Questões 1, 5 e 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Duas incógnitas pedem DUAS PISTAS: cada informação do texto vira uma equação.
#   O MOLDE: uma equação CONTA (cabeças, ingressos, veículos) e a outra SOMA VALORES (patas, reais, rodas).
#   Substituir é TROCAR A PEÇA pelo seu equivalente: m vale 30 − c, então onde estava m entra (30 − c), com parênteses.
#   TUDO DE UM TIPO: finja que todos são motos e veja quantas rodas faltam.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (do prompt e do material, conferidos em Python):
#   g + c = 10 e 2g + 4c = 28 → (6, 4); tabela de tentativas (0,10)…(10,0) com 40, 38, …, 20 patas: só (6, 4) dá 28.
#   Distrator (nosso): (10, 2) dá 28 patas mas 12 cabeças; (4, 6) dá 10 cabeças mas 32 patas.
#   Prova +5/−2: a + e = 20 e 5a − 2e = 51 → 13 acertos e 7 erros (65 − 14 = 51).
#   Carros e motos: c + m = 30 e 4c + 2m = 100 → c = 20, m = 10; erro 60 − c → 3c = 40 → c ≈ 13,3 (não é inteiro: denuncia).
#   Atalho: 30 motos = 60 rodas; faltam 40; 40 ÷ 2 = 20 carros.
# Nós fazemos (prompt): c + m = 25 e 4c + 2m = 70 → 10 carros e 15 motos; atalho 50 rodas, faltam 20, 20 ÷ 2 = 10.
# QUESTÃO 1 (eu faço, texto idêntico): i = 400 − m → 16 000 − 40m + 20m = 11 200 → m = 240 → D. Erradas (do material):
#   B 160 é o número de inteiras; C ≈ 187 é 11 200 ÷ 60, conta sem sentido; E 280 é 11 200 ÷ 40 (todos pagando inteira);
#   A 120 é 400 − 280, consequência do mesmo erro.
# QUESTÃO 5 (nós fazemos, texto idêntico): P = 2J e P − 6 = J + 6 → J = 12, P = 24 → D; depois da troca, 18 cada.
#   Erradas (do material): B 12 é Júlia (e o que sai para Pedro com P − 6 = J); C 18 é depois da troca; E 36 é o total;
#   A 6 são só as moedas transferidas.
# QUESTÃO 9 (você faz, texto idêntico): 20 + 60t = 200 − 120t → t = 1 h, km 80 → B. Erradas (do material): C 110 é o ponto
#   médio (só com velocidades iguais); D 140 troca as velocidades (20 + 120 · 1); A 60 é o deslocamento do carro; E 180 é a
#   distância inicial. Explicação nossa da posição: "onde ele está = onde começou + quanto andou" (60 km por hora · t horas).
# Acréscimos nossos (verde): "teste a tradução com números pequenos"; "tudo de um tipo" (do material) também no nós fazemos;
#   "confira o par nas DUAS equações".
# Frases-chave (meio e fim, idênticas): 1. Uma equação por informação. 2. Uma equação conta, a outra soma valores.
#   3. Substituiu? Ponha parênteses.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Sistema de equações do zero: do texto ao sistema e a substituição · Matemática ENEM, Sistemas episódio 1"

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
        "{a}*Pedro tem o dobro das moedas de Júlia.* [p=0.4] {b}Metade das pessoas escreve [p=0.2] *dois P igual a J,* "
        "[p=0.2] e está *errado.* [p=0.4] {c}Teste com Júlia tendo *cinco:* [p=0.2] Pedro tem *dez,* [p=0.2] e dez é igual "
        "a dois vezes cinco. [p=0.4] {d}A tradução certa é [p=0.2] *P igual a dois J.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai *transformar um texto em sistema* [p=0.3] {b}e resolvê-lo pela *substituição* "
        "[p=0.2] *sem perder sinal.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Equações do primeiro grau: [p=0.2] antes de montar, "
        "[p=0.2] cole uma *etiqueta* no x, [p=0.2] dizendo o que ele conta. [p=0.4] {b}Da série de Expressões Algébricas, a *distributiva:* [p=0.2] o número da frente "
        "multiplica *cada* termo do parêntese. [p=0.2] Dois vezes, trinta menos c: [p=0.2] *sessenta menos dois c.*"),

    # ================= CONCRETO: O SÍTIO =================
    dict(id="04", block="sitio", text=
        "{t}Imagine um sítio [p=0.2] com *galinhas e coelhos.* [p=0.3] {a}Você conta *dez cabeças.* [p=0.3] Quantas são "
        "galinhas? [p=0.5] {b}Podem ser [p=0.2] *uma galinha e nove coelhos.* [p=0.2] Ou *duas e oito.* [p=0.2] Ou *seis e "
        "quatro.* [p=0.4] {c}Só com as cabeças, [p=0.2] há *muitas* respostas."),
    dict(id="05", block="sitio", text=
        "{t}E se você contar também as *patas?* [p=0.3] {a}São *vinte e oito.* [p=0.2] Galinha tem duas patas; [p=0.2] "
        "coelho tem quatro. [p=0.4] {b}Vamos testar cada divisão das dez cabeças. [p=0.3] Quarenta patas, [p=0.2] trinta e "
        "oito, [p=0.2] trinta e seis... [p=0.4] {c}Só *uma* dá vinte e oito: [p=0.2] *seis galinhas e quatro coelhos.* "
        "[p=0.4] {d}A segunda informação [p=0.2] *escolheu* uma resposta só."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="06", block="definicao", text=
        "{t}Isso tem nome. [p=0.4] {a}Cada valor escondido [p=0.2] é uma *incógnita:* [p=0.2] aqui, "
        "*g* para galinhas e *c* para coelhos. [p=0.4] {b}Um *sistema linear* [p=0.2] é um grupo de equações do primeiro "
        "grau [p=0.2] que valem *ao mesmo tempo.* [p=0.4] {c}A resposta vem *em dupla,* [p=0.2] numa ordem combinada: "
        "[p=0.2] é o *par ordenado,* [p=0.2] seis vírgula quatro. [p=0.4] {d}E a *solução do sistema* [p=0.2] é o par que "
        "satisfaz *todas* as equações."),
    dict(id="07", block="definicao", text=
        "{t}Como fica o sítio em equações? [p=0.4] {a}Cabeças: [p=0.2] *g mais c igual a dez.* [p=0.4] {b}Patas: [p=0.2] "
        "*dois g mais quatro c igual a vinte e oito.* [p=0.4] {c}Confira o seis vírgula quatro nas *duas.* [p=0.2] Seis "
        "mais quatro, [p=0.2] *dez.* [p=0.2] Doze mais dezesseis, [p=0.2] *vinte e oito.* [p=0.2] Fecha nas duas. "
        "[p=0.4] {d}Duas incógnitas pedem *duas pistas:* [p=0.2] cada informação do texto [p=0.2] vira uma equação."),

    # ================= BLOCO C: TESTAR É PERMITIDO =================
    dict(id="08", block="testar", text=
        "{t}E na prova, dá para testar as alternativas? [p=0.4] {a}Dá. [p=0.2] Mas teste nas *duas* equações. [p=0.4] {b}O par dez vírgula dois [p=0.2] dá vinte e oito patas. [p=0.2] Só que são *doze "
        "cabeças.* [p=0.4] {c}O quatro vírgula seis dá dez cabeças, [p=0.2] mas *trinta e duas patas.* [p=0.4] {d}Um par "
        "que fecha só *uma* equação [p=0.2] é a *alternativa-armadilha* típica."),

    # ================= BLOCO D: O MOLDE =================
    dict(id="09", block="molde", text=
        "{t}E por que quase toda questão parece igual? [p=0.4] {a}Porque segue o mesmo *molde.* [p=0.2] Uma equação "
        "*conta:* [p=0.2] é a *equação das quantidades.* [p=0.4] {b}A outra *soma valores:* [p=0.2] patas, reais, rodas. "
        "[p=0.2] É a *equação dos valores.* [p=0.4] {c}Ingressos e reais. [p=0.2] Veículos e rodas. [p=0.2] Quilos de café e o preço da mistura. [p=0.3] {d}Sempre: "
        "[p=0.2] uma conta, [p=0.2] outra soma valores."),
    dict(id="10", block="molde", text=
        "{t}Até prova com nota negativa cabe no molde. [p=0.4] {a}Vinte questões. [p=0.2] Cada acerto vale *mais cinco;* "
        "[p=0.2] cada erro, *menos dois.* [p=0.2] A nota foi cinquenta e um. [p=0.4] {b}Quantidades: [p=0.2] *a mais e "
        "igual a vinte.* [p=0.2] Valores: [p=0.2] *cinco a menos dois e igual a cinquenta e um.* [p=0.4] {c}A resposta: "
        "[p=0.2] *treze acertos e sete erros.* [p=0.3] Confira: [p=0.2] sessenta e cinco menos catorze, [p=0.2] *cinquenta "
        "e um.*"),

    # ================= BLOCO E: FRASES DE COMPARAÇÃO =================
    dict(id="11", block="comparacao", text=
        "{t}E as frases de comparação? [p=0.4] {a}*Pedro tem o dobro de Júlia.* [p=0.2] Quem tem mais? [p=0.2] Pedro. "
        "[p=0.2] Então é *P igual a dois J.* [p=0.4] {b}Na dúvida, [p=0.2] *teste com números pequenos.* [p=0.2] Júlia "
        "com cinco, Pedro com dez: [p=0.2] fecha. [p=0.4] {c}Agora: [p=0.2] *se Pedro der seis moedas a Júlia, ficam "
        "iguais.* [p=0.4] {d}Quem dá, *perde;* [p=0.2] quem recebe, *ganha.* [p=0.2] *P menos seis igual a J mais seis.* "
        "[p=0.2] A troca mexe nos *dois* lados."),

    # ================= BLOCO F: SUBSTITUIÇÃO =================
    dict(id="12", block="substituicao", text=
        "{t}E como resolver? [p=0.4] {a}Trinta veículos, carros e motos, [p=0.2] e cem "
        "rodas. [p=0.2] *c mais m igual a trinta;* [p=0.2] *quatro c mais dois m igual a cem.* [p=0.4] {b}O método da "
        "*substituição:* [p=0.2] isole uma letra numa equação [p=0.2] e troque essa letra na outra. [p=0.4] {c}Passo um: "
        "[p=0.2] da primeira, [p=0.2] *m é igual a trinta menos c.*"),
    dict(id="13", block="substituicao", text=
        "{t}Passo dois: [p=0.2] trocar a peça. [p=0.4] {a}Onde estava o *m* na segunda equação, [p=0.2] entra *trinta "
        "menos c,* [p=0.2] *com parênteses e tudo.* [p=0.4] {b}Quatro c [p=0.2] mais dois vezes, trinta menos c, [p=0.2] "
        "igual a cem. [p=0.4] {c}Distributiva: [p=0.2] *quatro c mais sessenta menos dois c.* [p=0.2] *Dois c igual a quarenta,* "
        "[p=0.2] *c igual a vinte.* [p=0.4] {d}Passo três: [p=0.2] m é trinta menos vinte, [p=0.2] *dez.* "
        "[p=0.3] Confira: [p=0.2] oitenta rodas mais vinte, [p=0.2] *cem.*"),

    # ================= BLOCO G: TUDO DE UM TIPO =================
    dict(id="14", block="umtipo", text=
        "{t}Dá para fazer isso de cabeça? [p=0.4] {a}Dá. [p=0.2] Finja que os trinta veículos são *todos motos.* [p=0.2] "
        "Seriam *sessenta rodas.* [p=0.4] {b}Mas são cem. [p=0.2] *Faltam quarenta.* [p=0.4] {c}Cada vez que você troca "
        "uma moto por um carro, [p=0.2] ganha *duas rodas.* [p=0.4] {d}Quarenta dividido por dois: [p=0.2] *vinte "
        "carros.* [p=0.2] É a mesma conta da substituição, [p=0.2] feita de cabeça."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Num estacionamento há *vinte e cinco veículos,* [p=0.2] entre carros e motos, [p=0.2] com "
        "*setenta rodas.* [p=0.2] Quantos são os carros? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}*c mais m igual a vinte e cinco;* [p=0.2] *quatro c mais dois m igual a setenta.* "
        "[p=0.4] {b}m é vinte e cinco menos c. [p=0.2] Quatro c mais cinquenta menos dois c [p=0.2] igual a setenta. "
        "[p=0.2] Dois c igual a vinte: [p=0.2] *dez carros* [p=0.2] e *quinze motos.* [p=0.4] {c}Pelo atalho: [p=0.2] "
        "todas motos, cinquenta rodas. [p=0.2] Faltam vinte. [p=0.2] Vinte dividido por dois: [p=0.2] *dez.* [p=0.4] "
        "{d}Confira: [p=0.2] quarenta mais trinta, [p=0.2] *setenta rodas.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] uma equação por informação. [p=0.5] {b}Dois: [p=0.2] "
        "uma equação conta, a outra soma valores. [p=0.5] {c}Três: [p=0.2] substituiu? Ponha parênteses."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *Pedro tem o dobro de Júlia* [p=0.2] escrito "
        "*dois P igual a J.* [p=0.4] {b}Parece certo, [p=0.2] porque o *dois* aparece perto do *Pedro* na frase. [p=0.4] "
        "{c}Mas teste com números: [p=0.2] Júlia cinco, Pedro dez. [p=0.2] O dois multiplica *quem tem menos:* [p=0.2] *P "
        "igual a dois J.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] *dois vezes, trinta menos c* [p=0.2] virar *sessenta menos c.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o dois parece encostado só no trinta. [p=0.4] {c}Mas o coeficiente multiplica *tudo:* [p=0.2] "
        "*sessenta menos dois c.* [p=0.2] Com o erro, [p=0.2] saem *treze vírgula três* carros: "
        "[p=0.2] não existe."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *se Pedro der seis moedas* [p=0.2] escrito *P menos seis igual a J.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque a frase só fala do Pedro dando. [p=0.4] {c}Mas quem recebe também muda: [p=0.2] *P menos "
        "seis igual a J mais seis.*"),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] responder a *outra* incógnita. [p=0.2] Achou os carros, [p=0.2] mas a pergunta era das "
        "*motos.* [p=0.4] {b}Parece certo, [p=0.2] porque o número que você achou *está nas alternativas.* [p=0.4] "
        "{c}Antes de marcar, [p=0.2] *releia a pergunta* [p=0.2] e olhe a etiqueta."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="22", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, *eu faço.* [p=0.4] {a}Um teatro "
        "vendeu *quatrocentos ingressos* para uma sessão, [p=0.2] alguns pelo preço inteiro de *quarenta reais* [p=0.2] e "
        "os demais pela meia-entrada de *vinte reais.* [p=0.2] A arrecadação total foi de *onze mil e duzentos reais.* "
        "[p=0.2] O número de meias-entradas vendidas foi: [p=0.4] {qa}A: [p=0.2] cento e vinte. [p=0.3] {qb}B: [p=0.2] "
        "cento e sessenta. [p=0.3] {qc}C: [p=0.2] cerca de cento e oitenta e sete. [p=0.3] {qd}D: [p=0.2] duzentos e "
        "quarenta. [p=0.3] {qe}E: [p=0.2] duzentos e oitenta."),
    dict(id="23", block="q1", text=
        "{t}Etiquetas: [p=0.2] *i* são as inteiras, [p=0.2] *m* são as meias. [p=0.4] {a}Quantidades: [p=0.2] *i mais m "
        "igual a quatrocentos.* [p=0.2] Valores: [p=0.2] *quarenta i mais vinte m igual a onze mil e duzentos.* [p=0.4] "
        "{b}Isolando: [p=0.2] i é quatrocentos menos m. [p=0.2] Com parênteses: [p=0.2] quarenta vezes, quatrocentos "
        "menos m: [p=0.2] *dezesseis mil menos quarenta m.* [p=0.4] {c}Mais vinte m: [p=0.2] dezesseis mil menos vinte m "
        "[p=0.2] igual a onze mil e duzentos. [p=0.2] Vinte m igual a quatro mil e oitocentos: [p=0.2] *m igual a duzentos "
        "e quarenta.* [p=0.4] {d}Confira: [p=0.2] seis mil e quatrocentos das inteiras, [p=0.2] mais quatro mil e oitocentos "
        "das meias: [p=0.2] *onze mil e duzentos.* [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="q1", text=
        "{t}E as erradas? [p=0.3] {xb}A B, cento e sessenta, [p=0.2] é o número de *inteiras:* [p=0.2] resposta da outra "
        "incógnita. [p=0.4] {xc}A C divide onze mil e duzentos por sessenta, [p=0.2] a soma dos preços, [p=0.2] conta sem sentido "
        "no problema. [p=0.4] {xe}A E divide o total por quarenta, [p=0.2] como se *todos* "
        "pagassem inteira. [p=0.4] {xa}E a A [p=0.2] é quatrocentos menos duzentos e oitenta, [p=0.2] consequência desse "
        "mesmo erro."),

    # ================= QUESTÃO 5 (NÓS FAZEMOS) =================
    dict(id="25", block="q5", text=
        "{t}A próxima, *nós fazemos.* [p=0.4] {a}Pedro tem o *dobro* do número de moedas de Júlia. [p=0.2] Se Pedro *der "
        "seis* de suas moedas a Júlia, [p=0.2] os dois ficarão com a *mesma quantidade.* [p=0.2] Quantas moedas Pedro tem? "
        "[p=0.4] {qa}A: [p=0.2] seis. [p=0.3] {qb}B: [p=0.2] doze. [p=0.3] {qc}C: [p=0.2] dezoito. [p=0.3] {qd}D: [p=0.2] "
        "vinte e quatro. [p=0.3] {qe}E: [p=0.2] trinta e seis. [p=0.4] {p}Monte as duas equações. [p=0.2] *Pause.* "
        "[p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Uma equação por informação. [p=0.4] {a}O dobro: [p=0.2] *P igual a dois J.* [p=0.2] A troca: [p=0.2] *P menos "
        "seis igual a J mais seis.* [p=0.4] {b}Substitua o P por dois J: [p=0.2] dois J menos seis igual a J mais seis. "
        "[p=0.2] Sobra *J igual a doze.* [p=0.4] {c}E Pedro, o dobro: [p=0.2] *vinte e quatro.* [p=0.4] {d}Confira: [p=0.2] "
        "vinte e quatro menos seis, *dezoito;* [p=0.2] doze mais seis, *dezoito.* [p=0.2] Iguais. [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="q5", text=
        "{t}E as erradas? [p=0.3] {xb}A B, doze, [p=0.2] é o número de *Júlia.* [p=0.2] E o que sai para Pedro "
        "esquecendo que Júlia *recebe.* [p=0.4] {xc}A C, dezoito, [p=0.2] é quanto cada um tem *depois* da "
        "troca. [p=0.4] {xe}A E, trinta e seis, [p=0.2] é o *total* dos dois. [p=0.4] {xa}E a A, seis, [p=0.2] é só o "
        "número de moedas *transferidas.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="28", block="q9", text=
        "{t}A última é *sua.* [p=0.4] {a}Às oito horas, [p=0.2] um carro passa pelo *quilômetro vinte* de uma rodovia, "
        "[p=0.2] a *sessenta quilômetros por hora,* [p=0.2] no sentido crescente da quilometragem. [p=0.2] No mesmo "
        "instante, [p=0.2] um ônibus passa pelo *quilômetro duzentos,* [p=0.2] a *cento e vinte quilômetros por hora,* "
        "[p=0.2] no sentido contrário. [p=0.2] Mantidas as velocidades, [p=0.2] os dois se cruzarão no: [p=0.4] {qa}A: "
        "[p=0.2] quilômetro sessenta. [p=0.3] {qb}B: [p=0.2] quilômetro oitenta. [p=0.3] {qc}C: [p=0.2] quilômetro cento e "
        "dez. [p=0.3] {qd}D: [p=0.2] quilômetro cento e quarenta. [p=0.3] {qe}E: [p=0.2] quilômetro cento e oitenta. "
        "[p=0.4] {h}Uma dica: [p=0.2] onde cada um está [p=0.2] é *onde começou, mais ou menos o que andou.* [p=0.2] "
        "*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Etiqueta: [p=0.2] *t,* as horas depois das oito. [p=0.4] {a}O carro começa no vinte [p=0.2] e *anda* "
        "sessenta por hora: [p=0.2] *vinte mais sessenta t.* [p=0.4] {b}O ônibus começa no duzentos [p=0.2] e a "
        "quilometragem *diminui* cento e vinte por hora: [p=0.2] *duzentos menos cento e vinte t.* [p=0.4] {c}Cruzar é "
        "estar no *mesmo lugar, no mesmo instante.* [p=0.2] Iguale: [p=0.2] cento e oitenta t igual a cento e oitenta, "
        "[p=0.2] *t igual a uma hora.* [p=0.4] {d}Posição: [p=0.2] vinte mais sessenta, [p=0.2] *quilômetro oitenta.* "
        "[p=0.2] Confira no ônibus: [p=0.2] duzentos menos cento e vinte, [p=0.2] *oitenta.* [p=0.3] {ok}*Letra B!*"),
    dict(id="30", block="q9", text=
        "{t}E as erradas? [p=0.3] {xc}A C, cento e dez, [p=0.2] é o *ponto médio.* [p=0.2] Só valeria se as velocidades "
        "fossem iguais. [p=0.4] {xd}A D *troca as velocidades,* [p=0.2] pondo o carro a cento e vinte. [p=0.4] {xa}A A, "
        "sessenta, [p=0.2] é quanto o carro *andou,* [p=0.2] e não *onde* ele está. [p=0.4] {xe}E a E, cento e oitenta, "
        "[p=0.2] é a *distância inicial* entre os dois."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] uma equação por informação. [p=0.5] {b}Dois: "
        "[p=0.2] uma equação conta, a outra soma valores. [p=0.5] {c}Três: [p=0.2] substituiu? Ponha parênteses."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Dois sanduíches e um suco [p=0.2] custam *trinta e um reais;* [p=0.3] um sanduíche e dois sucos, [p=0.2] "
        "*vinte e seis.* [p=0.4] {b}Quanto custa *um de cada?* [p=0.4] {c}Dá para responder *em uma linha,* [p=0.2] sem "
        "descobrir o preço de nenhum. [p=0.4] {d}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses quatro erros você já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
