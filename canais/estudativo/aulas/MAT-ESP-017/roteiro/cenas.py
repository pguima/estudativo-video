# Estudativo · MAT-ESP-017 — Sólidos compostos: somar e subtrair volumes (Matemática · Geometria Espacial · Sólidos compostos e razão entre volumes).
# Habilidade: achar o volume de um silo feito de cilindro e cone e o de uma peça com um furo cilíndrico.
# Pré-requisitos: MAT-ESP-013 (cone = um terço do cilindro; atalho π = 3), MAT-ESP-014 (esfera). Usa MAT-ESP-005 (cubo), MAT-ESP-008 (cilindro), MAT-ARE-008 (coroa), MAT-MED-005 (1 dm³ = 1 L). Próxima: MAT-ESP-018.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Hemisfério (MAT-ESP-015) não entra (fora do "já ensinado").
# Questão inédita, criada para esta aula.
# Contas: silo r = 2, π = 3: base 3·4 = 12 m²; cilindro h = 6: 72; cone h = 3: 12·3/3 = 12; total 84 m³ (= 28π).
#   Atalho: 6 + 3/3 = 7; 12·7 = 84. Erro: cilindro com a altura total 9: 12·9 = 108; 108 + 12 = 120.
#   Peça: cubo 10³ = 1.000 cm³; furo r = 2, h = 10: 3·4·10 = 120; 1.000 − 120 = 880 cm³.
#   Questão (em dm): R = 5, r = 4, comprimento 10, π = 3: 3·25·10 = 750; 3·16·10 = 480; 750 − 480 = 270 dm³ = 270 L.
#   Conferência pela coroa: 3·(25 − 16) = 27 dm²; 27·10 = 270.
# Visual:
#   s01, s05-s07: silo = E.cilindro com E.cone em cima (mesmo raio), as peças se separando e as alturas 6 e 3 marcadas.
#   s08-s09: E.cubo de aresta 10 com um E.cilindro de raio 2 atravessando (furo), o furo saindo da peça.
#   s10: silo com a altura 9 riscada em vermelho no cilindro. s11-s12: palco escuro do atalho.
#   s13-s16: tubo de concreto (E.cilindro com furo cilíndrico), ponta em forma de coroa.

