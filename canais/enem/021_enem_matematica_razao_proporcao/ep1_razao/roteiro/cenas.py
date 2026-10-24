# Roteiro — Razão, Proporção e Regra de Três, Episódio 1 de 6: Razão, a ordem dos termos e as razões em todo lugar
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seções 02 e 03 (+ Questões 1 e 9 da seção 12).
# Da seção 03, só o "passeio" das taxas: SEM conversão km/h ↔ m/s e SEM cálculo de escala (séries próprias).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   RAZÃO = comparar dividindo: quantas vezes uma coisa cabe na outra (suco: 1 copo de concentrado para 3 de água).
#   "O que vem DEPOIS da palavra 'para' vai EMBAIXO da fração."
#   TAXA = razão com unidade, como o R$/kg da etiqueta do mercado.
# Desvio consciente: o bloco b) do prompt usava 18 meninas e 12 meninos (meninos/total = 2/5), que é a própria Questão 1.
#   O bloco usa um ÔNIBUS com 21 sentados e 7 em pé (em pé para sentados = 1/3; em pé para o total = 7/28 = 1/4).
#   O bloco f) usa 150 km a 10 km/L e R$ 6 o litro (15 L → R$ 90), para não entregar a Questão 9.
# Nós fazemos: 20 mulheres e 5 homens → homens para mulheres = 5/20 = 1/4; mulheres para o total = 20/25 = 4/5.
# QUESTÃO 1 do material (texto idêntico na tela): 12/30 = 2/5 → C. Explicações do material: A = meninos para meninas;
#   D = meninas para o total; B e E = as mesmas razões invertidas.
# QUESTÃO 9 do material: 480 ÷ 12 = 40 L; 40 · 5,80 = R$ 232 → B. E (R$ 2 784) = 480 · 5,80, pulou a 1ª etapa (material).
#   Explicações NOSSAS (o material só explica a E): A (R$ 82,80) ≈ 480 ÷ 5,80, dividiu os km pelo preço;
#   C (R$ 240) = 40 · 6, arredondou o preço do litro para R$ 6; D (R$ 696) não sai de um caminho coerente e o bom senso
#   elimina (daria R$ 1,45 por km, quando cada km custa uns 50 centavos: 5,80 ÷ 12 ≈ 0,48).
# Frases-chave (meio e fim, idênticas): 1. Razão é comparar dividindo. 2. O que vem depois de "para" vai embaixo.
#   3. Taxa é razão com unidade.
# Atalhos (verde): "sublinhe o que vem depois do 'para'" · "antes de montar, pergunte: comparado com QUEM?" ·
#   "taxa: leia o 'por' como 'dividido por'" · "siga as unidades: km ÷ km/L = litros; litros × R$/L = reais".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Razão: a ordem que derruba no ENEM (o que vem depois do “para” vai embaixo) · Matemática ENEM, episódio 1"

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
        "{a}Se você pudesse levar *um único assunto* de Matemática para o ENEM, [p=0.2] seria este. [p=0.5] {b}Velocidade, "
        "[p=0.2] escala, [p=0.2] densidade, [p=0.2] câmbio, [p=0.2] consumo: [p=0.3] {c}tudo é *razão.* [p=0.5] {d}E a "
        "*regra de três* resolve mais questões do que qualquer outra ferramenta."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai montar qualquer razão *na ordem certa,* [p=0.4] {b}e reconhecer as razões "
        "*escondidas* nos enunciados."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos, [p=0.2] da série de Frações. [p=0.3] {a}*Simplificar* uma fração é dividir em cima "
        "e embaixo pelo mesmo número: [p=0.2] seis oitavos, [p=0.2] dividindo por dois, [p=0.2] vira *três quartos.* [p=0.4] "
        "{b}E três quartos pode ser escrito de outros jeitos: [p=0.2] *zero vírgula setenta e cinco,* [p=0.2] ou *setenta e "
        "cinco por cento.* [p=0.3] É o mesmo número."),

    # ================= BLOCO A: O QUE É RAZÃO =================
    dict(id="04", block="suco", text=
        "{t}Olhe a receita na caixa de suco: [p=0.2] *um copo de concentrado para três copos de água.* [p=0.4] {a}O que essa "
        "frase está fazendo? [p=0.4] {b}Está *comparando* duas quantidades. [p=0.3] {c}E compara dividindo: [p=0.2] um "
        "dividido por três, [p=0.2] *um terço.* [p=0.4] {d}Isso é uma *razão:* [p=0.2] uma comparação por divisão. [p=0.3] "
        "{e}Ela diz quantas vezes uma coisa cabe na outra: [p=0.2] o concentrado cabe *três vezes* na água."),
    dict(id="05", block="definicao", text=
        "{t}No geral, [p=0.2] a razão entre *a* e *b* [p=0.2] é *a dividido por b.* [p=0.4] {a}Com uma condição: [p=0.2] o "
        "*b* não pode ser zero, [p=0.2] porque não existe divisão por zero. [p=0.4] {b}O número de cima tem nome: "
        "*antecedente,* [p=0.2] porque vem antes. [p=0.3] {c}O de baixo é o *consequente,* [p=0.2] o que vem depois."),

    # ================= BLOCO B: A ORDEM IMPORTA =================
    dict(id="06", block="ordem", text=
        "{t}E agora, a pergunta que vale ponto: [p=0.2] a ordem importa? [p=0.5] {a}Concentrado *para* água: [p=0.2] *um "
        "terço.* [p=0.4] {b}Água *para* concentrado: [p=0.2] três sobre um, [p=0.2] *três.* [p=0.4] {c}Números diferentes! "
        "[p=0.3] {d}A regra é esta: [p=0.2] *o que vem depois da palavra para vai embaixo.* [p=0.4] {e}E a frase *razão entre "
        "a e b* [p=0.2] segue a mesma ordem: [p=0.2] o primeiro em cima, [p=0.2] o segundo embaixo."),
    dict(id="07", block="onibus", text=
        "{t}Vamos treinar num ônibus. [p=0.3] {a}Vinte e uma pessoas estão *sentadas,* [p=0.2] {b}e sete estão *em pé.* "
        "[p=0.4] {c}Qual é a razão das pessoas em pé *para* as sentadas? [p=0.4] {d}Depois do *para* vêm as sentadas: "
        "[p=0.2] elas vão embaixo. [p=0.3] Sete sobre vinte e um. [p=0.4] {e}Simplificando por sete: [p=0.2] *um terço.* "
        "[p=0.3] Para cada pessoa em pé, [p=0.2] três sentadas."),
    dict(id="08", block="onibus", text=
        "{t}Agora mudo uma palavra: [p=0.2] em pé *para o total.* [p=0.4] {a}O total é todo mundo: [p=0.2] vinte e um mais "
        "sete, [p=0.2] *vinte e oito.* [p=0.4] {b}Sete sobre vinte e oito: [p=0.2] *um quarto.* [p=0.4] {c}Mesmas pessoas, "
        "[p=0.2] resposta diferente. [p=0.3] {d}Por isso, um atalho: [p=0.2] antes de montar, *sublinhe* o que vem depois "
        "do *para* [p=0.2] e pergunte: [p=0.2] comparado *com quem?*"),

    # ================= BLOCO C: AS QUATRO FORMAS =================
    dict(id="09", block="formas", text=
        "{t}Uma razão pode aparecer na prova de *quatro jeitos.* [p=0.4] {a}Como fração: [p=0.2] três quartos. [p=0.3] "
        "{b}Como decimal: [p=0.2] zero vírgula setenta e cinco. [p=0.3] {c}Como porcentagem: [p=0.2] setenta e cinco por "
        "cento. [p=0.3] {d}E com dois-pontos: [p=0.2] três, [p=0.2] dois-pontos, [p=0.2] quatro, [p=0.2] que se lê *três "
        "para quatro.* [p=0.4] {e}As quatro dizem *a mesma coisa.*"),

    # ================= BLOCO D: NÚMERO PURO × TAXA =================
    dict(id="10", block="taxa", text=
        "{t}Repare numa diferença. [p=0.3] {a}Pessoas em pé para pessoas sentadas: [p=0.2] as duas contam *pessoas.* "
        "[p=0.3] {b}A unidade some, [p=0.2] e sobra um *número puro,* [p=0.2] um número sem unidade nenhuma. [p=0.5] {c}Mas "
        "e quando as coisas são de espécies diferentes? [p=0.3] {d}Cem metros em vinte segundos: [p=0.2] metros divididos "
        "por segundos. [p=0.3] {e}Dá *cinco metros por segundo.* [p=0.3] Aí a razão carrega unidade, [p=0.2] e ganha outro "
        "nome: [p=0.2] *taxa.*"),
    dict(id="11", block="taxa", text=
        "{t}Você vê taxas todo dia. [p=0.3] {a}A etiqueta do mercado: [p=0.2] *trinta reais por dois quilos* de carne. "
        "[p=0.4] {b}Trinta dividido por dois: [p=0.2] *quinze reais por quilo.* [p=0.4] {c}Esse é o *valor unitário:* "
        "[p=0.2] quanto custa *uma* unidade. [p=0.4] {d}Atalho: [p=0.2] numa taxa, [p=0.2] leia o *por* como *dividido por.* "
        "[p=0.3] Reais *por* quilo: [p=0.2] reais divididos por quilos."),

    # ================= BLOCO E: O PASSEIO DAS TAXAS =================
    dict(id="12", block="passeio", text=
        "{t}Agora, um passeio rápido. [p=0.3] Veja quantas razões a prova usa. [p=0.4] {a}*Velocidade:* [p=0.2] distância "
        "dividida por tempo. [p=0.3] {b}*Densidade:* [p=0.2] massa dividida por volume. [p=0.3] {c}*Escala* de um mapa: "
        "[p=0.2] o tamanho no desenho dividido pelo tamanho real. [p=0.3] {d}*Densidade demográfica:* [p=0.2] habitantes "
        "divididos pela área."),
    dict(id="13", block="passeio", text=
        "{a}*Rendimento* do carro: [p=0.2] quilômetros divididos por litros, [p=0.2] o *quilômetro por litro* do painel. "
        "[p=0.3] {b}*Vazão* de uma torneira: [p=0.2] litros divididos por segundos. [p=0.3] {c}E o *custo unitário:* [p=0.2] "
        "o preço dividido pela quantidade. [p=0.4] {d}Todas têm a mesma cara: [p=0.2] *alguma coisa dividida por outra.* "
        "[p=0.4] {e}Converter essas unidades [p=0.2] e calcular escalas [p=0.2] ganham séries próprias aqui no canal."),

    # ================= BLOCO F: RAZÕES ENCADEADAS =================
    dict(id="14", block="encadeada", text=
        "{t}E às vezes uma razão só não basta. [p=0.3] {a}Um carro faz *dez quilômetros por litro.* [p=0.2] {b}A gasolina "
        "custa *seis reais o litro.* [p=0.3] {c}Quanto custa uma viagem de *cento e cinquenta quilômetros?* [p=0.5] {d}Primeiro, "
        "[p=0.2] quantos litros: [p=0.2] cento e cinquenta dividido por dez, [p=0.2] *quinze litros.* [p=0.4] {e}Depois, "
        "[p=0.2] quanto custam: [p=0.2] quinze vezes seis, [p=0.2] *noventa reais.*"),
    dict(id="15", block="encadeada", text=
        "{t}Uma razão levou à outra: [p=0.2] quilômetros viraram litros, [p=0.2] e litros viraram reais. [p=0.4] {a}Atalho: "
        "[p=0.2] *siga as unidades.* [p=0.3] {b}Quilômetros divididos por quilômetros por litro [p=0.2] dão litros. [p=0.3] "
        "{c}Litros vezes reais por litro [p=0.2] dão reais. [p=0.4] {d}Se a unidade final não for a que a pergunta pede, "
        "[p=0.2] falta uma etapa."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Numa sala há *vinte mulheres* e *cinco homens.* [p=0.4] {b}Escreva a razão dos homens *para* "
        "as mulheres. [p=0.3] {c}E a razão das mulheres *para o total.* [p=0.4] {d}*Pause o vídeo e escreva.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Homens para mulheres: [p=0.2] depois do *para* vêm as mulheres, [p=0.2] embaixo. "
        "[p=0.2] Cinco sobre vinte: [p=0.2] *um quarto.* [p=0.4] {b}Mulheres para o total: [p=0.2] o total é vinte e cinco. "
        "[p=0.3] Vinte sobre vinte e cinco, [p=0.2] simplificando por cinco: [p=0.2] *quatro quintos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] razão é comparar dividindo. [p=0.5] {b}Dois: [p=0.2] o que "
        "vem depois de *para* [p=0.2] vai embaixo. [p=0.5] {c}Três: [p=0.2] taxa é razão com unidade."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *inverter a razão.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque os mesmos dois números estão ali, [p=0.2] e a gente escreve na ordem em que lê. [p=0.4] {c}Mas a "
        "ordem muda o valor: [p=0.2] o que vem depois do *para* [p=0.2] vai embaixo."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] usar *o outro grupo* quando o enunciado pede *o total.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "o outro grupo é o número que está escrito. [p=0.4] {c}Mas o total quase nunca está escrito: [p=0.2] você soma os "
        "grupos, [p=0.2] e só depois divide."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] numa razão em duas etapas, [p=0.2] *pular a primeira:* [p=0.2] multiplicar os quilômetros "
        "direto pelo preço do litro. [p=0.4] {b}Parece certo, [p=0.2] porque são os dois números grandes do enunciado. "
        "[p=0.4] {c}Mas quilômetros vezes reais por litro [p=0.2] não dá reais. [p=0.3] Primeiro os litros, [p=0.2] depois "
        "o preço."),

    # ================= QUESTÃO 1 DO MATERIAL =================
    dict(id="22", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Em uma turma há *dezoito "
        "meninas* e *doze meninos.* [p=0.3] {b}A razão entre o número de meninos [p=0.2] e o número *total* de alunos da "
        "turma é: [p=0.4] {qa}A: [p=0.2] dois terços. [p=0.3] {qb}B: [p=0.2] três meios. [p=0.3] {qc}C: [p=0.2] dois quintos. "
        "[p=0.3] {qd}D: [p=0.2] três quintos. [p=0.3] {qe}E: [p=0.2] cinco meios. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q1", text=
        "{t}Vamos resolver. [p=0.3] {a}A razão é *entre meninos e o total:* [p=0.2] meninos em cima, [p=0.2] total embaixo. "
        "[p=0.4] {b}O total não está escrito: [p=0.2] dezoito mais doze, [p=0.2] *trinta.* [p=0.4] {c}Doze sobre trinta. "
        "[p=0.3] {d}Simplificando por seis: [p=0.2] *dois quintos.* [p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q1", text=
        "{t}E as outras? [p=0.3] Todas erram no número de baixo. [p=0.4] {xa}A A é meninos para *meninas:* [p=0.2] usou o "
        "outro grupo. [p=0.4] {xd}A D é meninas para o total. [p=0.4] {xb}A B [p=0.2] {xe}e a E [p=0.2] são essas mesmas "
        "razões, [p=0.2] *de cabeça para baixo.*"),

    # ================= QUESTÃO 9 DO MATERIAL =================
    dict(id="25", block="q9", text=
        "{t}Mais uma do material. [p=0.3] {a}Um automóvel percorre, em média, [p=0.2] *doze quilômetros com um litro* de "
        "combustível, [p=0.2] vendido a *cinco reais e oitenta centavos* o litro. [p=0.4] {b}O custo aproximado do "
        "combustível para uma viagem de *quatrocentos e oitenta quilômetros* será de: [p=0.4] {qa}A: [p=0.2] oitenta e dois "
        "reais e oitenta centavos. [p=0.3] {qb}B: [p=0.2] duzentos e trinta e dois reais. [p=0.3] {qc}C: [p=0.2] duzentos e "
        "quarenta reais. [p=0.3] {qd}D: [p=0.2] seiscentos e noventa e seis reais. [p=0.3] {qe}E: [p=0.2] dois mil, setecentos "
        "e oitenta e quatro reais. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q9", text=
        "{t}Duas razões em sequência. [p=0.3] {a}Primeiro, os litros: [p=0.2] quatrocentos e oitenta dividido por doze, "
        "[p=0.2] *quarenta litros.* [p=0.4] {b}Depois, o preço: [p=0.2] quarenta vezes cinco e oitenta, [p=0.2] *duzentos e "
        "trinta e dois reais.* [p=0.3] {ok}*Letra B!* [p=0.4] {c}E o bom senso confirma: [p=0.2] cada quilômetro custa uns "
        "*cinquenta centavos,* [p=0.2] e quinhentos quilômetros dariam uns *duzentos e cinquenta reais.* [p=0.3] Duzentos e "
        "trinta e dois está ali perto."),
    dict(id="27", block="q9", text=
        "{t}E as outras? [p=0.3] {xe}A E é o erro clássico: [p=0.2] multiplicou os quilômetros direto pelo preço, [p=0.2] "
        "pulando os litros. [p=0.3] Quase três mil reais de gasolina? [p=0.2] Absurdo. [p=0.4] {xa}A A dividiu os "
        "quilômetros pelo preço. [p=0.4] {xc}A C arredondou o litro para seis reais. [p=0.4] {xd}E a D passa de um real "
        "por quilômetro: [p=0.2] o bom senso elimina."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] razão é comparar dividindo. [p=0.5] {b}Dois: [p=0.2] "
        "o que vem depois de *para* [p=0.2] vai embaixo. [p=0.5] {c}Três: [p=0.2] taxa é razão com unidade."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}E quando duas razões são *iguais?* [p=0.4] {b}Isso se chama *proporção,* [p=0.3] {c}e uma única propriedade "
        "dela [p=0.2] faz toda a regra de três funcionar. [p=0.4] {d}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha invertido uma razão na prova? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
