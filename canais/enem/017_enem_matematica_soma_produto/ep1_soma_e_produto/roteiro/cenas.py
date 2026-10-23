# Roteiro — Equação do 2º grau sem Bhaskara: Soma e Produto (Relações de Girard), Episódio 1 de 1 (aula para iniciantes)
# Base: prompt detalhado do usuário (22/10/2026) — estrutura, falas citadas e exemplos dele; sem material HTML.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Falas literais do usuário: abertura ("Você sabia que é possível resolver..."), cena 04 ("Precisamos encontrar dois
#   números que..."), desafio ("Agora é sua vez! Quais são os dois números cuja soma é 9 e cujo produto é 20?") e
#   encerramento ("Nem toda equação terá raízes fáceis... como os números se relacionam!"). CTA vem DEPOIS do encerramento.
# Analogia âncora: a TABELA DE PARES (o "caça-pares") — comece pelo produto (poucos pares), use a soma para escolher.
# Contas conferidas por script (analise/conferir_contas.py — Girard × substituição × fatoração; sympy só como conferência):
#   Demonstração: a(x − r)(x − s) = ax² − a(r + s)x + a·r·s ⇒ b = −a(r + s) ⇒ r + s = −b/a ; c = a·r·s ⇒ r·s = c/a.
#   x² − 5x + 6 = 0 → soma −(−5)/1 = 5, produto 6/1 = 6 → tabela: 1 e 6 (soma 7, produto 6) · 2 e 3 (soma 5, produto 6) ✓
#     substituição: 2² − 5·2 + 6 = 4 − 10 + 6 = 0 ; 3² − 5·3 + 6 = 9 − 15 + 6 = 0 ; fatoração (x − 2)(x − 3) = x² − 3x − 2x + 6.
#   Ex.1 x² − 7x + 12 = 0 → soma 7, produto 12 → pares 1·12 (13), 2·6 (8), 3·4 (7) → 3 e 4.
#   Ex.2 x² + 5x + 6 = 0 → soma −5/1 = −5, produto 6 → produto + = mesmo sinal; soma − = os dois negativos → −2 e −3
#     ((−2) + (−3) = −5 ; (−2)·(−3) = +6 ; conferindo x = −2: 4 − 10 + 6 = 0). Produto negativo = sinais opostos.
#   Ex.3 2x² − 10x + 12 = 0 → soma −(−10)/2 = 5, produto 12/2 = 6 → 2 e 3 (2·4 − 20 + 12 = 0).
#   Desafio x² − 9x + 20 = 0 → soma 9, produto 20 → pares 1·20 (21), 2·10 (12), 4·5 (9) → x₁ = 4, x₂ = 5 (16 − 36 + 20 = 0).
#   Contagem regressiva: [p=10] na cena 21 (o voz_externa garante pausas ≥ 1 s no áudio).
# Crédito (só este fato): Albert Girard, matemático francês do século XVII.
# Nunca usar Bhaskara para resolver os exemplos. Nunca trocar sinais de coeficientes ou raízes.
# Voz: gerada em 2 partes (corte na cena 12); conferida pela transcrição (analise/extenso.py). Para caber em 10 min,
#   duas frases foram recortadas do áudio da parte 1 (backup em audio/nova_voz/parte_1_original.wav) e do roteiro:
#   03 "Uma equação do segundo grau tem no máximo duas." e 11 "Exatamente a soma e o produto que usamos!".
# Frases-chave (meio): 1. A soma das raízes é menos b sobre a. 2. O produto das raízes é c sobre a.
#   3. Comece pelo produto e use a soma para escolher o par. (Fim: os 5 passos pedidos pelo usuário, que as contêm.)
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha/sinais · verde = atalho/resposta · vermelho = erro.

TITULO = "Equação do 2º grau sem Bhaskara: Soma e Produto — Matemática ENEM"

# Estilo da voz (gerar_voz_local.py): voz Neno, igual às séries 015 e 016
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
}

