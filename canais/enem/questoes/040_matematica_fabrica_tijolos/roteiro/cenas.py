# Estudativo · Questão 040 — ENEM 2025, 2º dia, caderno amarelo, questão 152: uma fábrica de tijolos ecológicos com
# 3 funcionários, 6 horas por dia cada, produz 720 tijolos por dia. Passa a ter 5 funcionários, 9 horas cada; todos
# produzem a mesma quantidade por hora. Quantos tijolos por dia depois do aumento?
# Horas de trabalho por dia: antes 3 × 6 = 18; agora 5 × 9 = 45. Por hora de trabalho: 720 ÷ 18 = 40 tijolos.
# Agora: 45 × 40 = 1 800 → D. Conferência: 720 × 5/3 × 3/2 = 1 800.
# Pegadinhas: C (1 200 = só os funcionários: 720 × 5/3), B (1 080 = só as horas: 720 × 9/6), E (2 520 = 720 + 1 800,
# somou a produção antiga). A (800) não sai de conta certa.
# Figura: a grade "funcionários × horas" (cada quadradinho = 1 funcionário trabalhando 1 hora = 40 tijolos).
# Enunciado: enunciado/questao.png. Aula horizontal 1920x1080, explicada passo a passo.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: a fábrica de tijolos (proporcionalidade)"

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
        "{a}Questão cento e cinquenta e dois do ENEM dois mil e vinte e cinco. [p=0.2] Uma fábrica de tijolos "
        "ecológicos tem *três funcionários,* [p=0.1] cada um trabalhando *seis horas* por dia, [p=0.1] e produz "
        "*setecentos e vinte* tijolos por dia. [p=0.3] {b}Depois, a fábrica passou a ter *cinco funcionários,* "
        "[p=0.1] cada um trabalhando *nove horas.* [p=0.3] {c}Todos produzem a mesma quantidade por hora. [p=0.2] "
        "{d}Quantos tijolos a fábrica faz por dia agora? [p=0.3] {e}Nessa aula, [p=0.1] você vai usar a "
        "*proporcionalidade* [p=0.1] e a produção *por hora de trabalho.*"),
    dict(id="02", block="proporcao", text=
        "{a}Ferramenta um: [p=0.1] grandezas proporcionais. [p=0.3] {b}Se cada funcionário faz a mesma quantidade "
        "por hora, [p=0.1] {c}dobrar o número de funcionários [p=0.1] *dobra* a produção. [p=0.3] {d}E dobrar as "
        "horas [p=0.1] também *dobra* a produção. [p=0.3] {e}A produção é proporcional às duas coisas ao mesmo "
        "tempo."),
    dict(id="03", block="horas", text=
        "{a}Ferramenta dois: [p=0.1] a hora de trabalho. [p=0.3] {b}Cada quadradinho aqui é *um funcionário* "
        "[p=0.1] trabalhando *uma hora.* [p=0.3] {c}Antes, eram três funcionários, [p=0.1] seis horas cada: [p=0.1] "
        "três vezes seis, [p=0.1] *dezoito horas de trabalho* por dia."),
    dict(id="04", block="passo1", text=
        "{a}Passo um: [p=0.1] quanto sai de cada hora de trabalho. [p=0.3] {b}Setecentos e vinte tijolos [p=0.1] em "
        "dezoito horas de trabalho. [p=0.3] {c}Setecentos e vinte dividido por dezoito: [p=0.1] *quarenta.* [p=0.3] "
        "{d}Cada quadradinho vale *quarenta tijolos.*"),
    dict(id="05", block="passo2", text=
        "{a}Passo dois: [p=0.1] as horas de trabalho depois do aumento. [p=0.3] {b}Cinco funcionários, [p=0.1] nove "
        "horas cada: [p=0.1] {c}cinco vezes nove, [p=0.1] *quarenta e cinco horas de trabalho* por dia."),
    dict(id="06", block="passo3", text=
        "{a}Passo três: [p=0.1] a produção nova. [p=0.3] {b}Quarenta e cinco quadradinhos, [p=0.1] cada um com "
        "quarenta tijolos. [p=0.3] {c}Quarenta e cinco vezes quarenta: [p=0.1] *mil e oitocentos* tijolos por dia!"),
    dict(id="07", block="confere", text=
        "{a}Vamos conferir de outro jeito. [p=0.3] {b}Os funcionários foram de três para cinco: [p=0.1] a produção "
        "é multiplicada por *cinco terços.* [p=0.3] {c}As horas foram de seis para nove: [p=0.1] multiplica de novo, "
        "[p=0.1] por *três meios.* [p=0.3] "
        "{d}Setecentos e vinte, [p=0.1] vezes cinco terços, [p=0.1] dá mil e duzentos. [p=0.2] {e}Vezes três meios: "
        "[p=0.1] *mil e oitocentos.* [p=0.2] Bateu!"),
    dict(id="08", block="resposta", text=
        "{a}Depois do aumento, a fábrica faz *mil e oitocentos* tijolos por dia. [p=0.3] {b}Alternativa *D.*"),
    dict(id="09", block="pegadinhas", text=
        "{a}E as outras? [p=0.3] {b}A *C,* [p=0.1] mil e duzentos, [p=0.1] só aumenta os *funcionários* [p=0.1] e "
        "esquece as horas. [p=0.3] {c}A *B,* [p=0.1] mil e oitenta, [p=0.1] só aumenta as *horas* [p=0.1] e esquece "
        "os funcionários. [p=0.3] {d}A *E,* [p=0.1] dois mil quinhentos e vinte, [p=0.1] *soma* a produção antiga "
        "com a nova. [p=0.3] {e}E a *A* [p=0.1] não sai de nenhuma conta certa."),
    dict(id="10", block="desafio", text=
        "{a}Agora é com você. [p=0.2] {b}E se a fábrica tivesse *quatro funcionários,* [p=0.1] trabalhando *oito "
        "horas* cada? [p=0.3] {c}Quantos tijolos sairiam por dia? [p=0.3] {d}Deixe sua resposta nos comentários."),
    dict(id="11", block="resumo", text=
        "{a}Vamos recapitular. [p=0.2] {b}Multiplique funcionários por horas. [p=0.2] {c}Divida a produção pelas "
        "horas de trabalho [p=0.1] para achar quanto sai de cada uma. [p=0.2] {d}E multiplique pelas horas de "
        "trabalho novas."),
    dict(id="12", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*razão e proporção,* [p=0.2] {c}*grandezas proporcionais* [p=0.2] {d}e *regra de três composta.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
