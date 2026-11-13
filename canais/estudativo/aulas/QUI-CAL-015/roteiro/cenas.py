# Estudativo · QUI-CAL-015 — Praticando: estudo dos gases (Química · Cálculos Químicos · Estudo dos gases). PRÁTICA.
# Habilidade: aplicar as equações dos gases a balões, pneus e cilindros, em questões de prova.
# Pré-requisitos: QUI-CAL-010 a QUI-CAL-014 e QUI-CAL-016. Próxima: nenhuma (fim da trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; CNTP lido "cê ene tê pê". Cinco questões inéditas.
# Q1 isocórica: 3 · 330/300 = 3,3 atm (pressão absoluta do ar no pneu; não é a "calibragem", que é manométrica).
# Q2 geral: 10 · (1/0,25) · (210/300) = 10 · 4 · 0,7 = 28 L (−63 °C = 210 K).
# Q3 Clapeyron: 150 · 8,2 = 1.230; 1.230/24,6 = 50 mol; 50 · 32 = 1.600 g = 1,6 kg (cilindro hospitalar real: 150 a 200 bar).
# Q4 CNTP: 88/44 = 2 mol → 44,8 L. Q5: 1 de 5 mols → 1/5 · 5 = 1 atm; He (4) contra O₂ (32): √8 ≈ 2,8.

TITULO = "Praticando: estudo dos gases"

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
    dict(id="s01", block="gancho", text="{a}Pneu que esquenta na estrada, balão que sobe, cilindro de hospital. [p=0.3] {b}A prova adora gás no dia a dia. [p=0.2] {c}Hoje são cinco questões, [p=0.1] {d}com todas as ferramentas do módulo."),
    # lembrete
    dict(id="s02", block="lembrete", text="{a}As ferramentas. [p=0.1] {b}Temperatura, sempre em kelvin. [p=0.2] {c}Antes e depois, com o gás preso: a equação geral. [p=0.2] {d}Mols ou massa: pê vê igual a ene erre tê. [p=0.2] {e}Nas cê ene tê pê: vinte e dois vírgula quatro litros por mol. [p=0.2] {f}Na mistura: fração em mols vezes a pressão total. [p=0.2] {g}Na difusão: o gás mais leve ganha. [p=0.3] Pause e tente antes de cada resposta."),
    # questão 1
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] {b}O ar dentro de um pneu está a três atmosferas e vinte e sete graus Celsius. [p=0.2] {c}Depois de uma viagem, chega a cinquenta e sete graus. [p=0.2] {d}O volume do pneu quase não muda. [p=0.3] {e}Qual é a nova pressão?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="q1r", text="{a}Volume parado: isocórica, [p=0.1] {b}e pressão dividida por temperatura não muda. [p=0.3] {c}Em kelvin, de trezentos para trezentos e trinta: [p=0.1] {d}a temperatura subiu um décimo. [p=0.2] {e}A pressão sobe um décimo também: [p=0.1] {f}três vezes um vírgula um dá três vírgula três atmosferas."),
    # questão 2
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] {b}Um balão meteorológico sai do chão com dez litros de gás, [p=0.1] {c}a uma atmosfera e vinte e sete graus. [p=0.3] {d}Lá no alto, a pressão é de um quarto de atmosfera, [p=0.1] {e}e a temperatura, sessenta e três graus negativos. [p=0.3] {f}Qual é o volume do balão lá em cima?"),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="q2r", text="{a}Pelos fatores. [p=0.2] {b}A pressão caiu para um quarto: [p=0.1] o volume fica quatro vezes maior. [p=0.3] {c}Em kelvin, a temperatura vai de trezentos para duzentos e dez: [p=0.1] {d}duzentos e dez dividido por trezentos dá zero vírgula sete. [p=0.3] {e}Dez vezes quatro vezes zero vírgula sete dá vinte e oito litros."),
    # questão 3
    dict(id="s09", block="q3", text="{a}Questão três. [p=0.2] {b}Um cilindro de oxigênio de hospital tem oito vírgula dois litros, [p=0.1] {c}com o gás a cento e cinquenta atmosferas e vinte e sete graus. [p=0.3] {d}Use erre igual a zero vírgula zero oito dois. [p=0.2] {e}Quantos quilos de oxigênio ele guarda?"),
    dict(id="s10", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="q3r", text="{a}A trezentos kelvin, erre vezes tê dá vinte e quatro vírgula seis. [p=0.3] {b}Pê vezes vê: cento e cinquenta vezes oito vírgula dois dá mil duzentos e trinta. [p=0.2] {c}Mil duzentos e trinta dividido por vinte e quatro vírgula seis dá cinquenta mols. [p=0.3] {d}Cinquenta vezes trinta e dois dá mil e seiscentos gramas: [p=0.1] {e}um quilo e seiscentos gramas de oxigênio."),
    # questão 4
    dict(id="s12", block="q4", text="{a}Questão quatro. [p=0.2] {b}Um extintor libera oitenta e oito gramas de gás carbônico, [p=0.1] de massa molar quarenta e quatro. [p=0.2] {c}Que volume esse gás ocupa nas cê ene tê pê?"),
    dict(id="s13", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="q4r", text="{a}Oitenta e oito dividido por quarenta e quatro dá dois mols. [p=0.2] {b}Dois vezes vinte e dois vírgula quatro [p=0.1] {c}dá quarenta e quatro vírgula oito litros."),
    # questão 5
    dict(id="s15", block="q5", text="{a}Questão cinco. [p=0.2] {b}Uma mistura de mergulho tem um mol de oxigênio para cada quatro mols de hélio, [p=0.1] {c}a cinco atmosferas. [p=0.3] {d}Qual é a pressão parcial do oxigênio? [p=0.2] {e}E, se houver um vazamento, qual gás escapa mais rápido?"),
    dict(id="s16", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="q5r", text="{a}O oxigênio tem um de cinco mols: [p=0.1] {b}um quinto de cinco dá uma atmosfera. [p=0.3] {c}No vazamento, ganha o mais leve: [p=0.1] {d}o hélio, de massa molar quatro, contra trinta e dois do oxigênio. [p=0.2] {e}Trinta e dois dividido por quatro dá oito. [p=0.2] A raiz de oito fica entre dois e três, perto de dois vírgula oito: [p=0.1] quase três vezes mais rápido."),
    # fechamento
    dict(id="s18", block="fim", text="{a}Cinco problemas, uma lista de conferência: [p=0.2] {b}kelvin, [p=0.1] {c}as unidades do erre, [p=0.1] {d}e o que fica parado. [p=0.3] {e}Com isso, você fecha o estudo dos gases e a trilha de mol, estequiometria e gases."),
    dict(id="s19", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
