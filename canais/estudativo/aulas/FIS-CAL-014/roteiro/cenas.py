# Estudativo · FIS-CAL-014 — Segunda lei e máquinas térmicas (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: calcular o rendimento com τ/Qq e explicar por que nenhuma máquina transforma todo o calor em trabalho.
# Pré-requisitos: FIS-CAL-013 (primeira lei em cada transformação: no ciclo, ΔU = 0), FIS-ENE-002 (potência e rendimento).
# Próxima: FIS-CAL-015. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Qq e Qf como valores positivos (quantidades de calor); τ = Qq − Qf vem do ciclo (ΔU = 0). Rendimento real de motor a
# gasolina: cerca de 25 a 30 % (dito "cerca de um quarto"). Carnot e temperatura das fontes ficam para FIS-CAL-015.

TITULO = "Segunda lei e máquinas térmicas"

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
    dict(id="s01", block="gancho", text="{a}Num carro, a gasolina queima e libera calor. [p=0.3] {b}Só cerca de um quarto desse calor vira movimento. [p=0.3] {c}O resto sai pelo escapamento e pelo radiador. [p=0.3] {d}Defeito do motor? [p=0.2] Em parte. [p=0.2] {e}Mas nem um motor perfeito chegaria a cem por cento: é uma lei da natureza."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o rendimento de uma máquina térmica [p=0.2] e explicar {c}por que ele nunca chega a cem por cento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o rendimento, que é a parte útil dividida pelo total, em porcentagem; [p=0.2] e {c}que, num ciclo, delta U é zero, então o calor que entra menos o que sai vira trabalho. [p=0.3] Se faltar alguma, procure no canal."),
    # a máquina
    dict(id="s04", block="maquina", text="Máquina térmica é {a}tudo o que transforma calor em trabalho, repetindo um ciclo: [p=0.2] motor de carro, usina térmica, locomotiva a vapor. [p=0.3] Toda máquina térmica tem {b}três partes."),
    dict(id="s05", block="maquina", text="{a}A fonte quente, onde algo queima ou ferve. [p=0.2] {b}A máquina recebe dela um calor: o quê quente. [p=0.3] {c}Ela faz um trabalho, tau. [p=0.3] E {d}joga o resto na fonte fria, o ar ou a água de um rio: [p=0.2] {e}o quê frio."),
    dict(id="s06", block="maquina", text="{a}No ciclo, delta U é zero, [p=0.2] então nada fica guardado: [p=0.2] {b}tudo o que entra, sai. [p=0.3] {c}Quê quente é igual a tau mais quê frio. [p=0.2] Ou {d}tau é igual a quê quente menos quê frio. [p=0.3] {e}Aqui, quê quente e quê frio são só quantidades, sem sinal."),
    # rendimento
    dict(id="s07", block="rendimento", text="O rendimento usa a letra grega {a}eta. [p=0.2] {b}Eta é o útil dividido pelo total. [p=0.3] {c}O útil é o trabalho. [p=0.2] {d}O total é o calor que a máquina recebeu da fonte quente. [p=0.3] {e}Eta igual a tau dividido por quê quente."),
    dict(id="s08", block="rendimento", text="Exemplo. [p=0.2] {a}Uma máquina recebe mil joules da fonte quente [p=0.2] e {b}joga setecentos na fria. [p=0.3] {c}Trabalho: mil menos setecentos, trezentos joules. [p=0.3] {d}Rendimento: trezentos dividido por mil, [p=0.2] {e}zero vírgula três, [p=0.1] {f}trinta por cento."),
    # segunda lei
    dict(id="s09", block="segunda", text="E por que não cem por cento? [p=0.2] É a segunda lei da termodinâmica: [p=0.3] {a}nenhuma máquina, trabalhando em ciclo, transforma todo o calor recebido em trabalho. [p=0.3] {b}Sempre sobra um quê frio para a fonte fria."),
    dict(id="s10", block="segunda", text="Pense numa {a}roda-d'água. [p=0.2] {b}Ela só gira porque a água cai de cima para baixo. [p=0.3] {c}A água não some na roda: [p=0.2] ela chega lá embaixo. [p=0.3] {d}O calor também só passa sozinho do quente para o frio. [p=0.2] {e}A máquina aproveita essa passagem, [p=0.2] mas {f}o calor precisa chegar à fonte fria."),
    dict(id="s11", block="segunda", text="{a}Sem fonte fria, não há passagem de calor, [p=0.2] e {b}a máquina para. [p=0.3] Por isso, {c}o rendimento de uma máquina térmica é sempre menor que cem por cento."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dividir pelo calor errado. [p=0.3] No exemplo, quem faz {b}trezentos dividido por setecentos [p=0.2] acha {c}cerca de quarenta e três por cento. [p=0.3] {d}Mas setecentos é o que foi jogado fora. [p=0.2] {e}O total é o que entrou: mil."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}eta igual a um menos quê frio sobre quê quente. [p=0.3] {b}Setecentos dividido por mil, zero vírgula sete. [p=0.2] {c}Um menos zero vírgula sete, zero vírgula três: [p=0.1] {d}trinta por cento, sem calcular o trabalho."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o trabalho é quê quente menos quê frio: [p=0.2] {b}dividir tudo por quê quente dá um menos quê frio sobre quê quente. [p=0.3] {c}Ou pense assim: [p=0.2] se setenta por cento foi jogado fora, sobraram trinta. [p=0.3] {d}Não compensa quando a questão já dá o trabalho: [p=0.2] aí, use tau sobre quê quente direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Em cada ciclo, uma máquina {a}recebe oitocentos joules da fonte quente [p=0.2] e {b}joga seiscentos na fonte fria. [p=0.3] {c}Qual é o trabalho por ciclo? [p=0.2] E {d}o rendimento?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Tudo o que entra, sai: [p=0.2] {b}oitocentos menos seiscentos, duzentos joules de trabalho. [p=0.3] {c}Rendimento: duzentos dividido por oitocentos, [p=0.2] {d}um quarto, [p=0.1] {e}vinte e cinco por cento."),
    dict(id="s18", block="resposta", text="Com o atalho: {a}seiscentos dividido por oitocentos dá três quartos, setenta e cinco por cento jogados fora. [p=0.2] {b}Sobram vinte e cinco. [p=0.3] {c}Parecido com o motor do carro do começo da aula."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a máquina recebe quê quente, faz tau e joga quê frio fora; [p=0.2] {b}o rendimento é tau sobre quê quente; [p=0.2] e {c}pela segunda lei, ele nunca chega a cem por cento."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai descobrir {a}o rendimento máximo que uma máquina pode ter, [p=0.2] {b}só com as temperaturas das fontes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
