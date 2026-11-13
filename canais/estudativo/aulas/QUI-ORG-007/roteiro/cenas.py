# Estudativo · QUI-ORG-007 — Aldeído e cetona (Química · Química Orgânica · Funções orgânicas).
# Habilidade: diferenciar aldeído de cetona pela posição do C=O e nomear etanal e propanona.
# Pré-requisitos: QUI-ORG-006 (álcool, fenol, éter; nome em ol). Próxima: QUI-ORG-008 (ácido carboxílico e éster).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas faladas: CHO = "cê agá ó"; CO no meio = "cê ó".
# Fatos: formol = solução de metanal em água (conserva peças); acetona = propanona (removedor de esmalte); aldeído sem número
# (carbonila sempre no C1); pentan-2-ona ≠ pentan-3-ona; a menor cetona tem 3 carbonos.
# Questão: butanal CH3–CH2–CH2–CHO e butanona CH3–CO–CH2–CH3, os dois C4H8O; butanona dispensa número (só cabe no C2).
# Questão inédita, criada para esta aula.

TITULO = "Aldeído e cetona"

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
    dict(id="s01", block="gancho", text="{a}O formol, que conserva peças de anatomia, [p=0.1] {b}e a acetona, que tira esmalte. [p=0.3] {c}Os dois têm o mesmo pedaço: um carbono em dupla com um oxigênio. [p=0.2] {d}Só muda onde ele está."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai diferenciar {b}aldeído de cetona pela posição desse pedaço [p=0.2] e dar nome ao {c}etanal [p=0.1] e à {d}propanona."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}no álcool, no fenol e no éter, o oxigênio só tem ligações simples, [p=0.1] {b}e o nome do álcool termina em ol. [p=0.3] {c}Hoje, o oxigênio usa as duas ligações de uma vez, numa dupla."),
    # carbonila
    dict(id="s04", block="carbonila", text="{a}Cê, dupla, ó: [p=0.1] esse grupo se chama carbonila. [p=0.3] {b}O oxigênio gasta as duas ligações dele na dupla, [p=0.2] {c}e o carbono fica com duas ligações livres."),
    # aldeído
    dict(id="s05", block="aldeido", text="{a}Se a carbonila está na ponta da cadeia, [p=0.1] {b}uma das ligações livres vai para um hidrogênio. [p=0.2] {c}É o aldeído. [p=0.3] {d}Na fórmula condensada, ele aparece no fim, como cê agá ó."),
    dict(id="s06", block="aldeido", text="{a}O nome troca o ó do fim por al. [p=0.2] {b}Dois carbonos: etanal, [p=0.1] cê agá três, cê agá ó. [p=0.3] {c}Um carbono só: metanal, [p=0.1] {d}o formol, quando está dissolvido em água. [p=0.3] {e}O aldeído não leva número, porque a carbonila está sempre no carbono um."),
    # cetona
    dict(id="s07", block="cetona", text="{a}Se a carbonila está no meio, entre dois carbonos, [p=0.1] é a cetona. [p=0.3] {b}O nome termina em ona. [p=0.2] {c}Três carbonos: propanona, [p=0.1] {d}cê agá três, cê ó, cê agá três, [p=0.1] {e}a acetona. [p=0.3] {f}Compare com o propanal: [p=0.1] os mesmos átomos, [p=0.1] mas com a carbonila na ponta. [p=0.2] {g}A posição da carbonila muda a família."),
    dict(id="s08", block="cetona", text="{a}Com cinco carbonos, a carbonila da cetona tem mais de um lugar: [p=0.2] {b}pentan dois ona e pentan três ona são moléculas diferentes. [p=0.2] {c}Por isso, numere pela ponta mais perto da carbonila."),
    # erro comum
    dict(id="s09", block="erro", text="{a}O erro mais comum é ler cê agá ó como se fosse álcool. [p=0.3] {b}No aldeído, o agá está preso ao carbono, [p=0.1] {c}e o oxigênio está só na dupla. [p=0.2] {d}No álcool, o agá fica no oxigênio: ó agá. [p=0.3] {e}Se o oxigênio não tem agá, não é álcool."),
    # atalho
    dict(id="s10", block="atalho", text="{a}O atalho: [p=0.1] conte os carbonos. [p=0.2] {b}Com um ou dois carbonos, a carbonila só pode ser de aldeído. [p=0.2] {c}A cetona precisa de um carbono de cada lado, [p=0.1] então {d}a menor cetona tem três: [p=0.1] a propanona."),
    dict(id="s11", block="atalho", text="{a}Funciona porque, com dois carbonos, um lado da carbonila sempre fica sem carbono. [p=0.3] {b}Não decide nada com três carbonos ou mais: [p=0.1] {c}aí, olhe os vizinhos do carbono da carbonila. [p=0.2] {d}Vizinho agá: aldeído. [p=0.2] {e}Carbono dos dois lados: cetona."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}Estas duas moléculas têm a mesma fórmula, cê quatro agá oito ó. [p=0.3] {b}Qual é o aldeído e qual é a cetona? [p=0.2] {c}E qual é o nome de cada uma?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="{a}A primeira tem a carbonila na ponta, com agá: [p=0.1] aldeído. [p=0.2] {b}Quatro carbonos, só simples na cadeia, final al: [p=0.1] {c}butanal. [p=0.3] {d}A segunda tem a carbonila entre dois carbonos: cetona. [p=0.2] {e}Butanona."),
    dict(id="s15", block="resposta", text="{a}E a butanona não precisa de número: [p=0.1] com quatro carbonos, a carbonila de cetona só cabe no carbono dois, [p=0.2] {b}de qualquer ponta que você conte."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}a carbonila é o cê, dupla, ó. [p=0.2] {b}Na ponta, com agá, é aldeído, com al. [p=0.2] {c}No meio, entre carbonos, é cetona, com ona."),
    dict(id="s17", block="fim", text="Na próxima aula, a carbonila ganha um vizinho com oxigênio: [p=0.2] {a}o ácido do vinagre [p=0.1] e {b}o éster que dá cheiro às frutas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
