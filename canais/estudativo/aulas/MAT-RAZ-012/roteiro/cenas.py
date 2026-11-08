# Estudativo · MAT-RAZ-012 — Praticando: razão, proporção e regra de três (Matemática · Razão e Proporção · prática).
# Habilidade: identificar o tipo de relação e resolver problemas de regra de três simples e composta.
# Pré-requisitos: MAT-RAZ-001 a MAT-RAZ-011. Próxima: MAT-RAZ-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Termos das aulas anteriores: teste do dobro, colunas, produto cruzado, multiplicar na linha, horas de trabalho (homem-hora), fator ao quadrado.
# 1) 30 + 4 · 5 = 50; 30 + 4 · 10 = 70 (erro: 50 · 2 = 100). (A academia 50 + 80 já é a questão de MAT-RAZ-005.) 2) 96/x = 4/9 → 4x = 864 → x = 216; 96 ÷ 4 = 24; 24 · 9 = 216. (A impressora 45/3/8 é a questão de MAT-RAZ-006.)
# 3) 90 · 4 = 360 = 120 · x → x = 3. 4) 6 · 8 · 20 = 960 = 8 · 10 · x = 80x → x = 12; colunas 20/x = 8/6 · 10/8 = 80/48 = 5/3 → x = 12.
# 5) lado 5 → 25 m², R$ 100 (R$ 4 por m²); lado 10 → 100 m² → 4 · 100 = R$ 400 (erro: 200).

TITULO = "Praticando: razão, proporção e regra de três"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações do dia a dia, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, a primeira pergunta é sempre a mesma: [p=0.2] {b}que tipo de relação é essa? [p=0.3] Depois, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar estas ferramentas: [p=0.2] {a}o teste do dobro, [p=0.2] {b}a regra de três direta, com produto cruzado, [p=0.2] {c}a inversa, multiplicando na linha, [p=0.2] {d}a composta, comparando cada coluna com a do xis, [p=0.2] e {e}o quadrado do lado na área. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: nenhuma
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma transportadora cobra {b}trinta reais de despacho por encomenda, [p=0.1] mais {c}quatro reais por quilo. [p=0.3] Uma encomenda de cinco quilos custa {d}cinquenta reais. [p=0.2] {e}Quanto custa uma de dez quilos?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Os quilos dobraram, então muita gente {a}dobra o preço: cem reais. [p=0.3] Mas o despacho {b}não dobra. [p=0.2] {c}Dez vezes quatro dá quarenta. [p=0.2] {d}Mais trinta: setenta reais."),
    dict(id="s06", block="resposta1", text="Pelo teste do dobro, {a}dobrou o peso e o preço não dobrou. [p=0.2] {b}Não é proporcional, [p=0.2] e {c}regra de três aqui dá errado. [p=0.3] O teste do zero confirma: {d}uma encomenda sem peso ainda pagaria os trinta do despacho. [p=0.2] É o mesmo caso do táxi com bandeirada. [p=0.3] Antes de qualquer regra de três, {e}descubra o tipo de relação."),
    # situação 2: direta
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma padaria faz {b}noventa e seis pães com quatro quilos de farinha, sempre com a mesma receita. [p=0.3] {c}Quantos pães ela faz com nove quilos de farinha?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Teste do dobro: {a}dobrando a farinha, dobram os pães. [p=0.2] {b}Direta. [p=0.3] Colunas: {c}noventa e seis dividido por xis igual a quatro nonos. [p=0.2] Produto cruzado: {d}quatro vezes xis igual a noventa e seis vezes nove, oitocentos e sessenta e quatro. [p=0.2] {e}Xis igual a duzentos e dezesseis pães."),
    dict(id="s10", block="resposta2", text="Pelo valor de uma unidade é ainda mais rápido: [p=0.2] {a}noventa e seis dividido por quatro dá vinte e quatro pães por quilo. [p=0.2] {b}Vinte e quatro vezes nove dá duzentos e dezesseis. [p=0.3] Use o caminho que achar mais fácil: [p=0.2] {c}os caminhos chegam no mesmo lugar."),
    # situação 3: inversa
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] A {b}noventa quilômetros por hora, uma viagem leva {c}quatro horas. [p=0.3] {d}A cento e vinte quilômetros por hora, quanto tempo leva a mesma viagem?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Teste do dobro: {a}dobrando a velocidade, o tempo cai pela metade. [p=0.2] {b}Inversa. [p=0.3] Multiplique na linha: {c}noventa vezes quatro dá trezentos e sessenta, [p=0.2] {d}igual a cento e vinte vezes xis. [p=0.2] {e}Xis igual a três horas. [p=0.3] Mais rápido, menos tempo: {f}faz sentido."),
    # situação 4: composta com inversa
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Seis pintores, trabalhando oito horas por dia, pintam um prédio em vinte dias. [p=0.3] {c}Oito pintores, trabalhando dez horas por dia, pintam o mesmo prédio em quantos dias?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Compare cada coluna com a dos dias. [p=0.2] {a}Mais pintores, menos dias: inversa. [p=0.2] {b}Mais horas por dia, menos dias: inversa. [p=0.3] Vire as colunas de pintores e de horas: {c}vinte dividido por xis igual a oito sextos vezes dez oitavos, [p=0.2] que dá {d}cinco terços. [p=0.2] Produto cruzado: {e}xis igual a doze dias. [p=0.3] Mais gente e mais horas, {f}menos dias."),
    dict(id="s17", block="atalho", text="O atalho chega mais rápido: [p=0.2] o prédio é o mesmo, então {a}as horas de trabalho não mudam. [p=0.3] {b}Seis vezes oito vezes vinte: novecentos e sessenta. [p=0.2] {c}Oito vezes dez vezes xis: oitenta xis. [p=0.2] {d}Novecentos e sessenta dividido por oitenta: doze dias."),
    # situação 5: quadrado
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Uma lona quadrada de {b}cinco metros de lado custa {c}cem reais. [p=0.2] O preço é {d}cobrado pela área. [p=0.3] {e}Quanto custa uma lona quadrada com o dobro do lado?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Quem dobra o preço responde {a}duzentos. [p=0.2] Mas o preço segue a área, [p=0.2] e {b}dobrar o lado quadruplica a área. [p=0.3] {c}Cem vezes quatro: quatrocentos reais."),
    dict(id="s21", block="resposta5", text="Conferindo: a lona menor tem {a}cinco vezes cinco dá vinte e cinco metros quadrados, quatro reais cada. [p=0.2] A maior tem {b}dez vezes dez dá cem metros quadrados. [p=0.2] {c}Cem vezes quatro: quatrocentos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}primeiro, o tipo de relação. [p=0.2] {b}Depois, a conta. [p=0.2] {c}No fim, veja se o resultado faz sentido."),
    dict(id="s23", block="fim", text="Na próxima aula, começa a {a}divisão proporcional: [p=0.2] você reparte {b}mil e duzentos reais na razão três para cinco [p=0.2] e {c}divide o lucro entre sócios de um jeito justo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
