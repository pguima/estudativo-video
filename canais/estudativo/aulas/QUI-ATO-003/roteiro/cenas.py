# Estudativo · QUI-ATO-003 — Modelo de Bohr: saltos e cores (Química · Átomo e Tabela Periódica · Modelos atômicos).
# Habilidade: explicar as cores dos fogos de artifício e do teste de chama pelos saltos dos elétrons entre os níveis de energia.
# Pré-requisitos: QUI-ATO-002. Próxima: QUI-ATO-004 (prótons, nêutrons e elétrons: Z, A, íons e isótopos).
# Questão inédita, criada para esta aula. Camadas narradas pelas letras: K = "cá", L = "éle", M = "eme", N = "ene".
# Fatos: Niels Bohr (dinamarquês), 1913; camadas K a Q (sete); cores de chama: estrôncio vermelho, bário verde, sódio amarelo,
# cobre verde-azulado; lâmpada de vapor de sódio da iluminação pública (amarelo-alaranjada); o sal de cozinha (NaCl) tem sódio.
# O modelo atual (quântico, orbital) só é citado como assunto de outra aula.

TITULO = "Modelo de Bohr: saltos e cores"

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
    dict(id="s01", block="gancho", text="{a}Fogos de artifício vermelhos, verdes, amarelos. [p=0.3] {b}Essas cores não vêm de tinta. [p=0.3] {c}Vêm dos elétrons, [p=0.1] {d}pulando de um lugar para outro dentro do átomo."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai explicar {a}a cor dos fogos [p=0.2] e {b}o teste de chama [p=0.2] com {c}o modelo de Bohr."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}o átomo tem um núcleo pequeno e positivo [p=0.1] e, em volta, {b}a eletrosfera, com os elétrons negativos."),
    # o problema de Rutherford
    dict(id="s04", block="problema", text="No modelo de Rutherford, os elétrons giram em volta do núcleo, como planetas em volta do Sol. [p=0.2] Só que isso tinha {a}um problema. [p=0.2] Pela física da época, um elétron girando {b}perderia energia aos poucos [p=0.2] e {c}cairia no núcleo, em espiral. [p=0.3] {d}O átomo desmontaria numa fração de segundo. [p=0.2] E os átomos não desmontam."),
    # os níveis
    dict(id="s05", block="niveis", text="Em mil novecentos e treze, o dinamarquês {a}Niels Bohr propôs uma saída. [p=0.2] {b}O elétron só pode ficar em certos níveis de energia, [p=0.1] chamados {c}camadas. [p=0.3] A partir do núcleo, elas recebem {d}as letras cá, éle, eme e ene, [p=0.1] e assim por diante, até a sétima. [p=0.2] {e}Também se usa número: a camada um é a cá, a dois é a éle."),
    dict(id="s06", block="niveis", text="{a}Pense numa escada. [p=0.2] Você pisa num degrau ou no outro, [p=0.1] {b}nunca no meio. [p=0.3] {c}Degrau mais alto, mais longe do núcleo, é mais energia. [p=0.3] E, enquanto o elétron fica no seu degrau, [p=0.1] {d}ele não perde energia. [p=0.2] {e}Assim, o átomo não desmonta."),
    # o salto
    dict(id="s07", block="salto", text="Para subir de degrau, {a}o elétron precisa receber energia, [p=0.2] {b}na medida exata do salto. [p=0.2] Essa energia pode vir {c}do calor de uma chama ou da eletricidade. [p=0.3] Lá em cima, ele fica {d}excitado: [p=0.1] {e}um estado instável, que não dura."),
    dict(id="s08", block="salto", text="{a}Logo, o elétron volta para o degrau de antes [p=0.2] e {b}devolve a energia em forma de luz. [p=0.3] {c}A cor da luz depende do tamanho do salto. [p=0.3] E cada elemento tem {d}os seus próprios degraus. [p=0.2] {e}Por isso, cada elemento tem a sua cor."),
    # as cores
    dict(id="s09", block="cores", text="É isso que acontece nos fogos de artifício. [p=0.2] {a}O estrôncio dá vermelho. [p=0.2] {b}O bário, verde. [p=0.2] {c}O sódio, amarelo. [p=0.2] {d}O cobre, verde-azulado."),
    dict(id="s10", block="cores", text="No laboratório, a mesma ideia vira {a}o teste de chama: [p=0.2] {b}põe um pouco da amostra no fogo [p=0.1] e {c}olha a cor. [p=0.2] {d}Amarelo forte? Tem sódio. [p=0.3] E a luz amarelada {e}dos postes antigos, com lâmpada de sódio, [p=0.1] vem do mesmo salto."),
    dict(id="s11", block="cores", text="O modelo de Bohr {a}não é o mais moderno: [p=0.2] o atual {b}é assunto de outra aula. [p=0.3] Mas é {c}o de Bohr que a prova usa para explicar a luz."),
    # erro
    dict(id="s12", block="erro", text="O erro comum: [p=0.1] {a}dizer que a luz sai quando o elétron sobe. [p=0.3] {b}Para subir, o elétron recebe energia. [p=0.2] {c}A luz sai na volta, quando ele devolve essa energia."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.1] {a}fogos, teste de chama, lâmpada de sódio, letreiro de néon. [p=0.3] Apareceu luz com cor própria? [p=0.1] {b}A resposta é Bohr. [p=0.3] {c}Recebe energia, sobe, volta, solta luz."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a luz de cor própria de um elemento vem desse salto. [p=0.3] {b}Só cuidado com alternativa que fala do núcleo se partindo: [p=0.2] {c}a cor da chama não mexe no núcleo, só nos elétrons."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] O sal de cozinha tem sódio. [p=0.2] {a}Uma pitada cai na chama do fogão, [p=0.1] e {b}a chama fica amarela. [p=0.3] {c}Explique pelo modelo de Bohr, [p=0.1] {d}em quatro passos."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Primeiro: o calor da chama dá energia aos elétrons do sódio. [p=0.2] {b}Segundo: eles sobem para uma camada mais externa e ficam excitados. [p=0.2] {c}Terceiro: voltam para a camada de antes. [p=0.2] {d}Quarto: devolvem a energia como luz amarela, a cor própria do sódio. [p=0.3] {e}Repare: a luz sai no quarto passo, na volta, e não no segundo."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}o elétron só fica em certas camadas. [p=0.2] {b}Recebe energia e sobe. [p=0.1] {c}Volta e solta luz, [p=0.1] {d}com a cor própria de cada elemento."),
    dict(id="s19", block="fim", text="Na próxima aula, você entra no átomo e conta {a}prótons, nêutrons e elétrons, [p=0.2] e descobre {b}o que são íons e isótopos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
