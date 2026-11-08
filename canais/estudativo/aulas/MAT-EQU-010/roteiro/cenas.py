# Estudativo · MAT-EQU-010 — Equação com frações ou decimais (Matemática · Equações do 1º Grau).
# Habilidade: resolver x/2 + x/3 = 5 eliminando os denominadores com o MMC e 0,5x + 1,2 = 3.
# Pré-requisitos: MAT-DIV-005 (MMC), MAT-EQU-008 (letra dos dois lados), MAT-FRA-012, MAT-FRA-015, MAT-FRA-018. Próxima: MAT-EQU-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equação com frações ou decimais"

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
    dict(id="s01", block="gancho", text="{a}Xis sobre dois mais xis sobre três igual a cinco. [p=0.3] Fração dentro de equação assusta. [p=0.2] Mas existe um jeito de {b}fazer as frações sumirem num passo só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com frações e com vírgula, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}achar o MMC, [p=0.2] {c}andar com a vírgula ao multiplicar por dez [p=0.2] e {d}resolver equação com xis dos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # frações
    dict(id="s04", block="fracoes", text="Lembre que {a}xis sobre dois é xis dividido por dois. [p=0.3] A ideia é {b}multiplicar cada lado por um número que todos os denominadores dividem. [p=0.2] O melhor é {c}o MMC. [p=0.3] MMC de dois e três é {d}seis."),
    dict(id="s05", block="fracoes", text="Por que funciona? [p=0.2] Multiplicar um prato da balança por seis é {a}juntar seis cópias dele. [p=0.3] {b}Seis metades de xis dão três xis. [p=0.2] {c}Seis terços de xis dão dois xis. [p=0.2] E no outro prato, {d}seis vezes cinco dá trinta. [p=0.3] Os pratos cresceram {e}o mesmo tanto, então continuam equilibrados."),
    dict(id="s06", block="fracoes", text="Para fazer sem desenhar, use a frase das frações: [p=0.2] {a}divide pelo de baixo, multiplica pelo de cima. [p=0.3] {b}Seis dividido por dois dá três. [p=0.1] Vezes xis dá três xis. [p=0.2] {c}Seis dividido por três dá dois. [p=0.1] Vezes xis dá dois xis."),
    dict(id="s07", block="fracoes", text="Fica {a}três xis mais dois xis igual a trinta, [p=0.2] sem nenhuma fração. [p=0.3] {b}Juntando, cinco xis igual a trinta. [p=0.2] {c}Divida cada lado por cinco: xis igual a seis. [p=0.3] Conferindo: {d}seis sobre dois dá três. [p=0.1] Seis sobre três dá dois. [p=0.2] {e}Três mais dois dá cinco. Bateu."),
    # decimais
    dict(id="s08", block="decimais", text="Com vírgula, a ideia é a mesma. [p=0.2] Veja {a}zero vírgula cinco xis mais um vírgula dois igual a três. [p=0.3] Para sumir com a vírgula, {b}multiplique tudo por dez, [p=0.2] porque nenhum número tem mais de {c}uma casa depois da vírgula. [p=0.2] Com duas casas, seria por cem."),
    dict(id="s09", block="decimais", text="{a}Zero vírgula cinco xis vira cinco xis. [p=0.2] {b}Um vírgula dois vira doze. [p=0.2] E {c}o três também vai junto: trinta. [p=0.3] Fica {d}cinco xis mais doze igual a trinta."),
    dict(id="s10", block="decimais", text="{a}Subtraia doze de cada lado: cinco xis igual a dezoito. [p=0.2] {b}Divida por cinco: xis igual a três vírgula seis. [p=0.3] Conferindo: {c}zero vírgula cinco vezes três vírgula seis dá um vírgula oito. [p=0.2] {d}Mais um vírgula dois dá três. Bateu."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}multiplicar só as frações. [p=0.2] Na primeira equação, a pessoa escreve {b}três xis mais dois xis igual a cinco, [p=0.2] esquecendo de multiplicar o cinco. [p=0.3] E chega em {c}xis igual a um."),
    dict(id="s12", block="erro", text="Conferindo: {a}um meio mais um terço dá cinco sextos, [p=0.2] {b}e não cinco. [p=0.3] Se um prato vai vezes seis, o outro também vai, [p=0.2] e {c}cada termo é multiplicado, até o número sem fração."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para a vírgula: [p=0.2] {a}dividir por zero vírgula cinco é dobrar. [p=0.3] Na segunda equação, subtraia um vírgula dois de cada lado: [p=0.2] {b}zero vírgula cinco xis igual a um vírgula oito. [p=0.2] Para soltar o xis, divida por zero vírgula cinco, [p=0.1] ou seja, {c}dobre: xis igual a três vírgula seis."),
    dict(id="s14", block="atalho", text="Funciona porque {a}zero vírgula cinco cabe duas vezes em cada inteiro. [p=0.3] {b}Não compensa com números como zero vírgula três: [p=0.2] aí, {c}multiplique tudo por dez."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis sobre quatro mais um igual a xis sobre seis mais dois. [p=0.3] {b}Quanto vale xis?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}MMC de quatro e seis é doze. [p=0.2] Multiplique cada termo por doze. [p=0.2] {b}Doze dividido por quatro dá três: três xis. [p=0.2] {c}Um vezes doze dá doze. [p=0.2] {d}Doze dividido por seis dá dois: dois xis. [p=0.2] {e}Dois vezes doze dá vinte e quatro."),
    dict(id="s18", block="resposta", text="Fica {a}três xis mais doze igual a dois xis mais vinte e quatro. [p=0.2] {b}Tire dois xis de cada lado: [p=0.1] xis mais doze igual a vinte e quatro. [p=0.2] {c}Subtraia doze: xis igual a doze. [p=0.3] Conferindo: {d}doze sobre quatro dá três. [p=0.1] Mais um dá quatro. [p=0.2] {e}Doze sobre seis dá dois. [p=0.1] Mais dois dá quatro. Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}com fração, multiplique tudo pelo MMC. [p=0.2] {b}Com vírgula, multiplique tudo por dez, ou por cem se houver duas casas. [p=0.2] E {c}tudo quer dizer cada termo, nos dois lados."),
    dict(id="s20", block="fim", text="Na próxima aula, você usa a balança numa {a}fórmula com várias letras, [p=0.2] como a da {b}velocidade de um carro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
