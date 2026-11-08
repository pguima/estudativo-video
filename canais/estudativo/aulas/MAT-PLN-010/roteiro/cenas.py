# Estudativo · MAT-PLN-010 — Praticando: raízes complexas (Matemática · Polinômios · Raízes complexas · prática).
# Habilidade: achar as raízes reais e complexas de uma equação polinomial com coeficientes reais.
# Pré-requisitos: MAT-PLN-008 (número i), MAT-PLN-009 (o par de conjugadas). Próxima: nenhuma (última da trilha).
# Girard (MAT-PLN-006) e multiplicidade (MAT-PLN-005) não estão na ficha: as questões usam Bhaskara, Briot-Ruffini,
# o atalho do par (MAT-PLN-009), o teste do um (MAT-PLN-004) e a diferença de dois quadrados (MAT-FAT-003).
# Questões inéditas, criadas para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o número i se escreve "í".

TITULO = "Praticando: raízes complexas"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões criadas para esta aula, [p=0.2] misturando raízes reais e complexas. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}í ao quadrado igual a menos um, [p=0.2] {b}o conjugado, que troca só o sinal do í, [p=0.2] {c}o Briô-Rufíni [p=0.2] e {d}o atalho do par, que vira um fator de grau dois. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Resolva {b}xis ao quadrado menos seis xis mais dez igual a zero."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Delta: trinta e seis menos quarenta, menos quatro. [p=0.2] {b}Raiz de menos quatro: dois í. [p=0.3] {c}Seis, mais ou menos dois í, dividido por dois. [p=0.2] Divida cada parte: {d}xis igual a três mais í, ou três menos í."),
    dict(id="s06", block="resposta1", text="Confira pelo atalho do par: [p=0.2] {a}menos duas vezes três, menos seis xis; [p=0.2] {b}três ao quadrado mais um ao quadrado, dez. [p=0.2] {c}Volta a equação do começo."),
    # questão 2
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] Ache todas as raízes de {b}xis ao cubo menos um igual a zero."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}O um é raiz: um ao cubo menos um dá zero. [p=0.3] {b}Briô-Rufíni com o um, com zero nos termos que faltam: um, zero, zero, menos um. [p=0.3] {c}Baixe o um. [p=0.2] {d}Um vezes um, mais zero, um. [p=0.2] {e}Um vezes um, mais zero, um de novo. [p=0.2] {f}Um menos um, zero."),
    dict(id="s10", block="resposta2", text="Sobra {a}xis ao quadrado mais xis mais um igual a zero. [p=0.2] {b}Delta: um menos quatro, menos três. [p=0.2] {c}Raiz de menos três: í raiz de três. [p=0.3] {d}Xis igual a menos um, mais ou menos í raiz de três, tudo dividido por dois. [p=0.3] {e}Uma raiz real e um par de complexas."),
    # questão 3
    dict(id="s11", block="questao3", text="{a}Questão três. [p=0.2] {b}Dois mais í é raiz de xis ao cubo menos cinco xis ao quadrado mais nove xis menos cinco. [p=0.2] {c}Ache as outras raízes."),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}O conjugado também é raiz: dois menos í. [p=0.3] Pelo atalho, o par vira: [p=0.2] {b}menos duas vezes dois, menos quatro xis; [p=0.2] {c}dois ao quadrado mais um ao quadrado, cinco. [p=0.2] {d}Xis ao quadrado menos quatro xis mais cinco."),
    dict(id="s14", block="resposta3", text="Antes de dividir, {a}teste o um: um menos cinco mais nove menos cinco, zero. [p=0.2] {b}O um é raiz. [p=0.3] {c}Grau três, três raízes: dois mais í, dois menos í e um. [p=0.3] Se o um não fosse raiz, bastaria dividir pelo par. [p=0.2] Para conferir, {d}xis ao quadrado menos quatro xis mais cinco, vezes xis menos um, [p=0.2] volta o polinômio."),
    # questão 4
    dict(id="s15", block="questao4", text="{a}Última questão. [p=0.2] Ache todas as raízes de {b}xis elevado a quatro, menos dezesseis, igual a zero."),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] {a}Xis elevado a quatro é o quadrado de xis ao quadrado, [p=0.2] e dezesseis é o quadrado de quatro. [p=0.2] {b}Diferença de dois quadrados: xis ao quadrado mais quatro, vezes xis ao quadrado menos quatro."),
    dict(id="s18", block="resposta4", text="Algum fator vale zero. [p=0.2] {a}Xis ao quadrado menos quatro igual a zero: xis igual a dois ou menos dois. [p=0.3] {b}Xis ao quadrado mais quatro igual a zero: xis ao quadrado igual a menos quatro, [p=0.2] e {c}xis igual a dois í ou menos dois í. [p=0.3] Quem respondeu só dois e menos dois {d}achou as reais, mas a questão pedia todas."),
    # atalho
    dict(id="s19", block="atalho", text="O atalho desta prática: {a}conte as raízes antes de começar. [p=0.2] O número de raízes é o grau, [p=0.2] e as raízes com í vêm em pares, quando os coeficientes são reais. [p=0.3] {b}Grau quatro: quatro raízes. [p=0.2] Na última questão, {c}duas reais e duas complexas, e a conta fecha. [p=0.3] {d}Se a contagem não fechar, falta raiz na sua resposta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}delta negativo pede í, [p=0.2] {b}raiz complexa traz o conjugado, [p=0.2] e {c}o grau diz quantas raízes há, contando as que têm í."),
    dict(id="s21", block="fim", text="Com isso, você fecha {a}a trilha de polinômios. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
