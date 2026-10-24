# Roteiro — Razão, Proporção e Regra de Três, Episódio 6 de 6: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seções 01, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
#   Os erros de km/h ↔ m/s e de escala (seção 11) são só CITADOS, com a regra em uma frase e o aviso de série própria
#   ("Velocidade, densidade e vazão"; "Escalas, plantas e mapas").
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 COPOS DE SUCO: razão = comparar dividindo; "o que vem depois do 'para' vai embaixo" ·
#   ep2 RECEITA DUPLA: proporção = a mesma receita em tamanhos diferentes; PONTAS × PONTAS = MIOLO × MIOLO; PACOTINHOS de k ·
#   ep3 BARRAS DIRETA/INVERSA: o TESTE DO DOBRO · ep4 PACOTE DE TRABALHO: cada coluna interrogada sozinha; pacote de
#   pessoa-hora fixo · ep5 GATOS: a PERGUNTA DE OURO ("dobrar a causa dobra mesmo o efeito?").
# Treino-relâmpago (direta, inversa ou nem é proporcional?): pães e preço → DIRETA · pintores iguais e dias para o mesmo
#   muro → INVERSA · lado do quadrado e área → NEM · consumo e conta de luz com tarifa por faixa → NEM.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras): 1 F (em pé para o total = 7/21; é 7/28 = 1/4) ·
#   2 F (10 operários em 6 dias → 20 em 12 dias; é inversa: 3 dias) · 3 V (padronizar horas e minutos antes) ·
#   4 F (36 km/h = 36 m/s; regra: ÷ 3,6 — série própria) · 5 V (composta: cada coluna com a incógnita, uma de cada vez) ·
#   6 F (lado dobra → área dobra; quadruplica) · 7 F (juros compostos: dobro do tempo, dobro de juros; só nos simples) ·
#   8 V (1:50 000 é maior que 1:250 000 — série própria) · 9 F (4 gatos, 4 ratos → 4 min; continua 2 min).
# QUESTÕES INÉDITAS (todas conferidas em Python: uma única correta; cada errada = um erro clássico):
#   Q1 (razão "para o total") feira: 25 públicas + 15 particulares = 40; particulares para o total = 15/40 = 3/8 → B.
#      A 3/5 (comparou com o outro grupo: 15/25) · C 5/8 (públicas para o total) · D 5/3 e E 8/3 (inverteram a ordem).
#   Q2 (inversa + unidades) 2 bombas em 1 h 30 min; 3 bombas → 2·90 = 3·x → x = 60 min → C.
#      A 1 (fez em horas, 2·1,5/3 = 1, e não converteu para minutos) · B 52 (leu 1 h 30 como 1,3 h = 78 min: 2·78/3) ·
#      D 90 (achou que o tempo não muda) · E 135 (aplicou direta: 90·3/2).
#   Q3 (composta, atalho dos homens-hora) 6 costureiras, 8 h/dia, 12 dias → 4 costureiras, 4 h/dia:
#      6·8·12 = 576 = 4·4·x → x = 36 dias → E.
#      A 4 (não inverteu nenhuma coluna: 12·4/6·4/8) · B 9 (esqueceu de inverter a das horas: 12·6/4·4/8) ·
#      C 16 (esqueceu de inverter a das costureiras: 12·4/6·8/4) · D 18 (ignorou as horas: 12·6/4).
#   Q4 (truque do k, três partes) rifa: R$ 20, R$ 30 e R$ 50 → 2:3:5; prêmio R$ 4 000 → k = 400 → 800, 1 200, 2 000;
#      a que pagou MENOS: R$ 800 → A.
#      B 1 200 (a do meio) · C 1 333,33 (partes iguais) · D 1 600 (esqueceu a 3ª amiga: 4 000·2/5) · E 2 000 (a MAIOR).
#   Q5 (não vale: área a partir do lado) jardim quadrado de 4 m → 2 sacos de adubo; de 8 m → área 16 → 64 m² (×4) → 8 → D.
#      A 1 (inversa pelo lado) · B 2 (achou que nada muda) · C 4 (regra de três direta com o lado) · E 16 (ao cubo, volume).
# Checklist (seção 13, 13 itens) → episódio: razão na ordem certa e razões usuais: ep1 · propriedade fundamental e
#   truque do k: ep2 · teste do dobro e unidades: ep3 · composta e homens-hora: ep4 · quando não vale, plausibilidade e
#   valor unitário: ep5 · km/h ↔ m/s: série "Velocidade, densidade e vazão" · escala: série "Escalas, plantas e mapas".
# Meta (material): 40 questões (não 30), pelo menos 28 acertos (70%), incluindo Física e Química.
# Ponte (do usuário): Grandezas proporcionais (gráfico, tabela e constante).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de razão, proporção e regra de três: treino, 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 6"

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
        "{a}Este é o assunto de *maior retorno* de toda a Matemática básica, [p=0.2] talvez da prova inteira. [p=0.4] "
        "{b}Ele aparece em porcentagem, [p=0.2] Física, [p=0.2] Química [p=0.2] e Geografia. [p=0.4] {c}Hoje você confere "
        "se está *pronto.* [p=0.4] {d}Com um treino, [p=0.2] nove pegadinhas [p=0.2] e cinco questões novas."),

    # ================= ONDE APARECE (seção 01) =================
    dict(id="02", block="onde", text=
        "{t}Onde ele aparece? [p=0.3] {a}*Direto,* [p=0.2] em escala, [p=0.2] velocidade, [p=0.2] densidade, [p=0.2] "
        "consumo, [p=0.2] câmbio [p=0.2] e produtividade. [p=0.3] {b}Dentro da *porcentagem:* "
        "[p=0.2] todo aumento e todo desconto é uma proporção. [p=0.3] {c}Na *Física,* [p=0.2] quase toda fórmula é uma "
        "razão. [p=0.3] {d}Na *Química,* [p=0.2] a estequiometria, [p=0.2] o cálculo das quantidades numa reação, [p=0.2] "
        "é regra de três com mols, [p=0.2] a dúzia da Química. [p=0.3] "
        "{e}E na *Geografia:* [p=0.2] densidade demográfica "
        "e escala."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] razão é comparar dividindo, [p=0.2] "
        "e o que vem depois do *para* vai embaixo. [p=0.4] {b}Dois: [p=0.2] proporção é a *mesma receita* em tamanhos "
        "diferentes. [p=0.2] Pontas vezes pontas [p=0.2] é igual a miolo vezes miolo. [p=0.2] E razão com soma [p=0.2] "
        "vira *pacotinhos* de k. [p=0.4] {c}Três: [p=0.2] o *teste do dobro.* [p=0.2] Dobrou também? [p=0.2] Direta. "
        "[p=0.2] Virou metade? [p=0.2] Inversa."),
    dict(id="04", block="indice", text=
        "{a}Quatro: [p=0.2] na regra de três composta, [p=0.2] cada coluna é interrogada *sozinha,* [p=0.2] frente a "
        "frente com a incógnita, [p=0.2] o valor procurado. [p=0.2] E numa obra fixa, [p=0.2] o *pacote* de "
        "pessoa-hora não muda. [p=0.4] {b}E cinco: [p=0.2] antes de qualquer regra de três, [p=0.2] a *pergunta de ouro:* "
        "[p=0.2] dobrar a causa dobra *mesmo* o efeito?"),

    # ================= O QUE MAIS RENDE + TREINO-RELÂMPAGO =================
    dict(id="05", block="rendem", text=
        "{t}E se você só tiver tempo para duas coisas? [p=0.4] {a}Primeiro: [p=0.2] decidir se a relação é *direta ou "
        "inversa.* [p=0.4] {b}Segundo: [p=0.2] saber *quando a regra de "
        "três não vale.* "),
    dict(id="06", block="treino", text=
        "{t}Treino-relâmpago. [p=0.3] {a}Direta, [p=0.2] inversa, [p=0.2] ou "
        "*nem é proporcional?* [p=0.4] {b}Um: [p=0.2] a quantidade de pães e o preço a pagar. [p=0.3] {c}Dois: [p=0.2] o "
        "número de pintores iguais e os dias para pintar o mesmo muro. [p=0.3] {d}Três: [p=0.2] o lado de um quadrado e "
        "a área dele. [p=0.3] {e}Quatro: [p=0.2] o consumo de energia e o valor da conta de luz, [p=0.2] com tarifa por "
        "faixa, [p=0.2] em que o preço muda conforme o consumo. [p=0.4] {p}*Pause e decida.* "
        "[p=2.0]"),
    dict(id="07", block="treino", text=
        "{t}Conferindo! [p=0.3] {a}Pães e preço: [p=0.2] o dobro de pães custa o dobro. [p=0.2] *Direta.* [p=0.3] "
        "{b}Pintores e dias: [p=0.2] o dobro de pintores leva metade dos dias. [p=0.2] *Inversa.* [p=0.3] {c}Lado e área: "
        "[p=0.2] dobrar o lado deixa a área *quatro vezes* maior. [p=0.2] *Nem é proporcional.* [p=0.3] {d}E a tarifa por faixa: "
        "[p=0.2] não há uma razão única. [p=0.2] *Nem é "
        "proporcional.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam "
        "pontos. [p=0.4] {b}Em cada uma, [p=0.2] pause e "
        "responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] num ônibus com sete pessoas em pé e vinte e uma sentadas, [p=0.2] a razão de quem está em pé *para "
        "o total* é sete sobre vinte e um. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o vinte e um "
        "parece o outro lado da comparação. [p=0.3] {g}Mas o que vem depois do *para* vai embaixo: "
        "[p=0.2] o total, [p=0.2] vinte e oito. [p=0.2] Sete vinte e oito avos, [p=0.2] *um quarto.*"),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] se dez operários fazem uma obra em seis dias, [p=0.2] vinte operários fazem a mesma obra em "
        "*doze* dias. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a gente monta tudo como direta, "
        "[p=0.2] no automático. [p=0.3] {g}Teste do dobro: [p=0.2] o dobro de operários leva *metade* dos dias. [p=0.2] "
        "Inversa: [p=0.2] *três* dias."),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] antes de montar a regra de três, [p=0.2] horas e minutos precisam virar a *mesma unidade.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque, com as unidades misturadas, [p=0.2] a "
        "conta fecha do mesmo jeito. [p=0.3] {g}E o resultado sai errado, [p=0.2] sem alarme. "
        "[p=0.2] Unidades iguais *antes de tudo.*"),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] trinta e seis quilômetros por hora [p=0.2] e trinta e seis metros por segundo [p=0.2] são a "
        "*mesma* velocidade. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o número é o mesmo. [p=0.3] "
        "{g}A regra: [p=0.2] para passar a metros por segundo, [p=0.2] *divida* por três vírgula seis. "
        "[p=0.2] [p=0.3] {s}Isso tem *série própria:* [p=0.2] Velocidade, "
        "densidade e vazão."),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] na regra de três composta, [p=0.2] cada coluna é comparada com a da incógnita, [p=0.2] *uma de "
        "cada vez.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de comparar "
        "as colunas entre si. [p=0.3] {g}Mas cada suspeito é interrogado *sozinho:* [p=0.2] as "
        "outras colunas ficam fora da sala."),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] se o lado de um quadrado dobra, [p=0.2] a área também *dobra.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque parece uma regra de três direta. [p=0.3] {g}Teste: [p=0.2] lado um, [p=0.2] "
        "área um. [p=0.2] Lado dois, [p=0.2] área *quatro.* [p=0.2] A área vai *ao quadrado.*"),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] em juros compostos, [p=0.2] o dobro do tempo dá o dobro de juros. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque, nos juros simples, [p=0.2] é assim mesmo. [p=0.3] {g}Mas nos compostos, "
        "[p=0.2] os juros rendem juros, [p=0.2] e o crescimento acelera. [p=0.2] Regra de três, [p=0.2] *só* nos juros "
        "simples."),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] a escala um para cinquenta mil é *maior* que a escala um para duzentos e cinquenta mil. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque duzentos e cinquenta mil é um número maior. "
        "[p=0.3] {g}A regra: [p=0.2] denominador menor, [p=0.2] escala *maior,* [p=0.2] com mais detalhe. [p=0.3] {s}Isso "
        "também tem *série própria:* [p=0.2] Escalas, plantas e mapas."),
    dict(id="17", block="vf", text=
        "{t}E nove: [p=0.2] se dois gatos caçam dois ratos em dois minutos, [p=0.2] quatro gatos caçam quatro ratos em "
        "*quatro* minutos. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece regra de três. [p=0.3] "
        "{g}Mas cada gato caça o seu rato em dois minutos, [p=0.2] todos ao mesmo tempo. [p=0.2] O tempo "
        "*não muda:* [p=0.2] dois minutos."),
    dict(id="18", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM."),

    # ================= QUESTÃO 1: RAZÃO "PARA O TOTAL" =================
    dict(id="19", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma feira de ciências recebeu *quarenta* trabalhos: [p=0.2] vinte e cinco de escolas "
        "públicas [p=0.2] e quinze de escolas particulares. [p=0.3] {b}A razão entre o número de trabalhos de escolas "
        "particulares [p=0.2] e o número *total* de trabalhos é: [p=0.4] {la}A, [p=0.2] três quintos. [p=0.2] {lb}B, "
        "[p=0.2] três oitavos. [p=0.2] {lc}C, [p=0.2] cinco oitavos. [p=0.2] {ld}D, [p=0.2] cinco terços. [p=0.2] {le}E, "
        "[p=0.2] oito terços. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q1", text=
        "{g}Pergunta de ouro: [p=0.2] precisa de regra de três? [p=0.2] Não: [p=0.2] é uma razão, [p=0.2] só dividir. "
        "[p=0.3] {a}Particulares *para o total:* [p=0.2] o total vai embaixo. [p=0.2] Quinze sobre quarenta. [p=0.3] "
        "{b}Simplificando por cinco: [p=0.2] *três oitavos.* [p=0.2] {ok}*Letra B!* [p=0.3] {d}Teste do dobro: "
        "[p=0.2] com o dobro de tudo, [p=0.2] trinta de oitenta, [p=0.2] continua três "
        "oitavos. [p=0.4] {xa}A A comparou com o outro grupo. [p=0.2] {xc}A C é públicas para o "
        "total. [p=0.2] {xd}A D e {xe}a E inverteram a ordem."),

    # ================= QUESTÃO 2: INVERSA COM UNIDADES =================
    dict(id="21", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Duas bombas d'água iguais esvaziam um tanque em *uma hora e meia.* [p=0.3] {b}Com "
        "*três* bombas iguais a essas, [p=0.2] no mesmo ritmo, [p=0.2] em quantos *minutos* o mesmo tanque será "
        "esvaziado? [p=0.4] {la}A, [p=0.2] um. [p=0.2] {lb}B, [p=0.2] cinquenta e dois. [p=0.2] {lc}C, [p=0.2] sessenta. "
        "[p=0.2] {ld}D, [p=0.2] noventa. [p=0.2] {le}E, [p=0.2] cento e trinta e cinco. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="22", block="q2", text=
        "{g}Pergunta de ouro: [p=0.2] o dobro de bombas esvazia mesmo na metade do tempo? [p=0.2] Sim. "
        "[p=0.3] {d}Teste do dobro: [p=0.2] bombas vezes dois, [p=0.2] tempo dividido por dois. "
        "[p=0.2] *Inversa.* [p=0.3] {a}Passo zero, [p=0.2] unidades: [p=0.2] uma hora e meia são *noventa* minutos. "
        "[p=0.3] {b}Na inversa, [p=0.2] o produto é constante: [p=0.2] dois vezes noventa, [p=0.2] cento e oitenta, "
        "[p=0.2] igual a três vezes xis. [p=0.3] {c}Xis igual a *sessenta* minutos. [p=0.2] {ok}*Letra C!* [p=0.3] {v}Faz "
        "sentido: [p=0.2] mais bombas, [p=0.2] menos tempo. [p=0.4] {xe}A E usou direta. [p=0.2] {xb}A B leu uma hora e "
        "meia como um vírgula três hora. [p=0.2] {xa}A A fez a conta em horas [p=0.2] e não converteu para minutos. "
        "[p=0.2] {xd}E a D achou que o tempo não muda."),

    # ================= QUESTÃO 3: COMPOSTA (ATALHO DOS HOMENS-HORA) =================
    dict(id="23", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Numa confecção, [p=0.2] *seis* costureiras, [p=0.2] trabalhando *oito* horas por "
        "dia, [p=0.2] produzem um lote de uniformes em *doze* dias. [p=0.3] {b}No mesmo ritmo, [p=0.2] *quatro* "
        "costureiras, [p=0.2] trabalhando *quatro* horas por dia, [p=0.2] produzirão um lote idêntico em quantos dias? "
        "[p=0.4] {la}A, [p=0.2] quatro. [p=0.2] {lb}B, [p=0.2] nove. [p=0.2] {lc}C, [p=0.2] dezesseis. [p=0.2] {ld}D, "
        "[p=0.2] dezoito. [p=0.2] {le}E, [p=0.2] trinta e seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q3", text=
        "{g}Pergunta de ouro: [p=0.2] o lote é *idêntico,* [p=0.2] então o trabalho é fixo. [p=0.2] Vale o *pacote* de "
        "pessoa-hora. [p=0.3] {d}Teste do dobro, [p=0.2] coluna por coluna: [p=0.2] as duas "
        "são inversas. [p=0.3] {a}O pacote: [p=0.2] seis "
        "vezes oito vezes doze, [p=0.2] *quinhentos e setenta e seis.* [p=0.3] {b}Do outro lado, [p=0.2] quatro vezes "
        "quatro vezes xis, [p=0.2] dezesseis xis. [p=0.3] {c}Quinhentos e setenta e seis dividido por dezesseis: [p=0.2] "
        "*trinta e seis* dias. [p=0.2] {ok}*Letra E!* [p=0.3] {v}Faz sentido: [p=0.2] menos gente, [p=0.2] menos horas, "
        "[p=0.2] mais dias. [p=0.4] {xa}A A não inverteu nenhuma coluna. [p=0.2] {xb}A B esqueceu de inverter a das "
        "horas. [p=0.2] {xc}A C esqueceu de inverter a das costureiras. [p=0.2] {xd}E a D ignorou as horas."),

    # ================= QUESTÃO 4: TRUQUE DO k COM TRÊS PARTES =================
    dict(id="25", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Três amigas compraram juntas um bilhete de rifa: [p=0.2] uma pagou *vinte* reais, "
        "[p=0.2] outra *trinta* [p=0.2] e outra *cinquenta.* [p=0.3] {b}O prêmio de *quatro mil reais* foi dividido na "
        "razão do que cada uma pagou. [p=0.3] {c}Quanto recebeu a amiga que pagou *menos?* [p=0.4] {la}A, [p=0.2] "
        "oitocentos reais. [p=0.2] {lb}B, [p=0.2] mil e duzentos reais. [p=0.2] {lc}C, [p=0.2] mil trezentos e trinta e "
        "três reais e trinta e três centavos. [p=0.2] {ld}D, [p=0.2] mil e seiscentos reais. [p=0.2] {le}E, [p=0.2] dois "
        "mil reais. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{g}Pergunta de ouro: [p=0.2] quem paga o dobro recebe o dobro? [p=0.2] Sim. [p=0.2] "
        "{d}Teste do dobro: [p=0.2] *direta.* [p=0.3] {a}Simplifique a razão: [p=0.2] vinte, [p=0.2] trinta e cinquenta "
        "[p=0.2] viram *dois, três e cinco* pacotinhos. [p=0.3] {b}São dez pacotinhos. [p=0.2] Quatro mil dividido por "
        "dez: [p=0.2] cada pacotinho, [p=0.2] o k, [p=0.2] vale *quatrocentos.* [p=0.3] {c}A que pagou menos tem dois "
        "pacotinhos: [p=0.2] *oitocentos reais.* [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confere: [p=0.2] as três partes "
        "somam quatro mil. [p=0.4] {xe}A E é a parte *maior.* [p=0.2] {xb}A B é "
        "a do meio. [p=0.2] {xc}A C dividiu em partes iguais. [p=0.2] {xd}E a D esqueceu a terceira amiga."),

    # ================= QUESTÃO 5: QUANDO A REGRA DE TRÊS NÃO VALE =================
    dict(id="27", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um jardim quadrado com *quatro metros* de lado [p=0.2] precisa de *dois sacos* "
        "de adubo, [p=0.2] espalhados por igual em toda a área. [p=0.3] {b}Quantos sacos serão necessários para um jardim "
        "quadrado com *oito metros* de lado? [p=0.4] {la}A, [p=0.2] um. [p=0.2] {lb}B, [p=0.2] dois. [p=0.2] {lc}C, "
        "[p=0.2] quatro. [p=0.2] {ld}D, [p=0.2] oito. [p=0.2] {le}E, [p=0.2] dezesseis. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="28", block="q5", text=
        "{g}Pergunta de ouro: [p=0.2] dobrar o *lado* dobra mesmo o adubo? [p=0.2] *Não!* [p=0.2] O adubo segue a "
        "*área.* [p=0.3] {d}Teste do dobro: [p=0.2] lado vezes dois, [p=0.2] área vezes *quatro.* [p=0.2] Com o lado, "
        "[p=0.2] nem é proporcional. [p=0.3] {a}As áreas: [p=0.2] quatro vezes quatro, [p=0.2] dezesseis "
        "metros quadrados; [p=0.2] oito vezes oito, [p=0.2] *sessenta e quatro.* [p=0.3] {b}A área ficou quatro vezes "
        "maior: [p=0.2] dois sacos vezes quatro, [p=0.2] *oito* sacos. [p=0.2] {ok}*Letra D!* [p=0.3] {v}Faz sentido: "
        "[p=0.2] no jardim de oito por oito cabem *quatro* jardins de quatro por quatro. [p=0.4] {xc}A C fez regra de "
        "três com o lado. [p=0.2] {xa}A A usou inversa. [p=0.2] {xb}A B achou que nada muda. [p=0.2] {xe}E a E elevou "
        "ao cubo, [p=0.2] como se fosse volume."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="29", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta,* "
        "sem consultar nada. [p=0.4] {b}Montar a razão na ordem certa [p=0.2] e conhecer as razões "
        "do dia a dia: [p=0.2] episódio um. [p=0.3] {c}Propriedade fundamental [p=0.2] e truque do k: [p=0.2] episódio "
        "dois. [p=0.3] {d}Teste do dobro [p=0.2] e unidades padronizadas: [p=0.2] episódio três."),
    dict(id="30", block="checklist", text=
        "{a}Regra de três composta [p=0.2] e o atalho dos homens-hora: [p=0.2] episódio quatro. [p=0.3] {b}Quando a regra "
        "de três não vale, [p=0.2] conferir o sentido [p=0.2] e reduzir ao valor unitário: [p=0.2] episódio cinco. "
        "[p=0.3] {c}Velocidade e escalas: [p=0.2] nas "
        "*séries próprias.* [p=0.4] {d}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="31", block="meta", text=
        "{t}A meta, [p=0.2] maior que a de costume. [p=0.3] {a}Como este é o "
        "assunto que *mais cai,* [p=0.2] resolva *quarenta* questões, [p=0.2] e não trinta, [p=0.2] {b}e acerte pelo "
        "menos *vinte e oito,* [p=0.2] setenta por cento. [p=0.4] {c}Inclua questões de *Física* e de *Química:* [p=0.2] "
        "lá a regra de três aparece com outra roupa."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}O próximo assunto é *Grandezas proporcionais,* [p=0.3] {b}onde a direta e a inversa ganham *gráfico,* [p=0.2] "
        "*tabela* [p=0.2] e *constante.*"),
    dict(id="33", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das nove frases você acertou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de razão, proporção e regra de três está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
