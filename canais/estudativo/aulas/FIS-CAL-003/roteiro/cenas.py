# Estudativo · FIS-CAL-003 — Calor sensível: Q = m·c·ΔT (Física · Calor e Termodinâmica · Calorimetria e mudanças de estado).
# Habilidade: calcular o calor que muda a temperatura, com o macete do "que macete", e explicar por que a água segura o clima das
# cidades litorâneas.
# Pré-requisitos: FIS-CAL-001 (temperatura, calor, variação), MAT-EQU-011 (isolar uma letra). Próxima: FIS-CAL-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Energia e joule ainda não foram ensinados (FIS-ENE): a unidade da aula é a caloria; o joule só é citado como "aula de energia",
# sem o fator 4,2 (a prova dá a conversão).
# Valores de tabela arredondados: c da água = 1 cal/(g·°C); c da areia ≈ 0,2 cal/(g·°C).
# Sinal: Q > 0 recebe, Q < 0 cede (base para FIS-CAL-005, soma dos calores = 0).

TITULO = "Calor sensível: Q = m·c·ΔT"

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
    dict(id="s01", block="gancho", text="{a}Meio-dia na praia. [p=0.2] {b}A areia queima o pé, [p=0.2] e {c}a água do mar continua fresca. [p=0.3] {d}O mesmo sol esquentou as duas. [p=0.3] Por que só a areia fica tão quente?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai responder isso [p=0.2] e calcular {b}quanto calor é preciso para mudar a temperatura de qualquer coisa."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}calor é a energia que passa do mais quente para o mais frio, [p=0.1] e delta tê é a variação de temperatura; [p=0.2] e {c}isolar uma letra numa fórmula. [p=0.3] Se faltar alguma, procure no canal."),
    # caloria
    dict(id="s04", block="caloria", text="Primeiro, a unidade. [p=0.2] Calor se mede em {a}caloria. [p=0.3] {b}Uma caloria é o calor que faz um grama de água subir um grau Celsius. [p=0.3] {c}Mil calorias são uma quilocaloria, [p=0.2] a que aparece nos rótulos de comida."),
    dict(id="s05", block="caloria", text="{a}No Sistema Internacional, a energia se mede em outra unidade, o joule, [p=0.2] assunto da aula de energia. [p=0.2] {b}Quando a prova usa joule, ela dá a conversão. [p=0.2] Aqui, fique com a caloria."),
    # a fórmula
    dict(id="s06", block="formula", text="Quanto calor é preciso para esquentar alguma coisa? [p=0.2] Depende de {a}três coisas. [p=0.3] {b}Da massa: [p=0.1] uma panela cheia demora mais que uma xícara. [p=0.2] {c}De quanto a temperatura vai subir. [p=0.2] E {d}do material."),
    dict(id="s07", block="formula", text="Juntando tudo: [p=0.2] {a}quê igual a eme vezes cê vezes delta tê. [p=0.3] {b}A letra quê é o calor, em calorias. [p=0.2] {c}A letra eme é a massa, em gramas. [p=0.2] {d}Delta tê é a variação de temperatura, em graus Celsius."),
    dict(id="s08", block="formula", text="E {a}a letra cê é o calor específico: [p=0.2] quantas calorias {b}cada grama do material precisa para subir um grau. [p=0.3] Na água, {c}uma caloria por grama por grau Celsius. [p=0.2] Na areia, {d}só zero vírgula dois. [p=0.3] Esse calor se chama {e}sensível, [p=0.1] porque a mudança de temperatura dá para sentir."),
    dict(id="s09", block="formula", text="Para não esquecer, leia a fórmula em voz alta: [p=0.2] {a}quê, eme, cê, delta tê. [p=0.3] Vira {b}que macete! [p=0.3] O tê do delta tê fecha a palavra."),
    # exemplo
    dict(id="s10", block="exemplo", text="Vamos usar. [p=0.2] Quanto calor leva {a}meio litro de água, quinhentos gramas, [p=0.1] {b}de vinte para oitenta graus Celsius?"),
    dict(id="s11", block="exemplo", text="{a}Delta tê é oitenta menos vinte, que dá sessenta. [p=0.2] {b}O calor é quinhentos vezes um vezes sessenta: [p=0.2] {c}trinta mil calorias, [p=0.1] ou {d}trinta quilocalorias."),
    dict(id="s12", block="exemplo", text="E se a água esfriasse de oitenta para vinte? [p=0.2] {a}Delta tê seria menos sessenta, [p=0.2] e {b}quê, menos trinta mil. [p=0.3] {c}Sinal de menos quer dizer que o corpo cedeu calor; [p=0.2] {d}sinal de mais, que recebeu."),
    # praia
    dict(id="s13", block="praia", text="Agora, a praia. [p=0.2] Imagine {a}mil gramas de água e mil gramas de areia, [p=0.2] e as duas recebendo {b}mil calorias. [p=0.3] Isole o delta tê: {c}é o quê dividido pelo produto eme vezes cê."),
    dict(id="s14", block="praia", text="Na água, {a}eme vezes cê dá mil vezes um, mil. [p=0.1] Mil dividido por mil: um grau. [p=0.3] Na areia, {b}eme vezes cê dá mil vezes zero vírgula dois, duzentos. [p=0.1] Mil dividido por duzentos: cinco graus. [p=0.3] {c}Com o mesmo calor, a areia esquenta cinco vezes mais."),
    dict(id="s15", block="praia", text="Por isso, {a}a água esquenta devagar e esfria devagar. [p=0.3] Cidades do litoral, perto dessa água toda, {b}têm dias menos quentes e noites menos frias. [p=0.2] Longe do mar, {c}no deserto, a diferença entre o dia e a noite é enorme."),
    # erro
    dict(id="s16", block="erro", text="Cuidado com {a}as unidades. [p=0.2] Se o calor específico está em calorias por grama, [p=0.2] {b}a massa tem que estar em gramas. [p=0.3] Quem põe {c}zero vírgula cinco quilograma no lugar de quinhentos gramas [p=0.2] acha {d}trinta calorias, [p=0.2] {e}mil vezes menos que o certo."),
    # atalho
    dict(id="s17", block="atalho", text="Agora, o atalho: {a}leia a fórmula como proporção. [p=0.3] Com o mesmo calor e a mesma massa, [p=0.2] {b}quem tem o calor específico cinco vezes menor, esquenta cinco vezes mais. [p=0.3] {c}Dobrou a massa, dobra o calor. [p=0.3] Funciona porque {d}é tudo multiplicação. [p=0.2] {e}Não compensa quando a questão dá todos os números e pede um valor exato: [p=0.2] aí, faça a conta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma panela tem {a}quatrocentos gramas de água a vinte e cinco graus Celsius. [p=0.3] Ela recebe {b}doze mil calorias. [p=0.3] {c}Qual é a temperatura final da água?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Isole o delta tê: {a}quê dividido pelo produto eme vezes cê. [p=0.2] {b}Eme vezes cê dá quatrocentos vezes um, quatrocentos. [p=0.1] Doze mil dividido por quatrocentos: [p=0.2] {c}trinta graus. [p=0.3] Mas trinta é quanto ela subiu, {d}não a temperatura final. [p=0.2] {e}Vinte e cinco mais trinta: [p=0.1] {f}cinquenta e cinco graus Celsius."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}que macete, quê igual a eme cê delta tê; [p=0.2] {b}calor específico alto, como o da água, esquenta devagar; [p=0.2] e {c}massa em gramas, se o cê estiver por grama."),
    dict(id="s22", block="fim", text="Na próxima aula, o calor entra {a}e a temperatura não sobe: [p=0.2] é o {b}calor latente, que derrete o gelo e ferve a água. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
