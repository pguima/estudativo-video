# Estudativo · MAT-EQU-014 — Comparar dois planos (Matemática · Equações do 1º Grau).
# Habilidade: achar quantos minutos igualam um plano de R$ 40 + 0,50 por minuto a outro de R$ 20 + 1 por minuto.
# Pré-requisitos: MAT-EQU-009 (equação com parênteses), MAT-EQU-013 (montar a equação). Próxima: MAT-EQU-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Planos e valores inventados para a aula. Questão inédita. "Qual fica mais barato a partir de quanto" com inequação é a MAT-EQU-016.

TITULO = "Comparar dois planos"

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
    dict(id="s01", block="gancho", text="{a}O plano A cobra quarenta reais por mês, [p=0.2] mais cinquenta centavos por minuto. [p=0.3] {b}O plano B cobra vinte reais por mês, [p=0.2] mais um real por minuto. [p=0.3] {c}Qual é mais barato?"),
    dict(id="s02", block="gancho", text="Quem responde B na hora pode {a}pagar mais caro. [p=0.3] {b}A resposta depende de quanto você fala. [p=0.2] Os valores foram {c}inventados para a aula, [p=0.2] mas o raciocínio serve para planos de verdade."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você acha com quantos minutos dois planos custam o mesmo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s04", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}montar a equação de um problema, [p=0.2] com o desconhecido virando xis, [p=0.2] e {c}resolver equação com xis dos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # a conta de cada plano
    dict(id="s05", block="conta", text="O que você não sabe é {a}quantos minutos vai falar. [p=0.2] Então {b}os minutos viram xis."),
    dict(id="s06", block="conta", text="No plano A, você paga os quarenta fixos [p=0.2] e mais cinquenta centavos a cada minuto. [p=0.2] Fica {a}quarenta mais zero vírgula cinco xis. [p=0.3] No plano B, {b}vinte mais um xis, [p=0.2] que se escreve só {c}vinte mais xis."),
    # tabela
    dict(id="s07", block="tabela", text="Vamos testar alguns valores numa {a}tabela. [p=0.3] {b}Sem falar nada, A custa quarenta e B custa vinte. [p=0.2] B ganha. [p=0.3] {c}Com vinte minutos, A custa cinquenta e B custa quarenta. [p=0.2] B ainda ganha."),
    dict(id="s08", block="tabela", text="{a}Com sessenta minutos, A custa setenta e B custa oitenta. [p=0.3] {b}Virou! [p=0.2] Agora A é o mais barato. [p=0.3] Em algum ponto no meio do caminho, [p=0.2] {c}os planos custaram exatamente o mesmo."),
    # equação
    dict(id="s09", block="equacao", text="Esse ponto se chama {a}ponto de equilíbrio: [p=0.2] é onde os preços ficam iguais. [p=0.3] Preços iguais, então {b}a conta de A é igual à conta de B."),
    dict(id="s10", block="equacao", text="{a}Quarenta mais zero vírgula cinco xis, igual a vinte mais xis. [p=0.3] Vamos deixar o xis de um lado só. [p=0.2] {b}Tire zero vírgula cinco xis de cada lado: [p=0.2] {c}quarenta igual a vinte mais zero vírgula cinco xis."),
    dict(id="s11", block="equacao", text="{a}Tire vinte de cada lado: [p=0.2] {b}vinte igual a zero vírgula cinco xis. [p=0.3] {c}Divida cada lado por zero vírgula cinco. [p=0.2] Dividir por meio é o mesmo que {d}dobrar: [p=0.2] {e}xis igual a quarenta."),
    dict(id="s12", block="equacao", text="A resposta é {a}quarenta minutos. [p=0.3] Conferindo nos planos: [p=0.2] em A, {b}quarenta mais vinte dá sessenta reais. [p=0.2] Em B, {c}vinte mais quarenta dá sessenta reais. [p=0.2] {d}Bateu."),
    dict(id="s13", block="equacao", text="E a tabela conta o resto da história: [p=0.2] {a}antes dos quarenta minutos, B sai mais barato. [p=0.2] {b}Depois, A sai mais barato."),
    # erro
    dict(id="s14", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}olhar só a mensalidade. [p=0.3] Vinte é menos que quarenta, então a pessoa escolhe B. [p=0.2] Só que, com sessenta minutos, ela paga {b}oitenta reais, [p=0.2] quando poderia pagar {c}setenta. [p=0.3] {d}Quem fala muito sente o peso do minuto mais caro."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}diferença das mensalidades dividida pela diferença do minuto. [p=0.3] {b}Quarenta menos vinte dá vinte reais. [p=0.2] {c}Um real menos cinquenta centavos dá cinquenta centavos. [p=0.2] {d}Vinte dividido por zero vírgula cinco dá quarenta minutos."),
    dict(id="s16", block="atalho", text="Funciona porque {a}B começa vinte reais mais barato, [p=0.2] e {b}a cada minuto essa vantagem cai cinquenta centavos. [p=0.2] Em quarenta minutos, {c}a vantagem acaba. [p=0.3] {d}Não compensa quando o plano tem outras cobranças, [p=0.2] como taxa extra ou franquia. [p=0.2] Aí, {e}monte a equação."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, com valores inventados. [p=0.2] {a}O táxi A cobra cinco reais de saída, [p=0.2] mais três reais por quilômetro. [p=0.3] {b}O táxi B cobra onze reais de saída, [p=0.2] mais dois reais e cinquenta centavos por quilômetro. [p=0.3] {c}Com quantos quilômetros as corridas custam o mesmo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Os quilômetros viram xis. [p=0.2] {b}Cinco mais três xis, igual a onze mais dois vírgula cinco xis. [p=0.3] {c}Tire dois vírgula cinco xis de cada lado: [p=0.2] {d}cinco mais zero vírgula cinco xis, igual a onze."),
    dict(id="s20", block="resposta", text="{a}Tire cinco de cada lado: [p=0.2] {b}zero vírgula cinco xis igual a seis. [p=0.2] Dobrando: {c}xis igual a doze quilômetros. [p=0.3] Conferindo: [p=0.2] {d}cinco mais três vezes doze dá quarenta e um reais. [p=0.2] {e}Onze mais dois e meio vezes doze também dá quarenta e um. [p=0.2] {f}Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}escreva a conta de cada plano [p=0.2] e {b}iguale as contas para achar o empate."),
    dict(id="s22", block="fim", text="Na próxima aula, a pergunta muda de {a}quando fica igual [p=0.2] para {b}quando fica menor. [p=0.2] É a {c}inequação, [p=0.2] e você vai entender por que, às vezes, {d}o sinal vira. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
