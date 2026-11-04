# Roteiro — Redação ENEM, Introdução, Episódio 3 de 7: A ponte — como ligar a referência ao recorte (e o teste da retirada)
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seção 04 + Questões 7 e 3 da seção 12 (nesta ordem).
#   Prompt do usuário: _material/prompts_02-introducao.md, "Vídeo 3". Critérios do repertório (legitimado, pertinente,
#   produtivo) só citados: terão série própria (Repertório sociocultural).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias: a PONTE é a RUA DE ACESSO (leva do mapa geral até a porta do endereço) · repertório de bolso = CARTÃO-POSTAL
#   GENÉRICO (serve para qualquer cidade e não leva a nenhuma casa) · TESTE DA RETIRADA ("se a referência sai e nada muda,
#   ela não estava trabalhando"). A peça RUA DE ACESSO entra na etiqueta da série neste episódio.
# Lidos EXATAMENTE como no material: a citação da Cartilha de 2026 sobre A República, de Platão (cena 06), os trechos
#   "sem ponte" e "com ponte" (cenas 07–09, com o aviso "Trechos elaborados para fins didáticos" na tela), a fórmula de
#   ponte e as expressões de passagem (cenas 10–11), as alternativas das Questões 7 e 3.
# Platão e Aristóteles NÃO são proibidos (cena 12 e Questão 3): o problema é o encaixe genérico.
# Exercício "nós fazemos" (cena 13) = a referência da Questão 7 (Lei nº 9.534/1997); a Questão 7 (cenas 18–20) confere o exercício.
# Gabaritos: Questão 7 = E · Questão 3 = E.
# Cores: azul = definição · verde = método (a ponte) · amarelo = armadilha (bolso) · vermelho = erro · roxo = regra oficial.

