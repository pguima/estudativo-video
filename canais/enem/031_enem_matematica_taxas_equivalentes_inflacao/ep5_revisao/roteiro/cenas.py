# Roteiro — Taxas Equivalentes e Inflação, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
# Base: Estudos/Enem/estudos/01-matematica/16-taxas-equivalentes-inflacao.html — seções 01, 10, 11 e 13 (+ 03, 06 e 07
#   para "onde aparece"). NÃO usa a seção 12 (Questões 1 a 9) nem as questões novas dos eps 2 (financeiras X e Y) e 3
#   (inflação de 25% e 20%). As 5 questões são INÉDITAS, com os números e distratores do prompt.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o MESMO DESTINO por caminhos diferentes · FATOR PRIMEIRO, TAXA DEPOIS (tire o 1 no fim) · a RETA da proporcional ×
#     a CURVA da equivalente ·
#   ep2 a nominal é o PREÇO DA VITRINE; a efetiva é o que passa NO CAIXA ·
#   ep3 a ESCADA ROLANTE de preços · PODER DE COMPRA É UMA DIVISÃO ·
#   ep4 DEFLACIONAR é traduzir para o dinheiro de antigamente · taxa real: DIVIDA OS FATORES.
#   Ícones do índice (prompt): reta × curva · etiqueta de vitrine · carrinho de supermercado · escada rolante.
# O que a prova cobra (seção 01): trocar o período sem multiplicar nem dividir · separar inflação de ganho real
#   multiplicando/dividindo fatores · usar as potências dadas.
# Onde aparece (03, 06, 07): rotativo do cartão (10% ao mês → 1,1^12 ≈ 3,14 → cerca de 214% ao ano: três dígitos) ·
#   IPCA do IBGE e gráficos de inflação em Humanas · reajuste de salário e poder de compra · Empréstimos e Comparação.
# Estratégia (seção 10): fatores ao lado de cada taxa · regime e tipo de taxa ("capitalizado" = nominal) · use as
#   aproximações dadas e confira a plausibilidade.
#   IMPRECISÃO DO MATERIAL (hábito 3): "a taxa real deve ficar um pouco ABAIXO da diferença entre nominal e inflação" só
#   vale quando há ganho (26% e 20%: 5% < 6%). Com perda, a real fica ACIMA da diferença (8% e 20%: −10% > −12%). O certo é
#   "um pouco MENOR que a diferença, em tamanho": real = (n − π) ÷ (1 + π). O vídeo diz assim.
# V/F (os 9 erros da seção 11, com números NOSSOS — sem os 44%/20% da Q9, os 26%/20% da Q6 nem os 10% e 20% da Q4;
#   6 falsas e 3 verdadeiras):
#   1 F (2% a.m. = 24% a.a. em compostos; é 1,02^12 ≈ 1,268 → ≈ 26,8%) ·
#   2 F (21% em dois anos = 10,5% ao ano; é a raiz do fator: 1,1² = 1,21 → 10%) ·
#   3 F (12% a.a. capitalizados mensalmente custam 12% ao ano; 1,01^12 ≈ 1,1268 → ≈ 12,68%) ·
#   4 V (fator acumulado 1,268 = aumento de 26,8%; o distrator 126,8% esqueceu de tirar o 1) ·
#   5 F (inflação de 5% e depois 10% = 15%; 1,05 · 1,1 = 1,155 → 15,5%) ·
#   6 V (inflação de 100% tira metade do poder de compra: 1 ÷ 2 = 0,5; quem diria "perde 100%" ficaria sem nada) ·
#   7 F (rendeu 17,6% com inflação de 12%: ganho real de 5,6%; 1,176 ÷ 1,12 = 1,05 → 5%) ·
#   8 V (render 8% num ano de inflação de 10% é perder poder de compra: 1,08 ÷ 1,10 ≈ 0,982) ·
#   9 F (a inflação caiu de 8% para 4%: os preços caíram; continuam subindo, mais devagar; preço caindo = deflação).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 5% a.m. → trimestral, dado 1,05³ ≈ 1,158 → 15,8% → C. A 15% (proporcional, a reta) · B 115,8% (fator sem tirar o 1)
#      · D 1,58% (vírgula deslocada) · E 5% (repetiu a mensal).
#   Q2 30% a.a. capitalizados semestralmente → 15% a.s. → 1,15² = 1,3225 → 32,25% → A. B 30% (a vitrine) · C 15% (só a
#      taxa do semestre) · D 132,25% (fator) · E 60% (somou 30% duas vezes). Conferência pelo atalho do ep2: 30 + 15²/100.
#   Q3 inflação de 50% com renda parada → 1 ÷ 1,5 ≈ 0,667 → perda de ≈ 33,3% → D. A 50% (= inflação) · B 66,7% (o que
#      restou) · C 25% (metade da inflação) · E 150% (o fator).
#   Q4 reajuste de 8% com inflação de 20% → 1,08 ÷ 1,20 = 0,90 → perda real de 10% → B. A perda de 12% (subtraiu) ·
#      C ganho de 8% (ignorou a inflação) · D perda de 28% (somou as taxas) · E ganho de 10% (sinal trocado).
#   Q5 inflação de 6%, 4% e 2% → 1,06 · 1,04 · 1,02 ≈ 1,124 → os preços SUBIRAM ≈ 12,4% → E. A "caíram" e B "voltaram ao
#      nível inicial" (inflação caindo ≠ preço caindo) · C 12% (somou) · D 2% (só o último ano).
# Gabaritos: C, A, D, B, E.
# Checklist (seção 13, 13 itens) → episódio (como o prompt indica): proporcional × equivalente, potências: ep1 · nominal ×
#   efetiva e acumuladas: ep2 · inflação, poder de compra e inflação em queda: ep3 · deflacionar, taxa real e aproximação:
#   ep4 · o último item (Empréstimos) é a ponte.
# Meta (material): 20 questões, pelo menos 14 acertos (70%), priorizando taxa real e reajuste e comparação de períodos.
# Ponte (do usuário): Empréstimos, financiamentos e parcelamentos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("Revisão de taxas equivalentes e inflação: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, "
          "Taxas episódio 5")

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "IPCA": "i-pê-cê-á",
    "IBGE": "i-bê-gê-é",
}

