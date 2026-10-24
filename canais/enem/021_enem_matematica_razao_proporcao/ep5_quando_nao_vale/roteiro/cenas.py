# Roteiro — Razão, Proporção e Regra de Três, Episódio 5 de 6: Quando a regra de três NÃO funciona, e os 3 hábitos de prova
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seções 09 e 10 (+ Questão 8 da seção 12).
# Juros compostos, área e volume só como exemplos do que NÃO é proporcional (sem fórmula de juros compostos: séries próprias).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a PERGUNTA DE OURO: "dobrar a causa dobra MESMO o efeito? Se a resposta for 'não' ou 'depende', a regra
#   de três está fora." O selo aparece antes de cada situação.
# Desvio consciente: o gancho do usuário já É a Questão 8 (gatos). O bloco a) explica o ritmo individual; a Questão 8 entra
#   depois como a "prova oficial" do gancho: enunciado, pausa, resolução curta e foco em por que A e C são as duas regras de
#   três possíveis (A = inversa só com os gatos; C = direta só com os ratos — explicação do material: "as duas regras de três").
#   Explicações NOSSAS (o material não explica): D (8 min) = dobrou o tempo duas vezes, uma pelos gatos e outra pelos ratos;
#   E (16 min) = multiplicou quatro gatos por quatro ratos.
# Exemplos nossos (o material não dá números): juros de 10% ao mês sobre R$ 100 (simples: +10 por mês; compostos: 110, 121,
#   133,10 → em 2 meses R$ 21 de juros, em 4 meses R$ 46,41: não dobra); conta de água hipotética (até 10 m³ a R$ 3 o m³,
#   acima disso R$ 6: 10 m³ = R$ 30, 20 m³ = R$ 90); 4 músicos tocam uma música de 5 min (8 músicos não tocam em 2,5);
#   valor unitário: 500 g por R$ 8 (R$ 16/kg) × 1 kg por R$ 14 (R$ 14/kg); unidades: 1 h 30 min = 90 min, não "1,30".
# Pizza de diâmetro dobrado: quatro pizzas pequenas NÃO cabem geometricamente dentro da grande; a tela mostra a grande ao lado
#   de 4 pequenas com "=" (mesma quantidade de pizza: a área), e o quadrado de lado 2 com 4 quadradinhos dentro.
# Nós fazemos (4 situações): receita para 4 → 8 (DÁ: dobra tudo) · lado do terreno dobrou e a área? (NÃO: ×4) ·
#   conta de água por faixa (NÃO) · carro a velocidade constante, distância e tempo (DÁ: dobra o tempo, dobra a distância).
# Frases-chave (meio e fim, idênticas): 1. Dobrar a causa dobra mesmo o efeito? Se não, nada de regra de três.
#   2. Área vai ao quadrado; volume, ao cubo. 3. Resultado estranho? Confira o sentido.
# Atalhos (verde): "reduza a UM: quanto UM faz sozinho?" · "lado ×2 → área ×4; lado ×3 → área ×9" ·
#   "aresta ×2 → volume ×8" · "preço ÷ quantidade = preço de UMA unidade" · "converta primeiro, monte depois".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Quando a regra de três NÃO funciona (o problema dos gatos) · Matemática ENEM, episódio 5"

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
        "{a}Dois gatos caçam dois ratos em dois minutos. [p=0.5] {b}Em quanto tempo *quatro gatos* caçam *quatro ratos?* "
        "[p=0.6] {c}Se você respondeu *quatro minutos,* [p=0.2] ou *um,* [p=0.4] {d}a regra de três te *enganou.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai reconhecer as questões em que a regra de três é uma *armadilha,* [p=0.4] "
        "{b}e ganhar *três hábitos* que pegam a maioria dos erros."),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido, [p=0.2] do episódio três: [p=0.2] o *teste do dobro.* [p=0.4] {a}Dobre uma grandeza "
        "[p=0.2] e veja a outra. [p=0.3] Dobrou também? [p=0.2] *Direta.* [p=0.3] Virou metade? [p=0.2] *Inversa.* [p=0.4] "
        "{b}Quando dobrar uma dobra *exatamente* a outra, [p=0.2] ou corta exatamente pela metade, [p=0.2] as grandezas são "
        "*proporcionais.* [p=0.3] {c}E só aí a regra de três funciona."),

    # ================= A PERGUNTA DE OURO =================
    dict(id="04", block="cotidiano", text=
        "{t}Mas nem tudo na vida é proporcional. [p=0.4] {a}Uma pizza com o *dobro do diâmetro* [p=0.2] não tem o dobro "
        "de pizza: [p=0.2] tem *quatro vezes mais.* [p=0.4] {b}A conta de luz não dobra certinho quando o consumo dobra. "
        "[p=0.4] {c}E nove pessoas não fazem um bebê em *um mês.*"),
    dict(id="05", block="ouro", text=
        "{t}Por isso, antes de qualquer regra de três, [p=0.2] faça a *pergunta de ouro.* [p=0.5] {a}Dobrar a causa "
        "[p=0.2] dobra *mesmo* o efeito? [p=0.5] {b}Se a resposta for *sim,* [p=0.2] pode usar. [p=0.4] {c}Se for *não,* "
        "[p=0.2] ou *depende,* [p=0.3] a regra de três está *fora.*"),

    # ================= BLOCO A: OS GATOS =================
    dict(id="06", block="gatos", text=
        "{t}Vamos aos gatos. [p=0.3] {a}O segredo é olhar o ritmo de *um* gato só. [p=0.4] {b}Dois gatos, dois ratos: "
        "[p=0.2] cada gato caça *um* rato. [p=0.3] {c}E eles caçam *em paralelo,* [p=0.2] ou seja, ao mesmo tempo. [p=0.4] "
        "{d}Então cada gato leva *dois minutos* para pegar o seu rato."),
    dict(id="07", block="gatos", text=
        "{t}Agora, quatro gatos e quatro ratos. [p=0.3] {a}Cada gato continua com *um* rato, [p=0.3] {b}e continua levando "
        "*dois minutos.* [p=0.4] {c}Os quatro cronômetros correm juntos [p=0.2] e param juntos. [p=0.3] *Dois minutos.* "
        "[p=0.4] {d}Dobraram os gatos *e* os ratos ao mesmo tempo: [p=0.2] o ritmo não mudou. [p=0.4] {e}Atalho: [p=0.2] "
        "*reduza a um.* [p=0.2] Quanto *um* faz sozinho?"),

    # ================= BLOCO B: ÁREA E LADO =================
    dict(id="08", block="area", text=
        "{t}E a pizza? [p=0.3] Por que dobrar o diâmetro dá quatro vezes mais? [p=0.4] {a}A quantidade de pizza é a "
        "*área:* [p=0.2] o tamanho da superfície, [p=0.2] quantos quadradinhos cabem nela. [p=0.4] {b}Um quadrado de lado "
        "um tem *um* quadradinho. [p=0.3] {c}Dobre o lado para dois: [p=0.2] cabem dois quadradinhos de largura [p=0.2] e "
        "dois de altura. [p=0.3] *Quatro.*"),
    dict(id="09", block="area", text=
        "{t}Com a pizza é igual. [p=0.3] {a}A pizza grande tem a mesma quantidade que *quatro pizzas pequenas.* [p=0.4] "
        "{b}A área depende do lado *vezes ele mesmo.* [p=0.2] Por isso essa relação se chama *quadrática.* [p=0.4] "
        "{c}Atalho: [p=0.2] lado vezes dois, [p=0.2] área vezes *quatro.* [p=0.3] Lado vezes três, [p=0.2] área vezes "
        "*nove.*"),

    # ================= BLOCO C: VOLUME E ARESTA =================
    dict(id="10", block="volume", text=
        "{t}E com uma caixa? [p=0.4] {a}O *volume* é o espaço que cabe dentro: [p=0.2] quantos cubinhos enchem a caixa. "
        "[p=0.3] {b}A *aresta* é cada lado do cubo. [p=0.4] {c}Dobre a aresta: [p=0.2] dois de largura, [p=0.2] dois de "
        "altura, [p=0.2] dois de fundo. [p=0.3] Dois vezes dois vezes dois: [p=0.2] *oito cubinhos.* [p=0.4] {d}Aresta "
        "vezes dois, [p=0.2] volume vezes *oito.*"),

    # ================= BLOCO D: JUROS COMPOSTOS =================
    dict(id="11", block="juros", text=
        "{t}E o dinheiro guardado? [p=0.4] {a}Nos *juros simples,* [p=0.2] o rendimento é sempre calculado sobre o valor "
        "inicial. [p=0.3] Cem reais a dez por cento ao mês: [p=0.2] *dez reais* todo mês. [p=0.3] Isso é proporcional ao "
        "tempo. [p=0.4] {b}Nos *juros compostos,* [p=0.2] os juros de cada mês entram na conta do mês seguinte: [p=0.2] "
        "*juros sobre juros.* [p=0.3] Cento e dez, [p=0.2] cento e vinte e um, [p=0.2] cento e trinta e três e dez. "
        "[p=0.4] {c}Esse crescimento cada vez mais rápido é o *exponencial.* [p=0.3] Dobrar o tempo não dobra os juros: "
        "[p=0.2] {d}regra de três, *só nos simples.*"),

    # ================= BLOCO E: TARIFAS POR FAIXA =================
    dict(id="12", block="faixa", text=
        "{t}E a conta de água? [p=0.4] {a}Muitas cidades cobram por *faixa:* [p=0.2] o preço do metro cúbico muda "
        "conforme o consumo. [p=0.4] {b}Imagine: [p=0.2] até dez metros cúbicos, [p=0.2] *três reais* cada. [p=0.3] Acima "
        "disso, [p=0.2] *seis reais* cada. [p=0.4] {c}Dez metros cúbicos: [p=0.2] trinta reais. [p=0.3] {d}Vinte metros "
        "cúbicos: [p=0.2] trinta, [p=0.2] mais dez vezes seis, [p=0.2] *noventa.* [p=0.4] {e}O consumo dobrou, [p=0.2] e a "
        "conta *triplicou.* [p=0.3] Não existe uma razão única."),

    # ================= BLOCO F: TAREFAS INDIVISÍVEIS =================
    dict(id="13", block="indivisivel", text=
        "{t}E tem trabalho que não se divide. [p=0.4] {a}Quatro músicos tocam uma música de *cinco minutos.* [p=0.3] {b}Com "
        "oito músicos, [p=0.2] a música dura dois minutos e meio? [p=0.4] {c}Claro que não. [p=0.3] Continua com cinco. "
        "[p=0.4] {d}Isso é uma *tarefa indivisível:* [p=0.2] mais gente não deixa mais rápido. [p=0.3] Como o bebê, "
        "[p=0.2] que leva nove meses, [p=0.2] não importa quantas pessoas ajudem."),

    # ================= BLOCO G: OS 3 HÁBITOS =================
    dict(id="14", block="habitos", text=
        "{t}Agora, os *três hábitos de prova.* [p=0.4] {a}Hábito um: [p=0.2] confira a *plausibilidade,* [p=0.2] ou seja, "
        "se o resultado faz sentido. [p=0.4] {b}Mais operários deram *mais* dias? [p=0.3] Você inverteu. [p=0.4] {c}Correr "
        "mais rápido aumentou o tempo da viagem? [p=0.3] Mesmo erro. [p=0.3] Três segundos de conferência pegam essa troca."),
    dict(id="15", block="habitos", text=
        "{t}Hábito dois: [p=0.2] *reduza ao valor unitário,* [p=0.2] o valor de *uma* unidade. [p=0.4] {a}Um pacote de "
        "quinhentos gramas custa *oito reais.* [p=0.3] {b}Outro, de um quilo, [p=0.2] custa *catorze.* [p=0.3] Qual compensa? "
        "[p=0.4] {c}O primeiro sai a *dezesseis reais o quilo.* [p=0.3] {d}O segundo, a *catorze.* [p=0.3] O de um quilo "
        "compensa. [p=0.4] {e}Atalho: [p=0.2] preço dividido pela quantidade [p=0.2] dá o preço de *uma* unidade."),
    dict(id="16", block="habitos", text=
        "{t}Hábito três: [p=0.2] *padronize as unidades* antes de tudo. [p=0.4] {a}Uma hora e meia não é *um vírgula "
        "trinta.* [p=0.3] {b}São *noventa minutos.* [p=0.4] {c}Com unidades misturadas, [p=0.2] a conta fecha [p=0.2] e o "
        "resultado sai errado, [p=0.2] sem nenhum alarme. [p=0.4] {d}Atalho: [p=0.2] *converta primeiro,* [p=0.2] monte "
        "depois."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Quatro situações. [p=0.3] Dá para usar regra de três? [p=0.4] {a}Um: [p=0.2] uma receita para "
        "quatro pessoas, [p=0.2] adaptada para oito. [p=0.3] {b}Dois: [p=0.2] o lado de um terreno dobrou. [p=0.2] E a "
        "área? [p=0.3] {c}Três: [p=0.2] uma conta de água com tarifa por faixa. [p=0.3] {d}Quatro: [p=0.2] um carro a "
        "velocidade constante: [p=0.2] distância e tempo. [p=0.4] {e}*Pause o vídeo e responda.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos conferir, [p=0.2] com a pergunta de ouro. [p=0.3] {a}A receita: [p=0.2] o dobro de pessoas pede o dobro "
        "de cada ingrediente. [p=0.2] *Dá.* [p=0.4] {b}O terreno: [p=0.2] lado dobrado, [p=0.2] área vezes quatro. "
        "[p=0.2] *Não dá.* [p=0.4] {c}A conta por faixa: [p=0.2] o preço muda no caminho. [p=0.2] *Não dá.* [p=0.4] {d}E o "
        "carro: [p=0.2] o dobro do tempo, [p=0.2] o dobro da distância. [p=0.2] *Dá.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dobrar a causa dobra *mesmo* o efeito? [p=0.2] Se não, "
        "nada de regra de três. [p=0.5] {b}Dois: [p=0.2] área vai ao quadrado; [p=0.2] volume, ao cubo. [p=0.5] {c}Três: "
        "[p=0.2] resultado estranho? [p=0.2] Confira o sentido."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dobrar gatos e ratos, [p=0.2] e *dobrar o "
        "tempo.* [p=0.4] {b}Parece certo, [p=0.2] porque mais ratos parecem dar mais trabalho. [p=0.4] {c}Mas os gatos "
        "também dobraram: [p=0.2] cada um continua com um rato, [p=0.2] no mesmo tempo."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] usar regra de três na *área* [p=0.2] a partir do lado. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "o terreno ficou maior, [p=0.2] então a área deveria crescer igual. [p=0.4] {c}Mas a área vai ao quadrado: [p=0.2] "
        "lado vezes dois, [p=0.2] área vezes quatro."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] usar regra de três em *juros compostos.* [p=0.4] {b}Parece certo, [p=0.2] porque mais tempo "
        "dá mais juros. [p=0.4] {c}Mas os juros crescem sobre os juros: [p=0.2] regra de três, *só nos simples.*"),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] *não conferir* se o resultado faz sentido. [p=0.4] {b}Parece certo, [p=0.2] porque a conta "
        "fechou sem erro. [p=0.4] {c}Mas uma conta perfeita pode resolver o problema trocado: [p=0.2] confira o sentido "
        "antes de marcar."),

    # ================= QUESTÃO 8 DO MATERIAL =================
    dict(id="24", block="q8", text=
        "{t}Agora, a *prova oficial* do gancho, [p=0.2] numa questão no estilo do ENEM, [p=0.2] do nosso material de "
        "estudo. [p=0.4] {a}Dois gatos caçam dois ratos em dois minutos. [p=0.3] {b}Mantido esse mesmo ritmo de caça, "
        "[p=0.2] quatro gatos caçarão quatro ratos em: [p=0.4] {qa}A: [p=0.2] um minuto. [p=0.3] {qb}B: [p=0.2] dois "
        "minutos. [p=0.3] {qc}C: [p=0.2] quatro minutos. [p=0.3] {qd}D: [p=0.2] oito minutos. [p=0.3] {qe}E: [p=0.2] "
        "dezesseis minutos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q8", text=
        "{t}Pergunta de ouro: [p=0.2] dobrar os gatos dobra *mesmo* o tempo? [p=0.3] Não. [p=0.4] {a}Então, ritmo "
        "individual: [p=0.2] cada gato, um rato, [p=0.2] dois minutos. [p=0.3] {b}Com quatro gatos e quatro ratos, "
        "[p=0.2] nada muda. [p=0.3] {ok}*Dois minutos. Letra B!*"),
    dict(id="26", block="q8", text=
        "{t}E repare nas armadilhas. [p=0.3] {xa}A A é a regra de três *inversa,* [p=0.2] olhando só os gatos: [p=0.2] o "
        "dobro de gatos, [p=0.2] metade do tempo. [p=0.4] {xc}A C é a regra de três *direta,* [p=0.2] olhando só os ratos: "
        "[p=0.2] o dobro de ratos, [p=0.2] o dobro do tempo. [p=0.4] {m}As duas regras de três possíveis, [p=0.2] e as duas "
        "*erradas,* [p=0.2] porque causa e efeito dobraram juntos. [p=0.4] {xd}A D dobrou o tempo duas vezes, [p=0.2] "
        "{xe}e a E multiplicou quatro por quatro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dobrar a causa dobra *mesmo* o efeito? [p=0.2] Se "
        "não, nada de regra de três. [p=0.5] {b}Dois: [p=0.2] área vai ao quadrado; [p=0.2] volume, ao cubo. [p=0.5] "
        "{c}Três: [p=0.2] resultado estranho? [p=0.2] Confira o sentido."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.2] {c}caçamos as pegadinhas [p=0.2] {d}e "
        "treinamos com *questões novas.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você tinha respondido quatro minutos para os gatos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
