# Estudativo · QUI-ORG-021 — Oxidação de álcoois (Química · Química Orgânica · Reações orgânicas).
# Habilidade: prever o que vira um álcool primário, secundário e terciário ao oxidar e explicar o vinagre e o bafômetro.
# Pré-requisitos: QUI-ORG-008, QUI-ELE-002. Próxima: QUI-ORG-022 (esterificação: ácido + álcool → éster + água).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso. Nox do carbono do OH no etanol: −1; no etanal: +1; no ácido: +3.
# Fatos: vinagre = ácido acético (etanoico) de 4 a 6%, feito por bactérias (Acetobacter) que oxidam o etanol com o oxigênio do ar.
# Bafômetro químico: dicromato de potássio (K2Cr2O7, laranja, Cr +6) vira Cr3+ (verde) ao oxidar o etanol. Os aparelhos da
# polícia hoje são quase todos eletrônicos (célula de combustível), mas a reação química é a que cai em prova.
# Terciário não oxida em condições brandas. Metanol (3 H no carbono) vai além: fica fora da aula.
# Questão inédita: butan-2-ol → butanona; 2-metilpropan-2-ol → não oxida.

TITULO = "Oxidação de álcoois"

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
    dict(id="s01", block="gancho", text="{a}Vinho esquecido aberto vira vinagre. [p=0.3] {b}O bafômetro químico muda de cor com o hálito de quem bebeu. [p=0.3] {c}As duas coisas são o mesmo tipo de reação: [p=0.2] {d}a oxidação do álcool."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai prever o que vira {b}um álcool primário, {c}um secundário e {d}um terciário ao oxidar, [p=0.2] e explicar {e}o vinagre e o bafômetro. [p=0.2] E ainda leva um {f}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de três coisas. [p=0.2] {a}Oxidar é perder elétrons, e o número de oxidação sobe. [p=0.3] {b}O aldeído tem o cê dupla ó na ponta da cadeia; {c}a cetona, no meio. [p=0.2] E {d}o ácido carboxílico tem o cê ó ó agá."),
    dict(id="s04", block="lembrete", text="O álcool também se classifica pelo {a}carbono do ó agá. [p=0.2] {b}Ligado a um carbono, é álcool primário. [p=0.2] {c}A dois, secundário. [p=0.2] {d}A três, terciário."),
    # primário
    dict(id="s05", block="primario", text="Comece pelo etanol, um álcool primário. [p=0.2] {a}Um oxidante, que pode ser o oxigênio do ar com a ajuda de bactérias, [p=0.2] {b}tira dois hidrogênios: [p=0.1] {c}o do ó agá e um do carbono do ó agá. [p=0.3] {d}No lugar, aparece a dupla cê ó: [p=0.2] {e}é o etanal, um aldeído."),
    dict(id="s06", block="primario", text="E o aldeído ainda oxida. [p=0.2] {a}No lugar do hidrogênio que sobrou naquele carbono, entra um ó agá, [p=0.2] e {b}sai o ácido etanoico, o ácido acético. [p=0.3] {c}É o vinagre: o vinho azeda assim."),
    dict(id="s07", block="primario", text="Confira pelo número de oxidação daquele carbono: [p=0.2] {a}menos um no etanol, [p=0.1] {b}mais um no etanal, [p=0.1] {c}mais três no ácido. [p=0.3] {d}Ele sobe a cada passo: é oxidação."),
    # secundário e terciário
    dict(id="s08", block="secterc", text="{a}Num álcool secundário, como o propan dois ol, [p=0.2] o carbono do ó agá tem {b}um hidrogênio só. [p=0.3] {c}Ele sai junto com o do ó agá, e forma a dupla cê ó no meio da cadeia: [p=0.2] {d}a propanona, a acetona, uma cetona. [p=0.3] {e}Não sobra hidrogênio ali, e a oxidação para."),
    dict(id="s09", block="secterc", text="{a}No álcool terciário, o carbono do ó agá não tem nenhum hidrogênio. [p=0.3] {b}Sem ele, a dupla cê ó não se forma, [p=0.2] e {c}o álcool não oxida."),
    # bafômetro
    dict(id="s10", block="bafometro", text="O bafômetro químico usa isso. [p=0.2] {a}Dentro dele há dicromato de potássio, que é laranja. [p=0.3] {b}O etanol do hálito se oxida, [p=0.2] e {c}o crômio do dicromato ganha elétrons, ou seja, se reduz. [p=0.3] {d}O número de oxidação do crômio cai de mais seis para mais três, [p=0.2] e {e}a cor passa de laranja para verde."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}achar que todo álcool oxida, [p=0.2] e que {b}o terciário vira cetona. [p=0.3] {c}Para virar cetona, o carbono do ó agá precisa perder um hidrogênio, [p=0.2] e {d}o terciário não tem nenhum para perder."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}conte os hidrogênios do carbono do ó agá. [p=0.3] {b}Dois hidrogênios: vira aldeído, e depois ácido. [p=0.2] {c}Um: vira cetona. [p=0.2] {d}Nenhum: não oxida. [p=0.3] Funciona porque {e}cada passo da oxidação gasta um hidrogênio daquele carbono."),
    dict(id="s13", block="atalho", text="{a}Só não use o atalho no metanol, que tem três hidrogênios nesse carbono [p=0.2] e vai ainda mais longe: [p=0.1] isso fica para outra aula."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}O que se forma ao oxidar o butan dois ol, de quatro carbonos, com o ó agá no carbono dois? [p=0.3] {b}E o dois metil propan dois ol, em que o carbono do ó agá está preso a três grupos cê agá três?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}No butan dois ol, o ó agá está no carbono dois, [p=0.2] ligado a dois carbonos: secundário. [p=0.2] {b}Esse carbono tem um hidrogênio. [p=0.2] {c}Um hidrogênio, cetona: [p=0.1] {d}a butanona."),
    dict(id="s17", block="resposta", text="{a}No dois metil propan dois ol, o carbono do ó agá está ligado a três carbonos: terciário. [p=0.2] {b}Nenhum hidrogênio nele. [p=0.2] {c}Não oxida."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}o primário vira aldeído e depois ácido, [p=0.1] {b}o secundário vira cetona [p=0.1] e {c}o terciário não oxida. [p=0.3] {d}O vinagre é o etanol oxidado até ácido, [p=0.2] e {e}o bafômetro mostra o crômio se reduzindo."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai juntar {a}um ácido com um álcool [p=0.2] e fabricar {b}um éster, a molécula do cheiro das frutas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
