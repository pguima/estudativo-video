# Estudativo · QUI-ELE-003 — Pilha de Daniell (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: explicar o caminho dos elétrons pelo fio (a corrente) e o dos íons pela ponte salina, dizer qual placa perde massa
# e quem é ânodo e cátodo.
# Pré-requisitos: QUI-ELE-002, FIS-ELE-008. Próxima: QUI-ELE-004 (calcular a ddp de 1,10 V e prever a reação pelo potencial).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: John Frederic Daniell, 1836. Ponte salina: tubo com solução de um sal (KNO₃ ou KCl). Na Daniell real, a lâmpada pequena
# acende fraca; o voltímetro marca cerca de 1,1 V (o cálculo fica para a próxima aula). Ni é mais reativo que Ag (fila).
# A ponte: ânions vão para o lado do zinco (sobra Zn²⁺), cátions para o lado do cobre (sobra SO₄²⁻). Elétron nunca passa na ponte.
# Sentido convencional da corrente (FIS-ELE-008): do + para o −, contrário ao dos elétrons.

TITULO = "Pilha de Daniell"

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
    dict(id="s01", block="gancho", text="{a}Zinco no sulfato de cobre: [p=0.1] o zinco perde elétrons, o cobre ganha, [p=0.2] e {b}a energia sai como um pouco de calor. [p=0.3] {c}Agora, separe os dois em potes diferentes [p=0.1] e ligue por um fio. [p=0.3] {d}A mesma reação acende uma lampadinha, fraquinha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai seguir {b}o caminho dos elétrons pelo fio [p=0.1] e {c}o dos íons pela ponte salina, [p=0.2] e dizer {d}qual placa se gasta. [p=0.2] E ainda leva um {e}macete para não trocar ânodo e cátodo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}No zinco com cobre dois mais, o zinco se oxida e o cobre se reduz. [p=0.3] E {b}corrente elétrica é carga andando num sentido só, como os elétrons num fio. [p=0.2] Se faltar alguma, procure no canal."),
    # montagem
    dict(id="s04", block="montagem", text="Essa montagem tem nome: {a}pilha de Daniell, de mil oitocentos e trinta e seis. [p=0.3] {b}De um lado, uma placa de zinco numa solução de sulfato de zinco. [p=0.2] {c}Do outro, uma placa de cobre no sulfato de cobre, azul. [p=0.3] {d}Um fio liga as placas, passando por uma lampadinha. [p=0.2] {e}E um tubo com água e sal liga as soluções: [p=0.1] a ponte salina."),
    # elétrons
    dict(id="s05", block="eletrons", text="Siga os elétrons. [p=0.2] {a}Na placa de zinco, cada átomo perde dois elétrons [p=0.1] e vira zinco dois mais, que se solta na solução. [p=0.3] {b}Os elétrons ficam na placa [p=0.1] e {c}fogem pelo fio, até a placa de cobre."),
    dict(id="s06", block="eletrons", text="{a}Lá, os íons cobre dois mais da solução recebem esses elétrons [p=0.1] e {b}viram cobre metálico, grudado na placa. [p=0.3] {c}Elétrons andando pelo fio, num sentido só: [p=0.1] {d}isso é a corrente elétrica. [p=0.3] {e}A energia que antes virava calor agora acende a lâmpada."),
    # ânodo e cátodo
    dict(id="s07", block="polos", text="Cada placa tem nome. [p=0.2] {a}Onde acontece a oxidação, é o ânodo: [p=0.1] aqui, o zinco. [p=0.2] {b}Ele manda elétrons para o fio, então é o polo negativo. [p=0.3] {c}Onde acontece a redução, é o cátodo: [p=0.1] o cobre. [p=0.2] {d}Ele recebe os elétrons: é o polo positivo."),
    dict(id="s08", block="polos", text="{a}Os elétrons andam no fio do ânodo para o cátodo, do negativo para o positivo. [p=0.3] {b}A corrente da Física, a convencional, é marcada ao contrário, [p=0.1] do positivo para o negativo."),
    # massa
    dict(id="s09", block="massa", text="E as placas? [p=0.2] {a}A de zinco vira íon e se dissolve: [p=0.1] {b}ela perde massa, vai ficando fina. [p=0.3] {c}A de cobre recebe metal novo: [p=0.1] {d}ganha massa. [p=0.3] {e}E a solução azul vai clareando, [p=0.1] porque o cobre dois mais, que dá a cor, está virando metal."),
    # ponte salina
    dict(id="s10", block="ponte", text="Falta a ponte salina. [p=0.2] Sem ela, a pilha para em instantes. [p=0.3] {a}Do lado do zinco, entram íons positivos na solução, [p=0.1] e sobra carga positiva. [p=0.2] {b}Do lado do cobre, os íons positivos saem da solução, [p=0.1] e sobra carga negativa, do sulfato."),
    dict(id="s11", block="ponte", text="{a}A ponte equilibra as cargas. [p=0.2] {b}Ela manda íons negativos para o lado do zinco [p=0.1] {c}e íons positivos para o lado do cobre. [p=0.3] {d}As soluções ficam neutras, e os elétrons continuam andando."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que os elétrons voltam pela ponte salina, fechando o caminho. [p=0.3] {b}Elétron não anda solto na água. [p=0.2] {c}Elétrons só passam pelo fio. [p=0.2] {d}Pela ponte, só passam íons."),
    # macete
    dict(id="s13", block="atalho", text="Agora, o macete para não trocar os nomes: [p=0.2] {a}ânodo e oxidação começam com vogal. [p=0.2] {b}Cátodo e redução, com consoante. [p=0.3] {c}Vogal com vogal, consoante com consoante."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o ânodo é sempre onde há oxidação, em qualquer montagem. [p=0.3] {b}Não serve para o sinal do polo: [p=0.1] na eletrólise, assunto de outra aula, o mais e o menos se invertem. [p=0.2] {c}Por isso, guarde o sinal pelo motivo: [p=0.1] na pilha, quem manda elétrons é o negativo."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma pilha tem uma placa de níquel numa solução com íons níquel, [p=0.1] {b}e uma placa de prata numa solução com íons prata. [p=0.2] {c}O níquel é mais reativo: ele se oxida. [p=0.3] {d}Quem é o ânodo? [p=0.2] {e}Para onde vão os elétrons no fio? [p=0.2] {f}Qual placa perde massa? [p=0.2] E {g}para que lado vão os íons negativos da ponte?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}O níquel se oxida: oxidação, vogal, ânodo. [p=0.2] {b}É o polo negativo. [p=0.3] {c}Os elétrons saem do níquel e vão pelo fio até a prata, o cátodo. [p=0.3] {d}A placa de níquel vira íon e perde massa, [p=0.1] {e}e a de prata ganha a prata que se deposita. [p=0.3] {f}Do lado do níquel, entram íons positivos: [p=0.1] é para lá que vão os íons negativos da ponte."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}elétrons andam pelo fio, do ânodo ao cátodo; [p=0.1] {b}íons andam pela ponte; [p=0.1] {c}e o ânodo é a placa que se gasta."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai calcular {a}a tensão dessa pilha, um vírgula dez volt, [p=0.2] e prever se uma reação acontece sozinha. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
