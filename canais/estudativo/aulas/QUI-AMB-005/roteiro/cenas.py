# Estudativo · QUI-AMB-005 — Esgoto, DBO e oxigênio dissolvido (Química · Química e Ambiente · Tratamento de água e química verde).
# Habilidade: dizer o que é DBO, explicar por que o esgoto e a água aquecida asfixiam os peixes e descrever como se trata o
# esgoto.
# Pré-requisitos: QUI-AMB-004, QUI-SOL-002, QUI-SOL-003. Próxima: QUI-AMB-006 (química verde e economia atômica).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Siglas faladas: DBO "dê bê ó", OD "ó dê", ppm "pê pê eme", H₂S "agá dois esse", CH₄ "cê agá quatro".
# Fatos: água limpa e fria dissolve só cerca de 8 a 9 mg/L de O₂ (cerca de 9 a 20 °C, 8 a 25 °C); abaixo de cerca de
# 4 mg/L muitos peixes já sofrem; DBO = mg de O₂ que as bactérias consomem para decompor a matéria orgânica de 1 L de
# amostra (em geral, em 5 dias a 20 °C); rio limpo até cerca de 3 mg/L (classe 1 do CONAMA: até 3; classe 2: até 5);
# esgoto doméstico sem tratamento, cerca de 300 mg/L. Sem O₂, bactérias anaeróbias soltam H₂S (ovo podre) e metano.
# Estação de esgoto: grade e caixa de areia → decantação (lodo) → tanque com ar (bactérias aeróbias) → água devolvida.
# Questão simplificada: DBO = OD inicial − OD depois de 5 dias (amostra sem diluir).

