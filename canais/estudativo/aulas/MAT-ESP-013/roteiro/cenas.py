# Estudativo · MAT-ESP-013 — Cone: geratriz, área e volume (Matemática · Geometria Espacial · Pirâmides e cones).
# Habilidade: achar a geratriz de um cone de raio 3 e altura 4 (5), o volume (12π) e a área lateral (15π).
# Pré-requisitos: MAT-ARE-008 (A = πr², setor), MAT-ESP-008 (cilindro, πr²·h), MAT-ESP-012 (apótema, triângulo em pé, Pitágoras). Usa MAT-ESP-011 (um terço do prisma), MAT-ANG-016 (ternos e múltiplos), MAT-POL-004/005 (volta 2πr, fração da volta), MAT-ESP-002 (cone abre em círculo + leque). Próxima: MAT-ESP-014.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Letras: "érre", "agá", "gê".
# Questão inédita, criada para esta aula.
# Contas: g² = 3² + 4² = 25 → g = 5. V = π·9·4/3 = 12π (cilindro 36π). Leque: volta da base 2π·3 = 6π; círculo de raio 5: volta 10π, área 25π;
#   6π/10π = 3/5; 3/5 · 25π = 15π = π·3·5. Total 15π + 9π = 24π. Atalho π = 3: V = r²h = 9·4 = 36 = 12·3.
#   Erro: r = 6, h = 8 → π·6·8 = 48π; g = 10 → π·6·10 = 60π. Questão: r = 5, h = 12 → g = 13; lateral 65π = 195 cm²; V = 25·12 = 300 cm³ (= 100π).
# Visual:
#   s01: E.cilindro e E.cone de mesma base e altura; o cone despeja três vezes no cilindro.
#   s04-s07: E.cone com raio, altura (tracejada, por dentro) e geratriz (inclinada) marcadas; corte vertical mostra o triângulo retângulo 3-4-5.
#   s11-s13: molde do cone (E.cone planificado): círculo da base e leque de raio 5; a borda do leque (6π) comparada à volta do círculo de raio 5 (10π).
#   s14: cone 6-8-10 com a altura riscada em vermelho na lateral. s15-s16: palco escuro do atalho.

