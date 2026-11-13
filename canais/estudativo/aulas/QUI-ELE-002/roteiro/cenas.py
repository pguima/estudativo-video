# Estudativo · QUI-ELE-002 — Oxirredução: quem perde e quem ganha elétrons (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: apontar quem oxida, quem reduz e os agentes em Zn + Cu²⁺ e no alto-forno.
# Pré-requisitos: QUI-ELE-001, QUI-INO-010. Próxima: QUI-ELE-015 (balancear por oxirredução: igualar elétrons perdidos e ganhos).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Leituras: Zn = "zinco", Cu²⁺ = "cobre dois mais", Fe₂O₃ = "fé dois ó três", CO = "cê ó, o monóxido de carbono" (sempre com o
# nome, para não confundir com o cobalto), CO₂ = "cê ó dois", HCl = "agá cê ele", MgCl₂ = "cloreto de magnésio".
# Contas: Zn 0 → +2 (perde 2 e⁻) · Cu²⁺ +2 → 0 (ganha 2 e⁻) · Fe₂O₃: 2x − 6 = 0 → +3 · Fe 0 · CO: x − 2 = 0 → +2 ·
# CO₂: x − 4 = 0 → +4 · Mg 0 → +2 · H em HCl +1 → H₂ 0 · Cl −1 nos dois lados. Alto-forno: Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂.