TITULO = "Esgoto, DBO e oxigênio dissolvido"

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
    dict(id="s01", block="gancho", text="{a}Um rio pode estar cheio de comida [p=0.1] {b}e, mesmo assim, os peixes morrem sem ar. [p=0.3] {c}O culpado é o esgoto. [p=0.2] {d}E a medida que denuncia o problema tem três letras: dê bê ó."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai entender {b}o que é dê bê ó, [p=0.2] {c}por que o esgoto e a água quente asfixiam os peixes [p=0.2] e {d}como uma estação trata o esgoto."),
    # lembrete
    dict(id="s03", block="lembrete", text="Dois lembretes. [p=0.2] {a}Gás dissolve menos na água quente: [p=0.1] é por isso que o refrigerante quente perde gás. [p=0.3] {b}E um pê pê eme é um miligrama por litro."),
    # OD
    dict(id="s04", block="od", text="Peixe não respira a água: [p=0.1] {a}ele respira o gás oxigênio dissolvido nela. [p=0.3] {b}E é pouco. [p=0.2] {c}Um litro de água limpa, a uns vinte graus, tem só uns oito ou nove miligramas de ó dois. [p=0.3] {d}Essa medida se chama oxigênio dissolvido, ou ó dê."),
    dict(id="s05", block="od", text="{a}Abaixo de uns quatro miligramas por litro, muitos peixes já sofrem. [p=0.3] {b}Perto de zero, morrem asfixiados."),
    # esgoto
    dict(id="s06", block="esgoto", text="{a}O esgoto é cheio de matéria orgânica: [p=0.1] {b}restos de comida, fezes, tudo o que já foi vivo. [p=0.3] {c}No rio, bactérias se alimentam dessa matéria. [p=0.2] {d}E, para isso, gastam o oxigênio dissolvido, [p=0.1] {e}o mesmo que os peixes respiram."),
    dict(id="s07", block="esgoto", text="{a}Quanto mais esgoto, mais comida para as bactérias, [p=0.1] {b}mais oxigênio gasto [p=0.1] {c}e menos oxigênio para os peixes. [p=0.3] É assim que um rio cheio de comida para as bactérias mata os peixes por falta de ar."),
    dict(id="s08", block="esgoto", text="{a}Quando o oxigênio acaba, entram outras bactérias, que vivem sem ele. [p=0.3] {b}Elas soltam gás sulfídrico, agá dois ésse, com cheiro de ovo podre, [p=0.1] {c}e metano. [p=0.2] {d}É o cheiro dos rios mortos das cidades."),
    # DBO
    dict(id="s09", block="dbo", text="{a}Dê bê ó quer dizer demanda bioquímica de oxigênio. [p=0.3] {b}É quanto oxigênio as bactérias consomem para decompor a matéria orgânica de um litro de água. [p=0.3] {c}No laboratório, a amostra fica cinco dias fechada, no escuro, [p=0.1] {d}e mede-se quanto oxigênio sumiu."),
    dict(id="s10", block="dbo", text="{a}Ela é dada em miligramas por litro, ou seja, em pê pê eme. [p=0.3] {b}Rio limpo tem dê bê ó de até uns três. [p=0.2] {c}Esgoto de casa, sem tratamento, chega a uns trezentos. [p=0.3] {d}Quanto maior a dê bê ó, mais poluída a água."),
    # água quente
    dict(id="s11", block="quente", text="E a água quente? [p=0.2] {a}Algumas usinas e fábricas usam água do rio para resfriar máquinas [p=0.1] {b}e a devolvem limpa, porém mais quente. [p=0.3] {c}Água quente dissolve menos gás: [p=0.1] {d}cabe menos oxigênio nela. [p=0.3] {e}E, no calor, o peixe precisa de mais oxigênio. [p=0.2] Isso se chama poluição térmica."),
    # tratamento
    dict(id="s12", block="ete", text="Como se trata o esgoto? [p=0.2] {a}Primeiro, grades seguram o lixo grosso e um tanque deixa a areia descer. [p=0.3] {b}Depois, uma decantação: a parte sólida desce e forma o lodo."),
    dict(id="s13", block="ete", text="{a}Aí vem o pulo do gato: um tanque com ar bombeado sem parar. [p=0.3] {b}Ali, bactérias comem a matéria orgânica que sobrou, [p=0.1] com oxigênio de sobra. [p=0.3] {c}A ideia é deixar as bactérias gastarem oxigênio dentro da estação, e não no rio. [p=0.3] {d}A água sai com dê bê ó baixa e volta para o rio."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: {a}dê bê ó alta, ó dê baixo. [p=0.3] Funciona porque {b}a dê bê ó mede o oxigênio que vai ser gasto: [p=0.1] {c}quanto mais alta, menos sobra para os peixes."),
    dict(id="s15", block="atalho", text="{a}O atalho falha com água quente. [p=0.2] {b}Ali, o ó dê cai mesmo com a dê bê ó baixa, [p=0.1] {c}porque o problema não é o esgoto: é a temperatura."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}achar que dê bê ó alta quer dizer muito oxigênio na água. [p=0.3] {b}É o contrário. [p=0.2] {c}Demanda é o que as bactérias pedem, não o que a água tem. [p=0.3] {d}Dê bê ó alta é água com muito esgoto, e pouco oxigênio."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Uma amostra de água de rio começou com nove miligramas de oxigênio por litro. [p=0.2] {b}Depois de cinco dias fechada, no escuro, tinha três. [p=0.3] {c}Qual é a dê bê ó? [p=0.2] {d}E esse rio está limpo, se rio limpo tem dê bê ó de até três miligramas por litro?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="{a}A dê bê ó é o oxigênio que as bactérias gastaram. [p=0.2] {b}Nove menos três dá seis miligramas por litro, [p=0.1] {c}ou seis pê pê eme."),
    dict(id="s20", block="resposta", text="{a}Seis é o dobro do limite de rio limpo: [p=0.1] {b}esse rio está recebendo esgoto. [p=0.3] {c}Quem respondeu três, o que sobrou, mediu o ó dê no fim, e não a dê bê ó."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}peixe depende do oxigênio dissolvido; [p=0.2] {b}esgoto alimenta bactérias que gastam esse oxigênio; [p=0.2] {c}a dê bê ó mede esse gasto; [p=0.2] e {d}água quente segura menos oxigênio."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai ver como a indústria tenta não sujar nada desde o começo: [p=0.2] {a}a química verde e a conta da economia atômica. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
