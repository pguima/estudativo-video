# Estudativo · MAT-FAV-008 — Praticando: funções modular, composta e inversa (Matemática · Funções Avançadas · prática).
# Habilidade: resolver equações modulares, compor funções, achar inversas e reconhecer a paridade pelo gráfico.
# Pré-requisitos: MAT-FAV-001 a MAT-FAV-007. Próxima: nenhuma (fecha a trilha).
# Questões inéditas, criadas para esta aula.
# 1. Água: 30 se 0 ≤ x ≤ 10; 30 + 5(x − 10) se x > 10 · x = 14 → 14 − 10 = 4 → 4 · 5 = 20 → 50 · fronteira: 30 e 30 + 0 = 30, sem salto.
# 2. |x − 1| ≤ 3 → centro 1, raio 3 → [−2, 4] → inteiros −2, −1, 0, 1, 2, 3, 4 = 7 (4 − (−2) = 6, mas as pontas entram).
# 3. f(x + 1) = 3x + 5 · f(7): x + 1 = 7 → x = 6 → 18 + 5 = 23 · erro: 3 · 7 + 5 = 26 · conferência pela lei: f(u) = 3(u − 1) + 5 = 3u + 2 → f(7) = 23.
# 4. f(x) = (x + 5)/2 → f⁻¹(x) = 2x − 5 · f⁻¹(3) = 1 · f(1) = 6/2 = 3.
# 5. Gráficos: A = x² − 2 (par), B = x³ − 3x em escala (ímpar), C = |x − 1| (nenhuma) → resposta B.
# Visual: chave da água e plano com a conta; reta numérica com os sete inteiros acendendo; caixinha do de dentro; setas de ida e volta;
#   três planos pequenos lado a lado (A, B, C) com dobra e meia volta.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: funções modular, composta e inversa"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com as funções desta trilha, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}cinco ferramentas: [p=0.2] {b}a lei certa para cada faixa; [p=0.2] {c}o módulo como distância; [p=0.2] {d}a composta, de dentro para fora; [p=0.2] {e}a inversa, que desfaz de trás para frente; [p=0.2] e {f}a simetria do gráfico. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: por partes
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma cidade cobra a água assim: [p=0.2] {b}até dez metros cúbicos, trinta reais fixos. [p=0.2] {c}Acima de dez, trinta reais, mais cinco reais por metro cúbico que passar dos dez. [p=0.3] {d}Quanto paga quem gastou catorze metros cúbicos?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Catorze é mais que dez: vale a segunda regra. [p=0.2] {b}Passou dos dez: catorze menos dez, quatro. [p=0.2] {c}Quatro vezes cinco, vinte. [p=0.2] {d}Trinta mais vinte: cinquenta reais. [p=0.3] Na fronteira, {e}as duas regras dão trinta: [p=0.2] {f}o gráfico não tem salto."),
    # situação 2: inequação modular
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}Quantos números inteiros satisfazem módulo de xis menos um, menor ou igual a três?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}O centro é um, e o raio é três. [p=0.2] Pontas: {b}um menos três, menos dois; [p=0.2] e {c}um mais três, quatro. [p=0.2] {d}Menor ou igual: fica entre, com as pontas. [p=0.3] Os inteiros são {e}menos dois, menos um, zero, um, dois, três e quatro. [p=0.2] {f}Sete números. [p=0.3] Cuidado: {g}de uma ponta à outra são seis passos, [p=0.2] mas os inteiros são sete, porque as pontas entram."),
    # situação 3: composta
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] Sabe-se que {b}éfe de xis mais um é igual a três xis mais cinco. [p=0.3] {c}Quanto vale éfe de sete?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] Use o atalho: {a}faça o de dentro valer sete. [p=0.2] {b}Xis mais um igual a sete dá xis igual a seis. [p=0.2] {c}No lado direito: três vezes seis, mais cinco, vinte e três. [p=0.3] {d}Éfe de sete é vinte e três. [p=0.3] O erro aqui é {e}trocar o xis por sete direto, [p=0.2] o que daria {f}vinte e seis. [p=0.2] O sete é o valor do de dentro, não do xis."),
    # situação 4: inversa
    dict(id="s12", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Éfe de xis é xis mais cinco, sobre dois. [p=0.3] {c}Ache a inversa e calcule éfe à menos um de três."),
    dict(id="s13", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta4", text="Vamos lá. [p=0.2] {a}Éfe soma cinco e depois divide por dois. [p=0.2] A inversa desfaz de trás para frente: [p=0.2] {b}multiplica por dois e depois tira cinco. [p=0.2] {c}Éfe à menos um de xis é dois xis menos cinco. [p=0.3] {d}No três: dois vezes três, seis; menos cinco, um. [p=0.2] Confira: {e}um mais cinco, seis; dividido por dois, três."),
    # situação 5: paridade pelo gráfico
    dict(id="s15", block="questao5", text="{a}Última situação. [p=0.2] Olhe os três gráficos. [p=0.2] {b}O A é uma parábola com o ponto mais baixo em ípsilon menos dois. [p=0.2] {c}O B sobe, desce e volta a subir, passando pela origem. [p=0.2] {d}O C é um vê com a ponta em xis um. [p=0.3] {e}Qual deles é de uma função ímpar?"),
    dict(id="s16", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta5", text="Vamos lá. [p=0.2] {a}O A é simétrico no eixo ípsilon: dobra e cobre. [p=0.2] {b}É par. [p=0.3] {c}O C não dobra no eixo ípsilon, porque a ponta está em xis um, [p=0.2] e também não se encaixa com meia volta. [p=0.2] {d}Nem par, nem ímpar. [p=0.3] {e}O B, girado meia volta em torno da origem, cai em cima de si mesmo. [p=0.2] {f}O B é ímpar."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}cada ferramenta responde uma pergunta. [p=0.2] {b}Qual faixa? [p=0.1] Qual distância? [p=0.1] Quem vem primeiro? [p=0.1] Como desfazer? [p=0.1] Que espelho?"),
    dict(id="s19", block="fim", text="Com esta aula, {a}você fecha a trilha de funções modular, composta e inversa. [p=0.2] {b}Se algum passo travou, procure a aula no canal e refaça. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
