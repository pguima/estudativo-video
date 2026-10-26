# Roteiro — Cartografia, Episódio 6: Revisão geral, pegadinhas e treino para o ENEM (aula de revisão)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seções 01, 10, 11 e 13 (sem reutilizar as Questões 1 a 9)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Âncoras retomadas: escala = zoom · coordenadas = batalha naval · projeção = casca de laranja ·
#   curvas de nível = degraus de escada · anamorfose = mapa de balões
# Questões INÉDITAS (contas conferidas):
#   Q1 1:200 000, 6 cm → 1 200 000 cm = 12 km (B)
#   Q2 de 20° S, 40° O para 10° S, 55° O → norte + oeste = noroeste (B)
#   Q3 comparar áreas de florestas → equivalente/Peters (B)
#   Q4 1:25 000, 2 cm = 500 m; 450 − 300 = 150 m; 150 ÷ 500 = 30% (B)
#   Q5 tamanho ∝ emissões de CO₂ → os maiores no mapa são os que mais emitem (C)

TITULO = "Revisão de Cartografia para o ENEM: 9 Pegadinhas e 5 Questões | Cartografia Ep. 6"
PRONUNCIA = {
    "ENEM": "Enem",
    "CO₂": "C O dois",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "A cartografia é a porta de entrada da Geografia no ENEM. [p=0.4] {a}Ela cai de dois jeitos: [p=0.2] *como conta,* "
        "[p=0.3] {b}e como *leitura crítica.* [p=0.5] {c}Hoje você vai ver se está pronto para os dois."),
    dict(id="01b", block="doisjeitos", text=
        "{t}Como *conta:* [p=0.2] {a}escala, distância e declividade. [p=0.4] {b}Como *leitura crítica:* [p=0.2] por que a Groenlândia parece enorme, "
        "[p=0.2] quem decidiu que o norte fica em cima, [p=0.2] e o que o mapa quer mostrar. [p=0.4] {c}A boa notícia: [p=0.2] os dois jeitos usam os *mesmos* poucos conceitos."),
    dict(id="02", block="indice", text=
        "{t}Vamos revisar os cinco episódios, [p=0.2] cada um com a sua imagem. [p=0.4] {a}Escala é *zoom.* [p=0.3] {b}Coordenadas são uma "
        "*batalha naval.* [p=0.3] {c}Projeção é uma *casca de laranja.* [p=0.3] {d}Curvas de nível são *degraus de escada.* [p=0.3] "
        "{e}E anamorfose é um *mapa de balões.*"),

    # ================= AS 3 IDEIAS QUE MAIS RENDEM =================
    dict(id="03", block="ideias", text=
        "{t}Se você só pudesse levar três ideias para a prova, seriam estas. [p=0.4] {a}Um: [p=0.2] escala *grande* é número de baixo *pequeno,* "
        "[p=0.2] e mostra *mais detalhe.* [p=0.2] É o zoom aproximado. [p=0.5] {b}Dois: [p=0.2] *nenhuma projeção é neutra:* [p=0.2] a conforme "
        "guarda a forma, a equivalente guarda a área, [p=0.2] e nenhuma faz as duas coisas. [p=0.5] {c}Três: [p=0.2] curvas de nível *próximas* "
        "são terreno *íngreme:* [p=0.2] degraus colados."),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="04", block="vf_intro", text=
        "{t}Agora, um jogo: [p=0.2] *verdadeiro ou falso.* [p=0.4] {a}Eu leio uma frase, [p=0.2] você pausa e responde. [p=0.4] "
        "{b}Atenção: [p=0.2] todas elas são pegadinhas de verdade, [p=0.2] que já derrubaram muita gente."),
    dict(id="05", block="vf", text=
        "{t}Um: [p=0.2] \"um para cinco milhões é escala grande\". [p=0.3] {p}Pause e responda. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque cinco milhões é um número enorme. [p=0.4] {c}Mas é o número de baixo da fração: [p=0.2] escala *pequena,* "
        "[p=0.2] zoom afastado."),
    dict(id="06", block="vf", text=
        "{t}Dois: [p=0.2] \"num mapa ampliado no xerox, a escala numérica continua valendo\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque o número está impresso ali. [p=0.4] {c}Mas só a *barrinha* cresce junto com o mapa."),
    dict(id="07", block="vf", text=
        "{t}Três: [p=0.2] \"oito centímetros, num mapa de um para duzentos e cinquenta mil, são dois quilômetros\". [p=0.3] {p}Pause. [p=2.0] "
        "{r}*Falso.* [p=0.3] {e}Engana porque a conta parece fácil. [p=0.4] {c}Mas oito vezes duzentos e cinquenta mil dá dois milhões de centímetros: "
        "[p=0.2] corte cinco zeros, [p=0.2] *vinte* quilômetros."),
    dict(id="08", block="vf", text=
        "{t}Quatro: [p=0.2] \"a latitude é medida a partir de Greenwich\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque Greenwich é o zero mais famoso. [p=0.4] {c}Mas, na batalha naval, a linha é a latitude, [p=0.2] e ela começa no *Equador.*"),
    dict(id="09", block="vf", text=
        "{t}Cinco: [p=0.2] \"de cinco graus norte a quinze graus sul, a diferença é de dez graus\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque a gente sempre subtrai. [p=0.4] {c}Mas os dois estão em lados opostos do Equador: [p=0.2] *soma.* Vinte graus."),
    dict(id="10", block="vf", text=
        "{t}Seis: [p=0.2] \"a projeção de Mercator mostra as áreas reais\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque é o mapa da escola. [p=0.4] {c}Mas, na casca de laranja, ela protegeu a *forma:* [p=0.2] e infla as áreas perto dos polos."),
    dict(id="11", block="vf", text=
        "{t}Sete: [p=0.2] \"a projeção de Peters preserva as formas\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque ela é a projeção \"mais justa\". [p=0.4] {c}Mas ela protegeu a *área,* [p=0.2] e estica as formas."),
    dict(id="12", block="vf", text=
        "{t}Oito: [p=0.2] \"curvas de nível juntinhas mostram um terreno plano\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque linhas juntas parecem tranquilas. [p=0.4] {c}Mas são degraus *colados:* [p=0.2] terreno íngreme."),
    dict(id="13", block="vf", text=
        "{t}Nove: [p=0.2] \"anamorfose é o mesmo que projeção equivalente\". [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{e}Engana porque as duas falam de área. [p=0.4] {c}Mas a equivalente *mantém* a área real; [p=0.2] no mapa de balões, o tamanho é um *dado.*"),

    dict(id="13b", block="vf_fim", text=
        "{t}Quantas você acertou? [p=0.4] {a}Se errou mais de três, [p=0.2] não tem problema. [p=0.3] {b}Anote quais foram, [p=0.2] "
        "e reveja o episódio de cada uma. [p=0.4] {c}Errar aqui é muito melhor do que errar na prova."),

    # ================= QUESTÃO 1: ESCALA =================
    dict(id="13c", block="lembra", text=
        "{t}Agora, cinco questões inéditas, uma de cada episódio. [p=0.3] Antes de cada uma, uma lembrança rápida. [p=0.4] "
        "{a}Escala é o *zoom:* [p=0.2] o número de baixo diz quantas vezes o mundo encolheu. [p=0.4] {b}E para passar de centímetros para quilômetros, "
        "[p=0.2] *corte cinco zeros.*"),
    dict(id="14", block="q1", text=
        "{t}Primeira: [p=0.2] {e1}num mapa de um para duzentos mil, "
        "[p=0.2] duas cidades estão a seis centímetros. [p=0.3] {e2}A distância real é de... [p=0.3] {a}A: um vírgula dois quilômetros. "
        "[p=0.2] {b}B: doze quilômetros. [p=0.2] {c}C: cento e vinte quilômetros. [p=0.2] {d}D: trinta e três quilômetros. [p=0.2] "
        "{e}E: mil e duzentos quilômetros. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="q1", text=
        "{t}Seis vezes duzentos mil: [p=0.2] um milhão e duzentos mil centímetros. [p=0.3] Corte cinco zeros: [p=0.2] *doze quilômetros,* letra B. "
        "[p=0.4] {a}A, C e E erraram os zeros. [p=0.3] {d}E D dividiu duzentos mil por seis, [p=0.2] em vez de multiplicar."),

    # ================= QUESTÃO 2: COORDENADAS =================
    dict(id="15b", block="lembra", text=
        "{t}Lembra da *batalha naval:* [p=0.3] {a}a latitude é a linha, contada a partir do Equador. [p=0.3] {b}A longitude é a coluna, a partir de Greenwich. "
        "[p=0.4] {c}E no lado oeste, [p=0.2] número de longitude *maior* é mais longe de Greenwich: [p=0.2] mais para o *oeste.*"),
    dict(id="16", block="q2", text=
        "{t}Segunda: [p=0.2] {e1}um barco sai de vinte graus sul e quarenta graus oeste, [p=0.3] {e2}e vai até dez graus sul e cinquenta e cinco graus oeste. "
        "[p=0.3] {e3}Para que lado ele foi? [p=0.3] {a}A: nordeste. [p=0.2] {b}B: noroeste. [p=0.2] {c}C: sudoeste. [p=0.2] {d}D: sudeste. "
        "[p=0.2] {e}E: norte. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="q2", text=
        "{t}Linha e coluna, separadas. [p=0.3] {s1}De vinte para dez graus sul: [p=0.2] mais perto do Equador, [p=0.2] foi para o *norte.* [p=0.4] "
        "{s2}De quarenta para cinquenta e cinco oeste: [p=0.2] mais longe de Greenwich, [p=0.2] foi para o *oeste.* [p=0.4] {r}Noroeste, letra B. "
        "[p=0.4] {a}A achou que cinquenta e cinco fica a leste. [p=0.2] {c}C errou a latitude. [p=0.2] {d}D errou as duas. [p=0.2] {e}E esqueceu a longitude."),

    # ================= QUESTÃO 3: PROJEÇÕES =================
    dict(id="17b", block="lembra", text=
        "{t}Lembra da *casca de laranja:* [p=0.2] {a}ou ela rasga, ou estica. [p=0.4] {b}A projeção *conforme* protege a forma. [p=0.3] "
        "{c}A *equivalente* protege a área."),
    dict(id="18", block="q3", text=
        "{t}Terceira: [p=0.2] {e1}um atlas quer comparar o tamanho das florestas de cada continente. [p=0.3] {e2}Qual projeção ele deve usar? [p=0.3] "
        "{a}A: a de Mercator, conforme, porque preserva as formas. [p=0.3] {b}B: a de Peters, equivalente, porque mantém a proporção entre as áreas. "
        "[p=0.3] {c}C: uma cilíndrica qualquer, já que o Equador é onde o erro é maior. [p=0.3] {d}D: uma anamorfose de população. [p=0.3] "
        "{e}E: uma equivalente, porque preserva as formas e as áreas ao mesmo tempo. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q3", text=
        "{t}Para comparar tamanhos, [p=0.2] você protege a *área:* [p=0.2] equivalente, letra B. [p=0.4] {a}A é a Mercator, que infla os polos. "
        "[p=0.3] {c}C erra o lugar do erro: [p=0.2] onde toca, ele é *menor.* [p=0.3] {d}D troca a área por um dado. [p=0.3] "
        "{e}E promete o impossível: [p=0.2] forma e área juntas."),

    # ================= QUESTÃO 4: CURVAS DE NÍVEL =================
    dict(id="19b", block="lembra", text=
        "{t}Lembra da *escada:* [p=0.3] {a}o desnível é o quanto você sobe; [p=0.3] {b}a distância é o quanto anda na horizontal. [p=0.4] "
        "{c}Declividade é um dividido pelo outro, [p=0.2] vezes cem, [p=0.2] metro com metro."),
    dict(id="20", block="q4", text=
        "{t}Quarta: [p=0.2] {e1}numa carta de um para vinte e cinco mil, [p=0.2] {e2}dois pontos estão nas curvas de trezentos e de quatrocentos e cinquenta metros, "
        "[p=0.2] {e3}a dois centímetros um do outro. [p=0.3] Qual é a declividade? [p=0.3] {a}A: zero vírgula três por cento. [p=0.2] "
        "{b}B: trinta por cento. [p=0.2] {c}C: noventa por cento. [p=0.2] {d}D: três por cento. [p=0.2] {e}E: trezentos por cento. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q4", text=
        "{t}Dois vezes vinte e cinco mil: [p=0.2] cinquenta mil centímetros, [p=0.2] *quinhentos metros.* [p=0.3] {s1}Desnível: [p=0.2] "
        "quatrocentos e cinquenta menos trezentos, [p=0.2] cento e cinquenta. [p=0.3] {s2}Cento e cinquenta sobre quinhentos: [p=0.2] *trinta por cento,* letra B. "
        "[p=0.4] {a}A dividiu metro por centímetro. [p=0.2] {c}C usou a altitude, quatrocentos e cinquenta. [p=0.2] {d}D errou a conversão, "
        "[p=0.2] {e}e E também. [p=0.4] {x}E repare: trinta por cento é justamente o limite da lei para lotear."),

    # ================= QUESTÃO 5: ANAMORFOSE =================
    dict(id="21b", block="lembra", text=
        "{t}E o *mapa de balões:* [p=0.3] {a}cada país incha ou murcha conforme um dado, [p=0.3] {b}mas continua no mesmo lugar."),
    dict(id="22", block="q5", text=
        "{t}Quinta: [p=0.2] {e1}num mapa, o tamanho de cada país é proporcional às suas emissões de gás carbônico. [p=0.3] {e2}Estados Unidos e China "
        "aparecem enormes, [p=0.2] e a África quase some. [p=0.3] {e3}Qual conclusão está correta? [p=0.3] {a}A: a África tem pouco território. [p=0.3] "
        "{b}B: é uma projeção equivalente, então as áreas são reais. [p=0.3] {c}C: os países maiores no mapa são os que mais emitem. [p=0.3] "
        "{d}D: a China é o maior país do mundo em território. [p=0.3] {e}E: é um mapa de escala grande. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q5", text=
        "{t}Mapa de balões: [p=0.2] o tamanho é o dado. [p=0.2] Letra C. [p=0.4] {a}A e D leram o tamanho como território. [p=0.3] "
        "{b}B confundiu anamorfose com equivalente. [p=0.3] {e}E confundiu escala com tamanho do desenho: [p=0.2] o mapa-múndi tem escala *pequena.*"),

    # ================= CONEXÕES =================
    dict(id="24", block="conexoes", text=
        "{t}A cartografia também aparece em outras matérias. [p=0.4] {a}A escala é *proporção,* da Matemática. [p=0.3] {b}Latitude e longitude são *ângulos.* "
        "[p=0.3] {c}A Mercator nasceu nas *Grandes Navegações,* da História. [p=0.3] {d}A longitude vira *fuso horário.* [p=0.3] "
        "{e}E as curvas de nível explicam a *erosão:* [p=0.2] por onde a água escorre e leva o solo."),

    # ================= CHECKLIST =================
    dict(id="25", block="checklist", text=
        "{t}Agora, o seu checklist. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta para outra pessoa, [p=0.2] sem consultar nada. "
        "[p=0.4] {b}Calcular distância com a escala, [p=0.2] entender o mapa ampliado, [p=0.2] e escala grande ou pequena: [p=0.2] episódio um. "
        "[p=0.4] {c}Latitude, longitude, as linhas da Terra, [p=0.2] a distância no meridiano e a direção: [p=0.2] episódio dois."),
    dict(id="26", block="checklist", text=
        "{d}Os tipos de projeção, [p=0.2] conforme e equivalente, [p=0.2] a Mercator e a Peters: [p=0.2] episódio três. [p=0.4] "
        "{e}Ler curvas de nível, [p=0.2] o perfil e a declividade: [p=0.2] episódio quatro. [p=0.4] {f}E reconhecer uma anamorfose: [p=0.2] episódio cinco. "
        "[p=0.4] {g}O que você não marcou, [p=0.2] *reveja o episódio.*"),

    # ================= META =================
    dict(id="27", block="meta", text=
        "{t}E quando dá para dizer que você *dominou?* [p=0.4] {a}Resolva *vinte* questões de cartografia, [p=0.3] {b}e acerte pelo menos *catorze:* "
        "[p=0.2] setenta por cento. [p=0.4] {c}Priorize escala e projeções, [p=0.2] que são as que mais caem, [p=0.3] {d}e inclua pelo menos três de curvas de nível."),

    # ================= PONTE =================
    dict(id="28", block="ponte", text=
        "{t}E o próximo assunto é *fusos horários.* [p=0.4] {a}Ele usa direto a longitude: [p=0.2] {b}cada quinze graus vale *uma hora.* [p=0.4] "
        "{c}Se o episódio dois está firme, [p=0.2] vai ser rápido."),
    dict(id="29", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder a próxima série. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das nove pegadinhas você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