SCENES = [
    # ================= CENA 1 — INTRODUÇÃO =================
    dict(id="01", block="hook", text=
        "{a}Você sabia que é possível resolver uma equação do segundo grau *sem* utilizar a fórmula de Bhaskara? "
        "[p=0.5] {b}E melhor: [p=0.2] em alguns casos, [p=0.2] você consegue descobrir a resposta *apenas olhando para "
        "os números!* [p=0.6] {c}Olhe esta equação: [p=0.2] x ao quadrado, menos cinco x, mais seis, igual a zero. "
        "[p=0.5] {d}Em poucos minutos, [p=0.2] você vai enxergar as respostas *em segundos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai encontrar as raízes de equações como essa [p=0.2] usando só *duas "
        "operações:* [p=0.3] {b}a *soma* [p=0.3] {c}e a *multiplicação.* [p=0.5] {d}E entendendo *por que* "
        "funciona."),
    dict(id="03", block="prereq", text=
        "{t}Antes, uma lembrança rápida. [p=0.3] {a}Equação do segundo grau é a que tem *x ao quadrado,* [p=0.2] e "
        "nenhuma potência maior. [p=0.4] {b}E *raiz* [p=0.2] é o número que, colocado no lugar do x, [p=0.2] faz a conta "
        "dar *zero.*"),

    # ================= CENA 2 — ENTENDENDO A LÓGICA =================
    dict(id="04", block="logica", text=
        "{t}Vamos voltar à nossa equação. [p=0.3] {a}x ao quadrado, menos cinco x, mais seis, igual a zero. [p=0.5] "
        "{b}Precisamos encontrar dois números que, quando *somados,* resultem em *cinco* [p=0.3] {c}e, quando "
        "*multiplicados,* resultem em *seis.* [p=0.5] {d}Repare numa curiosidade: [p=0.2] na equação aparece *menos* "
        "cinco, [p=0.2] mas a soma que procuramos é cinco *positivo.* [p=0.3] {e}Já, já eu mostro de onde vem essa "
        "troca."),
    dict(id="05", block="tabela", text=
        "{t}Vamos testar pares numa tabela. [p=0.3] {a}Uma dica: [p=0.2] comece pelo *produto,* [p=0.2] porque existem "
        "poucos pares com produto seis. [p=0.4] {b}Primeiro par: [p=0.2] um e seis. [p=0.3] {c}Somando, "
        "[p=0.2] um mais seis dá *sete.* [p=0.3] {d}Multiplicando, [p=0.2] um vezes seis dá *seis.* [p=0.3] {e}O produto "
        "bateu, [p=0.2] mas a soma deu sete, [p=0.2] e não cinco. [p=0.2] Não serve. [p=0.5] {f}Segundo par: [p=0.2] dois "
        "e três. [p=0.3] {g}Somando, [p=0.2] dois mais três dá *cinco.* [p=0.3] {h}Multiplicando, [p=0.2] dois vezes três "
        "dá *seis.* [p=0.4] {i}As duas condições batem! [p=0.3] {j}Os números são *dois e três.*"),
    dict(id="06", block="porque", text=
        "{t}Mas por que dois e três são as raízes? [p=0.4] {a}Vamos testar o *dois* na equação. [p=0.4] {b}Dois ao quadrado é quatro. [p=0.3] {c}Cinco vezes dois é dez. [p=0.3] "
        "{d}Então fica quatro, menos dez, mais seis. [p=0.3] {e}Quatro menos dez é menos seis; [p=0.2] menos seis mais "
        "seis, [p=0.2] *zero!* [p=0.4] {f}Agora o três: [p=0.2] três ao quadrado é nove; [p=0.2] cinco vezes três, quinze. "
        "[p=0.3] {g}Nove menos quinze mais seis: [p=0.2] *zero* de novo. [p=0.4] {h}Os dois são "
        "raízes!"),
    dict(id="07", block="fatoracao", text=
        "{t}E tem um jeito ainda mais bonito de ver isso. [p=0.3] {a}Escreva assim: [p=0.2] x menos dois, [p=0.2] vezes "
        "x menos três, [p=0.2] igual a zero. [p=0.5] {b}Vamos multiplicar para conferir. [p=0.3] x vezes x: [p=0.2] x ao "
        "quadrado. [p=0.4] {c}x vezes menos três: [p=0.2] menos três x. [p=0.3] {d}Menos dois vezes x: [p=0.2] menos dois "
        "x. [p=0.3] {e}Juntos, [p=0.2] *menos cinco x.* [p=0.4] {f}E menos dois vezes menos três: [p=0.2] menos com menos "
        "dá mais, [p=0.2] *mais seis.* [p=0.4] {g}Voltou a nossa equação!"),
    dict(id="08", block="fatoracao", text=
        "{t}Agora olhe para essa multiplicação. [p=0.3] {a}Quando uma multiplicação dá *zero,* [p=0.2] pelo menos um dos "
        "fatores é zero. [p=0.4] {b}Se x menos dois for zero, [p=0.2] *x é dois.* [p=0.4] {c}Se x menos três for zero, "
        "[p=0.2] *x é três.* [p=0.4] {d}As soluções são x igual a dois [p=0.2] e x igual a três. [p=0.4] {e}E repare: "
        "[p=0.2] o cinco da equação é a *soma,* dois mais três, [p=0.2] {f}e o seis é o *produto,* dois vezes três."),

    # ================= CENA 3 — REGRA GERAL =================
    dict(id="09", block="geral", text=
        "{t}Agora, a regra geral. [p=0.3] {a}Toda equação do segundo grau pode ser escrita assim: [p=0.2] a x ao "
        "quadrado, mais b x, mais c, igual a zero. [p=0.5] {b}O *a* é o número que acompanha o x ao quadrado. [p=0.3] "
        "{c}O *b* é o número que acompanha o x, [p=0.2] *com o sinal.* [p=0.3] {d}E o *c* é o número sozinho. "
        "[p=0.5] {e}Um detalhe importante: [p=0.2] o a *nunca* pode ser zero. [p=0.3] {f}Se fosse, "
        "[p=0.2] o x ao quadrado sumiria, [p=0.2] e a equação deixaria de ser do segundo grau."),
    dict(id="10", block="geral", text=
        "{t}Vamos identificar as letras na nossa equação. [p=0.3] {a}Na frente do x ao quadrado não aparece nada. "
        "[p=0.2] Quando isso acontece, [p=0.2] tem um *um* escondido: [p=0.2] a é um. [p=0.4] {b}O b é *menos cinco,* "
        "[p=0.2] com o sinal de menos junto. [p=0.3] {c}E o c é *seis.*"),
    dict(id="11", block="girard", text=
        "{t}Com essas letras, [p=0.2] vêm as *Relações de Girard,* [p=0.2] do matemático francês Albert Girard, "
        "[p=0.2] do século dezessete. [p=0.4] {a}A soma das raízes é *menos b sobre a.* [p=0.4] {b}E o produto "
        "das raízes é *c sobre a.* [p=0.5] {c}Testando: [p=0.2] menos b sobre a [p=0.2] é menos, menos cinco, sobre um. "
        "[p=0.2] Menos com menos dá mais: [p=0.2] *cinco.* [p=0.4] {d}E c sobre a [p=0.2] é seis sobre um: [p=0.2] "
        "*seis.*"),
    dict(id="12", block="prova", text=
        "{t}Mas por que o sinal do b aparece *trocado* na soma? [p=0.4] Vamos descobrir. [p=0.3] {a}Chame as duas raízes "
        "de *r* e *s.* [p=0.4] {b}Como vimos na fatoração, [p=0.2] a equação pode ser escrita assim: [p=0.2] a, vezes x "
        "menos r, vezes x menos s, igual a zero. [p=0.5] {c}Multiplicando os parênteses: [p=0.2] x vezes x, [p=0.2] x ao "
        "quadrado. [p=0.3] {d}Os termos do meio: [p=0.2] menos s x [p=0.2] e menos r x. [p=0.3] {e}Juntos, [p=0.2] "
        "*menos, r mais s, vezes x.* [p=0.4] {f}E menos r vezes menos s: [p=0.2] *mais r s.* [p=0.4] {g}Agora, multiplique "
        "tudo pelo a: [p=0.2] a x ao quadrado, [p=0.2] menos a vezes r mais s, x, [p=0.2] mais a r s."),
    dict(id="13", block="prova", text=
        "{t}Agora compare com a forma geral, [p=0.2] pedaço por pedaço. [p=0.4] {a}O número que acompanha o x [p=0.2] é o "
        "b. [p=0.2] Então, b é igual a menos a, vezes r mais s. [p=0.5] {b}Para isolar a soma, [p=0.2] divida os dois "
        "lados por menos a. [p=0.3] {c}Fica: [p=0.2] r mais s é igual a *menos b sobre a.* [p=0.4] {d}Viu? [p=0.2] O sinal "
        "de menos *já estava lá,* [p=0.2] escondido no menos r e no menos s dos parênteses. [p=0.5] {e}E o número sozinho "
        "é o c: [p=0.2] c é igual a a r s. [p=0.3] {f}Dividindo por a, [p=0.2] o produto r s é *c sobre a.*"),
    dict(id="14", block="armadilha", text=
        "{t}Cuidado com a armadilha mais comum. [p=0.3] {a}Em x ao quadrado, menos cinco x, mais seis, [p=0.2] "
        "muita gente diz que a soma é *menos cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque o menos cinco está à vista. "
        "[p=0.4] {c}Mas a regra é *menos b* sobre a: [p=0.2] o sinal troca. [p=0.2] A soma é *mais cinco.*"),

    # ================= CENA 4 — EXEMPLOS PROGRESSIVOS =================
    dict(id="15", block="ex1", text=
        "{t}Hora de praticar. [p=0.3] {a}Exemplo um: [p=0.2] x ao quadrado, menos "
        "sete x, mais doze, igual a zero. [p=0.4] {b}Aqui, a é um, [p=0.2] b é menos sete [p=0.2] e c é doze. [p=0.4] "
        "{c}Soma: [p=0.2] menos b sobre a, [p=0.2] menos, menos sete, sobre um: [p=0.2] *sete.* [p=0.3] {d}Produto: "
        "[p=0.2] c sobre a, [p=0.2] doze sobre um: [p=0.2] *doze.* [p=0.4] {e}Pares que, multiplicados, dão doze: [p=0.2] "
        "um e doze, [p=0.2] que somam treze. [p=0.3] {f}Dois e seis, [p=0.2] que somam oito. [p=0.3] {g}Três e quatro, "
        "[p=0.2] que somam *sete!* [p=0.4] {h}As raízes são *três e quatro.*"),
    dict(id="16", block="ex2", text=
        "{t}Exemplo dois: [p=0.2] agora com sinais. [p=0.3] {a}x ao quadrado, *mais* cinco x, mais seis, igual a zero. "
        "[p=0.4] {b}Aqui, b é *mais cinco.* [p=0.3] {c}Soma: [p=0.2] menos b sobre a, [p=0.2] menos cinco sobre um: "
        "[p=0.2] *menos cinco.* [p=0.3] {d}Produto: [p=0.2] seis sobre um: [p=0.2] *seis.* [p=0.4] {e}Dois números com "
        "soma *negativa* [p=0.2] e produto *positivo.* [p=0.2] Como descobrir os sinais?"),
    dict(id="17", block="ex2", text=
        "{t}Primeiro, o produto. [p=0.3] {a}Se ele é *positivo,* [p=0.2] os dois números têm o *mesmo "
        "sinal:* [p=0.2] os dois positivos, [p=0.2] ou os dois negativos. [p=0.4] {b}Aí, olhe para a soma. [p=0.2] Se a "
        "soma é *negativa,* [p=0.2] os dois são *negativos.* [p=0.2] Se é positiva, [p=0.2] os dois são positivos. "
        "[p=0.4] {c}E se o produto for *negativo,* [p=0.2] os números têm *sinais opostos:* [p=0.2] um positivo [p=0.2] e "
        "um negativo. [p=0.4] {d}No nosso caso, [p=0.2] o produto é positivo [p=0.2] e a soma é negativa: [p=0.2] *os "
        "dois são negativos.* [p=0.4] {e}Menos dois e menos três. [p=0.3] {f}Somando: [p=0.2] menos dois, menos três, "
        "[p=0.2] *menos cinco.* [p=0.3] {g}Multiplicando: [p=0.2] menos com menos dá mais, [p=0.2] *mais seis.* [p=0.3] "
        "{h}As raízes são *menos dois e menos três.*"),
    dict(id="18", block="ex3", text=
        "{t}Exemplo três: [p=0.2] quando o a *não* é um. [p=0.3] {a}Dois x ao quadrado, menos dez x, mais doze, igual a "
        "zero. [p=0.4] {b}Aqui, a é *dois,* [p=0.2] b é menos dez [p=0.2] e c é doze. [p=0.4] {c}Soma: [p=0.2] menos b "
        "sobre a, [p=0.2] menos, menos dez, sobre dois. [p=0.2] Dez sobre dois: [p=0.2] *cinco.* [p=0.4] {d}Produto: "
        "[p=0.2] c sobre a, [p=0.2] doze sobre dois: [p=0.2] *seis.* [p=0.4] {e}Soma cinco e produto seis: [p=0.2] você já "
        "conhece esses números! [p=0.3] {f}*Dois e três.* [p=0.4] {g}Conferindo o dois: [p=0.2] dois ao quadrado é quatro, "
        "vezes dois, oito. [p=0.2] Dez vezes dois, vinte. [p=0.2] Oito, menos vinte, mais doze: [p=0.2] *zero.*"),
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.4] {a}Um: [p=0.2] a soma das raízes é menos b sobre a. [p=0.4] {b}Dois: "
        "[p=0.2] o produto das raízes é c sobre a. [p=0.4] {c}Três: [p=0.2] comece pelo produto, [p=0.2] e use a soma "
        "para escolher o par."),

    # ================= CENA 5 — DESAFIO =================
    dict(id="20", block="desafio", text=
        "{t}*Agora é sua vez!* [p=0.4] {a}A equação é: [p=0.2] x ao quadrado, menos nove x, mais vinte, igual a zero. "
        "[p=0.5] {b}Quais são os dois números cuja soma é *nove* [p=0.2] e cujo produto é *vinte?* [p=0.4] {c}Você tem "
        "dez segundos. {cd}[p=10] {r}Tempo!"),
    dict(id="21", block="desafio", text=
        "{t}Vamos conferir. [p=0.3] {a}A soma é menos, menos nove, sobre um: [p=0.2] nove. [p=0.2] O produto, vinte sobre "
        "um: [p=0.2] vinte. [p=0.4] {b}Pares que, multiplicados, dão vinte: [p=0.2] um e vinte, [p=0.2] que somam vinte e "
        "um. [p=0.3] {c}Dois e dez, [p=0.2] que somam doze. [p=0.3] {d}Quatro e cinco, [p=0.2] que somam *nove!* [p=0.4] "
        "{e}Quatro mais cinco é nove; [p=0.2] {f}quatro vezes cinco é vinte. [p=0.4] {g}Logo, [p=0.2] x um é *quatro* "
        "[p=0.2] e x dois é *cinco.* [p=0.4] {h}Acertou? [p=0.2] Então você resolveu uma equação do "
        "segundo grau *de cabeça!*"),

    # ================= CENA 6 — ENCERRAMENTO =================
    dict(id="22", block="passos", text=
        "{t}Vamos recapitular o método em cinco passos. [p=0.4] {a}Um: [p=0.2] identifique a, b e c, [p=0.2] com os "
        "sinais. [p=0.4] {b}Dois: [p=0.2] a soma das raízes é menos b sobre a. [p=0.4] {c}Três: [p=0.2] o produto das "
        "raízes é c sobre a. [p=0.4] {d}Quatro: [p=0.2] procure dois números que satisfaçam as duas condições. [p=0.2] "
        "Comece pelo produto. [p=0.4] {e}Cinco: [p=0.2] confira, substituindo na equação original. [p=0.2] A conta tem "
        "que dar zero."),
    dict(id="23", block="fecho", text=
        "{a}Nem toda equação terá raízes fáceis de encontrar mentalmente. [p=0.5] {b}Mas, quando você entende a lógica "
        "da soma e do produto, [p=0.2] começa a enxergar a matemática de uma maneira *completamente diferente.* [p=0.6] "
        "{c}O segredo não é decorar fórmulas, [p=0.3] mas *compreender como os números se relacionam!* [p=0.6] {d}E, "
        "quando as raízes não forem fáceis de achar de cabeça, [p=0.2] veja a aula do *método de Po-Shen Loh,* [p=0.2] "
        "aqui no canal."),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto tempo você levou para resolver o desafio? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
