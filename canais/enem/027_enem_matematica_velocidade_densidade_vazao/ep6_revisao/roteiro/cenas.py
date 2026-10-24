# Roteiro — Velocidade, Densidade e Vazão, Episódio 6 de 6: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material) nem a questão do atleta. As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter). Ponte: frase do usuário, IDÊNTICA.
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a BARRA da unidade é um sinal de dividir · a taxa é como o PREÇO DO QUILO ·
#   ep2 o RITMO CONSTANTE imaginário · o CRONÔMETRO NÃO PARA NO POSTO · o RELÓGIO conta de 60 em 60 ·
#   ep3 QUEM MANDA NA MÉDIA É O RELÓGIO · a DISTÂNCIA AMIGA · ep4 a densidade como IMPRESSÃO DIGITAL · a ÁGUA COMO RÉGUA ·
#   ep5 os PEDAÇOS DO TANQUE · torneiras como TIME e o ralo como SABOTADOR.
#   (O ep5 foi escrito em paralelo: frases tiradas do prompt do vídeo 5.)
# O que a prova cobra (seção 01): velocidade média + armadilha · densidade (material, flutuação, g/cm³ ↔ kg/m³) ·
#   vazão (torneiras somam, ralos subtraem) · outras taxas do mesmo formato.
# Onde aparece (seção 09): Física · Química · Biologia · Geografia. "O mesmo conteúdo com outra roupa."
# Estratégia (seção 10): unidade ao lado do número · padronizar antes de dividir · conferir com valores de referência.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (ida 60, volta 40: média 50; é 48) · 2 V (a parada entra no tempo total) · 3 F (2,5 h = 2 h 50 min; é 2 h 30) ·
#   4 F (20 m/s é mais devagar que 60 km/h; 20 m/s = 72 km/h) · 5 V (0,9 g/cm³ = 900 kg/m³) ·
#   6 F (torneira 4 h e ralo 6 h: vazão 1/4 + 1/6; é 1/4 − 1/6 = 1/12, 12 h) ·
#   7 F (torneiras de 2 h e 3 h juntas: 5 h; é 1/2 + 1/3 = 5/6, 1 h 12 min) ·
#   8 F (torneira de 20 L/min enche 600 L em 30 horas; são 30 minutos) · 9 V (prego e portão de ferro: mesma densidade).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (Física, viagem com parada) 70 km em 1 h · parada de 30 min · 50 km em 30 min → 120 km em 2 h = 60 km/h → B.
#      A 85 (média das velocidades 70 e 100) · C 80 (esqueceu a parada: 1,5 h) · D 75 (leu 30 min como 0,30 h: 1,6 h) ·
#      E 70 (ficou com a velocidade do primeiro trecho).
#   Q2 (Matemática, ida e volta) 180 km para cada lado, ida a 90, volta a 60 → 2 h + 3 h = 5 h; 360 ÷ 5 = 72 km/h → D.
#      Abaixo da média simples (75) ✓. A 36 (esqueceu a volta: 180 ÷ 5) · B 75 (média simples) · C 150 (somou as
#      velocidades) · E 60 (achou que o trecho lento manda sozinho). Fórmula de distâncias iguais: 2 · 90 · 60 ÷ 150 = 72.
#   Q3 (Química, densidade) bloco de 600 g e 750 cm³ → 0,8 g/cm³ → boia; 800 kg/m³ → A.
#      B boia, 0,8 kg/m³ (esqueceu o fator 1 000) · C afunda, 1 250 kg/m³ (dividiu volume por massa) ·
#      D afunda, 800 kg/m³ (comparou 800 com o 1 da água, em unidades diferentes) · E boia, 80 kg/m³ (fator 100).
#   Q4 (torneira e ralo) torneira enche em 3 h, ralo esvazia em 12 h → 1/3 − 1/12 = 3/12 = 1/4 → 4 h → E. Maior que 3 h ✓.
#      A 2 h 24 min (somou a vazão do ralo: 5/12 → 2,4 h) · B 2 h 40 min (somou o ralo e ainda leu 2,4 h como 2 h 40) ·
#      C 9 h (subtraiu os tempos) · D 15 h (somou os tempos).
#   Q5 (Geografia, densidade demográfica) X: 240 000 hab em 600 km² = 400 hab/km² · Y: 90 000 hab em 15 000 ha =
#      150 km² → 600 hab/km² → C (Y, 600 hab/km²). A X, 400 contra 6 (não converteu hectare) · B X, mais habitantes
#      (comparou o total) · D Y, 60 000 hab/km² (tratou hectare como metro quadrado) · E X, 2 500 m² por habitante
#      (inverteu a razão: área por habitante, e escolheu o maior).
# Gabaritos: B, D, A, E, C.
# Checklist (seção 13, 13 itens) → episódio: mesma estrutura, unidade decide × ou ÷, valores de referência: ep1 ·
#   distância total ÷ tempo total, parada: ep2 · ida e volta ≠ média, puxa para a menor: ep3 · flutuação, fator 1 000,
#   característica do material: ep4 · frações do tanque, ralo subtrai, padronizar minutos e horas: ep5.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), incluindo Física (cinemática e hidrostática).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de velocidade, densidade e vazão: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 6"

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
        "{a}Velocidade média em *Física,* [p=0.3] {b}densidade em *Química,* [p=0.3] {c}densidade demográfica em "
        "*Geografia.* [p=0.4] {d}Na prova, [p=0.2] são três questões diferentes. [p=0.3] {e}Na sua cabeça, [p=0.2] a "
        "partir de hoje, [p=0.2] *é uma só.* [p=0.4] {f}Com nove frases de verdadeiro ou falso [p=0.2] e cinco questões "
        "novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}O que a prova cobra deste assunto? [p=0.4] {a}Um: [p=0.2] *velocidade média* em viagens com trechos "
        "diferentes, [p=0.2] e a armadilha da média. [p=0.3] {b}Dois: [p=0.2] *densidade,* [p=0.2] para descobrir o "
        "material, [p=0.2] saber se boia [p=0.2] e trocar grama por centímetro cúbico por quilo por metro cúbico. "
        "[p=0.3] {c}Três: [p=0.2] *vazão,* [p=0.2] com torneiras somando [p=0.2] e ralos subtraindo. [p=0.3] {d}E "
        "quatro: [p=0.2] *outras taxas* do mesmo formato, [p=0.2] como consumo, [p=0.2] concentração [p=0.2] e "
        "produtividade."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] a *barra* da unidade é um "
        "sinal de *dividir.* [p=0.2] Quilômetro por hora [p=0.2] é quilômetro dividido por hora. [p=0.3] E a taxa é "
        "como o *preço do quilo:* [p=0.2] comprar mais não muda o preço de cada quilo. [p=0.4] {b}Dois: [p=0.2] "
        "velocidade média é um *ritmo constante imaginário.* [p=0.2] O *cronômetro não para no posto.* [p=0.2] E o "
        "*relógio* conta de sessenta em sessenta."),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] *quem manda na média é o relógio.* [p=0.2] O trecho lento dura mais, [p=0.2] então pesa "
        "mais. [p=0.3] E a *distância amiga* deixa a conta de cabeça. [p=0.4] {b}Quatro: [p=0.2] a densidade é a "
        "*impressão digital* do material, [p=0.2] e a *água é a régua:* [p=0.2] menos de um, [p=0.2] boia; [p=0.2] "
        "mais de um, [p=0.2] afunda. [p=0.4] {c}Cinco: [p=0.2] pense em *pedaços do tanque* por hora. [p=0.2] Torneiras "
        "são um *time:* [p=0.2] o tempo diminui. [p=0.2] O ralo é um *sabotador:* [p=0.2] o tempo aumenta."),

    # ================= ONDE APARECE (seção 09) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}Na *Física:* [p=0.2] cinemática, [p=0.2] hidrostática [p=0.2] e vazão "
        "em canos. [p=0.3] {b}Na *Química:* [p=0.2] densidade de soluções [p=0.2] e concentração em grama por litro. "
        "[p=0.3] {c}Na *Biologia:* [p=0.2] taxas de natalidade e de mortalidade. [p=0.3] {d}Na *Geografia:* [p=0.2] "
        "densidade demográfica, [p=0.2] vazão de rios [p=0.2] e produtividade agrícola. [p=0.4] {e}É *o mesmo "
        "conteúdo com outra roupa:* [p=0.2] montar uma razão [p=0.2] e conferir as unidades."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 10) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] três hábitos resolvem quase tudo. [p=0.4] {a}Um: [p=0.2] escreva a *unidade* ao lado "
        "de cada número. [p=0.2] A barra já diz a conta. [p=0.3] {b}Dois: [p=0.2] *padronize as unidades* antes de "
        "dividir. [p=0.2] Litro por minuto com tempo em horas [p=0.2] é o erro silencioso. [p=0.3] {c}Três: [p=0.2] "
        "*confira com o mundo real.* [p=0.2] Um carro a quinhentos quilômetros por hora, [p=0.2] ou uma caixa-d'água "
        "de casa com cinco mil litros, [p=0.2] é sinal de unidade trocada."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] ida a sessenta, [p=0.2] volta a quarenta, [p=0.2] pelo mesmo caminho: [p=0.2] a velocidade "
        "média é *cinquenta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinquenta é a média dos "
        "dois números. [p=0.3] {g}Mas quem manda é o relógio: [p=0.2] distância total sobre tempo total, [p=0.2] "
        "*quarenta e oito.*"),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] numa viagem com parada, [p=0.2] o tempo parado *entra* na velocidade média do percurso "
        "completo. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque, parado, o carro não "
        "anda. [p=0.3] {g}Mas o *cronômetro não para no posto:* [p=0.2] todo o tempo conta."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] *dois vírgula cinco horas* [p=0.2] são duas horas e *cinquenta* minutos. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o cinco parece virar cinquenta. [p=0.3] {g}Mas o relógio conta "
        "de sessenta em sessenta: [p=0.2] meia hora, [p=0.2] *trinta minutos.*"),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] um carro a *vinte metros por segundo* [p=0.2] anda mais devagar que um a sessenta "
        "quilômetros por hora. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque vinte é menor que "
        "sessenta. [p=0.3] {g}Mas as unidades são diferentes. [p=0.2] Vinte vezes três vírgula seis: [p=0.2] "
        "*setenta e dois quilômetros por hora.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] zero vírgula nove grama por centímetro cúbico [p=0.2] é o mesmo que *novecentos quilos "
        "por metro cúbico.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque os números são "
        "muito diferentes. [p=0.3] {g}Mas de grama por centímetro cúbico para quilo por metro cúbico, [p=0.2] "
        "multiplica por *mil.*"),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] uma torneira enche um tanque em quatro horas, [p=0.2] e um ralo esvazia em seis. [p=0.2] "
        "Juntos, [p=0.2] eles enchem *um quarto mais um sexto* por hora. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque, em torneiras, a gente soma. [p=0.3] {g}Mas o ralo é *sabotador:* [p=0.2] um quarto "
        "*menos* um sexto, [p=0.2] um doze avos. [p=0.2] Doze horas, [p=0.2] mais que quatro."),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] duas torneiras enchem um tanque, [p=0.2] sozinhas, [p=0.2] em duas e em três horas. [p=0.2] "
        "Juntas, [p=0.2] enchem em *cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque somar "
        "parece juntar. [p=0.3] {g}Mas o time *acelera:* [p=0.2] some os pedaços, [p=0.2] não os tempos. [p=0.2] Um "
        "meio mais um terço, [p=0.2] cinco sextos. [p=0.2] Uma hora e *doze minutos.*"),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] uma torneira de *vinte litros por minuto* [p=0.2] enche seiscentos litros [p=0.2] em *trinta "
        "horas.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque seiscentos dividido por vinte [p=0.2] "
        "dá mesmo trinta. [p=0.3] {g}Mas a vazão é *por minuto:* [p=0.2] são *trinta minutos.* [p=0.2] Padronize "
        "antes de dividir."),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] um *prego* e um *portão* de ferro [p=0.2] têm a mesma densidade. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o portão é muito mais pesado. [p=0.3] {g}Mas também tem muito "
        "mais volume. [p=0.2] A densidade é a *impressão digital* do material."),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as "
        "cinco questões, [p=0.2] todas inéditas, [p=0.2] de Física, [p=0.2] Matemática, [p=0.2] Química [p=0.2] e "
        "Geografia. [p=0.2] Em todas, [p=0.2] escreva a *unidade* ao lado de cada número."),

    # ================= QUESTÃO 1: VIAGEM COM PARADA =================
    dict(id="18", block="q1", text=
        "{t}Questão um, [p=0.2] de Física. [p=0.3] {a}Um carro anda *setenta quilômetros* em *uma hora,* [p=0.2] para "
        "*trinta minutos* num posto [p=0.2] e anda mais *cinquenta quilômetros* em *trinta minutos.* [p=0.3] {b}A "
        "velocidade média no percurso completo, [p=0.2] em quilômetros por hora, [p=0.2] é [p=0.4] {la}A, [p=0.2] "
        "oitenta e cinco. [p=0.2] {lb}B, [p=0.2] sessenta. [p=0.2] {lc}C, [p=0.2] oitenta. [p=0.2] {ld}D, [p=0.2] "
        "setenta e cinco. [p=0.2] {le}E, [p=0.2] setenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}Distância total sobre tempo total. [p=0.3] {a}Distância: [p=0.2] setenta mais cinquenta, [p=0.2] *cento e "
        "vinte quilômetros.* [p=0.3] {b}Tempo: [p=0.2] uma hora, [p=0.2] mais meia hora parado, [p=0.2] mais meia "
        "hora: [p=0.2] *duas horas.* [p=0.3] {c}Cento e vinte dividido por dois: [p=0.2] *sessenta.* [p=0.2] {ok}*Letra "
        "B!* [p=0.4] {xc}A C esqueceu a parada. [p=0.2] {xd}A D leu trinta minutos como zero vírgula três hora. "
        "[p=0.2] {xa}A A fez a média das velocidades, [p=0.2] {xe}e a E ficou com o primeiro trecho."),

    # ================= QUESTÃO 2: IDA E VOLTA =================
    dict(id="20", block="q2", text=
        "{t}Questão dois, [p=0.2] de Matemática. [p=0.3] {a}Um ônibus vai de uma cidade a outra, [p=0.2] a *cento e "
        "oitenta quilômetros,* [p=0.2] a *noventa* quilômetros por hora, [p=0.2] e volta pelo mesmo caminho a "
        "*sessenta.* [p=0.3] {b}A velocidade média na ida e volta, [p=0.2] em quilômetros por hora, [p=0.2] é [p=0.4] "
        "{la}A, [p=0.2] trinta e seis. [p=0.2] {lb}B, [p=0.2] setenta e cinco. [p=0.2] {lc}C, [p=0.2] cento e "
        "cinquenta. [p=0.2] {ld}D, [p=0.2] setenta e dois. [p=0.2] {le}E, [p=0.2] sessenta. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}Quem manda é o relógio. [p=0.3] {a}Ida: [p=0.2] cento e oitenta dividido por noventa, [p=0.2] *duas "
        "horas.* [p=0.2] Volta: [p=0.2] cento e oitenta dividido por sessenta, [p=0.2] *três horas.* [p=0.3] {b}Trezentos "
        "e sessenta quilômetros em cinco horas: [p=0.2] *setenta e dois.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Confere: "
        "[p=0.2] ficou abaixo de setenta e cinco, [p=0.2] puxada para a velocidade menor. [p=0.4] {xb}A B é a média "
        "simples. [p=0.2] {xa}A A esqueceu a volta. [p=0.2] {xc}A C somou as velocidades, [p=0.2] {xe}e a E achou que "
        "o trecho lento manda sozinho."),

    # ================= QUESTÃO 3: DENSIDADE =================
    dict(id="22", block="q3", text=
        "{t}Questão três, [p=0.2] de Química. [p=0.3] {a}Um bloco maciço tem massa de *seiscentos gramas* [p=0.2] e "
        "volume de *setecentos e cinquenta centímetros cúbicos.* [p=0.3] {b}Colocado na água, [p=0.2] o bloco, "
        "[p=0.2] e a sua densidade, [p=0.2] são [p=0.4] {la}A, [p=0.2] boia; [p=0.2] oitocentos quilos por metro "
        "cúbico. [p=0.2] {lb}B, [p=0.2] boia; [p=0.2] zero vírgula oito quilo por metro cúbico. [p=0.2] {lc}C, "
        "[p=0.2] afunda; [p=0.2] mil duzentos e cinquenta. [p=0.2] {ld}D, [p=0.2] afunda; [p=0.2] oitocentos. "
        "[p=0.2] {le}E, [p=0.2] boia; [p=0.2] oitenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}Densidade é massa sobre volume. [p=0.3] {a}Seiscentos sobre setecentos e cinquenta: [p=0.2] *zero vírgula "
        "oito grama por centímetro cúbico.* [p=0.3] {b}A água é a régua: [p=0.2] menor que um, [p=0.2] *boia.* "
        "[p=0.2] Vezes mil: [p=0.2] *oitocentos quilos por metro cúbico.* [p=0.2] {ok}*Letra A!* [p=0.4] {xd}A D "
        "comparou oitocentos com o um da água, [p=0.2] em unidades diferentes. [p=0.2] {xb}A B esqueceu o fator mil, "
        "[p=0.2] {xe}a E usou cem, [p=0.2] {xc}e a C dividiu ao contrário."),

    # ================= QUESTÃO 4: TORNEIRA E RALO =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro, [p=0.2] a do tanque. [p=0.3] {a}Uma torneira enche um tanque em *três horas.* [p=0.2] O "
        "ralo, [p=0.2] sozinho, [p=0.2] esvazia o tanque cheio em *doze horas.* [p=0.3] {b}Com o tanque vazio e os "
        "dois abertos, [p=0.2] ele enche em [p=0.4] {la}A, [p=0.2] duas horas e vinte e quatro minutos. [p=0.2] "
        "{lb}B, [p=0.2] duas horas e quarenta minutos. [p=0.2] {lc}C, [p=0.2] nove horas. [p=0.2] {ld}D, [p=0.2] "
        "quinze horas. [p=0.2] {le}E, [p=0.2] quatro horas. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}Pedaços do tanque por hora. [p=0.3] {a}A torneira enche *um terço* por hora; [p=0.2] o ralo tira *um "
        "doze avos.* [p=0.3] {b}Um terço é quatro doze avos. [p=0.2] Menos um: [p=0.2] *três doze avos,* [p=0.2] "
        "*um quarto* por hora. [p=0.2] Quatro horas. [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confere: [p=0.2] mais que "
        "três horas. [p=0.2] O sabotador atrasou. [p=0.4] {xa}A A somou o ralo, [p=0.2] {xb}e a B ainda leu dois "
        "vírgula quatro horas como duas e quarenta. [p=0.2] {xc}A C e a D [p=0.2] {xd}subtraíram e somaram os "
        "tempos."),

    # ================= QUESTÃO 5: DENSIDADE DEMOGRÁFICA =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco, [p=0.2] de Geografia. [p=0.3] {a}O município *X* tem duzentos e quarenta mil habitantes "
        "[p=0.2] em seiscentos quilômetros quadrados. [p=0.2] O município *Y* tem noventa mil habitantes [p=0.2] em "
        "*quinze mil hectares.* [p=0.2] Lembre: [p=0.2] um quilômetro quadrado tem *cem hectares.* [p=0.3] {b}A maior "
        "densidade demográfica é a de [p=0.4] {la}A, [p=0.2] X: [p=0.2] quatrocentos, contra seis. [p=0.2] {lb}B, "
        "[p=0.2] X, [p=0.2] porque tem mais habitantes. [p=0.2] {lc}C, [p=0.2] Y: [p=0.2] seiscentos habitantes por "
        "quilômetro quadrado. [p=0.2] {ld}D, [p=0.2] Y: [p=0.2] sessenta mil por quilômetro quadrado. [p=0.2] {le}E, "
        "[p=0.2] X: [p=0.2] dois mil e quinhentos metros quadrados por habitante. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}Compare pela *taxa,* [p=0.2] não pelo total. [p=0.3] {a}X: [p=0.2] duzentos e quarenta mil sobre "
        "seiscentos, [p=0.2] *quatrocentos habitantes por quilômetro quadrado.* [p=0.3] {b}Y: [p=0.2] primeiro, "
        "padronize. [p=0.2] Quinze mil hectares [p=0.2] são *cento e cinquenta quilômetros quadrados.* [p=0.2] Noventa "
        "mil sobre cento e cinquenta: [p=0.2] *seiscentos.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A não converteu os "
        "hectares. [p=0.2] {xb}A B comparou o total. [p=0.2] {xd}A D tratou hectare como metro quadrado, [p=0.2] "
        "{xe}e a E inverteu a razão."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}A mesma estrutura, [p=0.2] a unidade decidindo a "
        "conta [p=0.2] e os valores de referência: [p=0.2] episódio um. [p=0.3] {c}Distância total sobre tempo total, "
        "[p=0.2] e a parada: [p=0.2] episódio dois. [p=0.3] {d}Ida e volta, [p=0.2] puxando para a menor: [p=0.2] "
        "episódio três."),
    dict(id="29", block="checklist", text=
        "{a}Flutuação, [p=0.2] o fator mil [p=0.2] e a impressão digital: [p=0.2] episódio quatro. [p=0.3] {b}Pedaços "
        "do tanque, [p=0.2] o ralo que atrasa [p=0.2] e minutos com horas: [p=0.2] episódio cinco. [p=0.4] {c}O que "
        "você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E inclua questões de *Física,* [p=0.2] de cinemática e de hidrostática: [p=0.2] "
        "é o mesmo conteúdo com outra roupa."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Com este assunto, [p=0.2] fechamos o bloco de *Matemática Básica e Proporcionalidade,* [p=0.2] das "
        "operações às taxas. [p=0.4] {b}Vale uma revisão misturando os *doze temas,* [p=0.2] porque a prova não avisa "
        "de qual assunto é cada questão. [p=0.4] {c}O próximo assunto é *Juros simples,* [p=0.2] que abre a "
        "*Matemática Financeira.*"),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de velocidade, densidade e vazão está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
