# Estudativo · Questão 024 — ENEM 2025, 2º dia, caderno amarelo, questão 144: num jogo, um cubo (aresta 1) começa em
# x de 5 a 6, y de 1 a 2, z de 6 a 7 (lido nas projeções da figura). Ele se aproxima 3 do plano yz (x − 3), se afasta 5
# do plano xz (y + 5) e se aproxima 4 do plano xy (z − 4): fica em x de 2 a 3, y de 6 a 7, z de 2 a 3. Projeções:
# yz → (y, z) = 6–7 × 2–3; xz → (x, z) = 2–3 × 2–3; xy → (x, y) = 2–3 × 6–7 → alternativa E.
# (Medido nas figuras: A tem z de 3 a 4 na parede yz; B, y de 4 a 5; C e D, y de 5 a 6; só a E tem y de 6 a 7 e z de 2 a 3.)
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Caminho: A FERRAMENTA 1: os três planos coordenados (chão xy, parede do fundo yz, parede da esquerda xz) → A FERRAMENTA 2:
# distância a um plano = a coordenada que falta no nome (yz → x, xz → y, xy → z) → A FERRAMENTA 3: projeção ortogonal
# (a sombra com a luz perpendicular: apaga a coordenada que falta) → passo 1: ler a posição inicial → passo 2: os três
# movimentos → passo 3: as projeções finais → E → por que as outras estão erradas → desafio → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: o cubo que se move no espaço (coordenadas e projeções ortogonais)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e quarenta e quatro do ENEM dois mil e vinte e cinco. [p=0.2] Num jogo de computador, "
        "[p=0.1] um cubo se move no espaço, [p=0.1] sempre na direção de um dos três eixos. [p=0.3] {b}Ele se "
        "*aproxima três* do plano ípsilon zê, [p=0.1] se *afasta cinco* do plano xis zê [p=0.1] e se *aproxima quatro* do plano "
        "xis ípsilon. [p=0.3] {c}Qual figura mostra as *projeções* do cubo [p=0.1] depois desses movimentos? [p=0.3] {d}Nessa "
        "aula, você vai entender o que cada uma dessas palavras quer dizer."),
    dict(id="02", block="planos", text=
        "{a}Primeiro, [p=0.1] os três planos. [p=0.3] {b}O *chão* é o plano xis ípsilon: [p=0.1] ali, só existem xis e ípsilon. "
        "[p=0.3] {c}A parede do *fundo* é o plano ípsilon zê. [p=0.3] {d}E a parede da *esquerda* é o plano xis zê. [p=0.2] "
        "{e}Cada plano tem no nome os dois eixos que ele contém."),
    dict(id="03", block="distancia", text=
        "{a}Agora, [p=0.1] a ideia-chave: [p=0.1] a *distância* até um plano. [p=0.3] {b}A distância até o plano ípsilon zê "
        "[p=0.1] é medida no eixo que *falta* no nome: [p=0.1] o xis. [p=0.3] {c}Até o plano xis zê, [p=0.1] falta o ípsilon. "
        "[p=0.2] {d}E até o plano xis ípsilon, [p=0.1] o chão, [p=0.1] falta o zê: [p=0.1] a altura. [p=0.3] {e}Então, "
        "[p=0.1] aproximar de um plano é *diminuir* essa coordenada. [p=0.1] Afastar é *aumentar.*"),
    dict(id="04", block="projecao", text=
        "{a}E o que é a *projeção ortogonal?* [p=0.3] {b}É a sombra do cubo [p=0.1] com a luz chegando bem de frente, "
        "[p=0.1] perpendicular ao plano. [p=0.3] {c}Na parede ípsilon zê, [p=0.1] a sombra guarda o ípsilon e o zê [p=0.1] e perde o "
        "xis. [p=0.2] {d}No chão, [p=0.1] guarda xis e ípsilon [p=0.1] e perde a altura."),
    dict(id="05", block="inicial", text=
        "{a}Passo um: [p=0.1] onde o cubo começa. [p=0.3] {b}Pelas sombras da figura, [p=0.1] o cubo vai de *cinco a "
        "seis* no xis, [p=0.2] {c}de *um a dois* no ípsilon, [p=0.2] {d}e de *seis a sete* no zê."),
    dict(id="06", block="movimentos", text=
        "{a}Passo dois: [p=0.1] os movimentos. [p=0.3] {b}Aproximou três do plano ípsilon zê: [p=0.1] o xis *diminui três.* "
        "[p=0.1] De cinco a seis, [p=0.1] vai para *dois a três.* [p=0.3] {c}Afastou cinco do plano xis zê: [p=0.1] o ípsilon "
        "*aumenta cinco.* [p=0.1] De um a dois, [p=0.1] vai para *seis a sete.* [p=0.3] {d}Aproximou quatro do plano "
        "xis ípsilon: [p=0.1] o zê *diminui quatro.* [p=0.1] De seis a sete, [p=0.1] vai para *dois a três.*"),
    dict(id="07", block="final", text=
        "{a}Passo três: [p=0.1] as sombras no fim. [p=0.3] {b}Na parede ípsilon zê: [p=0.1] ípsilon de seis a sete, [p=0.1] zê de "
        "dois a três. [p=0.3] {c}Na parede xis zê: [p=0.1] xis de dois a três, [p=0.1] zê de dois a três. [p=0.3] {d}No "
        "chão: [p=0.1] xis de dois a três, [p=0.1] ípsilon de seis a sete. [p=0.3] {e}Só uma figura tem as três sombras "
        "nesses lugares: [p=0.1] a alternativa *E.*"),
    dict(id="08", block="pegadinhas", text=
        "{a}Para conferir, [p=0.1] basta olhar a sombra na parede do fundo. [p=0.3] {b}Na *A,* [p=0.1] ela está "
        "uma casa acima: [p=0.1] zê de três a quatro. [p=0.1] É quem troca o três com o quatro. [p=0.3] {c}Na *B,* "
        "[p=0.1] o ípsilon vai só de quatro a cinco. [p=0.3] {d}Na *C* e na *D,* [p=0.1] de cinco a seis. [p=0.2] Falta uma "
        "casa. [p=0.3] {e}Só na *E* a sombra está em ípsilon de seis a sete [p=0.1] e zê de dois a três."),
    dict(id="09", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}Depois de tudo isso, [p=0.1] o cubo se *afasta dois* do plano xis ípsilon. [p=0.3] "
        "{c}Em que altura fica a sombra dele na parede do fundo? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="10", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}A distância até um plano [p=0.1] é a coordenada que falta no nome dele. "
        "[p=0.2] {c}Aproximar diminui, [p=0.1] afastar aumenta. [p=0.2] {d}E a projeção num plano [p=0.1] guarda só "
        "as duas coordenadas do nome."),
    dict(id="11", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*coordenadas no espaço,* [p=0.2] {c}*projeção ortogonal* [p=0.2] {d}e *vistas de sólidos.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
