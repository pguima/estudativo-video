# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 5 de 7: MDC — o maior pedaço que cabe certinho (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seção 07 + Questões 2 e 6 da seção 12.
#   A Questão 9 (estacas) fica para o episódio 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: MDC é a MAIOR RÉGUA que mede todas as tábuas certinho, sem sobrar pedaço. Se a régua for maior que a
#   menor tábua, ela nem cabe nela (tábuas de 12 e 18 cm; réguas de 1, 2, 3, 4 e 6 cm — a de 4 sobra pedaço na de 18).
# Lidos EXATAMENTE como no material: definição (cena 07), regra da fatoração (08), "o 5 ficou de fora" (10),
#   regra de Euclides (13), palavras-chave (15), checagem (16), enunciados e alternativas das Questões 2 e 6.
# Erros das alternativas: Q2 E = 20 = usou 30 cm, um divisor comum que não é o maior (600 ÷ 30); as outras (6, 12, 15)
#   não saem de divisor comum nenhum. A Q2 NÃO tem a alternativa de quem parou no MDC (60 não está entre as opções).
#   Q6 C = 12 = parou no MDC (material); A = 4 = contou só os meninos; D = 14 = 6 grupos (8 + 6); E = 21 = 4 grupos (12 + 9).
# Exercício "nós fazemos" (cena 11): MDC(30, 45) = 15 pelo varal (inédito; não usa os números das questões).
# REFORMULAÇÃO 2026-10-22 (pedido do usuário): o ATALHO PRINCIPAL é o varal com todos os números juntos (decomposição
#   simultânea): só se MARCAM os primos que dividem todos ao mesmo tempo; MDC = produto dos marcados (cenas 10b–10d).
#   72, 120 │2 ✓ │2 ✓ │2 ✓ │3 ✓ → 3, 5 │3 → 1, 5 │5 → 1, 1: marcados 2·2·2·3 = 24 (MDC); todos = 360 (MMC do ep. 4).
#   Macete das questões: o que sobra no fim do varal (só MDC) = quantas vezes o MDC cabe em cada número
#   (Q2: 2, 3, 5 → 10 pedaços; Q6: 4 meninos e 3 meninas). A fatoração separada (cenas 08–10) fica como o "porquê".
#   Versão anterior em roteiro/_v1/.
# Frases-chave (meio e fim, idênticas):
#   1. Repartir em pedaços iguais, o maior possível: MDC.
#   2. No varal, só entram os primos que dividem todos.
#   3. Achou o MDC? Agora responda o que foi perguntado.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "MDC: o maior pedaço que cabe certinho — Matemática ENEM, Divisibilidade episódio 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Nas contas, fale devagar e com clareza, como quem raciocina junto com o aluno. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "MMC": "M M C",
    "MDC": "M D C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Você calcula o MDC certinho [p=0.2] e ainda *erra* a questão. [p=0.5] {b}Isso acontece porque o ENEM quase nunca "
        "pergunta o MDC: [p=0.3] {c}pergunta *quantos pedaços* [p=0.2] ou *quantas pessoas.* [p=0.4] {d}Hoje você aprende os "
        "*dois passos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular o MDC [p=0.4] {b}e dar o *passo final* [p=0.2] que a questão "
        "realmente pede."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembranças rápidas. [p=0.3] {a}*Divisor* é quem divide certinho, [p=0.2] sem sobrar bala. [p=0.4] "
        "{b}*Fatorar* é achar a receita do número: [p=0.2] quais primos, os tijolos, e quantos de cada. [p=0.4] {c}E o "
        "*MMC* é o reencontro: [p=0.2] coisas que se repetem e voltam a coincidir. [p=0.3] {d}Hoje é o contrário: [p=0.2] "
        "em vez de repetir, [p=0.2] a gente vai *repartir.*"),

    # ================= BLOCO A: A RÉGUA =================
    dict(id="04", block="regua", text=
        "{t}Imagine um marceneiro, [p=0.2] o profissional que trabalha com madeira. [p=0.4] {a}Ele tem duas tábuas: [p=0.2] "
        "uma de *doze* centímetros [p=0.2] e outra de *dezoito.* [p=0.4] {b}Quer cortar as duas em pedaços *iguais,* [p=0.2] "
        "sem sobrar nenhum pedacinho. [p=0.4] {c}E quer os pedaços *do maior tamanho possível.* [p=0.3] Qual é esse tamanho?"),
    dict(id="05", block="regua", text=
        "{t}Vamos testar réguas. [p=0.3] {a}Régua de um centímetro: [p=0.2] mede as duas certinho. [p=0.3] {b}De dois: "
        "[p=0.2] também. [p=0.3] {c}De três: [p=0.2] também. [p=0.4] {d}De quatro? [p=0.2] Na de doze, [p=0.2] cabe três "
        "vezes. [p=0.2] Na de dezoito, [p=0.2] sobra um pedaço de dois. [p=0.3] *Não serve.*"),
    dict(id="06", block="regua", text=
        "{a}E a régua de *seis?* [p=0.3] Cabe duas vezes na de doze [p=0.2] e três vezes na de dezoito. [p=0.2] Sem sobra! "
        "[p=0.4] {b}E dá para ir além? [p=0.3] Uma régua maior que doze [p=0.2] nem cabe na tábua menor. [p=0.4] {c}Então "
        "seis centímetros é a *maior régua* [p=0.2] que mede as duas tábuas certinho."),

    # ================= BLOCO B: DEFINIÇÃO =================
    dict(id="07", block="definicao", text=
        "{t}Essa maior régua tem nome: [p=0.2] *MDC,* [p=0.2] máximo divisor comum. [p=0.4] {a}Máximo quer dizer *o maior.* "
        "[p=0.3] {b}Divisor comum, [p=0.2] um número que divide *todos* os dados. [p=0.4] {c}A definição: [p=0.2] o maior "
        "número que divide todos os dados ao mesmo tempo, [p=0.2] sem deixar resto. [p=0.4] {d}MDC de doze e dezoito: "
        "[p=0.2] *seis.*"),

    # ================= BLOCO C: PELA FATORAÇÃO =================
    dict(id="08", block="fatoracao", text=
        "{t}E com números grandes, [p=0.2] testar régua por régua demora. [p=0.3] Tem atalho? [p=0.4] {a}Tem: [p=0.2] a "
        "receita. [p=0.3] {b}A regra é: [p=0.2] *fatores comuns, com o menor expoente.* [p=0.4] {c}Por quê? [p=0.2] O divisor "
        "comum precisa *caber* nos dois números. [p=0.3] {d}Então quem manda é o expoente *menor.* [p=0.3] {e}E um fator que "
        "falta em algum número [p=0.2] fica de fora."),
    dict(id="09", block="fatoracao", text=
        "{t}Testando com doze e dezoito. [p=0.3] {a}Doze é dois ao quadrado vezes três. [p=0.3] {b}Dezoito é dois vezes três "
        "ao quadrado. [p=0.4] {c}Fatores comuns: [p=0.2] o dois e o três. [p=0.3] {d}Do dois, o menor expoente é um. [p=0.2] "
        "Do três, também um. [p=0.4] {e}Dois vezes três: [p=0.2] *seis.* [p=0.3] {f}A mesma régua do marceneiro!"),
    dict(id="10", block="fatoracao", text=
        "{t}Agora eu faço um maior: [p=0.2] setenta e dois e cento e vinte. [p=0.4] {a}Setenta e dois é dois ao cubo vezes "
        "três ao quadrado. [p=0.3] {b}Cento e vinte é dois ao cubo vezes três vezes cinco. [p=0.4] {c}Comuns: [p=0.2] dois e "
        "três. [p=0.3] {d}Menores expoentes: [p=0.2] dois ao cubo [p=0.2] e três elevado a um. [p=0.4] {e}Oito vezes três: "
        "[p=0.2] *vinte e quatro.* [p=0.4] {f}E o cinco? [p=0.3] O cinco ficou de fora porque não aparece nos dois."),

    # ================= BLOCO C2: O ATALHO DO VARAL (TODOS JUNTOS) =================
    dict(id="10b", block="varal", text=
        "{t}Agora, o atalho de prova: [p=0.2] fatorar os dois números *juntos,* [p=0.2] num varal só. [p=0.4] {a}Escrevo "
        "setenta e dois e cento e vinte lado a lado. [p=0.3] {r1}O dois divide os dois? [p=0.2] Divide: [p=0.2] trinta e seis "
        "e sessenta. [p=0.2] Marco o dois. [p=0.3] {r2}De novo o dois: [p=0.2] dezoito e trinta. [p=0.2] Marco. [p=0.3] "
        "{r3}De novo: [p=0.2] nove e quinze. [p=0.2] Marco. [p=0.4] {r4}O dois não divide o nove. [p=0.2] Próximo primo, "
        "o três: [p=0.2] divide os dois, [p=0.2] três e cinco. [p=0.2] Marco o três. [p=0.4] {r5}E agora? [p=0.2] Nenhum "
        "primo divide o três *e* o cinco ao mesmo tempo. [p=0.4] {m}MDC: [p=0.2] só os marcados. [p=0.2] Dois vezes dois "
        "vezes dois vezes três: [p=0.2] *vinte e quatro.*"),
    dict(id="10c", block="varal", text=
        "{t}E tem um bônus. [p=0.3] {a}Termine o varal: [p=0.2] o três sozinho vira um; [p=0.2] o cinco sozinho vira um. "
        "[p=0.4] {b}Multiplique *todos* os primos do varal, [p=0.2] marcados ou não: [p=0.2] dois, dois, dois, três, três e "
        "cinco. [p=0.3] {c}Dá *trezentos e sessenta:* [p=0.2] o MMC do episódio passado! [p=0.4] {d}Um varal, [p=0.2] *dois "
        "resultados:* [p=0.2] todos os primos dão o MMC; [p=0.2] só os marcados dão o MDC."),
    dict(id="10d", block="varal", text=
        "{t}Três dicas de prova para o varal. [p=0.4] {a}Um: [p=0.2] teste os primos em ordem, [p=0.2] dois, três, cinco, "
        "sete, [p=0.2] usando os atalhos de divisibilidade do episódio um. [p=0.4] {b}Dois: [p=0.2] só marque quando o primo "
        "divide *todos* os números da linha. [p=0.4] {c}Três: [p=0.2] se a questão pede só o MDC, [p=0.2] pode *parar* "
        "assim que nenhum primo divide todos ao mesmo tempo. [p=0.3] O resto do varal não muda o MDC."),
    dict(id="11", block="nosfazemos", text=
        "{t}Sua vez. [p=0.3] {a}Calcule o MDC de *trinta* e *quarenta e cinco* [p=0.2] pelo varal. [p=0.3] {p}Pause e "
        "tente. [p=2.0] {b}O dois divide o trinta, [p=0.2] mas não o quarenta e cinco. [p=0.2] Como eu só quero o MDC, "
        "[p=0.2] pulo o dois. [p=0.3] {c}O três divide os dois: [p=0.2] dez e quinze. [p=0.2] Marco. [p=0.3] {d}O cinco "
        "divide os dois: [p=0.2] dois e três. [p=0.2] Marco. [p=0.3] {e}Dois e três: [p=0.2] nenhum primo divide os dois. "
        "[p=0.2] Paro. [p=0.3] {f}Três vezes cinco: [p=0.2] *quinze.*"),

    # ================= BLOCO D: EUCLIDES =================
    dict(id="12", block="euclides", text=
        "{t}E se o número for difícil de fatorar? [p=0.4] {a}Existe um caminho com divisões, [p=0.2] o *algoritmo de "
        "Euclides.* [p=0.3] {b}Algoritmo é uma sequência de passos, [p=0.2] como uma receita. [p=0.4] {c}A regra: [p=0.2] "
        "divida o maior pelo menor, "
        "[p=0.2] depois o divisor pelo resto, [p=0.2] e assim por diante. [p=0.3] {d}O último resto diferente de zero é o MDC."),
    dict(id="13", block="euclides", text=
        "{t}Veja com um retângulo de cento e vinte por setenta e dois. [p=0.4] {a}Corto o maior quadrado: [p=0.2] setenta e "
        "dois. [p=0.2] Sobram quarenta e oito. [p=0.4] {b}No que sobrou, [p=0.2] um quadrado de quarenta e oito. [p=0.2] "
        "Sobram vinte e quatro. [p=0.4] {c}Quadrados de vinte e quatro: [p=0.2] cabem *dois,* [p=0.2] sem sobra. [p=0.4] "
        "{d}Último resto diferente de zero: [p=0.2] *vinte e quatro.* [p=0.3] O mesmo do varal."),

    # ================= BLOCO E: COMO RECONHECER =================
    dict(id="14", block="reconhecer", text=
        "{t}E como saber que a questão é de MDC? [p=0.4] {a}Repare nas palavras: [p=0.2] o maior tamanho possível, [p=0.2] "
        "{b}dividir em partes iguais sem sobra, [p=0.2] {c}o maior número de grupos, [p=0.2] {d}a maior medida que cabe "
        "exatamente. [p=0.4] {e}Repartir em pedaços iguais, [p=0.2] o maior possível: [p=0.2] *MDC.*"),

    # ================= BLOCO F: CHECAGEM =================
    dict(id="15", block="sanidade", text=
        "{t}Fez a conta. [p=0.2] Como saber se está certa? [p=0.4] {a}Checagem rápida: [p=0.2] o MDC *nunca* é maior que o "
        "menor dos números dados. [p=0.4] {b}É a régua: [p=0.2] se ela for maior que a menor tábua, [p=0.2] nem cabe nela. "
        "[p=0.4] {c}Vinte e quatro é menor que setenta e dois? [p=0.2] É. [p=0.2] Passou."),

    # ================= BLOCO G: O SEGUNDO PASSO =================
    dict(id="16", block="passo2", text=
        "{t}E agora, o passo que mais derruba gente. [p=0.4] {a}Achou o MDC? [p=0.2] *Leia de novo a pergunta.* [p=0.4] "
        "{b}Ela quer o tamanho do pedaço? [p=0.2] Então o MDC já é a resposta. [p=0.4] {c}Ela quer *quantos* pedaços? [p=0.3] "
        "Volte às tábuas do marceneiro: [p=0.2] {d}doze dividido por seis dá dois, [p=0.2] dezoito dividido por seis dá "
        "três. [p=0.3] {e}Dois mais três: [p=0.2] *cinco pedaços.* [p=0.4] {f}O MDC é seis, [p=0.2] mas a resposta é cinco."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] repartir em pedaços iguais, [p=0.2] o maior possível: "
        "[p=0.2] MDC. [p=0.5] {b}Dois: [p=0.2] no varal, [p=0.2] só entram os primos que dividem *todos.* [p=0.5] {c}Três: [p=0.2] achou o "
        "MDC? [p=0.2] Agora responda o que foi perguntado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] no MDC, [p=0.2] multiplicar *todos* os primos do "
        "varal. [p=0.3] Com setenta e dois e cento e vinte, [p=0.2] dá trezentos e sessenta. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque é assim que se faz o MMC. [p=0.4] {c}Mas trezentos e sessenta é maior que setenta e dois: [p=0.2] a régua "
        "nem cabe. [p=0.2] No MDC, [p=0.2] só entram os primos *marcados.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] responder o MDC [p=0.2] quando a questão pede o número de pedaços [p=0.2] ou de alunos. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a conta difícil já foi feita. [p=0.4] {c}Mas o MDC é só o meio do caminho: "
        "[p=0.2] leia a pergunta e dê o *segundo passo.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir MDC com *MMC.* [p=0.4] {b}Parece certo, [p=0.2] porque os nomes são quase iguais "
        "[p=0.2] e as contas usam a mesma receita. [p=0.4] {c}Mas MMC é reencontro, [p=0.2] coisas que se repetem. [p=0.3] "
        "MDC é a maior régua, [p=0.2] coisas que se repartem. [p=0.3] {d}O próximo episódio é só sobre essa decisão."),

    # ================= QUESTÃO 2 =================
    dict(id="21", block="q2", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}Um marceneiro tem três tábuas medindo cento e vinte centímetros, "
        "[p=0.2] cento e oitenta centímetros [p=0.2] e trezentos centímetros. [p=0.4] {b}Ele quer cortá-las em pedaços de "
        "mesmo comprimento, [p=0.2] o maior possível, [p=0.2] sem que sobre nenhum pedaço menor. [p=0.4] {c}Quantos pedaços "
        "obterá ao todo? [p=0.4] {d}A: [p=0.2] seis. [p=0.3] {e}B: [p=0.2] dez. [p=0.3] {f}C: [p=0.2] doze. [p=0.3] {g}D: "
        "[p=0.2] quinze. [p=0.3] {h}E: [p=0.2] vinte. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{t}Vamos lá. [p=0.3] {a}Pedaços iguais, [p=0.2] o maior possível, [p=0.2] sem sobra: [p=0.2] *MDC.* [p=0.4] "
        "{b}Varal com as três tábuas. [p=0.3] {r1}O dois divide as três: [p=0.2] sessenta, noventa e cento e cinquenta. "
        "[p=0.2] Marco. [p=0.3] {r2}O dois de novo: [p=0.2] trinta, quarenta e cinco e setenta e cinco. [p=0.2] Marco. "
        "[p=0.3] {r3}O dois não divide o quarenta e cinco. [p=0.2] O três divide as três: [p=0.2] dez, quinze e vinte e "
        "cinco. [p=0.2] Marco. [p=0.3] {r4}O cinco divide as três: [p=0.2] dois, três e cinco. [p=0.2] Marco. [p=0.3] "
        "{r5}Dois, três e cinco: [p=0.2] nenhum primo divide os três. [p=0.2] Paro. [p=0.4] {f}Dois vezes dois vezes três "
        "vezes cinco: [p=0.2] *sessenta centímetros.* [p=0.3] {g}Checagem: [p=0.2] sessenta é menor que cento e vinte. "
        "[p=0.2] Passou."),
    dict(id="23", block="q2", text=
        "{t}Mas a pergunta é *quantos pedaços,* [p=0.2] não o tamanho. [p=0.4] {a}Juntando as tábuas: [p=0.2] cento e vinte, "
        "mais cento e oitenta, [p=0.2] mais trezentos: [p=0.2] seiscentos centímetros. [p=0.4] {b}Seiscentos dividido por "
        "sessenta: [p=0.2] *dez pedaços.* [p=0.4] {m}E um macete: [p=0.2] olhe o que sobrou no fim do varal: [p=0.2] dois, "
        "três e cinco. [p=0.3] É quantos pedaços sai de cada tábua. [p=0.2] Dois mais três mais cinco: [p=0.2] dez, de novo! "
        "[p=0.3] {ok}*Letra B!*"),
    dict(id="24", block="q2", text=
        "{x}E o vinte? [p=0.3] É de quem usou pedaços de trinta centímetros: [p=0.2] trinta divide as três tábuas, [p=0.2] "
        "mas não é a *maior* régua. [p=0.4] {y}Seis, doze e quinze [p=0.2] não saem de régua nenhuma que mede as três. "
        "[p=0.4] {z}E repare: [p=0.2] o sessenta nem está nas alternativas. [p=0.2] Quem parasse no MDC [p=0.2] ficaria "
        "procurando uma resposta que não existe."),

    # ================= QUESTÃO 6 =================
    dict(id="25", block="q6", text=
        "{t}Próxima. [p=0.3] {a}Uma escola vai organizar quarenta e oito meninos e trinta e seis meninas em grupos de "
        "trabalho. [p=0.4] {b}Todos os grupos devem ter o mesmo número de meninos [p=0.2] e o mesmo número de meninas, "
        "[p=0.2] sem que sobre nenhum aluno. [p=0.4] {c}Formando o maior número possível de grupos, [p=0.2] quantos alunos "
        "haverá em cada grupo?"),
    dict(id="26", block="q6", text=
        "{a}A: [p=0.2] quatro. [p=0.3] {b}B: [p=0.2] sete. [p=0.3] {c}C: [p=0.2] doze. [p=0.3] {d}D: [p=0.2] catorze. "
        "[p=0.3] {e}E: [p=0.2] vinte e um. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="27", block="q6", text=
        "{t}Repartir sem sobra, [p=0.2] o maior número de grupos: [p=0.2] *MDC.* [p=0.4] {a}Varal com quarenta e oito e "
        "trinta e seis. [p=0.3] {r1}O dois divide os dois: [p=0.2] vinte e quatro e dezoito. [p=0.2] Marco. [p=0.3] {r2}De "
        "novo: [p=0.2] doze e nove. [p=0.2] Marco. [p=0.3] {r3}O dois não divide o nove. [p=0.2] O três divide os dois: "
        "[p=0.2] quatro e três. [p=0.2] Marco. [p=0.3] {r4}Quatro e três: [p=0.2] nenhum primo divide os dois. [p=0.2] "
        "Paro. [p=0.4] {c}Dois vezes dois vezes três: [p=0.2] *doze grupos.* [p=0.3] {e}Checagem: [p=0.2] doze é menor que "
        "trinta e seis. [p=0.2] Passou."),
    dict(id="28", block="q6", text=
        "{t}Agora a pergunta real: [p=0.2] quantos alunos *em cada grupo?* [p=0.4] {a}Quarenta e oito meninos divididos por "
        "doze: [p=0.2] quatro meninos. [p=0.3] {b}Trinta e seis meninas divididas por doze: [p=0.2] três meninas. [p=0.4] "
        "{m}Repare: [p=0.2] quatro e três [p=0.2] é exatamente o que sobrou no fim do varal! [p=0.4] {c}Quatro mais três: "
        "[p=0.2] *sete alunos* por grupo. [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q6", text=
        "{x}E a armadilha? [p=0.3] Quem achou o MDC e *parou* [p=0.2] marca doze: [p=0.2] a letra C. [p=0.4] {y}Quem contou "
        "só os meninos [p=0.2] marca quatro. [p=0.4] {z}E catorze e vinte e um [p=0.2] são de quem formou seis [p=0.2] ou "
        "quatro grupos: [p=0.2] dá certo, [p=0.2] mas não é o *maior* número de grupos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] repartir em pedaços iguais, [p=0.2] o maior possível: "
        "[p=0.2] MDC. [p=0.5] {b}Dois: [p=0.2] no varal, [p=0.2] só entram os primos que dividem *todos.* [p=0.5] {c}Três: [p=0.2] achou o "
        "MDC? [p=0.2] Agora responda o que foi perguntado."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Agora você sabe calcular os dois. [p=0.4] {b}Mas a questão do ENEM *não diz* qual usar. [p=0.4] {c}No próximo "
        "episódio, [p=0.2] você aprende a decidir [p=0.2] em *dez segundos.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha respondido o MDC quando a questão pedia outra coisa? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
