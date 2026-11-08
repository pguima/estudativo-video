# Estudativo · MAT-TOP-014 — Bases de contagem: binária e sexagesimal (Matemática · Tópicos Avançados · Bases de contagem).
# Habilidade: converter 1011 da base 2 para 11 na base 10, escrever 13 como 1101 e explicar por que 90 minutos são 1 h 30 min.
# Pré-requisitos: MAT-MED-006 (hora tem 60 minutos), MAT-NUM-009 (dividir com resto), MAT-POT-001 (potência). Próxima: MAT-TOP-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Algarismos da base dois lidos um a um ("um, zero, um, um"), nunca "mil e onze".
# Fato: a contagem de 60 em 60 vem da antiga Mesopotâmia (sumérios e babilônios), sem data no texto.
# Contas: 1011₂ = 8 + 2 + 1 = 11. 13 ÷ 2 = 6 r1; 6 ÷ 2 = 3 r0; 3 ÷ 2 = 1 r1; 1 ÷ 2 = 0 r1 → 1101 = 8 + 4 + 1 = 13.
#   90 ÷ 60 = 1 r30. Questão: 10110₂ = 16 + 4 + 2 = 22; 25 = 16 + 8 + 1 = 11001₂; 150 ÷ 60 = 2 r30.

TITULO = "Bases de contagem: binária e sexagesimal"

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
    dict(id="s01", block="gancho", text="{a}Um, zero, um, um. [p=0.2] Parece mil e onze. [p=0.3] Mas, para um computador, {b}isso é onze. [p=0.3] E é a mesma ideia que faz {c}noventa minutos virarem uma hora e trinta minutos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você passa números da base dez para a base dois e de volta, [p=0.2] entende a base sessenta do relógio [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}no nosso jeito de escrever números, cada casa vale dez vezes a da direita: unidade, dezena, centena; [p=0.2] {c}dividir com resto; [p=0.2] e {d}potência: dois elevado a três é dois vezes dois vezes dois, oito. [p=0.3] Se faltar alguma, procure no canal."),
    # base dez
    dict(id="s04", block="base10", text="Por que a dezena vale dez? [p=0.2] Porque a gente {a}conta em grupos de dez. [p=0.2] Juntou dez unidades, {b}vira uma dezena. [p=0.2] Juntou dez dezenas, {c}vira uma centena. [p=0.3] É a {d}base dez: dez algarismos, do zero ao nove."),
    dict(id="s05", block="base10", text="Trezentos e cinquenta e dois é {a}três centenas, [p=0.2] {b}cinco dezenas {c}e duas unidades. [p=0.3] Cada algarismo vale {d}ele mesmo, vezes o valor da sua casa."),
    # base dois
    dict(id="s06", block="base2", text="Na {a}base dois, os grupos são de dois. [p=0.2] Só existem {b}dois algarismos: o zero e o um. [p=0.3] Juntou dois, já sobe uma casa. [p=0.2] Então cada casa vale {c}o dobro da casa da direita: [p=0.2] {d}um, dois, quatro, oito, dezesseis. [p=0.2] São as potências de dois."),
    dict(id="s07", block="base2", text="Agora, leia {a}um, zero, um, um na base dois. [p=0.2] Ponha cada algarismo na sua casa, {b}começando pela direita: [p=0.2] um, dois, quatro, oito. [p=0.3] {c}Some só as casas que têm um: [p=0.2] oito, mais dois, mais um. [p=0.2] {d}Onze."),
    dict(id="s08", block="base2", text="Para não confundir, a base vai {a}num número pequeno, embaixo, à direita. [p=0.2] Um, zero, um, um, na base dois, {b}é igual a onze na base dez."),
    # de dez para dois
    dict(id="s09", block="divisoes", text="E o caminho de volta? [p=0.2] Vamos escrever {a}treze na base dois. [p=0.2] {b}Divida por dois e anote o resto. [p=0.3] {c}Treze dividido por dois: seis, resto um. [p=0.2] {d}Seis dividido por dois: três, resto zero. [p=0.2] {e}Três dividido por dois: um, resto um. [p=0.2] {f}Um dividido por dois: zero, resto um."),
    dict(id="s10", block="divisoes", text="Quando o resultado chega a zero, pare. [p=0.2] Cada resto é {a}o que sobrou fora dos grupos de dois, [p=0.2] e o primeiro resto é {b}a casa da unidade. [p=0.3] Por isso, {c}leia os restos de baixo para cima: [p=0.2] {d}um, um, zero, um. [p=0.3] Confira: {e}oito mais quatro mais um, treze."),
    # base sessenta
    dict(id="s11", block="base60", text="Agora, a {a}base sessenta. [p=0.2] O relógio conta {b}em grupos de sessenta. [p=0.2] Juntou sessenta segundos, {c}vira um minuto. [p=0.2] Juntou sessenta minutos, {d}vira uma hora. [p=0.3] Essa contagem de sessenta em sessenta vem da antiga Mesopotâmia."),
    dict(id="s12", block="base60", text="Noventa minutos: {a}quantos grupos de sessenta cabem? [p=0.2] {b}Noventa dividido por sessenta dá um, resto trinta. [p=0.3] O resultado vira hora, {c}e o resto fica em minutos: [p=0.2] {d}uma hora e trinta minutos."),
    # erro
    dict(id="s13", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}ler os restos de cima para baixo. [p=0.2] No treze, a pessoa escreve {b}um, zero, um, um. [p=0.3] Mas um, zero, um, um é {c}o onze do começo da aula, não o treze."),
    dict(id="s14", block="erro", text="O primeiro resto é {a}a unidade, a casa mais à direita. [p=0.2] Por isso, ele {b}fica no fim do número. [p=0.3] {c}Leia sempre de baixo para cima."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para números pequenos: [p=0.2] {a}escreva as casas: dezesseis, oito, quatro, dois, um. [p=0.3] Para o treze, {b}pegue a maior casa que cabe: oito. [p=0.2] Sobram cinco. [p=0.2] {c}Cabe o quatro, e sobra um. [p=0.2] {d}O dois não cabe: zero. [p=0.2] {e}Cabe o um. [p=0.3] {f}Um, um, zero, um."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cada casa é maior que todas as da direita somadas: [p=0.2] oito é mais que quatro, mais dois, mais um. [p=0.2] Então, a maior casa que cabe tem de entrar. [p=0.3] {b}Não compensa com números grandes, como trezentos: [p=0.2] aí, as divisões são mais seguras."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, em três partes. [p=0.2] {a}Quanto vale um, zero, um, um, zero, na base dois? [p=0.3] {b}Escreva vinte e cinco na base dois. [p=0.3] E {c}quanto é cento e cinquenta minutos, em horas e minutos?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}As casas de um, zero, um, um, zero são dezesseis, oito, quatro, dois, um. [p=0.2] As que têm um: {b}dezesseis, quatro e dois. [p=0.2] {c}Vinte e dois."),
    dict(id="s20", block="resposta", text="No vinte e cinco, {a}a maior casa que cabe é dezesseis, e sobram nove. [p=0.2] {b}Cabe o oito, e sobra um. [p=0.2] {c}Quatro e dois não cabem. [p=0.2] {d}Cabe o um. [p=0.3] {e}Um, um, zero, zero, um."),
    dict(id="s21", block="resposta", text="E os minutos: {a}cento e cinquenta dividido por sessenta dá dois, resto trinta. [p=0.2] {b}Duas horas e trinta minutos."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}a base diz o tamanho do grupo: dez, dois ou sessenta. [p=0.2] {b}Na base dois, as casas dobram. [p=0.2] E {c}da base dez para a dois, divida por dois e leia os restos de baixo para cima."),
    dict(id="s23", block="fim", text="Na próxima aula, você descobre {a}quais algarismos de uma medida contam de verdade, [p=0.2] e por que dois vírgula cinco vezes três vírgula catorze, numa medida, vira {b}sete vírgula nove. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
