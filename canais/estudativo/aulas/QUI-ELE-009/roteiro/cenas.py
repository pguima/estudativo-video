# Estudativo · QUI-ELE-009 — Eletrólise aquosa (Química · Eletroquímica e Radioatividade · Eletrólise).
# Habilidade: prever o que sai em cada polo na eletrólise de NaCl e de CuSO₄ em água e explicar como se cobre uma peça de
# metal e se refina o cobre.
# Pré-requisitos: QUI-ELE-008. Próxima: QUI-ELE-010 (leis de Faraday: 10 A por 1.930 s depositam 6,35 g de cobre).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Ordem de descarga (regra de prova):
#   cátodo: cátions da família 1, da família 2 e Al³⁺ NÃO descarregam → a água se reduz: 2 H₂O + 2 e⁻ → H₂ + 2 OH⁻;
#           os outros metais (Cu²⁺, Ag⁺, Ni²⁺, Zn²⁺...) descarregam e o metal se deposita.
#   ânodo: ânions sem oxigênio (Cl⁻, Br⁻, I⁻) descarregam → Cl₂, Br₂, I₂; ânions com oxigênio (SO₄²⁻, NO₃⁻) e o F⁻ NÃO →
#          a água se oxida: 2 H₂O → O₂ + 4 H⁺ + 4 e⁻.
# NaCl(aq): cátodo H₂, ânodo Cl₂, sobra NaOH (soda cáustica) na solução. CuSO₄(aq): cátodo Cu, ânodo O₂, sobra H₂SO₄.
# Galvanoplastia: a peça é o cátodo, numa solução de íons do metal de cobertura; com ânodo do mesmo metal, ele se dissolve e
# repõe os íons. Refino: ânodo de cobre impuro, cátodo de cobre puro, solução de CuSO₄; o cobre passa de uma placa à outra
# (99,9%); ouro e prata caem no fundo como lama.
# Questão: AgNO₃(aq) → cátodo Ag, ânodo O₂; KI(aq) → cátodo H₂, ânodo I₂.

