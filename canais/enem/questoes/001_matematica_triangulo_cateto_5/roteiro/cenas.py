# Estudativo · Questão 001 — triângulo retângulo com um cateto c = 5 e lados inteiros: quanto valem a e b?
# Aula horizontal 1920x1080 (~5 min), explicada passo a passo. Convenção brasileira: a = hipotenusa, b e c = catetos.
# Caminho: nomes → Pitágoras (exemplo 3-4-5) → por que "lados inteiros" importa → isolar a² − b² →
# PRODUTO NOTÁVEL (produto da soma pela diferença, com a distributiva e um exemplo numérico) → divisores de 25 →
# sistema → conferência (5-12-13, única resposta) → o mesmo método com cateto 7 → desafio do cateto 9 → resumo.
# Versão em inglês (Estudativo English): roteiro/cenas_en.py, mesmo visual, ferramentas com --lang en.
# Narração PT: gravação do autor (2026-10-25); o texto abaixo segue o que foi falado (roteiro anterior em
# cenas_roteiro_gemini.py.bak, usado na voz Gemini).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa

TITULO = "Triângulo retângulo com um cateto 5 e lados inteiros: ache a e b com Pitágoras e produto notável"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão para um aluno: voz masculina "
            "adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, sem "
            "introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com curiosidade "
            "genuína, mostre surpresa no truque e comemore o resultado. Respeite as pausas entre as frases. Leia apenas "
            "o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Um triângulo retângulo tem um cateto igual a *cinco,* [p=0.2] e os três lados são *números inteiros.* "
        "[p=0.3] {b}Quanto valem os outros dois lados? [p=0.4] {c}Parece que falta informação, [p=0.2] mas não falta. "
        "[p=0.3] {d}Nessa aula, você vai resolver isso passo a passo, [p=0.1] usando o *Teorema de Pitágoras* "
        "[p=0.1] e um *produto notável.*"),
    dict(id="02", block="nomes", text=
        "{a}Primeiro, os nomes. [p=0.2] Triângulo retângulo é aquele que tem um *ângulo reto,* [p=0.1] de noventa "
        "graus. [p=0.3] {b}O lado oposto ao ângulo reto é a *hipotenusa,* [p=0.1] e ela é sempre o *maior lado.* "
        "[p=0.1] Vamos chamá-la de *a.* [p=0.3] {c}Os outros dois lados são os *catetos,* [p=0.1] que vamos chamar de "
        "*b* e *c.* [p=0.3] {d}No nosso problema, [p=0.1] o cateto c vale cinco."),
    dict(id="03", block="pitagoras", text=
        "{a}O Teorema de Pitágoras liga os três lados: [p=0.2] *a ao quadrado é igual a b ao quadrado mais c ao "
        "quadrado.* [p=0.3] {b}Por exemplo, [p=0.1] no triângulo de lados três, quatro e cinco: [p=0.1] três ao "
        "quadrado é nove, [p=0.1] quatro ao quadrado é dezesseis, [p=0.1] e nove mais dezesseis dá vinte e cinco, "
        "[p=0.1] que é cinco ao quadrado. [p=0.2] Repare: [p=0.1] naquele exemplo, o cinco era a hipotenusa. [p=0.3] "
        "{c}No nosso triângulo, [p=0.1] o cinco é um cateto. [p=0.2] {d}Então temos que [p=0.1] *a ao quadrado é "
        "igual a b ao quadrado mais vinte e cinco.*"),
    dict(id="04", block="infinitas", text=
        "{a}Só que essa equação tem *duas incógnitas.* [p=0.3] {b}Se os lados pudessem ser qualquer número real "
        "positivo, [p=0.1] haveria *infinitas respostas.* [p=0.2] {c}Com b igual a um, [p=0.1] a seria a raiz "
        "quadrada de vinte e seis. [p=0.2] Com b igual a dois, [p=0.1] a seria a raiz quadrada de vinte e nove, "
        "[p=0.1] e assim por diante. [p=0.3] {d}A informação que resolve tudo é esta: [p=0.1] *os lados são números "
        "inteiros.*"),
    dict(id="05", block="chute", text=
        "{a}Uma saída seria testar: [p=0.1] substituir b por um, dois, três, [p=0.1] e continuar até encontrar um "
        "valor que faça a ao quadrado resultar em um *quadrado perfeito.* [p=0.3] {b}Até funciona, [p=0.1] mas é "
        "lento, [p=0.1] e não prova que não existe outra resposta. [p=0.3] {c}Existe um caminho melhor, [p=0.1] que "
        "encontra *todas* as respostas de uma vez."),
    dict(id="06", block="isolar", text=
        "{a}Primeiro passo: [p=0.1] passar o b ao quadrado para o outro lado da equação. [p=0.2] {b}Como ele está "
        "somando, [p=0.1] passa *subtraindo.* [p=0.2] {c}Assim temos *a ao quadrado menos b ao quadrado é igual a "
        "vinte e cinco.* [p=0.3] {d}Do lado esquerdo ficou uma *diferença de dois quadrados.* [p=0.2] E é aqui que "
        "entra o produto notável."),
    dict(id="07", block="produto", text=
        "{a}Produtos notáveis são multiplicações que aparecem com tanta frequência na matemática [p=0.1] que vale a "
        "pena *conhecer seus resultados de cor.* [p=0.3] {b}Um deles é o *produto da soma pela diferença.* [p=0.2] "
        "{c}Funciona assim: [p=0.1] abrimos parênteses, x mais y, fechamos parênteses; [p=0.1] multiplicamos por: "
        "[p=0.1] abrimos parênteses, x menos y, fechamos parênteses. [p=0.1] O resultado é *x ao quadrado menos y ao "
        "quadrado.* [p=0.3] {d}Dá para conferir usando a propriedade distributiva. [p=0.2] {e}x vezes x dá x ao "
        "quadrado; [p=0.1] x vezes menos y dá menos x vezes y. [p=0.2] {f}y vezes x dá mais x vezes y; [p=0.1] e y "
        "vezes menos y dá menos y ao quadrado. [p=0.3] {g}Os dois termos do meio se *cancelam,* [p=0.1] porque um é "
        "negativo e o outro é positivo. [p=0.2] E o que sobra? [p=0.1] x ao quadrado menos y ao quadrado."),
    dict(id="08", block="exemplo", text=
        "{a}Vamos ver um exemplo com números: [p=0.1] dez mais três, [p=0.1] multiplicado por dez menos três, "
        "[p=0.2] é o mesmo que treze vezes sete, [p=0.1] que resulta em noventa e um. [p=0.3] {b}Agora, usando a "
        "diferença de quadrados, [p=0.1] temos dez ao quadrado menos três ao quadrado, [p=0.1] ou seja, cem menos "
        "nove, [p=0.1] que também resulta em *noventa e um.* [p=0.2] Funciona!"),
    dict(id="09", block="aplica", text=
        "{a}Agora, vamos ler a fórmula ao contrário, [p=0.1] colocando a no lugar de x e b no lugar de y: [p=0.2] "
        "a ao quadrado menos b ao quadrado [p=0.1] é igual a *a mais b, multiplicado por a menos b.* [p=0.3] "
        "{b}Portanto, nossa equação se transforma em: [p=0.1] a soma de a com b, [p=0.1] multiplicada pela diferença "
        "entre a e b, [p=0.1] *é igual a vinte e cinco.* [p=0.3] {c}Repare no que aconteceu: [p=0.1] a diferença de "
        "dois quadrados virou uma *multiplicação entre dois números inteiros,* [p=0.1] cujo resultado é vinte e "
        "cinco."),
    dict(id="10", block="divisores", text=
        "{a}E quais multiplicações entre números inteiros positivos resultam em vinte e cinco? [p=0.3] {b}Temos "
        "apenas duas possibilidades: [p=0.1] *um vezes vinte e cinco,* [p=0.1] e *cinco vezes cinco.* [p=0.3] "
        "{c}Agora, um detalhe importante: [p=0.1] como b é positivo, [p=0.1] a mais b é necessariamente *maior* que "
        "a menos b. [p=0.3] {d}Portanto, a mais b representa o fator maior, [p=0.1] enquanto a menos b representa o "
        "fator menor. [p=0.3] {e}No caso de cinco vezes cinco, [p=0.1] os dois fatores seriam iguais, [p=0.1] e "
        "isso só aconteceria se b fosse igual a zero. [p=0.2] Mas um lado de medida zero [p=0.1] *não forma um "
        "triângulo.*"),
    dict(id="11", block="sistema", text=
        "{a}Então, sobra apenas uma possibilidade: [p=0.1] a mais b é igual a *vinte e cinco,* [p=0.1] e a menos b "
        "é igual a *um.* [p=0.3] {b}Agora, temos um sistema de duas equações. [p=0.1] Somando as duas equações, "
        "[p=0.1] o b positivo e o b negativo se *cancelam.* [p=0.2] {c}Assim, duas vezes a é igual a vinte e seis. "
        "[p=0.1] Dividindo os dois lados por dois, [p=0.1] descobrimos que *a é igual a treze.* [p=0.3] {d}Agora, "
        "voltamos à primeira equação: [p=0.1] treze mais b é igual a vinte e cinco. [p=0.1] Logo, *b é igual a "
        "doze.*"),
    dict(id="12", block="confere", text=
        "{a}Encontramos a resposta. [p=0.1] Mas, em matemática, é sempre importante conferir. [p=0.2] Doze ao "
        "quadrado é cento e quarenta e quatro, [p=0.1] cinco ao quadrado é vinte e cinco. [p=0.1] Somando os dois "
        "resultados, encontramos cento e sessenta e nove. [p=0.2] {b}E treze ao quadrado [p=0.1] também é *cento e "
        "sessenta e nove.* [p=0.3] {c}Portanto, o nosso triângulo tem lados *cinco, doze e treze,* [p=0.1] e essa é a "
        "*única* resposta possível com lados inteiros."),
    dict(id="13", block="generaliza", text=
        "{a}E sabe o que é ainda melhor? [p=0.1] Esse mesmo método funciona para outros valores de catetos. [p=0.2] "
        "{b}Imagine, por exemplo, que um dos catetos seja igual a sete. [p=0.1] Aplicando o mesmo raciocínio, "
        "teremos: [p=0.1] a mais b, multiplicado por a menos b, é igual a quarenta e nove. [p=0.2] {c}Como um vezes "
        "quarenta e nove resulta em quarenta e nove, [p=0.1] podemos montar um novo sistema: [p=0.1] a mais b é igual "
        "a quarenta e nove, [p=0.1] e a menos b é igual a um. [p=0.1] Resolvendo, encontramos a igual a vinte e cinco "
        "[p=0.1] e b igual a vinte e quatro. [p=0.1] Assim, formamos outro triângulo retângulo de lados inteiros: "
        "[p=0.1] *sete, vinte e quatro e vinte e cinco.* [p=0.3] {d}Agora é com você: [p=0.1] tente resolver o mesmo "
        "problema considerando um cateto igual a *nove.* [p=0.1] Quais seriam as medidas dos outros dois lados? "
        "[p=0.1] Deixe sua resposta nos comentários. [p=0.2] E aqui vai uma dica: [p=0.1] dessa vez, pode existir "
        "*mais de uma solução.*"),
    dict(id="14", block="resumo", text=
        "{a}Vamos recapitular o caminho que aprendemos nesta aula. [p=0.2] {b}Primeiro, aplicamos o Teorema de "
        "Pitágoras. [p=0.2] {c}Depois, isolamos a diferença de dois quadrados. [p=0.2] {d}Em seguida, utilizamos o "
        "produto notável da soma pela diferença. [p=0.2] {e}Listamos as possibilidades de multiplicação entre os "
        "divisores do número encontrado. [p=0.2] {f}E, por último, resolvemos o sistema de equações [p=0.1] para "
        "descobrir as medidas dos lados."),
    dict(id="15", block="aulas", text=
        "{a}Cada uma dessas ferramentas [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*Teorema de Pitágoras,* [p=0.2] {c}*produtos notáveis* [p=0.2] {d}e *sistemas de equações.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procura essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima aula."),
]
