# Estudativo · MAT-EXP-015 — Praticando: logaritmos (Matemática · Exponencial e Logaritmo · prática).
# Habilidade: aplicar propriedades, resolver equações e interpretar escalas logarítmicas em problemas de ciências.
# Pré-requisitos: MAT-EXP-008 a MAT-EXP-014. Próxima: MAT-PRO-001 (fim da trilha; começa Progressões).
# Questões inéditas, criadas para esta aula; dados de pH, bactérias e terremotos inventados. log 2 ≈ 0,30 e log 3 ≈ 0,48, como na MAT-EXP-010.
# Situação 1: pH = −log(2 · 10⁻⁴) · log(2 · 10⁻⁴) = log 2 + log 10⁻⁴ = 0,30 − 4 = −3,70 → pH ≈ 3,7 (entre 3 e 4; real: 3,699).
# Situação 2: N = N₀ · 1,2ᵗ, dobrar: 1,2ᵗ = 2 → t · log 1,2 = log 2 · log 1,2 = log 12 − log 10 = (2 · 0,30 + 0,48) − 1 = 0,08
#   → t = 0,30 ÷ 0,08 = 3,75 h · 0,75 × 60 = 45 → 3 h 45 min (valor exato com logs reais: 3,80 h).
# Situação 3: log₂(x + 3) + log₂(x − 3) = 4 · condição x > 3 · (x + 3)(x − 3) = 2⁴ = 16 → x² − 9 = 16 → x² = 25 → x = 5 ou −5 · −5 sai (log₂(−2) não existe)
#   · conferir: log₂ 8 + log₂ 2 = 3 + 1 = 4. Erro: aceitar −5. (Diferente do exemplo da MAT-EXP-012.)
# Situação 4: M = log(A/A₀) · 5,3 − 5,0 = 0,3 · A₁/A₂ = 10^0,3 ≈ 2 (log 2 ≈ 0,30; real 1,995).
# Atalho: na base dez, +0,30 ≈ dobrar, +0,48 ≈ triplicar · em dB (10 · log), dobrar = +3 dB · não compensa quando o enunciado pede precisão.
# Visual: fórmulas na tela com cada letra legendada; propriedades como cartões (produto → soma, potência → vezes); log 2 ≈ 0,30 e log 3 ≈ 0,48 fixos no canto;
#   E.reta numérica com x > 3 e o −5 riscado em vermelho; dois sismogramas (E.curva em onda), um com o dobro da altura; barras (E.colunas) de bactérias dobrando.
# Fórmulas com letras na tela; narração fala as grandezas pelo nome (amplitude, referência).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; log narrado "logaritmo de oito na base dois"; pH "pê agá".

