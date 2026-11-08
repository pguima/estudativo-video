# Estudativo · MAT-ANG-012 — Triângulos semelhantes: critérios e razão de semelhança (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: reconhecer a semelhança por dois ângulos iguais, montar a razão entre lados correspondentes na ordem certa e achar o lado que falta.
# Pré-requisitos: MAT-ANG-007 (congruência, "dois ângulos valem por três"), MAT-ANG-010 (proporção, cruz, fator). Próxima: MAT-ANG-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "pê", "quê", "érre".
# Figuras: E.triangulo, E.angulo (marcas de arco, sem graus no exemplo).
#   s05: triângulo 4-5-6 ampliado três vezes para 12-15-18.
#   s08-s12: pequeno com lados 4, 5 e 6; ângulo de um arco de frente para o 4, de dois arcos de frente para o 5, sem marca de frente para o 6 (6 embaixo).
#            grande girado, com o lado 12 embaixo, de frente para o ângulo de um arco, e x de frente para o de dois arcos (x = 15).
#   s13: tesoura abrindo (ângulo maior, pontas mais longe).
#   Questão: ABC com Â = 30°, B̂ = 90°, BC = 4, AC = 8; PQR com P̂ = 30°, Q̂ = 60°, QR = 6 (R̂ = 90°, PQ = 12). Medidas coerentes com o 30-60-90.

