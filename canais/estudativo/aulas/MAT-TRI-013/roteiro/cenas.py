# Estudativo · MAT-TRI-013 — Praticando: ciclo e funções trigonométricas (Matemática · Trigonometria · Ciclo e funções trigonométricas · prática).
# Habilidade: usar o ciclo para achar valores e ler máximo, mínimo e período em uma situação periódica.
# Pré-requisitos: MAT-TRI-007, MAT-TRI-008, MAT-TRI-009, MAT-TRI-010, MAT-TRI-011, MAT-TRI-014, MAT-TRI-012. Próxima: nenhuma na trilha;
#   na playlist Matemática do Zero vem MAT-ESP-001 (sólidos, poliedros e relação de Euler).
# Questões inéditas, criadas para esta aula. Estufa imaginada (não são dados reais). Seno, cosseno e tangente por extenso; graus por extenso; π narrado "pi"; radianos lidos como na MAT-TRI-007 ("pi quartos", "três pi quartos", "pi meios").
# Q1: 495° − 360° = 135° · 2º quadrante (entre 90° e 180°) · 45° cabe 4 vezes em 180° → π/4 · 135° = 3 · 45° → 3π/4 · confere: 3 · 180 / 4 = 135.
#   (480° e 120° já são a questão da MAT-TRI-007: evitados.)
# Q2: sen 495° = sen 135° · 180° − 135° = 45° · sen 45° = √2/2, positivo no 2º · cos 45° = √2/2, negativo no 2º → −√2/2.
# Q3: sen x = −5/13, 3º quadrante · 13² − 5² = 169 − 25 = 144 · √144 = 12 · cos x = −12/13 · tg x = (−5/13) ÷ (−12/13) = 5/12 (positiva).
#   Erro: tangente negativa por hábito; menos dividido por menos dá mais (to, se, ta, co: no 3º só a tangente é positiva).
# Q4: estufa T(t) = 22 + 6 sen(πt/12), t em horas a partir das 9 h · máx 28 · mín 16 · período 24 h (dobro de 12) ·
#   máximo quando πt/12 = π/2 → t/12 = 1/2 → t = 6 → 9 + 6 = 15 h.
# Visual (E.circulo, E.plano, E.curva, E.triangulo, E.angulo):
#   s03-s05: ciclo com o arco de 495° dando uma volta e parando em 135°; 2º quadrante aceso; 135° = 3π/4.
#   s06-s08: ciclo com 135° e o parceiro 45° (espelho); projeções no eixo vertical (√2/2) e horizontal (−√2/2); sinais do 2º quadrante.
#   s09-s12: ciclo com arco no 3º quadrante; triângulo 5-12-13 abaixo e à esquerda; sinais; tangente positiva em verde.
#   s13-s16: gráfico de 22 + 6 sen(πt/12) com t de 0 a 24, máximo em t = 6 (15 h), mínimo em t = 18; relógio marcando 15 h.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: ciclo e funções trigonométricas"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões criadas para esta aula, [p=0.2] do ciclo trigonométrico até uma onda do dia a dia. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}cinco ferramentas: [p=0.2] {b}radianos e voltas no ciclo, [p=0.2] {c}o sinal do seno e do cosseno em cada quadrante, [p=0.2] {d}a redução ao primeiro quadrante, [p=0.2] {e}a relação fundamental [p=0.2] e {f}máximo, mínimo e período de uma onda. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: ciclo e radianos
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Um arco mede {b}quatrocentos e noventa e cinco graus. [p=0.3] {c}Em que quadrante ele termina, [p=0.2] e quanto mede, em radianos, o ângulo da primeira volta que cai no mesmo ponto?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Tire uma volta inteira: {a}quatrocentos e noventa e cinco menos trezentos e sessenta dá cento e trinta e cinco graus. [p=0.3] Cento e trinta e cinco fica {b}entre noventa e cento e oitenta: segundo quadrante. [p=0.3] Para radianos, o atalho: {c}quarenta e cinco cabe quatro vezes em cento e oitenta, então é pi quartos. [p=0.2] {d}Cento e trinta e cinco é três vezes quarenta e cinco, [p=0.2] então vale {e}três pi quartos. [p=0.3] Conferindo: [p=0.2] {f}troque o pi por cento e oitenta. [p=0.2] Três vezes cento e oitenta dá quinhentos e quarenta, [p=0.2] e dividido por quatro dá cento e trinta e cinco. [p=0.2] Bateu."),
    # questão 2: redução e sinais
    dict(id="s06", block="questao2", text="{a}Questão dois, com o mesmo arco. [p=0.3] {b}Quanto valem o seno e o cosseno de quatrocentos e noventa e cinco graus?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Mesmo ponto, mesmos valores: {a}vale o que vale cento e trinta e cinco. [p=0.2] O parceiro no primeiro quadrante: {b}cento e oitenta menos cento e trinta e cinco dá quarenta e cinco. [p=0.3] {c}Seno de quarenta e cinco é raiz de dois dividido por dois, [p=0.2] e no segundo quadrante {d}o seno é positivo. [p=0.3] {e}O cosseno de quarenta e cinco tem o mesmo valor, [p=0.2] mas no segundo quadrante {f}o cosseno é negativo: [p=0.2] {g}menos raiz de dois dividido por dois."),
    # questão 3: relação fundamental
    dict(id="s09", block="questao3", text="{a}Questão três. [p=0.2] O seno de um ângulo vale {b}menos cinco treze avos, [p=0.2] e o ângulo está {c}no terceiro quadrante. [p=0.3] {d}Calcule o cosseno e a tangente."),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] Pela relação fundamental, ou pelo triângulo: [p=0.2] {a}oposto cinco, hipotenusa treze. [p=0.2] {b}Cento e sessenta e nove menos vinte e cinco dá cento e quarenta e quatro, [p=0.2] e {c}a raiz dá doze. [p=0.3] No terceiro quadrante, o ponto fica à esquerda e embaixo: [p=0.2] {d}cosseno negativo, menos doze treze avos."),
    dict(id="s12", block="resposta3", text="A tangente é seno dividido por cosseno: [p=0.2] {a}menos cinco treze avos, dividido por menos doze treze avos. [p=0.2] Os treze avos se cancelam. [p=0.3] Aqui mora a pegadinha: [p=0.2] {b}muita gente põe o sinal de menos por hábito. [p=0.2] Mas {c}negativo dividido por negativo dá positivo: [p=0.2] no terceiro quadrante, pelo to, se, ta, co, só a tangente é positiva. [p=0.2] {d}Tangente: cinco doze avos."),
    # questão 4: situação periódica
    dict(id="s13", block="questao4", text="{a}Última questão. [p=0.2] Numa estufa imaginada para esta aula, a temperatura, em graus Celsius, é {b}vinte e dois, mais seis vezes o seno de pi tê dividido por doze. [p=0.2] {c}O tempo tê conta as horas a partir das nove da manhã. [p=0.3] {d}Qual é a temperatura máxima, a mínima e o período? [p=0.2] {e}E a que horas a estufa fica mais quente?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}Máxima: vinte e dois mais seis dá vinte e oito graus. [p=0.2] {b}Mínima: vinte e dois menos seis dá dezesseis graus. [p=0.3] Período, pelo atalho das marés: [p=0.2] pi tê dividido por doze, {c}o dobro de doze dá vinte e quatro horas. [p=0.2] {d}O ciclo se repete todo dia."),
    dict(id="s16", block="resposta4", text="E a hora mais quente? [p=0.2] O seno vale um {a}em noventa graus, ou pi meios. [p=0.3] {b}Pi tê dividido por doze igual a pi meios. [p=0.2] {c}Corte o pi de cada lado: tê dividido por doze igual a um meio. [p=0.2] {d}Tê igual a seis. [p=0.3] Seis horas depois das nove: {e}às três da tarde. [p=0.2] Faz sentido: é perto da hora mais quente do dia. [p=0.3] E a mais fria? [p=0.2] {f}Seno menos um, em duzentos e setenta graus, ou três pi meios. [p=0.2] Pelo mesmo caminho, tê dividido por doze igual a três meios, e tê dá dezoito. [p=0.2] Nove mais dezoito dá vinte e sete, [p=0.2] que passa da meia-noite em três horas: {g}três da madrugada."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}no ciclo, tire as voltas, ache o quadrante e reduza. [p=0.2] {b}O tamanho vem da conta, o sinal vem do quadrante. [p=0.2] E na onda, {c}máximo, mínimo e período saem de três contas."),
    dict(id="s18", block="fim", text="Com isso, você fecha a trilha de trigonometria. [p=0.2] Na próxima aula, a matemática {a}ganha volume: [p=0.2] você começa a geometria espacial, [p=0.2] {b}separa os sólidos, conta faces, arestas e vértices [p=0.2] e conhece {c}a relação de Euler. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
