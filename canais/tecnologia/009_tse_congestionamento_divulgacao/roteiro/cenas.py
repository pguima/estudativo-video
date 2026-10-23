# Roteiro — Tecnologia 009: O que aconteceu com o sistema do TSE durante a divulgação dos votos?
# Base: roteiro do usuário (texto literal das cenas 01–06) + fatos verificados em original/fonte_tse_congestionamento.md
# Frases ACRESCENTADAS ao texto do usuário (todas com fonte): marcadas com  # + no comentário de cada cena.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "O que aconteceu com o sistema do TSE durante a divulgação dos votos?"

VOZ = dict(
    tags=["confiante", "formal"],
    prompt=("Narre como o locutor de um minidocumentário jornalístico de televisão: voz masculina adulta, grave, segura, "
            "investigativa e com muita credibilidade. Tom sóbrio e equilibrado, sem alarmismo, sem drama exagerado e sem "
            "sensacionalismo. Ritmo de documentário: calmo, firme, bem articulado, respeitando as pausas entre as frases. "
            "Nas perguntas, entonação de pergunta genuína, reflexiva. Leia apenas o texto, exatamente como está escrito, "
            "sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {}

SCENES = [
    # ================= CENA 01 — ABERTURA =================
    dict(id="01", block="abertura", text=
        "{a}Milhões de brasileiros acompanhavam a *divulgação* dos resultados eleitorais [p=0.3] {b}quando algo inesperado "
        "aconteceu: [p=0.3] {c}o sistema nacional de divulgação do TSE [p=0.2] apresentou um *congestionamento.* [p=0.8] "
        "{q}Mas o que *realmente* aconteceu? [p=1.6] {r}A contagem dos votos [p=0.2] foi *interrompida?*"),

    # ================= CENA 02 — O CONGESTIONAMENTO =================
    # + "Foi no domingo, quatro de outubro..." (Agência Brasil, 04/10/2026)
    dict(id="02", block="congest", text=
        "{d}Foi no domingo, *quatro de outubro* de dois mil e vinte e seis, [p=0.2] primeiro turno das eleições. [p=0.6] "
        "{a}Segundo a explicação apresentada pelo Tribunal Superior Eleitoral, [p=0.2] o sistema responsável pela "
        "*divulgação nacional* dos resultados [p=0.2] {b}enfrentou um *congestionamento* no processamento de dados. [p=0.6] "
        "{c}Isso provocou uma *interrupção temporária* [p=0.2] na atualização das informações apresentadas ao público."),
    # + horários/percentuais e "cerca de uma hora" (Agência Brasil 04/10 e JB 05/10/2026); citação (Brasil 61, 04/10/2026)
    dict(id="03", block="linha", text=
        "{a}Por volta das *dezenove horas,* [p=0.2] a totalização para presidente parou em *sessenta e quatro por cento.* "
        "[p=0.6] {b}Só voltou a andar por volta das *vinte horas,* [p=0.2] já em *oitenta e quatro por cento.* [p=0.6] "
        "{c}Um atraso de *cerca de uma hora,* [p=0.2] segundo o presidente do TSE, [p=0.2] ministro *Kassio Nunes Marques.* "
        "[p=0.6] {d}Nas palavras dele: [p=0.3] *antes da eficiência ou da rapidez,* [p=0.2] prezamos pela segurança."),

    # ================= CENA 03 — A CONTAGEM DOS VOTOS PAROU? =================
    dict(id="04", block="etapas", text=
        "{t}Para entender a situação, [p=0.2] precisamos conhecer três etapas diferentes do processo eleitoral: [p=0.3] "
        "{a}*apuração,* [p=0.3] {b}*totalização* [p=0.3] {c}e *divulgação.* [p=0.6] "
        "{d}A apuração contabiliza os votos registrados nas *urnas.* [p=0.5] "
        "{e}A totalização *reúne* os resultados. [p=0.5] "
        "{f}Já a divulgação *apresenta* essas informações para a população."),
    # + "segundo o TSE, a dificuldade ficou restrita à divulgação..." (portal do TSE, 04/10/2026)
    dict(id="05", block="visualiza", text=
        "{a}Uma falha na *visualização* dos resultados [p=0.2] não significa, *necessariamente,* [p=0.2] "
        "que os votos deixaram de ser contabilizados. [p=0.6] {b}E, segundo o TSE, [p=0.2] a dificuldade ficou restrita "
        "à *divulgação* [p=0.2] {c}e não afetou a *totalização* dos votos."),

    # ================= CENA 04 — HOUVE FRAUDE? =================
    dict(id="06", block="fraude", text=
        "{a}O episódio levantou *questionamentos* sobre a segurança da divulgação eleitoral. [p=0.6] "
        "{b}Entretanto, [p=0.2] é importante separar uma *falha técnica* [p=0.2] {c}de uma possível *manipulação* de "
        "resultados. [p=0.6] {d}A existência de um congestionamento *não comprova,* por si só, [p=0.2] qualquer alteração "
        "nos votos. [p=0.6] {e}Para compreender completamente o incidente, [p=0.2] são necessárias informações técnicas "
        "*verificáveis.*"),

    # ================= CENA 05 — AS PERGUNTAS =================
    # + "Até a produção deste vídeo..." (busca em 22/10/2026: nenhum relatório técnico público encontrado)
    dict(id="07", block="perguntas", text=
        "{z}Até a produção deste vídeo, [p=0.2] não encontramos um relatório técnico público [p=0.2] detalhando o incidente. "
        "[p=0.6] {t}Do ponto de vista tecnológico, [p=0.2] algumas perguntas são *fundamentais.* [p=0.6] "
        "{a}Qual *componente* do sistema enfrentou o congestionamento? [p=0.8] "
        "{b}Por que a infraestrutura não conseguiu *absorver* o volume de dados? [p=0.8] "
        "{c}Quais mecanismos de *redundância* foram acionados? [p=0.8] "
        "{d}E quais medidas podem *impedir* que o problema volte a acontecer?"),

    # ================= CENA 06 — ENCERRAMENTO =================
    dict(id="08", block="fim", text=
        "{a}Em um processo eleitoral, [p=0.2] a *confiança* depende não apenas da segurança dos sistemas, [p=0.2] "
        "mas também da *transparência* sobre seu funcionamento. [p=0.6] {b}Investigar falhas, [p=0.2] divulgar explicações "
        "técnicas [p=0.2] e implementar melhorias [p=0.2] são medidas fundamentais para fortalecer essa confiança. [p=0.7] "
        "{c}Afinal, [p=0.2] compreender o que aconteceu [p=0.2] é tão importante quanto evitar que aconteça *novamente.* "
        "{x}[p=4.0]"),

    # ================= CTA + FONTES =================
    dict(id="09", block="cta", text=
        "Se esse vídeo te ajudou a entender o caso, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal "
        "[p=0.2] {bell}e ative o *sininho,* para não perder os próximos vídeos. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual dessas perguntas você gostaria de ver respondida? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.0]"),
    dict(id="10", block="fontes", text=
        "{a}As *fontes* deste vídeo [p=0.2] estão na tela [p=0.2] e na descrição. [p=5.0]"),
]