TITULO = "Triângulos semelhantes: critérios e razão de semelhança"

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
    dict(id="s01", block="gancho", text="{a}Você amplia uma foto no celular: [p=0.2] tudo fica maior, mas {b}nada entorta. [p=0.3] Com triângulos é igual. [p=0.2] E basta {c}conferir dois ângulos para saber que um é a ampliação do outro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece triângulos semelhantes, [p=0.2] {b}acha o lado que falta [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}congruência, quando os triângulos têm mesmo formato e mesmo tamanho, [p=0.2] e {c}proporção, como no Teorema de Tales. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="semelhanca", text="Triângulos {a}semelhantes têm o mesmo formato, [p=0.2] mas não precisam ter o mesmo tamanho. [p=0.3] Isso quer dizer {b}ângulos iguais [p=0.2] e {c}lados proporcionais: [p=0.2] todos multiplicados pelo mesmo número."),
    dict(id="s05", block="semelhanca", text="Esse número é {a}a razão de semelhança. [p=0.2] Um triângulo com lados de {b}quatro, de cinco e de seis centímetros, [p=0.2] ampliado três vezes, [p=0.2] fica com lados de {c}doze, de quinze e de dezoito. [p=0.3] {d}Razão de semelhança: três."),
    # critérios
    dict(id="s06", block="criterios", text="Para saber se dois triângulos são semelhantes, {a}basta conferir dois ângulos. [p=0.3] Se dois ângulos de um são iguais a dois ângulos do outro, [p=0.2] {b}o terceiro também é, pelo cento e oitenta. [p=0.2] É o atalho da congruência: {c}dois ângulos valem por três."),
    dict(id="s07", block="criterios", text="Também garantem semelhança {a}três lados na mesma razão, [p=0.2] ou {b}dois lados na mesma razão com o ângulo entre eles igual. [p=0.3] São {c}os casos da congruência, trocando lados iguais por lados proporcionais. [p=0.2] Mas o que mais aparece em prova é {d}o dos dois ângulos."),
    # ordem
    dict(id="s08", block="ordem", text="Para achar um lado, o mais importante é {a}a ordem. [p=0.2] Lado correspondente é {b}o lado de frente para o mesmo ângulo. [p=0.3] Na tela, o triângulo pequeno tem {c}lados de quatro, de cinco e de seis. [p=0.2] O grande tem os mesmos ângulos, mas está {d}girado."),
    dict(id="s09", block="ordem", text="No grande, o lado de {a}doze está de frente para o ângulo de um arco. [p=0.2] No pequeno, quem está de frente para esse ângulo é {b}o quatro. [p=0.3] E o xis está de frente para o ângulo de dois arcos, [p=0.2] como {c}o cinco no pequeno."),
    dict(id="s10", block="ordem", text="Monte as frações na mesma ordem, {a}grande sobre pequeno: [p=0.2] {b}doze está para quatro, assim como xis está para cinco. [p=0.3] Cruz: {c}quatro xis igual a doze vezes cinco, que dá sessenta. [p=0.2] {d}Xis igual a quinze. [p=0.3] A razão de semelhança é {e}doze dividido por quatro, que dá três."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}ligar os lados pela posição no desenho. [p=0.2] O doze está embaixo no grande, [p=0.2] e o seis está embaixo no pequeno. [p=0.3] Quem junta esses lados monta {b}doze está para seis, assim como xis está para cinco, [p=0.2] e acha {c}xis igual a dez."),
    dict(id="s12", block="erro", text="Mas o seis está de frente para {a}o ângulo sem marca, não para o de um arco. [p=0.3] Girou ou virou, {b}quem manda é o ângulo da frente, não a posição."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido: {a}maior com maior, menor com menor. [p=0.3] Num triângulo, {b}o maior lado fica de frente para o maior ângulo. [p=0.2] Pense numa tesoura: {c}quanto mais aberta, mais longe ficam as pontas."),
    dict(id="s14", block="atalho", text="Então, quando a questão dá {a}todos os lados, nem precisa dos ângulos. [p=0.2] Lados de {b}quatro, de cinco e de seis, [p=0.2] e lados de {c}quinze, de dezoito e de doze. [p=0.3] Coloque em ordem: {d}o doze vai com o quatro; o quinze, com o cinco; o dezoito, com o seis. [p=0.2] Tudo vezes três: {e}semelhantes."),
    dict(id="s15", block="atalho", text="Funciona porque ângulos iguais deixam {a}os lados na mesma fila, do menor ao maior. [p=0.3] Não compensa quando {b}falta um lado, e você não sabe onde ele entra na fila, [p=0.2] ou quando {c}há lados iguais. [p=0.2] Aí, {d}siga os ângulos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] No triângulo {a}á bê cê, o ângulo á mede trinta graus e o ângulo bê, noventa graus. [p=0.2] O lado bê cê mede quatro centímetros, e o lado á cê, oito."),
    dict(id="s17", block="questao", text="No triângulo {a}pê quê érre, o ângulo pê mede trinta graus e o ângulo quê, sessenta graus. [p=0.2] O lado quê érre mede seis centímetros. [p=0.3] {b}Os triângulos são semelhantes? [p=0.2] {c}Quanto mede o lado pê quê?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Em á bê cê, o ângulo cê é {a}cento e oitenta menos trinta menos noventa, que dá sessenta. [p=0.2] Em pê quê érre, o ângulo érre é {b}cento e oitenta menos trinta menos sessenta, que dá noventa. [p=0.3] Ambos têm trinta graus, sessenta graus e noventa graus: [p=0.2] {c}semelhantes, por dois ângulos."),
    dict(id="s20", block="resposta", text="Falta a ordem. [p=0.2] {a}Bê cê está de frente para o ângulo de trinta graus, no á. [p=0.2] Em pê quê érre, quem está de frente para os trinta graus é {b}quê érre, com seis. [p=0.3] {c}Á cê está de frente para o ângulo reto, no bê. [p=0.2] E {d}pê quê está de frente para o ângulo reto, no érre."),
    dict(id="s21", block="resposta", text="{a}Seis está para quatro, assim como xis está para oito. [p=0.2] Cruz: {b}quatro xis igual a seis vezes oito, que dá quarenta e oito. [p=0.2] {c}Xis igual a doze centímetros. [p=0.3] Ou pelo fator: {d}no pequeno, oito é o dobro de quatro, [p=0.2] então pê quê é o dobro de seis: {e}doze."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}dois ângulos iguais garantem a semelhança, [p=0.2] e {b}lado correspondente é o que fica de frente para o mesmo ângulo."),
    dict(id="s23", block="fim", text="Na próxima aula, a semelhança sai do papel: [p=0.2] você vai achar {a}a altura de um prédio pela sombra, [p=0.2] e separar {b}triângulos encaixados um dentro do outro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
