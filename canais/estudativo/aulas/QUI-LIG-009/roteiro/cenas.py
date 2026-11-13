# Estudativo · QUI-LIG-009 — Três forças intermoleculares (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: apontar a força principal entre moléculas de CH₄, HCl e H₂O: dipolo induzido, dipolo permanente ou ligação de hidrogênio.
# Pré-requisitos: QUI-LIG-007. Próxima: QUI-LIG-010 (comparar pontos de ebulição).
# Atenção: LIG-001, 003, 004 e 008 NÃO estão em "Já ensinado" (nada de íons, sal dissolvendo ou ponto de fusão de iônico).
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Leituras: HF = "agá éfe", HCl = "agá cê éle", H₂S = "agá dois esse", CH₄ = "cê agá quatro"; F, O, N = "éfe, ó, ene".
# Fatos: ordem de força (moléculas de tamanho parecido): ligação de H > dipolo permanente > dipolo induzido (London);
# o dipolo induzido existe entre todas as moléculas; ligação de H exige H ligado direto a F, O ou N; H₂S polar (angular, S
# sem ser F/O/N) = dipolo permanente; CO₂ apolar = dipolo induzido; HF = ligação de H. F, O e N estão entre os mais
# eletronegativos (o Cl, 3,2, fica entre O e N, mas é grande demais para a ligação de H).

TITULO = "Três forças intermoleculares"

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
    dict(id="s01", block="gancho", text="{a}Quando a água ferve, as bolhas não são de hidrogênio nem de oxigênio. [p=0.2] {b}O vapor ainda é agá dois ó. [p=0.3] {c}Então, o que a fervura rompe? [p=0.2] {d}As forças que seguram uma molécula na outra."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai conhecer {b}três forças entre moléculas [p=0.1] e apontar {c}a principal no metano, no agá cê éle e na água. [p=0.2] E leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de polaridade: [p=0.1] {a}molécula polar tem um lado delta mais e um lado delta menos. [p=0.2] {b}Molécula apolar não tem polos. [p=0.2] E {c}o flúor, o oxigênio e o nitrogênio estão entre os átomos mais eletronegativos. [p=0.2] Se faltar alguma aula, procure no canal."),
    # dentro e fora
    dict(id="s04", block="inter", text="{a}Dentro da molécula, os átomos estão presos por ligações covalentes, fortes. [p=0.3] {b}Entre uma molécula e outra, há forças bem mais fracas: [p=0.1] {c}as forças intermoleculares. [p=0.3] {d}Ferver separa as moléculas: [p=0.1] {e}rompe só as forças de fora, não as ligações de dentro."),
    # dipolo permanente
    dict(id="s05", block="permanente", text="A primeira força aparece entre {a}moléculas polares, como o agá cê éle: [p=0.1] o cloro puxa mais o par, e a molécula fica com polos. [p=0.2] {b}O lado delta mais de uma molécula atrai o lado delta menos da vizinha. [p=0.3] Como esses polos estão sempre lá, {c}a força se chama dipolo permanente, [p=0.1] ou dipolo-dipolo."),
    # ligação de hidrogênio
    dict(id="s06", block="hidrogenio", text="{a}Existe um caso especial, mais forte. [p=0.2] {b}Quando o hidrogênio está ligado direto a flúor, oxigênio ou nitrogênio, [p=0.1] {c}esses átomos puxam tanto o par de elétrons da ligação que o hidrogênio fica muito positivo. [p=0.3] {d}Ele gruda num par livre do flúor, oxigênio ou nitrogênio da molécula vizinha. [p=0.3] {e}É a ligação de hidrogênio, a força entre as moléculas de água."),
    # dipolo induzido
    dict(id="s07", block="induzido", text="E as moléculas apolares, {a}como o metano, cê agá quatro? [p=0.2] {b}Os elétrons não ficam parados. [p=0.2] {c}Por um instante, sobram mais elétrons de um lado: [p=0.1] {d}aparece um dipolo relâmpago, que os livros chamam de dipolo instantâneo. [p=0.3] {e}Ele empurra os elétrons da vizinha e cria nela outro dipolo. [p=0.3] {f}É o dipolo induzido, também chamado de força de London, a mais fraca das três."),
    dict(id="s08", block="induzido", text="{a}O dipolo induzido existe entre todas as moléculas, [p=0.1] {b}mas, nas apolares, é o único. [p=0.3] Em moléculas de tamanho parecido, a ordem de força é: [p=0.1] {c}ligação de hidrogênio, [p=0.1] {d}dipolo permanente, [p=0.1] {e}dipolo induzido."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a ligação de hidrogênio é a ligação entre o hidrogênio e o oxigênio dentro da água. [p=0.3] {b}Aquela é covalente. [p=0.2] {c}A ligação de hidrogênio fica entre uma molécula e outra: [p=0.1] {d}do hidrogênio de uma ao oxigênio da vizinha. [p=0.2] {e}O nome engana: é força intermolecular."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho de prova é uma sequência de perguntas. [p=0.2] {a}Tem hidrogênio ligado direto a flúor, oxigênio ou nitrogênio? [p=0.1] Ligação de hidrogênio. [p=0.3] {b}Não tem, mas a molécula é polar? [p=0.1] Dipolo permanente. [p=0.3] {c}É apolar? [p=0.1] Dipolo induzido. [p=0.3] Para lembrar dos três átomos, {d}éfe, ó, ene: [p=0.1] {e}FON, como em fone."),
    dict(id="s11", block="atalho", text="Funciona porque {a}as perguntas vão da força mais forte para a mais fraca, [p=0.1] e a primeira que der sim é a principal. [p=0.3] {b}Cuidado: hidrogênio preso a carbono não conta. [p=0.2] {c}O metano tem quatro hidrogênios e nenhuma ligação de hidrogênio."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Qual é a força principal entre as moléculas de cada substância? [p=0.2] {a}Agá éfe, o fluoreto de hidrogênio. [p=0.2] {b}Cê ó dois, o gás carbônico. [p=0.2] {c}Agá dois esse, o gás com cheiro de ovo podre."),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá, com as perguntas. [p=0.2] {a}Agá éfe: hidrogênio ligado direto ao flúor. [p=0.1] Ligação de hidrogênio. [p=0.3] {b}Gás carbônico: não tem hidrogênio, e a molécula é linear e apolar. [p=0.1] Dipolo induzido. [p=0.3] {c}Agá dois esse: o enxofre não é éfe, ó nem ene. [p=0.2] {d}Mas a molécula é angular, com pares livres no enxofre: polar. [p=0.1] Dipolo permanente."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}entre moléculas apolares, dipolo induzido; [p=0.1] {b}entre polares, dipolo permanente; [p=0.1] {c}com hidrogênio preso a éfe, ó ou ene, ligação de hidrogênio, a mais forte."),
    dict(id="s16", block="fim", text="Na próxima aula, você usa essas forças para {a}comparar pontos de ebulição, [p=0.2] e descobre por que {b}a água ferve tão acima do agá dois esse. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
