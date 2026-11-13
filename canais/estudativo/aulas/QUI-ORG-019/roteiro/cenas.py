# Estudativo · QUI-ORG-019 — Reações de substituição (Química · Química Orgânica · Reações orgânicas).
# Habilidade: escrever a cloração de um alcano e a nitração do benzeno e dizer qual hidrogênio sai primeiro.
# Pré-requisitos: QUI-ORG-004. Próxima: QUI-ORG-020 (eliminação: etanol vira eteno, o caminho oposto da adição).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso: CH4 = "cê agá quatro", HNO3 = "agá ene ó três".
# Fatos: CH4 + Cl2 → CH3Cl + HCl com luz ou calor; pode continuar até CCl4. Facilidade de saída do H: terciário > secundário >
# primário (na cloração do propano a 25 °C saem cerca de 55% com Cl no meio e 45% na ponta, mesmo com 6 H na ponta e 2 no meio).
# Nitração: C6H6 + HNO3 → C6H5NO2 + H2O, com H2SO4. O anel do benzeno troca em vez de abrir, porque é muito estável.
# Nomes de haletos e de ácidos inorgânicos não foram ensinados: a aula diz "o cloro no carbono do meio" e cita o ácido nítrico.
# Questão inédita: metilpropano + Br2 (luz) → o bromo entra no carbono terciário (mais de 99%; com Cl2 a 25 °C, o da ponta seria
# o principal, cerca de 63%, pelos nove H primários: por isso a questão usa bromo).

TITULO = "Reações de substituição"

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
    dict(id="s01", block="gancho", text="{a}No futebol, quando um jogador sai, outro entra no lugar dele, [p=0.2] e o time continua com o mesmo número de jogadores. [p=0.3] {b}Uma molécula sem ligação dupla também pode fazer essa troca: [p=0.2] {c}sai um hidrogênio, entra um cloro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escrever {b}a cloração de um alcano [p=0.2] e {c}a nitração do benzeno, [p=0.2] e {d}dizer qual hidrogênio sai primeiro. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas coisas. [p=0.2] {a}O alcano só tem ligações simples: [p=0.1] não tem ligação dupla. [p=0.3] E {b}o carbono pode ser primário, secundário ou terciário, [p=0.2] {c}se estiver ligado a um, dois ou três outros carbonos."),
    # o que é substituição
    dict(id="s04", block="troca", text="A reação de adição, da aula anterior, precisa de uma dupla. [p=0.2] Sem ela, o que acontece é {a}a substituição: [p=0.2] {b}um átomo sai da molécula [p=0.1] e {c}outro entra no lugar dele. [p=0.3] {d}Entram duas moléculas, e saem duas."),
    # cloração do metano
    dict(id="s05", block="metano", text="Veja o metano, {a}cê agá quatro, que forma quase todo o gás natural. [p=0.2] Junte {b}cloro, cê ele dois, com luz ou calor. [p=0.3] {c}A molécula de cloro se divide. [p=0.2] {d}Um cloro toma o lugar de um hidrogênio. [p=0.2] {e}O outro cloro sai junto com esse hidrogênio."),
    dict(id="s06", block="metano", text="Os produtos são {a}cê agá três cê ele, o metano com um cloro, [p=0.2] e {b}agá cê ele, um gás ácido. [p=0.3] {c}Com mais cloro, a troca continua, um hidrogênio por vez."),
    # qual H sai primeiro
    dict(id="s07", block="qual", text="Agora, uma molécula maior: {a}o propano, cê agá três, cê agá dois, cê agá três. [p=0.3] {b}Os hidrogênios das pontas estão em carbonos primários. [p=0.2] {c}Os do meio, num carbono secundário. [p=0.3] Qual sai primeiro?"),
    dict(id="s08", block="qual", text="{a}O hidrogênio de carbono secundário sai com mais facilidade que o de primário. [p=0.3] {b}E o de terciário, mais fácil ainda. [p=0.3] Por isso, {c}o produto principal tem o cloro no carbono do meio, [p=0.2] mesmo que as pontas tenham {d}seis hidrogênios, contra só dois no meio."),
    # benzeno
    dict(id="s09", block="benzeno", text="O benzeno também faz substituição. [p=0.2] {a}Ele tem duplas no anel, [p=0.2] mas {b}o anel é muito estável, e prefere trocar a se abrir. [p=0.3] Na nitração, ele reage com {c}ácido nítrico, agá ene ó três, [p=0.2] com um pouco de ácido sulfúrico ajudando."),
    dict(id="s10", block="benzeno", text="{a}Um hidrogênio do anel sai, [p=0.2] {b}e o grupo ene ó dois, chamado nitro, entra no lugar. [p=0.3] {c}O hidrogênio que saiu se junta com um ó agá do ácido, [p=0.2] e {d}forma água. [p=0.3] O produto é {e}o nitrobenzeno."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}achar que o benzeno faz adição, só porque tem duplas. [p=0.3] {b}Se as duplas abrissem, o anel perderia a estabilidade. [p=0.2] {c}Em prova, benzeno com ácido nítrico, cloro ou bromo, com um ajudante na reação, faz substituição: [p=0.2] {d}o anel continua inteiro."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho para saber de onde sai o hidrogênio: [p=0.2] {a}terciário, depois secundário, depois primário. [p=0.3] Pense assim: {b}o carbono com mais carbonos vizinhos solta o hidrogênio mais fácil. [p=0.3] {c}O motivo está no caminho da reação, e fica para outra aula."),
    dict(id="s13", block="atalho", text="{a}Não perca tempo com a ordem quando todos os hidrogênios são iguais, [p=0.2] como no metano e no etano. [p=0.3] {b}Aí, qualquer troca dá o mesmo produto."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}O metilpropano tem três grupos cê agá três presos a um carbono central, que tem um hidrogênio. [p=0.3] Ele reage com bromo e luz. [p=0.2] {b}De que carbono sai o hidrogênio mais fácil? [p=0.2] {c}E onde fica o bromo no produto principal?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Classifique os carbonos. [p=0.2] {a}Cada cê agá três está ligado a um carbono só: [p=0.1] primário. [p=0.2] {b}O carbono central está ligado a três carbonos: [p=0.1] terciário. [p=0.3] {c}Terciário solta o hidrogênio mais fácil. [p=0.2] Então {d}o bromo fica no carbono central."),
    dict(id="s17", block="resposta", text="Repare: {a}são nove hidrogênios nas pontas e só um no centro, [p=0.2] e mesmo assim, {b}com bromo, quase todo o produto é o do centro. [p=0.3] {c}O bromo escolhe o hidrogênio muito mais que o cloro."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}na substituição, um átomo sai e outro entra no lugar. [p=0.2] {b}O alcano troca hidrogênio por cloro, [p=0.1] {c}o benzeno troca hidrogênio por nitro, [p=0.2] e {d}o hidrogênio sai primeiro do carbono terciário."),
    dict(id="s19", block="fim", text="Na próxima aula, a eliminação: [p=0.2] {a}o etanol perde uma molécula de água e vira eteno, [p=0.2] {b}o caminho oposto da adição. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
