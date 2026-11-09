# Estudativo · FIS-ELE-008 — Corrente elétrica (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: calcular i = Q/Δt, usar a área do gráfico i × t, ler a carga de uma bateria em mAh e separar corrente
# contínua de alternada.
# Pré-requisitos: FIS-ELE-001 (carga, elétrons, condutor), FIS-CIN-012 (área do gráfico v × t). Próxima: FIS-ELE-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. FIS-ELE-002 a 007 NÃO estão em "Já ensinado" desta aula: nada de tensão, ddp ou
# potencial; "o que empurra a corrente" fica como assunto da próxima aula. Rede elétrica brasileira: 60 Hz, dita como
# "vai e volta sessenta vezes por segundo" (60 ciclos). Sentido convencional: escolhido antes da descoberta do elétron (1897).
# Contas: 30/10 = 3 A; 2·5 = 10 C; 4·2/2 = 4 C; 1 mAh = 1e-3·3600 = 3,6 C; 4 Ah = 14 400 C; 3000/300 = 10 h;
# 4000 mAh = 400 mA × 10 h = 2000 mA × 2 h; 5 Ah = 18 000 C; 5000/500 = 10 h.

TITULO = "Corrente elétrica"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="A bateria do seu celular tem {a}quatro mil miliampères-hora. [p=0.3] Isso {b}não é corrente [p=0.1] e {c}não é energia. [p=0.3] {d}É carga elétrica."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a corrente, [p=0.2] {b}tirar a carga da área de um gráfico, [p=0.2] {c}ler o miliampère-hora da bateria [p=0.1] e {d}separar corrente contínua de alternada."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}carga se mede em coulomb, e num metal quem anda são os elétrons; [p=0.3] e {c}no gráfico da velocidade pelo tempo, a área embaixo da linha é o deslocamento. [p=0.3] Se faltar alguma, procure no canal."),
    # corrente
    dict(id="s04", block="corrente", text="Num fio de metal, os elétrons andam soltos, {a}para todo lado. [p=0.3] {b}Ligue o fio a uma pilha, [p=0.1] e {c}eles passam a andar num sentido só. [p=0.3] Esse movimento organizado de cargas é a {d}corrente elétrica."),
    dict(id="s05", block="corrente", text="A corrente mede {a}quanta carga passa por um ponto do fio a cada segundo: [p=0.2] {b}i igual a quê dividido por delta tê. [p=0.3] {c}I é a corrente, em ampère; [p=0.2] {d}quê é a carga que passou, em coulomb; [p=0.2] {e}delta tê é o intervalo de tempo, em segundo. [p=0.3] {f}Um ampère é um coulomb por segundo."),
    dict(id="s06", block="corrente", text="Passam {a}trinta coulombs em {b}dez segundos: [p=0.2] {c}trinta dividido por dez, [p=0.1] {d}três ampères: [p=0.1] três coulombs passando a cada segundo."),
    dict(id="s07", block="corrente", text="Um detalhe de prova: [p=0.2] {a}o sentido da corrente é o de uma carga positiva. [p=0.2] {b}Ela sai do polo positivo da pilha, que é a ponta marcada com mais, [p=0.1] dá a volta e chega no polo negativo. [p=0.3] {c}Os elétrons andam ao contrário. [p=0.2] É o {d}sentido convencional, combinado antes de se descobrir o elétron."),
    # gráfico
    dict(id="s08", block="grafico", text="Quando a corrente muda, use {a}o gráfico da corrente pelo tempo. [p=0.2] {b}Como no gráfico da velocidade, a área embaixo da linha dá o que se acumula: [p=0.2] {c}a carga. [p=0.3] Corrente de {d}dois ampères por cinco segundos: [p=0.2] {e}um retângulo de cinco por dois, dez coulombs."),
    dict(id="s09", block="grafico", text="{a}Depois, a corrente cai de dois a zero em quatro segundos. [p=0.2] {b}A área é um triângulo: quatro vezes dois, dividido por dois, [p=0.1] {c}quatro coulombs. [p=0.3] {d}No total, catorze coulombs."),
    # bateria
    dict(id="s10", block="bateria", text="Agora, a bateria. [p=0.2] {a}Miliampère-hora é corrente vezes tempo, [p=0.1] e {b}corrente vezes tempo é carga. [p=0.3] {c}Um miliampère-hora é um milésimo de ampère durante uma hora, [p=0.1] ou três mil e seiscentos segundos: [p=0.2] {d}três vírgula seis coulombs."),
    dict(id="s11", block="bateria", text="{a}Quatro mil miliampères-hora são quatro ampères-hora. [p=0.2] {b}Quatro vezes três mil e seiscentos: [p=0.1] {c}catorze mil e quatrocentos coulombs. [p=0.3] {d}É a carga que a bateria entrega até descarregar."),
    # contínua e alternada
    dict(id="s12", block="tipos", text="Por fim, os dois tipos de corrente. [p=0.2] {a}Na pilha e na bateria, a corrente tem sempre o mesmo sentido: [p=0.1] {b}é a corrente contínua. [p=0.3] {c}Na tomada de casa, ela vai e volta, [p=0.1] {d}sessenta vezes por segundo no Brasil: [p=0.1] {e}é a corrente alternada. [p=0.3] {f}O carregador do celular transforma a alternada em contínua."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que miliampère-hora é corrente. [p=0.3] {b}A bateria de quatro mil miliampères-hora não fornece quatro mil miliampères. [p=0.3] {c}Ela pode dar quatrocentos miliampères por dez horas, [p=0.1] {d}ou dois mil por duas horas. [p=0.3] {e}O que não muda é a carga."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}quanto tempo a bateria dura? [p=0.2] {b}Divida a capacidade em miliampère-hora pela corrente em miliampère. [p=0.3] {c}Miliampère corta com miliampère, [p=0.1] e sobra hora. [p=0.3] {d}Três mil miliampères-hora, gastando quinhentos miliampères: [p=0.1] {e}seis horas."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a carga é corrente vezes tempo, [p=0.1] e o tempo é a carga dividida pela corrente. [p=0.3] {b}Não compensa quando a corrente muda com o tempo: [p=0.2] aí, use a área do gráfico."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma bateria portátil tem {a}cinco mil miliampères-hora. [p=0.3] {b}Quantos coulombs ela guarda? [p=0.3] {c}E por quantas horas ela alimenta um aparelho que puxa {d}quinhentos miliampères?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco mil miliampères-hora são cinco ampères-hora. [p=0.2] {b}Cinco vezes três mil e seiscentos: [p=0.1] {c}dezoito mil coulombs. [p=0.3] {d}O tempo: cinco mil dividido por quinhentos, [p=0.1] {e}dez horas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}corrente é carga dividida pelo tempo, em ampère; [p=0.2] {b}no gráfico da corrente pelo tempo, a área é a carga; [p=0.2] e {c}miliampère-hora é carga, não corrente."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}o que empurra a corrente, a tensão, [p=0.2] e {b}a resistência, com a primeira lei de Ohm. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
