# Estudativo · MAT-FUN-011 — Zero da função e estudo do sinal (Matemática · Funções · Função afim).
# Habilidade: achar onde f(x) = 2x − 6 corta o eixo x e dizer para quais x ela é positiva ou negativa.
# Pré-requisitos: MAT-EQU-015 (inequação do 1º grau), MAT-FUN-010 (coeficientes). Próxima: MAT-FUN-012.
# Questão inédita, criada para esta aula. Letras narradas: "á", "bê", "xis", "ípsilon". "Zero" como na MAT-FUN-007: onde a curva toca o eixo x.
# f(x) = 2x − 6 (saldo de quem gastou R$ 6 de material e ganha R$ 2 por brigadeiro): zero x = 3 · f(1) = −4 · f(5) = 4 ·
#   positiva x > 3 · negativa x < 3 · lucro a partir do 4º brigadeiro: f(4) = 2.
# g(x) = −3x + 12: zero x = 4 · −3x > −12 → x < 4 (vira o sinal) · erro: dizer positiva para x > 4; g(5) = −3.
# Atalho: à direita da raiz, o sinal do á; à esquerda, o contrário · não vale com á = 0 (f(x) = 5, sem zero).
# Questão: h(x) = −4x + 10 · zero 2,5 · positiva x < 2,5 · negativa x > 2,5 · teste h(0) = 10.
# Visual: plano (E.plano) com a reta de 2x − 6 (E.reta_pontos) cortando o eixo x em (3, 0) (E.ponto); parte acima do eixo verde
#   e abaixo vermelha; reta numérica com "−" antes do 3 e "+" depois; mesma coisa para −3x + 12 com zero em 4.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Zero da função e estudo do sinal"

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
    dict(id="s01", block="gancho", text="Uma pessoa gastou {a}seis reais de material {b}e ganha dois reais por brigadeiro vendido. [p=0.3] {c}Com quantos brigadeiros ela empata? [p=0.2] {d}E a partir de quantos ela sai no positivo? [p=0.3] As duas respostas estão {e}num ponto só do gráfico."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha onde a reta corta o eixo xis, [p=0.2] {b}diz onde a função é positiva e onde é negativa [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o á da função afim, que diz se a reta sobe ou desce, [p=0.2] e {c}inequação, que vira o sinal quando você divide por negativo. [p=0.3] Se faltar alguma, procure no canal."),
    # zero
    dict(id="s04", block="zero", text="O saldo dela é {a}efe de xis igual a dois xis menos seis, [p=0.2] em que xis é o número de brigadeiros vendidos. [p=0.3] Empatar é ter {b}saldo zero. [p=0.2] Então a pergunta é: {c}para qual xis o efe de xis vale zero?"),
    dict(id="s05", block="zero", text="Monte a equação: {a}dois xis menos seis igual a zero. [p=0.2] {b}Some seis de cada lado: dois xis igual a seis. [p=0.2] {c}Divida por dois: xis igual a três. [p=0.3] Com {d}três brigadeiros, ela empata."),
    dict(id="s06", block="zero", text="Esse xis é o {a}zero da função, também chamado de {b}raiz. [p=0.3] No gráfico, é {c}onde a reta corta o eixo xis: [p=0.2] o ponto {d}xis três, ípsilon zero. [p=0.2] Ali a reta não está acima nem abaixo do eixo."),
    # sinal
    dict(id="s07", block="sinal", text="Agora, o sinal. [p=0.2] {a}Função positiva é ípsilon maior que zero: [p=0.2] a reta {b}acima do eixo xis. [p=0.2] {c}Negativa é ípsilon menor que zero: [p=0.2] a reta {d}abaixo do eixo."),
    dict(id="s08", block="sinal", text="Quando é positiva? [p=0.2] {a}Dois xis menos seis maior que zero. [p=0.2] {b}Some seis: dois xis maior que seis. [p=0.2] {c}Divida por dois, que é positivo: xis maior que três. [p=0.3] Do mesmo jeito, {d}é negativa para xis menor que três."),
    dict(id="s09", block="sinal", text="Confira com dois números. [p=0.2] {a}Com um brigadeiro, dois menos seis dá menos quatro: [p=0.2] ela ainda está no prejuízo. [p=0.2] {b}Com cinco brigadeiros, dez menos seis dá quatro reais positivos. [p=0.3] Na reta numérica, fica assim: [p=0.2] {c}menos antes do três, [p=0.2] {d}mais depois do três. [p=0.3] Como ninguém vende meio brigadeiro, [p=0.2] ela sai no positivo {e}a partir do quarto brigadeiro: [p=0.2] oito menos seis dá dois reais."),
    # reta que desce
    dict(id="s10", block="desce", text="E se a reta descer? [p=0.2] Veja {a}gê de xis igual a menos três xis mais doze. [p=0.3] Zero: {b}menos três xis mais doze igual a zero. [p=0.2] {c}Tire doze de cada lado: menos três xis igual a menos doze. [p=0.2] {d}Divida por menos três: xis igual a quatro."),
    dict(id="s11", block="desce", text="Positiva: {a}menos três xis mais doze maior que zero. [p=0.2] {b}Tire doze: menos três xis maior que menos doze. [p=0.2] {c}Dividiu por negativo, vira o sinal: [p=0.2] {d}xis menor que quatro. [p=0.3] Aqui, {e}a parte positiva fica à esquerda do quatro. [p=0.2] Faz sentido: a reta {f}começa no alto e desce."),
    # erro
    dict(id="s12", block="erro", text="E esse é o erro mais comum: [p=0.2] {a}achar que a parte positiva fica sempre à direita da raiz. [p=0.3] Quem faz isso diz que gê de xis é positiva {b}para xis maior que quatro. [p=0.2] Teste o cinco: [p=0.2] {c}menos três vezes cinco dá menos quinze. [p=0.2] {d}Mais doze, menos três. [p=0.2] {e}Negativo. [p=0.3] {f}Quem decide o lado é o sinal do á."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, sem inequação nenhuma: [p=0.2] {a}à direita da raiz, a função tem o mesmo sinal do á. [p=0.2] {b}À esquerda, o sinal contrário. [p=0.3] Em dois xis menos seis, {c}o á é positivo: depois do três, sinal de mais. [p=0.2] Em menos três xis mais doze, {d}o á é negativo: depois do quatro, sinal de menos."),
    dict(id="s14", block="atalho", text="Funciona porque {a}á positivo faz a reta subir: [p=0.2] depois de cruzar o eixo, ela fica em cima. [p=0.2] {b}Á negativo faz a reta descer: [p=0.2] depois de cruzar, fica embaixo. [p=0.3] {c}Não vale quando o á é zero. [p=0.2] Em {d}efe de xis igual a cinco, a reta é horizontal, [p=0.2] {e}nunca corta o eixo [p=0.2] e é positiva para todo xis."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Na função {a}agá de xis igual a menos quatro xis mais dez, [p=0.3] {b}onde a reta corta o eixo xis? [p=0.2] {c}Para quais xis ela é positiva? [p=0.2] E {d}para quais é negativa?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Menos quatro xis mais dez igual a zero. [p=0.2] {b}Tire dez de cada lado: menos quatro xis igual a menos dez. [p=0.2] {c}Divida por menos quatro: xis igual a dois vírgula cinco. [p=0.3] A reta corta o eixo xis {d}no dois vírgula cinco."),
    dict(id="s18", block="resposta", text="O á é {a}menos quatro, negativo. [p=0.2] Pelo atalho, {b}à direita da raiz vem o menos: [p=0.2] {c}negativa para xis maior que dois vírgula cinco. [p=0.2] E {d}positiva para xis menor que dois vírgula cinco. [p=0.3] Teste o xis zero: {e}agá de zero dá dez, positivo. [p=0.2] E o zero está à esquerda do dois vírgula cinco: {f}bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o zero é o xis que faz o ípsilon valer zero, [p=0.2] {b}onde a reta corta o eixo xis, [p=0.2] e {c}o sinal do á diz de que lado fica o positivo."),
    dict(id="s20", block="fim", text="Na próxima aula, você faz o caminho contrário: [p=0.2] {a}recebe dois pontos ou um gráfico [p=0.2] e {b}descobre a lei da função, [p=0.2] para {c}prever o próximo valor. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
