# Estudativo · MAT-ARE-001 — Perímetro: o contorno de uma figura (Matemática · Áreas e Perímetros).
# Habilidade: calcular quantos metros de cerca contornam um terreno de 20 m por 35 m (110 m), convertendo unidades quando preciso.
# Pré-requisitos: MAT-MED-001 (escada do metro), MAT-POL-001 (lados opostos iguais no retângulo e no paralelogramo). Próxima: MAT-ARE-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Área fica para MAT-ARE-002. Soma de decimais (MAT-FRA-015) fora da cadeia:
# as conversões levam tudo a números inteiros antes de somar.
# Visual:
#   s01, s07-s08, s13-s14: E.retangulo 35 × 20 (terreno) com as cotas só em dois lados; depois as quatro cotas; a volta traçada na cor da matéria.
#   s04: um ponto percorre a borda de uma figura e volta ao início.
#   s06: E.triangulo de lados 5, 7 e 8 cm (E.segmento com medida).
#   s09: E.quadrado de lado 3 m.
#   s10-s12: mesa 1,2 m × 80 cm; a cota de 1,2 m vira 120 cm (escada de dois degraus).
#   s16-s19: horta 6 m × 250 cm com um trecho de 2 m tracejado (portão).

TITULO = "Perímetro: o contorno de uma figura"

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
    dict(id="s01", block="gancho", text="{a}Um terreno de vinte metros por trinta e cinco metros. [p=0.3] Quantos metros de cerca para fechar tudo? [p=0.3] Se você respondeu {b}cinquenta e cinco, [p=0.2] a sua cerca {c}parou no meio do caminho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o contorno de qualquer figura, [p=0.2] mesmo com medidas em unidades diferentes, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a escada do metro, em que cada degrau é uma casa da vírgula, [p=0.2] e {c}no retângulo, os lados opostos são iguais. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="conceito", text="{a}Perímetro é a medida do contorno de uma figura. [p=0.2] É o caminho de quem {b}anda pela borda, [p=0.2] dá a volta inteira [p=0.1] e {c}chega de novo ao ponto de partida."),
    dict(id="s05", block="conceito", text="O nome já explica: {a}peri quer dizer em volta, [p=0.2] e {b}metro quer dizer medida. [p=0.3] É o perímetro que diz quanto comprar de {c}cerca para um terreno, [p=0.1] {d}rodapé para uma sala [p=0.1] ou {e}fita para a borda de uma mesa."),
    dict(id="s06", block="conceito", text="Numa figura de lados retos, [p=0.2] a regra é uma só: {a}some todos os lados. [p=0.3] Um triângulo com lados de {b}cinco, de sete e de oito centímetros: [p=0.2] {c}cinco mais sete mais oito dá vinte centímetros."),
    # retângulo
    dict(id="s07", block="retangulo", text="Voltando ao terreno. [p=0.2] No desenho aparecem {a}só duas medidas: vinte e trinta e cinco. [p=0.3] Mas o retângulo tem {b}quatro lados, [p=0.2] e os opostos são iguais: [p=0.2] {c}um par de lados de vinte [p=0.2] e um par de lados de trinta e cinco."),
    dict(id="s08", block="retangulo", text="{a}Vinte mais trinta e cinco dá cinquenta e cinco. [p=0.2] Isso é {b}meia volta. [p=0.3] {c}Mais cinquenta e cinco dá cento e dez. [p=0.2] São {d}cento e dez metros de cerca."),
    dict(id="s09", block="retangulo", text="No quadrado, {a}os quatro lados são iguais. [p=0.2] Um canteiro quadrado de {b}três metros de lado: [p=0.2] {c}três vezes quatro dá doze metros de contorno. [p=0.3] No triângulo equilátero, com três lados iguais, {d}é o lado vezes três."),
    # unidades
    dict(id="s10", block="unidades", text="E se as medidas vierem em {a}unidades diferentes? [p=0.2] Uma mesa tem {b}um vírgula dois metro de comprimento [p=0.2] e {c}oitenta centímetros de largura. [p=0.3] Antes de somar, {d}tudo na mesma unidade."),
    dict(id="s11", block="unidades", text="Do metro ao centímetro, {a}dois degraus para baixo: duas casas para a direita. [p=0.2] {b}Um vírgula dois metro vira cento e vinte centímetros. [p=0.3] {c}Cento e vinte mais oitenta dá duzentos. [p=0.2] {d}O dobro dá quatrocentos centímetros, a volta inteira."),
    dict(id="s12", block="unidades", text="Para voltar ao metro, {a}dois degraus para cima, duas casas para a esquerda, [p=0.2] e {b}quatrocentos centímetros dão quatro metros de fita para contornar a mesa."),
    # erro
    dict(id="s13", block="erro", text="O erro do começo é o mais comum: {a}somar só as medidas que aparecem no desenho. [p=0.2] Vinte mais trinta e cinco dá {b}cinquenta e cinco, [p=0.2] e a cerca {c}cobre só dois lados do terreno. [p=0.3] Antes de somar, {d}conte os lados da figura: [p=0.2] quatro lados, quatro parcelas. [p=0.3] E desconfie de cerca que {e}não volta ao ponto de partida."),
    # atalho
    dict(id="s14", block="atalho", text="{a}Esse é o atalho do retângulo, que você já usou no terreno e na mesa: [p=0.2] {b}some comprimento e largura e dobre. [p=0.3] {c}Duas contas, em vez de somar os quatro lados um por um."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada lado tem um gêmeo do outro lado da figura. [p=0.3] Também vale para {b}o paralelogramo, que tem lados opostos iguais. [p=0.3] {c}Não serve quando os lados opostos não são iguais, [p=0.2] como no trapézio: [p=0.2] aí, {d}some um por um."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma horta retangular mede {a}seis metros por duzentos e cinquenta centímetros. [p=0.3] Ela vai ser cercada com tela, [p=0.1] {b}menos num portão de dois metros, que fica sem tela. [p=0.3] {c}Quantos metros de tela são necessários?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Primeiro, {a}a mesma unidade: [p=0.2] seis metros são {b}seiscentos centímetros. [p=0.3] Pelo atalho, {c}seiscentos mais duzentos e cinquenta dá oitocentos e cinquenta. [p=0.2] {d}O dobro dá mil e setecentos centímetros."),
    dict(id="s19", block="resposta", text="Dois degraus para cima, e {a}mil e setecentos centímetros dão dezessete metros de contorno. [p=0.3] Mas o portão fica sem tela: [p=0.2] {b}dezessete menos dois dá quinze metros de tela. [p=0.3] Quem esquece o portão {c}compra tela a mais."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}perímetro é a volta inteira. [p=0.2] {b}Some todos os lados, [p=0.2] {c}com as medidas na mesma unidade."),
    dict(id="s21", block="fim", text="Na próxima aula, você mede {a}o que fica dentro do contorno: a área. [p=0.2] Vai contar quadradinhos, usar {b}base vezes altura [p=0.2] e descobrir {c}quantos pisos cobrem o chão de um quarto. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
