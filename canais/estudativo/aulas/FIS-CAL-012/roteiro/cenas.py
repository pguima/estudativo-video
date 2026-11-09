# Estudativo · FIS-CAL-012 — Primeira lei da termodinâmica (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: usar Q = τ + ΔU com a regra de sinais certa, como balanço de contas da energia do gás.
# Pré-requisitos: FIS-CAL-011 (trabalho de um gás), FIS-CAL-003 (calor sensível). Próxima: FIS-CAL-013.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Energia interna é termo novo: explicada na hora como a energia de agitação das partículas, que acompanha a temperatura
# (gás ideal: o modelo das provas). As transformações uma a uma (o termo que some em cada caso) são da FIS-CAL-013.

TITULO = "Primeira lei da termodinâmica"

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
    dict(id="s01", block="gancho", text="{a}Um gás recebe quinhentos joules de calor. [p=0.3] {b}Ele empurra um êmbolo [p=0.1] e {c}ainda esquenta. [p=0.3] {d}Para onde foi cada joule?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai fechar essa conta {b}como um extrato de banco, [p=0.2] {c}sem errar nenhum sinal."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o calor, que é energia passando do mais quente para o mais frio, em joule; [p=0.2] e {c}o trabalho do gás, tau igual a pê vezes delta vê, positivo quando ele se expande. [p=0.3] Se faltar alguma, procure no canal."),
    # energia interna
    dict(id="s04", block="interna", text="Falta um nome. [p=0.2] {a}As partículas de um gás estão sempre se agitando. [p=0.3] {b}A soma da energia dessa agitação é a energia interna, a letra U. [p=0.3] {c}No gás ideal, o modelo que as provas usam, ela só depende da temperatura: [p=0.2] {d}esquentou, a energia interna aumentou; [p=0.2] {e}esfriou, diminuiu."),
    # a lei
    dict(id="s05", block="lei", text="Vamos à conta. [p=0.2] {a}A energia não some nem aparece do nada. [p=0.3] {b}O calor que entra no gás tem dois destinos: [p=0.2] {c}uma parte sai como trabalho, [p=0.2] e {d}o resto fica guardado como energia interna."),
    dict(id="s06", block="lei", text="Essa é a primeira lei da termodinâmica: [p=0.2] {a}quê igual a tau mais delta U. [p=0.3] {b}Quê é o calor, [p=0.1] {c}tau é o trabalho, [p=0.1] {d}delta U é a variação da energia interna. [p=0.2] {e}Tudo em joule."),
    dict(id="s07", block="lei", text="Pense num salário. [p=0.2] {a}O calor é o salário que entra. [p=0.2] {b}O trabalho é o que você gasta. [p=0.2] {c}Delta U é o quanto o saldo mudou. [p=0.3] Por isso, {d}delta U é igual a quê menos tau: [p=0.2] o que entrou, menos o que saiu."),
    # sinais
    dict(id="s08", block="sinais", text="Os sinais seguem o gás. [p=0.3] {a}Quê é positivo quando o gás recebe calor, [p=0.2] e negativo quando ele cede. [p=0.3] {b}Tau é positivo quando o gás se expande e faz trabalho, [p=0.2] e negativo quando ele é comprimido e recebe trabalho. [p=0.3] {c}Delta U é positivo quando a temperatura sobe, [p=0.2] e negativo quando cai."),
    # exemplo 1
    dict(id="s09", block="exemplo", text="Voltando ao gancho: [p=0.2] {a}o gás recebeu quinhentos joules, então quê é mais quinhentos. [p=0.2] Digamos que ele {b}fez duzentos joules de trabalho ao empurrar: tau é mais duzentos. [p=0.3] {c}Delta U é quinhentos menos duzentos: [p=0.2] {d}mais trezentos joules. [p=0.3] {e}Saldo positivo: o gás esquentou."),
    # exemplo 2
    dict(id="s10", block="exemplo2", text="Outro caso: uma bomba de encher pneu. [p=0.2] {a}Você comprime o ar e dá trezentos joules de trabalho a ele. [p=0.2] Ao mesmo tempo, {b}ele perde cem joules de calor para a bomba. [p=0.3] {c}Compressão: tau é menos trezentos. [p=0.2] {d}Calor saindo: quê é menos cem."),
    dict(id="s11", block="exemplo2", text="{a}Delta U é quê menos tau: [p=0.2] {b}menos cem, menos, abre parênteses, menos trezentos. [p=0.3] {c}Menos com menos dá mais: [p=0.2] {d}menos cem mais trezentos, [p=0.1] {e}mais duzentos joules. [p=0.3] {f}O ar esquentou, [p=0.2] e é por isso que a bomba fica quente na mão."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o sinal do trabalho na compressão. [p=0.3] Quem usa tau igual a mais trezentos faz {b}menos cem menos trezentos, [p=0.2] {c}menos quatrocentos, [p=0.2] e conclui que {d}o ar esfriou. [p=0.3] {e}Mas a bomba esquenta na sua mão: [p=0.2] o sinal estava errado."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: {a}desenhe o gás como uma caixa. [p=0.3] {b}Cada energia vira uma seta: [p=0.2] {c}seta entrando na caixa soma, [p=0.2] {d}seta saindo subtrai. [p=0.3] {e}Delta U é o que entra menos o que sai, [p=0.2] e você nem precisa lembrar a regra de sinais."),
    dict(id="s14", block="atalho", text="Na bomba: {a}entram trezentos de trabalho, [p=0.2] {b}saem cem de calor. [p=0.2] {c}Trezentos menos cem: mais duzentos. [p=0.3] Funciona porque {d}é a mesma conta da energia, sem os sinais escondidos. [p=0.3] {e}Não compensa quando a questão já dá quê e tau com sinal: [p=0.2] aí, é só pôr na fórmula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um gás {a}cede quatrocentos joules de calor [p=0.2] e, ao mesmo tempo, {b}faz cem joules de trabalho. [p=0.3] {c}Quanto vale delta U? [p=0.2] E {d}a temperatura sobe ou desce?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá, com a caixa. [p=0.2] {a}Saem quatrocentos de calor. [p=0.2] {b}Saem também cem de trabalho, porque o gás fez o trabalho. [p=0.3] Não entra nada, e saem quinhentos ao todo: [p=0.2] {c}zero menos quinhentos, [p=0.1] {d}delta U é menos quinhentos joules."),
    dict(id="s18", block="resposta", text="Pela fórmula, dá o mesmo: [p=0.2] {a}quê é menos quatrocentos, tau é mais cem: [p=0.2] {b}menos quatrocentos menos cem, menos quinhentos. [p=0.3] {c}A energia interna diminuiu: [p=0.2] {d}a temperatura desce."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}quê igual a tau mais delta U. [p=0.2] {b}Cada termo pode ser positivo ou negativo, [p=0.2] e {c}na dúvida do sinal, use a caixa: entra soma, sai subtrai."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}em que transformações um desses termos vira zero, [p=0.2] e {b}a conta fica ainda mais curta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