TITULO = "Eletrólise aquosa"

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
    dict(id="s01", block="gancho", text="{a}Derreta sal de cozinha e passe corrente: [p=0.1] sai sódio no cátodo. [p=0.3] {b}Agora dissolva o mesmo sal em água e faça igual. [p=0.3] {c}No cátodo, não aparece sódio nenhum. [p=0.2] {d}Saem bolhas de gás hidrogênio. [p=0.2] {e}Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai prever {b}o que sai em cada polo quando o sal está na água, [p=0.2] e explicar como se {c}cobre uma peça de metal [p=0.1] e se {d}purifica o cobre. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de uma coisa: [p=0.2] {a}na eletrólise, o cátion vai ao cátodo, o negativo, e ganha elétrons; [p=0.2] {b}o ânion vai ao ânodo, o positivo, e perde. [p=0.2] Se faltar, procure no canal."),
    # a disputa
    dict(id="s04", block="disputa", text="Na água, os polos têm uma concorrente: {a}a própria água. [p=0.3] {b}No cátodo, a água também pode ganhar elétrons [p=0.1] {c}e soltar gás hidrogênio. [p=0.3] {d}No ânodo, ela também pode perder elétrons [p=0.1] {e}e soltar gás oxigênio. [p=0.3] {f}Em cada polo, só um ganha a disputa."),
    # cátodo
    dict(id="s05", block="catodo", text="{a}No cátodo, a regra é: [p=0.1] {b}os metais da família um, da família dois e o alumínio perdem para a água. [p=0.3] {c}Sódio, potássio, cálcio, magnésio, alumínio: [p=0.1] {d}com eles, sai hidrogênio. [p=0.3] {e}Os outros metais, como cobre, prata, níquel e zinco, ganham: [p=0.1] {f}o metal se deposita na placa."),
    # ânodo
    dict(id="s06", block="anodo", text="{a}No ânodo, a regra é: [p=0.1] {b}os ânions sem oxigênio ganham da água, menos o fluoreto. [p=0.2] {c}Cloreto, brometo, iodeto: [p=0.1] {d}sai cloro, bromo ou iodo. [p=0.3] {e}Os ânions com oxigênio, como sulfato e nitrato, perdem para a água: [p=0.1] {f}sai gás oxigênio."),
    # NaCl
    dict(id="s07", block="nacl", text="Volte ao sal na água. [p=0.2] {a}No cátodo, o sódio é da família um: perde. [p=0.1] {b}A água ganha: solta gás hidrogênio e deixa íons hidróxido. [p=0.3] {c}No ânodo, o cloreto não tem oxigênio: ganha. [p=0.1] {d}Sai gás cloro."),
    dict(id="s08", block="nacl", text="{a}Na solução, sobram o sódio mais e esse hidróxido: [p=0.1] {b}é a soda cáustica, o hidróxido de sódio. [p=0.3] {c}Essa eletrólise faz, de uma vez, cloro, hidrogênio e soda, [p=0.1] produtos de uma indústria inteira."),
    # CuSO4
    dict(id="s09", block="cuso4", text="Agora, o sulfato de cobre, azul, com placas que não reagem, de grafite. [p=0.2] {a}No cátodo, o cobre não é família um, nem dois, nem alumínio: [p=0.1] {b}ele ganha, e a placa se cobre de cobre. [p=0.3] {c}No ânodo, o sulfato tem oxigênio: perde. [p=0.1] {d}A água se oxida, e sai gás oxigênio. [p=0.3] {e}E o azul vai sumindo, porque o cobre dois mais está virando metal."),
    # galvanoplastia
    dict(id="s10", block="aplica", text="Daí vem a {a}galvanoplastia: cobrir uma peça com metal. [p=0.2] {b}Ligue a peça ao polo negativo, como cátodo, numa solução de cobre. [p=0.2] {c}O cobre se deposita nela, numa camada fina e lisa. [p=0.3] {d}Com níquel, cromo ou prata na solução, sai um talher prateado, uma torneira cromada."),
    dict(id="s11", block="aplica", text="{a}E se o ânodo também for de cobre? [p=0.2] {b}Aí ele mesmo perde elétrons e se dissolve, [p=0.1] repondo o cobre que foi para a peça. [p=0.3] {c}É assim que se refina o cobre: [p=0.1] {d}o ânodo é o cobre impuro, o cátodo é uma placa de cobre puro. [p=0.2] {e}O cobre passa de uma placa à outra, [p=0.1] {f}e o ouro e a prata, que estavam misturados, caem no fundo."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a eletrólise do sal na água dá sódio, como no sal derretido. [p=0.3] {b}Na água, o sódio perde a disputa. [p=0.2] {c}E, mesmo que se formasse, o sódio metálico reagiria com a água na hora."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}família um, família dois ou alumínio no cátodo? [p=0.1] {b}Sai hidrogênio. [p=0.3] {c}Ânion com oxigênio no ânodo? [p=0.1] {d}Sai oxigênio. [p=0.3] {e}Em qualquer outro caso, sai o próprio íon: [p=0.1] o metal, ou o cloro, o bromo e o iodo."),
    dict(id="s14", block="atalho", text="Funciona porque {a}esses metais perdem elétrons com tanta facilidade que não aceitam recebê-los de volta, [p=0.1] {b}e os ânions com oxigênio seguram os seus. [p=0.3] {c}Não compensa quando o ânodo é de um metal que se dissolve, como no refino: [p=0.1] {d}aí, quem se oxida é a própria placa."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O que sai em cada polo na eletrólise do nitrato de prata em água? [p=0.3] {b}E na do iodeto de potássio em água?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Nitrato de prata: [p=0.1] {b}a prata não é família um, nem dois, nem alumínio: [p=0.1] sai prata no cátodo. [p=0.3] {c}O nitrato tem oxigênio: [p=0.1] sai gás oxigênio no ânodo."),
    dict(id="s18", block="resposta", text="{a}Iodeto de potássio: [p=0.1] {b}o potássio é da família um: [p=0.1] sai hidrogênio no cátodo. [p=0.3] {c}O iodeto não tem oxigênio: [p=0.1] sai iodo no ânodo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}na água, família um, dois e alumínio dão hidrogênio no cátodo; [p=0.1] {b}ânion com oxigênio dá oxigênio no ânodo; [p=0.1] {c}e a peça a cobrir vai no cátodo."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai calcular {a}quanto metal se deposita: [p=0.2] {b}uma corrente de dez ampères, durante mil novecentos e trinta segundos, deposita seis vírgula trinta e cinco gramas de cobre. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
