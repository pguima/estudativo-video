# Estudativo · FIS-MAG-010 — Vento e sol: rendimento e intermitência (Física · Magnetismo · Usinas e matriz elétrica).
# Habilidade: comparar eólica, solar, hídrica, térmica e nuclear em rendimento e intermitência.
# Pré-requisitos: FIS-MAG-009. Próxima: FIS-MAG-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Valores aproximados (ordem de grandeza usada em livros e provas): hidrelétrica cerca
# de 90%; térmica a combustível de um terço a pouco mais da metade (ciclo combinado); nuclear cerca de um terço; eólica: limite
# teórico de 59% (Betz), as melhores turbinas tiram por volta de metade; painel solar comum por volta de 20%.
# Sol forte ao meio-dia: cerca de 1.000 W por metro quadrado. Transformador e Lenz não estão em "Já ensinado".

TITULO = "Vento e sol: rendimento e intermitência"

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
    dict(id="s01", block="gancho", text="{a}Ao meio-dia, um painel solar gera bem. [p=0.2] {b}À meia-noite, gera zero. [p=0.3] {c}E uma represa gera às três da manhã, se você quiser. [p=0.3] {d}Essa diferença decide muita questão de prova."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai comparar as cinco fontes de eletricidade [p=0.2] em duas coisas: [p=0.1] {b}rendimento [p=0.1] e {c}intermitência."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Rendimento é a energia útil dividida pela energia que entrou. [p=0.3] E {c}hidrelétrica, termelétrica e nuclear giram uma turbina presa a um gerador. [p=0.3] Se faltar alguma, procure no canal."),
    # eólica
    dict(id="s04", block="eolica", text="Comece pelo vento. [p=0.2] {a}Na usina eólica, o vento empurra as pás, [p=0.2] {b}as pás giram o eixo, [p=0.1] e {c}o eixo gira um gerador, como nas outras. [p=0.3] {d}A energia que entra é a energia cinética do ar."),
    dict(id="s05", block="eolica", text="Mas {a}a turbina não pode tirar toda essa energia. [p=0.2] {b}Se tirasse, o ar pararia atrás das pás, [p=0.1] e o vento novo não teria por onde passar. [p=0.3] {c}As melhores turbinas aproveitam, no máximo, por volta de metade da energia do vento."),
    # solar
    dict(id="s06", block="solar", text="{a}O painel solar é diferente de todas. [p=0.2] {b}A luz bate no painel e vira eletricidade direto: [p=0.2] {c}sem turbina, sem gerador, sem nada girando. [p=0.3] {d}Um painel comum aproveita por volta de vinte por cento da luz."),
    dict(id="s07", block="solar", text="Um exemplo. [p=0.2] {a}Ao meio-dia, com sol forte, chegam cerca de mil watts de luz em cada metro quadrado. [p=0.3] {b}Um painel de um metro quadrado, com vinte por cento, [p=0.1] {c}entrega duzentos watts."),
    # rendimento
    dict(id="s08", block="rendimento", text="Agora, compare o rendimento. [p=0.2] {a}A hidrelétrica é campeã: cerca de noventa por cento. [p=0.3] {b}A térmica a combustível, de um terço a metade, [p=0.1] por causa da segunda lei. [p=0.2] {c}A nuclear, que também é térmica, fica perto de um terço. [p=0.3] {d}Vento, por volta de metade, no máximo; [p=0.1] {e}e sol, por volta de vinte por cento."),
    dict(id="s09", block="rendimento", text="Mas {a}rendimento baixo não quer dizer fonte ruim. [p=0.2] {b}O sol e o vento chegam de graça, [p=0.1] e {c}não queimam nada. [p=0.3] {d}O problema deles é outro."),
    # intermitência
    dict(id="s10", block="intermitencia", text="É a {a}intermitência: [p=0.2] a fonte que liga e desliga sozinha. [p=0.3] {b}O painel não gera à noite, [p=0.1] e gera menos com nuvem. [p=0.2] {c}A eólica para quando o vento cai. [p=0.3] {d}Ninguém escolhe a hora."),
    dict(id="s11", block="intermitencia", text="{a}A térmica e a nuclear não dependem do tempo: [p=0.1] geram de dia e de noite. [p=0.2] A térmica a gás ainda liga rápido; [p=0.1] a nuclear fica ligada direto. [p=0.3] {b}A hidrelétrica depende da chuva, [p=0.2] mas {c}a represa guarda água, [p=0.1] e a usina gera na hora que precisar. [p=0.3] {d}Por isso, ela é a parceira ideal do sol e do vento: [p=0.2] gera mais quando eles faltam."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que fonte renovável é fonte que gera o tempo todo. [p=0.3] {b}Renovável é a que não acaba: [p=0.1] sol, vento, água. [p=0.2] {c}Intermitente é a que não dá para controlar. [p=0.3] {d}A hidrelétrica é renovável e controlável. [p=0.2] {e}A solar é renovável e intermitente."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova. [p=0.2] Para cada fonte, faça {a}duas perguntas. [p=0.3] {b}Primeira: ela gira um gerador? [p=0.2] Só a solar diz não. [p=0.3] {c}Segunda: dá para ligar na hora que eu quiser? [p=0.2] {d}Eólica e solar dizem não: são as intermitentes."),
    dict(id="s14", block="atalho", text="{a}E se a questão pedir a fonte para cobrir a noite, [p=0.2] ou uma hora de muito consumo, [p=0.2] {b}procure uma controlável. [p=0.3] {c}Se pedir a que menos emite gás carbônico, [p=0.2] olhe quem não tem queima: [p=0.1] {d}hídrica, eólica, solar e nuclear, [p=0.1] que usa urânio sem fogo nenhum."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma casa tem dez metros quadrados de painéis, com vinte por cento de rendimento. [p=0.3] {b}Ao meio-dia, chegam mil watts de luz por metro quadrado. [p=0.3] {c}Quanto os painéis entregam ao meio-dia? [p=0.2] {d}E à meia-noite? [p=0.2] {e}Entre uma eólica e uma hidrelétrica com represa, qual garante a energia da noite?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Dez metros quadrados vezes mil watts: [p=0.1] {b}dez mil watts de luz. [p=0.3] {c}Vinte por cento disso: [p=0.1] {d}dois mil watts. [p=0.3] {e}À meia-noite, sem luz, zero."),
    dict(id="s18", block="resposta", text="{a}E a noite fica com a hidrelétrica: [p=0.2] {b}a represa guarda a água, [p=0.1] e ela gera quando precisar. [p=0.3] {c}A eólica pode até gerar à noite, [p=0.1] mas só se ventar."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a hidrelétrica tem o maior rendimento, [p=0.2] {b}o sol tem o menor, mas é de graça, [p=0.2] e {c}vento e sol são intermitentes. [p=0.3] Na próxima aula, {d}você pratica tudo isso em questões de usinas."),
    dict(id="s20", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
