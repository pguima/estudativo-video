# Estudativo · FIS-CAL-004 — Calor latente e curva de aquecimento (Física · Calor e Termodinâmica · Calorimetria e mudanças de estado).
# Habilidade: calcular Q = m·L e somar as etapas de uma curva de aquecimento, sabendo por que a temperatura fica parada no patamar
# e por que o suor resfria o corpo.
# Pré-requisitos: FIS-CAL-003 (Q = m·c·ΔT, sinal do calor), QUI-MIS-004 (curva de aquecimento, patamares). Próxima: FIS-CAL-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Valores de tabela (água ao nível do mar): L de fusão do gelo = 80 cal/g; L de vaporização = 540 cal/g; c do gelo = 0,5 cal/(g·°C);
# c da água = 1 cal/(g·°C). Forças entre partículas (QUI-LIG-009) não estão em "Já ensinado": o patamar é explicado como
# "o calor separa as partículas em vez de agitá-las mais" (QUI-MIS-003).

TITULO = "Calor latente e curva de aquecimento"

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
    dict(id="s01", block="gancho", text="{a}A água está fervendo na panela. [p=0.2] Você {b}aumenta o fogo. [p=0.3] A temperatura da água sobe? [p=0.3] {c}Não. [p=0.2] Ao nível do mar, ela fica {d}em cem graus até a última gota virar vapor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender {b}para onde vai esse calor [p=0.2] e somar {c}todas as etapas de uma curva de aquecimento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}quê igual a eme cê delta tê, o macete do que macete; [p=0.2] e {c}a curva de aquecimento, com os patamares da fusão e da ebulição. [p=0.3] Se faltar alguma, procure no canal."),
    # o patamar
    dict(id="s04", block="patamar", text="{a}Na curva de aquecimento da água, [p=0.2] a temperatura sobe, {b}para em zero grau, [p=0.2] {c}sobe de novo [p=0.1] e {d}para em cem. [p=0.3] Nos patamares, o fogo continua ligado. [p=0.2] O calor está entrando. [p=0.2] Para onde ele vai?"),
    dict(id="s05", block="patamar", text="{a}Ele vai para mudar o estado. [p=0.3] No gelo, as partículas estão presas numa arrumação. [p=0.2] No patamar, o calor {b}separa as partículas, [p=0.2] em vez de agitá-las mais. [p=0.3] {c}Como a agitação não muda, a temperatura também não muda."),
    # a fórmula
    dict(id="s06", block="formula", text="Esse calor que muda o estado sem mudar a temperatura se chama {a}calor latente. [p=0.2] Latente quer dizer escondido: [p=0.1] {b}o termômetro não mostra."),
    dict(id="s07", block="formula", text="A fórmula é {a}quê igual a eme vezes éle. [p=0.3] {b}A letra quê é o calor, em calorias; [p=0.1] {c}a letra eme, a massa, em gramas. [p=0.2] E {d}a letra éle é o calor latente: [p=0.2] quantas calorias {e}cada grama precisa para mudar de estado."),
    dict(id="s08", block="formula", text="Na água, {a}derreter o gelo pede oitenta calorias por grama. [p=0.2] {b}Ferver a água pede quinhentas e quarenta. [p=0.3] Na volta, {c}congelando ou condensando, o mesmo calor sai, [p=0.2] e o quê fica {d}negativo."),
    # o suor
    dict(id="s09", block="suor", text="É isso que faz {a}o suor resfriar o corpo. [p=0.3] Para evaporar, a água do suor {b}precisa de calor latente, [p=0.2] e {c}tira esse calor da sua pele. [p=0.3] {d}Pele que perde calor esfria."),
    # curva completa
    dict(id="s10", block="curva", text="Agora, juntando tudo. [p=0.2] Quanto calor leva {a}cem gramas de gelo a menos vinte graus [p=0.1] até {b}água a quarenta graus? [p=0.3] Siga a curva, {c}uma etapa de cada vez."),
    dict(id="s11", block="curva", text="{a}Etapa um: o gelo esquenta de menos vinte até zero. [p=0.2] Rampa, então {b}eme cê delta tê. [p=0.2] Cuidado: {c}o cê do gelo é zero vírgula cinco, não um. [p=0.3] {d}Cem vezes zero vírgula cinco vezes vinte: mil calorias."),
    dict(id="s12", block="curva", text="{a}Etapa dois: o gelo derrete, em zero grau. [p=0.2] Patamar, então {b}eme éle. [p=0.2] {c}Cem vezes oitenta: oito mil calorias."),
    dict(id="s13", block="curva", text="{a}Etapa três: a água esquenta de zero até quarenta. [p=0.2] Rampa de novo: {b}cem vezes um vezes quarenta, quatro mil calorias. [p=0.3] Somando, {c}mil mais oito mil mais quatro mil: [p=0.2] {d}treze mil calorias."),
    dict(id="s14", block="curva", text="E se a questão fosse até virar vapor? [p=0.2] Faltariam mais duas etapas: [p=0.2] {a}esquentar a água de quarenta até cem, seis mil calorias, [p=0.2] e {b}ferver tudo, cem vezes quinhentos e quarenta: cinquenta e quatro mil. [p=0.3] {c}Só a fervura gasta mais que todas as outras etapas juntas."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}fazer uma conta só, de menos vinte até quarenta: [p=0.2] {b}cem vezes um vezes sessenta, seis mil calorias. [p=0.3] {c}Faltou o patamar, [p=0.2] e o cê do gelo saiu errado. [p=0.3] Deu menos da metade do certo."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho da curva: [p=0.2] {a}rampa é eme cê delta tê, [p=0.2] {b}patamar é eme éle. [p=0.3] Desenhe a curva, {c}dê uma conta para cada pedaço e some. [p=0.3] E uma pista para conferir: [p=0.2] {d}na água, com o fogo constante, o patamar da fervura é quase sete vezes mais longo que o da fusão, [p=0.2] porque quinhentos e quarenta é quase sete vezes oitenta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Cinquenta gramas de gelo a zero grau [p=0.1] viram {b}água a vinte graus. [p=0.3] {c}Quanto calor foi preciso?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O gelo já está em zero, então começa no patamar. [p=0.2] {a}Derreter: cinquenta vezes oitenta, quatro mil calorias. [p=0.3] {b}Esquentar a água: cinquenta vezes um vezes vinte, mil calorias. [p=0.3] Total: {c}cinco mil calorias."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no patamar, o calor muda o estado e a temperatura fica parada; [p=0.2] {b}quê igual a eme éle; [p=0.2] e {c}na curva, uma conta por etapa."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}um corpo quente e um frio se encontram num calorímetro, [p=0.2] e você descobre {b}a temperatura de equilíbrio, a mesma para os dois no fim. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
