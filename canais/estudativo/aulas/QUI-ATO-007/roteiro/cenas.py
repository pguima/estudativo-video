# Estudativo · QUI-ATO-007 — Praticando: átomos e distribuição eletrônica (Química · Átomo e Tabela Periódica · prática).
# Habilidade: identificar modelos atômicos em textos e fazer contas de partículas e de distribuição eletrônica.
# Pré-requisitos: QUI-ATO-001 a QUI-ATO-006. Próxima: QUI-ATO-008 (períodos e famílias).
# Questões inéditas, criadas para esta aula.
# Contas: íon com 16 p, 16 n, 18 e → Z 16 (enxofre), A 32, carga 16 − 18 = −2; ³²S e ³⁴S são isótopos (Z 16);
# K (19) = 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ → valência 1; K⁺ = 1s² 2s² 2p⁶ 3s² 3p⁶ (18). Cobre na chama: verde-azulado.

TITULO = "Praticando: átomos e distribuição eletrônica"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões sobre o átomo, [p=0.1] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}os modelos atômicos, [p=0.2] {b}o salto do elétron, [p=0.2] {c}a conta de prótons, nêutrons e elétrons [p=0.2] e {d}o diagrama de Pauling. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: modelos
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Um texto diz: [p=0.1] {b}o cientista bombardeou uma folha de ouro [p=0.1] e concluiu que o átomo tem um núcleo pequeno e positivo. [p=0.3] {c}De quem é esse modelo? [p=0.2] E {d}qual observação mostrou que o átomo é quase todo vazio?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Folha de ouro e núcleo são as palavras-chave: [p=0.1] {a}é o modelo de Rutherford. [p=0.3] O vazio aparece porque {b}a grande maioria das partículas alfa atravessou sem desviar. [p=0.3] Cuidado para {c}não trocar com Thomson: [p=0.1] {d}no pudim de passas não há núcleo."),
    # questão 2: Bohr
    dict(id="s06", block="questao2", text="{a}Questão dois. [p=0.2] Um fio de cobre vai à chama, [p=0.1] e {b}a chama fica verde-azulada. [p=0.3] {c}Em que momento a luz é emitida: [p=0.1] quando o elétron sobe de camada, [p=0.1] ou quando ele volta?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}O calor dá energia, e o elétron sobe: [p=0.1] {b}na subida, ele recebe energia. [p=0.3] {c}A luz sai na volta, [p=0.1] quando ele devolve a energia. [p=0.3] E a cor é {d}a do cobre, porque os degraus de cada elemento são próprios dele."),
    # questão 3: partículas ao contrário
    dict(id="s09", block="questao3", text="{a}Questão três, no caminho inverso: das partículas para os números. [p=0.2] Um íon tem {b}dezesseis prótons, [p=0.1] {c}dezesseis nêutrons [p=0.1] e {d}dezoito elétrons. [p=0.3] {e}Qual é o zê, o número de massa e a carga desse íon? [p=0.2] E {f}um átomo de zê dezesseis e número de massa trinta e quatro é isótopo dele?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] {a}Zê é o número de prótons: dezesseis. [p=0.1] É o enxofre. [p=0.2] {b}O número de massa é prótons mais nêutrons: [p=0.1] dezesseis mais dezesseis dá trinta e dois. [p=0.3] {c}Tem dois elétrons a mais que prótons, [p=0.1] {d}então ganhou dois: carga dois menos. [p=0.3] {e}E o átomo de massa trinta e quatro tem o mesmo zê: [p=0.1] {f}é isótopo, com dois nêutrons a mais."),
    # atalho
    dict(id="s12", block="atalho", text="Aqui cabe um atalho: [p=0.1] {a}a carga é prótons menos elétrons. [p=0.3] {b}Dezesseis menos dezoito dá menos dois. [p=0.2] {c}O sinal já sai certo, sem pensar em perdeu ou ganhou."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada próton vale mais um e cada elétron vale menos um. [p=0.3] {b}Os nêutrons não entram, porque não têm carga. [p=0.2] {c}Só não esqueça a ordem: [p=0.1] prótons primeiro."),
    # questão 4: distribuição, valência e íon
    dict(id="s14", block="questao4", text="{a}Última questão, e ela junta tudo. [p=0.2] {b}O potássio tem zê dezenove. [p=0.3] {c}Faça a distribuição, [p=0.1] {d}diga quantos elétrons há na valência [p=0.1] e {e}distribua o íon potássio com carga um mais."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá, pelas diagonais. [p=0.2] {a}Um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê seis, [p=0.1] três esse dois, [p=0.1] três pê seis: [p=0.1] já são dezoito. [p=0.2] {b}Falta um: quatro esse um, [p=0.1] e não três dê um, porque pelas diagonais o quatro esse vem antes. [p=0.3] {c}A camada mais externa é a quatro, com um elétron só. [p=0.2] {d}Um elétron na valência."),
    dict(id="s17", block="resposta4", text="{a}Carga um mais: sai um elétron da camada mais externa, [p=0.1] {b}o quatro esse um. [p=0.2] {c}A distribuição fica até o três pê seis, com dezoito elétrons. [p=0.3] {d}Para conferir: dezenove menos um dá dezoito. [p=0.1] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}ache a palavra-chave do modelo, [p=0.2] {b}conte as partículas pelo zê e pelo á [p=0.2] e {c}siga as diagonais, tirando elétrons sempre da camada de fora."),
    dict(id="s19", block="fim", text="Na próxima aula, você abre {a}a tabela periódica [p=0.1] e acha {b}o período e a família de um elemento pela distribuição. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
