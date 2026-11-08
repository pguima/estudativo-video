# Estudativo · MAT-FAT-007 — Equação do 2º grau incompleta (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: apontar a, b e c em 2x² − 3x + 1 = 0 e resolver x² − 49 = 0 e x² − 5x = 0 sem fórmula, sem perder a raiz negativa nem o x = 0.
# Pré-requisitos: MAT-EQU-008 (balança), MAT-FAT-003 (diferença de dois quadrados), MAT-POT-007 (raiz quadrada). Próxima: MAT-FAT-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Equação do 2º grau incompleta"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado igual a quarenta e nove. [p=0.3] Quase todo mundo responde {b}sete. [p=0.2] Está certo, mas falta {c}metade da resposta. [p=0.3] {d}Menos sete, ao quadrado, também dá quarenta e nove."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com xis ao quadrado sem fórmula nenhuma, [p=0.2] sem perder {b}a raiz negativa [p=0.2] nem {c}o xis igual a zero."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}a balança, fazer o mesmo nos dois lados, [p=0.2] {c}a raiz quadrada [p=0.2] e {d}fatorar, colocando em evidência ou usando a diferença de dois quadrados. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="forma", text="Nas equações que você resolveu até aqui, o xis aparecia sem expoente. [p=0.2] Quando {a}o maior expoente do xis é dois, [p=0.2] a equação é {b}do segundo grau. [p=0.3] Toda equação do segundo grau pode ser arrumada assim: [p=0.2] {c}á xis ao quadrado, mais bê xis, mais cê, igual a zero."),
    dict(id="s05", block="forma", text="As letras á, bê e cê são {a}os coeficientes: os números que acompanham cada termo. [p=0.2] {b}O á multiplica o xis ao quadrado. [p=0.2] {c}O bê multiplica o xis. [p=0.2] {d}O cê é o número sozinho, sem xis."),
    dict(id="s06", block="forma", text="Em {a}dois xis ao quadrado menos três xis mais um igual a zero: [p=0.2] {b}á vale dois, [p=0.2] {c}bê vale menos três, com o sinal junto, [p=0.2] e {d}cê vale um. [p=0.3] O á {e}nunca é zero: sem xis ao quadrado, a equação não é do segundo grau."),
    dict(id="s07", block="forma", text="Quando {a}bê ou cê vale zero, falta um termo, [p=0.2] e a equação é {b}incompleta. [p=0.2] Essas se resolvem sem fórmula. [p=0.3] Um nome: as soluções de uma equação também se chamam {c}raízes. [p=0.2] Aqui, raiz quer dizer solução, e não raiz quadrada."),
    # caso sem bê
    dict(id="s08", block="semb", text="{a}Primeiro caso: sem o termo com xis. [p=0.2] {b}Xis ao quadrado menos quarenta e nove igual a zero. [p=0.3] Na balança, {c}some quarenta e nove em cada lado: [p=0.2] {d}xis ao quadrado igual a quarenta e nove."),
    dict(id="s09", block="semb", text="A pergunta é: {a}que número, vezes ele mesmo, dá quarenta e nove? [p=0.2] {b}Sete serve. [p=0.2] {c}Menos sete também, porque sinais iguais dão mais. [p=0.3] O símbolo da raiz escolhe só o positivo, [p=0.2] mas a equação pede {d}todos os números que servem: [p=0.2] {e}xis igual a sete ou xis igual a menos sete."),
    dict(id="s10", block="semb", text="Fatorando, dá o mesmo. [p=0.2] Pela diferença de dois quadrados, {a}xis mais sete, vezes xis menos sete, igual a zero. [p=0.3] E aqui entra a ideia que resolve o resto da aula: [p=0.2] {b}se uma multiplicação dá zero, algum fator vale zero. [p=0.2] Nenhum número diferente de zero, vezes outro diferente de zero, dá zero."),
    dict(id="s11", block="semb", text="{a}Xis mais sete igual a zero dá menos sete. [p=0.2] {b}Xis menos sete igual a zero dá sete. [p=0.3] As mesmas {c}duas raízes."),
    # caso sem cê
    dict(id="s12", block="semc", text="{a}Segundo caso: sem o número sozinho. [p=0.2] {b}Xis ao quadrado menos cinco xis igual a zero. [p=0.3] {c}O xis está nos dois termos: coloque em evidência. [p=0.2] {d}Xis, vezes o parêntese xis menos cinco, igual a zero."),
    dict(id="s13", block="semc", text="Uma multiplicação deu zero, então {a}algum fator vale zero. [p=0.2] Ou {b}xis igual a zero, [p=0.2] ou {c}xis menos cinco igual a zero, que dá xis igual a cinco. [p=0.3] Conferindo o cinco: {d}vinte e cinco menos vinte e cinco dá zero. [p=0.2] E o zero: {e}zero menos zero dá zero. [p=0.2] Bateu."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum aparece no segundo caso: [p=0.2] {a}dividir os dois lados por xis. [p=0.2] Sobra {b}xis menos cinco igual a zero, e só o cinco. [p=0.3] {c}O zero sumiu. [p=0.2] Dividir por xis é dividir por um número que pode ser zero, [p=0.2] e {d}divisão por zero não existe. [p=0.3] Por isso, {e}coloque o xis em evidência, e nunca divida por ele."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho. [p=0.2] {a}Sem o número sozinho, uma raiz é sempre zero. [p=0.2] A outra é {b}menos bê dividido por á. [p=0.3] Em {c}três xis ao quadrado mais doze xis igual a zero: [p=0.2] {d}zero, e menos doze dividido por três, que dá menos quatro."),
    dict(id="s16", block="atalho", text="Funciona porque, com o xis em evidência, {a}sobra á xis mais bê dentro do parêntese, [p=0.2] e esse parêntese zera quando {b}xis vale menos bê dividido por á. [p=0.3] {c}Só vale com cê igual a zero. [p=0.2] Com {d}os três termos, a equação é completa, e o caminho é outro."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Resolva as duas: [p=0.2] {a}dois xis ao quadrado menos setenta e dois igual a zero, [p=0.2] e {b}xis ao quadrado igual a seis xis."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Na primeira, {a}some setenta e dois em cada lado: dois xis ao quadrado igual a setenta e dois. [p=0.2] {b}Divida cada lado por dois: xis ao quadrado igual a trinta e seis. [p=0.2] {c}Xis igual a seis ou xis igual a menos seis."),
    dict(id="s20", block="resposta", text="Na segunda, {a}leve tudo para um lado: xis ao quadrado menos seis xis igual a zero. [p=0.2] {b}Xis em evidência: xis, vezes o parêntese xis menos seis. [p=0.2] {c}Xis igual a zero ou xis igual a seis. [p=0.3] Quem dividiu por xis {d}perdeu o zero."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}sem bê, isole o xis ao quadrado e pegue as duas raízes. [p=0.2] {b}Sem cê, coloque o xis em evidência, e uma raiz é zero."),
    dict(id="s22", block="fim", text="Na próxima aula, a equação vem {a}completa, com os três termos, [p=0.2] como {b}xis ao quadrado menos cinco xis mais seis igual a zero, [p=0.2] e você aprende {c}a fórmula de Bhaskara. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
