# Nós, os Antigos — Vídeo 02: "Por Que os Antigos Não Conseguiam Parar de Olhar?"
# Base: original/fontes.md (cada fato tem fonte; o que é moldura do museu de 2526 está marcado como FICÇÃO em `tela`).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso.
# Estrutura do modelo de episódio: vitrine → estranhamento → ciência → abismo → virada → etiqueta.

TITULO = "Por Que os Antigos Não Conseguiam Parar de Olhar?"

VOZ = dict(
    voiceName="Zephyr",
    tags=["curiosa", "gentil"],
    prompt=("Narre um documentário de ciência animado: voz feminina adulta, calma, curiosa e acolhedora, de uma "
            "curadora de museu que admira o que está mostrando. Tom de quem conta um segredo fascinante, com humor "
            "leve e seco nas frases irônicas. Ritmo tranquilo, sem pressa, com as pausas marcadas. Nada de tom "
            "acusador: mesmo nas partes sombrias, a voz continua serena e carinhosa com os Antigos. Leia apenas o "
            "texto, exatamente como está escrito, sem acrescentar, pular ou repetir nada."),
)

# só no texto enviado à voz (a legenda e a tela usam a grafia normal)
PRONUNCIA = {"Brichter": "Bríkter", "Schultz": "Shults", "Allcott": "Ólcot"}

