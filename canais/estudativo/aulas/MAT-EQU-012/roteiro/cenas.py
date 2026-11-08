# Estudativo · MAT-EQU-012 — Praticando: equações do 1º grau (Matemática · Equações do 1º Grau · prática).
# Habilidade: resolver equações de todos os tipos e conferir a resposta substituindo.
# Pré-requisitos: MAT-EQU-007, MAT-EQU-008, MAT-EQU-009, MAT-EQU-010, MAT-EQU-011. Próxima: MAT-EQU-013.
# Questões inéditas, criadas para esta aula. Montar a equação a partir do texto ainda não foi ensinado (MAT-EQU-013).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: equações do 1º grau"

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
    dict(id="s01", block="gancho", text="{a}Cinco equações, criadas para esta aula, [p=0.2] uma de cada tipo que você viu. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] E no fim, {c}confira substituindo, como sempre."),
    # lembrete
    dict(id="s02", block="lembrete", text="A ferramenta é uma só: [p=0.2] {a}fazer o mesmo nos dois lados da balança. [p=0.2] Antes dela, às vezes, {b}abrir parênteses [p=0.2] ou {c}sumir com frações e vírgulas. [p=0.3] Se alguma travar, procure a aula no canal."),
    # equação 1: xis dos dois lados
    dict(id="s03", block="questao1", text="{a}Equação um. [p=0.2] {b}Xis mais treze igual a quatro xis menos oito. [p=0.3] {c}Quanto vale xis?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] O lado com mais xis é {a}o direito. [p=0.2] Então {b}tire xis de cada lado: treze igual a três xis menos oito. [p=0.3] {c}Some oito de cada lado: vinte e um igual a três xis. [p=0.2] {d}Divida por três: sete igual a xis, [p=0.1] que é o mesmo que {e}xis igual a sete."),
    dict(id="s06", block="resposta1", text="Conferindo: {a}sete mais treze dá vinte. [p=0.2] {b}Quatro vezes sete dá vinte e oito. [p=0.1] Menos oito dá vinte. [p=0.2] Bateu."),
    dict(id="s07", block="atalho", text="Aqui vale o atalho: {a}deixe o xis no lado que tem mais xis, mesmo que seja o direito. [p=0.3] Funciona porque {b}o número que multiplica a letra fica positivo. [p=0.2] Tirando quatro xis, você chegaria em {c}menos três xis, com um sinal a mais para cuidar. [p=0.2] {d}Não faz diferença quando o xis já está num lado só."),
    # equação 2: parênteses
    dict(id="s08", block="questao2", text="{a}Equação dois. [p=0.2] {b}Dois, abre parênteses, xis mais quatro, fecha parênteses, igual a cinco xis menos um. [p=0.3] {c}Quanto vale xis?"),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] {a}Abra os parênteses: dois xis mais oito. [p=0.2] O lado com mais xis é o direito: {b}tire dois xis de cada lado. [p=0.2] {c}Oito igual a três xis menos um. [p=0.2] {d}Some um: nove igual a três xis. [p=0.2] {e}Xis igual a três."),
    dict(id="s11", block="resposta2", text="Conferindo: {a}três mais quatro dá sete. [p=0.1] Vezes dois dá catorze. [p=0.2] {b}Cinco vezes três dá quinze. [p=0.1] Menos um dá catorze. Bateu. [p=0.3] E se o lado direito fosse {c}dois xis mais cinco? [p=0.2] O xis sumiria e sobraria {d}oito igual a cinco: [p=0.1] nenhum número serviria."),
    # equação 3: frações
    dict(id="s12", block="questao3", text="{a}Equação três. [p=0.2] {b}Xis sobre três menos dois igual a xis sobre cinco. [p=0.3] {c}Quanto vale xis?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] {a}MMC de três e cinco é quinze. [p=0.2] Multiplique cada termo por quinze, [p=0.1] até o número sem fração. [p=0.2] {b}Xis sobre três vira cinco xis. [p=0.2] {c}Menos dois vira menos trinta. [p=0.2] {d}Xis sobre cinco vira três xis."),
    dict(id="s15", block="resposta3", text="Fica {a}cinco xis menos trinta igual a três xis. [p=0.2] {b}Tire três xis de cada lado: dois xis menos trinta igual a zero. [p=0.2] {c}Some trinta: dois xis igual a trinta. [p=0.2] {d}Xis igual a quinze. [p=0.3] Conferindo: {e}quinze sobre três dá cinco. [p=0.1] Menos dois dá três. [p=0.2] {f}Quinze sobre cinco dá três. Bateu. [p=0.3] Quem esquece de multiplicar o dois chega em {g}xis igual a um, [p=0.2] que não confere: um terço menos dois {h}dá um número negativo, [p=0.1] e um quinto é positivo."),
    # equação 4: decimais
    dict(id="s16", block="questao4", text="{a}Equação quatro. [p=0.2] {b}Zero vírgula dois xis mais três igual a zero vírgula cinco xis. [p=0.3] {c}Quanto vale xis?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Nenhum número tem mais de uma casa depois da vírgula: {a}multiplique tudo por dez. [p=0.2] {b}Dois xis mais trinta igual a cinco xis. [p=0.3] {c}Tire dois xis de cada lado: trinta igual a três xis. [p=0.2] {d}Xis igual a dez. [p=0.3] Conferindo: {e}zero vírgula dois vezes dez dá dois. [p=0.1] Mais três dá cinco. [p=0.2] {f}Zero vírgula cinco vezes dez dá cinco. Bateu."),
    # equação 5: fórmula
    dict(id="s19", block="questao5", text="{a}Última, com fórmula. [p=0.2] Um ciclista pedala a {b}doze quilômetros por hora. [p=0.2] {c}Quanto tempo ele leva para percorrer dezoito quilômetros? [p=0.3] Use {d}a fórmula da aula passada: [p=0.1] distância igual a velocidade vezes tempo."),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Ponha o que você sabe: {a}dezoito igual a doze vezes o tempo. [p=0.2] {b}Divida cada lado por doze. [p=0.2] {c}Dezoito dividido por doze dá um vírgula cinco. [p=0.3] Conferindo: {d}doze vezes um vírgula cinco dá dezoito. Bateu."),
    dict(id="s22", block="resposta5", text="Cuidado na resposta: {a}um vírgula cinco hora é uma hora e meia. [p=0.2] A hora tem sessenta minutos, e não cem, [p=0.2] então meia hora são trinta minutos: {b}uma hora e trinta minutos, [p=0.2] {c}e não uma hora e cinquenta."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}arrume a equação, [p=0.2] {b}faça o mesmo nos dois lados [p=0.2] e {c}confira substituindo."),
    dict(id="s24", block="fim", text="Na próxima aula, a equação não vem pronta: [p=0.2] você vai {a}montar a equação a partir de um problema escrito. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
