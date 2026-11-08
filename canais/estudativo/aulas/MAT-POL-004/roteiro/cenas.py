# Estudativo · MAT-POL-004 — Circunferência: raio, diâmetro e comprimento (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: usar C = 2πr para dizer que uma roda de raio 30 cm percorre 180 m em 100 voltas, com π = 3.
# Pré-requisitos: MAT-EQU-011 (isolar uma letra), MAT-RAZ-001 (razão), MAT-MED-001 (escada do metro). Próxima: MAT-POL-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Circunferência: raio, diâmetro e comprimento"

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
    dict(id="s01", block="gancho", text="{a}Uma roda de bicicleta dá cem voltas. [p=0.3] Quanto a bicicleta andou? [p=0.3] Sabendo só {b}o tamanho da roda, dá para responder. [p=0.2] E a conta usa {c}um dos números mais famosos da matemática."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede a volta de qualquer circunferência [p=0.2] e leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}razão é a comparação de dois números pela divisão, [p=0.2] {c}isolar uma letra numa fórmula, fazendo o mesmo nos dois lados, [p=0.2] e {d}converter comprimento na escada do metro. [p=0.3] Se faltar alguma, procure no canal."),
    # circunferência
    dict(id="s04", block="circ", text="Pegue {a}um barbante e prenda uma ponta com o dedo. [p=0.2] Amarre um lápis na outra ponta e {b}gire. [p=0.3] A linha que o lápis desenha é {c}uma circunferência. [p=0.2] Todos os pontos dela ficam {d}à mesma distância do ponto fixo, o centro."),
    dict(id="s05", block="circ", text="{a}A circunferência é só a linha, a borda. [p=0.2] {b}A região de dentro, pintada, se chama círculo. [p=0.3] É como {c}o pneu e a roda inteira."),
    # raio e diâmetro
    dict(id="s06", block="raio", text="{a}Raio é o segmento do centro até a circunferência: [p=0.2] é o barbante. [p=0.3] {b}Diâmetro é o segmento que atravessa de um lado ao outro, passando pelo centro. [p=0.2] Ele é feito de {c}um raio para cada lado: [p=0.2] {d}o diâmetro vale o dobro do raio."),
    # pi
    dict(id="s07", block="pi", text="Agora o comprimento: {a}quanto mede a volta inteira. [p=0.3] Enrole um barbante em volta de {b}uma lata e meça. [p=0.2] Depois, {c}meça o diâmetro da lata. [p=0.3] Divida a volta pelo diâmetro: [p=0.2] dá {d}pouco mais que três."),
    dict(id="s08", block="pi", text="Com uma lata, um prato ou uma roda gigante, {a}a razão entre a volta e o diâmetro é sempre a mesma. [p=0.3] Esse número se chama {b}pi, uma letra grega. [p=0.2] Ele vale {c}três vírgula catorze e mais casas que nunca acabam. [p=0.3] A prova costuma dizer qual valor usar: [p=0.2] {d}três ou três vírgula catorze."),
    # fórmula
    dict(id="s09", block="formula", text="Se a volta dividida pelo diâmetro dá pi, [p=0.2] isolando a volta, {a}ela é pi vezes o diâmetro. [p=0.3] Como o diâmetro é o dobro do raio, [p=0.2] fica {b}cê igual a dois pi érre. [p=0.3] {c}Cê é o comprimento da circunferência, [p=0.2] {d}érre é o raio, [p=0.2] e {e}o dois vem do diâmetro."),
    dict(id="s10", block="formula", text="Numa circunferência de {a}raio seis, a volta mede {b}duas vezes pi vezes seis, que dá doze pi. [p=0.3] Muitas provas deixam {c}o pi na resposta, como se fosse uma letra. [p=0.2] Com pi igual a três, {d}doze vezes três dá trinta e seis."),
    # roda
    dict(id="s11", block="roda", text="Voltando à bicicleta: {a}roda de raio trinta centímetros, com pi igual a três. [p=0.3] {b}Duas vezes três vezes trinta dá cento e oitenta centímetros. [p=0.3] É {c}o quanto a bicicleta anda em uma volta da roda: [p=0.2] a borda inteira encosta no chão uma vez."),
    dict(id="s12", block="roda", text="Em cem voltas: {a}cento e oitenta vezes cem dá dezoito mil centímetros. [p=0.3] Na escada do metro, de centímetro para metro {b}são dois degraus para cima: dividido por cem. [p=0.2] {c}Dezoito mil dividido por cem dá cento e oitenta metros."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}usar o diâmetro no lugar do raio. [p=0.3] Uma roda tem {b}sessenta centímetros de diâmetro. [p=0.2] Quem põe sessenta no lugar do érre faz {c}duas vezes três vezes sessenta, e acha trezentos e sessenta centímetros. [p=0.3] {d}O dobro do certo. [p=0.2] O raio é a metade: {e}sessenta dividido por dois dá trinta, e a volta mede cento e oitenta."),
    # atalho
    dict(id="s14", block="atalho", text="E o atalho prometido: [p=0.2] com pi igual a três, {a}a volta é o triplo do diâmetro. [p=0.3] Roda de raio trinta: {b}o diâmetro é duas vezes trinta, que dá sessenta. [p=0.2] {c}Sessenta vezes três dá cento e oitenta. [p=0.2] Uma conta só."),
    dict(id="s15", block="atalho", text="Funciona porque {a}dois pi érre é o mesmo que pi vezes o diâmetro. [p=0.3] {b}Não compensa quando a prova pede pi igual a três vírgula catorze: [p=0.2] aí, o triplo serve só para {c}conferir se a resposta está perto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma pista de corrida em forma de circunferência tem {a}seiscentos metros de volta. [p=0.3] {b}Usando pi igual a três, quanto mede o raio da pista?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Desta vez, a volta é conhecida, e o raio é o que falta. [p=0.2] {a}Seiscentos igual a duas vezes três vezes érre. [p=0.2] {b}Seiscentos igual a seis érre. [p=0.2] {c}Divida cada lado por seis: [p=0.2] {d}érre igual a cem metros."),
    dict(id="s19", block="resposta", text="Pelo atalho: {a}a volta é o triplo do diâmetro, [p=0.2] então {b}o diâmetro é seiscentos dividido por três, que dá duzentos metros. [p=0.2] {c}O raio é a metade: duzentos dividido por dois dá cem metros. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o diâmetro vale dois raios, [p=0.2] {b}a volta vale pi vezes o diâmetro, [p=0.2] e {c}cê é igual a dois pi érre."),
    dict(id="s21", block="fim", text="Na próxima aula, você mede {a}só um pedaço da volta: um arco. [p=0.2] E vai usar {b}a regra de três. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
