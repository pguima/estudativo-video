# Estudativo · QUI-ORG-026 — Polímeros de condensação (Química · Química Orgânica · Polímeros).
# Habilidade: reconhecer PET e náilon, apontar o éster e a amida da cadeia e dizer qual molécula pequena sai ao formar o polímero.
# Pré-requisitos: QUI-ORG-009, QUI-ORG-022. Próxima: QUI-ORG-027 (polímeros naturais, plásticos e reciclagem).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso; "6,6" = "seis seis".
# Fatos: PET = poli(tereftalato de etileno), de ácido tereftálico (HOOC–C6H4–COOH) + etilenoglicol (HO–CH2–CH2–OH), sai água;
# náilon 6,6 (1935, Carothers), de ácido adípico (HOOC–(CH2)4–COOH) + hexano-1,6-diamina (H2N–(CH2)6–NH2), sai água; os dois
# "6" contam os carbonos de cada monômero. Na indústria também se usa cloreto de ácido, que solta HCl: fica fora da aula.
# Questão inédita: poliéster de ácido adípico com etilenoglicol (sai água; monômeros: diácido + diálcool).

TITULO = "Polímeros de condensação"

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
    dict(id="s01", block="gancho", text="{a}A garrafa PET e a meia de náilon são polímeros, [p=0.2] mas não nascem como o polietileno. [p=0.3] {b}A cada ligação nova da cadeia, {c}sai uma molécula de água."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}reconhecer o PET e o náilon, [p=0.2] {c}apontar o éster e a amida na cadeia [p=0.2] e {d}dizer qual molécula pequena sai. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas aulas. [p=0.2] {a}Ácido mais álcool dá éster mais água: [p=0.1] {b}a ligação do éster é cê ó ó. [p=0.3] E {c}a amida tem o cê dupla ó ligado a um nitrogênio: [p=0.1] {d}cê ó, ene agá."),
    # condensação
    dict(id="s04", block="cond", text="Na condensação, {a}cada ligação nova entre dois monômeros solta uma molécula pequena, quase sempre água. [p=0.3] {b}Mas uma ligação só não faz cadeia. [p=0.2] Para a cadeia crescer, {c}cada monômero precisa de um grupo reativo em cada ponta."),
    dict(id="s05", block="cond", text="{a}Pense em peças de montar com encaixe nas duas pontas: [p=0.2] {b}encaixa uma, encaixa outra, e a fila cresce. [p=0.3] {c}Uma peça com encaixe numa ponta só fecha a fila."),
    # PET
    dict(id="s06", block="pet", text="O PET junta duas peças. [p=0.2] {a}A primeira é um ácido com cê ó ó agá nas duas pontas de um anel de benzeno: [p=0.1] o ácido tereftálico. [p=0.3] {b}A segunda é um álcool com ó agá nas duas pontas: [p=0.1] o etilenoglicol."),
    dict(id="s07", block="pet", text="{a}Cada cê ó ó agá encontra um ó agá, [p=0.2] {b}forma um éster [p=0.1] e {c}solta uma água. [p=0.3] {d}O éster se repete ao longo da cadeia: [p=0.2] é um poliéster. [p=0.3] {e}PET quer dizer poli tereftalato de etileno."),
    # náilon
    dict(id="s08", block="nailon", text="O náilon troca o álcool por {a}uma amina com ene agá dois nas duas pontas, a hexanodiamina, de seis carbonos. [p=0.3] {b}O outro monômero é um ácido com cê ó ó agá nas duas pontas, o ácido adípico. [p=0.3] {c}Cada cê ó ó agá encontra um ene agá dois, [p=0.2] {d}forma uma amida {e}e solta água."),
    dict(id="s09", block="nailon", text="{a}A amida se repete: é uma poliamida. [p=0.3] {b}No náilon seis seis, cada monômero tem seis carbonos, [p=0.2] e daí vem o nome."),
    # comparar
    dict(id="s10", block="compara", text="{a}Compare com a aula anterior. [p=0.2] {b}Na adição, a dupla abre e nada sai. [p=0.2] {c}Na condensação, dois grupos reagem e sai água."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}achar que qualquer ácido com qualquer álcool faz polímero. [p=0.3] {b}Ácido etanoico com etanol forma um éster só, [p=0.2] porque {c}cada um tem um grupo reativo. [p=0.2] {d}Depois da primeira ligação, não sobra ponta para continuar."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}procure cê ó ó ou cê ó ene agá que se repete na cadeia. [p=0.3] {b}Achou? É polímero de condensação, e saiu água. [p=0.3] {c}Para achar os monômeros, corte ali e devolva a água: [p=0.2] {d}o cê dupla ó ganha um ó agá e vira ácido, [p=0.2] {e}e o outro lado ganha um hidrogênio e vira álcool ou amina."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Na tela, a unidade de um polímero: [p=0.2] {b}um cê dupla ó, quatro cê agá dois, outro cê dupla ó, um oxigênio, dois cê agá dois e mais um oxigênio. [p=0.3] {c}Que grupo se repete? [p=0.2] {d}Que molécula saiu? [p=0.2] {e}E quais são os monômeros?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}O cê ó ligado ao oxigênio é um éster, [p=0.2] {b}então é um poliéster, e saiu água. [p=0.3] Agora, corte nos ésteres e devolva a água. [p=0.2] {c}O lado dos cê ó vira um ácido com cê ó ó agá nas duas pontas: [p=0.1] o ácido adípico. [p=0.3] {d}O lado dos oxigênios vira um álcool com ó agá nas duas pontas: [p=0.1] o etilenoglicol."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}na condensação, cada ligação solta uma molécula pequena, quase sempre água. [p=0.2] {b}O PET é um poliéster, [p=0.1] {c}o náilon é uma poliamida, [p=0.2] e {d}cada monômero precisa de grupos nas duas pontas."),
    dict(id="s17", block="fim", text="Na próxima aula, {a}os polímeros da natureza, como o amido e a borracha, [p=0.2] e {b}quais plásticos dá para reciclar derretendo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
