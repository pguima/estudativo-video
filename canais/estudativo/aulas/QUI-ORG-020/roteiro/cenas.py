# Estudativo · QUI-ORG-020 — Reações de eliminação (Química · Química Orgânica · Reações orgânicas).
# Habilidade: transformar etanol em eteno por desidratação e reconhecer a eliminação como o caminho oposto da adição.
# Pré-requisitos: QUI-ORG-006, QUI-ORG-018. Próxima: QUI-ORG-021 (oxidação de álcoois: vinagre e bafômetro).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso: CH3–CH2–OH = "cê agá três, cê agá dois, ó agá".
# Fatos: desidratação intramolecular do etanol com H2SO4 concentrado a cerca de 170 °C dá eteno + água; a cerca de 140 °C,
# duas moléculas perdem uma água e dão etoxietano (éter comum). Plástico verde: polietileno de eteno feito do etanol da cana,
# produzido no Brasil desde 2010. Hidratação do eteno (adição de água, com ácido) dá etanol.
# Questão inédita: propan-2-ol → propeno + água (os dois vizinhos do carbono do OH são iguais, só um alceno).

TITULO = "Reações de eliminação"

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
    dict(id="s01", block="gancho", text="{a}Desde dois mil e dez, o Brasil fabrica plástico a partir da cana-de-açúcar. [p=0.3] {b}O etanol da cana perde uma molécula de água [p=0.2] e vira {c}eteno, a matéria-prima de um plástico muito comum. [p=0.3] {d}Essa perda tem nome: reação de eliminação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}transformar etanol em eteno no papel [p=0.2] e {c}ver por que a eliminação é a adição de trás para a frente. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas aulas. [p=0.2] {a}O álcool tem o ó agá preso a um carbono de ligações simples, [p=0.2] como o etanol, {b}cê agá três, cê agá dois, ó agá. [p=0.3] E {c}na adição, a dupla se abre e duas moléculas viram uma."),
    # o que é eliminação
    dict(id="s04", block="elimina", text="A eliminação faz o contrário. [p=0.2] {a}Uma molécula perde um pedaço pequeno, [p=0.2] e {b}os dois carbonos que ficaram com uma vaga cada {c}se ligam de novo, formando uma dupla. [p=0.3] {d}Entra uma molécula, e saem duas."),
    # desidratação do etanol
    dict(id="s05", block="etanol", text="No etanol, o pedaço que sai é {a}água. [p=0.2] Por isso o nome {b}desidratação. [p=0.3] Aqueça o etanol a cerca de cento e setenta graus, {c}com ácido sulfúrico concentrado, que puxa a água."),
    dict(id="s06", block="etanol", text="{a}O ó agá sai do carbono dele. [p=0.2] {b}Um hidrogênio sai do carbono vizinho. [p=0.2] {c}Juntos, viram agá dois ó. [p=0.3] {d}Os dois carbonos ficam com uma vaga cada, e fecham uma ligação dupla: [p=0.2] {e}é o eteno, cê agá dois, dupla, cê agá dois."),
    # caminho oposto
    dict(id="s07", block="volta", text="Agora, volte à adição. [p=0.2] {a}Também dá para juntar água ao eteno, com um ácido ajudando, [p=0.1] {b}e sai etanol: é uma adição de água. [p=0.3] {c}A eliminação é esse mesmo caminho, de trás para a frente. [p=0.3] {d}Na adição, a dupla abre. [p=0.1] {e}Na eliminação, a dupla fecha."),
    # erro
    dict(id="s08", block="erro", text="O erro mais comum é {a}tirar o hidrogênio do mesmo carbono do ó agá. [p=0.3] {b}Aí os dois pedaços saem de um carbono só, [p=0.2] e {c}não sobra vaga no vizinho para fechar a dupla. [p=0.3] {d}O hidrogênio sai sempre do carbono ao lado."),
    # atalho
    dict(id="s09", block="atalho", text="O atalho de prova: [p=0.2] {a}risque o ó agá, [p=0.2] {b}risque um hidrogênio do carbono vizinho, [p=0.2] e {c}desenhe a dupla entre esses dois carbonos. [p=0.3] {d}O que você riscou forma a água."),
    dict(id="s10", block="atalho", text="{a}Cuidado com a temperatura: a cerca de cento e quarenta graus, [p=0.2] {b}duas moléculas de etanol perdem uma água só, e o que se forma é um éter. [p=0.3] {c}E se o carbono do ó agá tiver dois vizinhos diferentes, podem sair dois alcenos: [p=0.2] em geral, sai mais o que tem a dupla no meio da cadeia, regra que fica para outra aula."),
    # questão
    dict(id="s11", block="questao", text="Hora de testar. [p=0.2] O propan dois ol, com o ó agá no carbono dois, o do meio, é {a}cê agá três, cê agá com ó agá, cê agá três. [p=0.3] {b}Na desidratação, que alceno se forma? [p=0.2] {c}E que molécula pequena sai?"),
    dict(id="s12", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s13", block="resposta", text="Use o atalho. [p=0.2] {a}Risque o ó agá do carbono do meio. [p=0.2] {b}Risque um hidrogênio de um carbono vizinho, um dos cê agá três. [p=0.3] {c}Os dois vizinhos são iguais, então tanto faz qual. [p=0.3] {d}Desenhe a dupla: [p=0.1] {e}cê agá dois, dupla, cê agá, cê agá três, o propeno."),
    dict(id="s14", block="resposta", text="{a}O ó agá e o hidrogênio riscados formam a molécula pequena: [p=0.1] {b}água."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}na eliminação, uma molécula perde um pedaço pequeno e forma uma dupla. [p=0.2] {b}O etanol perde água e vira eteno, [p=0.2] e {c}a eliminação é a adição de trás para a frente."),
    dict(id="s16", block="fim", text="Na próxima aula, outro destino do álcool: [p=0.2] {a}a oxidação, [p=0.2] que explica por que {b}o vinho vira vinagre e como funciona {c}o bafômetro. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
