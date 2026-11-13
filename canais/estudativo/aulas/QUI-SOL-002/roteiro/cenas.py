# Estudativo · QUI-SOL-002 — Solubilidade e curvas de solubilidade (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: ler uma curva de solubilidade, dizer se a solução está saturada, calcular quanto sal fica no fundo e explicar
# por que o refrigerante perde gás ao esquentar.
# Pré-requisitos: QUI-SOL-001, MAT-EST-003, MAT-RAZ-006. Próxima: QUI-SOL-003 (concentração em g/L, porcentagem e ppm).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Dados (g por 100 g de água): NaCl 35,7 a 0 °C, 36,0 a 20 °C, 39,2 a 100 °C (arredondado: 36 g a 20 °C).
# KNO₃ (nitrato de potássio): 13 a 0 °C, 21 a 10, 32 a 20, 46 a 30, 64 a 40, 85 a 50, 110 a 60, 138 a 70, 169 a 80 °C
# (tabelas usuais, arredondadas). CO₂ na água: 3,4 g/L a 0 °C e 1,7 g/L a 20 °C ("quase o dobro" na água gelada).
# Contas: 50 − 36 = 14; 80 − 64 = 16; 50 g de água a 40 °C dissolvem 32 g (64 ÷ 2), 40 − 32 = 8; questão: 100 < 110, 100 − 64 = 36.

