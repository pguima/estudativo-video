# Estudativo · QUI-CAL-002 — Mol, massa molar e Avogadro (Química · Cálculos Químicos · Mol e massa molar).
# Habilidade: converter 36 g de água em 2 mol e em 1,2 × 10²⁴ moléculas, passando sempre pelo mol.
# Pré-requisitos: QUI-CAL-001, MAT-RAZ-006, MAT-POT-013. Próxima: QUI-CAL-003 (composição percentual e fórmula mínima).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: constante de Avogadro 6,022 × 10²³ (a prova usa 6 × 10²³) = 600 sextilhões; 36 g de água ≈ dois goles grandes.
# Contas: 36/18 = 2; 2 · 6 × 10²³ = 1,2 × 10²⁴; erro 36 · 6 × 10²³ = 2,16 × 10²⁵ = 18 vezes o certo; 132/44 = 3 → 1,8 × 10²⁴.

TITULO = "Mol, massa molar e Avogadro"

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
    dict(id="s01", block="gancho", text="{a}Uma dúzia de ovos são doze ovos. [p=0.3] {b}Um mol de água são seiscentos sextilhões de moléculas. [p=0.3] E {c}dois goles de água, trinta e seis gramas, [p=0.1] têm {d}o dobro disso. [p=0.3] Dá para contar essas moléculas {e}sem contar uma por uma."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber {b}o que é o mol, [p=0.2] {c}passar de gramas para mol e de mol para moléculas, [p=0.2] e ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}calcular a massa molecular, como os dezoito u da água; [p=0.2] {c}a regra de três; [p=0.2] e {d}multiplicar em notação científica. [p=0.3] Se faltar alguma, procure no canal."),
    # o mol
    dict(id="s04", block="mol", text="{a}Átomos e moléculas são pequenos demais para contar de um em um. [p=0.2] Por isso, a Química conta em pacotes, {b}como a feira conta ovos em dúzias. [p=0.3] {c}O pacote da Química se chama mol."),
    dict(id="s05", block="mol", text="{a}Um mol é seis vezes dez elevado a vinte e três unidades de qualquer coisa. [p=0.2] {b}Esse número tem nome: [p=0.1] constante de Avogadro, ou número de Avogadro. [p=0.3] {c}Um mol de moléculas de água são seis vezes dez elevado a vinte e três moléculas. [p=0.2] {d}O valor mais preciso é seis vírgula zero dois, [p=0.1] mas a prova costuma usar seis."),
    # massa molar
    dict(id="s06", block="massa", text="E quanto pesa um mol? [p=0.2] {a}Aí está o truque: [p=0.1] o número de Avogadro foi escolhido para que {b}um mol tenha, em gramas, o mesmo número da massa molecular. [p=0.3] {c}A molécula de água tem dezoito u. [p=0.2] {d}Um mol de água tem dezoito gramas."),
    dict(id="s07", block="massa", text="{a}Essa massa de um mol se chama massa molar, [p=0.2] e a unidade é {b}grama por mol. [p=0.3] {c}O gás carbônico, de quarenta e quatro u, tem massa molar de quarenta e quatro gramas por mol. [p=0.2] {d}A conta é a mesma da massa molecular: só troque u por grama por mol."),
    # a ponte do mol
    dict(id="s08", block="ponte", text="Pense no mol como {a}uma ponte. [p=0.2] {b}De um lado, a massa em gramas. [p=0.1] {c}Do outro, o número de moléculas. [p=0.2] {d}Para atravessar, você sempre passa pelo mol."),
    dict(id="s09", block="ponte", text="{a}Trinta e seis gramas de água. [p=0.2] Quantos mols? [p=0.2] {b}Cada mol tem dezoito gramas. [p=0.2] Pela regra de três: {c}dezoito gramas estão para um mol, [p=0.1] {d}assim como trinta e seis gramas estão para xis. [p=0.2] {e}Xis dá dois mols."),
    dict(id="s10", block="ponte", text="Falta o outro lado da ponte. [p=0.2] {a}Cada mol tem seis vezes dez elevado a vinte e três moléculas. [p=0.2] {b}Dois mols: dois vezes seis dá doze, vezes dez elevado a vinte e três. [p=0.3] {c}Em notação científica, um vírgula dois vezes dez elevado a vinte e quatro moléculas."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}pular o mol e multiplicar a massa direto pelo Avogadro. [p=0.3] {b}Trinta e seis vezes seis vezes dez elevado a vinte e três. [p=0.2] {c}Dá dois vírgula dezesseis vezes dez elevado a vinte e cinco: [p=0.1] dezoito vezes a resposta certa. [p=0.3] {d}O número de Avogadro conta moléculas em um mol, não em um grama. [p=0.2] {e}Primeiro, divida pela massa molar."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}pergunte quantas vezes a massa molar cabe na massa. [p=0.2] {b}Dezoito cabe duas vezes em trinta e seis: dois mols. [p=0.2] {c}Cada mol vale um Avogadro, então são dois Avogadros de moléculas."),
    dict(id="s13", block="atalho", text="{a}Funciona porque o mol é só um pacote, [p=0.1] e contar pacotes é dividir. [p=0.3] {b}Não compensa quando a massa molar não cabe um número inteiro de vezes, [p=0.1] como em cinquenta gramas de água. [p=0.2] {c}Aí, arme a divisão com vírgula."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um carro solta cento e trinta e dois gramas de gás carbônico, cê ó dois, [p=0.2] {b}de massa molar quarenta e quatro gramas por mol. [p=0.3] {c}Quantos mols são? [p=0.2] {d}E quantas moléculas?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Quantas vezes quarenta e quatro cabe em cento e trinta e dois? [p=0.2] {b}Três vezes: três mols. [p=0.3] {c}Três vezes seis dá dezoito, vezes dez elevado a vinte e três. [p=0.2] {d}Em notação científica, um vírgula oito vezes dez elevado a vinte e quatro moléculas."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}um mol são seis vezes dez elevado a vinte e três unidades; [p=0.2] {b}a massa de um mol é a massa molecular em gramas; [p=0.2] {c}e de massa para moléculas, sempre se passa pelo mol."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai usar a massa molar para descobrir {a}quanto de cada elemento há numa substância, em porcentagem, [p=0.2] e {b}a fórmula mais simples dela. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
