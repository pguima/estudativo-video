# Estudativo · QUI-CAL-008 — Rendimento e reações em etapas (Química · Cálculos Químicos · Estequiometria).
# Habilidade: corrigir o produto de uma reação com 75% de rendimento e somar S → SO₂ → SO₃ → H₂SO₄ em uma conta só.
# Pré-requisitos: QUI-CAL-005, MAT-POR-002. Próxima: QUI-CAL-009 (praticando: mol e estequiometria).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Etapas: S + O₂ → SO₂; 2 SO₂ + O₂ → 2 SO₃; SO₃ + H₂O → H₂SO₄ (todas balanceadas). 1 S : 1 H₂SO₄ = 32 g : 98 g.
# Contas: 64 g S → 196 g (máximo); 0,75 · 196 = 147 g; erro 0,25 · 196 = 49 g. Questão: 16 g → 49 g; 0,8 · 49 = 39,2 g.

TITULO = "Rendimento e reações em etapas"

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
    dict(id="s01", block="gancho", text="{a}Uma fábrica de ácido sulfúrico faz a conta: [p=0.1] {b}com sessenta e quatro gramas de enxofre, [p=0.1] deveriam sair cento e noventa e seis gramas de ácido. [p=0.3] {c}Saem cento e quarenta e sete. [p=0.2] {d}Para onde foi o resto? [p=0.2] E como passar por {e}três reações numa conta só?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}corrigir uma conta pelo rendimento [p=0.2] e {c}juntar reações em etapas numa proporção só, [p=0.2] com um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a conta de massa para massa numa equação [p=0.2] e {c}calcular uma porcentagem multiplicando pelo decimal. [p=0.3] Se faltar alguma, procure no canal."),
    # rendimento
    dict(id="s04", block="rendimento", text="{a}Nenhuma reação de fábrica dá tudo o que a conta promete. [p=0.2] {b}Parte do reagente fica sem reagir, [p=0.1] parte vira outra coisa, [p=0.1] parte se perde no caminho. [p=0.3] {c}Rendimento é a porcentagem do máximo que sai de verdade."),
    dict(id="s05", block="rendimento", text="{a}A conta que você já sabe dá o máximo, o rendimento teórico. [p=0.2] {b}Com setenta e cinco por cento de rendimento, [p=0.1] {c}multiplique esse máximo por zero vírgula setenta e cinco."),
    # etapas
    dict(id="s06", block="etapas", text="O ácido sulfúrico sai em três etapas. [p=0.2] {a}Primeiro, enxofre mais ó dois forma esse ó dois. [p=0.2] {b}Depois, dois esse ó dois mais ó dois formam dois esse ó três. [p=0.2] {c}Por fim, esse ó três mais agá dois ó forma agá dois esse ó quatro."),
    dict(id="s07", block="etapas", text="{a}Fazer três regras de três dá trabalho e abre espaço para erro. [p=0.3] {b}Siga o enxofre: [p=0.1] {c}um átomo de enxofre vira uma molécula de esse ó dois, [p=0.1] {d}depois uma de esse ó três, [p=0.1] {e}depois uma de ácido. [p=0.2] Na segunda etapa, dois para dois é o mesmo que um para um. [p=0.3] {f}Um mol de enxofre dá um mol de ácido."),
    dict(id="s08", block="etapas", text="{a}Em gramas: [p=0.1] trinta e dois gramas de enxofre [p=0.1] {b}dão noventa e oito de ácido, [p=0.1] a massa molar dele: [p=0.1] dois mais trinta e dois mais sessenta e quatro dá noventa e oito. [p=0.3] {c}Com sessenta e quatro gramas, o dobro: [p=0.1] {d}cento e noventa e seis gramas. [p=0.2] {e}Esse é o máximo."),
    dict(id="s09", block="etapas", text="{a}Falta o rendimento: [p=0.1] {b}zero vírgula setenta e cinco vezes cento e noventa e seis [p=0.1] {c}dá cento e quarenta e sete gramas. [p=0.2] {d}Aí está o número do começo."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}calcular a parte que se perdeu. [p=0.2] {b}Setenta e cinco por cento de rendimento quer dizer que sai setenta e cinco por cento, [p=0.1] {c}não que se perde. [p=0.3] {d}Quem faz vinte e cinco por cento de cento e noventa e seis [p=0.1] responde {e}quarenta e nove gramas: a parte perdida."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho das etapas: [p=0.1] {a}siga o elemento que passa por todas elas. [p=0.2] {b}Conte quantos átomos dele há no começo e no fim: [p=0.1] {c}um enxofre no começo, [p=0.1] {d}um enxofre no agá dois esse ó quatro. [p=0.2] {e}A proporção é um para um, sem olhar as etapas do meio."),
    dict(id="s12", block="atalho", text="{a}Funciona porque o átomo não some nem aparece: [p=0.1] {b}todo enxofre que entra sai no ácido. [p=0.3] {c}Não compensa quando o elemento se divide entre dois produtos. [p=0.3] {d}E se cada etapa tiver o seu rendimento, o atalho ainda vale: [p=0.1] multiplique o máximo por todos os rendimentos, um depois do outro."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}A mesma fábrica usa dezesseis gramas de enxofre, [p=0.2] {b}com oitenta por cento de rendimento. [p=0.3] {c}Quantos gramas de ácido sulfúrico ela produz?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Um enxofre para um ácido: [p=0.1] trinta e dois gramas dão noventa e oito. [p=0.2] {b}Dezesseis é a metade: [p=0.1] {c}quarenta e nove gramas no máximo. [p=0.3] {d}Zero vírgula oito vezes quarenta e nove [p=0.1] {e}dá trinta e nove vírgula dois gramas."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}o rendimento multiplica o máximo; [p=0.2] {b}e, em etapas, siga o elemento do começo ao fim."),
    dict(id="s17", block="fim", text="Na próxima aula, você pratica: [p=0.2] {a}problemas de fábrica e de meio ambiente [p=0.1] {b}com mol, pureza, rendimento e reagente limitante. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