TITULO = "Sólidos compostos: somar e subtrair volumes"

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
    dict(id="s01", block="gancho", text="{a}Um silo de fazenda: [p=0.2] {b}um cilindro com um telhado em forma de cone. [p=0.3] Não existe fórmula de silo. [p=0.2] E nem precisa: [p=0.2] {c}você corta o silo em sólidos que já conhece."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o volume de sólidos montados com peças, [p=0.2] com e sem furo, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três volumes: [p=0.2] {b}o cilindro, pi érre ao quadrado vezes agá; [p=0.2] {c}o cone, um terço do cilindro de mesma base e mesma altura; [p=0.2] e {d}o cubo, aresta vezes aresta vezes aresta. [p=0.3] Se faltar algum, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Passo um: separe o sólido em peças conhecidas. [p=0.2] {c}Passo dois: calcule o volume de cada peça, cada uma com a sua altura. [p=0.2] {d}Passo três: some o que foi juntado e subtraia o que foi tirado."),
    # silo
    dict(id="s05", block="silo", text="O silo: {a}um cilindro de raio dois metros e altura seis, [p=0.2] e em cima {b}um cone de mesmo raio, com três metros de altura. [p=0.2] {c}Use pi igual a três."),
    dict(id="s06", block="silo", text="{a}Base: três vezes dois ao quadrado dá doze metros quadrados. [p=0.2] Cilindro e cone têm essa mesma base. [p=0.3] {b}Cilindro: doze vezes seis dá setenta e dois. [p=0.2] {c}Cone: doze vezes três dá trinta e seis, [p=0.2] e dividido por três dá doze."),
    dict(id="s07", block="silo", text="As peças foram juntadas, então {a}some: [p=0.2] {b}setenta e dois mais doze dá oitenta e quatro. [p=0.3] O silo guarda {c}oitenta e quatro metros cúbicos de grãos."),
    # furo
    dict(id="s08", block="furo", text="Agora o contrário: {a}tirar. [p=0.2] Uma peça de metal é {b}um cubo de dez centímetros de aresta, [p=0.2] com {c}um furo cilíndrico de dois centímetros de raio, [p=0.2] que atravessa a peça de lado a lado."),
    dict(id="s09", block="furo", text="{a}Cubo: dez vezes dez vezes dez dá mil centímetros cúbicos. [p=0.2] O furo atravessa o cubo, então {b}a altura do furo é dez. [p=0.2] {c}Furo: dois ao quadrado dá quatro, [p=0.2] e três vezes quatro vezes dez dá cento e vinte. [p=0.3] O furo foi tirado, então {d}subtraia: [p=0.2] {e}mil menos cento e vinte dá oitocentos e oitenta centímetros cúbicos de metal."),
    # erro comum
    dict(id="s10", block="erro", text="O erro mais comum é {a}usar a altura total numa peça só. [p=0.2] O silo tem {b}nove metros, do chão até a ponta. [p=0.2] Quem põe nove no cilindro faz {c}doze vezes nove, que dá cento e oito, [p=0.2] e, com o cone, chega a {d}cento e vinte. [p=0.3] Mas o cilindro de nove metros já ocupa o lugar do cone. [p=0.2] {e}Cada peça usa só a sua altura."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho, para cilindro e cone de {a}mesmo raio. [p=0.2] O cone vale um cilindro com {b}um terço da altura dele. [p=0.3] Então junte as alturas: [p=0.2] {c}um terço de três dá um, [p=0.2] e {d}seis mais um dá sete. [p=0.2] {e}Doze vezes sete dá oitenta e quatro. [p=0.2] Uma conta só."),
    dict(id="s12", block="atalho", text="Funciona porque {a}a base é a mesma: [p=0.2] doze vezes seis, mais doze vezes um, [p=0.2] é {b}doze vezes sete. [p=0.3] {c}Não compensa quando os raios são diferentes, [p=0.2] como um telhado mais largo que a parede: [p=0.2] aí, {d}calcule peça por peça."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um tubo de concreto tem forma de {a}cilindro, [p=0.2] com {b}cinquenta centímetros de raio e um metro de comprimento. [p=0.2] Por dentro, passa {c}um furo cilíndrico de quarenta centímetros de raio, de ponta a ponta. [p=0.2] {d}Use pi igual a três. [p=0.3] {e}Quantos litros de concreto formam o tubo?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Trabalhe em {a}decímetros, porque o litro é um decímetro cúbico. [p=0.2] Dez centímetros fazem um decímetro. [p=0.2] {b}Raio de fora: cinquenta centímetros são cinco decímetros. [p=0.1] {c}Raio do furo: quarenta centímetros são quatro. [p=0.1] {d}Comprimento: um metro são dez decímetros. [p=0.3] {e}Cilindro cheio: três vezes vinte e cinco vezes dez dá setecentos e cinquenta."),
    dict(id="s16", block="resposta", text="{a}Furo: três vezes dezesseis vezes dez dá quatrocentos e oitenta. [p=0.2] O furo foi tirado: [p=0.2] {b}setecentos e cinquenta menos quatrocentos e oitenta dá duzentos e setenta. [p=0.3] São {c}duzentos e setenta litros de concreto. [p=0.3] Confira pela ponta do tubo, que é {d}uma coroa, o anel entre o círculo de fora e o furo: [p=0.2] {e}vinte e cinco menos dezesseis dá nove, e três vezes nove dá vinte e sete, [p=0.2] e {f}vinte e sete vezes dez dá duzentos e setenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}corte em peças conhecidas, [p=0.2] {b}cada peça com a sua altura, [p=0.2] {c}some o que junta e subtraia o que tira."),
    dict(id="s18", block="fim", text="Na próxima aula, a água mede o volume para você: [p=0.2] {a}você descobre o volume de uma pedra pelo quanto a água sobe num aquário [p=0.2] e {b}prevê se o líquido transborda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
