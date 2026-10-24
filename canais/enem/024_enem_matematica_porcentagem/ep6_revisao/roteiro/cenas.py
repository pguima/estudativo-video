# Roteiro — Porcentagem, Episódio 6 de 6: Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seções 01, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 o TRIÂNGULO (parte / total × taxa; o denominador é de onde você partiu) · ep2 a MÁQUINA de fator e o "1" que já
#   existia · ep3 a BOLA DE NEVE e a corrente de máquinas · ep4 A BASE MUDOU (barra 100 → 120 → 96; para voltar, divida
#   pelo fator) · ep5 ponto percentual = GRAU no termômetro · a pizza de 360° (1% = 3,6°).
#   (Os eps 4 e 5 ainda não tinham cenas.py quando este foi escrito: frases tiradas do PLANO_DA_SERIE.md e dos prompts.)
# Estratégia (seção 10): converta tudo em fator · use 100 · confira o sentido.
# Treino-relâmpago (variação → fator): +12% 1,12 · −8% 0,92 · +200% 3 · −35% 0,65 · +7,5% 1,075 · −2% 0,98.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (+10% e +20% = +30%) · 2 V (+20% e −20% termina 4% abaixo) · 3 F (depois de +25%, 25% de desconto volta) ·
#   4 V (150 com 20% de desconto → original 187,50) · 5 F (descontos de 30% e 10% = 40%) · 6 F (8% → 10% = subiu 2%) ·
#   7 V (aumentar 200% é triplicar) · 8 F (de 50 para 40 é queda de 25%; é 20%) · 9 F (30% dos homens + 30% das mulheres = 60%).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (tabela, denominador) matrículas 2022 = 800, 2023 = 1 000, 2024 = 900; de 2023 para 2024: −100 ÷ 1 000 = −10% → B.
#      A +12,5% (comparou com 2022, a linha errada) · C −11,1% (usou o valor FINAL, 900, como base) ·
#      D −90% (confundiu o que FICOU, 90%, com o que caiu) · E −100% (leu a diferença de 100 matrículas como porcentagem).
#   Q2 (três sucessivas) +20%, −25%, +10% → 1,20 · 0,75 · 1,10 = 0,99 → 1% mais barato → A. Com 100: 120 → 90 → 99.
#      B 5% mais caro (somou as taxas) · C 10% mais barato (esqueceu o terceiro fator) · D 99% mais barato (leu o fator
#      como o desconto) · E igual (achou que aumentos e descontos se compensam).
#   Q3 (preço original) R$ 1 360 já com 15% de desconto → 1 360 ÷ 0,85 = 1 600 → D. Confere: 1 600 · 0,85 = 1 360.
#      A 204 (calculou só a parte: 15% de 1 360) · B 1 156 (aplicou o desconto de novo) · C 1 564 (somou 15% ao preço com
#      desconto) · E 9 066,67 (dividiu pela TAXA 0,15, e não pelo fator 0,85).
#   Q4 (p.p. × %) aprovação 60% → 45%: −15 p.p. e −25% em relação ao que era → E. A caiu 15% (erro de linguagem) ·
#      B caiu 25 p.p. (trocou os dois) · C caiu 33,3% (base final, 15 ÷ 45) · D caiu 75% (confundiu o que restou, 45 ÷ 60).
#   Q5 (bases diferentes) 200 meninos (30% de bicicleta) e 300 meninas (40%) → 60 + 120 = 180 de 500 = 36% → C.
#      A 12% (multiplicou as taxas, como em sucessivas) · B 35% (média simples, sem pesar os grupos) ·
#      D 60% (usou só as meninas como total) · E 70% (somou porcentagens de grupos diferentes).
# Checklist (seção 13, 13 itens) → episódio: três cálculos, denominador, conta de cabeça: ep1 · fator, ler ao contrário,
#   200% = triplicar: ep2 · sucessivas: ep3 · iguais não se anulam, voltar dividindo, preço antes do desconto: ep4 ·
#   ponto percentual, ângulo de setor, bases diferentes: ep5.
# Meta (material): 40 questões (não 30), pelo menos 28 acertos, concentrando em sucessivas e retorno ao valor original.
# Ponte (do usuário): Unidades e conversões; a repetição do mesmo fator vai virar juros compostos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de porcentagem: estratégia de prova, 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 6"

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
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Porcentagem disputa com a regra de três [p=0.2] o posto de conteúdo *mais cobrado do ENEM.* [p=0.4] {b}Hoje "
        "você confere [p=0.2] se esse ponto *já é seu.* [p=0.4] {c}Com um treino, [p=0.2] nove frases [p=0.2] e cinco "
        "questões novas."),

    # ================= OS FORMATOS (seção 01) =================
    dict(id="02", block="formatos", text=
        "{t}E como ela aparece na prova? [p=0.3] Quase sempre num destes formatos. [p=0.3] {a}*Aumentos e descontos* "
        "[p=0.2] em preços, salários e tarifas. [p=0.3] {b}*Variações sucessivas:* [p=0.2] duas ou mais mudanças em "
        "sequência. [p=0.3] {c}A *variação* entre dois valores de uma tabela. [p=0.3] {d}*Pontos percentuais,* [p=0.2] "
        "em desemprego, juros e aprovação. [p=0.3] {e}E *gráficos* de pizza e de barras."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] o *triângulo.* [p=0.2] Parte em "
        "cima, [p=0.2] total e taxa embaixo. [p=0.2] E o denominador é sempre *de onde você partiu.* [p=0.4] {b}Dois: "
        "[p=0.2] a *máquina de fator.* [p=0.2] O *um* é o que você já tinha. [p=0.4] {c}Três: [p=0.2] a *bola de neve.* "
        "[p=0.2] Variações em sequência, [p=0.2] *multiplique* os fatores."),
    dict(id="04", block="indice", text=
        "{a}Quatro: [p=0.2] *a base mudou.* [p=0.2] Cem sobe para cento e vinte, [p=0.2] cai para noventa e seis. "
        "[p=0.2] E para voltar, [p=0.2] *divida* pelo fator. [p=0.4] {b}E cinco: [p=0.2] ponto percentual é como *grau* "
        "no termômetro, [p=0.2] a diferença. [p=0.2] E na pizza do gráfico, [p=0.2] cada um por cento vale *três vírgula "
        "seis graus.*"),

    # ================= ESTRATÉGIA DE PROVA (seção 10) =================
    dict(id="05", block="estrategia", text=
        "{t}E na hora da prova? [p=0.3] Três hábitos. [p=0.4] {a}Um: [p=0.2] *converta tudo em fator* antes de "
        "calcular. [p=0.2] A questão vira uma multiplicação. [p=0.4] {b}Dois: [p=0.2] o enunciado não deu o valor? "
        "[p=0.2] *Use cem.* [p=0.2] A resposta já sai em porcentagem. [p=0.4] {c}Três: [p=0.2] *confira o sentido.* "
        "[p=0.2] Aumento e desconto iguais terminam *abaixo.* [p=0.2] E desconto sobre desconto dá *menos* que a soma."),

    # ================= TREINO-RELÂMPAGO: VARIAÇÃO → FATOR =================
    dict(id="06", block="treino", text=
        "{t}Treino-relâmpago. [p=0.3] Transforme cada variação em *fator.* [p=0.4] {b}Mais doze por cento. [p=0.3] "
        "{c}Menos oito. [p=0.3] {d}Mais duzentos. [p=0.3] {e}Menos trinta e cinco. [p=0.3] {f}Mais sete vírgula cinco. "
        "[p=0.3] {g}E menos dois. [p=0.4] {p}*Pause e escreva os seis.* [p=2.0]"),
    dict(id="07", block="treino", text=
        "{t}Conferindo! [p=0.3] {b}Um vírgula doze. [p=0.3] {c}Zero vírgula noventa e dois. [p=0.3] {d}*Três:* "
        "[p=0.2] mais duzentos é *triplicar.* [p=0.3] {e}Zero vírgula sessenta e cinco. [p=0.3] {f}Um vírgula zero "
        "setenta e cinco. [p=0.3] {g}E zero vírgula noventa e oito. [p=0.4] {a}Aumento, [p=0.2] um *mais* a taxa. "
        "[p=0.2] Desconto, [p=0.2] um *menos* a taxa."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] um aumento de dez por cento [p=0.2] e depois outro de vinte [p=0.2] dão *trinta por cento.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dez mais vinte é trinta. [p=0.3] {g}Mas o "
        "segundo aumento incide sobre o valor já aumentado. [p=0.2] Multiplique: [p=0.2] *trinta e dois por cento.*"),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] subir vinte por cento [p=0.2] e depois cair vinte por cento [p=0.2] termina *quatro por "
        "cento abaixo.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque parece que um "
        "desfaz o outro. [p=0.3] {g}Mas a base mudou: [p=0.2] cem, [p=0.2] cento e vinte, [p=0.2] *noventa e seis.*"),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] depois de um aumento de vinte e cinco por cento, [p=0.2] um desconto de *vinte e cinco* "
        "volta ao preço antigo. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é o mesmo número. "
        "[p=0.3] {g}Divida pelo fator: [p=0.2] um dividido por um vírgula vinte e cinco, [p=0.2] zero vírgula oitenta. "
        "[p=0.2] O desconto é de *vinte.*"),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] um produto custa cento e cinquenta reais [p=0.2] já com vinte por cento de desconto. "
        "[p=0.2] O preço original era *cento e oitenta e sete e cinquenta.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o instinto soma vinte por cento e dá cento e oitenta. "
        "[p=0.3] {g}Mas os vinte por cento foram sobre o original. [p=0.2] *Divida* por zero vírgula oitenta."),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] um desconto de trinta por cento [p=0.2] e mais dez no caixa [p=0.2] dão *quarenta* de "
        "desconto. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a soma é quarenta. [p=0.3] {g}Mas "
        "zero vírgula setenta vezes zero vírgula noventa [p=0.2] é zero vírgula sessenta e três. [p=0.2] Você paga "
        "sessenta e três: [p=0.2] o desconto é de *trinta e sete.*"),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] o desemprego foi de oito para dez por cento. [p=0.2] Ele *subiu dois por cento.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dez menos oito é dois. [p=0.3] {g}Subiu dois *pontos "
        "percentuais.* [p=0.2] Em relação ao que era, [p=0.2] subiu *vinte e cinco por cento.*"),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] aumentar duzentos por cento [p=0.2] é *triplicar.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque duzentos lembra o dobro. [p=0.3] {g}Mas o fator é um mais "
        "dois, [p=0.2] *três.* [p=0.2] O um é o que você já tinha."),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] cair de cinquenta para quarenta [p=0.2] é uma queda de *vinte e cinco por cento.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque subir de quarenta para cinquenta é vinte e cinco. "
        "[p=0.3] {g}Mas a base é de onde você partiu: [p=0.2] dez dividido por *cinquenta,* [p=0.2] vinte por cento."),
    dict(id="17", block="vf", text=
        "{t}E nove: [p=0.2] se trinta por cento dos homens [p=0.2] e trinta por cento das mulheres praticam esporte, "
        "[p=0.2] então *sessenta por cento* do grupo pratica. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque as duas porcentagens estão na mesma frase. [p=0.3] {g}Mas são *todos diferentes.* [p=0.2] Só se somam "
        "porcentagens do mesmo todo."),
    dict(id="18", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM. [p=0.2] Em todas: [p=0.2] *fatores primeiro,* "
        "[p=0.2] e confira com cem."),

    # ================= QUESTÃO 1: TABELA, O DENOMINADOR =================
    dict(id="19", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma escola registrou suas matrículas: [p=0.2] oitocentas em dois mil e vinte e dois, "
        "[p=0.2] mil em dois mil e vinte e três [p=0.2] e novecentas em dois mil e vinte e quatro. [p=0.3] {b}Em relação "
        "a *dois mil e vinte e três,* [p=0.2] as matrículas de dois mil e vinte e quatro [p=0.4] {la}A, [p=0.2] "
        "aumentaram doze vírgula cinco por cento. [p=0.2] {lb}B, [p=0.2] caíram dez por cento. [p=0.2] {lc}C, [p=0.2] "
        "caíram cerca de onze vírgula um. [p=0.2] {ld}D, [p=0.2] caíram noventa. [p=0.2] {le}E, [p=0.2] caíram cem. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q1", text=
        "{d}De onde você partiu? [p=0.2] De *dois mil e vinte e três.* [p=0.3] {a}A diferença: [p=0.2] novecentos "
        "menos mil, [p=0.2] menos cem. [p=0.3] {b}Dividido pela base, [p=0.2] *mil:* [p=0.2] menos zero vírgula um. "
        "[p=0.3] {c}Caíram *dez por cento.* [p=0.2] {ok}*Letra B!* [p=0.4] {xc}A C usou o novecentos, [p=0.2] o valor "
        "final, [p=0.2] como base. [p=0.2] {xa}A A comparou com o ano errado. [p=0.2] {xd}A D confundiu o que *ficou* "
        "com o que caiu. [p=0.2] {xe}E a E leu cem matrículas como cem por cento."),

    # ================= QUESTÃO 2: TRÊS VARIAÇÕES SUCESSIVAS =================
    dict(id="21", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}O preço de um produto subiu *vinte por cento,* [p=0.2] depois caiu *vinte e "
        "cinco* [p=0.2] e depois subiu *dez,* [p=0.2] sempre sobre o preço do momento. [p=0.3] {b}Em relação ao "
        "início, [p=0.2] o preço final ficou [p=0.4] {la}A, [p=0.2] um por cento mais barato. [p=0.2] {lb}B, [p=0.2] "
        "cinco por cento mais caro. [p=0.2] {lc}C, [p=0.2] dez por cento mais barato. [p=0.2] {ld}D, [p=0.2] noventa e "
        "nove por cento mais barato. [p=0.2] {le}E, [p=0.2] igual. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{d}Fatores primeiro: [p=0.2] um vírgula vinte, [p=0.2] zero vírgula setenta e cinco [p=0.2] e um vírgula dez. "
        "[p=0.3] {a}Multiplique os *três:* [p=0.2] zero vírgula noventa e nove. [p=0.3] {b}Com cem: [p=0.2] cento e "
        "vinte, [p=0.2] noventa, [p=0.2] *noventa e nove.* [p=0.3] {c}Um por cento *mais barato.* [p=0.2] {ok}*Letra "
        "A!* [p=0.4] {xb}A B somou as taxas. [p=0.2] {xc}A C esqueceu o terceiro fator. [p=0.2] {xd}A D leu o fator "
        "como desconto. [p=0.2] {xe}E a E achou que aumentos e descontos se compensam."),

    # ================= QUESTÃO 3: PREÇO ORIGINAL =================
    dict(id="23", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um celular custa *mil trezentos e sessenta reais* [p=0.2] já com *quinze por "
        "cento* de desconto. [p=0.3] {b}Qual era o preço original? [p=0.4] {la}A, [p=0.2] duzentos e quatro reais. "
        "[p=0.2] {lb}B, [p=0.2] mil cento e cinquenta e seis. [p=0.2] {lc}C, [p=0.2] mil quinhentos e sessenta e "
        "quatro. [p=0.2] {ld}D, [p=0.2] mil e seiscentos. [p=0.2] {le}E, [p=0.2] nove mil e sessenta e seis e sessenta "
        "e sete. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q3", text=
        "{d}O fator do desconto: [p=0.2] um menos zero vírgula quinze, [p=0.2] *zero vírgula oitenta e cinco.* [p=0.3] "
        "{a}Para voltar, [p=0.2] *divida* pelo fator: [p=0.2] mil trezentos e sessenta dividido por zero vírgula oitenta "
        "e cinco, [p=0.2] *mil e seiscentos.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Confere: [p=0.2] mil e seiscentos vezes "
        "zero vírgula oitenta e cinco [p=0.2] dá mil trezentos e sessenta. [p=0.4] {xc}A C somou quinze por cento, "
        "[p=0.2] mas a base mudou. [p=0.2] {xb}A B deu o desconto de novo. [p=0.2] {xe}A E dividiu pela taxa, [p=0.2] "
        "não pelo fator. [p=0.2] {xa}E a A calculou só a parte."),

    # ================= QUESTÃO 4: PONTO PERCENTUAL × POR CENTO =================
    dict(id="25", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}A aprovação de um prefeito [p=0.2] caiu de *sessenta* para *quarenta e cinco "
        "por cento.* [p=0.3] {b}Sobre essa mudança, [p=0.2] é correto afirmar que a aprovação [p=0.4] {la}A, [p=0.2] "
        "caiu quinze por cento. [p=0.2] {lb}B, [p=0.2] caiu vinte e cinco pontos percentuais. [p=0.2] {lc}C, [p=0.2] "
        "caiu trinta e três vírgula três por cento. [p=0.2] {ld}D, [p=0.2] caiu setenta e cinco por cento. [p=0.2] "
        "{le}E, [p=0.2] caiu quinze pontos percentuais, [p=0.2] ou vinte e cinco por cento do que era. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{d}O termômetro: [p=0.2] a diferença. [p=0.3] {a}Sessenta menos quarenta e cinco, [p=0.2] *quinze pontos "
        "percentuais.* [p=0.3] {b}E em relação ao que era: [p=0.2] quinze dividido por *sessenta,* [p=0.2] *vinte e "
        "cinco por cento.* [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A é o erro de linguagem. [p=0.2] {xb}A B trocou os "
        "dois. [p=0.2] {xc}A C usou o valor final como base. [p=0.2] {xd}E a D confundiu o que restou com o que caiu."),

    # ================= QUESTÃO 5: BASES DIFERENTES =================
    dict(id="27", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma escola tem *duzentos meninos* [p=0.2] e *trezentas meninas.* [p=0.3] "
        "{b}Trinta por cento dos meninos [p=0.2] e quarenta por cento das meninas [p=0.2] vão de bicicleta. [p=0.3] "
        "{c}Que porcentagem de *todos os alunos* vai de bicicleta? [p=0.4] {la}A, [p=0.2] doze por cento. [p=0.2] "
        "{lb}B, [p=0.2] trinta e cinco. [p=0.2] {lc}C, [p=0.2] trinta e seis. [p=0.2] {ld}D, [p=0.2] sessenta. [p=0.2] "
        "{le}E, [p=0.2] setenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{d}Bases diferentes: [p=0.2] *não some* as porcentagens. [p=0.3] {a}Volte para pessoas: [p=0.2] trinta por "
        "cento de duzentos, [p=0.2] sessenta meninos. [p=0.2] Quarenta por cento de trezentas, [p=0.2] cento e vinte "
        "meninas. [p=0.3] {b}Juntos, [p=0.2] cento e oitenta, [p=0.2] de um total de *quinhentos.* [p=0.3] {c}Cento e "
        "oitenta dividido por quinhentos: [p=0.2] *trinta e seis por cento.* [p=0.2] {ok}*Letra C!* [p=0.4] {xe}A E "
        "somou as porcentagens. [p=0.2] {xb}A B tirou a média, [p=0.2] sem pesar os grupos. [p=0.2] {xd}A D usou só as "
        "meninas como total. [p=0.2] {xa}E a A multiplicou as taxas."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="29", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Os três cálculos, [p=0.2] o denominador [p=0.2] e a "
        "conta de cabeça: [p=0.2] episódio um. [p=0.3] {c}O fator, [p=0.2] ler o fator ao contrário [p=0.2] e os "
        "duzentos por cento: [p=0.2] episódio dois. [p=0.3] {d}Variações sucessivas: [p=0.2] episódio três."),
    dict(id="30", block="checklist", text=
        "{a}Aumento e desconto que não se anulam, [p=0.2] voltar ao original [p=0.2] e o preço antes do desconto: "
        "[p=0.2] episódio quatro. [p=0.3] {b}Ponto percentual, [p=0.2] a pizza [p=0.2] e as bases diferentes: [p=0.2] "
        "episódio cinco. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="31", block="meta", text=
        "{t}E a meta. [p=0.3] Este é um dos assuntos que mais caem, [p=0.2] então não são trinta questões: [p=0.2] "
        "{a}são *quarenta.* [p=0.3] {b}E acerte pelo menos *vinte e oito,* [p=0.2] setenta por cento. [p=0.4] "
        "{c}Concentre-se nas *variações sucessivas* [p=0.2] e no *retorno ao valor original:* [p=0.2] é onde o "
        "caminho do instinto erra."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}O próximo assunto é *Unidades e conversões,* [p=0.3] {b}e mais adiante [p=0.2] a repetição do mesmo fator "
        "[p=0.2] vai virar *juros compostos.*"),
    dict(id="33", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de porcentagem está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