TITULO = "Oxirredução: quem perde e quem ganha elétrons"

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
    dict(id="s01", block="gancho", text="{a}Mergulhe uma placa de zinco numa solução azul de sulfato de cobre. [p=0.3] Em minutos, {b}a placa fica coberta de uma camada avermelhada de cobre, [p=0.2] e, aos poucos, {c}o azul vai sumindo. [p=0.3] Ninguém pôs cobre ali. [p=0.2] {d}De onde ele veio?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai apontar {b}quem se oxida, quem se reduz {c}e quem são os agentes, [p=0.2] no zinco com cobre e no {d}alto-forno que faz o ferro. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Calcular o Nox: [p=0.1] substância simples vale zero, íon de um átomo só vale a carga, e a soma fecha em zero. [p=0.3] E {b}a fila de reatividade: [p=0.1] {c}o zinco é mais reativo que o cobre. [p=0.2] Se faltar alguma, procure no canal."),
    # o que aconteceu
    dict(id="s04", block="troca", text="Escreva o que aconteceu. [p=0.2] {a}Zinco metálico mais cobre dois mais, [p=0.1] {b}dá zinco dois mais e cobre metálico. [p=0.3] {c}O cobre já estava na solução, como íon. [p=0.2] {d}Ele só virou metal. [p=0.2] O sulfato só assiste: não muda."),
    dict(id="s05", block="troca", text="Olhe o Nox de cada um. [p=0.2] {a}O zinco começa em zero e termina em mais dois. [p=0.2] Para ficar mais positivo, {b}ele perdeu dois elétrons. [p=0.3] {c}O cobre começa em mais dois e termina em zero: [p=0.1] {d}ganhou dois elétrons. [p=0.3] {e}Os elétrons que saíram do zinco foram para o cobre."),
    # definições
    dict(id="s06", block="nomes", text="Cada metade da troca tem nome. [p=0.2] {a}Perder elétrons é se oxidar: [p=0.1] {b}o Nox sobe. [p=0.3] {c}Ganhar elétrons é se reduzir: [p=0.1] {d}o Nox desce. [p=0.3] {e}Uma não acontece sem a outra, [p=0.1] porque o elétron que um perde, o outro ganha. [p=0.2] Por isso, o nome é {f}oxirredução."),
    dict(id="s07", block="nomes", text="E os agentes? [p=0.2] O agente é quem provoca. [p=0.2] {a}O zinco provocou a redução do cobre, [p=0.1] {b}então o zinco é o agente redutor. [p=0.3] {c}O cobre dois mais provocou a oxidação do zinco: [p=0.1] {d}é o agente oxidante. [p=0.3] {e}Repare: o redutor se oxida, e o oxidante se reduz."),
    # alto-forno
    dict(id="s08", block="forno", text="Agora, um caso de prova: {a}o alto-forno, o forno gigante da siderúrgica. [p=0.2] Ali, o minério, {b}fé dois ó três, reage com {c}cê ó, o monóxido de carbono, [p=0.2] e dá {d}ferro e gás carbônico."),
    dict(id="s09", block="forno", text="Calcule o Nox do ferro. [p=0.2] {a}No minério, três oxigênios dão menos seis, [p=0.1] e dois ferros precisam dar mais seis: [p=0.1] {b}cada ferro é mais três. [p=0.3] {c}No ferro metálico, zero. [p=0.2] {d}Desceu de mais três para zero: o ferro se reduziu."),
    dict(id="s10", block="forno", text="Agora o carbono. [p=0.2] {a}No monóxido, um oxigênio dá menos dois: [p=0.1] o carbono é mais dois. [p=0.2] {b}No gás carbônico, dois oxigênios dão menos quatro: [p=0.1] mais quatro. [p=0.3] {c}Subiu: o carbono se oxidou. [p=0.3] {d}E o oxigênio fica em menos dois o tempo todo."),
    dict(id="s11", block="forno", text="{a}O ferro do minério se reduziu, então o minério inteiro {b}é o agente oxidante. [p=0.2] {c}Quem se oxidou foi o monóxido de carbono: {d}o agente redutor. [p=0.3] Na prova, {e}o agente é a substância inteira, não só o átomo."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o agente oxidante é quem se oxida. [p=0.3] No zinco com cobre, a pessoa marca {b}o zinco como oxidante, só pelo som da palavra."),
    dict(id="s13", block="erro", text="{a}O nome conta o que o agente faz no outro. [p=0.2] {b}O zinco se oxidou? [p=0.1] Então ele {c}reduziu o cobre: [p=0.1] é o redutor."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}Nox subiu, a substância ou o íon se oxidou e é o redutor. [p=0.2] {b}Nox desceu, se reduziu e é o oxidante. [p=0.3] {c}Os nomes sempre se cruzam."),
    dict(id="s15", block="atalho", text="E para achar rápido quem muda: [p=0.2] {a}procure o elemento que aparece sozinho de um lado, como substância simples, [p=0.1] e combinado do outro. [p=0.2] {b}Sozinho e sem carga, ele vale zero. [p=0.1] {c}Combinado, quase nunca. [p=0.3] {d}No alto-forno, o atalho acha o ferro, mas não o carbono, que está combinado dos dois lados. [p=0.2] Aí, não compensa: calcule."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma fita de magnésio no ácido clorídrico solta gás hidrogênio: [p=0.2] {b}magnésio mais dois agá cê ele, [p=0.1] dá cloreto de magnésio e agá dois. [p=0.3] {c}Quem se oxida, quem se reduz, [p=0.1] {d}e quais são os agentes?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O magnésio sai de zero e vai a mais dois, [p=0.1] porque, no cloreto, os dois cloros valem menos um cada. [p=0.2] Ele se oxida e {b}é o agente redutor. [p=0.3] {c}O hidrogênio sai de mais um e vai a zero: [p=0.1] se reduz. [p=0.2] {d}Quem traz esse hidrogênio é o ácido: [p=0.1] {e}o agá cê ele é o agente oxidante."),
    dict(id="s19", block="resposta", text="{a}E o cloro fica em menos um dos dois lados: [p=0.1] nem se oxida, nem se reduz."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}oxidar é perder elétrons, e o Nox sobe; [p=0.1] {b}reduzir é ganhar, e o Nox desce; [p=0.2] {c}e o agente faz no outro o contrário do que sofre."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai usar {a}os elétrons perdidos e ganhos para balancear a equação. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
