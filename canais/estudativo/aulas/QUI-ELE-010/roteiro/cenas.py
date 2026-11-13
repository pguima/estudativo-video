# Estudativo · QUI-ELE-010 — Leis de Faraday (Química · Eletroquímica e Radioatividade · Eletrólise).
# Habilidade: calcular que 10 A durante 1.930 s depositam 6,35 g de cobre, usando Q = i · t e 96.500 C por mol de elétrons.
# Pré-requisitos: QUI-ELE-009, QUI-CAL-002, MAT-RAZ-006, MAT-MED-006, FIS-ELE-008. Próxima: QUI-ELE-011 (emissões alfa, beta e gama).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Contas: Q = 10 × 1.930 = 19.300 C · 19.300 / 96.500 = 0,2 mol de e⁻ (19.300 × 5 = 96.500) · Cu²⁺ + 2 e⁻ → Cu: 0,1 mol Cu ·
# 0,1 × 63,5 = 6,35 g · regra de três: 2 × 96.500 = 193.000 C — 63,5 g; 19.300 C — x → x = 6,35 g.
# Erro (sem o 2): 0,2 mol Cu × 63,5 = 12,7 g. Constante: 6,02 × 10²³ × 1,602 × 10⁻¹⁹ C ≈ 96.485 C, arredondado para 96.500.
# Questão: Zn²⁺ + 2 e⁻ → Zn; 10 A × 965 s = 9.650 C = 1/10 de 96.500 = 0,1 mol e⁻ → 0,05 mol Zn × 65 = 3,25 g (erro sem o 2: 6,5 g).
# 1.930 s = 32 min 10 s. Massas molares de tabela: Cu 63,5 g/mol, Zn 65 g/mol (65,4 arredondado).

