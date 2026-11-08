# Estudativo · MAT-ESP-020 — Razão entre volumes de sólidos semelhantes (Matemática · Geometria Espacial · Sólidos compostos e razão entre volumes).
# Habilidade: usar k³: dobrar as medidas multiplica o volume por 8, e cortar um cone na metade da altura deixa em cima 1/8 do volume.
# Pré-requisitos: MAT-ARE-010 (área vezes k², k narrado "cá"), MAT-ESP-013 (cone de raio 3 e altura 4: 12π).
#   Usa MAT-ANG-012 (triângulos semelhantes), MAT-RAZ-022 (escala ao cubo), MAT-ESP-005 (volume do bloco). Próxima: MAT-ESP-021.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra k narrada "cá"; pi narrado "pi".
# Questão inédita, criada para esta aula. Esfera fora do "já ensinado" desta aula: nenhum exemplo com esfera.
# Contas: 2 · 2 · 2 = 8. Bloco 2 · 3 · 4 = 24; 4 · 6 · 8 = 192 = 8 · 24. 3³ = 27.
#   Cone r = 3, h = 4: 9 · 4 / 3 = 12π. Cone r = 6, h = 8: 36 · 8 = 288, / 3 = 96π = 8 · 12π. Tronco 96π − 12π = 84π = 7/8.
#   Taça 400 mL até metade: 400 / 8 = 50 (erro: 200). Cubos 1, 8, 27, 64, 125; 4³ = 64; 1,26³ ≈ 2,0004.
#   Questão: 250 · 8 = 2 000 mL; 270 / 27 = 10 mL.
# Visual:
#   s01, s11, s12: E.cone de ponta para baixo (taça) com líquido até metade da altura.
#   s04-s05: E.cubo de aresta 1 e E.cubo de aresta 2 dividido em 8 cubinhos.
#   s06: blocos 2 × 3 × 4 e 4 × 6 × 8.
#   s07: tabela comprimento · k, área · k², volume · k³.
#   s08-s10: E.cone r = 3, h = 4 ao lado do cone r = 6, h = 8; corte na metade da altura: cone de cima e tronco; corte lateral com dois triângulos semelhantes.
#   s13-s14: palco escuro com os cubos 1, 8, 27, 64, 125.