TITULO = "Cone: geratriz, área e volume"

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
    dict(id="s01", block="gancho", text="{a}Um copo em forma de cilindro [p=0.2] e {b}um copo em forma de cone, [p=0.2] com a mesma boca e a mesma altura. [p=0.3] Quantos cones cheios você despeja até encher o cilindro? [p=0.3] {c}Três, certinho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a linha inclinada do cone, [p=0.2] o volume e a área da lateral, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área do círculo é pi érre ao quadrado; [p=0.2] {c}a pirâmide é um terço do prisma de mesma base e mesma altura; [p=0.2] e {d}o triângulo em pé dentro da pirâmide, resolvido com Pitágoras. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="cone", text="{a}O cone tem {b}uma base redonda, um círculo, [p=0.2] e {c}uma lateral curva que afina até um ponto, {d}o vértice. [p=0.3] É a casquinha de sorvete, o funil, o chapéu de festa."),
    dict(id="s05", block="cone", text="{a}A altura desce do vértice até o centro da base, em pé, por dentro. [p=0.2] {b}A geratriz vai do vértice até a borda da base, inclinada, pela lateral. [p=0.3] É parecida com a apótema da pirâmide: [p=0.2] {c}por ser inclinada, é mais comprida que a altura."),
    dict(id="s06", block="geratriz", text="Corte o cone ao meio, de cima a baixo. [p=0.2] Aparece {a}um triângulo retângulo. [p=0.2] {b}A altura e o raio são os catetos, [p=0.2] e {c}a geratriz é a hipotenusa."),
    dict(id="s07", block="geratriz", text="Com {a}raio três e altura quatro: [p=0.2] {b}três ao quadrado dá nove, [p=0.2] {c}quatro ao quadrado dá dezesseis. [p=0.2] {d}Nove mais dezesseis dá vinte e cinco, [p=0.2] e {e}a raiz de vinte e cinco é cinco. [p=0.3] A geratriz mede cinco: [p=0.2] {f}é o terno três, quatro e cinco."),
    # volume
    dict(id="s08", block="volume", text="Agora o volume. [p=0.2] O cone faz com o cilindro {a}o mesmo que a pirâmide faz com o prisma: [p=0.2] {b}é um terço do cilindro de mesma base e mesma altura. [p=0.3] Foi o que você viu no começo: {c}três cones enchem um cilindro."),
    dict(id="s09", block="volume", text="Na fórmula: {a}vê igual a pi érre ao quadrado vezes agá, dividido por três. [p=0.2] {b}Pi érre ao quadrado é a área da base, [p=0.1] e érre é o raio da base. [p=0.2] {c}Agá é a altura."),
    dict(id="s10", block="volume", text="No cone de raio três e altura quatro: [p=0.2] {a}a base tem nove pi. [p=0.2] {b}Vezes quatro dá trinta e seis pi: [p=0.2] esse é o cilindro. [p=0.2] {c}Dividido por três dá doze pi."),
    # área lateral
    dict(id="s11", block="leque", text="E a área da lateral? [p=0.2] {a}Abra o cone como um molde. [p=0.2] A lateral vira {b}um leque, um setor de círculo. [p=0.3] {c}O raio desse leque é a geratriz, cinco. [p=0.2] E {d}a borda curva do leque é a volta da base, [p=0.2] porque ela contornava o círculo de baixo."),
    dict(id="s12", block="leque", text="{a}A volta da base, de raio três, mede seis pi. [p=0.2] {b}Um círculo inteiro de raio cinco teria a volta de dez pi. [p=0.3] Seis pi de dez pi: [p=0.2] o leque é {c}três quintos do círculo de raio cinco."),
    dict(id="s13", block="leque", text="No setor, a área acompanha a borda. [p=0.2] {a}O círculo de raio cinco tem vinte e cinco pi de área, [p=0.2] e {b}três quintos de vinte e cinco pi dá quinze pi. [p=0.3] Repare: quinze é três vezes cinco, o raio vezes a geratriz. [p=0.2] Não é sorte: a fração do leque é sempre o raio dividido pela geratriz, [p=0.2] e a conta sempre termina em {c}pi vezes o raio vezes a geratriz: [p=0.2] {d}área lateral igual a pi érre gê. [p=0.3] Somando a base, nove pi, {e}a área total dá vinte e quatro pi."),
    # erro comum
    dict(id="s14", block="erro", text="O erro mais comum é {a}usar a altura no lugar da geratriz, na área lateral. [p=0.2] Num cone de {b}raio seis e altura oito, [p=0.2] a pessoa faz {c}pi vezes seis vezes oito, e acha quarenta e oito pi. [p=0.3] Mas a lateral é inclinada. [p=0.2] {d}A geratriz é dez, do terno seis, oito e dez, [p=0.2] e a área lateral dá {e}sessenta pi. [p=0.3] {f}Altura vai no volume. Geratriz vai na lateral."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para o volume, quando a prova manda usar {a}pi igual a três. [p=0.3] {b}O três do pi cancela o dividido por três. [p=0.2] Sobra só {c}érre ao quadrado vezes agá. [p=0.3] No cone de raio três e altura quatro: [p=0.2] {d}nove vezes quatro dá trinta e seis. [p=0.2] Confira: {e}doze vezes três também dá trinta e seis."),
    dict(id="s16", block="atalho", text="Funciona porque {a}multiplicar por três e dividir por três se desfazem. [p=0.3] {b}Não compensa quando a prova quer a resposta com o pi escrito, [p=0.2] ou com pi igual a três vírgula catorze. [p=0.2] Aí, {c}faça a conta inteira."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um chapéu de festa tem forma de cone, [p=0.2] com {a}raio de cinco centímetros e {b}altura de doze. [p=0.2] {c}Use pi igual a três. [p=0.3] {d}Quanto papel tem a lateral do chapéu? [p=0.2] {e}E quantos centímetros cúbicos cabem dentro dele?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Primeiro a geratriz. [p=0.2] Catetos cinco e doze: {a}é o terno cinco, doze e treze. [p=0.2] {b}A geratriz mede treze. [p=0.3] Lateral: {c}pi vezes cinco vezes treze dá sessenta e cinco pi. [p=0.2] {d}Sessenta e cinco vezes três dá cento e noventa e cinco centímetros quadrados de papel."),
    dict(id="s20", block="resposta", text="Volume, pelo atalho: [p=0.2] {a}cinco ao quadrado dá vinte e cinco, [p=0.2] e {b}vinte e cinco vezes doze dá trezentos centímetros cúbicos. [p=0.3] Repare: {c}a altura doze foi para o volume, [p=0.2] e {d}a geratriz treze foi para a lateral."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}geratriz pelo Pitágoras, [p=0.2] {b}volume, um terço do cilindro, [p=0.2] {c}lateral, pi érre gê."),
    dict(id="s22", block="fim", text="Na próxima aula, o sólido mais redondo de todos: {a}a esfera. [p=0.2] Você usa {b}as fórmulas da área e do volume [p=0.2] e calcula quanto cabe num {c}reservatório esférico de três metros de raio. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
