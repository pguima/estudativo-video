# Estudativo · FIS-ELE-023 — Praticando: potência, geradores e receptores (Física · Eletricidade · Geradores e receptores · prática).
# Habilidade: resolver questões de conta de luz, chuveiro, baterias e motores.
# Pré-requisitos: FIS-ELE-017, 018, 019, 020, 021, 022. Próxima: FIS-ELE-024.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: seis questões inéditas, criadas para esta aula.
# Preço do kWh (R$ 0,80) é de exemplo, perto do valor de 2026 com impostos; a questão não depende dele ser exato.
# Contas: Q1 4.400 W = 4,4 kW; 0,5·30 = 15 h; 4,4·15 = 66 kWh; 66·0,80 = R$ 52,80.
#   Q3 lâmpadas 220 V: R50 = 968 Ω = 2·R100 (484 Ω); paralelo 100 contra 50 W; série P ∝ R: a de 50 W, o dobro.
#   Q2 220² = 48.400; 48.400/4.840 = 10 Ω; 48.400/2.420 = 20 Ω.  Q4 20/(18 + 2) = 1 A; 20 − 2·1 = 18 V; 18/20 = 90 %.
#   Q5 (12 − 6)/(1 + 2) = 2 A; 6 + 2·2 = 10 V = 12 − 1·2; 6/10 = 60 %.  Q6 R = 4 Ω; 400/16 = 25 W; 20/8 = 2,5 A; 4·2,5² = 25.

TITULO = "Praticando: potência, geradores e receptores"

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
    dict(id="s01", block="gancho", text="{a}Conta de luz, chuveiro, bateria e motor: [p=0.2] {b}na prova, eles aparecem misturados. [p=0.3] {c}Até o fim desta aula, você vai resolver seis questões [p=0.1] e {d}saber qual fórmula chamar em cada uma."),
    # método
    dict(id="s02", block="metodo", text="Antes, o método: [p=0.2] {a}pergunte o que cada peça faz com a energia. [p=0.3] {b}Resistor só esquenta: [p=0.1] escolha a fórmula da potência pelo que não muda. [p=0.2] {c}Gerador perde dentro: [p=0.1] u igual a épsilon menos erre pequeno vezes i. [p=0.2] {d}Receptor precisa de mais: [p=0.1] u igual a épsilon linha mais erre linha vezes i. [p=0.2] {e}E a energia da conta é potência vezes tempo, em quilowatt-hora."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] {a}Um chuveiro de quatro mil e quatrocentos watts fica ligado meia hora por dia, [p=0.1] {b}durante trinta dias. [p=0.2] {c}O quilowatt-hora custa oitenta centavos. [p=0.3] {d}Quanto o chuveiro custa no mês? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s04", block="q1", text="{a}Divida por mil: quatro vírgula quatro quilowatts. [p=0.2] {b}Tempo no mês: meia hora vezes trinta, quinze horas. [p=0.3] {c}Energia: quatro vírgula quatro vezes quinze, [p=0.1] sessenta e seis quilowatts-hora. [p=0.3] {d}Sessenta e seis vezes oitenta centavos: [p=0.1] {e}cinquenta e dois reais e oitenta centavos."),
    # questão 2
    dict(id="s05", block="q2", text="Questão dois. [p=0.2] {a}Um chuveiro de duzentos e vinte volts tem duas posições: [p=0.1] {b}quatro mil oitocentos e quarenta watts [p=0.1] e {c}dois mil quatrocentos e vinte watts. [p=0.3] {d}Qual é a resistência na posição inverno? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q2", text="{a}Inverno é a posição de maior potência: quatro mil oitocentos e quarenta. [p=0.2] {b}A tensão é fixa: [p=0.1] isole o erre em pê igual a u ao quadrado dividido por erre. [p=0.2] {c}Erre é quarenta e oito mil e quatrocentos dividido por quatro mil oitocentos e quarenta: [p=0.1] {d}dez ohms. [p=0.3] {e}No verão, metade da potência, o dobro da resistência: vinte ohms."),
    # questão 3
    dict(id="s07", block="q3", text="Questão três. [p=0.2] Duas lâmpadas de duzentos e vinte volts: [p=0.1] {a}uma de cem watts [p=0.1] e {b}outra de cinquenta. [p=0.3] {c}Qual brilha mais em série, [p=0.1] {d}qual brilha mais em paralelo, [p=0.1] e quantas vezes mais? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q3", text="{a}Em paralelo, cada uma recebe os duzentos e vinte volts da etiqueta: [p=0.1] {b}a de cem brilha mais, o dobro. [p=0.3] {c}Em série, a corrente é a mesma, e ganha a de maior resistência: [p=0.1] {d}a de cinquenta watts brilha mais, [p=0.1] {e}também o dobro, porque cem dividido por cinquenta é dois."),
    # questão 4
    dict(id="s09", block="q4", text="Questão quatro. [p=0.2] {a}Uma bateria de vinte volts, com dois ohms de resistência interna, [p=0.1] {b}alimenta um resistor de dezoito ohms. [p=0.3] {c}Qual é a tensão nos polos, [p=0.1] e {d}qual é o rendimento da bateria? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s10", block="q4", text="{a}Pouillet: vinte dividido por dezoito mais dois, [p=0.1] {b}um ampère. [p=0.2] {c}Nos polos: vinte menos dois vezes um, [p=0.1] {d}dezoito volts. [p=0.3] {e}Rendimento: dezoito dividido por vinte, [p=0.1] noventa por cento."),
    # questão 5
    dict(id="s11", block="q5", text="Questão cinco. [p=0.2] {a}Uma bateria de doze volts, com um ohm interno, [p=0.1] {b}liga um motor de seis volts de força contraeletromotriz e dois ohms internos. [p=0.3] {c}Qual é a corrente, [p=0.1] e {d}qual é o rendimento do motor? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s12", block="q5", text="{a}A força contraeletromotriz subtrai: [p=0.1] {b}doze menos seis, seis, dividido por um mais dois, três: [p=0.1] {c}dois ampères. [p=0.3] {d}O motor recebe seis mais dois vezes dois, [p=0.1] dez volts. [p=0.2] {e}Rendimento do motor: seis dividido por dez, [p=0.1] {f}sessenta por cento."),
    # questão 6
    dict(id="s13", block="q6", text="Questão seis. [p=0.2] {a}Um gerador de vinte volts tem quatro ohms de resistência interna. [p=0.3] {b}Que resistor de fora recebe a maior potência, [p=0.1] e {c}de quantos watts? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s14", block="q6", text="{a}Potência máxima: a resistência de fora igual à de dentro, [p=0.1] {b}quatro ohms. [p=0.3] {c}Vinte ao quadrado, quatrocentos, [p=0.1] dividido por quatro vezes quatro, dezesseis: [p=0.1] {d}vinte e cinco watts. [p=0.3] {e}Confira: a corrente é vinte dividido por oito, dois vírgula cinco ampères, [p=0.1] e quatro vezes dois vírgula cinco ao quadrado dá vinte e cinco."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}pergunte o que cada peça faz com a energia, [p=0.2] e {b}a fórmula aparece. [p=0.3] Na próxima aula, {c}as leis de Kirchhoff: [p=0.1] {d}a lei dos nós e a das malhas, com a regra de sinais. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
