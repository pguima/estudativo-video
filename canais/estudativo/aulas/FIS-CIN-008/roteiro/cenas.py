# Estudativo · FIS-CIN-008 — Posição no MUV: a função do 2º grau (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: usar s = s0 + v0·t + a·t²/2 para achar posição ou tempo e o atalho da velocidade média (v0 + v)/2 para achar o deslocamento.
# Pré-requisitos: FIS-CIN-007 (v = v0 + at), MAT-POT-002 (potências), MAT-FUN-016 (parábola), MAT-FAT-008 (Bhaskara). Próxima: FIS-CIN-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "sorvetão" é o apelido de sala de aula da função. O delta da Bhaskara é avisado como outro delta.

TITULO = "Posição no MUV: a função do 2º grau"

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
    dict(id="s01", block="gancho", text="{a}Um carro parte do repouso e acelera {b}dois metros por segundo ao quadrado. [p=0.3] Depois de um segundo, ele está a {c}um metro da largada. [p=0.1] Depois de dois, a {d}quatro. [p=0.1] Três, {e}nove. [p=0.1] Quatro, {f}dezesseis. [p=0.3] São {g}os quadrados perfeitos. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a posição e o tempo no movimento com aceleração, [p=0.2] e levar {b}um atalho que dispensa o tê ao quadrado."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}vê igual a vê zero mais á tê; [p=0.2] {c}potência, como quatro ao quadrado; [p=0.2] e {d}a fórmula de Bhaskara, da equação do segundo grau. [p=0.3] Se faltar alguma, procure no canal."),
    # velocidade média
    dict(id="s04", block="media", text="Por que não dá para usar {a}esse igual a esse zero mais vê tê? [p=0.2] Porque {b}aqui a velocidade muda o tempo todo. [p=0.3] Qual vê você usaria? [p=0.2] {c}A do começo é pouca; [p=0.1] {d}a do fim é demais."),
    dict(id="s05", block="media", text="A saída é a {a}velocidade média. [p=0.2] No eme u vê, a velocidade muda por igual, [p=0.2] então a média é {b}o valor do meio: [p=0.2] {c}vê zero mais vê, dividido por dois. [p=0.3] E o deslocamento é {d}essa média vezes o tempo."),
    dict(id="s06", block="media", text="Um carro vai de {a}dez a trinta metros por segundo em {b}quatro segundos. [p=0.3] {c}Média: dez mais trinta, quarenta, dividido por dois, vinte. [p=0.2] {d}Vinte vezes quatro: oitenta metros."),
    # função
    dict(id="s07", block="funcao", text="Se você trocar o vê por {a}vê zero mais á tê e fizer as contas, [p=0.2] chega na função da posição do eme u vê: [p=0.3] {b}esse igual a esse zero, mais vê zero tê, mais á tê ao quadrado, dividido por dois."),
    dict(id="s08", block="funcao", text="{a}Esse zero é a posição inicial. [p=0.2] {b}Vê zero tê é o que o corpo andaria sem acelerar. [p=0.2] {c}Á tê ao quadrado dividido por dois é o que a aceleração acrescenta. [p=0.3] {d}Tê ao quadrado, porque o tempo pesa duas vezes: [p=0.2] mais tempo andando, e mais velocidade ganha nesse tempo. [p=0.3] Os professores chamam de {e}sorvetão."),
    dict(id="s09", block="funcao", text="Volte ao gancho. [p=0.2] {a}Partiu da posição zero, do repouso, com á igual a dois. [p=0.2] Sobra só {b}dois tê ao quadrado dividido por dois: [p=0.1] {c}esse igual a tê ao quadrado. [p=0.3] {d}Por isso os quadrados perfeitos."),
    dict(id="s10", block="funcao", text="Um ciclista está a {a}dez metros por segundo e acelera {b}dois metros por segundo ao quadrado. [p=0.3] Onde ele está depois de {c}quatro segundos, partindo da posição zero? [p=0.3] {d}Dez vezes quatro, quarenta. [p=0.2] {e}Dois vezes dezesseis, trinta e dois, dividido por dois, dezesseis. [p=0.2] {f}Quarenta mais dezesseis: cinquenta e seis metros."),
    # tempo
    dict(id="s11", block="tempo", text="E para achar o tempo? [p=0.2] Aí aparece {a}uma equação do segundo grau. [p=0.3] Um carro parte da posição zero a {b}cinco metros por segundo, com aceleração de {c}dois metros por segundo ao quadrado. [p=0.2] Quando ele chega aos {d}cinquenta metros? [p=0.3] {e}Cinquenta igual a cinco tê mais tê ao quadrado."),
    dict(id="s12", block="tempo", text="{a}Passe tudo para um lado: tê ao quadrado mais cinco tê menos cinquenta igual a zero. [p=0.3] {b}Bhaskara. [p=0.1] Cuidado: o delta da Bhaskara é outro, não é a variação. [p=0.2] {c}Aqui, ele dá vinte e cinco mais duzentos, duzentos e vinte e cinco, [p=0.1] e a raiz é quinze. [p=0.2] {d}Menos cinco mais quinze, dividido por dois: cinco segundos. [p=0.3] {e}A outra raiz dá menos dez: [p=0.1] {f}tempo negativo não serve."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}esquecer o dividido por dois. [p=0.3] No ciclista, {b}dois vezes dezesseis dá trinta e dois, [p=0.2] e a pessoa soma {c}quarenta mais trinta e dois: setenta e dois metros. [p=0.3] {d}A conta certa dá cinquenta e seis. [p=0.2] Sem o dividido por dois, a aceleração conta em dobro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}se você tem a velocidade do começo e a do fim, [p=0.2] {b}use a média: vê zero mais vê, dividido por dois, vezes o tempo. [p=0.3] No ciclista: {c}de dez, ele chega a dezoito em quatro segundos. [p=0.2] {d}Média, catorze. [p=0.1] {e}Catorze vezes quatro: os mesmos cinquenta e seis, sem tê ao quadrado."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a velocidade muda por igual: [p=0.2] o que falta no começo sobra no fim. [p=0.3] {b}Só vale com aceleração constante, no eme u vê. [p=0.2] {c}E não compensa quando a velocidade final não aparece: [p=0.2] aí, o sorvetão vai direto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um carro está a {a}doze metros por segundo e acelera {b}dois metros por segundo ao quadrado durante {c}cinco segundos. [p=0.3] {d}Quanto ele anda nesse tempo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Pelo sorvetão: {a}doze vezes cinco, sessenta. [p=0.2] {b}Dois vezes vinte e cinco, cinquenta, dividido por dois, vinte e cinco. [p=0.2] {c}Sessenta mais vinte e cinco: oitenta e cinco metros."),
    dict(id="s19", block="resposta", text="Confira pelo atalho. [p=0.2] {a}Velocidade final: doze mais dois vezes cinco, vinte e dois. [p=0.2] {b}Média: doze mais vinte e dois, trinta e quatro, dividido por dois, dezessete. [p=0.2] {c}Dezessete vezes cinco: oitenta e cinco. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no eme u vê, a posição tem tê ao quadrado, com o á dividido por dois; [p=0.2] {b}com as duas velocidades, use a média."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai achar {a}a distância de frenagem de um carro sem saber o tempo, [p=0.2] e ver por que {b}o dobro da velocidade dá quatro vezes essa distância. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
