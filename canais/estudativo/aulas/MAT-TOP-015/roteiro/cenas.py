# Estudativo · MAT-TOP-015 — Algarismos significativos e arredondamento (Matemática · Tópicos Avançados · Bases de contagem e algarismos significativos).
# Habilidade: dizer que 0,0420 tem 3 algarismos significativos e dar 2,5 × 3,14 com 2 significativos (7,9).
# Pré-requisitos: MAT-LEI-004 (estimar, arredondar), MAT-POT-012 (notação científica, "número da frente"). Usa MAT-FRA-014 (arredondar:
#   5 ou mais, sobe). Próxima: MAT-TOP-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; números com zeros significativos lidos algarismo a algarismo.
# Questão inédita, criada para esta aula. Arredondamento pela regra da MAT-FRA-014 (o algarismo seguinte é 5: sobe), como na ficha.
# Contas: 2,5 × 3,14 = 7,85 → 7,9. 0,0420 = 4,20 × 10⁻² (3). 4200 com 3 significativos = 4,20 × 10³.
#   Questão: 0,00305 = 3,05 × 10⁻³ (3); 6,0 × 1,25 = 7,500 → 7,5 (2 significativos).

TITULO = "Algarismos significativos e arredondamento"

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
    dict(id="s01", block="gancho", text="Um fio mede {a}dois vírgula cinco metros, [p=0.2] e cada metro dele pesa {b}três vírgula catorze gramas. [p=0.3] A calculadora multiplica e mostra {c}sete vírgula oitenta e cinco. [p=0.3] Só que esse último cinco {d}é inventado. [p=0.2] O resultado honesto é {e}sete vírgula nove gramas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta os algarismos que valem numa medida, [p=0.2] arredonda o resultado de uma conta do jeito certo [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}arredondar: olhe o algarismo logo depois da última casa que fica; se for cinco ou mais, ela sobe um; [p=0.2] e {c}a notação científica: um número da frente, de um até menos de dez, vezes uma potência de dez. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="regua", text="Toda medida tem {a}um limite. [p=0.2] Numa régua que só marca os centímetros, um lápis mede {b}doze vírgula três centímetros. [p=0.3] O um e o dois são {c}certos: estão marcados na régua. [p=0.2] O três é {d}estimado: o olho viu que o lápis passou um pouco do doze."),
    dict(id="s05", block="regua", text="Os algarismos certos, mais o primeiro estimado, são os {a}algarismos significativos. [p=0.2] Doze vírgula três tem {b}três. [p=0.3] Escrever doze vírgula três quatro cinco seria {c}inventar uma precisão que a régua não tem."),
    # as regras
    dict(id="s06", block="regras", text="Para contar os significativos, {a}três regras. [p=0.3] {b}Primeira: todo algarismo diferente de zero conta. [p=0.2] {c}Segunda: zero entre algarismos que contam também conta. [p=0.2] Duzentos e cinco tem {d}três."),
    dict(id="s07", block="regras", text="{a}Terceira: zero à esquerda não conta. [p=0.3] Em {b}zero vírgula zero, quatro, dois, zero, [p=0.2] os zeros antes do quatro {c}só mostram onde fica a vírgula. [p=0.3] Mas o zero do fim, {d}depois da vírgula, conta: [p=0.2] ele diz que a medida foi feita até aquela casa, e deu zero."),
    dict(id="s08", block="regras", text="Então esse número tem {a}três significativos: [p=0.2] {b}o quatro, o dois e o zero do fim."),
    # nas contas
    dict(id="s09", block="contas", text="E nas contas? [p=0.2] {a}Ao multiplicar ou dividir medidas, [p=0.2] o resultado fica com {b}o mesmo número de significativos da medida que tem menos. [p=0.3] {c}Dois vírgula cinco tem dois. [p=0.2] {d}Três vírgula catorze tem três. [p=0.2] O resultado fica com {e}dois."),
    dict(id="s10", block="contas", text="{a}Sete vírgula oitenta e cinco, com dois significativos: [p=0.2] {b}ficam o sete e o oito. [p=0.2] {c}O algarismo seguinte é cinco, então o oito sobe para nove. [p=0.3] {d}Sete vírgula nove gramas."),
    dict(id="s11", block="contas", text="Por quê? [p=0.2] O dois vírgula cinco {a}já tem dúvida nos décimos. [p=0.2] Nenhuma conta deixa o resultado {b}mais preciso que a medida mais pobre. [p=0.3] {c}Essa regra é para multiplicar e dividir."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}contar os zeros da esquerda. [p=0.2] Quem conta tudo em zero vírgula zero, quatro, dois, zero, responde {b}cinco. [p=0.3] Mas um número pequeno {c}não fica mais preciso só por ter zeros na frente. [p=0.2] Esses zeros são {d}só o lugar da vírgula."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}passe para notação científica. [p=0.3] {b}Zero vírgula zero, quatro, dois, zero, vira quatro vírgula dois zero vezes dez elevado a menos dois. [p=0.3] {c}Os zeros da esquerda somem sozinhos, [p=0.2] e todo algarismo do número da frente {d}é significativo: três."),
    dict(id="s14", block="atalho", text="Funciona porque a potência de dez {a}só guarda o lugar da vírgula, [p=0.2] e o número da frente guarda {b}a medida. [p=0.3] Ela também resolve {c}números como quatro mil e duzentos, [p=0.2] em que não dá para saber se os zeros do fim foram medidos: [p=0.2] com três significativos, escreva {d}quatro vírgula dois zero vezes dez elevado a três. [p=0.3] {e}Não compensa num número como três vírgula catorze: [p=0.2] aí, conte direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quantos algarismos significativos tem zero vírgula zero, zero, três, zero, cinco? [p=0.3] E {b}quanto dá seis vírgula zero vezes um vírgula vinte e cinco, [p=0.2] com os significativos certos?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Os três zeros da esquerda não contam. [p=0.2] Sobram {b}o três, o zero do meio e o cinco: [p=0.2] {c}três significativos. [p=0.3] Na notação científica, fica claro: {d}três vírgula zero cinco vezes dez elevado a menos três."),
    dict(id="s18", block="resposta", text="{a}Seis vírgula zero vezes um vírgula vinte e cinco dá sete vírgula cinco. [p=0.3] {b}Seis vírgula zero tem dois significativos: o zero do fim conta. [p=0.2] {c}Um vírgula vinte e cinco tem três. [p=0.2] O resultado fica com dois: {d}sete vírgula cinco."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}significativos são os algarismos certos mais o primeiro estimado; [p=0.2] {b}zero à esquerda não conta; [p=0.2] e {c}ao multiplicar, manda a medida com menos significativos."),
    dict(id="s20", block="fim", text="Na próxima aula, a geometria volta: [p=0.2] você corta {a}um cone perto da ponta [p=0.2] e acha o volume da parte de baixo, {b}o tronco. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