SCENES = [
    # ================= GANCHO (frases do usuário) =================
    dict(id="01", block="hook", text=
        "{a}A prova quase nunca escreve a palavra *\"equivalente\".* [p=0.4] {b}Ela pergunta qual aplicação *rende mais,* "
        "[p=0.2] se o salário *ganhou da inflação,* [p=0.2] quanto custou *de verdade* um empréstimo. [p=0.4] {c}Por trás "
        "de tudo, [p=0.2] uma ideia só: [p=0.3] *fatores.* [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso "
        "[p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova cobra? [p=0.4] {a}Um: [p=0.2] trocar o período de uma taxa composta [p=0.2] *sem* multiplicar "
        "nem dividir pelo número de períodos. [p=0.3] {b}Dois: [p=0.2] separar a inflação do *ganho real,* [p=0.2] "
        "combinando as taxas por *multiplicação de fatores.* [p=0.3] {c}Três: [p=0.2] usar as *potências* que o enunciado "
        "dá, [p=0.2] sem tentar calcular."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] taxas equivalentes são o "
        "*mesmo destino* por caminhos diferentes. [p=0.3] *Fator primeiro, taxa depois:* [p=0.2] no fim, [p=0.2] tire o "
        "um. [p=0.3] A proporcional segue a *reta;* [p=0.2] a equivalente, a *curva.* [p=0.4] {b}Dois: [p=0.2] a taxa "
        "nominal é o *preço da vitrine;* [p=0.2] a efetiva é o que passa *no caixa.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] a *escada rolante* de preços. [p=0.2] E poder de compra [p=0.2] é uma *divisão.* [p=0.4] "
        "{b}Quatro: [p=0.2] deflacionar é *traduzir* para o dinheiro de antigamente. [p=0.3] E taxa real: [p=0.2] "
        "*divida os fatores,* [p=0.2] nunca subtraia as taxas."),

    # ================= ONDE APARECE (seções 03, 06 e 07) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}No *rotativo do cartão:* [p=0.2] a taxa ao mês tem um dígito, [p=0.2] e a "
        "taxa ao ano tem *três.* [p=0.3] {b}No *IPCA,* do *IBGE,* [p=0.2] e nos gráficos de inflação de *Ciências "
        "Humanas.* [p=0.3] {c}No *reajuste do salário* [p=0.2] e no poder de compra. [p=0.3] {d}E nas próximas séries: "
        "[p=0.2] Empréstimos, [p=0.2] e Comparação de propostas."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 10) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] três hábitos. [p=0.4] {a}Um: [p=0.2] escreva o *fator* ao lado de cada taxa. [p=0.2] Vinte "
        "por cento, [p=0.2] um vírgula dois. [p=0.2] Menos dez, [p=0.2] zero vírgula nove. [p=0.3] {b}Dois: [p=0.2] "
        "identifique o *regime* e o *tipo* de taxa. [p=0.2] Leu *\"capitalizado\"?* [p=0.2] É taxa nominal. [p=0.3] "
        "{c}Três: [p=0.2] use as aproximações *dadas* [p=0.2] e confira se o resultado é *plausível.* [p=0.2] A taxa real "
        "fica perto da diferença, [p=0.2] mas sempre um pouco *menor* que ela, em tamanho."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] em juros compostos, [p=0.2] dois por cento ao mês [p=0.2] equivalem a *vinte e quatro por cento ao "
        "ano.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque doze vezes dois dá vinte e quatro. [p=0.3] "
        "{g}Mas isso é a reta, [p=0.2] dos juros simples. [p=0.2] Em compostos, [p=0.2] eleve o fator a doze: [p=0.2] "
        "cerca de *vinte e seis vírgula oito.*"),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] vinte e um por cento em dois anos [p=0.2] equivalem a *dez e meio por cento ao ano.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dividir por dois parece justo. [p=0.3] {g}Para encurtar o "
        "período, [p=0.2] tire a *raiz do fator.* [p=0.2] Um vírgula um ao quadrado [p=0.2] dá um vírgula vinte e um. "
        "[p=0.2] *Dez por cento* ao ano."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] doze por cento ao ano, [p=0.2] *capitalizados mensalmente,* [p=0.2] custam exatamente *doze por "
        "cento ao ano.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o doze está escrito ali. [p=0.3] "
        "{g}Mas é o preço da vitrine. [p=0.2] Divida por doze, [p=0.2] um por cento ao mês, [p=0.2] e capitalize: [p=0.2] "
        "cerca de *doze vírgula sessenta e oito.*"),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] um fator acumulado de *um vírgula dois seis oito* [p=0.2] significa um aumento de *vinte e "
        "seis vírgula oito por cento.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a "
        "alternativa de *cento e vinte e seis* vírgula oito [p=0.2] está sempre lá. [p=0.3] {g}Fator primeiro, taxa "
        "depois: [p=0.2] *tire o um.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] inflação de cinco por cento, [p=0.2] e depois de dez, [p=0.2] acumulam *quinze por cento.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinco mais dez dá quinze. [p=0.3] {g}Mas a "
        "segunda inflação incide sobre preços *já aumentados.* [p=0.2] Multiplique os fatores: [p=0.2] um vírgula cento e "
        "cinquenta e cinco. [p=0.2] *Quinze e meio* por cento."),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] uma inflação de *cem por cento* [p=0.2] tira *metade* do seu poder de compra. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente espera perder os mesmos cem por cento. "
        "[p=0.3] {g}Mas poder de compra é *divisão:* [p=0.2] um dividido por dois, [p=0.2] meio. [p=0.2] Os preços "
        "dobraram: [p=0.2] seu dinheiro compra *metade.*"),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] uma aplicação rendeu dezessete vírgula seis por cento [p=0.2] num ano de inflação de doze. "
        "[p=0.2] O ganho real foi de *cinco vírgula seis.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque a subtração é rápida. [p=0.3] {g}Mas taxa real é *divisão de fatores:* [p=0.2] um vírgula cento e setenta "
        "e seis [p=0.2] dividido por um vírgula doze. [p=0.2] *Cinco por cento.*"),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] render oito por cento [p=0.2] num ano de inflação de dez [p=0.2] é *perder* poder de compra. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o extrato mostra o saldo *subindo.* "
        "[p=0.3] {g}Mas você andou mais devagar que a escada rolante. [p=0.2] Um vírgula zero oito dividido por um "
        "vírgula dez: [p=0.2] *menos de um.*"),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] a inflação caiu de oito para quatro por cento. [p=0.2] Então os preços *caíram.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a palavra \"caiu\" está na manchete. [p=0.3] {g}Quem caiu "
        "foi a *velocidade.* [p=0.2] A escada ficou mais lenta, [p=0.2] mas continua *subindo.* [p=0.2] Preço caindo é "
        "*deflação:* [p=0.2] taxa negativa."),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas. [p=0.2] Em todas, [p=0.2] escreva os *fatores* primeiro."),

    # ================= QUESTÃO 1: TAXA EQUIVALENTE =================
    dict(id="18", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma aplicação rende *cinco por cento ao mês,* [p=0.2] em juros compostos. [p=0.2] "
        "Considere um vírgula zero cinco ao cubo [p=0.2] igual a um vírgula cento e cinquenta e oito. [p=0.3] {b}A taxa "
        "*trimestral* equivalente é de [p=0.4] {la}A, [p=0.2] quinze por cento. [p=0.2] {lb}B, [p=0.2] cento e quinze "
        "vírgula oito. [p=0.2] {lc}C, [p=0.2] quinze vírgula oito. [p=0.2] {ld}D, [p=0.2] um vírgula cinquenta e oito. "
        "[p=0.2] {le}E, [p=0.2] cinco por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}Fator primeiro: [p=0.2] *um vírgula zero cinco.* [p=0.3] {a}Três meses, [p=0.2] três fatores: [p=0.2] o cubo "
        "que o enunciado deu, [p=0.2] *um vírgula cento e cinquenta e oito.* [p=0.3] {b}Taxa depois: [p=0.2] tire o um. "
        "[p=0.2] *Quinze vírgula oito por cento.* [p=0.2] {ok}*Letra C!* [p=0.3] {v}Plausível: [p=0.2] um pouco acima "
        "dos quinze da reta. [p=0.4] {xa}A A é a proporcional. [p=0.2] {xb}A B esqueceu de tirar o um. [p=0.2] {xd}A D "
        "deslocou a vírgula, [p=0.2] {xe}e a E repetiu a taxa do mês."),

    # ================= QUESTÃO 2: NOMINAL → EFETIVA =================
    dict(id="20", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um banco anuncia *trinta por cento ao ano,* [p=0.2] *capitalizados "
        "semestralmente.* [p=0.2] Considere um vírgula quinze ao quadrado [p=0.2] igual a um vírgula três dois dois cinco. "
        "[p=0.3] {b}A taxa *efetiva* anual é de [p=0.4] {la}A, [p=0.2] trinta e dois vírgula vinte e cinco. [p=0.2] "
        "{lb}B, [p=0.2] trinta. [p=0.2] {lc}C, [p=0.2] quinze. [p=0.2] {ld}D, [p=0.2] cento e trinta e dois vírgula vinte "
        "e cinco. [p=0.2] {le}E, [p=0.2] sessenta por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}\"Capitalizados\" [p=0.2] anuncia o preço da *vitrine.* [p=0.3] {a}A nominal só serve para dividir: [p=0.2] "
        "trinta por dois semestres, [p=0.2] *quinze por cento* ao semestre. [p=0.3] {b}Agora, capitalize: [p=0.2] um "
        "vírgula quinze ao quadrado, [p=0.2] um vírgula três dois dois cinco. [p=0.2] Tire o um: [p=0.2] *trinta e dois "
        "vírgula vinte e cinco.* [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confira pelo atalho: [p=0.2] trinta, [p=0.2] mais "
        "quinze ao quadrado sobre cem. [p=0.4] {xb}A B é a vitrine. [p=0.2] {xc}A C é só o semestre. [p=0.2] {xd}A D "
        "esqueceu de tirar o um, [p=0.2] {xe}e a E somou trinta duas vezes."),

    # ================= QUESTÃO 3: PODER DE COMPRA =================
    dict(id="22", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Num ano de inflação de *cinquenta por cento,* [p=0.2] uma pessoa ficou com a renda "
        "*parada.* [p=0.3] {b}O poder de compra dela caiu cerca de [p=0.4] {la}A, [p=0.2] cinquenta por cento. [p=0.2] "
        "{lb}B, [p=0.2] sessenta e seis vírgula sete. [p=0.2] {lc}C, [p=0.2] vinte e cinco. [p=0.2] {ld}D, [p=0.2] trinta "
        "e três vírgula três. [p=0.2] {le}E, [p=0.2] cento e cinquenta por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}Poder de compra [p=0.2] é uma *divisão.* [p=0.3] {a}O mesmo dinheiro, [p=0.2] dividido pelo fator dos preços: "
        "[p=0.2] um dividido por um vírgula cinco, [p=0.2] *zero vírgula seis seis sete.* [p=0.3] {b}Sobraram dois "
        "terços. [p=0.2] Perdeu *um terço:* [p=0.2] cerca de *trinta e três vírgula três.* [p=0.2] {ok}*Letra D!* "
        "[p=0.3] {v}Plausível: [p=0.2] a perda é *menor* que a inflação. [p=0.4] {xa}A A perdeu a inflação inteira. "
        "[p=0.2] {xb}A B é o que *sobrou.* [p=0.2] {xc}A C cortou a inflação ao meio, [p=0.2] {xe}e a E é o fator."),

    # ================= QUESTÃO 4: REAJUSTE × INFLAÇÃO =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma categoria teve reajuste de *oito por cento* [p=0.2] num ano de inflação de "
        "*vinte por cento.* [p=0.3] {b}Em termos reais, o salário [p=0.4] {la}A, [p=0.2] perdeu doze por cento. [p=0.2] "
        "{lb}B, [p=0.2] perdeu dez. [p=0.2] {lc}C, [p=0.2] ganhou oito. [p=0.2] {ld}D, [p=0.2] perdeu vinte e oito. "
        "[p=0.2] {le}E, [p=0.2] ganhou dez. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}Taxa real: [p=0.2] *divida os fatores.* [p=0.3] {a}Um vírgula zero oito [p=0.2] dividido por um vírgula vinte: "
        "[p=0.2] *zero vírgula nove.* [p=0.3] {b}Fator menor que um, [p=0.2] perda. [p=0.2] Tire do um: [p=0.2] *perda "
        "real de dez por cento.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Plausível: [p=0.2] um pouco menor que os doze da "
        "subtração. [p=0.4] {xa}A A subtraiu as taxas. [p=0.2] {xc}A C esqueceu a inflação. [p=0.2] {xd}A D somou as "
        "duas, [p=0.2] {xe}e a E trocou o sinal."),

    # ================= QUESTÃO 5: INFLAÇÃO EM QUEDA =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um gráfico mostra a inflação de três anos seguidos: [p=0.2] *seis,* [p=0.2] "
        "*quatro* [p=0.2] e *dois por cento.* [p=0.2] O produto dos fatores é cerca de um vírgula cento e vinte e quatro. "
        "[p=0.3] {b}Nesses três anos, os preços [p=0.4] {la}A, [p=0.2] caíram. [p=0.2] {lb}B, [p=0.2] voltaram ao nível "
        "inicial. [p=0.2] {lc}C, [p=0.2] subiram doze por cento. [p=0.2] {ld}D, [p=0.2] subiram dois por cento. [p=0.2] "
        "{le}E, [p=0.2] subiram cerca de doze vírgula quatro. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}A escada rolante ficou *mais lenta,* [p=0.2] mas não parou. [p=0.3] {a}Todo ano, [p=0.2] um fator *maior que "
        "um.* [p=0.2] Os preços subiram *nos três.* [p=0.3] {b}Multiplique: [p=0.2] um vírgula cento e vinte e quatro. "
        "[p=0.2] Tire o um: [p=0.2] subiram cerca de *doze vírgula quatro.* [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A {xb}e "
        "a B [p=0.2] confundiram inflação caindo com preço caindo. [p=0.2] Isso seria *deflação.* [p=0.2] {xc}A C somou "
        "as taxas, [p=0.2] {xd}e a D olhou só o último ano."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Proporcional e equivalente, [p=0.2] e as potências de "
        "cabeça: [p=0.2] episódio um. [p=0.3] {c}Nominal e efetiva, [p=0.2] e taxas acumuladas: [p=0.2] episódio dois."),
    dict(id="29", block="checklist", text=
        "{a}Inflação, [p=0.2] poder de compra [p=0.2] e inflação em queda: [p=0.2] episódio três. [p=0.3] {b}Deflacionar, "
        "[p=0.2] taxa real [p=0.2] e a aproximação: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] "
        "reveja o episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* [p=0.2] {b}e acerte pelo menos *catorze,* [p=0.2] setenta por "
        "cento. [p=0.4] {c}Priorize as de *taxa real e reajuste de salário* [p=0.2] e as que comparam taxas de *períodos "
        "diferentes:* [p=0.2] são as que mais caem."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O próximo assunto é *Empréstimos, financiamentos e parcelamentos:* [p=0.3] {b}os juros escondidos no *\"sem "
        "juros\",* [p=0.3] {c}a tabela do *SAC* [p=0.2] {d}e a da *Price.*"),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de taxas equivalentes e inflação está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