SCENES = [
    # ── A VITRINE ─────────────────────────────────────────────
    dict(id="01", block="vitrine",
         tela="Escuro. Um holofote acende sobre a vitrine 002: o mesmo retângulo de vidro e metal, agora em pé e ACESO, "
              "jogando luz azulada no vidro. Etiqueta: PEÇA Nº 002 · c. 2026 d.C. (FICÇÃO: o museu)",
         text=
        "{a}Esta é a peça número dois. [p=0.3] "
        "{b}À primeira vista, é igual à peça número um: [p=0.1] um retângulo de vidro e metal. [p=0.3] "
        "{c}A diferença é que esta foi reconstituída *acesa.* [p=0.3] "
        "{d}Porque era assim que os Antigos mais a viam: [p=0.1] acesa, [p=0.1] a um palmo do rosto."),
    dict(id="02", block="vitrine",
         tela="A câmera recua: o salão do museu. A Lume entra pulando, acena e aponta a vitrine. Logo: NÓS, OS ANTIGOS. "
              "Placa do salão: ALA 01 · O QUE PRENDIA OS OLHOS (FICÇÃO)",
         text=
        "{a}Bem-vindos de volta ao Museu da Era dos Antigos. [p=0.2] {b}Eu sou a Lume, a curadora. [p=0.3] "
        "{c}Hoje a pergunta é: [p=0.2] *por que eles não conseguiam parar de olhar?*"),

    # ── O ESTRANHAMENTO ──────────────────────────────────────
    dict(id="03", block="estranhamento",
         tela="Reconstituição quente: rua cheia de Antigos, todos de cabeça baixa, rostos iluminados de baixo pelo "
              "celular. Contador 5,78 BILHÕES. Relógio de 24 h que se pinta de azul: 6 h 38 min por dia online "
              "(DataReportal/GWI). Fatia de mais de 1/3 do dia acordado.",
         text=
        "{a}Por volta de dois mil e vinte e cinco, [p=0.1] *cinco bilhões e setecentos e oitenta milhões* de Antigos "
        "usavam celular. [p=0.3] "
        "{b}E os adultos conectados passavam, em média, [p=0.1] *mais de seis horas e meia por dia* na internet. [p=0.2] "
        "{c}Mais de um terço do tempo em que estavam acordados. [p=0.4] "
        "{d}Nas reconstituições, [p=0.1] a postura é inconfundível: [p=0.2] pescoço dobrado, [p=0.1] rosto iluminado "
        "de baixo para cima."),
    dict(id="04", block="estranhamento",
         tela="Um Antigo de pé; o bolso da calça treme com ondas de vibração… mas o celular está na mesa, apagado. "
              "Contador 89% sobre 290 universitários (Drouin et al., 2012). Rótulo: VIBRAÇÃO FANTASMA.",
         text=
        "{a}O retângulo entrou tão fundo na vida deles [p=0.1] que o corpo começou a inventar o retângulo. [p=0.3] "
        "{b}Em dois mil e doze, uma pesquisa com duzentos e noventa universitários americanos perguntou: [p=0.2] "
        "você já sentiu o celular vibrar no bolso [p=0.1] sem que ele tivesse vibrado? [p=0.3] "
        "{c}*Oitenta e nove por cento* disseram que sim. [p=0.3] "
        "{d}Os Antigos chamavam isso de *vibração fantasma.*"),

    # ── A CIÊNCIA ────────────────────────────────────────────
    dict(id="05", block="ciencia",
         tela="Uma chuva de informação (ícones, manchetes, vídeos) cai sobre um Antigo; a atenção dele é uma "
              "ampulheta pequena que esvazia. Citação: 'A riqueza de informação cria uma pobreza de atenção' — Herbert "
              "Simon, 1971.",
         text=
        "{a}Para entender esta peça, [p=0.1] precisamos de uma ideia de um economista dos Antigos, [p=0.1] Herbert "
        "Simon, [p=0.1] de mil novecentos e setenta e um. [p=0.3] "
        "{b}Quando a informação fica abundante, [p=0.2] alguma coisa fica escassa: [p=0.2] {c}*a atenção* de quem "
        "recebe."),
    dict(id="06", block="ciencia",
         tela="O celular vira uma vitrine de loja: o Antigo do lado de dentro, anúncios do lado de fora olhando para "
              "ele. Pizza: 97,6% da receita da Meta em 2025 = publicidade (Form 10-K).",
         text=
        "{a}Meio século depois, [p=0.1] a atenção virou o produto. [p=0.3] "
        "{b}Os aplicativos mais usados eram de graça. [p=0.2] Quem pagava eram os anunciantes, [p=0.1] por cada "
        "olhar. [p=0.3] "
        "{c}Em dois mil e vinte e cinco, [p=0.1] *noventa e sete por cento* do dinheiro da Meta, [p=0.1] a dona do "
        "Facebook e do Instagram, [p=0.1] veio de publicidade. [p=0.3] "
        "{d}Quanto mais tempo olhando, [p=0.1] mais anúncios vistos."),
    dict(id="07", block="ciencia",
         tela="Caixa de Skinner estilizada com um rato fofo e uma alavanca. Lado A: comida toda vez → o rato aperta e "
              "vai dormir. Lado B: comida às vezes (ponto de interrogação) → o rato aperta sem parar. Depois uma "
              "máquina de apostas de três rolos ao lado. Fonte: Skinner, 1953.",
         text=
        "{a}E como se prende a atenção de alguém? [p=0.3] Os cientistas dos Antigos já desconfiavam havia muito "
        "tempo. [p=0.3] "
        "{b}O psicólogo B. F. Skinner colocava ratos numa caixa com uma alavanca. [p=0.3] "
        "{c}Se a alavanca dava comida toda vez, [p=0.1] o rato comia [p=0.1] e ia cuidar da vida. [p=0.3] "
        "{d}Mas, se a comida vinha só às vezes, [p=0.1] depois de um número imprevisível de apertões, [p=0.2] o rato "
        "apertava sem parar. [p=0.2] E continuava apertando mesmo quando a comida acabava. [p=0.4] "
        "{e}O próprio Skinner comparou isso às máquinas de apostas."),
    dict(id="08", block="ciencia",
         tela="Cérebro estilizado; um neurônio de dopamina pisca. 1) recompensa surpresa → flash na recompensa. "
              "2) uma luz passa a anunciar a recompensa → o flash migra para a luz. Fonte: Schultz et al., Science, "
              "1997 (macacos). Depois: som, luz, número vermelho no canto do celular.",
         text=
        "{a}Dentro do cérebro, [p=0.1] a história é parecida. [p=0.3] "
        "{b}Em mil novecentos e noventa e sete, [p=0.1] o neurocientista Wolfram Schultz mostrou que neurônios de "
        "dopamina em macacos disparavam com uma recompensa inesperada. [p=0.3] "
        "{c}Mas, quando um sinal passava a anunciar a recompensa, [p=0.2] o disparo mudava de lugar: [p=0.2] ia para "
        "o sinal. [p=0.4] "
        "{d}O cérebro reagia *à promessa.* [p=0.3] "
        "{e}E o retângulo estava cheio de sinais: [p=0.2] um som, [p=0.1] uma luz, [p=0.1] um numerozinho vermelho "
        "no canto."),
    dict(id="09", block="ciencia",
         tela="Mão puxa a tela para baixo; o ícone de atualizar gira como os rolos de uma máquina de apostas: às vezes "
              "novidade, às vezes nada. Rótulo: PUXAR PARA ATUALIZAR · 2009. Depois um coração de curtida explode "
              "em faíscas. Fonte: The Guardian, 2017.",
         text=
        "{a}Algumas das pessoas que desenharam o retângulo [p=0.1] sabiam bem disso. [p=0.3] "
        "{b}Em dois mil e nove, Loren Brichter inventou o gesto de puxar a tela para baixo para atualizar. [p=0.2] "
        "Você puxa, [p=0.1] espera um instante, [p=0.2] e às vezes vem novidade. [p=0.2] Às vezes, não. [p=0.3] "
        "{c}Anos depois, [p=0.1] ele mesmo disse que esses recursos viciam. [p=0.4] "
        "{d}Justin Rosenstein ajudou a criar o botão de curtir. [p=0.2] Ele chamou as curtidas de [p=0.1] *toques "
        "brilhantes de pseudoprazer.*"),
    dict(id="10", block="ciencia",
         tela="Página antiga com fim e botão 'PRÓXIMA PÁGINA'. Depois o fundo da página some e o feed desce para "
              "sempre, num poço sem fundo. Rótulo: ROLAGEM INFINITA · 2006.",
         text=
        "{a}Em dois mil e seis, [p=0.1] Aza Raskin inventou a *rolagem infinita.* [p=0.3] "
        "{b}Antes dela, as páginas tinham fim. [p=0.2] Você chegava lá embaixo [p=0.1] e precisava decidir se queria "
        "mais. [p=0.3] "
        "{c}Com ela, [p=0.1] o fundo da página sumiu. [p=0.2] E, sem fundo, [p=0.1] não tinha onde parar. [p=0.4] "
        "{d}Anos depois, [p=0.1] Raskin disse que se arrependia."),
    dict(id="11", block="ciencia",
         tela="Duas semanas lado a lado num calendário: semana barulhenta (celular na mão, sininhos piscando) e semana "
              "silenciosa (celular na gaveta). Medidor de desatenção mais alto na barulhenta. Fonte: Kushlev et al., "
              "CHI 2016 · 221 universitários.",
         text=
        "{a}E o retângulo não esperava ser chamado. [p=0.2] *Ele chamava.* [p=0.3] "
        "{b}Em dois mil e dezesseis, pesquisadores no Canadá publicaram um experimento com duzentos e vinte e um "
        "universitários. [p=0.2] Uma semana com todas as notificações ligadas e o celular por perto. [p=0.2] Outra "
        "semana com tudo silenciado e o celular guardado. [p=0.3] "
        "{c}Na semana barulhenta, [p=0.1] eles relataram mais desatenção e mais agitação. [p=0.3] "
        "{d}Não era doença. [p=0.2] Era o ambiente."),
    dict(id="12", block="ciencia",
         tela="Cronômetro sobre uma tela de computador de escritório: 2004 → 2 min 30 s numa tela antes de trocar; "
              "a partir de 2016 → ~47 s. Janelas pulando uma atrás da outra. Fonte: Gloria Mark, 'Attention Span', "
              "2023.",
         text=
        "{a}A psicóloga Gloria Mark passou anos cronometrando trabalhadores de escritório na frente do computador. [p=0.3] "
        "{b}Em dois mil e quatro, [p=0.1] eles ficavam em média *dois minutos e meio* numa tela antes de pular para "
        "outra. [p=0.3] "
        "{c}Nos estudos a partir de dois mil e dezesseis, [p=0.1] a média caiu para uns *quarenta e sete "
        "segundos.* [p=0.4] "
        "{d}A atenção dos Antigos tinha virado uma bolinha de pingue-pongue."),

    # ── O ABISMO ────────────────────────────────────────────
    dict(id="13", block="abismo",
         tela="Volta ao museu, luz mais baixa. A Lume diante de um painel: citação de Steve Jobs (NYT, 2014) e de "
              "Tristan Harris (Guardian, 2017). Depois o celular visto de trás: do outro lado do vidro, um placar "
              "gigante 'TEMPO OLHANDO' subindo.",
         text=
        "{a}Agora, [p=0.1] a parte que mais intriga os pesquisadores deste museu. [p=0.3] "
        "{b}No fim de dois mil e dez, [p=0.1] um jornalista perguntou a Steve Jobs, [p=0.1] o chefe da Apple, [p=0.1] "
        "se os filhos dele adoravam o iPad. [p=0.3] "
        "{c}A resposta: [p=0.2] *eles ainda não usaram.* [p=0.2] *Nós limitamos quanta tecnologia nossos filhos usam "
        "em casa.* [p=0.4] "
        "{d}Um ex-funcionário do Google, Tristan Harris, [p=0.1] resumiu assim: [p=0.2] *todas as nossas mentes "
        "podem ser sequestradas.* [p=0.4] "
        "{e}Os Antigos não eram fracos. [p=0.3] *Eram o alvo.* [p=0.3] Do outro lado da tela havia empresas que "
        "ganhavam mais [p=0.1] quanto mais tempo eles ficassem olhando."),

    # ── A VIRADA ────────────────────────────────────────────
    dict(id="14", block="virada",
         tela="A luz volta a subir. Reconstituição: um Antigo desliga o Facebook; o calendário avança 4 semanas; ele "
              "aparece numa mesa com família e amigos. Barras: bem-estar sobe um pouco; uso depois cai. Fonte: Allcott "
              "et al., American Economic Review, 2020.",
         text=
        "{a}Mas a peça número dois não é só sobre uma armadilha. [p=0.2] *É também sobre a saída.* [p=0.3] "
        "{b}Em dois mil e dezoito, [p=0.1] economistas americanos sortearam usuários do Facebook [p=0.1] e pagaram "
        "para que eles desativassem a conta por quatro semanas. [p=0.3] "
        "{c}Quem desativou passou mais tempo com a família e com os amigos. [p=0.2] E se sentiu um pouco "
        "melhor. [p=0.3] "
        "{d}Depois do experimento, [p=0.1] continuou usando menos."),
    dict(id="15", block="virada",
         tela="Mapa-múndi: Brasil acende (Lei 15.100, jan/2025: celular restrito nas escolas, inclusive no recreio) e "
              "Austrália acende (10/12/2025: menores de 16 sem conta nas principais redes). Pátio de escola com "
              "crianças brincando.",
         text=
        "{a}E os Antigos começaram a mudar as regras do jogo. [p=0.3] "
        "{b}Em janeiro de dois mil e vinte e cinco, [p=0.1] o Brasil aprovou uma lei que restringiu o celular dos "
        "alunos nas escolas, [p=0.1] inclusive no recreio. [p=0.3] "
        "{c}Em dezembro do mesmo ano, [p=0.1] a Austrália proibiu menores de dezesseis anos de ter conta nas "
        "principais redes sociais. [p=0.4] "
        "{d}Ninguém sabia ainda o resultado. [p=0.2] Mas, pela primeira vez, [p=0.1] eles estavam redesenhando o "
        "ambiente."),
    dict(id="16", block="virada",
         tela="Close no celular: sininho de notificação riscado, celular indo para uma gaveta. Depois o retângulo "
              "mostra mapas, músicas, uma chamada de vídeo com a avó. Ícone de cadeado: 'quem decide quando ele "
              "chama'.",
         text=
        "{a}Dentro de casa, [p=0.1] o que ajudou no experimento do Canadá foi simples: [p=0.2] silenciar as "
        "notificações [p=0.1] e deixar o celular longe da mão. [p=0.4] "
        "{b}O retângulo nunca foi o vilão. [p=0.2] Era uma ferramenta incrível: [p=0.2] guardava mapas, [p=0.1] "
        "músicas, [p=0.1] a voz de quem eles amavam. [p=0.3] "
        "{c}O problema era quem decidia *quando ele chamava.* [p=0.3] "
        "{d}E isso, [p=0.1] os Antigos podiam tomar de volta."),

    # ── A ETIQUETA ───────────────────────────────────────────
    dict(id="17", block="etiqueta",
         tela="A Lume desliga a tela da peça 002. Close na etiqueta de museu, escrita à máquina, linha por linha: "
              "PEÇA Nº 002 · Retângulo brilhante · Século 21 d.C. · a frase final. (FICÇÃO)",
         text=
        "{a}Então, [p=0.1] vamos à etiqueta da *peça número dois.* [p=0.3] "
        "{b}Retângulo brilhante. [p=0.2] Século vinte e um. [p=0.4] "
        "{c}*Foi desenhado para nunca acabar.* [p=0.4] "
        "{d}*Os Antigos aprenderam a pôr um fim.*"),
    dict(id="18", block="proxima",
         tela="A Lume caminha até a próxima vitrine, coberta por um pano; por baixo, a silhueta de uma nota de "
              "dinheiro. Texto: PRÓXIMA PEÇA · Nº 003. Pergunta na tela: 'Quanto tempo de tela o seu celular marcou "
              "ontem?'",
         text=
        "{a}Na próxima vitrine: [p=0.2] um pedaço de papel que os Antigos trocavam por quase tudo. [p=0.4] "
        "{b}E você? [p=0.2] Quanto tempo de tela o seu retângulo marcou ontem? [p=0.2] {c}Conta aqui nos "
        "comentários. [p=0.2] Eu leio todos."),
]
