# Estudativo · MAT-FIN-005 — Juros simples contra compostos (Matemática · Matemática Financeira).
# Habilidade: dizer quem rende mais em 1 mês, em menos de 1 mês e em 2 anos.
# Pré-requisitos: MAT-FIN-004 (fórmula dos compostos), MAT-POT-008 (expoente fracionário). Próxima: MAT-FIN-006.
# Questão inédita, criada para esta aula. Taxa de 21% ao mês fictícia, dita como tal: escolhida para a raiz de 1,21 sair exata.
# Visual: gráfico com a reta dos simples e a curva dos compostos, cruzando em t = 1.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Juros simples contra compostos: quem rende mais"

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
    dict(id="s01", block="gancho", text="{a}Juros compostos rendem sempre mais que juros simples. [p=0.3] Parece verdade, [p=0.2] mas {b}é falso. [p=0.2] Em um caso, {c}os simples ganham."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer quem rende mais em qualquer prazo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a fórmula dos compostos, capital vezes o fator elevado ao tempo, [p=0.2] e {c}expoente em fração: nove elevado a um meio é raiz de nove. [p=0.3] Se faltar alguma, procure no canal."),
    # um mês
    dict(id="s04", block="um", text="Compare com {a}mil reais, a {b}vinte e um por cento ao mês. [p=0.2] É uma taxa absurda, escolhida só para as contas saírem redondas. [p=0.3] Fator: {c}um vírgula vinte e um."),
    dict(id="s05", block="um", text="{a}Em um mês. [p=0.2] Nos simples, vinte e um por cento de mil: {b}mil duzentos e dez. [p=0.2] Nos compostos, {c}mil vezes um vírgula vinte e um: o mesmo mil duzentos e dez. [p=0.3] Em um período, {d}empate. [p=0.2] Ainda não houve juro sobre juro."),
    # mais de um mês
    dict(id="s06", block="mais", text="{a}Em dois meses. [p=0.2] Nos simples, quarenta e dois por cento: {b}mil quatrocentos e vinte. [p=0.2] Nos compostos, {c}um vírgula vinte e um ao quadrado dá um vírgula quatro seis quatro um. [p=0.2] {d}Mil quatrocentos e sessenta e quatro reais e dez centavos. [p=0.3] {e}Os compostos ganham. [p=0.2] No segundo mês, os juros do primeiro também renderam."),
    dict(id="s07", block="mais", text="E quanto mais tempo, maior a vantagem. [p=0.2] Com uma taxa menor, {a}dois por cento ao mês, em dois anos: [p=0.2] nos simples, mil reais viram {b}mil quatrocentos e oitenta. [p=0.2] Nos compostos, com a potência tirada de uma tabela, {c}cerca de mil seiscentos e oito."),
    # menos de um mês
    dict(id="s08", block="meio", text="E {a}em menos de um mês? [p=0.2] Volte aos vinte e um por cento, por {b}meio mês. [p=0.3] Nos simples, metade da taxa: {c}dez vírgula cinco por cento. [p=0.2] Montante: {d}mil cento e cinco."),
    dict(id="s09", block="meio", text="Nos compostos, o tempo é {a}um meio: [p=0.1] {b}um vírgula vinte e um elevado a um meio. [p=0.2] Expoente um meio é {c}raiz quadrada. [p=0.2] {d}Raiz de um vírgula vinte e um dá um vírgula um, [p=0.1] porque um vírgula um ao quadrado dá um vírgula vinte e um. [p=0.3] Montante: {e}mil e cem. [p=0.3] {f}Os simples ganham, por cinco reais."),
    dict(id="s10", block="meio", text="Por quê? [p=0.2] Nos compostos, {a}dez por cento na primeira metade, [p=0.2] e {b}mais dez por cento sobre o que já rendeu, [p=0.1] fecham os vinte e um do mês. [p=0.3] Então cada metade rende só dez. [p=0.2] Nos simples, {c}cada metade rende dez e meio."),
    # gráfico
    dict(id="s11", block="grafico", text="No gráfico, {a}os simples são uma reta, [p=0.2] e {b}os compostos, uma curva. [p=0.2] Elas {c}se cruzam em um período. [p=0.3] {d}Antes disso, a reta fica por cima. [p=0.2] {e}Depois, a curva passa na frente."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}achar que compostos sempre rendem mais. [p=0.2] Em prazo menor que um período, {b}é o contrário. [p=0.3] E cuidado com o período: [p=0.1] ele é {c}o da taxa. [p=0.2] Com taxa ao ano, {d}seis meses ainda é menos que um período. [p=0.2] Com taxa ao mês, {e}quinze dias também."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}compare o prazo com um período da taxa. [p=0.3] {b}Igual a um, empate. [p=0.2] {c}Menor que um, ganham os simples. [p=0.2] {d}Maior que um, ganham os compostos."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o juro sobre juro só aparece depois do primeiro período. [p=0.3] Não compensa quando a pergunta é {b}quanto a mais, e não quem ganha. [p=0.2] Aí, {c}faça as contas."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma aplicação paga {a}doze por cento ao ano. [p=0.3] Quem rende mais, juros simples ou compostos: [p=0.2] {b}em seis meses? [p=0.2] {c}Em um ano? [p=0.2] {d}Em dois anos?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] A taxa é ao ano, então {a}o período é um ano. [p=0.3] {b}Seis meses é meio período: ganham os simples. [p=0.2] {c}Um ano é um período: empate. [p=0.2] {d}Dois anos passam de um período: ganham os compostos."),
    dict(id="s18", block="resposta", text="Com mil reais em dois anos: [p=0.2] nos simples, vinte e quatro por cento, {a}mil duzentos e quarenta. [p=0.2] Nos compostos, {b}um vírgula doze ao quadrado dá um vírgula dois cinco quatro quatro: [p=0.1] {c}mil duzentos e cinquenta e quatro reais e quarenta centavos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}em um período, empate. [p=0.2] {b}Antes, ganham os simples. [p=0.2] {c}Depois, ganham os compostos."),
    dict(id="s20", block="fim", text="Na próxima aula, a conta ao contrário: [p=0.2] {a}quanto aplicar hoje para ter mil duzentos e dez reais em dois anos, [p=0.2] e {b}em quanto tempo um dinheiro dobra nos juros compostos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
