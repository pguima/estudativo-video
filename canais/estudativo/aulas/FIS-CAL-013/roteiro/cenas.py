# Estudativo · FIS-CAL-013 — A primeira lei em cada transformação (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: dizer qual termo some em cada caso: isotérmica sem ΔU, isovolumétrica sem τ, adiabática sem Q, e ciclo sem ΔU.
# Pré-requisitos: FIS-CAL-012 (primeira lei). Próxima: FIS-CAL-014.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Isotérmica, isobárica e isovolumétrica (isocórica) vêm de QUI-CAL-011; adiabática é termo novo, explicado na hora.
# Isobárica: nenhum termo some (fica citada em uma frase, porque as provas a cobram junto).

TITULO = "A primeira lei em cada transformação"

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
    dict(id="s01", block="gancho", text="{a}Abra uma garrafa de refrigerante. [p=0.3] {b}Às vezes, aparece uma fumacinha branca no gargalo. [p=0.3] {c}É vapor de água que esfriou e virou gotinhas. [p=0.2] {d}Mas quem esfriou esse gás, se nada gelado encostou nele?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer, em cada transformação, {b}qual termo da primeira lei vira zero, [p=0.2] e {c}resolver a questão quase sem conta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a primeira lei, quê igual a tau mais delta U; [p=0.2] e {c}que delta U acompanha a temperatura: [p=0.1] subiu, é positivo; [p=0.1] desceu, é negativo; [p=0.1] {d}não mudou, é zero. [p=0.3] Se faltar alguma, procure no canal."),
    # isotérmica
    dict(id="s04", block="isotermica", text="{a}Primeira: a isotérmica. [p=0.2] {b}Iso quer dizer igual, e térmica, temperatura. [p=0.3] {c}Temperatura igual, delta U igual a zero. [p=0.3] Sobra {d}quê igual a tau: [p=0.2] {e}o calor e o trabalho são iguais."),
    dict(id="s05", block="isotermica", text="Exemplo: [p=0.2] numa expansão isotérmica, {a}o gás recebe oitocentos joules de calor. [p=0.2] {b}Ele faz oitocentos joules de trabalho. [p=0.3] {c}Nem um joule fica guardado, [p=0.2] por isso a temperatura não muda."),
    # isovolumétrica
    dict(id="s06", block="isovolumetrica", text="{a}Segunda: a isovolumétrica, também chamada de isocórica. [p=0.2] {b}Volume igual, delta vê igual a zero. [p=0.3] E {c}tau é pê vezes delta vê: [p=0.2] {d}trabalho zero. [p=0.3] Sobra {e}quê igual a delta U: [p=0.2] {f}todo o calor fica no gás e muda a temperatura."),
    dict(id="s07", block="isovolumetrica", text="{a}Um gás num recipiente rígido recebe duzentos joules. [p=0.2] {b}O volume não muda, [p=0.2] então {c}a energia interna sobe duzentos joules. [p=0.3] {d}No gráfico pê vê, ela é uma linha em pé: [p=0.2] {e}área zero, trabalho zero."),
    # adiabática
    dict(id="s08", block="adiabatica", text="{a}Terceira: a adiabática. [p=0.2] {b}O nome quer dizer que o calor não atravessa: é a transformação sem troca de calor. [p=0.3] Acontece {c}quando o gás está bem isolado, [p=0.2] ou {d}quando tudo é rápido demais para o calor passar. [p=0.3] {e}Quê igual a zero. [p=0.2] Sobra {f}zero igual a tau mais delta U: [p=0.2] {g}delta U igual a menos tau."),
    dict(id="s09", block="adiabatica", text="Em palavras: [p=0.2] {a}se o gás se expande e faz trabalho, ele paga com a própria energia interna, [p=0.2] e {b}esfria. [p=0.3] {c}É a fumacinha do gancho: [p=0.2] o gás sai de repente, se expande e esfria tanto que o vapor de água vira gotinhas. [p=0.3] {d}Se é comprimido depressa, ele esquenta, [p=0.2] como o ar da bomba de encher pneu."),
    dict(id="s10", block="adiabatica", text="Exemplo: [p=0.2] {a}um gás é comprimido de repente e recebe trezentos joules de trabalho. [p=0.2] {b}Tau é menos trezentos. [p=0.2] {c}Delta U é menos tau: [p=0.1] {d}mais trezentos joules. [p=0.2] {e}O gás esquenta."),
    # ciclo
    dict(id="s11", block="ciclo", text="{a}Quarta: o ciclo. [p=0.2] {b}O gás termina onde começou, [p=0.1] com a mesma temperatura. [p=0.3] {c}Delta U igual a zero de novo, [p=0.2] e {d}quê igual a tau. [p=0.3] {e}Se a área de dentro do ciclo é trezentos quilojoules, [p=0.2] {f}o saldo de calor de cada volta, o que entra menos o que sai, também é trezentos quilojoules."),
    dict(id="s12", block="ciclo", text="E {a}a isobárica, com pressão constante? [p=0.2] {b}Nela, nenhum termo some: [p=0.2] {c}o gás troca calor, faz trabalho e muda de temperatura. [p=0.2] {d}Use a lei inteira."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que isotérmica não troca calor. [p=0.3] {b}Troca, sim: quê é igual a tau, e não zero. [p=0.2] {c}A temperatura fica igual justamente porque o calor entra e sai como trabalho. [p=0.3] {d}A que não troca calor é a adiabática, [p=0.2] e nela {e}a temperatura muda."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}cada caso tem uma coisa que não muda, e ela zera um termo. [p=0.3] {b}Temperatura parada, delta U zero. [p=0.2] {c}Volume parado, tau zero. [p=0.2] {d}Calor sem passar, quê zero. [p=0.2] {e}Voltou ao começo, delta U zero."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada termo zera por um motivo só: [p=0.2] delta U, se a temperatura não muda; [p=0.1] tau, se o volume não muda; [p=0.1] quê, se não passa calor. [p=0.3] {b}Não compensa na isobárica: [p=0.2] nada some, {c}e você faz a conta inteira."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um gás passa por {a}uma expansão adiabática [p=0.2] e {b}faz quinhentos joules de trabalho. [p=0.3] {c}Quanto vale delta U? [p=0.2] E {d}o gás esquenta ou esfria?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Adiabática: quê igual a zero. [p=0.2] {b}Expansão, o gás faz trabalho: tau é mais quinhentos. [p=0.3] {c}Delta U é menos tau: [p=0.1] {d}menos quinhentos joules. [p=0.3] {e}A energia interna caiu, então o gás esfria. [p=0.2] Como o gás que sai do refrigerante."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}isotérmica e ciclo, sem delta U; [p=0.2] {b}isovolumétrica, sem tau; [p=0.2] {c}adiabática, sem quê; [p=0.2] e {d}isobárica, com a lei inteira."),
    dict(id="s20", block="fim", text="Na próxima aula, o ciclo vira {a}motor: [p=0.2] você vai calcular {b}o rendimento de uma máquina térmica [p=0.2] e ver {c}por que nenhuma transforma todo o calor em trabalho. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
