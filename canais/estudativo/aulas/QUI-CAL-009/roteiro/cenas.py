# Estudativo · QUI-CAL-009 — Praticando: mol e estequiometria (Química · Cálculos Químicos · Estequiometria). PRÁTICA.
# Habilidade: resolver problemas de fábrica e de meio ambiente com mol, pureza, rendimento e reagente limitante.
# Pré-requisitos: QUI-CAL-001 a QUI-CAL-008. Próxima: QUI-CAL-010 (pressão, volume e temperatura: a escala Kelvin).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Quatro questões inéditas, criadas para esta aula.
# Q1: 880/44 = 20 mol; 20 · 6 × 10²³ = 1,2 × 10²⁵. Q2: Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂ (balanceada); 160 g → 112 g;
# 0,8 · 1.000 = 800 kg = 5 · 160 → 5 · 112 = 560 kg. Q3: N₂ + 3 H₂ → 2 NH₃; 56 kg → 68 kg; 25% = 1/4 → 17 kg (rendimento
# de uma passagem pelo reator, na faixa real de 15 a 25%). Q4: CaO + SO₂ → CaSO₃ (56 : 64); 112/56 = 2; 160/64 = 2,5 → CaO
# limita; 2 · 64 = 128 kg retidos; 160 − 128 = 32 kg escapam.

TITULO = "Praticando: mol e estequiometria"

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
    dict(id="s01", block="gancho", text="{a}Escapamento de carro, siderúrgica, fábrica de adubo, chaminé. [p=0.3] {b}Na prova, a estequiometria quase sempre vem vestida de problema real. [p=0.2] {c}Hoje são quatro questões, [p=0.1] {d}com mol, pureza, rendimento e reagente limitante."),
    # lembrete
    dict(id="s02", block="lembrete", text="{a}As ferramentas: [p=0.1] {b}massa dividida pela massa molar dá mol; [p=0.2] {c}massas embaixo da equação e regra de três; [p=0.2] {d}pureza e rendimento multiplicam; [p=0.2] {e}e o limitante é o menor resultado da divisão pela massa da equação. [p=0.3] Em cada questão, pause e tente antes da resposta."),
    # questão 1
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] {b}Um carro solta oitocentos e oitenta gramas de gás carbônico num trajeto. [p=0.2] {c}A massa molar do cê ó dois é quarenta e quatro gramas por mol. [p=0.3] {d}Quantos mols e quantas moléculas são?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="q1r", text="{a}Oitocentos e oitenta dividido por quarenta e quatro dá vinte mols. [p=0.3] {b}Cada mol tem seis vezes dez elevado a vinte e três moléculas. [p=0.2] Vinte vezes seis dá cento e vinte, vezes dez elevado a vinte e três. [p=0.2] {c}Em notação científica, dá um vírgula dois vezes dez elevado a vinte e cinco moléculas."),
    # questão 2
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] {b}Na siderúrgica, o ferro sai do minério, a rocha que traz a hematita, efe é dois ó três. [p=0.2] {c}A reação: efe é dois ó três mais três cê ó forma dois efe é mais três cê ó dois. [p=0.3] {d}Cento e sessenta gramas de hematita dão cento e doze gramas de ferro. [p=0.3] {e}Quanto ferro sai de mil quilos de minério com oitenta por cento de hematita?"),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="q2r", text="{a}A parte pura: [p=0.1] zero vírgula oito vezes mil dá oitocentos quilos de hematita. [p=0.3] {b}Cento e sessenta dão cento e doze, [p=0.1] {c}e a proporção vale em gramas ou em quilos. [p=0.2] {d}Oitocentos é cinco vezes cento e sessenta: [p=0.1] {e}cinco vezes cento e doze dá quinhentos e sessenta quilos de ferro."),
    # questão 3
    dict(id="s09", block="q3", text="{a}Questão três. [p=0.2] {b}Na fábrica de adubo, a amônia sai de ene dois mais três agá dois, formando dois ene agá três. [p=0.3] {c}Vinte e oito gramas de ene dois dão trinta e quatro de amônia. [p=0.2] {d}Numa passagem pelo reator, o rendimento é de vinte e cinco por cento. [p=0.3] {e}Quanta amônia sai de cinquenta e seis quilos de ene dois?"),
    dict(id="s10", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="q3r", text="{a}O máximo: cinquenta e seis é o dobro de vinte e oito, [p=0.1] {b}então sai o dobro de trinta e quatro, sessenta e oito quilos. [p=0.3] {c}Vinte e cinco por cento é um quarto: [p=0.1] {d}sessenta e oito dividido por quatro dá dezessete quilos de amônia."),
    # questão 4
    dict(id="s12", block="q4", text="{a}Questão quatro. [p=0.2] {b}Para segurar o esse ó dois, um gás que causa chuva ácida, [p=0.1] {c}a fumaça da chaminé passa por cal: [p=0.1] cê á ó mais esse ó dois forma cê á esse ó três. [p=0.3] {d}Cinquenta e seis gramas de cal seguram sessenta e quatro de esse ó dois. [p=0.3] {e}Num dia, entram cento e doze quilos de cal e cento e sessenta quilos de esse ó dois. [p=0.2] {f}Quanto esse ó dois escapa?"),
    dict(id="s13", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="q4r", text="{a}Divida cada massa pela da equação. [p=0.2] {b}Cal: cento e doze dividido por cinquenta e seis dá dois. [p=0.2] {c}Esse ó dois: cento e sessenta dividido por sessenta e quatro dá dois e meio. [p=0.3] {d}A cal é o limitante. [p=0.2] {e}Duas receitas seguram duas vezes sessenta e quatro, que dá cento e vinte e oito quilos. [p=0.3] {f}Cento e sessenta menos cento e vinte e oito dá trinta e dois quilos, que escapam."),
    # fechamento
    dict(id="s15", block="fim", text="{a}Quatro problemas, um caminho só: [p=0.2] {b}fique com a parte que reage, [p=0.1] {c}use as massas da equação [p=0.1] {d}e corrija pelo rendimento no fim."),
    dict(id="s16", block="fim", text="Na próxima aula, começa o estudo dos gases: [p=0.2] {a}o que são a pressão e o volume de um gás [p=0.1] e {b}por que a temperatura dele se mede em kelvin. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
