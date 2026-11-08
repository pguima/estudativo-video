# Estudativo · MAT-PLN-009 — Raízes complexas vêm em pares (Matemática · Polinômios · Raízes complexas).
# Habilidade: saber que, se 1 + 2i é raiz de x³ − 3x² + 7x − 5, então 1 − 2i também é, e achar a terceira raiz, 1.
# Pré-requisitos: MAT-PLN-004 (forma fatorada, grau n dá n raízes), MAT-PLN-008 (número i, conjugado). Próxima: MAT-PLN-010.
# Girard (MAT-PLN-006) e soma e produto (MAT-FAT-011) não estão na ficha: a terceira raiz sai da divisão pela chave (MAT-PLN-002),
# com o teste do um (P(1) = soma dos coeficientes, MAT-PLN-004) como conferência. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o número i se escreve "í".

TITULO = "Raízes complexas vêm em pares"

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
    dict(id="s01", block="gancho", text="{a}Um mais dois í é raiz de xis ao cubo menos três xis ao quadrado mais sete xis menos cinco. [p=0.3] Sem fazer conta nenhuma, você já sabe {b}outra raiz: um menos dois í. [p=0.3] E a terceira sai {c}em poucos passos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa o par de uma raiz complexa para achar todas as raízes, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}o conjugado: o de dois mais três í é dois menos três í; [p=0.2] {c}a forma fatorada, com um parêntese por raiz; [p=0.2] e {d}a divisão de polinômios pela chave. [p=0.3] Se faltar alguma, procure no canal."),
    # o par
    dict(id="s04", block="par", text="Na aula passada, {a}dois mais três í e dois menos três í saíram juntos da mesma equação. [p=0.2] Não foi sorte: [p=0.2] {b}o mais ou menos da fórmula sempre entrega o par. [p=0.3] E isso vale em qualquer grau: [p=0.2] {c}se um complexo é raiz, [p=0.2] {d}o conjugado dele também é."),
    dict(id="s05", block="par", text="Por quê? [p=0.2] {a}Trocar í por menos í não muda nenhum número real, [p=0.2] e {b}menos í, ao quadrado, também dá menos um. [p=0.3] Então, se a conta com {c}um mais dois í dá zero, [p=0.2] a mesma conta com {d}um menos dois í também dá. [p=0.3] Só tem uma condição: {e}os coeficientes do polinômio precisam ser reais."),
    dict(id="s06", block="par", text="Uma consequência: {a}grau três tem três raízes, [p=0.2] e as que têm í vêm {b}de duas em duas. [p=0.3] Então {c}todo polinômio de grau três com coeficientes reais tem pelo menos uma raiz real."),
    # a terceira raiz
    dict(id="s07", block="terceira", text="Falta a terceira raiz. [p=0.2] O par vira {a}dois parênteses: [p=0.2] {b}xis menos, abre parênteses, um mais dois í, fecha parênteses, [p=0.2] vezes {c}xis menos, abre parênteses, um menos dois í, fecha parênteses."),
    dict(id="s08", block="terceira", text="Junte {a}xis menos um em cada parêntese: [p=0.2] fica {b}xis menos um, menos dois í, vezes xis menos um, mais dois í. [p=0.3] É soma vezes diferença: [p=0.2] {c}xis menos um, ao quadrado, menos, abre parênteses, dois í, fecha parênteses, ao quadrado."),
    dict(id="s09", block="terceira", text="{a}Xis menos um, ao quadrado: xis ao quadrado menos dois xis mais um. [p=0.2] {b}Dois í, ao quadrado: quatro vezes menos um, menos quatro. [p=0.2] {c}Tirar menos quatro é somar quatro: [p=0.2] {d}xis ao quadrado menos dois xis mais cinco. [p=0.3] O í sumiu: {e}o par sempre dá coeficientes reais."),
    dict(id="s10", block="terceira", text="Divida o polinômio por esse pedaço, pela chave. [p=0.2] {a}Xis ao cubo dividido por xis ao quadrado: xis. [p=0.2] {b}Xis vezes o divisor: xis ao cubo menos dois xis ao quadrado mais cinco xis. [p=0.2] {c}Trocando os sinais e somando, fica menos xis ao quadrado mais dois xis menos cinco."),
    dict(id="s11", block="terceira", text="{a}Menos xis ao quadrado dividido por xis ao quadrado: menos um. [p=0.2] {b}Menos um vezes o divisor: menos xis ao quadrado mais dois xis menos cinco. [p=0.2] {c}Subtraindo: resto zero. [p=0.3] Quociente {d}xis menos um: [p=0.2] a terceira raiz é {e}um."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}trocar o sinal errado no conjugado. [p=0.2] O par de um mais dois í {b}não é menos um menos dois í. [p=0.3] {c}A parte real fica igual, e só o sinal do í muda: [p=0.2] {d}um menos dois í."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}o par já sai pronto, sem abrir parênteses. [p=0.3] Para {b}um mais ou menos dois í: [p=0.2] {c}o termo do meio é menos duas vezes a parte real, vezes xis: menos dois xis. [p=0.2] {d}O número sozinho é a parte real ao quadrado, mais o quadrado do número que acompanha o í: um mais quatro, cinco. [p=0.3] {e}Xis ao quadrado menos dois xis mais cinco."),
    dict(id="s14", block="atalho", text="Funciona porque {a}é a mesma conta que você acabou de fazer, para qualquer par. [p=0.3] E antes de dividir, {b}teste o um: [p=0.2] aqui, {c}um menos três mais sete menos cinco dá zero. [p=0.2] {d}O um é raiz, e a divisão só confirma. [p=0.2] Se o um não fosse raiz, a divisão pelo par seria o caminho."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Dois í é raiz de xis ao cubo menos xis ao quadrado mais quatro xis menos quatro. [p=0.2] {b}Ache as outras duas raízes."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Dois í é zero mais dois í: o conjugado é menos dois í. [p=0.3] Pelo atalho, {b}o termo do meio é menos duas vezes zero: desaparece. [p=0.2] {c}O número sozinho é zero mais quatro, quatro. [p=0.2] O par vira {d}xis ao quadrado mais quatro."),
    dict(id="s18", block="resposta", text="Na chave: {a}xis ao cubo dividido por xis ao quadrado, xis. [p=0.2] {b}Xis vezes xis ao quadrado mais quatro: xis ao cubo mais quatro xis. [p=0.2] Sobra {c}menos xis ao quadrado menos quatro: [p=0.2] {d}menos um vezes o divisor, resto zero. [p=0.3] Quociente xis menos um. [p=0.2] Raízes: {e}dois í, menos dois í e um."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}com coeficientes reais, raiz complexa vem com o conjugado, [p=0.2] {b}o par vira um fator de grau dois, [p=0.2] e {c}a divisão entrega as outras raízes."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica raízes reais e complexas juntas, [p=0.2] {b}em questões no estilo das provas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
