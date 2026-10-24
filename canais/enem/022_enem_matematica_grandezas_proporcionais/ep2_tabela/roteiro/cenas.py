# Roteiro — Grandezas Proporcionais, Episódio 2 de 6: Reconhecer a proporcionalidade numa tabela (duas contas resolvem tudo)
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seção 08 (+ Questão 1 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa · {r1}…{r4} = linha da tabela (a coluna auxiliar nasce na fala)
# Analogia âncora: o DETETIVE DA TABELA tem DOIS testes: divide (não muda? direta) e multiplica (não muda? inversa).
#   Nenhum dos dois? Não há proporção, e nada de regra de três.
# Exemplos (nossos; nenhum usa os pares da Q1):
#   arroz: 1→5, 2→10, 3→15, 4→20 (÷ = 5 sempre → DIRETA, k = 5 R$/kg)
#   torneiras: 1→12 h, 2→6, 3→4, 4→3 (÷: 12, 3… muda; × = 12 sempre → INVERSA, k = 12 h de uma torneira sozinha)
#   estacionamento: 1 h→R$ 7, 2→9, 3→11 (÷: 7; 4,5; ≈3,67 · ×: 7; 18; 33 → NENHUMA)
#   "teste todas": (2; 6), (4; 12), (5; 20) → ÷: 3, 3, 4 → não é direta (as duas primeiras linhas enganam)
# Nós fazemos (conferido em Python): A (2; 30), (4; 15), (6; 10) → ÷ 15; 3,75; ≈1,67 · × 60 sempre → INVERSA, k = 60
#   B (2; 14), (3; 21), (7; 49) → ÷ 7 sempre → DIRETA, k = 7 (× 28; 63; 343)
#   C (1; 8), (2; 10), (4; 14) → ÷ 8; 5; 3,5 · × 8; 20; 56 → NENHUMA (falha nos dois testes)
# QUESTÃO 1 do material (texto idêntico na tela): × = 120 em todas as linhas → inversa, k = 120 → B.
#   Explicação do material: C = quociente da 1ª linha (40 ÷ 3 ≈ 13), o erro de testar uma linha só.
#   Explicações NOSSAS (o material só explica a C): A = achou o 120 mas chamou de direta (produto constante é inversa);
#   D = somou 3 + 40 = 43 (o k da inversa vem da multiplicação); E = desistiu depois do 1º teste.
# Frases-chave (meio e fim, idênticas, do usuário): 1. Divide: constante? Direta. 2. Multiplica: constante? Inversa.
#   3. Teste todas as linhas, nunca uma só.
# Atalhos (verde): "escreva a coluna auxiliar na margem: ela mostra a relação E o k" · "a constância é a prova".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Proporcional ou não? Reconheça na tabela com DUAS contas · Matemática ENEM, Grandezas Proporcionais, episódio 2"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como um detetive "
            "que está quase resolvendo o caso; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê "
            "ênfase forte às palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e "
            "tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está "
            "escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Tabela de valores [p=0.2] é o formato *mais comum* deste assunto no ENEM. [p=0.5] {b}E existe um procedimento "
        "*mecânico* [p=0.2] que resolve *todas* [p=0.2] em segundos."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai bater o olho numa tabela [p=0.2] e dizer se a relação é *direta,* "
        "[p=0.2] *inversa* [p=0.2] ou *nenhuma,* [p=0.4] {b}e ainda achar o *k.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio um. [p=0.3] {a}Na relação *direta,* [p=0.2] o que não muda é o "
        "*quociente,* [p=0.2] o resultado da divisão: [p=0.2] preço dividido por quilos dá sempre o preço do quilo, "
        "[p=0.2] o da etiqueta. [p=0.4] {b}Na *inversa,* [p=0.2] o que não muda é o *produto,* [p=0.2] o resultado da "
        "multiplicação: [p=0.2] velocidade vezes tempo dá sempre os mesmos duzentos e quarenta quilômetros. [p=0.4] "
        "{c}Esse número que não muda [p=0.2] é o *k.*"),

    # ================= A TABELA DO COTIDIANO =================
    dict(id="04", block="arroz", text=
        "{t}Olhe esta tabela do mercado. [p=0.3] {r1}Um quilo de arroz, [p=0.2] *cinco reais.* [p=0.3] {r2}Dois quilos, "
        "[p=0.2] dez. [p=0.3] {r3}Três quilos, [p=0.2] quinze. [p=0.3] {r4}Quatro quilos, [p=0.2] vinte. [p=0.4] {a}Uma "
        "*tabela de valores* é isso: [p=0.2] uma coluna para cada grandeza, [p=0.2] lado a lado. [p=0.4] {b}E cada linha é "
        "um *par ordenado:* [p=0.2] dois valores que andam juntos, [p=0.2] sempre na mesma ordem. [p=0.3] Dois quilos, "
        "[p=0.2] dez reais."),

    # ================= TESTE 1: DIVIDIR =================
    dict(id="05", block="teste1", text=
        "{t}Agora, vire *detetive.* [p=0.3] Ele tem *dois testes.* [p=0.4] {a}Teste um: [p=0.2] *dividir* a segunda coluna "
        "pela primeira, [p=0.2] linha por linha. [p=0.4] {r1}Cinco dividido por um, [p=0.2] cinco. [p=0.3] {r2}Dez por dois, "
        "[p=0.2] cinco. [p=0.3] {r3}Quinze por três, [p=0.2] cinco. [p=0.3] {r4}Vinte por quatro, [p=0.2] cinco. [p=0.4] "
        "{v}O quociente *não muda:* [p=0.2] a relação é *direta.* [p=0.4] {k}E esse cinco é o *k:* [p=0.2] cinco reais por "
        "quilo, [p=0.2] o preço da etiqueta."),

    # ================= TESTE 2: MULTIPLICAR =================
    dict(id="06", block="torneira", text=
        "{t}Agora, uma caixa-d'água. [p=0.3] {r1}Com *uma* torneira, [p=0.2] ela enche em doze horas. [p=0.3] {r2}Com duas, "
        "[p=0.2] seis. [p=0.3] {r3}Com três, [p=0.2] quatro. [p=0.3] {r4}Com quatro, [p=0.2] três. [p=0.4] {a}Teste um, "
        "dividir: [p=0.2] {d1}doze por um, [p=0.2] doze. [p=0.3] {d2}Seis por dois, [p=0.2] *três.* [p=0.4] {v}Mudou! "
        "[p=0.3] Não é direta. [p=0.4] {e}Muita gente para aqui. [p=0.2] O detetive, não."),
    dict(id="07", block="torneira", text=
        "{t}Teste dois: [p=0.2] *multiplicar* as duas colunas, [p=0.2] linha por linha. [p=0.4] {r1}Um vezes doze, "
        "[p=0.2] doze. [p=0.3] {r2}Dois vezes seis, [p=0.2] doze. [p=0.3] {r3}Três vezes quatro, [p=0.2] doze. [p=0.3] "
        "{r4}Quatro vezes três, [p=0.2] doze. [p=0.4] {v}O produto *não muda:* [p=0.2] a relação é *inversa.* [p=0.4] "
        "{k}E o k é doze: [p=0.2] as doze horas que *uma* torneira sozinha levaria."),

    # ================= NENHUMA DAS DUAS =================
    dict(id="08", block="nenhuma", text=
        "{t}E se nenhum dos dois testes der certo? [p=0.4] {a}Um estacionamento cobra: [p=0.2] {r1}uma hora, [p=0.2] *sete "
        "reais;* [p=0.2] {r2}duas horas, [p=0.2] nove; [p=0.2] {r3}três horas, [p=0.2] onze. [p=0.4] {b}Dividindo: [p=0.2] "
        "sete, [p=0.2] quatro e meio, [p=0.2] uns três vírgula sete. [p=0.2] Muda. [p=0.4] {c}Multiplicando: [p=0.2] sete, "
        "[p=0.2] dezoito, [p=0.2] trinta e três. [p=0.2] Também muda. [p=0.4] {v}Nenhum dos dois é constante: [p=0.2] *não "
        "há proporcionalidade.* [p=0.4] {x}E aí a regra de três está *proibida.*"),

    # ================= O HÁBITO: A COLUNA AUXILIAR =================
    dict(id="09", block="auxiliar", text=
        "{t}Agora, o hábito que economiza tempo. [p=0.4] {a}Viu uma tabela no enunciado? [p=0.2] Escreva uma *terceira "
        "coluna* na margem, [p=0.2] a *coluna auxiliar,* [p=0.2] com o quociente [p=0.2] ou o produto de cada linha. "
        "[p=0.4] {b}Ela responde duas perguntas de uma vez: [p=0.2] qual é a relação, [p=0.3] {c}e quanto vale o *k.* "
        "[p=0.4] {d}E o k costuma ser justamente o que a questão pede *em seguida.*"),

    # ================= TESTE TODAS AS LINHAS =================
    dict(id="10", block="todas", text=
        "{t}Mas quantas linhas você precisa testar? [p=0.4] {a}Veja esta tabela: [p=0.2] dois e seis, [p=0.2] quatro e "
        "doze, [p=0.2] cinco e vinte. [p=0.4] {r1}Seis por dois, [p=0.2] três. [p=0.3] {r2}Doze por quatro, [p=0.2] três. "
        "[p=0.3] Parece direta… [p=0.4] {r3}Vinte por cinco: [p=0.2] *quatro!* [p=0.4] {v}Uma linha sozinha *sempre* dá "
        "algum número. [p=0.3] O que prova a relação [p=0.2] é o número se *repetir* em todas. [p=0.4] {k}Por isso, [p=0.2] "
        "teste *todas* as linhas."),

    # ================= NÓS FAZEMOS =================
    dict(id="11", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Três tabelas. [p=0.3] {a}Tabela A: [p=0.2] dois e trinta, [p=0.2] quatro e quinze, [p=0.2] "
        "seis e dez. [p=0.4] {b}Tabela B: [p=0.2] dois e catorze, [p=0.2] três e vinte e um, [p=0.2] sete e quarenta e "
        "nove. [p=0.4] {c}Tabela C: [p=0.2] um e oito, [p=0.2] dois e dez, [p=0.2] quatro e catorze. [p=0.4] {d}Em cada "
        "uma, [p=0.2] os dois testes: [p=0.2] direta, [p=0.2] inversa [p=0.2] ou nenhuma? [p=0.3] *Pause o vídeo.* [p=2.0]"),
    dict(id="12", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Tabela A: [p=0.2] dividindo, [p=0.2] quinze, [p=0.2] três vírgula setenta e cinco… "
        "[p=0.2] muda. [p=0.3] {a2}Multiplicando: [p=0.2] sessenta, [p=0.2] sessenta, [p=0.2] sessenta. [p=0.3] *Inversa,* "
        "[p=0.2] com k igual a sessenta. [p=0.4] {b}Tabela B: [p=0.2] dividindo, [p=0.2] sete, [p=0.2] sete, [p=0.2] sete. "
        "[p=0.3] *Direta,* [p=0.2] com k igual a sete. [p=0.4] {c}Tabela C: [p=0.2] dividindo, [p=0.2] oito, [p=0.2] "
        "cinco… [p=0.2] muda. [p=0.3] {c2}Multiplicando, [p=0.2] oito, [p=0.2] vinte… [p=0.2] também muda. [p=0.3] "
        "*Nenhuma.* [p=0.2] Nada de regra de três."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="13", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] divide: [p=0.2] constante? [p=0.2] Direta. [p=0.5] "
        "{b}Dois: [p=0.2] multiplica: [p=0.2] constante? [p=0.2] Inversa. [p=0.5] {c}Três: [p=0.2] teste todas as linhas, "
        "[p=0.2] nunca uma só."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="14", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] testar *uma linha só* [p=0.2] e chamar aquele "
        "número de k. [p=0.4] {b}Parece certo, [p=0.2] porque a conta deu um número bonito. [p=0.4] {c}Mas uma linha "
        "sozinha sempre dá algum número. [p=0.3] Só a repetição em *todas* as linhas prova a relação."),
    dict(id="15", block="erros", text=
        "{a}Segundo: [p=0.2] *desistir* depois do primeiro teste. [p=0.4] {b}Parece certo, [p=0.2] porque a divisão não "
        "deu constante, [p=0.2] e dá vontade de concluir que não há relação. [p=0.4] {c}Mas falta o teste dois: [p=0.2] "
        "multiplique. [p=0.3] A relação pode ser *inversa.*"),
    dict(id="16", block="erros", text=
        "{a}Terceiro: [p=0.2] aplicar *regra de três* numa tabela sem proporcionalidade. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque os números crescem juntos. [p=0.4] {c}Mas a regra de três só vale com quociente ou produto "
        "constante. [p=0.3] Nenhum dos dois? [p=0.2] Ela está *proibida.*"),

    # ================= QUESTÃO 1 DO MATERIAL =================
    dict(id="17", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um estudo registrou os "
        "seguintes pares de valores para duas grandezas, [p=0.2] *x* e *y:* [p=0.3] três e quarenta; [p=0.2] cinco e vinte "
        "e quatro; [p=0.2] oito e quinze; [p=0.2] e doze e dez. [p=0.4] {b}Sobre essas grandezas, [p=0.2] é correto afirmar "
        "que: [p=0.4] {qa}A: [p=0.2] são diretamente proporcionais, [p=0.2] com k igual a cento e vinte. [p=0.3] {qb}B: "
        "[p=0.2] são inversamente proporcionais, [p=0.2] com k igual a cento e vinte. [p=0.3] {qc}C: [p=0.2] são "
        "diretamente proporcionais, [p=0.2] com k igual a treze. [p=0.3] {qd}D: [p=0.2] são inversamente proporcionais, "
        "[p=0.2] com k igual a quarenta e três. [p=0.3] {qe}E: [p=0.2] não guardam relação de proporcionalidade. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="18", block="q1", text=
        "{t}Vamos montar a coluna auxiliar. [p=0.3] {a}Teste um, [p=0.2] dividir *y* por *x:* [p=0.2] {d1}quarenta por três, "
        "[p=0.2] uns treze vírgula três. [p=0.3] {d2}Vinte e quatro por cinco, [p=0.2] quatro vírgula oito. [p=0.3] {b}Mudou: "
        "[p=0.2] não é direta. [p=0.4] {c}Teste dois, multiplicar: [p=0.2] {r1}três vezes quarenta, [p=0.2] cento e vinte. "
        "[p=0.3] {r2}Cinco vezes vinte e quatro, [p=0.2] cento e vinte. [p=0.3] {r3}Oito vezes quinze, [p=0.2] cento e vinte. "
        "[p=0.3] {r4}Doze vezes dez, [p=0.2] cento e vinte. [p=0.4] {v}Produto constante: [p=0.2] *inversa,* [p=0.2] com "
        "k igual a cento e vinte. [p=0.3] {ok}*Letra B!*"),
    dict(id="19", block="q1", text=
        "{t}E as outras? [p=0.3] {xc}A C é o erro clássico: [p=0.2] o treze é o quociente *só da primeira linha.* [p=0.4] "
        "{xa}A A achou o cento e vinte, [p=0.2] mas chamou de direta: [p=0.2] produto constante é *inversa.* [p=0.4] "
        "{xe}A E é de quem desistiu depois do primeiro teste. [p=0.4] {xd}E a D *somou* três mais quarenta: [p=0.2] o k "
        "da inversa vem da *multiplicação.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="20", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] divide: [p=0.2] constante? [p=0.2] Direta. [p=0.5] "
        "{b}Dois: [p=0.2] multiplica: [p=0.2] constante? [p=0.2] Inversa. [p=0.5] {c}Três: [p=0.2] teste todas as linhas, "
        "[p=0.2] nunca uma só."),

    # ================= PONTE E CTA =================
    dict(id="21", block="ponte", text=
        "{a}E quando, em vez de tabela, [p=0.2] a questão mostra um *gráfico?* [p=0.4] {b}Cada relação tem um desenho "
        "*inconfundível,* [p=0.3] {c}e existe uma reta que engana quase todo mundo. [p=0.4] {d}Próximo episódio."),
    dict(id="22", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha desistido depois do primeiro teste? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