TITULO = "Leis de Faraday"

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
    dict(id="s01", block="gancho", text="{a}Uma peça fica numa solução de sulfato de cobre, ligada ao polo negativo, com uma corrente de dez ampères, [p=0.1] durante mil novecentos e trinta segundos. [p=0.3] {b}Sem pesar nada, dá para saber quanto cobre grudou nela: [p=0.2] {c}seis vírgula trinta e cinco gramas. [p=0.3] {d}Como?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a massa de metal que uma corrente deposita, [p=0.2] em quatro passos curtos. [p=0.2] E ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de três coisas. [p=0.2] {a}Corrente é carga dividida pelo tempo, em ampère. [p=0.2] {b}Um mol de cobre tem sessenta e três vírgula cinco gramas. [p=0.2] E {c}a regra de três. [p=0.2] Se faltar alguma, procure no canal."),
    # passo 1: carga
    dict(id="s04", block="carga", text="{a}Passo um: a carga que passou. [p=0.2] Se a corrente é carga dividida pelo tempo, [p=0.1] {b}a carga é corrente vezes tempo: [p=0.1] {c}quê igual a i vezes tê. [p=0.3] {d}Quê é a carga, em coulomb; [p=0.1] {e}i é a corrente, em ampère; [p=0.1] {f}tê é o tempo, em segundo."),
    dict(id="s05", block="carga", text="{a}Dez vezes mil novecentos e trinta {b}dá dezenove mil e trezentos coulombs."),
    # passo 2: faraday
    dict(id="s06", block="faraday", text="{a}Passo dois: quantos mols de elétrons são esses. [p=0.2] {b}Um mol de elétrons é um número gigante deles: seis seguido de vinte e três zeros. [p=0.2] {c}Multiplique pela carga de cada um, [p=0.1] {d}e dá cerca de noventa e seis mil e quinhentos coulombs. [p=0.3] {e}Esse número é a constante de Faraday."),
    dict(id="s07", block="faraday", text="{a}Dezenove mil e trezentos dividido por noventa e seis mil e quinhentos. [p=0.2] {b}Repare: dezenove mil e trezentos vezes cinco dá noventa e seis mil e quinhentos. [p=0.3] {c}Então passou um quinto de mol, [p=0.1] {d}zero vírgula dois mol de elétrons."),
    # passo 3: semirreação
    dict(id="s08", block="semi", text="{a}Passo três: a semirreação do cátodo. [p=0.2] {b}O íon cobre dois mais recebe dois elétrons e vira cobre metálico. [p=0.3] {c}Cada íon cobre precisa de dois elétrons para virar metal. [p=0.2] {d}Então dois mols de elétrons fazem um mol de cobre. [p=0.3] {e}Zero vírgula dois mol de elétrons fazem {f}zero vírgula um mol de cobre."),
    # passo 4: massa
    dict(id="s09", block="massa", text="{a}Passo quatro: a massa. [p=0.2] {b}Um mol de cobre tem sessenta e três vírgula cinco gramas. [p=0.2] {c}Zero vírgula um mol {d}dá seis vírgula trinta e cinco gramas. [p=0.3] {e}O número do começo."),
    dict(id="s10", block="massa", text="{a}Dá para fazer tudo numa regra de três. [p=0.2] {b}Dois mols de elétrons, que são cento e noventa e três mil coulombs, depositam sessenta e três vírgula cinco gramas. [p=0.2] {c}Dezenove mil e trezentos coulombs dão xis. [p=0.3] {d}Xis dá seis vírgula trinta e cinco gramas."),
    dict(id="s11", block="massa", text="{a}Essa é a ideia de Faraday: [p=0.1] {b}a massa depositada é proporcional à carga que passou. [p=0.3] {c}Dobre a corrente, ou dobre o tempo, [p=0.1] {d}e o cobre dobra."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer a carga do íon. [p=0.3] A pessoa acha zero vírgula dois mol de elétrons [p=0.1] {b}e diz zero vírgula dois mol de cobre. [p=0.2] {c}Dá doze vírgula sete gramas, o dobro."),
    dict(id="s13", block="erro", text="{a}Cobre dois mais pede dois elétrons por átomo. [p=0.2] {b}Divida os mols de elétrons pela carga do íon: [p=0.1] {c}dois para o cobre, um para a prata, três para o alumínio, na eletrólise ígnea."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a carga da questão quase sempre é uma fração redonda de noventa e seis mil e quinhentos. [p=0.3] {b}Nove mil seiscentos e cinquenta é um décimo. [p=0.2] {c}Dezenove mil e trezentos, um quinto. [p=0.2] {d}Quarenta e oito mil duzentos e cinquenta, a metade. [p=0.3] {e}Achou a fração, achou os mols de elétrons."),
    dict(id="s15", block="atalho", text="Funciona porque {a}quem faz a prova escolhe o tempo para a conta fechar. [p=0.3] {b}Atenção: se o tempo vier em minutos, [p=0.1] {c}passe para segundos primeiro, vezes sessenta, e só depois procure a fração. [p=0.3] E não compensa quando a carga não é uma fração redonda: aí, divida."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Para cobrir um parafuso de zinco, passa uma corrente de dez ampères, [p=0.1] durante novecentos e sessenta e cinco segundos, [p=0.1] {b}numa solução de zinco dois mais. [p=0.3] {c}Um mol de zinco tem sessenta e cinco gramas. [p=0.2] {d}Quantos gramas de zinco se depositam?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Carga: dez vezes novecentos e sessenta e cinco dá nove mil seiscentos e cinquenta coulombs. [p=0.3] {b}Isso é um décimo de noventa e seis mil e quinhentos: [p=0.1] {c}zero vírgula um mol de elétrons."),
    dict(id="s19", block="resposta", text="{a}O zinco dois mais pede dois elétrons: [p=0.1] {b}zero vírgula um dividido por dois dá zero vírgula zero cinco mol de zinco. [p=0.3] {c}Vezes sessenta e cinco, {d}dá três vírgula vinte e cinco gramas. [p=0.3] {e}Quem esquece a carga do íon acha seis vírgula cinco, o dobro."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}carga é corrente vezes tempo; [p=0.1] {b}noventa e seis mil e quinhentos coulombs são um mol de elétrons; [p=0.1] {c}e a carga do íon diz quantos elétrons cada átomo pede."),
    dict(id="s21", block="fim", text="Na próxima aula, você sai dos elétrons {a}e entra no núcleo do átomo: [p=0.2] {b}as emissões alfa, beta e gama da radioatividade. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
