# Divulgação da série Introdução da Redação (Redação ENEM) em outras redes — HORIZONTAL 1920x1080, ~65 s.
# Para YouTube (feed), Facebook (feed), X e LinkedIn. Mesmo gancho do Short (o 1º quadro já mostra o clichê e a
# pergunta; carimbo PARE! em ~1,5 s) + um bloco curto por episódio (com a capa real), a série anterior
# (Leitura da Proposta) e o convite para as playlists "Redação: Introdução" e "Redação ENEM do Zero".
# Sem religião nos exemplos. Visual em ../divulgacao_visual.py. Marcas: {cue} · *destaque* · [p=0.2] pausa

TITULO = "Sua redação começa com \"Desde os primórdios\"? A série Introdução da Redação"

VOZ = dict(
    tags=["animada", "confiante", "curiosa"],
    prompt=("Narre um vídeo curto de divulgação para estudantes do ENEM: voz de professor jovem, carismático e "
            "MUITO envolvente, falando direto com o aluno. Energia alta já na primeira palavra, sem introdução. "
            "Tom de alerta no gancho, de revelação nas três perguntas, ritmo de lista animada nos episódios e "
            "entusiasmo no convite final. Ritmo ágil mas claro, com ênfase nas palavras-chave. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {"ENEM": "Enem"}

RITMO = dict(gap_bloco=0.15, pad_inicio=0.0, pad_fim=1.5)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Se a sua redação começa assim, [p=0.1] {b}*pare agora.*"),
    dict(id="02", block="generico", text=
        "{a}*Desde os primórdios* serve pra *qualquer tema.* [p=0.15] {b}Por isso, não diz *nada* sobre o seu."),
    dict(id="03", block="perguntas", text=
        "{a}Uma boa introdução responde *três perguntas:* [p=0.1] {b}de onde parte a discussão, [p=0.1] "
        "{c}o que você defende [p=0.1] {d}e por quais caminhos vai provar."),
    dict(id="04", block="intro", text=
        "{a}Na série *Introdução da Redação,* [p=0.1] {b}você aprende, em *sete aulas,* do zero:"),
    dict(id="05", block="eps", text="{a}as *três perguntas* que o primeiro parágrafo responde;"),
    dict(id="06", block="eps", text="{a}*quatro jeitos* de começar, sem *desde os primórdios;*"),
    dict(id="07", block="eps", text="{a}a *ponte* e o *teste da retirada* do repertório;"),
    dict(id="08", block="eps", text="{a}por que *opinião não é tese,* e como antecipar os argumentos;"),
    dict(id="09", block="eps", text="{a}introduções *fracas* e *boas,* e as *sete armadilhas;*"),
    dict(id="10", block="eps", text="{a}uma *oficina* para escrever a introdução do zero, em *seis passos;*"),
    dict(id="11", block="eps", text="{a}e uma revisão com *dez pegadinhas* e um *desafio.*"),
    dict(id="12", block="anteriores", text=
        "{a}E se você ainda não viu, [p=0.1] {b}a série *Leitura da Proposta* vem antes: [p=0.1] "
        "{c}ela ensina a ler o tema *sem fugir dele.*"),
    dict(id="13", block="cta", text=
        "{a}As sete aulas estão no canal *Estudativo,* no YouTube, [p=0.1] {b}na playlist *Redação: Introdução.* "
        "[p=0.2] {c}E, para a redação completa, [p=0.1] siga a playlist *Redação ENEM do Zero.* [p=0.2] "
        "{d}Te vejo na primeira aula!"),
]