TITULO = "Sua Citação de Filósofo Pode Ser Apagada? O Teste da Retirada | Introdução da Redação Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Nesta aula, o aluno descobre um truque para testar se a "
            "citação dele está trabalhando: crie suspense antes de cada teste, mostre surpresa quando a frase "
            "desmorona e comemore quando a ponte funciona. Ritmo didático e tranquilo, sem pressa, respeitando as "
            "pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem "
            "repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Muita gente decora uma frase de filósofo [p=0.2] e cola no começo de *toda* redação. [p=0.4] {b}A Cartilha do "
        "ENEM tem um nome para isso. [p=0.3] {c}E não é elogio."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai escrever a frase que faz *qualquer* referência trabalhar a favor do seu "
        "tema, [p=0.3] {b}e vai saber *testar* se ela está trabalhando."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago. [p=0.3] {a}A introdução é a *etiqueta completa da encomenda.* [p=0.3] "
        "{b}No episódio passado, a gente viu o *mapa:* [p=0.2] a contextualização, [p=0.2] com quatro portas de entrada: "
        "[p=0.2] {c}lei ou obra, [p=0.2] fato histórico, [p=0.2] dado [p=0.2] e conceito. [p=0.4] {d}Hoje, a etiqueta ganha "
        "uma peça nova: [p=0.2] a *rua de acesso.*"),

    # ================= CARTÃO-POSTAL × RUA =================
    dict(id="04", block="postal", text=
        "{t}Imagine que você vai visitar um amigo. [p=0.3] {a}Ele te manda um *cartão-postal* com uma foto linda de uma "
        "cidade. [p=0.3] {b}Bonito, [p=0.2] mas essa foto serviria para qualquer cidade, [p=0.2] e não te leva a casa "
        "nenhuma. [p=0.4] {c}Agora ele te manda um *mapa,* [p=0.2] com a rua que sai da avenida principal [p=0.2] e chega "
        "na porta dele. [p=0.4] {d}Esse segundo você usa de verdade."),
    dict(id="05", block="postal", text=
        "{a}Na redação é igual. [p=0.3] {b}O *recorte* é o tema exato da prova: [p=0.2] o endereço completo. [p=0.4] "
        "{c}*Repertório de bolso* é o cartão-postal genérico: [p=0.2] uma referência decorada que serve para qualquer tema "
        "[p=0.2] e não leva a nenhuma casa. [p=0.4] {d}E a *ponte* é a rua de acesso: [p=0.2] a frase que leva do mapa geral "
        "até a porta do endereço."),

    # ================= O ERRO MAIS COMUM =================
    dict(id="06", block="cartilha", text=
        "{t}E qual é o erro mais comum na contextualização? [p=0.3] {a}Não é a referência em si. [p=0.3] {b}É a falta de "
        "ligação com o tema. [p=0.5] {c}A Cartilha de dois mil e vinte e seis comenta um exemplo: [p=0.2] uma menção à *A "
        "República,* de Platão, [p=0.2] {d}que, nas palavras da Cartilha, [p=0.2] poderia ser retirada da introdução sem "
        "alterar significativamente a compreensão do texto. [p=0.5] {e}Daí sai o nosso teste. [p=0.3] {f}O *teste da "
        "retirada:* [p=0.2] se a referência sai e nada muda, [p=0.2] ela não estava trabalhando."),

    # ================= EU FAÇO: SEM PONTE =================
    dict(id="07", block="sem", text=
        "{t}Vamos aplicar o teste ao vivo. [p=0.3] {a}Tema de dois mil e vinte e quatro: [p=0.2] Desafios para a valorização "
        "da herança africana no Brasil. [p=0.4] {b}Primeiro trecho: [p=0.3] {c}A Constituição Federal de mil novecentos e "
        "oitenta e oito é conhecida como Constituição Cidadã. [p=0.3] {d}Nesse sentido, a herança africana é muito "
        "importante para o Brasil. [p=0.6] {e}Agora eu tiro a referência. [p=0.4] {f}Risco a primeira frase [p=0.2] e leio "
        "de novo: [p=0.3] {g}a herança africana é muito importante para o Brasil. [p=0.4] {h}Mudou alguma coisa? [p=0.3] "
        "*Nada.* [p=0.3] A segunda frase não dependia da primeira. [p=0.3] {i}A Constituição era só um *rótulo.*"),

    # ================= EU FAÇO: COM PONTE =================
    dict(id="08", block="com", text=
        "{b}Segundo trecho: [p=0.3] {c}A Constituição Federal de mil novecentos e oitenta e oito reconhece como patrimônio "
        "cultural brasileiro os bens que guardam a memória dos diferentes grupos formadores da sociedade. [p=0.4] {d}Entre "
        "esses grupos, porém, os povos africanos e seus descendentes ainda veem sua contribuição tratada como folclore ou "
        "restrita a datas comemorativas, [p=0.2] o que revela a distância entre o reconhecimento legal e a valorização "
        "efetiva."),
    dict(id="09", block="com", text=
        "{e}Teste da retirada de novo. [p=0.3] {f}Tiro a Constituição. [p=0.4] {g}E agora? [p=0.2] Entre *esses* grupos? "
        "[p=0.2] Que grupos? [p=0.3] Reconhecimento legal? [p=0.2] Qual lei? [p=0.4] {h}A frase *desmorona.* [p=0.4] {i}Aqui "
        "a referência trabalha: [p=0.2] a Constituição foi *interpretada,* [p=0.2] o que ela reconhece, [p=0.3] {j}e "
        "*confrontada* com a realidade, [p=0.2] como a herança africana é tratada. [p=0.4] {k}E esse *contraste,* [p=0.2] a "
        "diferença entre o que a lei diz e o que acontece, [p=0.2] já prepara a tese."),

    # ================= A FÓRMULA DA PONTE =================
    dict(id="10", block="formula", text=
        "{t}Dá para transformar isso numa fórmula. [p=0.3] {m}É um método de estudo, [p=0.2] não uma regra do Inep. [p=0.4] "
        "{a}Primeiro, a *referência.* [p=0.3] {b}Depois, *o que ela mostra.* [p=0.3] {c}E, por fim, *como isso se relaciona "
        "com o recorte.* [p=0.5] {d}No nosso trecho: [p=0.2] a Constituição, [p=0.2] {e}reconhece a memória dos grupos "
        "formadores, [p=0.3] {f}mas a herança africana ainda é tratada como folclore."),
    dict(id="11", block="expressoes", text=
        "{t}E como a gente marca essa passagem? [p=0.3] {a}Com um *conectivo:* [p=0.2] a palavrinha que liga uma ideia à "
        "outra. [p=0.4] {b}Para ligar o contexto ao problema, [p=0.2] estas costumam funcionar: [p=0.3] {c}de modo "
        "semelhante, [p=0.3] {d}essa realidade, no entanto, [p=0.3] {e}tal cenário se repete, [p=0.3] {f}ao contrário do que "
        "prevê a lei. [p=0.5] {g}A série de Conectivos vai aprofundar isso."),
    dict(id="12", block="filosofo", text=
        "{t}Então, [p=0.2] está proibido citar Platão? [p=0.2] Aristóteles? [p=0.4] {a}*Não!* [p=0.3] {b}Nenhum autor é "
        "proibido. [p=0.3] {c}O problema é o *encaixe genérico:* [p=0.2] a citação que serviria para qualquer tema. [p=0.4] "
        "{d}Se você constrói a rua até o recorte, [p=0.2] qualquer referência legítima pode trabalhar. [p=0.3] {e}Os "
        "critérios do bom repertório ficam para a série de Repertório sociocultural."),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="nos", text=
        "{t}Agora é você. [p=0.3] {a}Tema de dois mil e vinte e um: [p=0.2] Invisibilidade e registro civil: garantia de "
        "acesso à cidadania no Brasil. [p=0.4] {b}A referência: [p=0.2] A Lei nove mil quinhentos e trinta e quatro, de mil "
        "novecentos e noventa e sete, tornou gratuitos o registro civil de nascimento e a primeira certidão. [p=0.5] {c}Pause "
        "e escreva *você mesmo* a frase seguinte, [p=0.2] contrapondo a lei à realidade. [p=0.3] {p}Pause! [p=2.0] {d}Guarde a sua frase: [p=0.2] daqui a pouco, [p=0.2] uma questão confere."),

    # ================= RECAPITULAÇÃO (MEIO) =================
    dict(id="14", block="recap", text=
        "{t}Agora, [p=0.2] três frases para guardar. [p=0.3] {a}A ponte é a rua: [p=0.2] leva do mapa até a porta. [p=0.5] "
        "{b}Referência, [p=0.2] o que mostra, [p=0.2] como se liga ao recorte. [p=0.5] {c}Tirou e nada mudou? [p=0.2] Não "
        "estava trabalhando."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.3] {a}Primeiro: [p=0.2] citar e *abandonar* a referência. [p=0.4] {b}Parece "
        "certo porque a citação está lá, [p=0.2] bonita, [p=0.2] e dá a impressão de repertório. [p=0.4] {c}Mas, sem a "
        "ponte, [p=0.2] ela não trabalha: [p=0.2] faça a referência mostrar algo sobre o recorte."),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] achar que o problema é o *autor clássico.* [p=0.4] {b}Parece certo porque a Cartilha criticou "
        "justamente Platão e Aristóteles. [p=0.4] {c}Mas o que ela criticou foi o *encaixe genérico,* [p=0.2] não o autor."),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] usar o conectivo sem que exista relação de verdade. [p=0.2] Nesse sentido, [p=0.2] e a frase "
        "seguinte fala de outra coisa. [p=0.4] {b}Parece certo porque o conectivo dá cara de texto ligado. [p=0.4] {c}Mas "
        "conectivo não cria ligação: [p=0.2] ele só *marca* uma ligação que precisa existir na ideia."),

    # ================= QUESTÃO 7 =================
    dict(id="18", block="q7", text=
        "{a}Questão sete. [p=0.2] Para o tema de dois mil e vinte e um, [p=0.2] um participante iniciou a introdução assim: "
        "[p=0.2] A Lei nove mil quinhentos e trinta e quatro, de mil novecentos e noventa e sete, tornou gratuitos o "
        "registro civil de nascimento e a primeira certidão. [p=0.3] A frase seguinte que melhor faz a ponte entre essa "
        "referência e o recorte do tema é: [p=0.4] {A}A: [p=0.2] Nesse sentido, as leis brasileiras são muito numerosas. "
        "[p=0.4] {B}B: [p=0.2] Além disso, o Brasil tem uma das maiores populações do mundo."),
    dict(id="19", block="q7", text=
        "{C}C: [p=0.2] Por isso, todos os brasileiros já têm acesso pleno à cidadania. [p=0.4] {D}D: [p=0.2] Dessa forma, a "
        "cidadania surgiu na Grécia Antiga. [p=0.4] {E}E: [p=0.2] Ainda assim, há brasileiros sem certidão de nascimento, "
        "[p=0.2] e, sem ela, invisíveis para o Estado e afastados de direitos básicos. [p=0.4] {p}Pause o vídeo e tente! "
        "[p=2.0]"),
    dict(id="20", block="q7", text=
        "{ok}Letra *E.* [p=0.3] {ok2}O ainda assim contrapõe a lei à realidade, [p=0.2] e liga a falta de registro à "
        "invisibilidade e ao acesso à cidadania: [p=0.2] todos os blocos do tema aparecem, [p=0.2] e a tese pode vir em "
        "seguida. [p=0.4] {xa}A A generaliza para as leis em geral. [p=0.3] {xb}A B traz uma informação sem relação com o "
        "recorte. [p=0.3] {xc}A C tira uma conclusão que a realidade do tema contradiz, [p=0.2] e eliminaria o problema a "
        "discutir. [p=0.3] {xd}E a D salta para o assunto amplo, [p=0.2] fora do Brasil. [p=0.4] {f}Se a sua frase contrapôs "
        "a lei à realidade, [p=0.2] *parabéns:* [p=0.2] você construiu a rua."),

    # ================= QUESTÃO 3 =================
    dict(id="21", block="q3", text=
        "{a}Questão três. [p=0.2] Uma introdução para o tema de dois mil e vinte e cinco começa assim: [p=0.3] Segundo "
        "Aristóteles, o ser humano é um animal político. [p=0.2] Dessa forma, o envelhecimento é uma questão relevante na "
        "sociedade brasileira. [p=0.3] Com base no que a Cartilha de dois mil e vinte e seis diz sobre repertório, [p=0.2] o "
        "principal problema desse início é que: [p=0.4] {A}A: [p=0.2] autores da Antiguidade não podem ser citados na "
        "redação do ENEM. [p=0.4] {B}B: [p=0.2] a citação deveria vir entre aspas e com o ano da obra."),
    dict(id="22", block="q3", text=
        "{C}C: [p=0.2] a referência viola os direitos humanos e zera a Competência cinco. [p=0.4] {D}D: [p=0.2] o trecho tem "
        "desvios de norma que comprometem a Competência um. [p=0.4] {E}E: [p=0.2] a referência é genérica e não se conecta ao "
        "recorte: [p=0.2] poderia ser retirada sem mudar o sentido, [p=0.2] o que caracteriza o repertório de bolso. [p=0.4] "
        "{p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="23", block="q3", text=
        "{ok}Letra *E.* [p=0.3] {ok2}Faça o teste da retirada: [p=0.2] tire Aristóteles, [p=0.2] e o envelhecimento continua "
        "uma questão relevante. [p=0.2] Nada mudou. [p=0.3] A Cartilha dá exatamente Aristóteles e Platão como exemplos de "
        "repertório de bolso nesse tema. [p=0.4] {xa}A A generaliza: [p=0.2] o problema não é o autor, [p=0.2] é o encaixe. "
        "[p=0.3] {xb}A B inventa uma exigência formal. [p=0.3] {xc}A C confunde as coisas: [p=0.2] nada ali desrespeita "
        "direitos humanos. [p=0.3] {xd}E a D não se sustenta: [p=0.2] o trecho não tem desvio gramatical relevante."),

    # ================= RECAPITULAÇÃO (FIM) =================
    dict(id="24", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}A ponte é a rua: [p=0.2] leva do mapa até a porta. "
        "[p=0.5] {b}Referência, [p=0.2] o que mostra, [p=0.2] como se liga ao recorte. [p=0.5] {c}Tirou e nada mudou? "
        "[p=0.2] Não estava trabalhando."),

    # ================= PONTE =================
    dict(id="25", block="ponte", text=
        "{a}O mapa e a rua levam até a porta. [p=0.4] {b}Agora falta o principal: [p=0.2] o que você vai *entregar,* "
        "[p=0.2] {c}e a lista do que vai na caixa. [p=0.4] {d}Próximo episódio: [p=0.2] a *tese* e a *antecipação dos "
        "eixos.*"),

    # ================= CTA =================
    dict(id="26", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi a frase-ponte que você escreveu para a lei do registro civil? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
