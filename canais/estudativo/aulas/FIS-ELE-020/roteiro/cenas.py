# Estudativo · FIS-ELE-020 — Gerador real: força eletromotriz (Física · Eletricidade · Geradores e receptores).
# Habilidade: usar U = ε − r·i, ler o gráfico U × i e calcular o rendimento de uma bateria.
# Pré-requisitos: FIS-ELE-009 (U = R·i, ddp), FIS-ELE-017 (P = U·i, R·i²), FIS-ENE-002 (rendimento), MAT-FUN-012. Próxima: FIS-ELE-021.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# ε narrado "épsilon"; r interna = "erre pequeno". Curto-circuito (FIS-ELE-014) só definido como U = 0 e citado como outra aula.
# Medidores (FIS-ELE-015) não estão em "Já ensinado": o gancho fala em "tensão nos polos", sem voltímetro.
# Contas: 0,5·6 = 3; 12 − 3 = 9 V; i_cc = 12/0,5 = 24 A; Pt = 12·6 = 72 W; Pu = 9·6 = 54 W; Pd = 0,5·36 = 18 W; 54/72 = 9/12 = 75 %.
#   Questão: r = 10/5 = 2 Ω; U = 10 − 2·1 = 8 V; 8/10 = 80 %.

TITULO = "Gerador real: força eletromotriz"

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
    dict(id="s01", block="gancho", text="{a}Uma pilha nova traz escrito: um vírgula cinco volts. [p=0.2] {b}Ligue nela um brinquedo que puxa muita corrente, [p=0.1] e {c}a tensão nos polos cai. [p=0.3] {d}Parte da tensão se perde {e}dentro da própria pilha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular essa perda, [p=0.2] {b}ler o gráfico de um gerador [p=0.1] e {c}achar o rendimento de uma bateria."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a tensão é a resistência vezes a corrente; [p=0.2] {c}a potência é a tensão vezes a corrente; [p=0.2] e {d}o rendimento é a potência útil dividida pela total. [p=0.3] Se faltar alguma, procure no canal."),
    # gerador e fem
    dict(id="s04", block="fem", text="{a}Gerador é o que transforma outra energia em energia elétrica: [p=0.2] {b}a pilha usa uma reação química; [p=0.1] {c}a usina, o giro de uma turbina. [p=0.3] {d}A tensão que ele cria se chama força eletromotriz, [p=0.1] {e}a letra grega épsilon, em volt."),
    dict(id="s05", block="fem", text="{a}Apesar do nome, ela não é uma força: [p=0.2] {b}é a energia que o gerador dá a cada coulomb de carga. [p=0.3] {c}Uma pilha de um vírgula cinco volts dá um vírgula cinco joule a cada coulomb."),
    # resistência interna
    dict(id="s06", block="interna", text="Mas {a}a corrente também atravessa o gerador por dentro, [p=0.2] e lá dentro {b}existe uma resistência: [p=0.1] {c}a resistência interna, erre pequeno. [p=0.3] {d}Nela se perde uma tensão de erre pequeno vezes i, [p=0.1] {e}que vira calor. [p=0.2] Por isso a pilha esquenta quando trabalha muito."),
    dict(id="s07", block="interna", text="Sobra para fora {a}u igual a épsilon menos erre pequeno vezes i. [p=0.3] {b}A letra u é a tensão útil, nos polos; [p=0.1] {c}épsilon, a força eletromotriz; [p=0.1] {d}erre pequeno, a resistência interna, em ohm; [p=0.1] e {e}i, a corrente, em ampère."),
    dict(id="s08", block="interna", text="Exemplo: {a}uma bateria de doze volts, com resistência interna de meio ohm, [p=0.1] fornece {b}seis ampères. [p=0.3] {c}A perda é meio vezes seis: três volts. [p=0.2] {d}Nos polos sobram doze menos três, [p=0.1] {e}nove volts."),
    dict(id="s09", block="interna", text="{a}E sem corrente nenhuma? [p=0.2] {b}Com i igual a zero, não há perda: u é igual a épsilon. [p=0.3] {c}A força eletromotriz é a tensão do gerador sem nada ligado."),
    # gráfico
    dict(id="s10", block="grafico", text="{a}Agora, o gráfico da tensão pela corrente. [p=0.2] {b}u igual a doze menos meio vezes i é uma função afim: [p=0.1] {c}uma reta que desce. [p=0.3] {d}Ela começa em doze volts, que é épsilon, [p=0.2] e {e}a cada ampère a mais, perde meio volt."),
    dict(id="s11", block="grafico", text="{a}A reta toca o eixo da corrente onde u vale zero. [p=0.2] {b}Doze dividido por meio, que é o mesmo que doze vezes dois: vinte e quatro ampères. [p=0.3] {c}É a corrente de curto-circuito, [p=0.1] {d}com os polos ligados por um fio sem resistência. [p=0.2] {e}Toda a tensão se perde dentro, e a bateria esquenta. [p=0.2] Os detalhes do curto ficam para outra aula."),
    # rendimento
    dict(id="s12", block="rendimento", text="{a}E o rendimento? [p=0.2] {b}A potência total é épsilon vezes i: [p=0.1] doze vezes seis, setenta e dois watts. [p=0.2] {c}A útil é u vezes i: [p=0.1] nove vezes seis, cinquenta e quatro watts. [p=0.3] {d}Os dezoito watts que faltam viram calor dentro da bateria: [p=0.1] erre pequeno vezes i ao quadrado, meio vezes trinta e seis."),
    dict(id="s13", block="rendimento", text="{a}Rendimento: cinquenta e quatro dividido por setenta e dois, [p=0.1] {b}setenta e cinco por cento."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar épsilon como a tensão nos polos. [p=0.3] Com seis ampères, {b}a pessoa calcula doze vezes seis, setenta e dois watts, como potência útil. [p=0.2] {c}Mas os polos têm só nove volts: [p=0.1] {d}a útil é cinquenta e quatro. [p=0.2] {e}Épsilon só aparece nos polos quando não há corrente."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, os atalhos. [p=0.2] {a}Rendimento é u dividido por épsilon, [p=0.1] {b}porque a corrente aparece em cima e embaixo, e corta. [p=0.3] {c}Nove dividido por doze: setenta e cinco por cento, [p=0.1] sem calcular nenhuma potência."),
    dict(id="s16", block="atalho", text="{a}No gráfico, épsilon é onde a reta corta o eixo da tensão, [p=0.2] {b}e erre pequeno é épsilon dividido pela corrente de curto. [p=0.3] {c}Doze dividido por vinte e quatro: meio ohm. [p=0.3] {d}Não compensa quando a questão pede as potências em watt: [p=0.1] aí, multiplique pela corrente."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] O gráfico de um gerador {a}começa em dez volts [p=0.1] e {b}toca o eixo da corrente em cinco ampères. [p=0.3] {c}Qual é a resistência interna, [p=0.1] e {d}qual é o rendimento quando ele fornece um ampère?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Épsilon é dez volts. [p=0.2] {b}A resistência interna é dez dividido por cinco: [p=0.1] {c}dois ohms. [p=0.3] {d}Com um ampère, a perda é dois vezes um, dois volts, [p=0.1] {e}e nos polos sobram oito volts."),
    dict(id="s20", block="resposta", text="{a}Rendimento: oito dividido por dez, [p=0.1] {b}oitenta por cento."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}u igual a épsilon menos erre pequeno vezes i; [p=0.2] {b}no gráfico, a reta começa em épsilon e termina na corrente de curto; [p=0.2] e {c}o rendimento é u dividido por épsilon."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai ligar o gerador a um resistor [p=0.1] e {a}achar a corrente com uma fração só, [p=0.2] {b}a lei de Pouillet. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
