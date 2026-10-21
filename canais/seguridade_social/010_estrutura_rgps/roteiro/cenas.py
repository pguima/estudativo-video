# Roteiro — Seguridade Social 010: A estrutura do RGPS — segurados e dependentes (Módulo M07)
# Base: Estudos/Seguridade Social/modulos/M07-rgps-estrutura-e-beneficiarios.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "A estrutura do RGPS: segurados, dependentes e prestações (Lei 8.213, arts. 10, 11 e 18)"

# Estilo da voz (gerar_voz_local.py): mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa"],
    prompt=("Narre como um professor de cursinho apaixonado pela matéria, conversando com o aluno: "
            "voz calorosa e envolvente, bem expressiva, variando a entonação. Dê ênfase às palavras-chave, "
            "faça as perguntas com curiosidade de verdade, mostre surpresa nas pegadinhas e firmeza nas respostas "
            "('Errado!', 'Certo!'). Sorria na voz. Ritmo didático e tranquilo, sem pressa, respeitando as pausas."),
)

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Começa agora a *temporada dois!* [p=0.4] E ela começa com uma ideia simples. [p=0.3] {a}No RGPS, [p=0.2] "
        "só existem *dois tipos* de gente: [p=0.4] {b}quem *contribui,* [p=0.3] {c}e quem *depende* de quem contribui. [p=0.5] "
        "{d}Hoje você vai ver o *mapa* do RGPS inteiro: [p=0.2] quem está dentro, [p=0.2] e o que ele entrega."),

    # ================= O QUE É =================
    dict(id="02", block="rgps", text=
        "{t}Primeiro: [p=0.2] o que é o RGPS? [p=0.4] É o regime de quem trabalha na *iniciativa privada,* [p=0.2] "
        "e de todo mundo que *não* tem regime próprio. [p=0.4] {a}Quem gere é o *INSS.* [p=0.3] {b}A filiação é *obrigatória.* "
        "[p=0.3] {c}O custeio é *contributivo.* [p=0.3] {d}E o regime é de *repartição simples:* [p=0.2] "
        "não existe poupança individual. [p=0.3] Quem trabalha hoje paga quem está aposentado hoje."),
    dict(id="03", block="normas", text=
        "{t}E agora, um par de leis que a banca *adora* trocar. [p=0.4] {a}A Lei oito mil, duzentos e *doze* é o *custeio:* "
        "[p=0.2] o dinheiro *entrando.* [p=0.4] {b}A Lei oito mil, duzentos e *treze* trata dos *benefícios:* [p=0.2] "
        "o dinheiro *saindo.* [p=0.5] {c}O macete é lindo: [p=0.2] o *dois* vem antes, [p=0.2] porque primeiro se *paga.* "
        "[p=0.3] {d}O *três* vem depois, [p=0.2] porque depois se *recebe.* [p=0.4] {e}E o Decreto três mil e quarenta e oito "
        "regulamenta as duas."),

    # ================= BENEFICIÁRIOS =================
    dict(id="04", block="binaria", text=
        "{t}Então, quem são os *beneficiários* do RGPS? [p=0.4] {a}O artigo *dez* da Lei oito mil, duzentos e treze responde: "
        "[p=0.3] {b}*segurados* [p=0.3] {c}e *dependentes.* [p=0.5] {d}Só isso! [p=0.3] A divisão é *binária.* "
        "[p=0.2] Não existe uma terceira categoria."),
    dict(id="05", block="pensionista", text=
        "{t}E é aqui que a banca arma a primeira pegadinha. [p=0.4] {a}São beneficiários do RGPS os segurados, os dependentes "
        "[p=0.2] *e os pensionistas.* [p=0.5] {r}*Errado!* [p=0.3] {b}O pensionista é só um *dependente* [p=0.2] "
        "que já está recebendo pensão. [p=0.3] {c}Pensionista e aposentado são *situações,* [p=0.2] e não categorias."),

    # ================= SEGURADOS =================
    dict(id="06", block="obrigatorios", text=
        "{t}Agora, os *segurados obrigatórios,* [p=0.2] no artigo *onze.* [p=0.3] São *cinco.* [p=0.4] "
        "{s1}O *empregado.* [p=0.3] {s2}O *empregado doméstico.* [p=0.3] {s3}O *contribuinte individual.* [p=0.3] "
        "{s4}O *trabalhador avulso.* [p=0.3] {s5}E o *segurado especial.* [p=0.5] {m}Para decorar: [p=0.2] *E, E, C, T, S.*"),
    dict(id="07", block="revogados", text=
        "{t}Mas repare numa coisa curiosa. [p=0.3] {a}Os incisos são *um, dois, cinco, seis e sete.* [p=0.4] "
        "{b}Cadê o *três* e o *quatro?* [p=0.5] {c}Foram *revogados* em mil novecentos e noventa e nove. [p=0.3] "
        "{d}O *empresário* e o *autônomo* [p=0.2] {e}viraram, os dois, *contribuinte individual.* [p=0.4] "
        "{f}Então, se a questão listar empresário ou autônomo como categoria de segurado, [p=0.2] *errado!*"),
    dict(id="08", block="facultativo", text=
        "{t}E existe um *sexto* segurado. [p=0.3] {a}O *facultativo,* [p=0.2] no artigo *treze.* [p=0.4] "
        "{b}Ele não está no artigo onze, [p=0.2] porque *não* é obrigatório: [p=0.2] ele entra *porque quer.* [p=0.5] "
        "{c}Então, quantas categorias de segurado existem? [p=0.3] {d}*Seis:* [p=0.2] cinco obrigatórios [p=0.2] e um facultativo."),

    # ================= PRESTAÇÕES =================
    dict(id="09", block="art18", text=
        "{t}E o que o RGPS entrega? [p=0.3] Está no artigo *dezoito.* [p=0.4] {a}São as *prestações,* [p=0.2] "
        "e elas se dividem em *benefícios,* [p=0.2] que são pagos em *dinheiro,* [p=0.3] {b}e *serviços.* [p=0.5] "
        "{c}E guarde esta expressão do artigo: [p=0.2] *inclusive* em razão de *acidente do trabalho.* [p=0.3] "
        "O RGPS cobre o acidente, [p=0.2] sim!"),
    dict(id="10", block="segurado", text=
        "{t}Do lado do *segurado,* [p=0.2] a lista é grande. [p=0.4] {a}As *aposentadorias.* [p=0.3] "
        "{b}O auxílio por *incapacidade temporária.* [p=0.3] {c}O *salário-família.* [p=0.3] {d}O *salário-maternidade.* "
        "[p=0.3] {e}E o *auxílio-acidente.*"),
    dict(id="11", block="dependente", text=
        "{t}Mas do lado do *dependente,* [p=0.2] são só *dois* benefícios. [p=0.4] {a}A *pensão por morte* [p=0.3] "
        "{b}e o *auxílio-reclusão.* [p=0.5] {m}Para decorar: [p=0.2] *P, A.* [p=0.4] {x}E olha a pegadinha: [p=0.2] "
        "o auxílio-reclusão é devido ao segurado preso? [p=0.4] {r}*Não!* [p=0.3] É devido aos *dependentes* dele."),
    dict(id="12", block="servicos", text=
        "{t}E os *serviços?* [p=0.3] Esses servem aos *dois:* [p=0.2] segurados e dependentes. [p=0.4] E são só *dois.* "
        "[p=0.3] {a}O *serviço social* [p=0.3] {b}e a *reabilitação profissional.* [p=0.5] {c}Perícia médica *não* é serviço. "
        "[p=0.3] Não caia nessa!"),
    dict(id="13", block="nomes", text=
        "{t}E atenção aos *nomes,* [p=0.2] porque a reforma de dois mil e dezenove mudou vários. [p=0.4] "
        "{a}O antigo *auxílio-doença* [p=0.2] virou auxílio por *incapacidade temporária.* [p=0.4] "
        "{b}A antiga aposentadoria por *invalidez* [p=0.2] virou aposentadoria por *incapacidade permanente.* [p=0.4] "
        "{c}E a aposentadoria por *tempo de contribuição* [p=0.2] só sobrevive nas *regras de transição* [p=0.2] "
        "e no direito adquirido. [p=0.4] {d}A banca pode usar o nome antigo *ou* o novo."),

    # ================= PEGADINHAS =================
    dict(id="14", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}O RGPS possui *cinco* categorias de segurado. [p=0.4] "
        "{r1}*Errado:* [p=0.2] são *seis,* [p=0.2] contando o facultativo. [p=0.5] {p2}A pensão por morte é devida ao *segurado.* "
        "[p=0.4] {r2}*Errado:* [p=0.2] é dos *dependentes.* [p=0.5] {p3}As prestações são devidas *inclusive* em razão de "
        "acidente do trabalho. [p=0.4] {r3}*Certo!*"),
    dict(id="15", block="q_lei", text=
        "{t}E uma questão de prova: [p=0.3] {e}a Lei oito mil, duzentos e *doze* dispõe sobre os *planos de benefícios* "
        "da previdência social. [p=0.6] {r}*Errado!* [p=0.3] {x}Doze é o *custeio.* [p=0.2] Os benefícios estão na *treze.*"),

    # ================= FECHAMENTO =================
    dict(id="16", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}RGPS: [p=0.2] INSS, obrigatório, contributivo e de repartição simples. [p=0.3] "
        "{b}Doze é custeio, [p=0.2] treze é benefício. [p=0.3] {c}Beneficiários: [p=0.2] só *segurados* e *dependentes.* "
        "[p=0.3] {d}Obrigatórios: [p=0.2] *E, E, C, T, S,* [p=0.2] mais o facultativo: [p=0.2] *seis.* [p=0.3] "
        "{e}Só do dependente: [p=0.2] *P, A.* [p=0.3] {f}E serviços, [p=0.2] só *dois.*"),
    dict(id="17", block="cta", text=
        "Na próxima aula, [p=0.2] vamos abrir o primeiro grupo: [p=0.2] o *empregado,* [p=0.2] o *doméstico* [p=0.2] e o *avulso.* "
        "[p=0.4] {pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* "
        "de Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que os incisos três e quatro foram revogados? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
