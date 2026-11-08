# Estudativo · MAT-TRA-007 — Praticando: leis, identidades e equações (Matemática · Trigonometria Avançada · Identidades, adição de arcos e equações · prática).
# Habilidade: escolher entre lei dos senos e dos cossenos, simplificar expressões e resolver equações no ciclo.
# Pré-requisitos: MAT-TRA-001 a MAT-TRA-006. Próxima: nenhuma na trilha (fim de Trigonometria Avançada); nas playlists de
#   vestibular (Fuvest e Unicamp) vem MAT-PLN-001 (o que é polinômio: grau, valor e operações).
# Questões inéditas, criadas para esta aula; nenhuma é de prova real. Termos das aulas de origem: par completo, número fixo,
#   "Pitágoras com um ajuste", atalho de 120° (+ bc), "tudo em seno e cosseno", a música do seno da soma, a linha no ciclo e o parceiro.
# Q1: 6 e 10 com 120° (LAL → cossenos) · 36 + 100 + 6 · 10 = 196 → 14 m · confere: √136 ≈ 11,7 < 14 (aberto estica).
# Q2: 45° e 30°, lado de frente para 45° = 8 (par completo → senos) · número fixo 8 ÷ (√2/2) = 16/√2 = 8√2 · lado = 8√2 · 1/2 = 4√2 ≈ 5,6 (< 8).
# Q3: (sec² x − 1) · cos² x · sec² − 1 = tg² · (sen²/cos²) · cos² = sen² x (cos x ≠ 0).
# Q4: sen 15° = sen(45° − 30°) = √2/2 · √3/2 − 1/2 · √2/2 = (√6 − √2)/4 ≈ (2,4 − 1,4)/4 = 0,25 (exato ≈ 0,259).
# Q5: 2 sen x + √3 = 0 → sen x = −√3/2 · tabela: 60° · seno negativo: 3º e 4º · 180 + 60 = 240° = 4π/3 · 360 − 60 = 300° = 5π/3.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: leis, identidades e equações"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões criadas para esta aula, [p=0.2] uma para cada ferramenta da trilha. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] {c}Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a lei dos senos, [p=0.2] {b}a lei dos cossenos, [p=0.2] {c}as identidades, [p=0.2] {d}o seno da soma e da diferença [p=0.2] e {e}as equações no ciclo. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: lei dos cossenos
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Dois lados de um terreno medem {b}seis e dez metros, [p=0.2] e o ângulo entre eles é de {c}cento e vinte graus. [p=0.3] {d}Quanto mede o terceiro lado?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Dois lados e o ângulo entre eles: {a}nenhum par completo, lei dos cossenos. [p=0.3] Cento e vinte graus: {b}vale o atalho do mais o produto. [p=0.2] {c}Trinta e seis mais cem, mais seis vezes dez: [p=0.2] {d}cento e noventa e seis. [p=0.2] {e}A raiz dá catorze metros."),
    dict(id="s06", block="r1", text="Confira: o ângulo é aberto, e {a}o Pitágoras daria raiz de cento e trinta e seis, menos de doze. [p=0.2] {b}Catorze passou: faz sentido."),
    # questão 2: lei dos senos
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] Num triângulo, dois ângulos medem {b}quarenta e cinco e trinta graus. [p=0.2] {c}O lado de frente para os quarenta e cinco mede oito. [p=0.3] {d}Quanto mede o lado de frente para os trinta?"),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="Tem {a}par completo: oito e quarenta e cinco graus. [p=0.2] Lei dos senos. [p=0.3] O número fixo: {b}oito dividido pelo seno de quarenta e cinco, que é raiz de dois dividido por dois. [p=0.2] Dividir pela fração é multiplicar pela de ponta-cabeça: [p=0.2] {c}dezesseis dividido por raiz de dois. [p=0.2] Tirando a raiz de baixo, {d}oito raiz de dois."),
    dict(id="s10", block="r2", text="O lado de frente para os trinta: {a}oito raiz de dois vezes seno de trinta, um meio. [p=0.2] {b}Quatro raiz de dois. [p=0.2] Com raiz de dois perto de um vírgula quatro, cerca de cinco vírgula seis. [p=0.3] {c}Ângulo menor, lado menor: faz sentido."),
    # questão 3: identidade
    dict(id="s11", block="q3", text="{a}Questão três. [p=0.2] Simplifique: {b}secante ao quadrado de xis, menos um, [p=0.2] {c}tudo vezes cosseno ao quadrado de xis."),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="r3", text="Da identidade, {a}secante ao quadrado é um mais tangente ao quadrado. [p=0.2] Então {b}secante ao quadrado menos um é tangente ao quadrado. [p=0.3] Agora, {c}tudo em seno e cosseno: [p=0.2] seno ao quadrado dividido por cosseno ao quadrado, vezes cosseno ao quadrado. [p=0.2] {d}O cosseno ao quadrado é fator: corta. [p=0.2] {e}Sobra seno ao quadrado de xis."),
    # questão 4: seno da diferença
    dict(id="s14", block="q4", text="{a}Questão quatro. [p=0.2] Calcule {b}o seno de quinze graus, [p=0.2] {c}usando quarenta e cinco e trinta."),
    dict(id="s15", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="r4", text="Quinze é {a}quarenta e cinco menos trinta. [p=0.2] Pela música, com o sinal do meio trocado: [p=0.2] {b}seno de quarenta e cinco vezes cosseno de trinta, [p=0.2] {c}menos seno de trinta vezes cosseno de quarenta e cinco. [p=0.3] {d}Raiz de seis dividido por quatro, menos raiz de dois dividido por quatro."),
    dict(id="s17", block="r4", text="Mesmo denominador: {a}raiz de seis menos raiz de dois, tudo dividido por quatro. [p=0.3] {b}Cerca de dois vírgula quatro menos um vírgula quatro, dividido por quatro: [p=0.2] {c}uns zero vírgula vinte e cinco. [p=0.2] Ângulo pequeno, seno pequeno: faz sentido."),
    # questão 5: equação no ciclo
    dict(id="s18", block="q5", text="{a}Última questão. [p=0.2] Resolva {b}dois seno de xis mais raiz de três igual a zero, [p=0.2] {c}com xis entre zero e dois pi."),
    dict(id="s19", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="r5", text="Isole o seno: {a}seno de xis igual a menos raiz de três dividido por dois. [p=0.3] Sem o sinal, {b}é o seno de sessenta graus. [p=0.2] {c}Seno negativo: o ponto fica embaixo, no terceiro e no quarto quadrantes. [p=0.2] Trace a linha {d}abaixo do eixo: ela corta o ciclo em dois pontos."),
    dict(id="s21", block="r5", text="No terceiro, {a}cento e oitenta mais sessenta, duzentos e quarenta graus: [p=0.2] {b}quatro pi terços. [p=0.2] No quarto, {c}trezentos e sessenta menos sessenta, trezentos graus: [p=0.2] {d}cinco pi terços. [p=0.3] Quem parou no primeiro quadrante errou o sinal: {e}lá o seno é positivo."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}tem par completo, senos; [p=0.2] sem par, cossenos. [p=0.2] {b}Na identidade, tudo em seno e cosseno. [p=0.2] E {c}na equação, a linha corta o ciclo em dois pontos."),
    dict(id="s23", block="fim", text="Com isso, você fecha a trilha de trigonometria avançada. [p=0.3] Na sequência dos vestibulares, o próximo assunto é {a}polinômio: [p=0.2] {b}grau, valor numérico e as contas com eles. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
