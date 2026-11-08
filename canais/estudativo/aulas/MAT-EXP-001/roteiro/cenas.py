# Estudativo · MAT-EXP-001 — Função exponencial: lei e gráfico (Matemática · Exponencial e Logaritmo).
# Habilidade: traçar y = 2ˣ e y = (1/2)ˣ, dizer qual cresce e qual decresce e explicar por que a base é positiva e diferente de 1.
# Pré-requisitos: MAT-FUN-006 (gráfico de uma função), MAT-POT-005 (expoente negativo), MAT-POT-008 (expoente fracionário). Próxima: MAT-EXP-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Função exponencial: lei e gráfico"

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
    dict(id="s01", block="gancho", text="{a}Dobre uma folha de papel ao meio. [p=0.2] A espessura {b}dobra. [p=0.2] Dobre de novo, e de novo. [p=0.3] Se desse para dobrar {c}dez vezes, a folha ficaria {d}mil e vinte e quatro vezes mais grossa."),
    dict(id="s02", block="gancho", text="Essa conta é uma função em que o xis {a}mora no expoente. [p=0.3] {b}Até o fim desta aula, você desenha o gráfico dela, diz quando ele sobe e quando desce, [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}desenhar um gráfico com tabela, pontos e curva suave, [p=0.2] {b}expoente negativo, que vira fração, [p=0.2] e {c}expoente em fração, que vira raiz. [p=0.3] Se faltar alguma, procure no canal."),
    # lei
    dict(id="s04", block="lei", text="No papel, a espessura fica multiplicada por {a}dois elevado ao número de dobras. [p=0.3] Chame o número de dobras de xis: [p=0.2] {b}efe de xis igual a dois elevado a xis. [p=0.3] A base, o dois, {c}fica fixa. [p=0.2] O que muda é {d}o expoente, e ele é a entrada. [p=0.3] Função assim se chama {e}função exponencial."),
    # tabela de dois elevado a xis
    dict(id="s05", block="tabela2", text="Vamos à tabela, com xis de menos dois até três. [p=0.2] {a}Dois elevado a zero dá um. [p=0.2] {b}Dois elevado a um dá dois. [p=0.2] {c}Ao quadrado dá quatro. [p=0.2] {d}Ao cubo dá oito."),
    dict(id="s06", block="tabela2", text="Expoente negativo vira fração. [p=0.2] {a}Dois elevado a menos um dá um meio. [p=0.2] {b}Dois elevado a menos dois dá um quarto."),
    # gráfico crescente
    dict(id="s07", block="grafico2", text="Marque os pontos e ligue com {a}uma curva suave. [p=0.3] Da esquerda para a direita, ela sobe cada vez mais rápido: [p=0.2] cada passo para a direita {b}dobra a altura. [p=0.3] Quando a saída aumenta junto com o xis, a função é {c}crescente. [p=0.3] E repare: ela passa pelo ponto {d}xis zero, ípsilon um, porque dois elevado a zero dá um."),
    dict(id="s08", block="grafico2", text="E para a esquerda? [p=0.2] {a}Um meio. Um quarto. Um oitavo. [p=0.3] A curva chega {b}cada vez mais perto do eixo xis, [p=0.2] mas {c}nunca encosta. [p=0.3] A metade de um número positivo ainda é positiva. [p=0.2] Por isso, dois elevado a xis {d}nunca dá zero nem negativo."),
    # base um meio
    dict(id="s09", block="tabelameio", text="Agora troque a base por {a}um meio: [p=0.2] efe de xis igual a um meio elevado a xis. [p=0.3] {b}Um meio elevado a zero dá um. [p=0.2] {c}Elevado a um dá um meio. [p=0.2] {d}Ao quadrado dá um quarto. [p=0.2] {e}Ao cubo dá um oitavo."),
    dict(id="s10", block="tabelameio", text="E com xis negativo? [p=0.2] Expoente negativo vira fração com um em cima: [p=0.2] {a}um dividido por um meio. [p=0.2] Dividir por um meio é multiplicar por dois: {b}dá dois. [p=0.3] Do mesmo jeito, {c}um meio elevado a menos dois dá quatro."),
    # gráfico decrescente
    dict(id="s11", block="graficomeio", text="Essa curva {a}desce. [p=0.2] Cada passo para a direita {b}corta a altura pela metade. [p=0.2] A função é {c}decrescente. [p=0.3] Ela também passa pelo ponto {d}xis zero, ípsilon um, [p=0.2] e também nunca encosta no eixo xis, só que agora do lado direito."),
    dict(id="s12", block="graficomeio", text="Quem decide é a base. [p=0.2] {a}Base maior que um: a curva sobe. [p=0.2] {b}Base entre zero e um: a curva desce."),
    # por que a base é positiva e diferente de um
    dict(id="s13", block="base", text="E por que a base não pode ser {a}um? [p=0.2] Um elevado a qualquer expoente dá um. [p=0.2] O gráfico vira {b}uma reta deitada, na altura um. [p=0.3] Não sobe nem desce: não é exponencial."),
    dict(id="s14", block="base", text="E base negativa? [p=0.2] Tente {a}menos dois elevado a um meio. [p=0.2] Expoente um meio é raiz quadrada: [p=0.2] {b}raiz de menos dois, que não dá número da reta. [p=0.3] E nos expoentes inteiros, o sinal fica pulando. [p=0.2] {c}Menos dois. [p=0.1] Depois quatro. [p=0.1] Depois menos oito. [p=0.3] Não sai curva nenhuma."),
    dict(id="s15", block="base", text="A base zero também fica de fora: [p=0.2] {a}zero elevado a menos um seria um dividido por zero. [p=0.3] Por isso, a base da exponencial é sempre {b}positiva e diferente de um."),
    # erro
    dict(id="s16", block="erro", text="O erro comum é achar que expoente negativo deixa a saída negativa. [p=0.2] A pessoa escreve {a}dois elevado a menos um igual a menos dois, [p=0.2] e desenha a curva {b}passando para baixo do eixo xis."),
    dict(id="s17", block="erro", text="Mas dois elevado a menos um é {a}um meio. [p=0.2] Um número positivo. [p=0.3] Com base positiva, a exponencial {b}fica sempre acima do eixo xis."),
    # atalho
    dict(id="s18", block="atalho", text="Agora o atalho: {a}o espelho. [p=0.3] A tabela de um meio elevado a xis é a de dois elevado a xis {b}com o sinal do xis trocado. [p=0.3] Dois elevado a xis dá quatro em {c}xis igual a dois. [p=0.2] Um meio elevado a xis dá quatro em {d}xis igual a menos dois. [p=0.3] No desenho, uma curva é {e}a outra refletida no eixo ípsilon."),
    dict(id="s19", block="atalho", text="Funciona porque um meio é {a}dois elevado a menos um. [p=0.2] Potência de potência multiplica os expoentes: [p=0.2] {b}um meio elevado a xis é dois elevado a menos xis. [p=0.3] Só vale quando uma base é {c}o inverso da outra, como três e um terço. [p=0.2] Entre três e um meio, {d}não há espelho: monte a tabela."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Monte a tabela de {a}três elevado a xis, com xis de menos um até dois. [p=0.2] Depois, use o espelho para a tabela de {b}um terço elevado a xis. [p=0.3] {c}Qual das duas cresce, e qual decresce?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}Três elevado a menos um dá um terço. [p=0.2] {b}Três elevado a zero dá um. [p=0.2] {c}Elevado a um dá três. [p=0.2] {d}Ao quadrado dá nove."),
    dict(id="s23", block="resposta", text="No espelho, troque o sinal do xis. [p=0.2] {a}Um terço elevado a menos um dá três. [p=0.2] {b}Elevado a zero dá um. [p=0.2] {c}Elevado a um dá um terço. [p=0.2] {d}Ao quadrado dá um nono. [p=0.3] Base três, maior que um: {e}cresce. [p=0.2] Base um terço, entre zero e um: {f}decresce."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}na exponencial, o xis está no expoente. [p=0.2] {b}Base maior que um sobe, base entre zero e um desce, [p=0.2] e {c}a curva passa por xis zero, ípsilon um, sem nunca tocar o eixo xis."),
    dict(id="s25", block="fim", text="Na próxima aula, a exponencial vai para a vida real: [p=0.2] {a}uma população que cresce três por cento ao ano [p=0.2] e {b}um carro que perde dez por cento do valor a cada ano. [p=0.3] E você descobre, por uma tabela, quando o crescimento é de somar e quando é de multiplicar. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
