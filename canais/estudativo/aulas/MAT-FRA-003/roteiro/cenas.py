# Estudativo · MAT-FRA-003 — Frações equivalentes e simplificação (Matemática · Frações e Decimais).
# Habilidade: mostrar que 1/2, 2/4 e 3/6 são a mesma quantidade e reduzir 18/24 a 3/4 dividindo pelo MDC.
# Pré-requisitos: MAT-DIV-002, MAT-DIV-004, MAT-FRA-001. Próxima: MAT-FRA-004.

TITULO = "Frações equivalentes e simplificação"

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
    dict(id="s01", block="gancho", text="{a}Dezoito vinte e quatro avos. [p=0.3] Parece uma fração difícil, né? [p=0.3] Mas é só {b}três quartos disfarçados."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}descobrir quando duas frações valem a mesma coisa, [p=0.2] {b}deixar qualquer fração na forma mais simples, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}saber o que é uma fração, [p=0.2] {c}as regras de divisibilidade [p=0.2] e {d}o MDC. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # equivalentes
    dict(id="s04", block="barras", text="Olhe {a}esta barra, dividida em dois pedaços iguais. [p=0.2] Pintamos {b}um deles: [p=0.2] {c}um meio."),
    dict(id="s05", block="barras", text="Agora, vamos {a}cortar cada pedaço em dois. [p=0.3] A barra tem {b}quatro pedaços, [p=0.2] e {c}dois estão pintados: [p=0.2] {d}dois quartos."),
    dict(id="s06", block="barras", text="Agora, volte para a barra de dois pedaços e corte cada um em três. [p=0.3] {a}Seis pedaços, [p=0.2] {b}três pintados: [p=0.2] {c}três sextos."),
    dict(id="s07", block="barras", text="O que mudou na parte pintada? [p=0.3] {a}Nada. [p=0.3] Um meio, dois quartos e três sextos são {b}a mesma quantidade, com nomes diferentes. [p=0.3] Frações assim se chamam {c}equivalentes."),
    # regra
    dict(id="s08", block="regra", text="E a regra aparece na hora. [p=0.2] Cortar cada pedaço em dois {a}multiplica por dois o total de pedaços [p=0.2] e {b}também os pintados. [p=0.3] Então: {c}multiplique em cima e embaixo pelo mesmo número."),
    dict(id="s09", block="regra", text="Vamos usar isso. [p=0.2] {a}Três quintos é igual a quantos vinte avos? [p=0.3] Do cinco para o vinte, {b}multiplicou por quatro. [p=0.2] Faça o mesmo em cima: {c}três vezes quatro, doze. [p=0.2] {d}Doze vinte avos."),
    # simplificar
    dict(id="s10", block="simplificar", text="Simplificar é o caminho de volta: {a}dividir em cima e embaixo pelo mesmo número. [p=0.3] Veja {b}seis oitavos. [p=0.2] Seis e oito são pares, então {c}divida por dois. [p=0.2] {d}Três quartos."),
    dict(id="s11", block="simplificar", text="Quando parar? [p=0.2] Quando {a}só o número um dividir o de cima e o de baixo. [p=0.3] Em três quartos, só o número um divide o três e o quatro. [p=0.2] Essa fração não simplifica mais. [p=0.2] Ela se chama {b}irredutível."),
    # degrau a degrau
    dict(id="s12", block="degraus", text="Voltando à do começo: {a}dezoito vinte e quatro avos. [p=0.3] Dezoito e vinte e quatro são pares: {b}divida por dois. [p=0.2] {c}Nove doze avos."),
    dict(id="s13", block="degraus", text="Nove e doze: [p=0.2] a soma dos algarismos de cada um dá múltiplo de três. [p=0.2] {a}Divida por três. [p=0.2] {b}Três quartos. [p=0.3] Funcionou, mas foram dois passos."),
    dict(id="s14", block="degraus", text="Quer fazer em um passo só? [p=0.2] {a}Divida pelo MDC, o maior número que divide os dois. [p=0.3] MDC de dezoito e vinte e quatro é {b}seis. [p=0.2] {c}Dezoito dividido por seis, três. [p=0.2] {d}Vinte e quatro dividido por seis, quatro. [p=0.2] Direto."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com uma coisa. [p=0.2] Só vale {a}multiplicar ou dividir. [p=0.3] Tem gente que {b}soma o mesmo número em cima e embaixo. [p=0.2] Pega {c}um meio, soma um nos dois, e escreve {d}dois terços."),
    dict(id="s16", block="erro", text="Mas {a}dois terços é mais que metade. [p=0.3] A quantidade mudou. [p=0.2] {b}Somar não mantém a fração. Multiplicar e dividir mantêm."),
    # atalho
    dict(id="s17", block="atalho", text="E o atalho prometido: {a}o teste da cruz, também chamado de produto cruzado. [p=0.3] Ele diz se duas frações são equivalentes, sem simplificar nada."),
    dict(id="s18", block="atalho", text="{a}Dois terços e oito doze avos são equivalentes? [p=0.3] Multiplique em cruz: {b}dois vezes doze, vinte e quatro. [p=0.2] {c}Três vezes oito, vinte e quatro. [p=0.2] {d}Deu igual, são equivalentes. [p=0.3] Deu diferente, não são."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Em um simulado de {a}quarenta questões, [p=0.1] uma pessoa acertou {b}trinta. [p=0.3] {c}Que fração da prova ela acertou, na forma mais simples?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] A fração é {a}trinta quarenta avos: acertos em cima, total embaixo. [p=0.3] MDC de trinta e quarenta: {b}dez. [p=0.2] {c}Trinta dividido por dez, três. [p=0.2] {d}Quarenta dividido por dez, quatro. [p=0.2] {e}Três quartos da prova."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}multiplicar ou dividir em cima e embaixo pelo mesmo número não muda a fração. [p=0.3] {b}E o MDC simplifica em um passo só."),
    dict(id="s23", block="fim", text="Na próxima aula, as {a}frações maiores que um e o número misto. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