TITULO = "Razão entre volumes de sólidos semelhantes"

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
    dict(id="s01", block="gancho", text="{a}Uma taça em forma de cone, de ponta para baixo, [p=0.2] com suco até {b}a metade da altura. [p=0.3] Está meio cheia? [p=0.2] Não. [p=0.2] Tem só {c}um oitavo do que cabe nela."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você compara volumes de sólidos ampliados ou reduzidos sem calcular cada um, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}em figuras semelhantes, todas as medidas são multiplicadas pelo mesmo número, a razão de semelhança, cá; [p=0.2] {c}a área fica multiplicada por cá ao quadrado; [p=0.2] e {d}o volume do cone é pi érre ao quadrado vezes a altura, dividido por três. [p=0.3] Se faltar alguma, procure no canal."),
    # dobrar o cubo
    dict(id="s04", block="cubo", text="Sólidos {a}semelhantes têm a mesma forma, em tamanhos diferentes. [p=0.2] Pegue {b}um cubinho de um centímetro de aresta. [p=0.2] Agora, {c}dobre a aresta: dois centímetros. [p=0.3] Quantos cubinhos cabem? [p=0.2] {d}Dois na frente, dois para o lado, dois para cima: [p=0.2] {e}dois vezes dois vezes dois dá oito."),
    dict(id="s05", block="cubo", text="O volume usa {a}três medidas: comprimento, largura e altura. [p=0.2] E {b}cada uma ganhou o fator dois. [p=0.3] Por isso, {c}o volume fica multiplicado por dois ao cubo, que dá oito."),
    dict(id="s06", block="bloco", text="Vale para {a}qualquer sólido. [p=0.2] Uma caixa de {b}dois por três por quatro centímetros tem vinte e quatro centímetros cúbicos. [p=0.2] Com o dobro de cada medida, vira {c}quatro por seis por oito, [p=0.2] e quatro vezes seis vezes oito dá cento e noventa e dois. [p=0.3] {d}Cento e noventa e dois dividido por vinte e quatro dá oito."),
    dict(id="s07", block="regra", text="Na fórmula: se a razão de semelhança é {a}cá, [p=0.2] {b}a razão entre os volumes é cá ao cubo, [p=0.2] a mesma escala ao cubo da maquete. [p=0.3] Junto com o que você já sabe: [p=0.2] {c}comprimento, vezes cá; [p=0.2] {d}área, vezes cá ao quadrado; [p=0.2] {e}volume, vezes cá ao cubo. [p=0.3] Medidas três vezes maiores? {f}Volume vinte e sete vezes maior."),
    # cone
    dict(id="s08", block="cone", text="Agora, o cone. [p=0.2] Um cone de {a}raio três e altura quatro tem volume {b}doze pi. [p=0.3] Dobre tudo: {c}raio seis e altura oito. [p=0.2] Pela fórmula, {d}seis ao quadrado dá trinta e seis, [p=0.2] vezes oito dá duzentos e oitenta e oito, [p=0.2] dividido por três dá noventa e seis pi. [p=0.3] {e}Noventa e seis é oito vezes doze."),
    dict(id="s09", block="corte", text="Corte esse cone grande {a}na metade da altura, paralelo à base. [p=0.2] O pedaço de cima é {b}um cone menor, com a mesma forma. [p=0.3] Olhe o corte de lado: {c}dois triângulos semelhantes. [p=0.2] Altura pela metade, {d}raio pela metade também: [p=0.2] raio três e altura quatro."),
    dict(id="s10", block="corte", text="É o cone de doze pi! [p=0.2] A razão é um meio, [p=0.2] e {a}um meio ao cubo dá um oitavo. [p=0.3] {b}Em cima, um oitavo do volume. [p=0.2] Embaixo, a parte larga, chamada {c}tronco de cone, [p=0.2] fica com {d}sete oitavos: [p=0.2] noventa e seis menos doze dá oitenta e quatro pi."),
    dict(id="s11", block="taca", text="E a taça do começo? [p=0.2] De ponta para baixo, o suco forma {a}um cone com metade da altura da taça. [p=0.2] Por isso, {b}um oitavo. [p=0.3] Numa taça de {c}quatrocentos mililitros, [p=0.2] {d}quatrocentos dividido por oito dá cinquenta mililitros."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}pensar que metade da altura é metade do volume. [p=0.2] Quem faz isso diz {b}duzentos mililitros. [p=0.3] Mas a parte de baixo da taça é {c}a ponta, estreita. [p=0.2] {d}O suco encolhe nas três medidas, não só na altura."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para o caminho de volta: {a}decore os cubos. [p=0.2] {b}Um. [p=0.1] Oito. [p=0.1] Vinte e sete. [p=0.1] Sessenta e quatro. [p=0.1] Cento e vinte e cinco. [p=0.3] Se um volume é {c}sessenta e quatro vezes outro, [p=0.2] {d}as medidas são quatro vezes maiores, [p=0.2] porque quatro vezes quatro vezes quatro dá sessenta e quatro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o volume multiplica o fator da medida três vezes: cá vezes cá vezes cá. [p=0.3] {b}Não compensa quando o volume não é um cubo da lista. [p=0.2] Volume dobrado, por exemplo: [p=0.2] {c}um ao cubo dá um, e dois ao cubo já dá oito. [p=0.2] Nenhum número inteiro ao cubo dá dois. [p=0.2] {d}As medidas crescem só uns vinte e seis por cento, [p=0.2] e esse número não sai de cabeça."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um pote guarda duzentos e cinquenta mililitros. [p=0.2] A fábrica lança {b}um pote semelhante, com o dobro de cada medida. [p=0.2] {c}Quanto cabe no pote novo? [p=0.3] E uma taça em forma de cone, de ponta para baixo, {d}guarda duzentos e setenta mililitros quando cheia. [p=0.2] {e}Com suco até um terço da altura, quanto suco tem?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] No pote, {a}cá é dois, e dois ao cubo dá oito. [p=0.2] {b}Duzentos e cinquenta vezes oito dá dois mil mililitros: [p=0.2] {c}dois litros."),
    dict(id="s18", block="resposta", text="Na taça, o suco é um cone com {a}cá igual a um terço. [p=0.2] {b}Um terço ao cubo dá um vinte e sete avos. [p=0.2] {c}Duzentos e setenta dividido por vinte e sete dá dez mililitros. [p=0.3] Um terço da altura, {d}e só dez mililitros de suco."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}medidas vezes cá, [p=0.2] {b}volume vezes cá ao cubo. [p=0.2] E {c}metade da altura do cone guarda um oitavo do volume."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica tudo deste módulo: [p=0.2] {b}sólidos compostos, a água que sobe com uma pedra, [p=0.2] {c}sólidos encaixados um no outro [p=0.2] e {d}volumes ampliados. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
