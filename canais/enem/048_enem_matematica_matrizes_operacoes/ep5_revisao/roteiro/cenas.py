# Roteiro — Matrizes e Operações, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/33-matrizes-operacoes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (dados exatos do prompt). Determinantes e A · X = B: só a ponte.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 O ASSENTO DO CINEMA (fileira antes da poltrona) · a tabela de mão dupla como ESPELHO · linha = o que o time FEZ,
#       coluna = o que SOFREU (ícone: poltrona de cinema) ·
#   ep2 AS FOLHAS TRANSPARENTES da soma · O AUMENTO GERAL do número vezes matriz (ícone: folhas transparentes) ·
#   ep3 O CAIXA DO SUPERMERCADO (linha vezes coluna) · A REGRA DO DOMINÓ das ordens (ícone: cupom de supermercado) ·
#   ep4 MEIA E SAPATO (a ordem importa) · a identidade como o NÚMERO 1 · a inversa como CHAVE DO CADEADO (ícone: cadeado).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): ler o endereço · multiplicar com sentido · decidir se a conta existe · imagens e
#   códigos. O que mais rende: saber o que cada elemento do produto representa (c_ij = quanto a filial i gasta no j).
# Onde aparece (seção 10): tecnologia (pixels) · economia (quantidade × preço) · nutrição (porções × nutrientes) ·
#   Geografia (distâncias, redes; A² conta conexões com uma escala) · sistemas A · X = B (próxima série).
# Estratégia (seção 09): 4 hábitos — rotular linhas e colunas · conferir as ordens · calcular só o elemento pedido ·
#   conferir a inversa multiplicando.
# V/F (os 9 erros da seção 11, NA ORDEM do material). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível,
#   três frases aparecem na versão CERTA (verdadeiras: 3, 6 e 8); as outras seis são o erro (falsas). Números NOSSOS
#   (fora das Q1–Q9 e dos exemplos dos eps. 1 a 4; conferidos em trabalho/conferir_questoes.py):
#   1 F a_23 é linha 3, coluna 2 · 2 F (1 0 / 2 1) · (3 1 / 1 2) casa a casa = (3 0 / 2 2) (certo: (3 1 / 7 4)) ·
#   3 V (2 × 3) · (2 × 3) NÃO existe · 4 F AB = BA sempre (A = (1 1 / 0 1), B = (1 0 / 1 1): AB = (2 1 / 1 1),
#   BA = (1 1 / 1 2)) · 5 F AB = 0 obriga um fator nulo ((1 2 / 2 4) · (2 −2 / −1 1) = 0) ·
#   6 V a inversa de (4 1 / 3 1) é (1 −1 / −3 4) (ad − bc = 1; conferida multiplicando) · 7 F a transposta de uma
#   2 × 3 é 2 × 3 (é 3 × 2) · 8 V na tabela de jogos, a coluna conta os gols SOFRIDOS · 9 F 3 · (1 2 / 0 4) = (3 6 / 0 4)
#   (certo: (3 6 / 0 12)).
# QUESTÕES INÉDITAS (dados, alternativas e motivos das erradas do PROMPT; conferidas em trabalho/conferir_questoes.py):
#   Q1 vendas V = (12 8 15 / 10 14 6 / 7 11 13), total do mês 2 = coluna 2: 8 + 14 + 11 = 33 → C.
#      A 14 (só v_22) · B 30 (soma a linha 2) · D 35 (soma a linha 1) · E 96 (a tabela inteira).
#   Q2 2X + A = B: X = (B − A) ÷ 2 = (2 1 / 1 4), soma 8 → B. A 4,5 (B ÷ 2 − A) · C 9 (B − 2A) · D 15 ((B + A) ÷ 2) ·
#      E 16 (esquece de dividir por 2).
#   Q3 Q · N: proteína da refeição 2 = linha 2 de Q × coluna 1 de N = 1 · 3 + 3 · 7 = 24 → D. A 10 (soma as proteínas
#      sem as porções) · B 13 (refeição 1) · C 16 (troca as porções: 1 · 7 + 3 · 3) · E 73 (coluna dos carboidratos).
#   Q4 A (3 × 2), B (2 × 4), C (3 × 4): A · B é 3 × 4 e soma com C → C. A B · A (4 ≠ 3) · B A + B (ordens diferentes) ·
#      D C · A (4 ≠ 3) · E A · C (2 ≠ 3).
#   Q5 chave A = (2 1 / 5 3), E = (7 / 18): ad − bc = 1, A⁻¹ = (3 −1 / −5 2), M = (3 / 1); conferência 2·3 + 1 = 7 e
#      5·3 + 3·1 = 18 → B. A inverte a ordem (1 e 3) · C troca os sinais da diagonal principal (−3 e −1) · D só troca a
#      diagonal (39 e 71) · E multiplica de novo por A (32 e 89).
# Gabaritos: C, B, D, C, B.
# Atalhos (verde): os 4 hábitos (cenas 08 e 09) · "rotule antes de somar" na Q1 · "isole X como num número" na Q2 ·
#   "calcule só a casa pedida" na Q3 · "escreva as ordens e confira o meio" na Q4 · "confira multiplicando" na Q5.
# Checklist (seção 13) → episódio (como o prompt pede): endereço, tipos, tabelas → ep1 · soma, número e igualdade → ep2 ·
#   produto e A² → ep3 · propriedades e inversa → ep4.
# Meta (prompt e material): 25 questões, 18 acertos, com pelo menos oito de leitura de tabela e cinco de produto em
#   contexto.
# Ponte (do usuário): Determinantes e sistemas lineares.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de matrizes: tabelas, produto e código secreto · Matemática ENEM, Matrizes ep. 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}No ENEM, [p=0.2] a matriz quase nunca vem com esse nome. [p=0.4] {b}Ela vem como tabela de jogos, [p=0.2] "
        "de distâncias, [p=0.2] de compras [p=0.2] ou como foto digital. [p=0.4] {c}Hoje você treina a *reconhecer o "
        "disfarce.* [p=0.5] {d}São nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Ler o endereço:* [p=0.2] o que significa cada casa, [p=0.2] a soma de uma "
        "linha [p=0.2] e a de uma coluna. [p=0.3] {b}*Multiplicar com sentido:* [p=0.2] quantidade vezes preço. [p=0.3] "
        "{c}*Decidir se a conta existe.* [p=0.3] {d}E *imagens e códigos:* [p=0.2] a foto de pixels [p=0.2] e a "
        "mensagem secreta."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] {a}Saber o que *cada elemento do produto* representa. [p=0.4] {b}Se a linha i "
        "é o que a filial i compra, [p=0.2] e a coluna j são os preços do fornecedor j, [p=0.3] então o elemento c i j "
        "[p=0.2] é *quanto a filial i gasta no fornecedor j.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] em a dois três, [p=0.2] *qual número é a linha?* [p=1.2] "
        "{a}Um: [p=0.2] o *assento do cinema.* [p=0.2] Primeiro a fileira, [p=0.2] depois a poltrona: [p=0.2] o dois "
        "é a *linha.* [p=0.2] A tabela de mão dupla é um *espelho,* [p=0.2] e no campeonato a linha é o que o time "
        "*fez;* [p=0.2] a coluna, o que *sofreu.* [p=0.4] {b}Dois: [p=0.2] as *folhas transparentes.* [p=0.2] Na soma, "
        "cada casa conversa com a de baixo. [p=0.2] E número vezes matriz é um *aumento geral:* [p=0.2] atinge todo "
        "mundo."),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *caixa do supermercado.* [p=0.2] Linha vezes coluna: [p=0.2] cada quantidade encontra o seu "
        "preço, [p=0.2] e o caixa soma tudo. [p=0.2] E a *regra do dominó:* [p=0.2] os números de dentro precisam "
        "encaixar. [p=0.4] {b}Quatro: [p=0.2] *meia e sapato,* [p=0.2] a ordem importa. [p=0.2] A identidade é *o número "
        "um* das matrizes, [p=0.2] e a inversa é a *chave do cadeado.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E nas outras áreas? [p=0.4] {a}Na *tecnologia,* [p=0.2] cada pixel de uma foto é um elemento. [p=0.3] "
        "{b}Na *economia,* [p=0.2] quantidade vezes preço é produto de matrizes. [p=0.3] {c}Na *nutrição,* [p=0.2] "
        "porções vezes nutrientes dão o total de cada nutriente em cada refeição."),
    dict(id="07", block="onde", text=
        "{d}Na *Geografia,* [p=0.2] as tabelas de distância entre cidades [p=0.2] e as redes de transporte. [p=0.3] "
        "{e}E os *sistemas lineares,* [p=0.2] na forma *A vezes X igual a B:* [p=0.2] esse é o assunto da próxima "
        "série."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *antes de calcular, rotule.* [p=0.2] "
        "Escreva ao lado o que é linha [p=0.2] e o que é coluna. [p=0.2] Boa parte dos erros é de *leitura,* [p=0.2] não "
        "de conta. [p=0.4] {b}Dois: [p=0.2] *confira as ordens antes de multiplicar.* [p=0.2] Escreva dois por três, "
        "vezes três por dois, [p=0.2] e veja se os números de dentro batem."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *calcule só o elemento pedido.* [p=0.2] Se a pergunta é uma casa, [p=0.2] não monte a matriz "
        "inteira. [p=0.4] {d}Quatro: [p=0.2] *confira a inversa multiplicando.* [p=0.2] O produto com a original tem de "
        "dar a identidade."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] o elemento *a dois três* [p=0.2] fica na *linha três, coluna dois.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque os dois números estão ali, [p=0.2] e a ordem parece detalhe. [p=0.3] "
        "{g}Mas, como no cinema, [p=0.2] *primeiro a fileira:* [p=0.2] linha dois, coluna três."),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] para multiplicar *um, zero; dois, um* [p=0.2] por *três, um; um, dois,* [p=0.2] basta "
        "multiplicar casa com casa. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a soma é mesmo casa "
        "a casa. [p=0.3] {g}Mas o produto é *linha por coluna:* [p=0.2] o resultado é *três, um; sete, quatro.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] uma matriz dois por três, [p=0.2] vezes outra dois por três, [p=0.2] *não existe.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque as duas são do mesmo tamanho. [p=0.3] {g}Mas "
        "o dominó não encaixa: [p=0.2] as *colunas da primeira,* três, [p=0.2] têm de ser iguais às *linhas da "
        "segunda,* dois."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] com matrizes, [p=0.2] *A vezes B é sempre igual a B vezes A.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque com números a ordem não importa. [p=0.3] {g}Mas é meia e sapato: "
        "[p=0.2] com *um, um; zero, um* [p=0.2] e *um, zero; um, um,* [p=0.2] uma ordem dá *dois, um; um, um,* [p=0.2] a "
        "outra dá *um, um; um, dois.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] se *A vezes B dá a matriz nula,* [p=0.2] então A ou B tem de ser nula. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque, com números, um produto zero obriga um fator zero. [p=0.3] {g}Mas "
        "*um, dois; dois, quatro* [p=0.2] vezes *dois, menos dois; menos um, um* [p=0.2] dá *tudo zero,* [p=0.2] e "
        "nenhuma das duas é nula."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] a inversa de *quatro, um; três, um* [p=0.2] é *um, menos um; menos três, quatro.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque não é só trocar a diagonal. [p=0.3] {g}E não "
        "é mesmo: [p=0.2] troca a diagonal, [p=0.2] *muda o sinal da outra* [p=0.2] e divide por a d menos b c, que aqui "
        "dá um. [p=0.2] Multiplicando, *sai a identidade.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] a transposta de uma matriz *dois por três* [p=0.2] também é dois por três. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque os números são os mesmos. [p=0.3] {g}Mas as *linhas "
        "viram colunas:* [p=0.2] a transposta é *três por dois.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] numa tabela de jogos em que a i j são os gols do time i contra o time j, [p=0.2] a *coluna* "
        "conta os gols *sofridos.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade "
        "de somar a coluna como gols marcados. [p=0.3] {g}Mas a linha é o que o time *fez;* [p=0.2] a coluna, o que "
        "fizeram *contra ele.* [p=0.2] Sempre releia a definição."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] *três vezes* a matriz *um, dois; zero, quatro* [p=0.2] dá *três, seis; zero, quatro.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o três parece ficar só na primeira linha. "
        "[p=0.3] {g}Mas é um *aumento geral:* [p=0.2] atinge todas as casas. [p=0.2] *Três, seis; zero, doze.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *rotule linha e coluna,* [p=0.2] *escreva as ordens* [p=0.2] e "
        "*confira no fim.*"),

    # ================= QUESTÃO 1: LEITURA DE TABELA =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}A matriz V mostra as vendas de três vendedores em três meses: [p=0.2] o elemento v i j "
        "é o número de unidades vendidas pelo *vendedor i* no *mês j.* [p=0.3] {b}Qual foi o total vendido no *mês "
        "dois* pelos três vendedores? [p=0.4] {la}A, [p=0.2] catorze. [p=0.2] {lb}B, [p=0.2] trinta. [p=0.2] {lc}C, "
        "[p=0.2] trinta e três. [p=0.2] {ld}D, [p=0.2] trinta e cinco. [p=0.2] {le}E, [p=0.2] noventa e seis. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Rotule primeiro: [p=0.2] *linha é o vendedor, coluna é o mês.* [p=0.3] {a}O mês dois é a *coluna dois:* "
        "[p=0.2] oito, mais catorze, mais onze, [p=0.2] *trinta e três.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A pegou só "
        "a casa dois dois. [p=0.2] {xb}A B somou a *linha* dois, [p=0.2] {xd}a D somou a linha um, [p=0.2] {xe}e a E "
        "somou a *tabela inteira.*"),

    # ================= QUESTÃO 2: EQUAÇÃO DE MATRIZES =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Considere a equação *dois X mais A igual a B,* [p=0.2] com A igual a *um, quatro; "
        "dois, zero* [p=0.2] e B igual a *cinco, seis; quatro, oito.* [p=0.3] {b}A soma dos elementos de X é: [p=0.4] "
        "{la}A, [p=0.2] quatro vírgula cinco. [p=0.2] {lb}B, [p=0.2] oito. [p=0.2] {lc}C, [p=0.2] nove. [p=0.2] {ld}D, "
        "[p=0.2] quinze. [p=0.2] {le}E, [p=0.2] dezesseis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Isole o X como se fosse um número: [p=0.2] *X é B menos A, dividido por dois.* [p=0.3] {a}B menos A, casa a "
        "casa: [p=0.2] quatro, dois; dois, oito. [p=0.2] Dividindo por dois: [p=0.2] *dois, um; um, quatro.* [p=0.2] "
        "Somando, *oito.* [p=0.2] {ok}*Letra B!* [p=0.4] {xe}A E esqueceu de *dividir por dois.* [p=0.2] {xd}A D fez B "
        "*mais* A. [p=0.2] {xc}A C fez B menos *duas vezes* A, [p=0.2] {xa}e a A dividiu só o B."),

    # ================= QUESTÃO 3: PRODUTO EM CONTEXTO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}A matriz Q dá as *porções* de arroz e de feijão nas refeições um e dois. [p=0.2] A "
        "matriz N dá, *por porção,* os gramas de proteína e de carboidrato de cada alimento. [p=0.3] {b}Quantos gramas de "
        "*proteína* tem a *refeição dois?* [p=0.4] {la}A, [p=0.2] dez. [p=0.2] {lb}B, [p=0.2] treze. [p=0.2] {lc}C, "
        "[p=0.2] dezesseis. [p=0.2] {ld}D, [p=0.2] vinte e quatro. [p=0.2] {le}E, [p=0.2] setenta e três. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}É o caixa do supermercado. [p=0.2] Calcule *só a casa pedida:* [p=0.2] a *linha dois* de Q, [p=0.2] vezes a "
        "*coluna um* de N. [p=0.3] {a}Uma porção de arroz vezes três, [p=0.2] mais três porções de feijão vezes sete: "
        "[p=0.2] *vinte e quatro gramas.* [p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A somou as proteínas *sem as porções.* "
        "[p=0.2] {xb}A B calculou a *refeição um.* [p=0.2] {xc}A C trocou as porções entre os alimentos, [p=0.2] {xe}e a "
        "E usou a coluna dos *carboidratos.*"),

    # ================= QUESTÃO 4: QUANDO O PRODUTO EXISTE =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}A é uma matriz *três por dois,* [p=0.2] B é *dois por quatro* [p=0.2] e C é "
        "*três por quatro.* [p=0.3] {b}Qual é a *única* operação possível? [p=0.4] {la}A, [p=0.2] B vezes A. [p=0.2] "
        "{lb}B, [p=0.2] A mais B. [p=0.2] {lc}C, [p=0.2] A vezes B, mais C. [p=0.2] {ld}D, [p=0.2] C vezes A. [p=0.2] "
        "{le}E, [p=0.2] A vezes C. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Escreva as ordens e confira o dominó. [p=0.3] {a}A vezes B: [p=0.2] três por *dois,* vezes *dois* por "
        "quatro. [p=0.2] Os de dentro encaixam, [p=0.2] e o resultado é *três por quatro,* [p=0.2] o mesmo tamanho de C. "
        "[p=0.2] Então dá para somar. [p=0.2] {ok}*Letra C!* [p=0.4] {xa}Na A, [p=0.2] quatro não encaixa com três. "
        "[p=0.2] {xb}Na B, [p=0.2] as ordens são diferentes. [p=0.2] {xd}Na D, [p=0.2] quatro e três de novo, [p=0.2] "
        "{xe}e na E, [p=0.2] dois e três."),

    # ================= QUESTÃO 5: CÓDIGO COM INVERSA =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma mensagem foi trancada com a chave *A igual a dois, um; cinco, três.* "
        "[p=0.2] Chegou a mensagem *sete, dezoito.* [p=0.3] {b}Quais eram os números originais, de cima para baixo? "
        "[p=0.4] {la}A, [p=0.2] um e três. [p=0.2] {lb}B, [p=0.2] três e um. [p=0.2] {lc}C, [p=0.2] menos três e menos "
        "um. [p=0.2] {ld}D, [p=0.2] trinta e nove e setenta e um. [p=0.2] {le}E, [p=0.2] trinta e dois e oitenta e "
        "nove. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}A chave do cadeado: [p=0.2] a inversa. [p=0.2] a d menos b c, [p=0.2] seis menos cinco, [p=0.2] *um.* "
        "[p=0.2] Troca a diagonal, [p=0.2] muda o sinal da outra: [p=0.2] *três, menos um; menos cinco, dois.* [p=0.3] "
        "{a}Vezes sete, dezoito: [p=0.2] vinte e um menos dezoito, *três;* [p=0.2] menos trinta e cinco mais trinta e "
        "seis, *um.* [p=0.2] {v}Conferindo: [p=0.2] dois vezes três mais um, sete. [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A "
        "A inverteu a ordem. [p=0.2] {xc}A C mudou os sinais da diagonal errada. [p=0.2] {xd}A D *só trocou* a diagonal, "
        "[p=0.2] {xe}e a E trancou de novo com A."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}O endereço, os tipos de matriz [p=0.2] e as tabelas de jogos e distâncias: "
        "[p=0.2] episódio um. [p=0.3] {c}Soma, número vezes matriz e igualdade: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}O produto linha por coluna [p=0.2] e as rotas com A ao quadrado: [p=0.2] episódio três. [p=0.3] {b}As "
        "propriedades e a inversa: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte e cinco questões* [p=0.2] {b}e acerte pelo menos *dezoito.* [p=0.4] "
        "{c}Com pelo menos *oito* de leitura de tabela [p=0.2] e *cinco* de produto em contexto."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Determinantes e sistemas lineares:* [p=0.3] {b}o número *a d menos b c* da inversa "
        "ganha nome [p=0.3] {c}e passa a decidir se um sistema tem *uma solução, nenhuma ou infinitas.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de matrizes está completa. [p=0.2] Bons "
        "estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
