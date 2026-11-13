# Estudativo · QUI-ORG-009 — Amina, amida e nitrila (Química · Química Orgânica · Funções orgânicas).
# Habilidade: reconhecer as três funções nitrogenadas, dizer por que a amina é base e achar a amida em uma molécula de remédio.
# Pré-requisitos: QUI-ORG-008 (carboxila). Próxima: QUI-ORG-010 (haletos, CFC, DDT, nitrocomposto, tiol).
# Marcas: {cue} animação · [p=0.2] pausa. NH₃ = "ene agá três"; H⁺ = "agá mais"; CN = "cê ene"; CFC = "cê éfe cê"; DDT = "dê dê tê".
# Fatos: cheiro de peixe = trimetilamina; o ácido do limão reage com ela; amina é base pelo par livre do N (captura H⁺);
# amida quase não é base (o porquê fica para outra aula); etanamida CH3–CO–NH2; etanonitrila (acetonitrila) CH3–CN, solvente;
# paracetamol HO–C6H4–NH–CO–CH3: amida + fenol. Questão: lidocaína (anestésico local): N ligado ao anel e à carbonila = amida;
# N(C2H5)2 ligado ao CH2 = amina (terciária). Questão inédita, criada para esta aula.

TITULO = "Amina, amida e nitrila"

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
    dict(id="s01", block="gancho", text="{a}O cheiro de peixe vem de uma amina. [p=0.3] {b}E o limão ajuda a tirar esse cheiro, porque a amina reage com o ácido do limão. [p=0.2] {c}Tudo por causa de um nitrogênio."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai reconhecer {b}amina, amida e nitrila, [p=0.2] {c}entender por que a amina é uma base [p=0.2] e {d}achar a amida num remédio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}a carbonila é o cê, dupla, ó, [p=0.1] {b}e, no ácido carboxílico, ela vem com um ó agá ao lado. [p=0.3] {c}E, da aula de Lewis: [p=0.1] o nitrogênio faz três ligações [p=0.1] {d}e ainda fica com um par de elétrons livre."),
    # amina
    dict(id="s04", block="amina", text="{a}Comece pela amônia, ene agá três. [p=0.2] {b}Troque um agá por um carbono: [p=0.1] {c}é uma amina. [p=0.3] {d}Cê agá três, ene agá dois: [p=0.1] {e}o prefixo de um carbono, met, mais il e amina: metilamina."),
    dict(id="s05", block="amina", text="{a}Você pode trocar mais de um agá. [p=0.2] {b}Com três grupos cê agá três presos ao nitrogênio, não sobra agá nenhum: [p=0.1] {c}é a trimetilamina, com tri de três, a do cheiro de peixe."),
    dict(id="s06", block="amina", text="{a}Por que a amina é base? [p=0.2] {b}Base, aqui, é quem captura o agá mais, o cátion hidrogênio. [p=0.3] {c}O par livre do nitrogênio agarra esse agá mais. [p=0.3] {d}É assim que a amina reage com o ácido do limão. [p=0.2] {e}Ácidos e bases têm aula própria."),
    # amida e nitrila
    dict(id="s07", block="amida", text="{a}Agora, pegue o ácido carboxílico e troque o ó agá por ene agá dois. [p=0.2] {b}O nitrogênio fica colado na carbonila: [p=0.1] {c}é a amida. [p=0.3] {d}Cê agá três, cê ó, ene agá dois: a etanamida."),
    dict(id="s08", block="amida", text="{a}E a nitrila: [p=0.1] um carbono em tripla com o nitrogênio, na ponta da cadeia. [p=0.3] {b}Cê agá três, cê ene: a etanonitrila, um solvente de laboratório."),
    # o remédio
    dict(id="s09", block="remedio", text="{a}A amida aparece em muito remédio. [p=0.2] {b}Este é o paracetamol, um remédio comum para dor e febre. [p=0.3] {c}Procure o nitrogênio. [p=0.2] {d}Ele está colado num carbono que tem dupla com oxigênio: [p=0.1] {e}é uma amida. [p=0.3] {f}E o ó agá preso ao anel? [p=0.1] Fenol, da aula de álcool, fenol e éter."),
    # erro comum
    dict(id="s10", block="erro", text="{a}O erro mais comum é ver um nitrogênio e dizer amina. [p=0.3] {b}No paracetamol, o nitrogênio tem um agá e um carbono do anel, [p=0.1] e parece uma amina. [p=0.3] {c}Mas o outro vizinho dele é o carbono da carbonila. [p=0.2] {d}Nitrogênio colado em carbonila é amida."),
    # atalho
    dict(id="s11", block="atalho", text="{a}O atalho: [p=0.1] olhe os carbonos vizinhos do nitrogênio. [p=0.2] {b}Algum tem dupla com oxigênio? Amida. [p=0.2] {c}Ele está em tripla com o nitrogênio? Nitrila. [p=0.2] {d}Só ligações simples, sem carbonila ao lado? Amina."),
    dict(id="s12", block="atalho", text="{a}Funciona porque as três funções mudam só o que está preso ao nitrogênio. [p=0.3] {b}E guarde a diferença que cai em prova: [p=0.1] a amida quase não age como base. [p=0.2] {c}Por que, é assunto de outra aula."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}A lidocaína é um anestésico muito usado pelo dentista. [p=0.2] {b}Ela tem dois nitrogênios. [p=0.3] {c}Qual deles é de amina, e qual é de amida?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}O nitrogênio da esquerda está colado num carbono com dupla com oxigênio: [p=0.1] {b}amida. [p=0.3] {c}O da direita só tem ligações simples, com três carbonos, e nenhuma carbonila ao lado: [p=0.1] {d}amina, como a do peixe, sem nenhum agá."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}nitrogênio só com simples e sem carbonila ao lado é amina, uma base. [p=0.2] {b}Nitrogênio colado em carbonila é amida. [p=0.2] {c}E cê, tripla, ene é nitrila."),
    dict(id="s17", block="fim", text="Na próxima aula, entram {a}os haletos, com cloro e flúor. [p=0.2] Você vai ver {b}por que o cê éfe cê destrói a camada de ozônio [p=0.1] e {c}por que o dê dê tê se acumula no ambiente. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