TITULO = "Praticando: logaritmos"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações de ciências, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}as propriedades, em que produto vira soma e potência vira multiplicação; [p=0.2] {b}logaritmo de dois perto de zero vírgula trinta, e de três perto de zero vírgula quarenta e oito; [p=0.2] {c}o logaritmando sempre positivo; [p=0.2] e {d}a diferença na escala, que vira expoente do dez. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: pH com log 2
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] A fórmula do pê agá é {b}menos o logaritmo da concentração de hidrogênio. [p=0.2] Um suco tem concentração de {c}dois vezes dez elevado a menos quatro. [p=0.3] {d}Qual é o pê agá do suco? [p=0.2] Use logaritmo de dois perto de zero vírgula trinta."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Logaritmo de um produto é {a}a soma dos logaritmos. [p=0.2] {b}Logaritmo de dois dá zero vírgula trinta. [p=0.2] {c}Logaritmo de dez elevado a menos quatro dá menos quatro. [p=0.3] Somando, {d}zero vírgula trinta menos quatro dá menos três vírgula setenta. [p=0.2] Com o menos da fórmula, {e}pê agá três vírgula sete."),
    dict(id="s06", block="resposta1", text="Confira se faz sentido. [p=0.2] A concentração está {a}entre dez elevado a menos quatro e dez elevado a menos três. [p=0.2] Então o pê agá tem que ficar {b}entre três e quatro. [p=0.2] Bateu."),
    # situação 2: achar o expoente
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma cultura de bactérias cresce {b}vinte por cento por hora. [p=0.2] A quantidade segue {c}ene igual a ene zero vezes um vírgula dois elevado a tê, com tê em horas. [p=0.3] {d}Em quanto tempo a cultura dobra? [p=0.2] Use logaritmo de dois perto de zero vírgula trinta, e de três perto de zero vírgula quarenta e oito."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Dobrar é {a}um vírgula dois elevado a tê igual a dois. [p=0.2] O tê está no expoente, e dois não é potência de um vírgula dois. [p=0.2] Então tire o logaritmo na base dez de cada lado. [p=0.2] O expoente desce multiplicando: {b}tê vezes logaritmo de um vírgula dois, igual a logaritmo de dois."),
    dict(id="s10", block="resposta2", text="Agora desmonte o um vírgula dois: {a}é doze dividido por dez. [p=0.2] Doze é {b}dois vezes dois vezes três: [p=0.2] zero vírgula trinta mais zero vírgula trinta mais zero vírgula quarenta e oito dá {c}um vírgula zero oito. [p=0.2] Tire o logaritmo de dez, que é um: [p=0.2] {d}logaritmo de um vírgula dois dá zero vírgula zero oito."),
    dict(id="s11", block="resposta2", text="Então {a}tê é zero vírgula trinta dividido por zero vírgula zero oito. [p=0.2] Multiplique em cima e embaixo por cem: {b}trinta dividido por oito dá três vírgula setenta e cinco. [p=0.3] Zero vírgula setenta e cinco de hora é três quartos de sessenta minutos, que dá quarenta e cinco. [p=0.2] {c}Cerca de três horas e quarenta e cinco minutos."),
    # situação 3: equação com condição de existência
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Resolva, com a base dois: [p=0.2] {b}logaritmo de xis mais três, [p=0.1] mais logaritmo de xis menos três, [p=0.1] igual a quatro. [p=0.2] Xis mais três fica todo dentro do primeiro logaritmo, e xis menos três, todo dentro do segundo. [p=0.3] {c}Atenção às condições."),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Primeiro, as condições: {a}xis mais três e xis menos três positivos. [p=0.2] As duas valem juntas quando {b}xis é maior que três. [p=0.3] Soma de logaritmos de mesma base vira {c}logaritmo do produto. [p=0.2] Logaritmo igual a quatro na base dois: {d}o produto é dois elevado a quatro, que dá dezesseis."),
    dict(id="s15", block="resposta3", text="Soma vezes diferença: os termos do meio se cancelam, e fica {a}xis ao quadrado menos nove igual a dezesseis. [p=0.2] {b}Xis ao quadrado igual a vinte e cinco. [p=0.2] Dá {c}cinco ou menos cinco. [p=0.3] Aqui está a armadilha: {d}menos cinco não é maior que três. [p=0.2] Com ele, apareceria logaritmo de menos dois, que não existe. [p=0.2] {e}A resposta é só xis igual a cinco."),
    dict(id="s16", block="resposta3", text="Conferindo: {a}cinco mais três dá oito, e o logaritmo de oito na base dois dá três. [p=0.2] {b}Cinco menos três dá dois, e o logaritmo de dois na base dois dá um. [p=0.2] {c}Três mais um dá quatro. [p=0.2] Bateu."),
    # situação 4: escala com log 2
    dict(id="s17", block="questao4", text="{a}Situação quatro. [p=0.2] A magnitude de um terremoto é {b}eme igual ao logaritmo da amplitude dividida por uma amplitude de referência, [p=0.2] e a amplitude é o tamanho do tremor. [p=0.3] Um tremor marcou {c}cinco vírgula três, e outro, {d}cinco vírgula zero. [p=0.3] {e}Quantas vezes a amplitude do primeiro é maior?"),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] A diferença das magnitudes é {a}zero vírgula três. [p=0.2] Ela é o logaritmo da divisão das amplitudes, [p=0.2] então a divisão é {b}dez elevado a zero vírgula três. [p=0.3] E que número tem logaritmo perto de zero vírgula trinta? [p=0.2] {c}O dois. [p=0.2] A amplitude é {d}cerca de duas vezes maior."),
    # atalho
    dict(id="s20", block="atalho", text="Aqui cabe um atalho de prova: {a}na base dez, zero vírgula três a mais é dobrar. [p=0.2] E {b}zero vírgula quarenta e oito a mais é triplicar. [p=0.3] Em decibéis, com o dez na frente da fórmula, {c}dobrar a intensidade soma três decibéis."),
    dict(id="s21", block="atalho", text="Funciona porque {a}logaritmo de dois perto de zero vírgula trinta é o mesmo que dez elevado a zero vírgula trinta perto de dois. [p=0.3] Não compensa quando o enunciado {b}dá outros valores ou pede mais precisão: [p=0.2] aí, {c}use os números da questão."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}desmonte os números em dois, três e dez; [p=0.2] {b}confira as condições antes de responder; [p=0.2] e {c}na escala, a diferença vira expoente do dez."),
    dict(id="s23", block="fim", text="Com isso, você fecha exponencial e logaritmo. [p=0.3] Na próxima aula, começa um assunto novo: {a}sequências. [p=0.2] Você vai achar {b}o décimo termo de uma lista de números só pela regra, sem escrever todos, [p=0.2] e separar {c}a posição do valor. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
