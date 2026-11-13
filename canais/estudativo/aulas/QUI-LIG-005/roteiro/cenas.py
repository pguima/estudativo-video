# Estudativo · QUI-LIG-005 — Praticando: tipos de ligação (Química · Ligações Químicas · prática).
# Habilidade: montar fórmulas e prever propriedades de materiais pelo tipo de ligação.
# Pré-requisitos: QUI-LIG-001, QUI-LIG-002, QUI-LIG-003, QUI-LIG-004. Próxima: QUI-LIG-006 (geometria molecular).
# Questões inéditas, criadas para esta aula. Leituras: K⁺ = "cá mais", S²⁻ = "esse dois menos", K₂S = "cá dois esse", MgO = "eme gê ó".
# Fatos: K família 1 → K⁺; S família 16 → S²⁻; O₂ = O=O com 2 pares livres em cada O; Al: panela e papel-alumínio;
# MgO (óxido de magnésio) reveste fornos (refratário), PF ≈ 2852 °C. Contas: 2(+1) + (−2) = 0; O: 4 + 4 = 8.
# Macete da carga pela família: metal de família 1, 2, 13 → +1, +2, +3; ametal de família 15, 16, 17 → −3, −2, −1 (o que falta para 18).

TITULO = "Praticando: tipos de ligação"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões, criadas para esta aula, [p=0.2] sobre as três ligações: {b}iônica, covalente e metálica. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.2] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a carga dos íons pela família, [p=0.2] {b}o cruzamento das cargas, [p=0.2] {c}a conta das ligações que faltam para oito [p=0.2] e {d}o que a ligação diz sobre conduzir e derreter. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] O potássio é da {b}família um. [p=0.1] O enxofre, da {c}família dezesseis. [p=0.3] {d}Qual é a fórmula do composto formado entre eles?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Família um: um elétron na última camada, que o potássio perde. [p=0.1] Cá mais. [p=0.3] {b}Família dezesseis: seis elétrons, faltam dois. [p=0.1] O enxofre ganha dois: [p=0.1] esse dois menos. [p=0.3] {c}Cruzando, o dois desce para o potássio, e o um, para o enxofre. [p=0.2] {d}Cá dois esse. [p=0.3] Confira: {e}dois potássios, mais dois; um enxofre, menos dois. [p=0.1] Zero."),
    # atalho
    dict(id="s06", block="atalho", text="Aqui cabe o atalho da carga. [p=0.2] {a}Metal das famílias um, dois e treze: [p=0.1] a carga é positiva e vale o último algarismo da família. [p=0.3] {b}Família um, mais um; dois, mais dois; treze, mais três. [p=0.3] {c}Ametal: a carga é negativa e vale o que falta para dezoito. [p=0.2] {d}Família quinze, menos três; dezesseis, menos dois; dezessete, menos um."),
    dict(id="s07", block="atalho", text="Funciona porque {a}a família conta os elétrons de valência, [p=0.1] e {b}dezoito é a família dos gases nobres, com oito. [p=0.3] {c}Não compensa nos metais do meio da tabela, como o ferro: [p=0.1] {d}eles formam mais de um íon, e a questão precisa dizer qual."),
    # questão 2
    dict(id="s08", block="questao2", text="{a}Questão dois. [p=0.2] {b}O gás oxigênio que você respira é ó dois. [p=0.3] {c}Que ligação une esses átomos: simples, dupla ou tripla? [p=0.2] E {d}quantos pares livres tem cada oxigênio?"),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] {a}O oxigênio, da família dezesseis, tem seis elétrons de valência: [p=0.1] faltam dois, então ele faz duas ligações. [p=0.3] {b}Entre os átomos, dois pares compartilhados: uma ligação dupla. [p=0.3] {c}Cada oxigênio conta quatro elétrons na dupla e precisa de mais quatro: [p=0.1] {d}dois pares livres. [p=0.2] {e}Quatro mais quatro, oito."),
    # questão 3
    dict(id="s11", block="questao3", text="{a}Questão três. [p=0.2] {b}Uma panela de alumínio esquenta rápido no fogo, [p=0.1] e {c}o papel-alumínio dobra sem rasgar. [p=0.3] {d}Qual é a explicação das duas propriedades?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}Alumínio é metal: ligação metálica. [p=0.2] {b}Os elétrons livres, o mar de elétrons, levam o calor do fogo para a panela toda. [p=0.3] {c}E, quando você dobra o papel, as fileiras de íons escorregam, [p=0.1] {d}e o mar de elétrons continua segurando tudo junto. [p=0.3] {e}Uma explicação só: os elétrons livres."),
    # questão 4
    dict(id="s14", block="questao4", text="{a}Última questão. [p=0.2] {b}O magnésio, da família dois, e o oxigênio formam um sólido branco usado por dentro de fornos industriais. [p=0.3] {c}Qual é a fórmula? [p=0.2] {d}Ele conduz eletricidade sólido? E derretido?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Magnésio, família dois: [p=0.1] eme gê dois mais. [p=0.2] {b}Oxigênio: [p=0.1] ó dois menos. [p=0.3] {c}Cargas do mesmo tamanho, dois mais e dois menos: um para um. [p=0.2] {d}Eme gê ó. [p=0.3] {e}Quem cruza sem pensar escreve eme gê dois ó dois, e precisa reduzir para a menor proporção."),
    dict(id="s17", block="resposta4", text="{a}Metal com ametal: ligação iônica. [p=0.3] {b}Sólido, os íons estão presos: não conduz. [p=0.2] {c}Derretido, os íons andam: conduz. [p=0.3] E o forno? [p=0.1] {d}Composto iônico tem ponto de fusão alto: [p=0.1] {e}o óxido de magnésio só derrete perto de dois mil oitocentos e cinquenta graus."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}a família dá a carga, [p=0.1] {b}o cruzamento dá a fórmula, [p=0.1] {c}o que falta para oito dá as ligações, [p=0.1] e {d}o tipo de ligação dá as propriedades."),
    dict(id="s19", block="fim", text="Na próxima aula, as moléculas ganham forma: [p=0.2] {a}a geometria molecular. [p=0.2] Você vai descobrir por que {b}a molécula de água é dobrada e a de gás carbônico é reta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
