# Estudativo · MAT-NUM-017 — Multiplicar e dividir inteiros: regra de sinais (Matemática · Números e Contas).
# Habilidade: calcular (−4) × (−3) e (−20) ÷ 4, entendendo a regra de sinais.
# Pré-requisitos: MAT-NUM-009 (dividir por um algarismo), MAT-NUM-016 (somar e subtrair inteiros). Próxima: MAT-NUM-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Multiplicar e dividir inteiros: regra de sinais"

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
    dict(id="s01", block="gancho", text="{a}Menos quatro vezes menos três dá {b}mais doze. [p=0.3] Mas como duas coisas negativas viram dinheiro no bolso? [p=0.3] Decorar não ajuda. [p=0.2] {c}Entender, sim."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você multiplica e divide com sinal sabendo o motivo, [p=0.2] e leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}a tabuada, [p=0.2] {c}a prova real da divisão, que é multiplicar de volta, [p=0.2] e {d}a ideia de que tirar uma dívida é como ganhar. [p=0.3] Se faltar alguma, procure no canal."),
    # casos
    dict(id="s04", block="casos", text="Multiplicar é repetir. [p=0.2] {a}Menos quatro vezes três é repetir três vezes uma dívida de quatro reais. [p=0.3] {b}Uma dívida de quatro, mais outra, mais outra. [p=0.2] Você passa a dever doze: {c}menos doze. [p=0.3] Trocar a ordem não muda nada: {d}três vezes menos quatro também dá menos doze."),
    dict(id="s05", block="casos", text="E se o número que diz quantas vezes for negativo? [p=0.2] O sinal de menos {a}inverte a ação: [p=0.2] em vez de pôr, você tira. [p=0.3] {b}Quatro vezes menos três: [p=0.2] você tira quatro reais do bolso, três vezes. [p=0.2] Perdeu doze: {c}menos doze."),
    dict(id="s06", block="casos", text="E se o que você tira é dívida? [p=0.2] Você tem {a}cinco dívidas de quatro reais. [p=0.2] Saldo: {b}menos vinte. [p=0.3] A loja {c}cancela três dessas dívidas. [p=0.2] Sobram duas dívidas: {d}saldo de menos oito."),
    dict(id="s07", block="casos", text="De menos vinte para menos oito, [p=0.2] seu saldo {a}subiu doze. [p=0.2] Confira: {b}menos vinte mais doze dá menos oito. [p=0.3] Essa é a conta {c}menos quatro vezes menos três. [p=0.2] Menos quatro é a dívida. [p=0.2] Vezes menos três é tirar três delas. [p=0.3] Resultado: {d}mais doze. [p=0.2] Tirar uma dívida é como ganhar."),
    dict(id="s08", block="casos", text="Juntando tudo: [p=0.2] {a}mais vezes mais dá mais. [p=0.2] {b}Menos vezes menos dá mais. [p=0.2] {c}Mais vezes menos dá menos. [p=0.2] {d}Menos vezes mais dá menos. [p=0.3] Em uma frase: {e}multiplicando ou dividindo, sinais iguais dão mais, e sinais diferentes dão menos."),
    dict(id="s09", block="casos", text="Na prática, são {a}dois passos: [p=0.2] primeiro o sinal, depois a conta. [p=0.3] {b}Menos seis vezes sete. [p=0.2] Sinais diferentes: {c}o resultado é negativo. [p=0.2] {d}Seis vezes sete dá quarenta e dois. [p=0.2] Resposta: {e}menos quarenta e dois."),
    # dividir
    dict(id="s10", block="dividir", text="Dividir segue a mesma regra. [p=0.2] {a}Menos vinte dividido por quatro é uma dívida de vinte reais {b}repartida igualmente entre quatro pessoas. [p=0.2] Cada uma deve cinco: {c}menos cinco. [p=0.3] Prova real: {d}quatro vezes menos cinco dá menos vinte. [p=0.3] Com mais cinco, a prova não fecharia: quatro vezes cinco dá vinte positivo."),
    dict(id="s11", block="dividir", text="E {a}menos vinte dividido por menos quatro? [p=0.2] A pergunta é: {b}quantas dívidas de quatro cabem em uma dívida de vinte? [p=0.3] Cabem cinco. [p=0.2] Sinais iguais: {c}mais cinco. [p=0.3] Prova real: {d}cinco vezes menos quatro dá menos vinte."),
    dict(id="s12", block="dividir", text="E {a}vinte dividido por menos quatro? [p=0.2] Sinais diferentes: {b}menos cinco. [p=0.3] Prova real: {c}menos quatro vezes menos cinco dá vinte."),
    # erro
    dict(id="s13", block="erro", text="Cuidado: {a}essa regra é só para vezes e dividido. [p=0.3] Muita gente repete menos com menos dá mais {b}na conta de menos quatro menos três. [p=0.3] Aí não tem vezes. [p=0.2] É uma dívida de quatro e {c}mais uma dívida de três. [p=0.2] Você deve sete: {d}menos sete. [p=0.3] Já em {e}três menos, abre parênteses, menos cinco, fecha parênteses, vira mais por outro motivo: [p=0.2] ali você tira uma dívida, como já viu."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}conte os sinais de menos. [p=0.3] Em {b}menos dois vezes menos cinco vezes menos um, [p=0.2] são {c}três sinais. [p=0.2] Contagem ímpar, como três ou cinco, {d}resultado negativo. [p=0.2] Contagem par, como dois ou quatro, positivo. [p=0.3] Sem os sinais, {e}a conta dá dez. [p=0.2] Resposta: {f}menos dez."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada dupla de menos vira mais. [p=0.2] Na contagem ímpar, {b}sobra um menos sem dupla. [p=0.3] {c}Só vale se a conta inteira for vezes e dividido. [p=0.2] E com dois números, não compensa: [p=0.2] é a própria regra."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Seu saldo é {a}menos quarenta e dois reais: [p=0.2] uma dívida dividida em {b}seis parcelas iguais. [p=0.3] A loja {c}cancela duas parcelas. [p=0.3] {d}Qual é o novo saldo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Cada parcela: {a}menos quarenta e dois dividido por seis dá menos sete. [p=0.3] Cancelar duas é {b}menos sete vezes menos dois. [p=0.2] Sinais iguais: {c}mais catorze."),
    dict(id="s19", block="resposta", text="Novo saldo: {a}menos quarenta e dois mais catorze [p=0.2] dá {b}menos vinte e oito. [p=0.3] Confira: sobraram {c}quatro parcelas de sete reais, [p=0.2] que são vinte e oito reais de dívida."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}sinais iguais, mais. [p=0.2] {b}Sinais diferentes, menos. [p=0.2] E {c}a regra é de vezes e dividido. [p=0.2] Com mais e menos, pense em dívida."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}junta tudo em uma conta só: [p=0.2] {b}negativos e parênteses [p=0.2] na {c}ordem certa das operações. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
