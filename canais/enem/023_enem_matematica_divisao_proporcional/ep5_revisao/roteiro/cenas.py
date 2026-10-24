# Roteiro — Divisão Proporcional, Episódio 5 de 5: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/08-divisao-proporcional.html — seções 01, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 PACOTINHOS: some os pesos, divida o total, multiplique cada peso; o k é o valor de um pacotinho ·
#   ep2 vire a FRAÇÃO, não a FILA; o MMC tira as frações do caminho · ep3 PESSOA-DIA e o retângulo de quadradinhos;
#   na sociedade, capital vezes tempo · ep4 a parte fixa é a BANDEIRADA (separe antes, devolva depois); FECHAR O CAIXA.
# Treino-relâmpago (só os pesos): prêmio pelos pontos 20, 30, 50 → 2 : 3 : 5 · inversamente às faltas 1, 2, 4 →
#   inversos × 4 → 4 : 2 : 1 · 2 e 3 pessoas por 5 e 4 dias → 10 e 12 → 5 : 6 · R$ 1 000 fixos para cada e o resto
#   proporcional a 1 e 2 → separa o fixo; os pesos 1 : 2 valem só sobre o resto.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (inversamente a 2, 3, 4 → pesos 2, 3, 4) · 2 F (inversamente a 2, 3, 4 → pesos 4, 3, 2) ·
#   3 V (5 pessoas por 2 dias = peso 10, não 7) · 4 F (R$ 3 600 em 2 : 3 : 4 → cada um 3 600 ÷ 3) ·
#   5 F (com R$ 1 000 fixos para cada, a proporção vale sobre o total) · 6 V (k não exato: mantenha como fração até o fim) ·
#   7 F (calculou todas as partes certas, não tem como errar a questão) ·
#   8 F (na composta, simplifique só as pessoas e use como peso; é preciso multiplicar primeiro) ·
#   9 V (conferir a soma das partes pega erro de k, de peso ou de método).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (direta, DIFERENÇA) R$ 18 000 entre turmas de 24, 30, 36 alunos → ÷ 6: 4 : 5 : 6 → k = 1 200 → 4 800, 6 000, 7 200;
#      diferença (6 − 4) · 1 200 = 2 400 → B. A 1 200 (parou no k) · C 4 800 (menor parte) · D 6 000 (dividiu pelo número
#      de turmas) · E 7 200 (maior parte).
#   Q2 (inversa) bônus R$ 4 000 inversamente a 3, 4, 12 reclamações → MMC 12 → 4 : 3 : 1 → k = 500 → 2 000, 1 500, 500;
#      a de 3 reclamações → D (2 000). A 500 (trocou quem leva mais) · B 631,58 (usou 3, 4, 12 como pesos) ·
#      C 1 333,33 (partes iguais) · E 2 526,32 (inverteu a ORDEM: 12, 4, 3).
#   Q3 (composta, série inversa) R$ 9 000; integrantes 2, 3, 4 e INVERSAMENTE às faltas 1, 2, 4 → inversos × 4 = 4, 2, 1
#      → produtos 8, 6, 4 → 4 : 3 : 2 → k = 1 000 → 4 000, 3 000, 2 000; a equipe de 4 → A (2 000).
#      B 3 000 (partes iguais) · C 4 000 (só os integrantes) · D 4 500 (SOMOU as séries: 3, 5, 8) ·
#      E 6 000 (multiplicou sem inverter as faltas: 2, 6, 16).
#   Q4 (sociedade, capital × tempo) A 12 mil × 10, B 15 mil × 10, C 18 mil × 5; lucro R$ 30 000 → 120, 150, 90 → 4 : 5 : 3
#      → k = 2 500 → 10 000, 12 500, 7 500; sócio C → B (7 500). A 6 000 (só o tempo) · C 10 000 (partes iguais) ·
#      D 12 000 (só o capital) · E 12 500 (a parte do sócio B).
#   Q5 (parte fixa) R$ 12 000; R$ 2 000 fixos para cada; resto 6 000 em 1 : 3 : 4 → k = 750 → 750, 2 250, 3 000;
#      o de peso 4 recebe 2 000 + 3 000 = 5 000 → C. A 2 750 (a parte do peso 1) · B 3 000 (esqueceu de devolver o fixo) ·
#      D 6 000 (proporção sobre o total) · E 8 000 (sobre o total e ainda somou o fixo).
# Checklist (seção 13, 13 itens) → episódio: k pela soma dos pesos, por que funciona, MDC, total pela parte, diferença: ep1 ·
#   inversa com MMC, valor e não ordem: ep2 · composta multiplica, sociedade com capital e capital × tempo: ep3 ·
#   parte fixa e as três conferências (soma, ordem, reler): ep4.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), priorizando inversa e composta.
# Ponte (do usuário): Porcentagem.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de divisão proporcional: treino, 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 5"

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
        "{a}Este assunto é de *procedimento:* [p=0.3] um caminho único resolve todos os casos. [p=0.4] {b}A dificuldade "
        "não está na conta, [p=0.3] está em decidir *quais são os pesos.* [p=0.4] {c}Hoje, [p=0.2] um treino, [p=0.2] "
        "nove frases [p=0.2] e cinco questões novas."),

    # ================= OS CONTEXTOS DA PROVA (seção 01) =================
    dict(id="02", block="contextos", text=
        "{t}E onde isso aparece na prova? [p=0.3] Sempre nos mesmos lugares. [p=0.3] {a}*Sociedade e lucro:* [p=0.2] "
        "sócios que investiram valores diferentes. [p=0.3] {b}*Rateio de despesas:* [p=0.2] a conta de luz, [p=0.2] o "
        "condomínio, [p=0.2] a viagem entre amigos. [p=0.3] {c}*Verbas* [p=0.2] entre setores ou escolas. [p=0.3] "
        "{d}*Herança* entre herdeiros. [p=0.3] {e}E *premiação* por desempenho."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] os *pacotinhos.* [p=0.2] Some os "
        "pesos, [p=0.2] divida o total, [p=0.2] multiplique cada peso. [p=0.2] O k é o valor de *um* pacotinho. [p=0.4] "
        "{b}Dois: [p=0.2] na inversa, [p=0.2] vire a *fração,* [p=0.2] não a fila. [p=0.2] E o MMC tira as frações do "
        "caminho."),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] dois critérios se *multiplicam.* [p=0.2] Cinco pessoas por dois dias [p=0.2] são dez "
        "pessoa-dia, [p=0.2] como um retângulo de quadradinhos. [p=0.2] E na sociedade, [p=0.2] quem manda é capital "
        "vezes tempo. [p=0.4] {b}E quatro: [p=0.2] a parte fixa é a *bandeirada:* [p=0.2] separe antes, [p=0.2] devolva "
        "depois. [p=0.2] E no fim, [p=0.2] *feche o caixa.*"),

    # ================= O QUE MAIS RENDE + TREINO-RELÂMPAGO =================
    dict(id="05", block="rendem", text=
        "{t}E se você só tiver tempo para duas coisas? [p=0.4] {a}Primeiro: [p=0.2] o *atalho do MMC* na divisão "
        "inversa. [p=0.4] {b}Segundo: [p=0.2] *multiplicar* na composta, [p=0.2] porque o instinto manda somar."),
    dict(id="06", block="treino", text=
        "{t}Treino-relâmpago. [p=0.3] Só os *pesos,* [p=0.2] sem terminar a conta. [p=0.4] {b}Um: [p=0.2] um prêmio "
        "proporcional aos pontos vinte, [p=0.2] trinta [p=0.2] e cinquenta. [p=0.3] {c}Dois: [p=0.2] um bônus "
        "inversamente proporcional às faltas: [p=0.2] uma, [p=0.2] duas [p=0.2] e quatro. [p=0.3] {d}Três: [p=0.2] duas "
        "equipes, [p=0.2] com duas e três pessoas, [p=0.2] que trabalharam cinco e quatro dias. [p=0.3] {e}Quatro: "
        "[p=0.2] mil reais fixos para cada um, [p=0.2] e o resto proporcional a um e dois. [p=0.4] {p}*Pause e monte os "
        "pesos.* [p=2.0]"),
    dict(id="07", block="treino", text=
        "{t}Conferindo! [p=0.3] {a}Um: [p=0.2] dividindo por dez, [p=0.2] *dois, três e cinco.* [p=0.3] {b}Dois: "
        "[p=0.2] os inversos, [p=0.2] vezes quatro: [p=0.2] *quatro, dois e um.* [p=0.3] {c}Três: [p=0.2] multiplique: "
        "[p=0.2] dez e doze, [p=0.2] ou *cinco e seis.* [p=0.3] {d}E quatro: [p=0.2] primeiro *separe o fixo.* [p=0.2] "
        "O um e o dois valem só sobre o resto."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] para dividir *inversamente* a dois, três e quatro, [p=0.2] os pesos são dois, três e quatro. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque são os números do enunciado. [p=0.3] {g}Mas aí "
        "quem tem o maior número leva mais. [p=0.2] Use os *inversos:* [p=0.2] seis, quatro e três."),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] para dividir inversamente a dois, três e quatro, [p=0.2] os pesos são quatro, três e dois. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o menor passa a levar mais. [p=0.3] {g}Mas virar "
        "a *fila* não é virar a *fração.* [p=0.2] Um meio, um terço e um quarto, [p=0.2] vezes doze: [p=0.2] seis, "
        "quatro e três."),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] na divisão composta, [p=0.2] uma equipe de cinco pessoas por dois dias [p=0.2] tem peso *dez,* "
        "[p=0.2] e não sete. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque somar parece mais "
        "natural. [p=0.3] {g}Mas é um retângulo: [p=0.2] cinco por dois, [p=0.2] *dez* quadradinhos de trabalho."),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] para dividir três mil e seiscentos reais em dois, três e quatro, [p=0.2] cada pessoa recebe "
        "três mil e seiscentos dividido por *três.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque são "
        "três pessoas. [p=0.3] {g}Mas são *nove* pacotinhos. [p=0.2] Divida pela *soma dos pesos.*"),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] se cada um recebe mil reais fixos [p=0.2] e o resto é proporcional, [p=0.2] a proporção vale "
        "sobre o *total.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o total é o número que aparece. "
        "[p=0.3] {g}Mas a proporção vale só sobre o *resto.* [p=0.2] Separe o fixo antes, [p=0.2] e devolva no fim."),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] se o k não der exato, [p=0.2] mantenha ele como *fração* até o fim. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque arredondar parece mais prático. [p=0.3] {g}Mas o arredondamento "
        "faz a soma das partes *não fechar* com o total."),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] se você calculou todas as partes certinho, [p=0.2] não tem como errar a questão. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a conta está perfeita. [p=0.3] {g}Mas a questão pode "
        "pedir a menor parte, [p=0.2] a do segundo sócio [p=0.2] ou a *diferença.* [p=0.2] *Releia* o que foi pedido."),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] na composta, [p=0.2] dá para simplificar só as *pessoas* [p=0.2] e usar o resultado como peso. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque simplificar sempre ajuda. [p=0.3] {g}Mas assim "
        "os dias ficam pelo caminho. [p=0.2] *Multiplique primeiro,* [p=0.2] e simplifique os pesos finais."),
    dict(id="17", block="vf", text=
        "{t}E nove: [p=0.2] conferir a soma das partes pega erro de k, [p=0.2] de peso [p=0.2] ou de método. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque parece só uma conferência. [p=0.3] {g}Mas se "
        "o caixa não fecha, [p=0.2] alguma coisa deu errado, [p=0.2] e ainda dá tempo de refazer."),
    dict(id="18", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM."),

    # ================= QUESTÃO 1: DIRETA, A DIFERENÇA =================
    dict(id="19", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma escola vai dividir *dezoito mil reais* entre três turmas, [p=0.2] em partes "
        "diretamente proporcionais ao número de alunos: [p=0.2] vinte e quatro, [p=0.2] trinta [p=0.2] e trinta e seis. "
        "[p=0.3] {b}Qual é a *diferença* entre a maior e a menor parte? [p=0.4] {la}A, [p=0.2] mil e duzentos reais. "
        "[p=0.2] {lb}B, [p=0.2] dois mil e quatrocentos. [p=0.2] {lc}C, [p=0.2] quatro mil e oitocentos. [p=0.2] {ld}D, "
        "[p=0.2] seis mil. [p=0.2] {le}E, [p=0.2] sete mil e duzentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q1", text=
        "{d}Sublinhe o pedido: [p=0.2] a *diferença.* [p=0.3] {a}Simplifique os pesos por seis: [p=0.2] quatro, cinco e "
        "seis. [p=0.2] Soma quinze. [p=0.3] {b}O k é dezoito mil dividido por quinze: [p=0.2] *mil e duzentos.* [p=0.3] "
        "{c}Diferença dos pesos, [p=0.2] seis menos quatro, [p=0.2] dois. [p=0.2] Dois vezes mil e duzentos: [p=0.2] *dois "
        "mil e quatrocentos.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}O caixa fecha: [p=0.2] quatro mil e oitocentos, [p=0.2] "
        "seis mil [p=0.2] e sete mil e duzentos [p=0.2] somam dezoito mil. [p=0.4] {xc}A C e a E são partes, [p=0.2] "
        "{xe}não a diferença. [p=0.2] {xa}A A parou no k. [p=0.2] {xd}E a D dividiu pelo número de turmas."),

    # ================= QUESTÃO 2: INVERSA =================
    dict(id="21", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um bônus de *quatro mil reais* será dividido entre três atendentes, [p=0.2] em "
        "partes *inversamente* proporcionais ao número de reclamações do mês: [p=0.2] três, [p=0.2] quatro [p=0.2] e doze. "
        "[p=0.3] {b}Quanto recebe a atendente com *três* reclamações? [p=0.4] {la}A, [p=0.2] quinhentos reais. [p=0.2] "
        "{lb}B, [p=0.2] seiscentos e trinta e um e cinquenta e oito. [p=0.2] {lc}C, [p=0.2] mil trezentos e trinta e "
        "três e trinta e três. [p=0.2] {ld}D, [p=0.2] dois mil. [p=0.2] {le}E, [p=0.2] dois mil quinhentos e vinte e "
        "seis e trinta e dois. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{d}Menos reclamação, [p=0.2] mais bônus: [p=0.2] *inversa.* [p=0.3] {a}Vire as frações: [p=0.2] um terço, "
        "[p=0.2] um quarto, [p=0.2] um doze avos. [p=0.2] Vezes doze, [p=0.2] o MMC: [p=0.2] *quatro, três e um.* [p=0.3] "
        "{b}Soma oito. [p=0.2] O k é quatro mil dividido por oito: [p=0.2] quinhentos. [p=0.3] {c}Quatro vezes "
        "quinhentos: [p=0.2] *dois mil.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Caixa: [p=0.2] dois mil, [p=0.2] mil e "
        "quinhentos [p=0.2] e quinhentos [p=0.2] fecham quatro mil. [p=0.2] E quem reclamou menos levou mais. [p=0.4] "
        "{xb}A B usou os próprios números, [p=0.2] {xe}e a E virou a fila: [p=0.2] repare nos números quebrados. [p=0.2] "
        "{xc}A C dividiu igual. [p=0.2] {xa}E a A deu o bônus de quem reclamou mais."),

    # ================= QUESTÃO 3: COMPOSTA COM SÉRIE INVERSA =================
    dict(id="23", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um prêmio de *nove mil reais* será dividido entre três equipes, [p=0.2] "
        "diretamente proporcional ao número de integrantes, [p=0.2] dois, três e quatro, [p=0.3] {b}e *inversamente* "
        "proporcional ao número de faltas da equipe, [p=0.2] uma, duas e quatro. [p=0.3] {c}Quanto recebe a equipe de "
        "*quatro* integrantes? [p=0.4] {la}A, [p=0.2] dois mil reais. [p=0.2] {lb}B, [p=0.2] três mil. [p=0.2] {lc}C, "
        "[p=0.2] quatro mil. [p=0.2] {ld}D, [p=0.2] quatro mil e quinhentos. [p=0.2] {le}E, [p=0.2] seis mil. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q3", text=
        "{d}Dois critérios, [p=0.2] e um deles é inverso. [p=0.3] {a}*Antes* de multiplicar, [p=0.2] inverta as faltas: "
        "[p=0.2] vezes quatro, [p=0.2] viram quatro, dois e um. [p=0.3] {b}Agora multiplique: [p=0.2] dois vezes quatro, "
        "oito. [p=0.2] Três vezes dois, seis. [p=0.2] Quatro vezes um, quatro. [p=0.3] {c}Simplificando: [p=0.2] quatro, "
        "três e dois. [p=0.2] O k é mil. [p=0.2] A equipe de quatro leva *dois mil.* [p=0.2] {ok}*Letra A!* [p=0.3] "
        "{v}Faz sentido: [p=0.2] a maior equipe faltou mais. [p=0.4] {xd}A D *somou* as séries. [p=0.2] {xe}A E "
        "multiplicou sem inverter. [p=0.2] {xc}A C só olhou os integrantes. [p=0.2] {xb}E a B dividiu igual."),

    # ================= QUESTÃO 4: SOCIEDADE, CAPITAL × TEMPO =================
    dict(id="25", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Três sócios dividem um lucro de *trinta mil reais.* [p=0.3] {b}O sócio A investiu "
        "doze mil, [p=0.2] por dez meses. [p=0.2] O B, [p=0.2] quinze mil, [p=0.2] por dez meses. [p=0.2] E o C, "
        "[p=0.2] dezoito mil, [p=0.2] por *cinco* meses. [p=0.3] {c}Dividindo pelo capital e pelo tempo, [p=0.2] quanto "
        "recebe o sócio C? [p=0.4] {la}A, [p=0.2] seis mil reais. [p=0.2] {lb}B, [p=0.2] sete mil e quinhentos. [p=0.2] "
        "{lc}C, [p=0.2] dez mil. [p=0.2] {ld}D, [p=0.2] doze mil. [p=0.2] {le}E, [p=0.2] doze mil e quinhentos. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{d}Capital *vezes* tempo. [p=0.3] {a}Em milhares: [p=0.2] doze vezes dez, [p=0.2] cento e vinte. [p=0.2] Quinze "
        "vezes dez, [p=0.2] cento e cinquenta. [p=0.2] Dezoito vezes cinco, [p=0.2] noventa. [p=0.3] {b}Dividindo por "
        "trinta: [p=0.2] quatro, cinco e três. [p=0.2] O k é dois mil e quinhentos. [p=0.3] {c}O sócio C: [p=0.2] três "
        "vezes dois mil e quinhentos, [p=0.2] *sete mil e quinhentos.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Repare: [p=0.2] "
        "o maior capital levou a *menor* parte. [p=0.2] Quem manda é o produto. [p=0.4] {xd}A D só olhou o capital. "
        "[p=0.2] {xa}A A, [p=0.2] só o tempo. [p=0.2] {xc}A C dividiu igual. [p=0.2] {xe}E a E respondeu a parte do B."),

    # ================= QUESTÃO 5: PARTE FIXA =================
    dict(id="27", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um prêmio de *doze mil reais* vai para três finalistas. [p=0.3] {b}Cada um "
        "recebe *dois mil* fixos, [p=0.2] e o restante é dividido em partes proporcionais às notas um, três e quatro. "
        "[p=0.3] {c}Quanto recebe, no total, [p=0.2] o finalista de nota *quatro?* [p=0.4] {la}A, [p=0.2] dois mil "
        "setecentos e cinquenta reais. [p=0.2] {lb}B, [p=0.2] três mil. [p=0.2] {lc}C, [p=0.2] cinco mil. [p=0.2] "
        "{ld}D, [p=0.2] seis mil. [p=0.2] {le}E, [p=0.2] oito mil. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{d}Parte fixa: [p=0.2] a bandeirada. [p=0.3] {a}Separe: [p=0.2] três vezes dois mil, [p=0.2] seis mil. [p=0.2] "
        "Sobram *seis mil* para dividir. [p=0.3] {b}Pesos um, três e quatro, [p=0.2] soma oito. [p=0.2] O k é setecentos "
        "e cinquenta. [p=0.2] Quatro vezes setecentos e cinquenta, [p=0.2] três mil. [p=0.3] {c}Agora *devolva* o "
        "fixo: [p=0.2] dois mil mais três mil, [p=0.2] *cinco mil.* [p=0.2] {ok}*Letra C!* [p=0.4] {xb}A B esqueceu de "
        "devolver o fixo. [p=0.2] {xd}A D aplicou a proporção sobre o total. [p=0.2] {xe}A E fez isso e ainda somou o "
        "fixo. [p=0.2] {xa}E a A respondeu a parte do finalista de nota um."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="29", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Achar o k pela soma dos pesos, [p=0.2] simplificar "
        "pelo MDC, [p=0.2] achar o total por uma parte [p=0.2] e a diferença entre partes: [p=0.2] episódio um. [p=0.3] "
        "{c}Inversa com o MMC, [p=0.2] invertendo o valor e não a ordem: [p=0.2] episódio dois."),
    dict(id="30", block="checklist", text=
        "{a}Composta multiplicando, [p=0.2] e sociedade com capital e com capital vezes tempo: [p=0.2] episódio três. "
        "[p=0.3] {b}Parte fixa [p=0.2] e as três conferências, [p=0.2] soma, [p=0.2] ordem [p=0.2] e reler o pedido: "
        "[p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="31", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta* questões [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}Priorize a divisão *inversa* [p=0.2] e a *composta:* [p=0.2] são as duas em que o "
        "caminho do instinto leva à alternativa errada."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}O próximo assunto é *Porcentagem,* [p=0.3] {b}e tudo o que você aprendeu de razão e proporção [p=0.2] vai "
        "virar a ferramenta para *aumentos,* [p=0.2] *descontos* [p=0.2] e *juros.*"),
    dict(id="33", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual questão te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de divisão proporcional está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
