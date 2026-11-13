# Estudativo · QUI-ATO-002 — Modelo de Rutherford: o experimento do ouro (Química · Átomo e Tabela Periódica · Modelos atômicos).
# Habilidade: explicar por que a maioria das partículas alfa atravessa a lâmina de ouro e concluir que o átomo tem um núcleo
# pequeno e positivo e muito espaço vazio.
# Pré-requisitos: QUI-ATO-001. Próxima: QUI-ATO-003 (Bohr: camadas, saltos e as cores dos fogos).
# Questão inédita, criada para esta aula.
# Fatos: experimento de Geiger e Marsden no laboratório de Rutherford (neozelandês), 1909, modelo publicado em 1911;
# folha de ouro com menos de um milésimo de milímetro (fio de cabelo: 0,05 a 0,1 mm); tela de sulfeto de zinco que cintila;
# cerca de 1 em 8 000 alfas voltava; núcleo de 10 mil a 100 mil vezes menor que o átomo (estádio e bolinha de gude).
# Próton e nêutron ficam para a QUI-ATO-004; radioatividade, para outra trilha.

TITULO = "Modelo de Rutherford: o experimento do ouro"

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
    dict(id="s01", block="gancho", text="{a}Imagine atirar bolinhas contra uma folha de papel [p=0.2] e {b}algumas voltarem na sua direção. [p=0.3] Foi o que aconteceu {c}no laboratório de Ernest Rutherford, [p=0.1] há mais de cem anos. [p=0.3] {d}E isso mudou a imagem do átomo."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai entender {a}por que a maioria atravessou, [p=0.2] {b}por que algumas voltaram [p=0.2] e {c}o que isso revelou: o núcleo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}no modelo de Thomson, o átomo é uma esfera positiva com elétrons espalhados. [p=0.3] {b}Cargas iguais se repelem. [p=0.1] {c}Cargas opostas se atraem."),
    # o projétil e a montagem
    dict(id="s04", block="alfa", text="O projétil do experimento é {a}a partícula alfa. [p=0.2] Ela é {b}minúscula, positiva e muito rápida, [p=0.2] e sai {c}de um material radioativo. [p=0.3] Radioatividade {d}é assunto de outra aula. [p=0.2] Aqui, basta saber que a alfa é {e}um projétil positivo."),
    dict(id="s05", block="alfa", text="Rutherford mirou as alfas em {a}uma folha de ouro finíssima, [p=0.1] muito mais fina que um fio de cabelo. [p=0.3] {b}Em volta, uma tela que brilha no ponto onde a partícula bate. [p=0.3] Assim dava para ver {c}o caminho de cada uma."),
    dict(id="s06", block="alfa", text="Pelo modelo de Thomson, o que se esperava? [p=0.2] {a}A carga positiva está espalhada pela esfera toda, [p=0.1] fraca em cada ponto. [p=0.2] Então, {b}todas as alfas deviam atravessar, [p=0.1] {c}quase em linha reta."),
    # as três observações
    dict(id="s07", block="resultado", text="{a}Primeira observação: [p=0.1] {b}a grande maioria atravessou reto, sem desviar. [p=0.3] Se quase nada atrapalha o caminho, {c}o átomo é quase todo espaço vazio."),
    dict(id="s08", block="resultado", text="{a}Segunda: [p=0.1] {b}algumas desviaram. [p=0.3] A alfa é positiva, e desvia quando passa perto de outra carga positiva, que a empurra. [p=0.2] Então, {c}existe no átomo uma região positiva."),
    dict(id="s09", block="resultado", text="{a}Terceira, a surpresa: [p=0.1] {b}pouquíssimas voltaram. [p=0.3] Para jogar de volta um projétil tão rápido, [p=0.1] {c}essa região precisa ser muito pequena [p=0.1] e {d}concentrar quase toda a massa do átomo. [p=0.3] Essa região é {e}o núcleo."),
    # o modelo nuclear
    dict(id="s10", block="nuclear", text="O modelo de Rutherford: [p=0.1] {a}no centro, um núcleo pequeno e positivo, com quase toda a massa. [p=0.2] Em volta, {b}a eletrosfera, a região onde os elétrons giram em volta do núcleo. [p=0.3] {c}Ela ocupa quase todo o tamanho do átomo."),
    dict(id="s11", block="nuclear", text="O núcleo é {a}de dez mil a cem mil vezes menor que o átomo. [p=0.3] Se o átomo fosse {b}um estádio de futebol, [p=0.2] o núcleo seria {c}uma bolinha de gude no meio do campo."),
    # erro
    dict(id="s12", block="erro", text="O erro comum: [p=0.1] {a}achar que, por ter quase toda a massa, o núcleo é grande. [p=0.3] {b}É o contrário: [p=0.1] {c}o núcleo é pesado e minúsculo. [p=0.2] Quem dá o tamanho do átomo é {d}a eletrosfera: enorme, quase vazia e quase sem massa. [p=0.3] Por isso a maioria das alfas atravessa: [p=0.1] {e}passa pela eletrosfera, longe do núcleo."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova é {a}uma tabela de três linhas. [p=0.2] {b}Atravessou: átomo vazio. [p=0.2] {c}Desviou: região positiva. [p=0.2] {d}Voltou: núcleo pequeno e denso, [p=0.1] ou seja, muita massa num espaço minúsculo."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada observação leva a uma conclusão diferente, [p=0.2] e a prova costuma trocar uma pela outra. [p=0.3] {b}A tabela não basta quando a questão pede o porquê do desvio. [p=0.2] Aí, use as cargas: [p=0.1] {c}o núcleo positivo empurra a alfa positiva."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] No experimento da folha de ouro, [p=0.1] {a}qual observação mostrou que o átomo é quase todo vazio? [p=0.2] E {b}qual mostrou que existe uma região muito pequena, com quase toda a massa? [p=0.3] {c}Letra á: a maioria atravessou. [p=0.2] {d}Letra bê: algumas desviaram. [p=0.2] {e}Letra cê: pouquíssimas voltaram."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Átomo vazio é {a}caminho livre: [p=0.1] {b}a maioria atravessou, letra á. [p=0.3] Região pequena e pesada é {c}o que joga a alfa de volta: [p=0.1] {d}pouquíssimas voltaram, letra cê. [p=0.3] A letra bê, as que desviaram, mostra outra coisa: [p=0.1] {e}que essa região é positiva."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}a maioria atravessa porque o átomo é quase vazio, [p=0.2] e {b}as poucas que voltam revelam um núcleo pequeno, positivo e com quase toda a massa."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}Bohr organiza os elétrons em camadas [p=0.2] e explica {b}as cores dos fogos de artifício. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
