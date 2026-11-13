# Estudativo · QUI-SOL-007 — Praticando: concentração e diluição (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: ler rótulos, laudos de água e curvas e fazer contas de concentração, diluição e titulação.
# Pré-requisitos: QUI-SOL-001 a QUI-SOL-006. Próxima: QUI-SOL-008 (pressão de vapor e ponto de ebulição).
# Aula de prática: cinco questões inéditas (a dois tem duas partes), criadas para esta aula, cada uma com pausa e resolução.
# Contas: Q1 KNO₃ a 60 °C = 110 g/100 g; 50 g de água → 55 g; 60 − 55 = 5 g no fundo (saturada com corpo de fundo).
# Q2 vinagre 4% → 40 g/L; 750 mL = 0,75 L; 40 × 0,75 = 30 g; laudo 0,015 g = 15 mg; 15 ÷ 5 = 3 mg/L = 3 ppm.
# Q3 NaOH 40 g/mol: 4 g = 0,1 mol; 250 mL = 0,25 L; 0,1 ÷ 0,25 = 0,4 mol/L; até 1 L = 4 vezes → 0,1 mol/L.
# Q4 mistura: 200 mL × 0,5 = 0,1 mol; 300 mL × 0,1 = 0,03 mol; 0,13 mol ÷ 0,5 L = 0,26 mol/L (média simples daria 0,3).
# Q5 H₂SO₄ + 2 NaOH: 2 × Ma × 10 = 1 × 0,2 × 15 = 3 → 20 × Ma = 3 → Ma = 0,15 mol/L; sem o 2: 0,3 (erro).

