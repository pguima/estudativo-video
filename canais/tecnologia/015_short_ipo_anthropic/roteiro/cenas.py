# Short — Tecnativo 015: a Anthropic (empresa do Claude) pediu para abrir capital na Nasdaq
# Base: original/fonte_ipo_anthropic.md (S-1 de 26/10/2026 + imprensa). Marcas: {cue} animação · *texto* destaque ·
# [p=0.2] pausa · números por extenso (viram algarismos na legenda, ver NUMEROS no visual.py)

TITULO = "A empresa do Claude perdeu 80 bilhões em 6 meses e vai para a bolsa"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia e negócios: voz masculina adulta, grave, enérgica e empolgada, como quem "
            "conta para um amigo uma notícia chocante que acabou de ler. Ritmo rápido e energia alta desde a primeira "
            "palavra, sem introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. "
            "Tom provocador e divertido na pergunta final. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}A empresa do *Claude* perdeu *oitenta bilhões de dólares* [p=0.1] em *seis meses.* [p=0.2] "
        "{b}E mesmo assim [p=0.1] quer fazer a *maior estreia da história* da bolsa."),
    dict(id="02", block="s1", text=
        "{a}Na segunda-feira, [p=0.1] a *Anthropic* entregou o pedido oficial [p=0.1] {b}para vender ações na *Nasdaq.*"),
    dict(id="03", block="receita", text=
        "{a}E olha a receita: [p=0.1] em dois mil e vinte e três, *quarenta e um milhões* de dólares. [p=0.1] "
        "{b}Em dois mil e vinte e cinco, *quatro vírgula seis bilhões.* [p=0.1] "
        "{c}E só no primeiro semestre deste ano: [p=0.1] *dezesseis vírgula três bilhões.*"),
    dict(id="04", block="prejuizo", text=
        "{a}Então, [p=0.1] e o prejuízo? [p=0.2] {b}*Setenta e dois bilhões* dele são *contabilidade:* [p=0.1] "
        "{c}a empresa passou a valer tanto [p=0.1] que as dívidas que viram ações *encareceram* no balanço. [p=0.2] "
        "{d}Na operação, [p=0.1] o prejuízo foi de *seiscentos e noventa e três milhões.*"),
    dict(id="05", block="recorde", text=
        "{a}A imprensa americana fala em captar *cem bilhões* de dólares, [p=0.1] "
        "{b}acima do recorde da *SpaceX,* [p=0.1] *setenta e cinco bilhões,* em junho. [p=0.2] "
        "{c}O preço da ação ainda nem saiu."),
    dict(id="06", block="controle", text=
        "{a}Mas tem um detalhe: [p=0.1] os *sete fundadores* ficam com *cinquenta vírgula um por cento* dos votos, [p=0.1] "
        "{b}e um *fundo independente* elege a maioria do conselho."),
    dict(id="07", block="final", text=
        "{a}E aí: [p=0.1] você compraria uma ação da empresa do Claude? [p=0.2] {b}Ou acha que é *bolha?*"),
]
