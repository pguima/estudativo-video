# Estudativo · Questão 008 — ENEM 2025, 2º dia, caderno amarelo, questão 137: 10 L de solução com 99,95% de S1;
# retira-se S1 até S1 ser 99,90% da nova solução. Quanto S1 sai? → 5 L (alternativa E). Enunciado: enunciado/questao.png.
# Aula horizontal 1920x1080 (~5 min), explicada passo a passo.
# Caminho: PORCENTAGEM (de cada cem, % de uma quantidade, % com vírgula) → complemento (S2 = 0,05% → 0,10%) →
# a pegadinha (subtrair as % → 0,005 L, alternativa A: totais diferentes) → o que não muda: S2 = 0,005 L →
# nova solução: 0,001·T = 0,005 → T = 5 L → retirada 10 − 5 = 5 L (E) → por quê (a % de S2 dobrou, o total cai à metade)
# + conferência (4,995/5 = 99,90%) → paradoxo da batata + desafio (99,80%) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: quanto de S1 sai da solução? (a resposta é metade do recipiente!)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. 'S um' e 'S dois' são os nomes "
            "das substâncias (leia 'ésse um' e 'ésse dois'). Faça as perguntas com curiosidade genuína, mostre surpresa "
            "na resposta e comemore o resultado. Respeite as pausas entre as frases. Leia apenas o texto, exatamente "
            "como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e trinta e sete do ENEM dois mil e vinte e cinco. [p=0.2] Um recipiente tem *dez litros* de "
        "uma solução, [p=0.1] feita só de duas substâncias: [p=0.1] *S um* e *S dois.* [p=0.3] {b}No começo, [p=0.1] "
        "noventa e nove vírgula noventa e cinco por cento da solução é de S um. [p=0.3] {c}Vamos retirar um pouco de "
        "S um, [p=0.1] até que ele seja noventa e nove vírgula noventa por cento da nova solução. [p=0.3] {d}Quanto de "
        "S um sai? [p=0.3] Parece que é só uma gotinha... [p=0.3] {e}mas a resposta vai te surpreender. [p=0.3] Nessa "
        "aula, você vai entender tudo, passo a passo, [p=0.1] usando *porcentagem* [p=0.1] e uma ideia muito "
        "poderosa: [p=0.1] olhar para *o que não muda.*"),
    dict(id="02", block="porcentagem", text=
        "{a}Primeiro, a ferramenta: [p=0.1] *porcentagem.* [p=0.2] Por cento quer dizer *de cada cem.* [p=0.3] "
        "{b}Vinte por cento é vinte em cada cem, [p=0.1] ou seja, *vinte sobre cem.* [p=0.3] {c}Para calcular a "
        "porcentagem de uma quantidade, [p=0.1] a gente multiplica. [p=0.2] Vinte por cento de cinquenta [p=0.1] é vinte "
        "sobre cem, vezes cinquenta, [p=0.1] que dá *dez.* [p=0.3] {d}E a porcentagem pode ter vírgula. [p=0.2] Zero "
        "vírgula zero cinco por cento [p=0.1] é zero vírgula zero cinco sobre cem, [p=0.1] que dá *zero vírgula zero "
        "zero zero cinco.* [p=0.2] Um número bem pequeno."),
    dict(id="03", block="complemento", text=
        "{a}Agora, um detalhe que o enunciado entrega: [p=0.1] a solução tem *só* S um e S dois. [p=0.3] {b}Então as "
        "duas porcentagens somam *cem por cento.* [p=0.3] {c}Se S um é noventa e nove vírgula noventa e cinco por "
        "cento, [p=0.1] S dois é o que falta: [p=0.1] *zero vírgula zero cinco por cento.* [p=0.3] {d}E depois da "
        "retirada, [p=0.1] com S um em noventa e nove vírgula noventa, [p=0.1] S dois passa a ser *zero vírgula dez por "
        "cento.*"),
    dict(id="04", block="pegadinha", text=
        "{a}Aqui mora a *pegadinha.* [p=0.2] É tentador fazer assim: [p=0.1] noventa e nove vírgula noventa e cinco, "
        "menos noventa e nove vírgula noventa, [p=0.1] dá zero vírgula zero cinco por cento. [p=0.3] {b}E zero vírgula "
        "zero cinco por cento de dez litros [p=0.1] dá zero vírgula zero zero cinco litro. [p=0.2] Alternativa A. "
        "[p=0.3] {c}Só que isso está *errado.* [p=0.2] As duas porcentagens são de *totais diferentes:* [p=0.1] uma é "
        "dos dez litros, [p=0.1] a outra é da solução nova, [p=0.1] que ficou menor. [p=0.3] {d}Não dá para subtrair "
        "porcentagens de totais diferentes."),
    dict(id="05", block="naomuda", text=
        "{a}Então, qual é o caminho? [p=0.2] Olhar para o que *não muda.* [p=0.3] {b}A gente só tira S um. [p=0.2] A "
        "quantidade de S dois *fica igual,* [p=0.1] do começo ao fim. [p=0.3] {c}Passo um: [p=0.1] calcular quanto "
        "S dois existe. [p=0.2] Zero vírgula zero cinco por cento de dez litros [p=0.1] é zero vírgula zero zero zero "
        "cinco, vezes dez, [p=0.1] que dá *zero vírgula zero zero cinco litro.* [p=0.3] {d}Isso é *cinco mililitros:* "
        "[p=0.1] mais ou menos uma colher de chá, [p=0.1] dentro de dez litros."),
    dict(id="06", block="novototal", text=
        "{a}Passo dois: [p=0.1] a nova solução. [p=0.2] Vamos chamar o total da nova solução de *T.* [p=0.3] {b}Nela, "
        "S dois é zero vírgula dez por cento do total, [p=0.1] e continua sendo zero vírgula zero zero cinco litro. "
        "[p=0.3] {c}Zero vírgula dez por cento é zero vírgula zero zero um. [p=0.2] Então: [p=0.1] *zero vírgula zero "
        "zero um vezes T [p=0.1] é igual a zero vírgula zero zero cinco.* [p=0.3] {d}Para deixar o T sozinho, [p=0.1] "
        "dividimos os dois lados por zero vírgula zero zero um. [p=0.3] {e}E zero vírgula zero zero cinco dividido por "
        "zero vírgula zero zero um [p=0.1] é o mesmo que cinco dividido por um. [p=0.2] *T é igual a cinco litros.*"),
    dict(id="07", block="retirada", text=
        "{a}Passo três: [p=0.1] a retirada. [p=0.2] Tínhamos dez litros, [p=0.1] ficamos com cinco. [p=0.3] {b}Saíram "
        "*cinco litros* de S um. [p=0.2] *Metade* do recipiente! [p=0.3] {c}Alternativa *E.*"),
    dict(id="08", block="porque", text=
        "{a}Mas por que tanto? [p=0.2] Repare na porcentagem de S dois: [p=0.1] ela foi de zero vírgula zero cinco "
        "[p=0.1] para zero vírgula dez. [p=0.2] *Dobrou.* [p=0.3] {b}Só que a quantidade de S dois não mudou. [p=0.2] "
        "Para a mesma quantidade valer o dobro da porcentagem, [p=0.1] o total tem que *cair pela metade.* [p=0.3] "
        "{c}Vamos conferir. [p=0.2] S um tinha nove vírgula nove nove cinco litros, [p=0.1] perdeu cinco, [p=0.1] e "
        "ficou com *quatro vírgula nove nove cinco.* [p=0.3] {d}Quatro vírgula nove nove cinco dividido por cinco "
        "[p=0.1] dá zero vírgula nove nove nove, [p=0.1] ou seja, *noventa e nove vírgula noventa por cento.* [p=0.2] "
        "Confere!"),
    dict(id="09", block="batata", text=
        "{a}Esse problema tem um primo famoso: [p=0.1] o *paradoxo da batata.* [p=0.2] Cem quilos de batata, [p=0.1] "
        "com noventa e nove por cento de água. [p=0.3] {b}Elas secam um pouco, [p=0.1] até a água ser noventa e oito "
        "por cento. [p=0.2] Quanto pesam agora? [p=0.3] {c}A parte seca era um por cento, [p=0.1] um quilo, [p=0.1] e "
        "virou dois por cento. [p=0.2] Dobrou! [p=0.2] Então o peso cai pela metade: [p=0.1] *cinquenta quilos.* "
        "[p=0.3] {d}Agora é com você: [p=0.1] e se, na nossa questão, [p=0.1] S um tivesse que ficar em *noventa e nove "
        "vírgula oitenta por cento?* [p=0.2] Quantos litros sairiam? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="10", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, achamos a porcentagem de S dois, [p=0.1] pelo que falta "
        "para cem. [p=0.2] {c}Depois, calculamos quanto S dois existe, [p=0.1] a quantidade que não muda. [p=0.2] {d}Em "
        "seguida, usamos esse valor na nova porcentagem [p=0.1] e achamos o novo total: [p=0.1] cinco litros. [p=0.2] "
        "{e}E a retirada é a diferença: [p=0.1] cinco litros."),
    dict(id="11", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*porcentagem,* [p=0.2] {c}*razão e proporção* [p=0.2] {d}e *equação do primeiro grau.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
