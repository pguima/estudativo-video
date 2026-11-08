# Estudativo · MAT-FUN-003 — Notação f(x): calcular e fazer o caminho de volta (Matemática · Funções · O que é função).
# Habilidade: calcular f(5) em f(x) = 2x + 3 e achar o x que faz f(x) = 30, sem trocar uma pergunta pela outra.
# Pré-requisitos: MAT-FUN-002 (entrada e saída), MAT-EQU-010 (equação com decimais). Próxima: MAT-FUN-004.
# Questão inédita, criada para esta aula, com o táxi da MAT-FUN-002 (P = 5 + 2,5d).
# Contas: f(5) = 2 × 5 + 3 = 13 · f(−2) = −4 + 3 = −1 · f(x) = 30 → 2x = 27 → x = 13,5; 2 × 13,5 + 3 = 30 · erro: 2 × 30 + 3 = 63 = f(30).
# Atalho (desfazer de trás para a frente): 30 − 3 = 27; 27 ÷ 2 = 13,5.
# Questão: P(8) = 5 + 20 = 25 · P(d) = 40 → 40 − 5 = 35; 35 ÷ 2,5 = 350 ÷ 25 = 14; 2,5 × 14 = 35.
# Visual: f(x) = 2x + 3 com "nome", "entrada" e "saída" apontados; máquina com entrada e saída; f(5) = 13 e f(13,5) = 30 lado a lado;
#   regra "dentro dos parênteses: calcule / depois do igual: resolva"; setas de ida (×2, +3) e de volta (−3, ÷2).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; f(x) narrado "efe de xis".

TITULO = "Notação f(x): calcular e fazer o caminho de volta"

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
    dict(id="s01", block="gancho", text="Na função {a}efe de xis igual a dois xis mais três dá [p=0.2] duas perguntas. [p=0.2] {b}Quanto vale efe de cinco? [p=0.2] E {c}qual xis faz efe de xis dar trinta? [p=0.3] Parecem iguais, mas {d}uma pede a saída e a outra pede a entrada. [p=0.2] Quem confunde responde {e}sessenta e três, e erra."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você responde as duas sem trocar uma pela outra, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}função, em que cada entrada tem uma saída só, [p=0.2] e {c}resolver equação, inclusive com resposta decimal. [p=0.3] Se faltar alguma, procure no canal."),
    # notação
    dict(id="s04", block="notacao", text="As provas escrevem função assim: [p=0.2] {a}efe de xis igual a dois xis mais três. [p=0.3] {b}Efe é o nome da função, [p=0.2] como o nome de uma máquina. [p=0.2] {c}O que vai nos parênteses é a entrada. [p=0.2] E efe de xis, tudo junto, é {d}a saída: o que a máquina devolve quando entra xis."),
    dict(id="s05", block="notacao", text="Esta máquina {a}multiplica a entrada por dois [p=0.2] e depois {b}soma três. [p=0.3] E atenção: {c}efe de xis não é efe vezes xis. [p=0.2] Aqui, o parêntese {d}não é multiplicação: [p=0.2] ele mostra o que entra."),
    # pergunta um
    dict(id="s06", block="calcular", text="Pergunta um: {a}efe de cinco. [p=0.2] O cinco está {b}dentro dos parênteses, no lugar do xis: [p=0.2] ele é a entrada. [p=0.3] Então troque o xis pelo cinco, com parênteses: [p=0.2] {c}dois vezes cinco mais três. [p=0.2] {d}Dez mais três dá treze. [p=0.3] Escreve-se {e}efe de cinco igual a treze: [p=0.2] entra cinco, sai treze."),
    dict(id="s07", block="calcular", text="Com negativo, o cuidado é o de sempre. [p=0.2] {a}Efe de menos dois: [p=0.2] {b}dois vezes, abre parênteses, menos dois, fecha parênteses, mais três. [p=0.2] {c}Menos quatro mais três dá menos um. [p=0.2] {d}Efe de menos dois é igual a menos um."),
    # pergunta dois
    dict(id="s08", block="volta", text="Pergunta dois: {a}efe de xis igual a trinta. [p=0.2] Agora o trinta está {b}depois do igual, no lugar da saída. [p=0.3] Você já sabe o que saiu da máquina. [p=0.2] {c}Falta descobrir o que entrou. [p=0.3] Isso é uma {d}equação: dois xis mais três igual a trinta."),
    dict(id="s09", block="volta", text="{a}Tire três de cada lado: dois xis igual a vinte e sete. [p=0.2] {b}Divida cada lado por dois: xis igual a treze vírgula cinco. [p=0.3] Conferindo: {c}dois vezes treze vírgula cinco dá vinte e sete. [p=0.2] {d}Mais três dá trinta. Bateu. [p=0.3] Então {e}efe de treze vírgula cinco é igual a trinta."),
    dict(id="s10", block="volta", text="Quem decide a pergunta é {a}o lugar do número. [p=0.3] {b}Número dentro dos parênteses é entrada: troque e calcule. [p=0.2] {c}Número depois do igual é saída: monte a equação e resolva."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}ver o trinta e trocar o xis por ele. [p=0.2] A pessoa faz {b}dois vezes trinta mais três, e chega em sessenta e três. [p=0.3] Mas isso é {c}efe de trinta: [p=0.2] o que sai quando o trinta entra. [p=0.2] A pergunta dava {d}a saída, e não a entrada. [p=0.3] Confira sempre: {e}a sua resposta, posta na função, tem que devolver o trinta."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho para o caminho de volta: [p=0.2] {a}desfaça as contas de trás para a frente. [p=0.3] A máquina {b}multiplica por dois e depois soma três. [p=0.2] Para voltar, {c}primeiro tire três: vinte e sete. [p=0.2] {d}Depois divida por dois: treze vírgula cinco."),
    dict(id="s13", block="atalho", text="Funciona como {a}tirar o sapato antes da meia: [p=0.2] o que foi feito por último se desfaz primeiro. [p=0.3] {b}Não compensa quando o xis aparece em mais de um lugar da fórmula. [p=0.2] Aí, {c}monte a equação e resolva pela balança."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar, com o táxi: [p=0.2] {a}pê de dê igual a cinco mais dois vírgula cinco dê, [p=0.2] o preço de uma corrida de dê quilômetros. [p=0.3] {b}Quanto vale pê de oito? [p=0.2] {c}E se uma corrida custou quarenta reais, quantos quilômetros ela teve?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] O oito está nos parênteses: {a}é entrada. [p=0.2] {b}Dois vírgula cinco vezes oito dá vinte. [p=0.2] {c}Mais cinco dá vinte e cinco reais. [p=0.3] {d}Pê de oito é igual a vinte e cinco."),
    dict(id="s17", block="resposta", text="Os quarenta reais são {a}o preço, a saída. [p=0.2] Caminho de volta: {b}tire os cinco fixos e fica trinta e cinco. [p=0.2] {c}Divida por dois vírgula cinco. [p=0.2] Multiplique cada número por dez: [p=0.2] trezentos e cinquenta dividido por vinte e cinco dá {d}catorze quilômetros. [p=0.3] Conferindo: {e}dois vírgula cinco vezes catorze dá trinta e cinco. [p=0.2] Mais cinco dá quarenta. Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}número nos parênteses, calcule. [p=0.2] {b}Número depois do igual, resolva a equação. [p=0.2] E {c}confira devolvendo a resposta à função."),
    dict(id="s19", block="fim", text="Na próxima aula, você descobre {a}quais números podem entrar numa função [p=0.2] e quais saem dela: [p=0.2] {b}domínio, contradomínio e imagem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
