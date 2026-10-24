# Roteiro — Velocidade, Densidade e Vazão, Episódio 1 de 6: a estrutura comum (toda taxa é "quanto por unidade")
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seções 02, 07 e 08 + Questão 8 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A BARRA da unidade é um sinal de DIVIDIR: quilômetro POR hora é quilômetro DIVIDIDO por hora.
#   A UNIDADE ESCREVE A FÓRMULA sozinha: anote a unidade ao lado de cada número e a conta aparece.
#   A taxa é como o PREÇO DO QUILO: comprar 1 kg ou 10 kg de arroz não muda o preço do quilo.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos NOSSOS (o recorte não traz contas): três perguntas com o mesmo carro (160 km em 2 h = 80 km/h; 80 km/h por 3 h
#   = 240 km; 240 km a 80 km/h = 3 h); taxa constante com a água (200 g em 200 cm³ e 1 000 g em 1 000 cm³ = 1 g/cm³);
#   comparação de densidade demográfica (1 000 000 hab em 500 km² = 2 000 hab/km² × 200 000 hab em 50 km² = 4 000 hab/km²).
# Nós fazemos (prompt): arroz 5 kg por R$ 22,50 = R$ 4,50/kg × 2 kg por R$ 9,60 = R$ 4,80/kg → o de 5 kg é mais barato.
# QUESTÃO 8 (texto idêntico na tela, "eu faço"): 420 km ÷ 35 L = 12 km/L → C. Conferência: faixa de 10 a 15 km/L.
#   CORREÇÃO AO PROMPT: ele pede para explicar as erradas "como resultados fora da faixa plausível", mas só a A (8 km/L) está
#   fora da faixa de 10 a 15. B (10), D (14) e E (15) estão DENTRO dela. Explicação NOSSA: a faixa elimina a A; as outras
#   caem multiplicando de volta (35 L × 10 = 350 km; × 14 = 490 km; × 15 = 525 km; nenhuma dá 420 km). O material não
#   explica as erradas.
#   Depois (prompt): com 50 L → 12 × 50 = 600 km (eu faço); para 300 km → 300 ÷ 12 = 25 L ("você faz", com pausa).
# Atalhos (verde): "a unidade se cancela" (km/h × h = km; km ÷ km/h = h) · comparar só pela taxa (divida cada preço pelo
#   peso) · "multiplique de volta" para conferir uma taxa.
# Frases-chave (meio e fim, idênticas): 1. A barra da unidade é um sinal de dividir.
#   2. Taxa: divida. Numerador: multiplique. Denominador: divida ao contrário. 3. A taxa não muda com a quantidade.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Velocidade, densidade e vazão são UMA conta só · Matemática ENEM, Taxas episódio 1"

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
        "{a}Velocidade, [p=0.2] densidade, [p=0.2] vazão, [p=0.2] consumo do carro, [p=0.2] preço do quilo, [p=0.2] "
        "habitantes por quilômetro quadrado. [p=0.4] {b}Parecem *seis assuntos.* [p=0.4] {c}São *um só.* [p=0.4] "
        "{d}E quem percebe isso [p=0.2] estuda *seis vezes menos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai olhar para qualquer unidade com *barra* [p=0.3] {b}e saber na hora "
        "[p=0.2] se deve *multiplicar* [p=0.2] ou *dividir.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Razão: [p=0.2] *razão* é uma comparação feita por "
        "*divisão.* [p=0.2] Dois para cinco [p=0.2] é dois dividido por cinco. [p=0.4] {b}E, da série de Unidades: "
        "[p=0.2] uma *unidade composta* junta duas unidades numa só, [p=0.2] como *quilômetro por hora.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três coisas. [p=0.3] {a}O *painel do carro:* [p=0.2] oitenta quilômetros por hora [p=0.2] "
        "e doze quilômetros por litro. [p=0.4] {b}A *etiqueta* do supermercado: [p=0.2] quatro reais e cinquenta por "
        "quilo. [p=0.4] {c}A *conta de água:* [p=0.2] cento e cinquenta litros por dia. [p=0.4] {d}Repare na palavra "
        "que se repete: [p=0.2] *por.*"),

    # ================= BLOCO A: A ESTRUTURA COMUM =================
    dict(id="05", block="definicao", text=
        "{t}E o que essas coisas têm em comum? [p=0.4] {a}Todas são uma *taxa.* [p=0.3] Taxa é *quanto de uma coisa* "
        "[p=0.2] *por unidade de outra.* [p=0.4] {b}E toda taxa é uma *razão,* [p=0.2] uma divisão. [p=0.3] {c}O de "
        "cima é o *numerador:* [p=0.2] o quanto. [p=0.2] O de baixo é o *denominador:* [p=0.2] a unidade de "
        "referência."),
    dict(id="06", block="definicao", text=
        "{t}Agora olhe as três estrelas deste assunto. [p=0.3] {a}*Velocidade:* [p=0.2] distância dividida por tempo. "
        "[p=0.3] {b}*Densidade:* [p=0.2] massa dividida por volume. [p=0.3] {c}*Vazão:* [p=0.2] volume dividido por "
        "tempo. [p=0.4] {d}Lado a lado: [p=0.2] *a mesma forma.* [p=0.2] Uma coisa em cima, [p=0.2] outra embaixo."),

    # ================= BLOCO B: A UNIDADE ESCREVE A FÓRMULA =================
    dict(id="07", block="unidade", text=
        "{t}E se você esquecer a fórmula? [p=0.4] {a}Não precisa decorar. [p=0.2] *A unidade já escreve a fórmula.* "
        "[p=0.4] {b}Quilômetro *por* hora [p=0.2] é quilômetro *dividido* por hora. [p=0.3] *A barra da unidade é um "
        "sinal de dividir.* [p=0.4] {c}Grama por centímetro cúbico: [p=0.2] massa *dividida* por volume. [p=0.2] "
        "Litro por minuto: [p=0.2] volume *dividido* por tempo. [p=0.4] {d}Anote a unidade ao lado de cada número, "
        "[p=0.2] e a conta aparece sozinha."),

    # ================= BLOCO C: AS TRÊS PERGUNTAS =================
    dict(id="08", block="perguntas", text=
        "{t}Quantos tipos de pergunta uma taxa pode fazer? [p=0.4] {a}Só *três.* [p=0.3] E todas saem do mesmo "
        "triângulo: [p=0.2] o numerador em cima, [p=0.2] a taxa e o denominador embaixo. [p=0.4] {b}Primeira: "
        "[p=0.2] *achar a taxa.* [p=0.2] Um carro faz cento e sessenta quilômetros em duas horas. [p=0.4] {c}Taxa: "
        "[p=0.2] *divida.* [p=0.2] Cento e sessenta dividido por dois: [p=0.2] *oitenta quilômetros por hora.*"),
    dict(id="09", block="perguntas", text=
        "{t}Segunda: [p=0.2] *achar o numerador.* [p=0.3] {a}O carro anda a oitenta quilômetros por hora [p=0.2] durante "
        "três horas. [p=0.2] Quantos quilômetros? [p=0.4] {b}Numerador: [p=0.2] *multiplique.* [p=0.2] Oitenta vezes "
        "três: [p=0.2] *duzentos e quarenta quilômetros.*"),
    dict(id="10", block="perguntas", text=
        "{t}Terceira: [p=0.2] *achar o denominador.* [p=0.3] {a}Duzentos e quarenta quilômetros, [p=0.2] a oitenta "
        "quilômetros por hora. [p=0.2] Quantas horas? [p=0.4] {b}Denominador: [p=0.2] *divida ao contrário:* [p=0.2] o "
        "numerador dividido pela taxa. [p=0.2] Duzentos e quarenta dividido por oitenta: [p=0.2] *três horas.*"),
    dict(id="11", block="atalho", text=
        "{t}E como não trocar as contas? [p=0.4] {a}Atalho: [p=0.2] *deixe a unidade se cancelar.* [p=0.4] {b}Quilômetro "
        "por hora, [p=0.2] vezes hora: [p=0.2] a hora de cima cancela a de baixo [p=0.2] e sobra *quilômetro.* [p=0.4] "
        "{c}Quilômetro dividido por quilômetro por hora: [p=0.2] o quilômetro cancela [p=0.2] e sobra *hora.* [p=0.4] "
        "{d}Sobrou a unidade pedida? [p=0.2] A conta está certa."),

    # ================= BLOCO D: A TAXA NÃO MUDA COM A QUANTIDADE =================
    dict(id="12", block="constante", text=
        "{t}Se o carro andar o dobro do tempo, [p=0.2] a velocidade dobra? [p=0.4] {a}Não. [p=0.2] Oitenta "
        "quilômetros em uma hora, [p=0.2] ou cento e sessenta em duas: [p=0.2] *oitenta quilômetros por hora* nos "
        "dois casos. [p=0.4] {b}A distância dobrou, [p=0.2] o tempo dobrou, [p=0.2] e a divisão ficou igual. [p=0.4] "
        "{c}É como o *preço do quilo:* [p=0.2] comprar um quilo ou dez quilos de arroz [p=0.2] não muda o preço do "
        "quilo."),
    dict(id="13", block="constante", text=
        "{t}E com a densidade? [p=0.3] {a}Um copo de água: [p=0.2] duzentos gramas em duzentos centímetros cúbicos. "
        "[p=0.2] *Um grama por centímetro cúbico.* [p=0.4] {b}Uma garrafa: [p=0.2] mil gramas em mil centímetros "
        "cúbicos. [p=0.2] *Um grama por centímetro cúbico.* [p=0.4] {c}A quantidade mudou, [p=0.2] a densidade não. "
        "[p=0.3] Por isso ela identifica o *material,* [p=0.2] como você viu em Química."),

    # ================= BLOCO E: AS OUTRAS TAXAS =================
    dict(id="14", block="outras", text=
        "{t}E a prova inventa outras? [p=0.3] Inventa, [p=0.2] todas com a mesma forma. [p=0.4] {a}*Rendimento:* "
        "[p=0.2] quilômetros por litro de combustível. [p=0.3] {b}*Concentração:* [p=0.2] gramas "
        "por litro. [p=0.3] {c}*Densidade demográfica:* [p=0.2] habitantes por quilômetro quadrado. [p=0.3] "
        "{d}*Produtividade:* [p=0.2] sacas colhidas por hectare."),
    dict(id="15", block="outras", text=
        "{a}*Preço unitário:* [p=0.2] o preço de uma unidade, [p=0.2] reais por quilo. [p=0.3] {b}*Pressão:* [p=0.2] "
        "força por metro quadrado. [p=0.3] {c}*Natalidade:* [p=0.2] nascimentos por mil habitantes. [p=0.4] {d}Sete "
        "nomes diferentes, [p=0.2] *uma divisão só.* [p=0.2] Uma coisa *por* outra."),

    # ================= BLOCO F: A TAXA SERVE PARA COMPARAR =================
    dict(id="16", block="comparar", text=
        "{t}Qual cidade é mais apertada: [p=0.2] a de um milhão de habitantes [p=0.2] ou a de duzentos mil? [p=0.4] "
        "{a}Parece a de um milhão. [p=0.3] Mas ela tem *quinhentos* quilômetros quadrados, [p=0.2] e a outra, "
        "*cinquenta.* [p=0.4] {b}Divida: [p=0.2] um milhão por quinhentos, [p=0.2] *dois mil* habitantes por "
        "quilômetro quadrado. [p=0.2] Duzentos mil por cinquenta, [p=0.2] *quatro mil.* [p=0.4] {c}A menor é a mais "
        "apertada. [p=0.3] {d}Só a *taxa* compara quantidades diferentes."),

    # ================= BLOCO G: VALORES DE REFERÊNCIA =================
    dict(id="17", block="referencia", text=
        "{t}E como saber se a sua resposta faz sentido? [p=0.4] {a}Use os *valores de referência:* [p=0.2] números "
        "típicos do mundo real. [p=0.4] {b}Carro na rodovia, [p=0.2] uns cem quilômetros por hora. [p=0.2] "
        "Rendimento de carro, [p=0.2] de dez a quinze quilômetros por litro. [p=0.4] {c}Se a sua conta deu um carro a *quinhentos quilômetros por "
        "hora,* [p=0.2] {d}nem precisa revisar a conta: [p=0.2] *alguma unidade foi trocada.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um pacote de *cinco quilos* de arroz custa *vinte e dois reais e cinquenta.* [p=0.3] "
        "{b}Um de *dois quilos* custa *nove reais e sessenta.* [p=0.3] Qual é mais barato por quilo? [p=0.4] {c}*Pause "
        "e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A pergunta é *reais por quilo:* [p=0.2] a barra manda dividir os reais pelos "
        "quilos. [p=0.4] {b}Vinte e dois e cinquenta dividido por cinco: [p=0.2] *quatro reais e cinquenta* o quilo. "
        "[p=0.4] {c}Nove e sessenta dividido por dois: [p=0.2] *quatro reais e oitenta* o quilo. [p=0.4] {d}O pacote "
        "de cinco quilos é o *mais barato* por quilo, [p=0.2] mesmo custando mais no caixa."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a barra da unidade é um sinal de dividir. [p=0.5] "
        "{b}Dois: [p=0.2] taxa: divida. [p=0.2] Numerador: multiplique. [p=0.2] Denominador: divida ao contrário. "
        "[p=0.5] {c}Três: [p=0.2] a taxa não muda com a quantidade."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *decorar três fórmulas diferentes* [p=0.2] "
        "para velocidade, densidade e vazão. [p=0.4] {b}Parece mais seguro, [p=0.2] porque cada assunto ganha a sua "
        "fórmula. [p=0.4] {c}Mas é o triplo de coisa para lembrar. [p=0.2] Leia a unidade: [p=0.2] ela é a fórmula."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] comparar embalagens pelo *preço total.* [p=0.4] {b}Parece certo, [p=0.2] porque nove e "
        "sessenta é bem menos que vinte e dois e cinquenta. [p=0.4] {c}Mas os pacotes têm tamanhos diferentes. "
        "[p=0.2] Compare o *preço por quilo.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] aceitar um resultado *absurdo* sem conferir. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "conta foi feita com cuidado. [p=0.4] {c}Mas um carro a quinhentos quilômetros por hora [p=0.2] denuncia uma "
        "unidade trocada. [p=0.2] Compare com os *valores de referência.*"),

    # ================= QUESTÃO 8 (EU FAÇO) =================
    dict(id="24", block="q8", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Um automóvel percorreu *quatrocentos e vinte quilômetros* [p=0.2] consumindo "
        "*trinta e cinco litros* de combustível. [p=0.2] O rendimento médio desse veículo foi de: [p=0.4] {qa}A: "
        "[p=0.2] oito quilômetros por litro. [p=0.3] {qb}B: [p=0.2] dez. [p=0.3] {qc}C: [p=0.2] doze. [p=0.3] {qd}D: "
        "[p=0.2] catorze. [p=0.3] {qe}E: [p=0.2] quinze quilômetros por litro. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="25", block="q8", text=
        "{t}Primeiro, a unidade ao lado de cada número: [p=0.2] quatrocentos e vinte *quilômetros,* [p=0.2] trinta e "
        "cinco *litros.* [p=0.4] {a}A pergunta é *quilômetros por litro.* [p=0.2] É a taxa: [p=0.2] divida. [p=0.4] "
        "{b}Quatrocentos e vinte dividido por trinta e cinco: [p=0.2] *doze quilômetros por litro.* [p=0.4] {c}Faz "
        "sentido? [p=0.2] Carro rende de dez a quinze. [p=0.2] Doze está dentro. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q8", text=
        "{t}E as outras? [p=0.3] {xa}A A, [p=0.2] oito, [p=0.2] está *abaixo* da faixa de referência: [p=0.2] já "
        "desconfie. [p=0.4] {a}Mas repare: [p=0.2] dez, catorze e quinze estão *dentro* da faixa. [p=0.2] A "
        "referência sozinha não basta. [p=0.4] {b}Atalho: [p=0.2] *multiplique de volta.* [p=0.2] Taxa vezes litros "
        "tem que dar os quilômetros. [p=0.4] {xb}Dez vezes trinta e cinco, [p=0.2] trezentos e cinquenta. [p=0.2] "
        "{xd}Catorze, [p=0.2] quatrocentos e noventa. [p=0.2] {xe}Quinze, [p=0.2] quinhentos e vinte e cinco. [p=0.4] "
        "{c}Só o doze devolve os quatrocentos e vinte."),
    dict(id="27", block="mais", text=
        "{t}E o mesmo rendimento responde as outras duas perguntas. [p=0.4] {a}Com *cinquenta litros,* [p=0.2] "
        "quantos quilômetros o carro faz? [p=0.4] {b}Agora a pergunta é o *numerador:* [p=0.2] multiplique. [p=0.2] "
        "Doze quilômetros por litro, [p=0.2] vezes cinquenta litros: [p=0.2] *seiscentos quilômetros.* [p=0.4] {c}O "
        "litro cancela, [p=0.2] e sobra quilômetro."),
    dict(id="28", block="mais", text=
        "{t}E a última é *sua.* [p=0.3] {a}Para fazer *trezentos quilômetros,* [p=0.2] quantos litros o carro precisa? "
        "[p=0.4] {b}*Pause e resolva.* [p=2.0]"),
    dict(id="29", block="mais", text=
        "{t}Conferindo. [p=0.2] A pergunta é o *denominador:* [p=0.2] divida ao contrário. [p=0.4] {a}Trezentos "
        "quilômetros [p=0.2] dividido por doze quilômetros por litro: [p=0.2] *vinte e cinco litros.* [p=0.4] {b}O "
        "quilômetro cancela, [p=0.2] e sobra litro. [p=0.4] {c}E de volta: [p=0.2] doze vezes vinte e cinco, "
        "[p=0.2] trezentos. [p=0.2] Bateu."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a barra da unidade é um sinal de dividir. "
        "[p=0.5] {b}Dois: [p=0.2] taxa: divida. [p=0.2] Numerador: multiplique. [p=0.2] Denominador: divida ao "
        "contrário. [p=0.5] {c}Três: [p=0.2] a taxa não muda com a quantidade."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Um trem faz *cento e oitenta quilômetros* [p=0.2] em *duas horas e trinta minutos.* [p=0.5] {b}Se você "
        "dividiu cento e oitenta por *dois vírgula trinta,* [p=0.2] *errou.* [p=0.5] {c}Próximo episódio: [p=0.2] "
        "velocidade média."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual taxa você usa no seu dia a dia? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
