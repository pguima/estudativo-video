# Estudativo · MAT-PLN-003 — Dispositivo de Briot-Ruffini (Matemática · Polinômios · Operações e divisão de polinômios).
# Habilidade: dividir x³ − 2x² − 5x + 6 por x − 1 só com os coeficientes e achar o quociente x² − x − 6 e o resto 0.
# Pré-requisitos: MAT-PLN-002 (método da chave, teorema do resto). Próxima: MAT-PLN-004.
# Nome falado "Briô-Rufíni" (na tela, Briot-Ruffini). Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; a letra a se fala "á".

TITULO = "Dispositivo de Briot-Ruffini"

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
    dict(id="s01", block="gancho", text="{a}Xis ao cubo menos dois xis ao quadrado menos cinco xis mais seis, dividido por xis menos um. [p=0.3] Pela chave, são {b}três rodadas de dividir, multiplicar e subtrair. [p=0.3] Com {c}uma tabelinha que usa só os coeficientes, [p=0.2] sai em vinte segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você divide por xis menos um número usando só os coeficientes: [p=0.2] é o {b}dispositivo de Briô-Rufíni, uma tabelinha que faz a divisão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}na divisão, o polinômio é o divisor vezes o quociente, mais o resto, [p=0.2] e {c}o teorema do resto: o resto da divisão por xis menos á é P de á. [p=0.3] Se faltar alguma, procure no canal."),
    # montar
    dict(id="s04", block="montar", text="Monte assim. [p=0.2] {a}À esquerda, o número que zera o divisor. [p=0.2] Para xis menos um, {b}é o um. [p=0.3] {c}À direita, os coeficientes, do maior expoente para o menor: [p=0.2] {d}um, menos dois, menos cinco e seis."),
    # a regra
    dict(id="s05", block="regra", text="A regra tem duas partes: [p=0.2] {a}baixe o primeiro, [p=0.2] e depois {b}multiplique pelo número da esquerda e some com o próximo."),
    dict(id="s06", block="regra", text="{a}Baixe o um. [p=0.2] {b}Um vezes um, um. Mais menos dois: menos um. [p=0.3] {c}Menos um vezes um, menos um. Mais menos cinco: menos seis. [p=0.3] {d}Menos seis vezes um, menos seis. Mais seis: zero."),
    # ler o resultado
    dict(id="s07", block="ler", text="Agora leia a última linha. [p=0.2] {a}O último número é o resto: zero. [p=0.2] {b}Os outros são os coeficientes do quociente, [p=0.2] com grau {c}um a menos que o dividendo. [p=0.3] O dividendo tinha grau três, então {d}o quociente é xis ao quadrado menos xis menos seis."),
    dict(id="s08", block="ler", text="Confira pelo teorema do resto: [p=0.2] {a}P de um é um menos dois menos cinco mais seis: zero. [p=0.2] {b}Bateu com a tabela."),
    # termo que falta
    dict(id="s09", block="falta", text="E quando falta um termo? [p=0.2] Divida {a}xis ao cubo menos quatro xis mais cinco por xis mais dois. [p=0.3] {b}Xis mais dois zera com menos dois. [p=0.2] Não tem xis ao quadrado: {c}o coeficiente dele é zero, e o zero entra na tabela. [p=0.2] {d}Um, zero, menos quatro, cinco."),
    dict(id="s10", block="falta", text="{a}Baixe o um. [p=0.2] {b}Um vezes menos dois, menos dois. Mais zero: menos dois. [p=0.3] {c}Menos dois vezes menos dois, quatro. Mais menos quatro: zero. [p=0.3] {d}Zero vezes menos dois, zero. Mais cinco: cinco."),
    dict(id="s11", block="falta", text="Quociente: {a}xis ao quadrado menos dois xis mais zero, [p=0.2] ou seja, {b}xis ao quadrado menos dois xis. [p=0.2] {c}Resto cinco."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é justamente {a}pular o zero do termo que falta. [p=0.2] Com {b}um, menos quatro e cinco, [p=0.2] a tabela dá {c}resto dezessete. [p=0.3] Mas {d}P de menos dois é menos oito mais oito mais cinco: cinco. [p=0.2] {e}Termo que falta entra com zero, sempre."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}o último número da tabela é P do número da esquerda. [p=0.2] Então a mesma tabela {b}calcula o valor de um polinômio, [p=0.2] só com vezes e mais, sem potência. [p=0.3] {c}P de três, no polinômio do começo: [p=0.2] {d}baixe o um; [p=0.2] um vezes três, mais menos dois, um; [p=0.2] um vezes três, mais menos cinco, menos dois; [p=0.2] menos dois vezes três, mais seis, {e}zero."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o resto da divisão por xis menos três é P de três. [p=0.3] {b}Não serve para divisor como dois xis menos um, com número na frente do xis: [p=0.2] aí, use a chave."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Divida {a}dois xis ao cubo menos três xis mais um [p=0.2] por {b}xis menos um."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}À esquerda, o um. [p=0.2] Falta o xis ao quadrado: {b}dois, zero, menos três, um. [p=0.3] {c}Baixe o dois. [p=0.2] {d}Dois vezes um, mais zero: dois. [p=0.2] {e}Dois vezes um, mais menos três: menos um. [p=0.2] {f}Menos um vezes um, mais um: zero."),
    dict(id="s18", block="resposta", text="Quociente: {a}dois xis ao quadrado mais dois xis menos um. [p=0.2] {b}Resto zero: a divisão é exata. [p=0.3] Conferindo: {c}P de um é dois menos três mais um, zero. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o número que zera o divisor à esquerda, [p=0.2] {b}os coeficientes com zero no que falta, [p=0.2] e {c}baixe, multiplique e some."),
    dict(id="s20", block="fim", text="Na próxima aula, esse resto zero vira ferramenta: [p=0.2] você usa {a}uma raiz conhecida para quebrar o polinômio em pedaços, [p=0.2] como {b}xis menos um, vezes xis menos três, vezes xis mais dois. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
