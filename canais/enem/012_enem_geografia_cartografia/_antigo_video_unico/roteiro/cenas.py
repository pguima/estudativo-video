# Roteiro — ENEM Geografia 01: Cartografia (escalas, coordenadas, projeções e curvas de nível)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Escalas faladas por extenso ("um para duzentos e cinquenta mil"); na tela, 1 : 250 000.

TITULO = "Cartografia: escala, coordenadas, projeções e curvas de nível — Geografia ENEM do zero"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Em muitos mapas da escola, [p=0.2] {a}a Groenlândia parece do tamanho da *África.* [p=0.5] {b}Na verdade, "
        "a África é *catorze vezes* maior. [p=0.5] {c}O mapa errou? [p=0.3] *Não.* [p=0.3] Ele fez uma *escolha.* [p=0.4] "
        "{d}E o ENEM quer saber se você percebe quando um mapa *mente* [p=0.2] sobre tamanhos, distâncias ou relevo."),
    dict(id="02", block="enem", text=
        "A cartografia é a porta de entrada da Geografia no ENEM, [p=0.2] e aparece de dois jeitos. [p=0.4] "
        "{a}Como *conta:* [p=0.2] escala, distância e declividade. [p=0.4] {b}E como *leitura crítica:* [p=0.2] "
        "por que este mapa mostra a Groenlândia tão grande? [p=0.2] Quem decidiu que o norte fica em cima?"),
    dict(id="03", block="mapa", text=
        "Nesta aula: [p=0.2] {a}a escala; [p=0.2] {b}as coordenadas geográficas; [p=0.2] {c}as projeções e a política dos mapas; "
        "[p=0.3] {d}e as curvas de nível."),

    # ================= ESCALA =================
    dict(id="04", block="escala", text=
        "{t}A *escala* é a razão entre a distância no mapa e a distância no terreno. [p=0.4] {a}Na escala um para cem mil, "
        "[p=0.2] um centímetro no mapa são cem mil centímetros no terreno: [p=0.2] *um quilômetro.* [p=0.4] "
        "{b}E o atalho: [p=0.2] para passar de centímetros para quilômetros, [p=0.2] *corte cinco zeros.*"),
    dict(id="05", block="q_escala", text=
        "{t}Questão: [p=0.2] {e1}num mapa de um para duzentos e cinquenta mil, [p=0.2] {e2}duas cidades estão a *oito centímetros.* "
        "[p=0.3] {e3}Qual a distância real? [p=0.5] {s1}Cortando cinco zeros, [p=0.2] cada centímetro vale dois vírgula cinco quilômetros. "
        "[p=0.4] {s2}Oito vezes dois vírgula cinco: [p=0.2] *vinte quilômetros.*"),
    dict(id="06", block="ampliado", text=
        "{t}E se o mapa for *ampliado* numa fotocópia de duzentos por cento? [p=0.4] {g}A escala *gráfica,* aquela barrinha, "
        "[p=0.2] cresce junto com o desenho, [p=0.2] e continua *certa.* [p=0.4] {n}Mas o número impresso fica *errado:* "
        "[p=0.2] um para um milhão vira um para *quinhentos mil.* [p=0.4] {d}É por isso que mapas digitais usam escala gráfica."),
    dict(id="07", block="grande", text=
        "{t}Agora, a regra que parece invertida. [p=0.4] {a}Escala é uma fração, [p=0.2] e um sobre cinco mil é *maior* "
        "que um sobre cinco milhões. [p=0.4] {b}Denominador *pequeno:* [p=0.2] escala *grande,* [p=0.2] área pequena, com muito detalhe. "
        "[p=0.4] {c}Denominador *grande:* [p=0.2] escala *pequena,* [p=0.2] países e continentes. [p=0.4] {d}Um mapa-múndi num painel "
        "de dois metros continua sendo de escala *pequena.*"),
    dict(id="08", block="q_bairro", text=
        "{t}Questão: [p=0.2] {e1}a prefeitura vai planejar bocas de lobo, *rua a rua,* num bairro. [p=0.3] "
        "{e2}Tem um mapa de um para dois mil, [p=0.2] e outro de um para dois milhões. [p=0.4] {s1}Em um para dois mil, "
        "[p=0.2] um centímetro são vinte metros: [p=0.2] cada rua aparece. [p=0.4] {s2}Esse é o de escala *grande.* [p=0.3] "
        "{x}Quem escolheu o denominador maior achando que era escala maior, [p=0.2] errou."),

    # ================= COORDENADAS =================
    dict(id="09", block="coord", text=
        "{t}Para localizar qualquer ponto da Terra, [p=0.2] usamos uma rede de linhas imaginárias. [p=0.4] "
        "{p}A *latitude* é medida a partir do *Equador,* [p=0.2] de zero a noventa graus, [p=0.2] para o norte ou para o sul. [p=0.4] "
        "{m}A *longitude* é medida a partir de *Greenwich,* [p=0.2] de zero a cento e oitenta graus, [p=0.2] para leste ou para oeste. "
        "[p=0.4] {x}E as duas são *ângulos,* [p=0.2] não quilômetros."),
    dict(id="10", block="linhas", text=
        "{t}As linhas que caem na prova: [p=0.2] {e}o *Equador,* [p=0.2] {tr}os *trópicos,* perto de vinte e três graus, [p=0.2] "
        "{cp}e os *círculos polares,* perto de sessenta e seis. [p=0.4] {b}E o Brasil é cortado pelo Equador e pelo *Trópico de Capricórnio,* "
        "[p=0.2] {o}e está inteiro no hemisfério *ocidental:* [p=0.2] todas as suas longitudes são *oeste.*"),
    dict(id="11", block="meridiano", text=
        "{t}E uma conta que cai: [p=0.2] {a}a Terra tem uns quarenta mil quilômetros de volta. [p=0.3] Dividindo por trezentos e sessenta, "
        "[p=0.2] {b}um grau de latitude vale cerca de *cento e onze quilômetros.* [p=0.4] {c}Dois lugares no mesmo meridiano, "
        "[p=0.2] em dois graus sul e vinte e dois graus sul: [p=0.2] vinte graus de diferença, [p=0.2] *dois mil, duzentos e vinte quilômetros.* "
        "[p=0.4] {d}E se estiverem em hemisférios *diferentes,* [p=0.2] você *soma* as latitudes."),
    dict(id="12", block="direcao", text=
        "{t}Questão: [p=0.2] {e}um avião sai de dez graus sul e cinquenta oeste, [p=0.2] e vai para vinte sul e quarenta oeste. "
        "[p=0.3] Para que lado ele foi? [p=0.5] {s1}De dez para vinte sul: [p=0.2] mais para o *sul.* [p=0.4] {s2}De cinquenta para quarenta oeste: "
        "[p=0.2] mais *perto* de Greenwich, [p=0.2] ou seja, para o *leste.* [p=0.4] {r}*Sudeste.* [p=0.3] {x}O erro comum é achar "
        "que quarenta oeste fica mais a oeste que cinquenta."),

    # ================= PROJEÇÕES =================
    dict(id="13", block="projecoes", text=
        "{t}Agora, as projeções. [p=0.3] {a}Tente achatar uma casca de laranja: [p=0.2] ela *rasga.* [p=0.3] "
        "Por isso, *toda* projeção distorce alguma coisa. [p=0.4] {c}A *cilíndrica* toca o globo no Equador: [p=0.2] é a do mapa-múndi. "
        "[p=0.4] {k}A *cônica* toca num paralelo: [p=0.2] boa para latitudes médias. [p=0.4] {z}E a *azimutal* toca num ponto: "
        "[p=0.2] boa para os polos. [p=0.4] {x}A distorção é mínima onde a superfície *toca,* [p=0.2] e cresce longe dali."),
    dict(id="14", block="propriedade", text=
        "{t}E cada projeção escolhe o que *preservar.* [p=0.4] {a}A *conforme* preserva os *ângulos* e as formas, [p=0.2] "
        "e sacrifica as áreas. [p=0.4] {b}A *equivalente* preserva as *áreas,* [p=0.2] e deforma as formas. [p=0.4] "
        "{x}E guarde: [p=0.2] fazer as duas coisas ao mesmo tempo é *impossível.*"),
    dict(id="15", block="mercator", text=
        "{t}A projeção de *Mercator,* de mil quinhentos e sessenta e nove, [p=0.2] é cilíndrica e *conforme.* [p=0.4] "
        "{a}Foi feita para *navegar:* [p=0.2] uma rota de rumo constante vira uma linha reta. [p=0.4] {b}O preço: [p=0.2] "
        "as áreas *incham* rumo aos polos. [p=0.3] {c}A sessenta graus, quatro vezes. [p=0.2] {d}A setenta, oito vezes e meia. [p=0.4] "
        "{e}É por isso que a Groenlândia parece do tamanho da África."),
    dict(id="16", block="peters", text=
        "{t}Nos anos setenta, a projeção de *Peters,* [p=0.2] que é *equivalente,* [p=0.2] {a}mostrou os continentes do sul "
        "com suas áreas *reais,* [p=0.2] e a Europa encolheu. [p=0.4] {b}Ela veio como *crítica* a uma visão de mundo *eurocêntrica.* "
        "[p=0.4] {c}Mas nenhuma é o mapa certo: [p=0.2] o centro do mapa e o polo que fica em cima são *convenções.* [p=0.3] "
        "{d}Um mapa com o sul em cima é tão correto quanto o tradicional."),

    # ================= CURVAS DE NÍVEL =================
    dict(id="17", block="curvas", text=
        "{t}Agora, o relevo. [p=0.3] {a}A *curva de nível* liga pontos de *mesma altitude.* [p=0.4] {b}Curvas *próximas:* "
        "[p=0.2] declive *forte.* [p=0.3] {c}Curvas *espaçadas:* [p=0.2] declive *suave.* [p=0.4] {d}Curvas fechadas, "
        "com valores crescendo para dentro: [p=0.2] um *morro.* [p=0.4] {x}E curvas de nível *nunca* se cruzam: [p=0.2] "
        "um ponto não pode ter duas altitudes."),
    dict(id="18", block="trilhas", text=
        "{t}Questão: [p=0.2] {e}duas trilhas saem da mesma curva e chegam ao mesmo cume. [p=0.4] Qual é a mais íngreme? [p=0.5] "
        "{s1}O desnível é o *mesmo.* [p=0.3] {s2}Muda a distância horizontal. [p=0.4] {r}A trilha que cruza curvas *juntas* "
        "sobe o mesmo tanto num caminho curto: [p=0.2] é a *mais íngreme.*"),
    dict(id="19", block="declividade", text=
        "{t}E a *declividade* é o desnível dividido pela distância horizontal, [p=0.2] vezes cem. [p=0.4] {a}Numa carta de um para cinquenta mil, "
        "[p=0.2] dois pontos a quatro centímetros estão a *dois mil metros.* [p=0.4] {b}Se um está a duzentos metros de altitude "
        "e o outro a seiscentos, [p=0.2] o desnível é quatrocentos. [p=0.4] {c}Quatrocentos sobre dois mil: [p=0.2] *vinte por cento.* "
        "[p=0.4] {d}E a lei proíbe lotear terrenos a partir de *trinta por cento:* [p=0.2] é área de risco de deslizamento."),

    # ================= ANAMORFOSE E LEITURA =================
    dict(id="20", block="anamorfose", text=
        "{t}E a *anamorfose:* [p=0.2] um mapa em que o tamanho de cada país representa um *dado,* [p=0.2] como população ou PIB. "
        "[p=0.4] {a}Numa anamorfose de população, [p=0.2] Índia e China *incham;* [p=0.2] {b}Canadá e Rússia *encolhem.* [p=0.4] "
        "{x}Ela não é projeção: [p=0.2] abandona a área real *de propósito,* [p=0.2] para mostrar uma desigualdade."),
    dict(id="21", block="leitura", text=
        "{t}E um roteiro para ler qualquer mapa da prova: [p=0.3] {a}título e fonte; [p=0.2] {b}a *legenda,* [p=0.2] "
        "onde a resposta costuma estar; [p=0.2] {c}a escala; [p=0.2] {d}e a orientação e a projeção."),

    # ================= FECHAMENTO =================
    dict(id="22", block="erros", text=
        "{t}Os erros que mais custam pontos: [p=0.3] {e1}achar que denominador grande é escala grande; [p=0.2] "
        "{e2}confiar na escala numérica de um mapa ampliado; [p=0.2] {e3}medir latitude a partir de Greenwich; [p=0.2] "
        "{e4}achar que a Mercator mostra as áreas reais; [p=0.2] {e5}e ler curvas juntas como terreno plano."),
    dict(id="23", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar toda a Geografia do ENEM do zero. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que a Groenlândia era do tamanho da África? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
