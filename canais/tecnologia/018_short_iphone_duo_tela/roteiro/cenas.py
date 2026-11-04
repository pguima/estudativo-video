# Short — Tecnativo 018: a tela do iPhone dobrável (iPhone Duo) está rachando
# Base: original/fonte_iphone_duo_tela.md (CNBC 26/10, iFixit 25/10, Fortune 27/10/2026). Marcas: {cue} animação ·
# *texto* destaque · [p=0.2] pausa · números por extenso (viram algarismos na legenda, ver NUMEROS no visual.py)

TITULO = "A tela do iPhone dobrável está rachando (e o conserto custa metade do celular)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia: voz masculina adulta, grave, enérgica e empolgada, como quem conta para "
            "um amigo uma polêmica que acabou de estourar. Ritmo rápido e energia alta desde a primeira palavra, sem "
            "introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. Tom "
            "provocador na pergunta final. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}O primeiro iPhone *dobrável* custa quase *dois mil dólares.* [p=0.2] "
        "{b}E tem dono vendo a tela *rachar* [p=0.1] em poucas horas."),
    dict(id="02", block="relatos", text=
        "{a}O iPhone Duo chegou às lojas na sexta. [p=0.1] {b}Em dias, vieram os relatos: [p=0.1] a pessoa abre o "
        "celular, [p=0.1] ouve um *estalo,* [p=0.1] {c}e aparece uma *linha branca* na tela."),
    dict(id="03", block="apple", text=
        "{a}A Apple confirmou o problema, [p=0.1] em um *pequeno número* de aparelhos. [p=0.2] "
        "{b}Quem for afetado [p=0.1] *troca* o celular pela garantia."),
    dict(id="04", block="causa", text=
        "{a}E a causa? [p=0.1] O iFixit *desmontou* o aparelho. [p=0.1] {b}As quebras aparecem perto da *dobradiça,* "
        "[p=0.1] {c}onde uma barra de apoio pode estar *apertando a tela.* [p=0.1] Mas isso ainda é *hipótese.*"),
    dict(id="05", block="conta", text=
        "{a}Agora, a parte que dói: [p=0.1] fora da garantia, [p=0.1] trocar a tela interna custa "
        "*novecentos e noventa e nove dólares.* [p=0.2] {b}*Metade* do preço do celular."),
    dict(id="06", block="areia", text=
        "{a}Ninguém sabe ainda quantos aparelhos foram afetados, [p=0.1] e tem até *foto falsa* circulando. [p=0.2] "
        "{b}Mas o chefe do iFixit avisou: [p=0.1] um *grão de areia* [p=0.1] pode matar essa tela."),
    dict(id="07", block="final", text=
        "{a}E aí: [p=0.1] você pagaria isso [p=0.1] num celular que dobra? [p=0.2] {b}Ou vai esperar a *segunda geração?*"),
]