TITULO = "Praticando: concentração e diluição"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões, cinco situações de prova: [p=0.2] {b}uma curva, um rótulo com um laudo de água, [p=0.1] {c}uma diluição, uma mistura e uma titulação. [p=0.3] {d}Pause em cada uma, tente, e confira comigo."),
    # lembrete
    dict(id="s02", block="lembrete", text="Sua caixa de ferramentas. [p=0.2] {a}Gramas por litro: massa do soluto dividida pelo volume em litros. [p=0.3] {b}Porcentagem do rótulo vezes dez dá gramas por litro. [p=0.2] {c}Na água, pê pê eme é miligrama por litro. [p=0.3] {d}Mol por litro: gramas por litro divididos pela massa molar."),
    dict(id="s03", block="lembrete", text="{a}Na diluição, cê um vê um igual a cê dois vê dois. [p=0.2] {b}Na mistura, some os mols. [p=0.3] {c}E na titulação, conte quantos hidrogênios o ácido solta e quantas hidroxilas a base solta."),
    # questão 1: curva
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Pela curva, a sessenta graus, cem gramas de água dissolvem até cento e dez gramas de nitrato de potássio. [p=0.3] {b}Você põe sessenta gramas desse sal em cinquenta gramas de água, a sessenta graus. [p=0.3] {c}A solução é saturada? [p=0.1] {d}Sobra sal no fundo? Quanto?"),
    dict(id="s05", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s06", block="r1", text="{a}A água é a metade de cem gramas, [p=0.1] então dissolve a metade do sal: [p=0.1] {b}cento e dez dividido por dois dá cinquenta e cinco gramas. [p=0.3] {c}Sessenta passa de cinquenta e cinco: [p=0.1] {d}é saturada com corpo de fundo, [p=0.1] {e}e sessenta menos cinquenta e cinco dá cinco gramas no fundo."),
    dict(id="s07", block="r1", text="{a}Quem comparou sessenta com cento e dez [p=0.1] {b}disse insaturada. [p=0.2] Esqueceu que a curva vale para cem gramas de água."),
    # questão 2: rótulo e laudo
    dict(id="s08", block="q2", text="Questão dois, em duas partes. [p=0.2] {a}O rótulo de um vinagre diz: [p=0.1] {b}acidez de quatro por cento, em massa por volume. [p=0.2] {c}Quantos gramas de ácido há na garrafa de setecentos e cinquenta mililitros? [p=0.3] {d}Depois, um laudo de água de rio: [p=0.1] {e}em cinco litros, zero vírgula zero quinze grama de chumbo. [p=0.2] {f}Quantos pê pê eme são?"),
    dict(id="s09", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="r2", text="{a}Pelo atalho, quatro por cento vezes dez dá quarenta gramas por litro. [p=0.3] {b}Setecentos e cinquenta mililitros são zero vírgula setenta e cinco litro. [p=0.2] {c}Quarenta vezes zero vírgula setenta e cinco dá trinta gramas de ácido."),
    dict(id="s11", block="r2", text="{a}No laudo, pê pê eme pede miligramas. [p=0.2] {b}Um grama tem mil miligramas: zero vírgula zero quinze grama são quinze miligramas. [p=0.3] {c}Quinze dividido por cinco litros dá três miligramas por litro. [p=0.2] {d}Na água, três pê pê eme."),
    # questão 3: mol/L e diluição
    dict(id="s12", block="q3", text="Questão três. [p=0.2] {a}Você dissolve quatro gramas de soda cáustica, o hidróxido de sódio, até formar duzentos e cinquenta mililitros de solução. [p=0.3] {b}A massa molar é quarenta gramas por mol. [p=0.2] {c}Qual é a concentração em mol por litro? [p=0.3] {d}Depois, essa solução é diluída até um litro. [p=0.1] {e}Qual é a nova concentração?"),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="r3", text="{a}Quatro dividido por quarenta dá zero vírgula um mol. [p=0.3] {b}Duzentos e cinquenta mililitros são zero vírgula vinte e cinco litro. [p=0.2] {c}Zero vírgula um dividido por zero vírgula vinte e cinco dá zero vírgula quatro mol por litro."),
    dict(id="s15", block="r3", text="{a}Na diluição, de duzentos e cinquenta mililitros para um litro, o volume cresceu quatro vezes. [p=0.3] {b}Zero vírgula quatro dividido por quatro dá zero vírgula um mol por litro."),
    # questão 4: mistura
    dict(id="s16", block="q4", text="Questão quatro. [p=0.2] {a}Você junta duzentos mililitros de soda cáustica com zero vírgula cinco mol por litro [p=0.2] {b}a trezentos mililitros de soda cáustica com zero vírgula um mol por litro. [p=0.3] {c}Qual é a concentração final?"),
    dict(id="s17", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="r4", text="Some os mols. [p=0.2] {a}Zero vírgula cinco vezes zero vírgula dois litro dá zero vírgula um mol. [p=0.3] {b}Zero vírgula um vezes zero vírgula três litro dá zero vírgula zero três mol. [p=0.3] {c}Juntos, zero vírgula treze mol, em meio litro. [p=0.2] {d}Zero vírgula treze dividido por zero vírgula cinco dá zero vírgula vinte e seis mol por litro."),
    dict(id="s19", block="r4", text="{a}Quem fez a média das concentrações chegou a zero vírgula três. [p=0.3] {b}Mas há mais volume da solução fraca, [p=0.1] {c}então o resultado fica mais perto dela."),
    # questão 5: titulação
    dict(id="s20", block="q5", text="Questão cinco. [p=0.2] {a}Dez mililitros de ácido sulfúrico, com fenolftaleína, [p=0.1] {b}gastaram quinze mililitros de soda cáustica com zero vírgula dois mol por litro [p=0.1] {c}até ficar rosa. [p=0.3] {d}Qual é a concentração do ácido?"),
    dict(id="s21", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="r5", text="{a}O ácido sulfúrico solta dois hidrogênios; [p=0.1] a soda tem uma hidroxila. [p=0.3] {b}Então, dois vezes a concentração do ácido vezes dez [p=0.1] {c}é igual a zero vírgula dois vezes quinze, que dá três. [p=0.2] Pode deixar os volumes em mililitros, porque estão dos dois lados. [p=0.3] {d}Vinte vezes a concentração é igual a três: [p=0.1] {e}a concentração dá zero vírgula quinze mol por litro."),
    dict(id="s23", block="r5", text="{a}Sem o dois do ácido, [p=0.1] {b}sairia zero vírgula três, o dobro do certo."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo o módulo: [p=0.1] {a}passe o volume para litros, [p=0.1] {b}leve a curva para a água da questão, [p=0.1] {c}some mols, não concentrações, [p=0.1] e {d}conte os hidrogênios do ácido."),
    dict(id="s25", block="fim", text="Na próxima aula, começa um assunto novo: [p=0.2] {a}por que a água ferve abaixo de cem graus na montanha [p=0.1] e {b}acima disso na panela de pressão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
