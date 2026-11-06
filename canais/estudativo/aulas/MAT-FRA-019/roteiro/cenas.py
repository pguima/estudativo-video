# Estudativo · MAT-FRA-019 — Fração em decimal e decimal em fração (Matemática · Frações e Decimais).
# Habilidade: escrever 3/8 como 0,375 e 0,35 como 7/20.
# Pré-requisitos: MAT-FRA-003 (equivalentes e simplificação), MAT-FRA-017 (resultado decimal). Próxima: MAT-FRA-020.
# Questão inédita, criada para esta aula. Esta cadeia não tem MAT-FRA-016 nem MAT-FRA-018: nada de andar com a vírgula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Fração em decimal e decimal em fração"

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
    dict(id="s01", block="gancho", text="Muita gente escreve {a}três oitavos como {b}três vírgula oito. [p=0.3] Só que três oitavos é {c}menos que um inteiro, [p=0.2] e três vírgula oito é {d}quase quatro inteiros. [p=0.3] Não pode ser o mesmo número."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai trocar fração por decimal e decimal por fração, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}continuar uma divisão depois da vírgula [p=0.2] e {c}simplificar uma fração. [p=0.3] Se faltar alguma, procure no canal."),
    # o traço é divisão
    dict(id="s04", block="traco", text="{a}Você já viu que o traço da fração é uma divisão: [p=0.2] {b}doze quartos é doze dividido por quatro. [p=0.3] Com o de cima menor, vale igual: [p=0.2] {c}um meio é um dividido por dois, [p=0.2] que dá {d}zero vírgula cinco."),
    dict(id="s05", block="traco", text="Então, para virar decimal, {a}divida o de cima pelo de baixo."),
    # três oitavos
    dict(id="s06", block="conta", text="Vamos a {a}três oitavos: [p=0.1] três dividido por oito. [p=0.3] Três é menor que oito, então {b}escreva zero e vírgula no resultado [p=0.2] e {c}ponha um zero ao lado do três: trinta."),
    dict(id="s07", block="conta", text="{a}Trinta dividido por oito dá três, e sobram seis. [p=0.2] Ponha outro zero: {b}sessenta dividido por oito dá sete, e sobram quatro. [p=0.2] Mais um zero: {c}quarenta dividido por oito dá cinco, e {d}não sobra nada. [p=0.3] A conta acabou."),
    dict(id="s08", block="conta", text="{a}Três oitavos é zero vírgula trezentos e setenta e cinco. [p=0.3] Menos que um inteiro, {b}como tinha que ser. [p=0.3] A fração e o decimal são {c}o mesmo número, escrito de jeitos diferentes."),
    # decimal em fração
    dict(id="s09", block="volta", text="E o caminho de volta? [p=0.2] O segredo é {a}ler o número em voz alta. [p=0.3] {b}Zero vírgula seis se lê seis décimos, [p=0.2] e isso já é {c}uma fração, com dez embaixo. [p=0.3] Seis e dez são pares: {d}divida em cima e embaixo por dois. [p=0.2] {e}Três quintos."),
    dict(id="s10", block="volta", text="A regra: {a}o número sem vírgula vai em cima. [p=0.2] Embaixo vai {b}um, seguido de um zero para cada casa depois da vírgula. [p=0.3] Uma casa, {c}dez: décimos. [p=0.2] Duas casas, {d}cem: centésimos. [p=0.2] Três casas, {e}mil: milésimos. [p=0.3] Depois, {f}simplifique, se der."),
    dict(id="s11", block="volta", text="Vamos a {a}zero vírgula trinta e cinco. [p=0.2] Duas casas: {b}trinta e cinco centésimos. [p=0.3] Trinta e cinco termina em cinco, cem termina em zero, [p=0.2] então dá para {c}dividir em cima e embaixo por cinco. [p=0.2] {d}Trinta e cinco dividido por cinco, sete. [p=0.2] {e}Cem dividido por cinco, vinte. [p=0.3] Resposta: {f}sete vinte avos."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com um erro comum: {a}errar o número de zeros. [p=0.2] A pessoa vê zero vírgula trinta e cinco e escreve {b}trinta e cinco décimos. [p=0.3] Confira dividindo: {c}trinta e cinco dividido por dez é três vírgula cinco. [p=0.2] {d}Dez vezes maior. [p=0.3] Duas casas, {e}dois zeros."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}faça o de baixo virar dez ou cem. [p=0.3] Em sete vinte avos, {b}vinte vezes cinco dá cem. [p=0.2] Multiplique em cima também: {c}sete vezes cinco, trinta e cinco. [p=0.2] {d}Trinta e cinco centésimos, [p=0.1] zero vírgula trinta e cinco, sem armar a divisão."),
    dict(id="s14", block="atalho", text="Funciona porque você {a}troca por uma fração equivalente, [p=0.2] e fração com cem embaixo se lê direto como decimal. [p=0.3] Não compensa em {b}três oitavos: [p=0.2] oito só chega em mil, multiplicando por cento e vinte e cinco. [p=0.2] Aí, {c}divida."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma tábua mede {a}cinco oitavos de metro. [p=0.2] {b}Quanto é isso em decimal? [p=0.3] Outra tábua mede {c}zero vírgula vinte e oito metro. [p=0.2] {d}Que fração do metro é essa, na forma mais simples?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco dividido por oito. [p=0.2] Escreva zero e vírgula. [p=0.2] {b}Cinquenta dividido por oito dá seis, e sobram dois. [p=0.2] {c}Vinte dividido por oito dá dois, e sobram quatro. [p=0.2] {d}Quarenta dividido por oito dá cinco, e não sobra nada. [p=0.3] {e}Zero vírgula seiscentos e vinte e cinco metro."),
    dict(id="s18", block="resposta", text="Na outra tábua, duas casas: {a}vinte e oito centésimos. [p=0.2] Vinte e oito e cem são divisíveis por quatro, então {b}divida em cima e embaixo por quatro. [p=0.2] Resposta: {c}sete vinte e cinco avos do metro."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}de fração para decimal, divida o de cima pelo de baixo. [p=0.2] {b}De decimal para fração, conte as casas e simplifique."),
    dict(id="s20", block="fim", text="Três oitavos acabou em três casas. [p=0.2] Mas algumas divisões {a}nunca acabam: os algarismos se repetem sem fim. [p=0.3] Na próxima aula, você {b}reconhece essas dízimas [p=0.2] e {c}prevê quando elas aparecem, sem dividir. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
