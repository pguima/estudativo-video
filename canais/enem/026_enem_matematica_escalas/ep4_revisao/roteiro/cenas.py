# Roteiro — Escalas, Plantas e Mapas, Episódio 4 de 4: Revisão geral, estratégia de prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/11-escalas-plantas-mapas.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o mapa como FOTO ENCOLHIDA (cada 1 cm guarda n cm) · do mapa para o mundo multiplica, do mundo para o mapa divide ·
#   o ATALHO DOS 5 ZEROS (tesoura) · ep2 o ZOOM DO CELULAR (aproximado = escala grande) · a BARRA GRÁFICA que viaja com o
#   mapa · escala como fração (1/2 > 1/20) · ep3 o QUADRADINHO de 1 cm² que vira 4 m² · a MAQUETE que encolhe em três
#   direções · 1 : 100 = 1 cm é 1 m.
#   (Os eps 1–3 foram escritos em paralelo: frases tiradas do PLANO_DA_SERIE.md e das frases-chave dos prompts.)
# O que a prova cobra (seção 01): a cadeia de conversão · a escala de área · escala grande × pequena.
# Onde aparece (seção 09): Geografia · Matemática (semelhança: só a ponte, terá série própria) · Física · arquitetura.
# Estratégia (seção 10): tudo em centímetros antes · qual das três perguntas · plausibilidade.
# V/F (os 8 erros da seção 11; 5 falsas e 3 verdadeiras):
#   1 F (1 : 100 000, 4 cm = 400 000 km; são 400 000 cm = 4 km) · 2 F (1 : 50, 1 cm² = 50 cm²; são 2 500 cm² = 0,25 m²) ·
#   3 V (maquete 1 : 10: volume real = 1 000 vezes) · 4 V (1 : 50 000 é escala MAIOR que 1 : 250 000) ·
#   5 F (2 cm para 1 km → 50 000 : 1; é 1 : 50 000) · 6 F (5 cm para 10 km → 1 : 2; padronize: 1 : 200 000) ·
#   7 V (a barra gráfica continua valendo numa ampliação) · 8 F (do real para o mapa, multiplica; divide).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (Geografia, mapa rodoviário) 1 : 2 000 000, 7,5 cm → 15 000 000 cm → ÷ 100 000 = 150 km → C.
#      Atalho: 20 km por cm · 7,5 × 20 = 150. A 15 (cortou seis zeros) · B 1 500 (cortou só quatro) ·
#      D 15 000 (pulou o degrau cm → m: só ÷ 1 000) · E 150 000 (parou nos metros).
#   Q2 (planejamento urbano) faixas de pedestres e semáforos de cruzamentos → maior escala = menor denominador → A 1 : 2 000
#      (1 cm = 20 m). B 1 : 20 000 (1 cm = 200 m: a rua vira um risco) · C 1 : 200 000 (1 cm = 2 km) · D 1 : 2 000 000 ·
#      E 1 : 20 000 000 (de quem acha que denominador maior é escala maior).
#   Q3 (Matemática, planta de loteamento) 1 : 500, lote 4 cm × 6 cm → lados 20 m e 30 m → 600 m² → E.
#      Pelo n²: 24 cm² × 250 000 = 6 000 000 cm² ÷ 10 000 = 600 m². A 1,2 (fator linear na área) · B 120 (converteu só um
#      lado) · C 60 000 (dividiu por 100: 1 m² são 10 000 cm²) · D 6 000 000 (parou nos centímetros quadrados).
#   Q4 (maquete) piscina 1 : 25, maquete com 3,2 L → 25³ = 15 625 → 3,2 × 15 625 = 50 000 L = 50 m³ → B.
#      A 80 (fator linear) · C 2 000 (fator de área) · D 15 625 (fator certo, esqueceu os 3,2 L) · E 50 (achou 50 m³ e
#      chamou de litro). Plausível: piscina de 10 m × 5 m × 1 m.
#   Q5 (Geografia, fotocópia) mapa 1 : 80 000 com barra de 2 cm = 1,6 km, ampliado ao dobro → a barra passa a medir 4 cm e
#      continua valendo 1,6 km = 160 000 cm → 4 / 160 000 = 1 / 40 000 → D (gráfica válida; nova 1 : 40 000).
#      A numérica continua 1 : 80 000 (confiou no número impresso) · B 1 : 160 000 (multiplicou o denominador: ampliar dá
#      MAIS detalhe, escala maior) · C a gráfica deixa de valer (ela cresce junto) · E 1 : 20 000 (usou o fator ao quadrado,
#      como se fosse área).
# Gabaritos: C, A, E, B, D.
# Checklist (seção 13, 13 itens) → episódio: desenho/real, ler 1 : n, cadeia cm → km, atalho dos 5 zeros, os três cálculos,
#   plausibilidade: ep1 · denominador menor = escala maior, gráfica → numérica, gráfica sobrevive à ampliação: ep2 ·
#   n² e n³, lados primeiro, maquete com cubo, 1 : 100 = 1 m: ep3.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), incluindo Geografia com cartas topográficas.
# Ponte (do usuário): Velocidade, densidade e vazão.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de escalas, plantas e mapas: 8 pegadinhas e 5 questões estilo ENEM | Escalas Ep. 4"
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
        "{a}Escala é um dos poucos conteúdos que caem *literalmente iguais* em duas áreas do ENEM: [p=0.3] "
        "{b}*Matemática* e *Geografia.* [p=0.4] {c}Hoje você treina para as duas. [p=0.4] {d}Com oito frases de "
        "verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}A conta da escala é fácil: [p=0.2] uma multiplicação. [p=0.3] Então, o que a prova cobra de verdade? "
        "[p=0.3] Três coisas. [p=0.4] {a}Um: [p=0.2] a *cadeia de conversão,* [p=0.2] de centímetros até quilômetros. "
        "[p=0.3] {b}Dois: [p=0.2] a *escala de área,* [p=0.2] que vai ao quadrado. [p=0.3] {c}Três: [p=0.2] escala "
        "*grande* e escala *pequena,* [p=0.2] o nome que parece invertido."),

    # ================= ÍNDICE DA REVISÃO: OS 3 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] o mapa é uma *foto "
        "encolhida* do mundo. [p=0.2] Escala é desenho sobre real, [p=0.2] na mesma unidade. [p=0.3] Do mapa para o "
        "mundo, [p=0.2] *multiplique;* [p=0.2] do mundo para o mapa, [p=0.2] *divida.* [p=0.3] E a *tesoura:* "
        "[p=0.2] em um para *n,* [p=0.2] corte cinco zeros, [p=0.2] e cada centímetro vale isso em quilômetros."),
    dict(id="04", block="indice", text=
        "{a}Dois: [p=0.2] o *zoom do celular.* [p=0.2] Escala grande é zoom aproximado, [p=0.2] com as ruas. [p=0.2] "
        "Denominador menor, [p=0.2] escala maior. [p=0.3] E a *barra gráfica* viaja com o mapa; [p=0.2] o número, "
        "não. [p=0.4] {b}Três: [p=0.2] a *maquete.* [p=0.2] Comprimento usa *n,* [p=0.2] área usa *n ao quadrado,* "
        "[p=0.2] volume usa *n ao cubo.* [p=0.3] E em um para cem, [p=0.2] um centímetro é *um metro.*"),

    # ================= ONDE APARECE (seção 09) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais a escala aparece? [p=0.4] {a}Na *Geografia,* [p=0.2] em cartas topográficas, [p=0.2] com "
        "curvas de nível. [p=0.3] {b}Na *Física,* [p=0.2] em modelos reduzidos [p=0.2] e na ampliação das lentes. "
        "[p=0.3] {c}Em *arquitetura* e *urbanismo,* [p=0.2] em toda planta. [p=0.4] {d}E na *Matemática,* [p=0.2] "
        "ela volta como *semelhança de figuras,* [p=0.2] que vai ter série própria. [p=0.3] Spoiler: [p=0.2] lá, "
        "a razão dos lados é a escala, [p=0.2] a das áreas é o quadrado, [p=0.2] e a dos volumes, o cubo."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 10) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] três hábitos resolvem quase tudo. [p=0.4] {a}Um: [p=0.2] passe *tudo para "
        "centímetros* [p=0.2] antes de aplicar a escala. [p=0.3] {b}Dois: [p=0.2] descubra *qual pergunta* está sendo "
        "feita. [p=0.2] Medida real? [p=0.2] Multiplica. [p=0.2] Medida no desenho? [p=0.2] Divide. [p=0.2] A escala? "
        "[p=0.2] Monta a razão. [p=0.3] {c}Três: [p=0.2] *confira se faz sentido.* [p=0.2] Se a medida real saiu do "
        "tamanho do mapa, [p=0.2] faltou um degrau."),

    # ================= VERDADEIRO OU FALSO: OS 8 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Oito frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] num mapa um para cem mil, [p=0.2] quatro centímetros representam *quatrocentos mil "
        "quilômetros.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a multiplicação está certa. "
        "[p=0.3] {g}Mas o resultado está em *centímetros.* [p=0.2] Corte cinco zeros: [p=0.2] *quatro quilômetros.*"),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] numa planta um para cinquenta, [p=0.2] um centímetro quadrado vale *cinquenta* centímetros "
        "quadrados reais. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinquenta é o número da "
        "escala. [p=0.3] {g}Mas a área tem dois lados: [p=0.2] cinquenta vezes cinquenta, [p=0.2] *dois mil e "
        "quinhentos.*"),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] numa maquete um para dez, [p=0.2] o volume real é *mil vezes* o da maquete. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque mil parece exagero. [p=0.3] {g}Mas a "
        "maquete encolhe em *três direções:* [p=0.2] dez vezes dez vezes dez."),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] um para cinquenta mil [p=0.2] é escala *maior* que um para duzentos e cinquenta mil. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o número é menor. [p=0.3] "
        "{g}Mas pense na fração: [p=0.2] um meio é maior que um vinte avos. [p=0.2] Denominador menor, [p=0.2] "
        "*escala maior.*"),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] se dois centímetros do mapa valem um quilômetro, [p=0.2] a escala é *cinquenta mil para "
        "um.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a conta, cem mil dividido por dois, "
        "[p=0.2] está certa. [p=0.3] {g}Mas escala é *desenho sobre real:* [p=0.2] *um para cinquenta mil.*"),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] se cinco centímetros do mapa valem dez quilômetros, [p=0.2] a escala é *um para dois.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinco sobre dez simplifica bonito. [p=0.3] "
        "{g}Mas as unidades são diferentes. [p=0.2] Dez quilômetros são um milhão de centímetros: [p=0.2] *um para "
        "duzentos mil.*"),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] quando o mapa é ampliado numa fotocópia, [p=0.2] a *barra gráfica* continua valendo. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque tudo mudou de tamanho. [p=0.3] "
        "{g}Mas a barra *viaja com o mapa:* [p=0.2] cresce junto. [p=0.2] Quem fica errado é o *número.*"),
    dict(id="15", block="vf", text=
        "{t}E oito: [p=0.2] para achar o tamanho no mapa de uma distância real, [p=0.2] *multiplica-se* pelo "
        "denominador. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a primeira conta da escala é "
        "uma multiplicação. [p=0.3] {g}Mas do mundo para o mapa, [p=0.2] o número *encolhe:* [p=0.2] *divida.*"),
    dict(id="16", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Cinco falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as "
        "cinco questões, [p=0.2] todas inéditas, [p=0.2] de Matemática e de Geografia. [p=0.2] Em todas, [p=0.2] "
        "escreva a *unidade* ao lado de cada número."),

    # ================= QUESTÃO 1: MAPA RODOVIÁRIO (cadeia até o km) =================
    dict(id="17", block="q1", text=
        "{t}Questão um, [p=0.2] de Geografia. [p=0.3] {a}Num mapa rodoviário de escala *um para dois milhões,* "
        "[p=0.2] duas cidades estão a *sete vírgula cinco centímetros.* [p=0.3] {b}A distância real, [p=0.2] em "
        "quilômetros, [p=0.2] é [p=0.4] {la}A, [p=0.2] quinze. [p=0.2] {lb}B, [p=0.2] mil e quinhentos. [p=0.2] "
        "{lc}C, [p=0.2] cento e cinquenta. [p=0.2] {ld}D, [p=0.2] quinze mil. [p=0.2] {le}E, [p=0.2] cento e cinquenta "
        "mil. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="q1", text=
        "{d}Qual pergunta? [p=0.2] Medida *real:* [p=0.2] multiplica. [p=0.3] {a}Sete vírgula cinco vezes dois "
        "milhões: [p=0.2] *quinze milhões de centímetros.* [p=0.3] {b}Cortando cinco zeros: [p=0.2] *cento e "
        "cinquenta quilômetros.* [p=0.2] {ok}*Letra C!* [p=0.3] {v}Pelo atalho: [p=0.2] vinte quilômetros por "
        "centímetro, [p=0.2] vezes sete e meio. [p=0.4] {xe}A E parou nos metros. [p=0.2] {xd}A D pulou o degrau do "
        "metro. [p=0.2] {xb}A B cortou só quatro zeros, [p=0.2] {xa}e a A cortou seis."),

    # ================= QUESTÃO 2: PLANEJAMENTO URBANO (grande × pequena) =================
    dict(id="19", block="q2", text=
        "{t}Questão dois, [p=0.2] de planejamento urbano. [p=0.3] {a}Uma prefeitura vai decidir onde pintar *faixas "
        "de pedestres* [p=0.2] e instalar *semáforos* nos cruzamentos do centro. [p=0.3] {b}O mapa mais adequado tem "
        "escala [p=0.4] {la}A, [p=0.2] um para dois mil. [p=0.2] {lb}B, [p=0.2] um para vinte mil. [p=0.2] {lc}C, "
        "[p=0.2] um para duzentos mil. [p=0.2] {ld}D, [p=0.2] um para dois milhões. [p=0.2] {le}E, [p=0.2] um para "
        "vinte milhões. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q2", text=
        "{d}Faixa de pedestre é detalhe: [p=0.2] *zoom aproximado.* [p=0.3] {a}Mais detalhe é escala *maior,* "
        "[p=0.2] e escala maior é o *menor denominador.* [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confere: [p=0.2] em um "
        "para dois mil, [p=0.2] cada centímetro vale vinte metros. [p=0.2] Dá para ver a esquina. [p=0.4] {xb}Na B, "
        "[p=0.2] duzentos metros por centímetro: [p=0.2] a rua vira um risco. [p=0.2] {xc}Na C e na D, [p=0.2] "
        "{xd}cada centímetro vale quilômetros: [p=0.2] o centro inteiro cabe na ponta do dedo. [p=0.2] {xe}E a E é de quem acha que denominador maior é escala maior."),

    # ================= QUESTÃO 3: PLANTA DE LOTEAMENTO (n²) =================
    dict(id="21", block="q3", text=
        "{t}Questão três, [p=0.2] de Matemática. [p=0.3] {a}Na planta de um loteamento, [p=0.2] na escala *um para "
        "quinhentos,* [p=0.2] um lote retangular mede *quatro centímetros* por *seis centímetros.* [p=0.3] {b}A área "
        "real do lote, [p=0.2] em metros quadrados, [p=0.2] é [p=0.4] {la}A, [p=0.2] um vírgula dois. [p=0.2] {lb}B, "
        "[p=0.2] cento e vinte. [p=0.2] {lc}C, [p=0.2] sessenta mil. [p=0.2] {ld}D, [p=0.2] seis milhões. [p=0.2] "
        "{le}E, [p=0.2] seiscentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q3", text=
        "{d}O caminho seguro: [p=0.2] *converta os lados primeiro.* [p=0.3] {a}Quatro vezes quinhentos, [p=0.2] dois "
        "mil centímetros: [p=0.2] *vinte metros.* [p=0.2] Seis vezes quinhentos: [p=0.2] *trinta metros.* [p=0.3] "
        "{b}Vinte vezes trinta: [p=0.2] *seiscentos metros quadrados.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confere: "
        "[p=0.2] um lote de vinte por trinta é bem comum. [p=0.4] {xa}A A usou o fator linear na área. [p=0.2] "
        "{xb}A B converteu um lado só. [p=0.2] {xd}A D parou nos centímetros quadrados, [p=0.2] {xc}e a C dividiu por "
        "cem, [p=0.2] mas um metro quadrado tem *dez mil.*"),

    # ================= QUESTÃO 4: MAQUETE DA PISCINA (n³) =================
    dict(id="23", block="q4", text=
        "{t}Questão quatro, [p=0.2] a maquete. [p=0.3] {a}Uma maquete de uma piscina, [p=0.2] na escala *um para "
        "vinte e cinco,* [p=0.2] comporta *três vírgula dois litros.* [p=0.3] {b}A piscina real comporta [p=0.4] "
        "{la}A, [p=0.2] oitenta litros. [p=0.2] {lb}B, [p=0.2] cinquenta mil. [p=0.2] {lc}C, [p=0.2] dois mil. "
        "[p=0.2] {ld}D, [p=0.2] quinze mil, seiscentos e vinte e cinco. [p=0.2] {le}E, [p=0.2] cinquenta litros. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q4", text=
        "{d}Capacidade é volume: [p=0.2] *três direções,* [p=0.2] fator ao cubo. [p=0.3] {a}Vinte e cinco vezes vinte "
        "e cinco vezes vinte e cinco: [p=0.2] *quinze mil, seiscentos e vinte e cinco.* [p=0.3] {b}Vezes três vírgula "
        "dois: [p=0.2] *cinquenta mil litros.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Confere: [p=0.2] uma piscina de dez "
        "por cinco, [p=0.2] com um metro de fundo. [p=0.4] {xa}A A usou o fator linear, [p=0.2] {xc}a C o de área. "
        "[p=0.2] {xd}A D esqueceu os três vírgula dois litros. [p=0.2] {xe}E a E achou cinquenta metros cúbicos e "
        "chamou de litro."),

    # ================= QUESTÃO 5: MAPA AMPLIADO NA FOTOCÓPIA =================
    dict(id="25", block="q5", text=
        "{t}E a questão cinco, [p=0.2] de Geografia. [p=0.3] {a}Um mapa de escala *um para oitenta mil* [p=0.2] tem "
        "uma barra gráfica de *dois centímetros* [p=0.2] que vale *um vírgula seis quilômetro.* [p=0.2] Ele foi "
        "*ampliado ao dobro* numa fotocópia. [p=0.3] {b}Na cópia, [p=0.4] {la}A, [p=0.2] a escala numérica continua "
        "valendo: [p=0.2] um para oitenta mil. [p=0.2] {lb}B, [p=0.2] a barra vale, [p=0.2] e a nova escala é um para "
        "cento e sessenta mil. [p=0.2] {lc}C, [p=0.2] a barra deixa de valer, [p=0.2] e a nova escala é um para "
        "quarenta mil. [p=0.2] {ld}D, [p=0.2] a barra vale, [p=0.2] e a nova escala é um para quarenta mil. [p=0.2] "
        "{le}E, [p=0.2] a barra vale, [p=0.2] e a nova escala é um para vinte mil. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{d}A barra viaja com o mapa: [p=0.2] *ela continua valendo.* [p=0.3] {a}Na cópia, [p=0.2] ela mede *quatro "
        "centímetros,* [p=0.2] e ainda vale um vírgula seis quilômetro, [p=0.2] que são cento e sessenta mil "
        "centímetros. [p=0.3] {b}Desenho sobre real: [p=0.2] quatro sobre cento e sessenta mil, [p=0.2] *um para "
        "quarenta mil.* [p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A confiou no número impresso. [p=0.2] {xc}A C errou a "
        "barra. [p=0.2] {xb}A B multiplicou, [p=0.2] mas ampliar dá *mais* detalhe: [p=0.2] escala maior, "
        "denominador menor. [p=0.2] {xe}E a E usou o dobro ao quadrado, [p=0.2] como se fosse área."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="27", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Desenho sobre real, [p=0.2] ler um para *n,* "
        "[p=0.2] a cadeia até o quilômetro, [p=0.2] o atalho dos cinco zeros, [p=0.2] os três cálculos [p=0.2] e a "
        "conferência: [p=0.2] episódio um."),
    dict(id="28", block="checklist", text=
        "{a}Escala grande e pequena, [p=0.2] converter a barra em número [p=0.2] e por que a barra sobrevive à "
        "cópia: [p=0.2] episódio dois. [p=0.3] {b}Área ao quadrado, [p=0.2] volume ao cubo, [p=0.2] os lados "
        "primeiro [p=0.2] e o um para cem: [p=0.2] episódio três. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o "
        "episódio correspondente."),

    # ================= META =================
    dict(id="29", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E inclua questões de *Geografia,* [p=0.2] com cartas topográficas e curvas de "
        "nível: [p=0.2] lá a escala aparece sem números redondos."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}O próximo assunto é *Velocidade, densidade e vazão,* [p=0.3] {b}que fecha o bloco de proporcionalidade "
        "da Matemática básica."),
    dict(id="31", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de escalas, plantas e mapas está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
