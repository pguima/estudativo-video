# Estudativo · MAT-FRA-017 — Dividir com resultado decimal (Matemática · Frações e Decimais).
# Habilidade: calcular 7,5 ÷ 3 e 7 ÷ 4 = 1,75 continuando a conta depois da vírgula.
# Pré-requisitos: MAT-FRA-014 (ler e arredondar decimais), MAT-NUM-009 (dividir por um algarismo). Próxima: MAT-FRA-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dividir com resultado decimal"

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
    dict(id="s01", block="gancho", text="{a}Sete reais divididos entre {b}quatro pessoas. [p=0.3] A conta dá {c}um, e sobram três. [p=0.3] Se você escreveu {d}um vírgula três, [p=0.2] caiu numa armadilha: esse dinheiro não fecha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai continuar a divisão depois da vírgula, [p=0.2] até o resto acabar, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}dividir por um algarismo, com resto, [p=0.2] e {c}saber o que são décimos e centésimos. [p=0.3] Se faltar alguma, procure no canal."),
    # vírgula no dividendo
    dict(id="s04", block="virgula", text="Comece com uma vírgula que já está lá. [p=0.2] {a}Sete reais e cinquenta centavos para {b}três pessoas. [p=0.3] A conta é {c}sete vírgula cinco dividido por três."),
    dict(id="s05", block="virgula", text="Primeiro, os reais: {a}sete dividido por três dá dois, [p=0.2] e {b}sobra um. [p=0.3] Os inteiros acabaram e chegou a vírgula. [p=0.2] Então {c}coloque a vírgula no resultado."),
    dict(id="s06", block="virgula", text="O real que sobrou vira {a}dez moedas de dez centavos. [p=0.2] {b}Desça o cinco: são mais cinco moedas, [p=0.2] {c}quinze ao todo. [p=0.3] {d}Quinze dividido por três dá cinco. [p=0.2] Resultado: {e}dois vírgula cinco. [p=0.2] {f}Dois reais e cinquenta centavos para cada pessoa."),
    # continuar depois da vírgula
    dict(id="s07", block="continuar", text="E quando não há vírgula nenhuma? [p=0.2] Volte aos sete reais. [p=0.2] {a}Sete dividido por quatro dá um, [p=0.2] e {b}sobram três."),
    dict(id="s08", block="continuar", text="A conta não precisa parar. [p=0.2] Os três reais não somem: [p=0.2] viram {a}trinta moedas de dez centavos. [p=0.3] Na conta, {b}coloque a vírgula no resultado [p=0.2] e {c}um zero ao lado do resto. [p=0.2] O três vira {d}trinta."),
    dict(id="s09", block="continuar", text="{a}Trinta dividido por quatro dá sete, [p=0.2] e {b}sobram duas moedas. [p=0.3] Elas viram {c}vinte moedas de um centavo. [p=0.2] Mais um zero: {d}vinte."),
    dict(id="s10", block="continuar", text="{a}Vinte dividido por quatro dá cinco, [p=0.2] e {b}sobra zero. [p=0.3] Agora sim, acabou: {c}um vírgula setenta e cinco. [p=0.2] {d}Um real e setenta e cinco centavos para cada pessoa."),
    dict(id="s11", block="continuar", text="Confira: {a}quatro vezes um real são quatro reais, [p=0.2] e {b}quatro vezes setenta e cinco centavos são três reais. [p=0.3] Total: {c}sete reais. [p=0.2] Fecha."),
    dict(id="s12", block="continuar", text="A regra: {a}sobrou resto, acrescente um zero e continue. [p=0.2] Cada zero leva para a casa seguinte: [p=0.2] {b}décimos, [p=0.2] depois {c}centésimos."),
    # menor que o divisor
    dict(id="s13", block="menor", text="E se não der nem um inteiro? [p=0.2] {a}Um real para quatro pessoas. [p=0.3] Um dividido por quatro não dá, então {b}escreva zero e vírgula no resultado. [p=0.3] O um vira {c}dez: dá dois, e sobram dois. [p=0.2] Mais um zero: {d}vinte, que dá cinco, e sobra zero. [p=0.3] {e}Zero vírgula vinte e cinco: vinte e cinco centavos."),
    # zero no resultado
    dict(id="s14", block="zero", text="Outra armadilha: {a}quatro vírgula dois dividido por quatro. [p=0.3] {b}Quatro dividido por quatro dá um, e sobra zero. [p=0.2] {c}Vírgula no resultado. [p=0.2] Desça o dois: {d}dois dividido por quatro não dá."),
    dict(id="s15", block="zero", text="Não pule essa casa: {a}escreva zero no resultado [p=0.2] e {b}acrescente um zero ao lado do dois. [p=0.3] {c}Vinte dividido por quatro dá cinco. [p=0.2] Resultado: {d}um vírgula zero cinco."),
    # não acaba
    dict(id="s16", block="semfim", text="Às vezes o resto {a}nunca zera. [p=0.2] {b}Dez dividido por três dá três vírgula três três três, sem fim, [p=0.2] porque sobra um toda vez. [p=0.3] Aí você {c}para na casa que o problema pedir e arredonda. [p=0.2] Com duas casas, a terceira é um três, menos que cinco: [p=0.2] {d}três vírgula trinta e três."),
    # erro
    dict(id="s17", block="erro", text="O erro comum é {a}colar o resto depois da vírgula: [p=0.2] um, resto três, {b}um vírgula três. [p=0.3] Mas quatro pessoas com {c}um real e trinta centavos somam só {d}cinco reais e vinte centavos. [p=0.3] {e}O resto ainda precisa ser dividido. [p=0.2] Ele não é a parte depois da vírgula."),
    # atalho
    dict(id="s18", block="atalho", text="Agora o atalho: {a}dividir por quatro é tirar a metade, e depois a metade de novo. [p=0.3] {b}Metade de sete reais: três e cinquenta. [p=0.2] {c}Metade de três e cinquenta: um e setenta e cinco."),
    dict(id="s19", block="atalho", text="Funciona porque {a}quatro é dois vezes dois. [p=0.3] Por isso, ele é para quando o divisor, o número que divide, é quatro. [p=0.2] {b}Não compensa quando a metade não sai de cabeça: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Uma conta de {a}nove reais e trinta centavos [p=0.2] vai ser dividida igualmente entre {b}seis amigos. [p=0.3] {c}Quanto cada um paga?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}Nove dividido por seis dá um, [p=0.2] e {b}sobram três. [p=0.2] Chegou a vírgula: {c}vírgula no resultado. [p=0.3] Desça o três: {d}trinta e três. [p=0.2] {e}Dá cinco, e sobram três."),
    dict(id="s23", block="resposta", text="Sobrou resto, então a conta continua. [p=0.2] {a}Mais um zero: trinta. [p=0.2] {b}Trinta dividido por seis dá cinco, [p=0.2] e {c}sobra zero. [p=0.3] Cada amigo paga {d}um real e cinquenta e cinco centavos."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}chegou na vírgula, coloque a vírgula. [p=0.2] {b}Sobrou resto, acrescente zero. [p=0.2] {c}Continue até zerar ou até a casa pedida."),
    dict(id="s25", block="fim", text="Até aqui, quem divide sempre foi um número inteiro. [p=0.2] Na próxima aula, {a}o divisor tem vírgula, [p=0.2] e você aprende a {b}tirar essa vírgula antes de dividir. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
