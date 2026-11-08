# Estudativo · MAT-ANG-005 — Classificar triângulos por lados e ângulos (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: classificar um triângulo como equilátero, isósceles ou escaleno e como acutângulo, retângulo ou obtusângulo e achar os ângulos da base de um isósceles com topo de 40° (70° cada).
# Pré-requisitos: MAT-ANG-004 (soma 180°), MAT-ANG-001 (agudo, reto, obtuso). Próxima: MAT-ANG-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: E.triangulo com E.marcas_iguais (equilátero, isósceles, escaleno); isósceles com "base" e "topo" rotulados; três triângulos por ângulo.
# Na questão, não dar medidas de lados: com topo de 36° os lados não podem ser números quaisquer.

TITULO = "Classificar triângulos por lados e ângulos"

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
    dict(id="s01", block="gancho", text="{a}Um triângulo tem dois lados iguais, [p=0.2] e um ângulo da base mede {b}quarenta graus. [p=0.3] Muita gente responde que os outros ângulos medem {c}setenta e setenta. [p=0.3] {d}Errado. [p=0.2] E o motivo está num detalhe do desenho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você classifica qualquer triângulo pelos lados e pelos ângulos, [p=0.2] {b}acha os ângulos de um triângulo com dois lados iguais [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os ângulos de dentro de um triângulo somam cento e oitenta graus, [p=0.2] e {c}agudo é menor que noventa; obtuso, maior. [p=0.3] Se faltar alguma, procure no canal."),
    # pelos lados
    dict(id="s04", block="lados", text="Primeiro, pelos lados. [p=0.2] Na figura, {a}tracinhos iguais marcam lados iguais."),
    dict(id="s05", block="lados", text="{a}Três lados iguais: equilátero. [p=0.2] Equi quer dizer igual: lados iguais. [p=0.3] {b}Dois lados iguais: isósceles. [p=0.3] {c}Todos os lados diferentes: escaleno. [p=0.3] Sem tracinhos, olhe as medidas. [p=0.2] Lados de {d}cinco centímetros, cinco centímetros e oito centímetros: [p=0.2] isósceles. [p=0.2] Lados de {e}quatro, de cinco e de seis centímetros: [p=0.2] escaleno."),
    # isósceles
    dict(id="s06", block="isosceles", text="O isósceles tem um detalhe que cai muito. [p=0.2] O lado diferente se chama {a}base. [p=0.2] O ângulo entre os lados iguais é {b}o topo. [p=0.3] E {c}os ângulos da base são iguais entre si."),
    dict(id="s07", block="isosceles", text="Exemplo: {a}isósceles com topo de quarenta graus. [p=0.2] {b}Cento e oitenta menos quarenta dá cento e quarenta. [p=0.2] Esse resto se divide igualmente entre os ângulos da base: [p=0.2] {c}cento e quarenta dividido por dois dá setenta graus cada."),
    dict(id="s08", block="isosceles", text="No equilátero, {a}os três ângulos também são iguais: [p=0.2] {b}cento e oitenta dividido por três dá sessenta graus cada."),
    # pelos ângulos
    dict(id="s09", block="angulos", text="Agora, pelos ângulos. [p=0.2] {a}Três ângulos agudos: acutângulo. [p=0.2] {b}Um ângulo reto: retângulo. [p=0.2] {c}Um ângulo obtuso: obtusângulo."),
    dict(id="s10", block="angulos", text="Repare que {a}num triângulo não cabem dois ângulos retos. [p=0.2] Eles já gastariam os cento e oitenta, [p=0.2] e não sobraria nada para o terceiro ângulo. [p=0.3] Com obtuso, é pior ainda. [p=0.2] Então {b}todo triângulo tem pelo menos dois ângulos agudos."),
    dict(id="s11", block="angulos", text="Todo triângulo ganha {a}um nome pelos lados e outro pelos ângulos. [p=0.2] O de topo quarenta, com setenta e setenta na base, é {b}isósceles e acutângulo. [p=0.3] Um com {c}dois lados iguais e ângulos de quarenta e cinco graus, quarenta e cinco graus e noventa graus [p=0.2] é {d}isósceles e retângulo."),
    # erro
    dict(id="s12", block="erro", text="Voltando ao erro do começo. [p=0.2] Ali, os quarenta graus eram {a}de um ângulo da base, não do topo. [p=0.3] Quem não percebe faz {b}cento e oitenta menos quarenta, dividido por dois, [p=0.2] e acha {c}setenta e setenta."),
    dict(id="s13", block="erro", text="Mas os ângulos da base são iguais. [p=0.2] Se um tem quarenta, {a}o outro também tem quarenta. [p=0.2] O topo: {b}cento e oitenta menos quarenta menos quarenta dá cem graus. [p=0.3] O triângulo tem {c}quarenta graus, quarenta graus e cem graus: [p=0.2] é {d}obtusângulo, não acutângulo."),
    dict(id="s14", block="erro", text="Antes de calcular, pergunte: {a}esse ângulo é o do topo ou o da base?"),
    # atalho
    dict(id="s15", block="atalho", text="E o atalho prometido, para classificar pelos ângulos: [p=0.2] {a}olhe só o maior. [p=0.3] {b}Menor que noventa, acutângulo. [p=0.2] {c}Igual a noventa, retângulo. [p=0.2] {d}Maior que noventa, obtusângulo."),
    dict(id="s16", block="atalho", text="Funciona porque {a}os outros ângulos são sempre agudos: [p=0.2] quem decide é o maior. [p=0.3] {b}Não serve se falta um ângulo: [p=0.2] calcule o terceiro primeiro, [p=0.2] porque {c}ele pode ser justamente o maior."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um triângulo tem {a}dois lados iguais, [p=0.2] e o ângulo entre esses lados mede {b}trinta e seis graus. [p=0.3] {c}Quanto mede cada ângulo da base? [p=0.2] {d}E como ele se classifica, pelos lados e pelos ângulos?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O ângulo entre os lados iguais é {a}o topo. [p=0.2] {b}Cento e oitenta menos trinta e seis dá cento e quarenta e quatro. [p=0.2] {c}Cento e quarenta e quatro dividido por dois dá setenta e dois graus cada."),
    dict(id="s20", block="resposta", text="Pelos lados, {a}isósceles. [p=0.2] Pelos ângulos, o maior é setenta e dois, menor que noventa: [p=0.2] {b}acutângulo. [p=0.3] Conferindo: {c}trinta e seis mais setenta e dois mais setenta e dois dá cento e oitenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}pelos lados, conte os lados iguais. [p=0.2] {b}Pelos ângulos, olhe o maior. [p=0.2] E {c}no isósceles, os ângulos da base são iguais."),
    dict(id="s22", block="fim", text="Na próxima aula, uma pergunta que vem antes de tudo: [p=0.2] {a}três medidas quaisquer sempre formam um triângulo? [p=0.2] A resposta é {b}não, e você aprende a testar. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
