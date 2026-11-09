# Estudativo · FIS-ENE-008 — Conservação da quantidade de movimento (Física · Energia e Colisões · Impulso e colisões).
# Habilidade: usar Q antes = Q depois em recuos, explosões e empurrões, respeitando o sinal do sentido.
# Pré-requisitos: FIS-ENE-007 (Q e I = ΔQ), MAT-EQU-008 (equação de 1º grau). Próxima: FIS-ENE-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Terceira lei (FIS-DIN-003), peso e normal NÃO estão em "Já ensinado": a terceira lei é citada como assunto de outra aula,
#   e "isolado" é explicado como "nada de fora empurra para os lados", como no gelo.
# Contas: pai/filho 40·2 + 80·v = 0 → v = −1 m/s; espingarda 0,01·400 = 4 → 4·v = −4 → v = −1 m/s; explosão 3·10 = 30,
#   2·20 + 1·v = 30 → v = −10 m/s (erro: 40 + v = 0 → −40); atalho 4/0,01 = 400, 400/400 = 1; questão 3·6 = 18, 90·v = −18 →
#   v = −0,2 m/s; 90/3 = 30, 6/30 = 0,2.

TITULO = "Conservação da quantidade de movimento"

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
    dict(id="s01", block="gancho", text="{a}Ao disparar, a espingarda dá um tranco para trás no ombro: o coice. [p=0.2] {b}Durante o disparo, nada de fora empurra a espingarda para trás. [p=0.3] {c}Então, de onde vem esse movimento?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai igualar a quantidade de movimento de antes com a de depois [p=0.2] em {b}empurrões, {c}recuos e {d}explosões, [p=0.2] sem errar o sinal."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}quantidade de movimento, massa vezes velocidade; [p=0.2] {c}o impulso, que é a variação dela; [p=0.2] e {d}resolver uma equação de primeiro grau. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="{a}Dois patinadores, parados no gelo, se empurram. [p=0.2] {b}Um empurra o outro, [p=0.1] e {c}o outro empurra de volta, com a mesma força e no sentido oposto. [p=0.3] {d}Isso é a terceira lei de Newton, que tem aula própria."),
    dict(id="s05", block="ideia", text="{a}As duas forças agem durante o mesmo tempo. [p=0.2] {b}Então os impulsos têm o mesmo valor e sentidos opostos. [p=0.3] {c}O que um ganha de quantidade de movimento para um lado, o outro ganha para o outro lado. [p=0.2] {d}A soma não muda."),
    dict(id="s06", block="ideia", text="Essa é a conservação da quantidade de movimento: [p=0.2] {a}num sistema isolado, a quantidade de movimento total antes é igual à de depois. [p=0.3] {b}Isolado quer dizer que nada de fora empurra para os lados, [p=0.2] como no gelo."),
    dict(id="s07", block="ideia", text="Como a quantidade de movimento tem sentido, {a}escolha um sentido positivo, [p=0.2] por exemplo, {b}para a direita. [p=0.2] {c}Quem vai para a esquerda entra com sinal de menos."),
    # empurrão
    dict(id="s08", block="empurrao", text="Vamos às contas. [p=0.2] {a}Um pai de oitenta quilogramas e um filho de quarenta estão parados no gelo. [p=0.2] Eles se empurram, e {b}o filho sai a dois metros por segundo para a direita. [p=0.3] {c}Antes, tudo parado: quantidade de movimento zero."),
    dict(id="s09", block="empurrao", text="{a}Depois: quarenta vezes dois, oitenta, mais oitenta vezes vê, igual a zero. [p=0.2] {b}Oitenta vê igual a menos oitenta. [p=0.2] {c}Vê igual a menos um. [p=0.3] {d}O pai sai a um metro por segundo, para a esquerda."),
    # recuo
    dict(id="s10", block="recuo", text="{a}O coice é a mesma conta: [p=0.2] a pólvora empurra a bala para a frente e a espingarda para trás. [p=0.3] Uma espingarda de {b}quatro quilogramas dispara uma bala de {c}dez gramas, a quatrocentos metros por segundo. [p=0.3] {d}Dez gramas são zero vírgula zero um quilograma. [p=0.2] {e}A bala leva quatro de quantidade de movimento, para a frente."),
    dict(id="s11", block="recuo", text="{a}Então a espingarda leva quatro para trás: [p=0.2] {b}quatro vezes vê igual a menos quatro, [p=0.1] {c}vê igual a menos um metro por segundo. [p=0.3] {d}A bala tem pouca massa e sai rápida; a espingarda tem muita massa e recua devagar."),
    # explosão
    dict(id="s12", block="explosao", text="Por último, uma explosão em movimento. [p=0.2] {a}Um corpo de três quilogramas anda a dez metros por segundo, para a direita, [p=0.2] e {b}se parte em dois pedaços: um de dois quilogramas e outro de um. [p=0.2] {c}O de dois quilogramas sai a vinte metros por segundo, para a direita. [p=0.3] {d}E o outro?"),
    dict(id="s13", block="explosao", text="{a}Antes: três vezes dez, trinta. [p=0.2] {b}Depois: dois vezes vinte, quarenta, mais um vezes vê. [p=0.2] {c}Quarenta mais vê igual a trinta. [p=0.2] {d}Vê igual a menos dez: [p=0.1] {e}o pedaço menor vai a dez metros por segundo, para a esquerda."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a explosão sempre começa do zero. [p=0.2] A pessoa escreve {b}quarenta mais vê igual a zero [p=0.1] e acha {c}quarenta metros por segundo, para a esquerda."),
    dict(id="s15", block="erro", text="Mas o corpo {a}já andava antes de explodir. [p=0.2] {b}A quantidade de movimento antes era trinta, e é ela que se mantém. [p=0.3] {c}Zero, só quando tudo começa parado."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho de prova: [p=0.2] quando tudo começa parado, {a}as velocidades ficam na razão inversa das massas. [p=0.3] {b}Pai com o dobro da massa do filho: metade da velocidade. [p=0.2] {c}Espingarda com massa quatrocentas vezes maior que a da bala: [p=0.2] velocidade quatrocentas vezes menor, [p=0.1] quatrocentos dividido por quatrocentos, um."),
    dict(id="s17", block="atalho", text="Funciona porque {a}massa vezes velocidade dá o mesmo valor para os dois lados. [p=0.3] {b}Não compensa quando o sistema já anda antes, como na explosão em movimento: [p=0.2] aí, monte a equação com os sinais."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um astronauta de {a}noventa quilogramas, parado no espaço, [p=0.2] arremessa {b}uma ferramenta de três quilogramas a seis metros por segundo. [p=0.3] {c}Com que velocidade, e para que lado, o astronauta se move?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Antes, tudo parado: zero. [p=0.2] {b}Depois: três vezes seis, dezoito, mais noventa vezes vê, igual a zero. [p=0.2] {c}Noventa vê igual a menos dezoito. [p=0.2] {d}Vê igual a menos zero vírgula dois."),
    dict(id="s21", block="resposta", text="{a}Ele vai a zero vírgula dois metros por segundo, para o lado oposto ao da ferramenta. [p=0.3] {b}Pelo atalho: noventa é trinta vezes três, [p=0.2] então {c}seis dividido por trinta, zero vírgula dois."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}sem nada de fora empurrando, a quantidade de movimento total não muda; [p=0.2] {b}escolha um sentido positivo e respeite o sinal; [p=0.2] e {c}começando parado, as velocidades vão na razão inversa das massas."),
    dict(id="s23", block="fim", text="Na próxima aula, os corpos {a}batem: [p=0.2] você vai classificar {b}as colisões [p=0.2] e achar as velocidades depois da batida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