TITULO = "Solubilidade e curvas de solubilidade"

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
    dict(id="s01", block="gancho", text="{a}Ponha cinquenta gramas de sal de cozinha em cem gramas de água, [p=0.2] a vinte graus, e mexa. [p=0.3] {b}Mexa um minuto, mexa uma hora: [p=0.2] {c}catorze gramas continuam no fundo. [p=0.3] {d}A água tem um limite."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}ler esse limite num gráfico, [p=0.2] {c}calcular quanto sal sobra no fundo [p=0.2] e {d}entender por que o refrigerante quente perde o gás."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}o soluto é o que se dissolve, [p=0.1] e {b}o solvente, quase sempre a água, é o que dissolve. [p=0.3] Você também vai {c}ler um gráfico de linha [p=0.2] e usar {d}a regra de três: se dobra um, dobra o outro."),
    # solubilidade
    dict(id="s04", block="limite", text="{a}A quantidade máxima de soluto que se dissolve numa quantidade de água, numa certa temperatura, [p=0.2] se chama {b}coeficiente de solubilidade. [p=0.3] A medida mais usada é {c}em gramas para cada cem gramas de água."),
    dict(id="s05", block="limite", text="{a}Para o sal de cozinha, a vinte graus, o limite é de trinta e seis gramas. [p=0.3] Por isso, dos cinquenta do começo, [p=0.1] {b}trinta e seis se dissolvem, [p=0.2] e {c}cinquenta menos trinta e seis dá catorze, que ficam no fundo."),
    dict(id="s06", block="limite", text="Cada situação tem um nome. [p=0.2] {a}Abaixo do limite, a solução é insaturada: ainda dissolve mais. [p=0.3] {b}No limite, é saturada. [p=0.3] {c}Passou do limite, o que sobra fica no fundo: [p=0.1] é saturada com {d}corpo de fundo, o nome do sólido que ficou embaixo."),
    dict(id="s07", block="limite", text="{a}E existe um caso raro, a supersaturada: [p=0.2] o líquido segura mais do que o limite, sem nada no fundo. [p=0.3] {b}É instável: um grão de sal ou uma batida no copo, e o excesso cai de uma vez."),
    # curva
    dict(id="s08", block="curva", text="O limite muda com a temperatura. [p=0.2] {a}A curva de solubilidade mostra isso: [p=0.2] {b}temperatura no eixo de baixo, [p=0.1] {c}gramas de soluto em cem gramas de água no eixo do lado."),
    dict(id="s09", block="curva", text="{a}Veja o nitrato de potássio, um sal usado em adubo. [p=0.3] Para ler a curva, {b}suba da temperatura até a curva, [p=0.2] {c}e ande até o eixo do lado. [p=0.3] {d}A quarenta graus, o limite é de sessenta e quatro gramas."),
    dict(id="s10", block="curva", text="Ponha oitenta gramas desse sal em cem gramas de água, a quarenta graus. [p=0.2] {a}Oitenta passa de sessenta e quatro: [p=0.2] {b}é saturada com corpo de fundo, [p=0.2] e {c}oitenta menos sessenta e quatro dá dezesseis gramas no fundo."),
    dict(id="s11", block="curva", text="{a}Repare que a curva do nitrato sobe rápido: água quente dissolve muito mais. [p=0.3] {b}A do sal de cozinha é quase deitada: [p=0.2] aquecer quase não ajuda."),
    # gases
    dict(id="s12", block="gas", text="Com gás, é o contrário. [p=0.2] {a}Quanto mais quente a água, menos gás ela segura. [p=0.3] {b}A água gelada segura quase o dobro de gás carbônico que a água a vinte graus."),
    dict(id="s13", block="gas", text="{a}Por isso o refrigerante quente perde o gás: [p=0.2] o calor baixa o limite, [p=0.1] e {b}o gás que passou do limite escapa em bolhas. [p=0.3] {c}Gelado, ele segura o gás por mais tempo."),
    # erro
    dict(id="s14", block="erro", text="Agora, o erro mais comum: [p=0.2] {a}esquecer que o limite é para cem gramas de água. [p=0.3] A quarenta graus, {b}você põe quarenta gramas de nitrato em cinquenta gramas de água. [p=0.3] {c}A pessoa compara quarenta com sessenta e quatro, e diz que é insaturada."),
    dict(id="s15", block="erro", text="{a}Mas a água é a metade. [p=0.2] Pela regra de três, {b}metade da água dissolve metade do sal: trinta e dois gramas. [p=0.3] {c}Quarenta passa de trinta e dois, [p=0.2] e {d}quarenta menos trinta e dois dá oito gramas no fundo."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho de prova é {a}marcar a solução como um ponto no gráfico. [p=0.2] {b}Ponto abaixo da linha: insaturada. [p=0.2] {c}Ponto exatamente sobre a linha: saturada. [p=0.2] {d}Ponto mais alto que a linha: sobra sal no fundo, [p=0.1] e a sobra é a distância até a linha, [p=0.1] a não ser no caso raro da supersaturada."),
    dict(id="s17", block="atalho", text="Funciona porque {a}a curva é o próprio limite. [p=0.3] {b}Não compensa quando a água não é cem gramas: [p=0.2] antes, passe o sal para cada cem gramas de água, [p=0.1] e só depois marque o ponto."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Use a curva do nitrato de potássio. [p=0.3] {a}Você dissolve cem gramas do sal em cem gramas de água, a sessenta graus. [p=0.3] {b}A solução é saturada? [p=0.3] {c}Depois, ela esfria até quarenta graus, e o excesso vira cristal. [p=0.2] {d}Quantos gramas ficam no fundo?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="{a}A sessenta graus, a curva dá cento e dez gramas. [p=0.2] {b}Cem é menos que cento e dez: [p=0.1] {c}a solução é insaturada, tudo se dissolve. [p=0.3] {d}A quarenta graus, o limite cai para sessenta e quatro. [p=0.2] {e}Cem menos sessenta e quatro dá trinta e seis gramas, que ficam no fundo."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}a curva é o limite, [p=0.1] {b}abaixo dela é insaturada, sobre a linha é saturada, [p=0.1] {c}a sobra fica no fundo, [p=0.1] e {d}gás se dissolve menos no quente."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai medir {a}quanto soluto há em cada litro de solução: [p=0.2] {b}em gramas por litro, em porcentagem e em partes por milhão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
