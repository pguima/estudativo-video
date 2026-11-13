# Estudativo · QUI-CAL-007 — Pureza dos reagentes (Química · Cálculos Químicos · Estequiometria).
# Habilidade: calcular quanto CaO sai de 200 g de calcário com 80% de pureza.
# Pré-requisitos: QUI-CAL-005, MAT-POR-002. Próxima: QUI-CAL-008 (rendimento e reações em etapas).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: CaCO₃ → CaO + CO₂ = 100 g : 56 g : 44 g (Ca 40, C 12, O 16); 0,8 · 200 = 160 g; 160 · 56/100 = 89,6 g de CaO;
# erro (sem pureza) 200 · 0,56 = 112 g; atalho 0,8 · 112 = 89,6. Questão: 0,8 · 250 = 200 g → 2 · 44 = 88 g de CO₂;
# erro 250 · 0,44 = 110 g. Fato: cal virgem (CaO) sai do calcário aquecido no forno (calcinação).

TITULO = "Pureza dos reagentes"

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
    dict(id="s01", block="gancho", text="{a}A cal da construção sai do calcário aquecido no forno. [p=0.3] {b}A conta diz que duzentos gramas de calcário dão cento e doze gramas de cal. [p=0.3] {c}Mas, na fábrica, saem menos de noventa. [p=0.2] {d}O que a conta esqueceu?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}descontar a impureza de um reagente [p=0.2] e calcular {c}quanto produto sai de verdade, [p=0.2] com um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a conta de massa para massa numa equação, [p=0.2] e {c}calcular uma porcentagem multiplicando pelo decimal: [p=0.1] trinta e sete por cento de duzentos e quarenta é zero vírgula trinta e sete vezes duzentos e quarenta. [p=0.3] Se faltar alguma, procure no canal."),
    # pureza
    dict(id="s04", block="pureza", text="{a}O calcário é uma rocha. [p=0.2] {b}A parte que interessa é o carbonato de cálcio, cê á cê ó três. [p=0.2] {c}O resto é areia, argila e outras coisas, [p=0.1] que não viram cal. [p=0.3] {d}Pureza é a porcentagem da amostra que é a substância que reage."),
    dict(id="s05", block="pureza", text="{a}Com oitenta por cento de pureza, [p=0.1] {b}oitenta em cada cem gramas são carbonato. [p=0.2] {c}Os outros vinte não reagem."),
    # exemplo
    dict(id="s06", block="exemplo", text="{a}A reação no forno: [p=0.1] cê á cê ó três forma cê á ó mais cê ó dois. [p=0.3] {b}Embaixo, as massas: [p=0.1] {c}cem gramas de carbonato [p=0.1] {d}dão cinquenta e seis de cal, o cê á ó."),
    dict(id="s07", block="exemplo", text="{a}Passo um: tire a impureza. [p=0.2] {b}Oitenta por cento é zero vírgula oito. [p=0.1] {c}Zero vírgula oito vezes duzentos dá cento e sessenta gramas de carbonato puro."),
    dict(id="s08", block="exemplo", text="{a}Passo dois: a regra de três só com a parte pura. [p=0.2] {b}Cem gramas dão cinquenta e seis. [p=0.2] {c}Cento e sessenta dão xis. [p=0.3] {d}Xis igual a cento e sessenta vezes cinquenta e seis, dividido por cem: [p=0.2] {e}dá oitenta e nove vírgula seis gramas de cal."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}esquecer a pureza e usar os duzentos gramas inteiros. [p=0.3] {b}A conta dá cento e doze gramas, [p=0.1] {c}mais cal do que a pedra consegue dar. [p=0.3] {d}A impureza pesa na balança, mas não reage."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho: [p=0.1] {a}a pureza pode entrar no começo ou no fim, [p=0.1] e o resultado é o mesmo. [p=0.3] {b}Se o calcário fosse puro, duzentos gramas dariam cento e doze de cal. [p=0.2] {c}Oitenta por cento disso: zero vírgula oito vezes cento e doze [p=0.1] {d}dá os mesmos oitenta e nove vírgula seis."),
    dict(id="s11", block="atalho", text="{a}Funciona porque tudo é proporcional: [p=0.1] tirar vinte por cento do reagente tira vinte por cento do produto. [p=0.3] {b}Escolha a ordem que deixa a conta mais redonda. [p=0.3] {c}Não compensa quando a questão também pede o reagente limitante: [p=0.1] aí, tire a impureza primeiro. [p=0.2] E nunca aplique a pureza duas vezes."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}Duzentos e cinquenta gramas de calcário com oitenta por cento de pureza [p=0.1] vão ao forno. [p=0.2] {b}Na mesma reação, cem gramas de carbonato dão quarenta e quatro de gás carbônico. [p=0.3] {c}Quantos gramas de gás carbônico saem?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Passo um, a parte pura: [p=0.1] zero vírgula oito vezes duzentos e cinquenta dá duzentos gramas. [p=0.3] {b}Passo dois: cem gramas dão quarenta e quatro. [p=0.2] {c}Duzentos é o dobro: [p=0.1] {d}oitenta e oito gramas de gás carbônico. [p=0.3] {e}Quem esqueceu a pureza chegou a cento e dez."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}só a parte pura reage; [p=0.2] {b}multiplique a massa da amostra pela pureza, em decimal, [p=0.1] {c}e faça a estequiometria com a parte pura."),
    dict(id="s16", block="fim", text="Na próxima aula, a perda vem da própria reação: [p=0.2] {a}o rendimento, [p=0.1] e {b}como juntar várias reações seguidas numa conta só. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
