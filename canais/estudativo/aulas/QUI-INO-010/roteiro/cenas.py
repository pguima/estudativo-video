# Estudativo · QUI-INO-010 — Simples troca e fila de reatividade (Química · Funções e Reações Inorgânicas · Reações e balanceamento).
# Habilidade: dizer pela fila de reatividade por que o zinco reage com HCl e o cobre não.
# Pré-requisitos: QUI-INO-001, QUI-INO-008. Próxima: QUI-INO-011 (dupla troca).
# "Já ensinado" NÃO tem sais nem nomes de sal (QUI-INO-003) nem síntese/análise (QUI-INO-009): o produto ZnCl₂ fica só na
# tela, sem nome; a solução de cobre é dita "com íons de cobre". Substância simples/composta é explicada na hora.
# Fatos: Zn + 2 HCl → ZnCl₂ + H₂ (bolhas de hidrogênio); Cu + HCl não reage. Fila dos metais (livros brasileiros):
# K > Ca > Na > Mg > Al > Zn > Fe > ... > H > Cu > Hg > Ag > Pt > Au. Fe + Cu²⁺ → Fe²⁺ + Cu (prego cobreado na solução azul).
# Fila dos ametais: F > O > Cl > Br > I > S (só F, Cl, Br, I na aula). Cl₂ + 2 NaBr → 2 NaCl + Br₂.
# Questão inédita: Mg + 2 HCl → MgCl₂ + H₂ (reage); Ag + HCl não; Cu + 2 Ag⁺ → Cu²⁺ + 2 Ag (reage: a "árvore de prata").

TITULO = "Simples troca e fila de reatividade"

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
    dict(id="s01", block="gancho", text="{a}Ponha um pedaço de zinco no ácido clorídrico: [p=0.1] {b}borbulha. [p=0.3] {c}Ponha um fio de cobre no mesmo ácido: [p=0.1] {d}nada acontece. [p=0.3] {e}Os dois são metais. [p=0.1] Por que só um reage?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer uma simples troca [p=0.2] e {b}usar a fila de reatividade para prever se ela acontece."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}metal tende a perder elétrons e virar íon positivo. [p=0.3] E {b}o ácido clorídrico, na água, solta o íon agá mais e o íon cê éle menos."),
    # simples troca
    dict(id="s04", block="troca", text="Primeiro, duas palavras. [p=0.2] {a}Substância simples é feita de um elemento só, como o zinco ou o gás hidrogênio. [p=0.3] {b}Substância composta tem mais de um, como o agá cê éle."),
    dict(id="s05", block="troca", text="{a}Na simples troca, uma substância simples [p=0.1] {b}toma o lugar de um elemento numa composta. [p=0.3] {c}Á, mais bê cê, produz á cê, mais bê. [p=0.3] {d}O á entrou, e o bê saiu sozinho."),
    dict(id="s06", block="troca", text="Veja o zinco. [p=0.2] {a}Zê ene, mais dois agá cê éle, [p=0.1] {b}produz zê ene cê éle dois, mais agá dois. [p=0.3] {c}O zinco tomou o lugar do hidrogênio. [p=0.2] {d}O hidrogênio saiu como gás: [p=0.1] são as bolhas."),
    # por que
    dict(id="s07", block="fila", text="Mas a troca só acontece {a}se quem entra for mais reativo do que quem sai. [p=0.3] {b}Mais reativo é quem perde elétrons com mais facilidade. [p=0.3] {c}O zinco perde elétrons mais fácil que o hidrogênio, [p=0.1] e por isso o empurra para fora."),
    dict(id="s08", block="fila", text="Os metais têm uma ordem: [p=0.1] {a}a fila de reatividade. [p=0.2] {b}Mais reativos à esquerda: [p=0.1] potássio, cálcio, sódio, magnésio, alumínio, zinco e ferro. [p=0.3] {c}No meio, o hidrogênio. [p=0.3] {d}Depois, os menos reativos: [p=0.1] cobre, prata e ouro."),
    dict(id="s09", block="fila", text="{a}O cobre está depois do hidrogênio: é menos reativo. [p=0.2] {b}Ele não consegue empurrar o hidrogênio, [p=0.1] e {c}o cobre não reage com o ácido. [p=0.3] {d}Pela mesma razão, ouro e prata quase não reagem, [p=0.1] e duram séculos em joias."),
    # metal com metal
    dict(id="s10", block="metais", text="A fila vale entre metais também. [p=0.2] {a}Mergulhe um prego de ferro numa solução azul, com íons de cobre. [p=0.3] {b}O ferro é mais reativo: [p=0.1] {c}ele vira íon e vai para a solução, [p=0.1] {d}e o cobre se deposita no prego, avermelhado."),
    dict(id="s11", block="metais", text="{a}E o contrário? [p=0.1] Um fio de cobre numa solução com íons de ferro. [p=0.3] {b}O cobre está à direita do ferro na fila: é menos reativo. [p=0.2] {c}Ele não toma o lugar do ferro, [p=0.1] {d}e nada acontece."),
    dict(id="s12", block="metais", text="{a}Para os ametais há outra fila: [p=0.1] {b}flúor, cloro, bromo e iodo, nessa ordem. [p=0.3] {c}O cloro toma o lugar do bromo, [p=0.1] {d}mas o iodo não toma o lugar do cloro. [p=0.3] {e}Nos ametais, mais reativo é quem ganha elétron com mais facilidade."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}achar que todo metal reage com ácidos como o clorídrico. [p=0.3] {b}Só reage quem está antes do hidrogênio na fila. [p=0.3] {c}Cobre, prata e ouro ficam parados no ácido clorídrico."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.1] {a}ache os dois que disputam o lugar, [p=0.1] {b}o que está sozinho e o que está preso. [p=0.3] {c}O sozinho está mais à esquerda na fila? Reage. [p=0.2] {d}Está à direita? Não reage."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o mais reativo sempre fica com a posição de íon. [p=0.3] {b}Não compensa decorar a fila inteira: [p=0.1] {c}guarde o hidrogênio no meio, o ouro na ponta, [p=0.1] e use a fila que o enunciado costuma dar."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Use a fila da tela. [p=0.2] {a}Qual destes reage com ácido clorídrico: o magnésio ou a prata? [p=0.3] E {b}um fio de cobre numa solução com íons de prata, á gê mais: [p=0.1] {c}há troca?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O magnésio está antes do hidrogênio: [p=0.1] {b}reage, e solta gás hidrogênio. [p=0.3] {c}A prata está depois: [p=0.1] {d}não reage."),
    dict(id="s19", block="resposta", text="{a}O cobre está antes da prata na fila: [p=0.1] {b}é mais reativo. [p=0.2] {c}Então há troca: [p=0.1] o cobre vira íon e vai para a solução, [p=0.1] {d}e a prata se deposita no fio, como uma árvore prateada."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}na simples troca, um elemento sozinho toma o lugar de outro; [p=0.2] {b}só acontece se ele for mais reativo; [p=0.1] e {c}quem está antes do hidrogênio reage com ácidos como o clorídrico."),
    dict(id="s21", block="fim", text="Na próxima aula, são dois compostos que trocam de parceiros: [p=0.2] {a}a dupla troca, [p=0.1] {b}que só acontece se formar um sólido, um gás ou água. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
