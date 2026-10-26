# Roteiro — Matrizes e Operações, Episódio 4 de 5: o que muda em relação aos números e a matriz inversa
# Base: Estudos/Enem/estudos/01-matematica/33-matrizes-operacoes.html — seções 06 e 07 + Questões 4, 9 e 6 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   MEIA E SAPATO: multiplicar matrizes é como meia e sapato, a ordem muda o resultado (e, para desfazer, a ordem se
#     inverte: tira primeiro o sapato, depois a meia → (AB)ᵗ = BᵗAᵗ).
#   A IDENTIDADE É O NÚMERO 1 DAS MATRIZES: multiplicar por ela não muda nada.
#   A INVERSA É A CHAVE DO CADEADO: A tranca a mensagem, A⁻¹ destranca. Receita 2 × 2: troca a diagonal, muda o sinal da
#     secundária, divide por ad − bc.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida (sem reensinar): linha por coluna (episódio 3), identidade e transposta (episódio 1).
# Convenção de leitura falada: a matriz é lida LINHA POR LINHA ("um, dois; zero, um").
# Bloco a = exemplo da seção 06 (A = (1 2 / 0 1), B = (1 0 / 3 1)); a Questão 4 ("eu faço") usa as mesmas matrizes,
#   como o material e o prompt pedem.
# Bloco b: o "não se corta A" usa um exemplo NOSSO: U = (1 1 / 1 1), U · 0 = U · (1 −1 / −1 1) = 0, mas 0 ≠ (1 −1 / −1 1).
# Bloco e: a receita usa (3 1 / 5 2), como o prompt e a direção visual pedem (animação principal). RESSALVA: é a mesma
#   chave da Questão 6 ("você faz"); mantido por ser o desenho do usuário. Na Q6, o que é novo é multiplicar A⁻¹ pela
#   mensagem (a ordem A⁻¹ · E) e as alternativas erradas; a narração da Q6 avisa "a chave você já conhece".
# Acréscimos NOSSOS (marcados): atalhos verdes "para provar que AB ≠ BA basta UMA casa diferente; para saber se o produto
#   existe, confira o meio" (cena 07) e "receita em 3 movimentos: TROCA, SINAL, DIVIDE + conferência" (cena 14); a
#   leitura da transposta pelo "tirar a roupa ao contrário" (cena 10).
# Erros clássicos com números já resolvidos: erro 1 usa o bloco a (7 contra 1); erro 2, o gancho; erro 3, a matriz do
#   "nós fazemos" (2 1 / 3 2): só trocar a diagonal devolve a própria matriz, e o produto dá (7 4 / 12 7), não I.
#   Nenhum usa a chave da Questão 6.
# Nós fazemos (prompt): inversa de (2 1 / 3 2): ad − bc = 4 − 3 = 1 → (2 −1 / −3 2), conferida.
# Questão 4 ("eu faço"): gabarito B (6 0 / 0 −6). Erradas = material (A supõe AB = BA, C é BA − AB, D é A − B, E é a
#   identidade, sem relação com a conta).
# Questão 9 ("nós fazemos", com pausa): gabarito A (A · I = I · A = A). Erradas = material, cada uma derrubada por um
#   bloco desta aula (B → bloco a; C → bloco c; D → bloco c, ordem; E → bloco b).
# Questão 6 ("você faz", com pausa): gabarito D (5 e 2). Erradas = material e prompt (A inverte a ordem; B troca os
#   sinais da diagonal principal: −5 e −2; C só troca a diagonal: 63 e 172; E multiplica de novo por A: 80 e 143).
# Frases-chave (meio e fim, idênticas): 1. A ordem dos fatores altera o produto. 2. Produto zero não exige fator zero.
#   3. Inversa 2 × 2: troca a diagonal, muda o sinal da secundária, divide por ad − bc.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Matriz inversa e as regras que mudam (AB ≠ BA) | Matrizes Ep. 4"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Nos números, [p=0.2] se um produto dá *zero,* [p=0.2] um dos fatores é zero. [p=0.5] {b}Nas matrizes, "
        "*não:* [p=0.3] um, um; um, um, [p=0.2] vezes um, menos um; menos um, um, [p=0.3] {c}dá a *matriz nula,* "
        "[p=0.3] {d}e *nenhuma das duas* é nula."),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Matrizes.* [p=0.4] {a}Ao final, [p=0.2] você vai saber *quais regras "
        "dos números valem* para matrizes [p=0.4] {b}e vai calcular a *inversa* de uma dois por dois [p=0.2] para "
        "*decifrar um código.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio três: [p=0.2] multiplicar matrizes é *linha por coluna:* "
        "[p=0.2] multiplica casa com casa e soma. [p=0.4] {b}Do episódio um: [p=0.2] a *identidade* tem um na "
        "diagonal e zero no resto. [p=0.4] {c}E a *transposta* troca linhas por colunas. [p=0.4] {d}Hoje, [p=0.2] eu "
        "leio cada matriz *linha por linha.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Duas cenas do dia a dia. [p=0.4] {a}Calçar a *meia* e depois o *sapato.* [p=0.2] Agora o contrário: "
        "[p=0.2] o sapato e depois a meia. [p=0.4] {b}A ordem *mudou o resultado.* [p=0.4] {c}E um *cadeado* de "
        "segredo: [p=0.2] quem tranca [p=0.2] precisa de uma *chave* para destrancar."),

    # ================= BLOCO A: AB ≠ BA =================
    dict(id="05", block="ordem", text=
        "{t}A ordem importa nas matrizes? [p=0.4] {a}Nos números, [p=0.2] dois vezes três é três vezes dois. [p=0.2] "
        "Isso se chama propriedade *comutativa:* [p=0.2] trocar a ordem não muda o produto. [p=0.4] {b}Agora, A é um, "
        "dois; zero, um. [p=0.2] B é um, zero; três, um. [p=0.4] {c}A vezes B, [p=0.2] linha por coluna: [p=0.2] "
        "*sete, dois; três, um.* [p=0.4] {d}B vezes A: [p=0.2] *um, dois; três, sete.* [p=0.4] {e}Resultados "
        "diferentes. [p=0.2] Multiplicar matrizes é como *meia e sapato:* [p=0.2] a ordem muda o resultado."),
    dict(id="06", block="nem_existe", text=
        "{t}E às vezes [p=0.2] um dos produtos *nem existe.* [p=0.4] {a}A é dois por três. [p=0.2] B é três por "
        "quatro. [p=0.4] {b}A vezes B: [p=0.2] o três do meio encaixa no três. [p=0.2] Existe, [p=0.2] e dá dois por "
        "quatro. [p=0.4] {c}B vezes A: [p=0.2] o quatro do meio *não encaixa* no dois. [p=0.4] {d}Não existe."),
    dict(id="07", block="atalho_ordem", text=
        "{t}Atalho. [p=0.4] {a}Para saber se o produto existe, [p=0.2] *confira o meio:* [p=0.2] colunas da primeira "
        "[p=0.2] iguais às linhas da segunda. [p=0.4] {b}E para provar que A vezes B é diferente de B vezes A, "
        "[p=0.2] basta *uma casa diferente.* [p=0.4] {c}A primeira casa já resolve: [p=0.2] sete de um lado, [p=0.2] "
        "um do outro."),

    # ================= BLOCO B: PRODUTO NULO =================
    dict(id="08", block="nulo", text=
        "{t}E o produto que dá zero? [p=0.4] {a}Volte ao começo: [p=0.2] um, um; um, um, [p=0.2] vezes um, menos um; "
        "menos um, um. [p=0.4] {b}Primeira linha vezes primeira coluna: [p=0.2] um menos um, [p=0.2] *zero.* [p=0.2] "
        "Todas as casas dão zero. [p=0.4] {c}A *matriz nula* é a que só tem zeros. [p=0.2] E nenhum fator é nulo. "
        "[p=0.4] {d}Por isso, [p=0.2] de A B igual a A C, [p=0.2] você *não pode cortar o A:* [p=0.2] B e C podem "
        "ser *diferentes.*"),

    # ================= BLOCO C: AS PROPRIEDADES =================
    dict(id="09", block="props", text=
        "{t}Então nada dos números vale? [p=0.4] {a}Vale, sim. [p=0.2] A *identidade* é o número um das matrizes: "
        "[p=0.2] A vezes I é A, [p=0.2] e I vezes A também. [p=0.4] {b}A *associativa:* [p=0.2] pode agrupar como "
        "quiser, [p=0.2] A B, vezes C, [p=0.2] é A, vezes B C. [p=0.4] {c}A *distributiva:* [p=0.2] A vezes B mais C "
        "[p=0.2] é A B mais A C, [p=0.2] *mantendo o A do mesmo lado.*"),
    dict(id="10", block="props2", text=
        "{t}E onde mora a pegadinha? [p=0.4] {a}Na transposta do produto, [p=0.2] *a ordem se inverte:* [p=0.2] "
        "A B, transposta, [p=0.2] é B transposta vezes A transposta. [p=0.4] {b}Como tirar a roupa: [p=0.2] primeiro "
        "o sapato, [p=0.2] depois a meia. [p=0.4] {c}E A mais B, ao quadrado, [p=0.2] *não é* A ao quadrado mais dois "
        "A B mais B ao quadrado. [p=0.4] {d}O certo é A ao quadrado, [p=0.2] mais A B, [p=0.2] mais B A, [p=0.2] mais "
        "B ao quadrado. [p=0.2] A B e B A só viram dois A B [p=0.2] se as duas comutarem."),

    # ================= BLOCO D: A INVERSA =================
    dict(id="11", block="inversa", text=
        "{t}Existe divisão de matrizes? [p=0.4] {a}Nos números, [p=0.2] dividir por cinco [p=0.2] é multiplicar por "
        "*um quinto,* [p=0.2] o número que desfaz o cinco. [p=0.4] {b}Nas matrizes, [p=0.2] quem desfaz A [p=0.2] é a "
        "*matriz inversa,* A elevado a menos um: [p=0.2] A vezes A inversa dá a identidade, [p=0.2] nas duas ordens. "
        "[p=0.4] {c}A inversa é a *chave do cadeado:* [p=0.2] A tranca, [p=0.2] A inversa destranca. [p=0.4] {d}Ela "
        "só existe para matrizes *quadradas.* [p=0.2] E nem toda quadrada tem."),

    # ================= BLOCO E: A RECEITA 2 × 2 =================
    dict(id="12", block="receita", text=
        "{t}Como achar a chave de uma dois por dois? [p=0.4] {a}A é três, um; cinco, dois. [p=0.2] Chame as casas de "
        "a, b, c, d. [p=0.4] {b}Primeiro, a conta *a d menos b c:* [p=0.2] três vezes dois, menos um vezes cinco, "
        "[p=0.2] seis menos cinco, [p=0.2] *um.* [p=0.4] {c}Movimento um: [p=0.2] *troca a diagonal principal.* "
        "[p=0.2] O três e o dois trocam de lugar. [p=0.4] {d}Movimento dois: [p=0.2] *muda o sinal da secundária.* "
        "[p=0.2] O um e o cinco ganham um menos. [p=0.4] {e}Movimento três: [p=0.2] *divide tudo* por a d menos b c, "
        "[p=0.2] que é um. [p=0.4] {f}A inversa é *dois, menos um; menos cinco, três.*"),
    dict(id="13", block="confere", text=
        "{t}Será que está certa? [p=0.4] {a}Multiplique pela original. [p=0.2] Três vezes dois, mais um vezes menos "
        "cinco: [p=0.2] *um.* [p=0.4] {b}Três vezes menos um, mais um vezes três: [p=0.2] *zero.* [p=0.4] {c}A "
        "segunda linha dá zero e um. [p=0.2] Apareceu a *identidade:* [p=0.2] confere! [p=0.4] {d}E se a d menos b c "
        "der zero? [p=0.2] Não dá para dividir: [p=0.2] *não há inversa.* [p=0.4] {e}Esse número tem nome e série "
        "própria: [p=0.2] *determinante.*"),
    dict(id="14", block="atalho_receita", text=
        "{t}Atalho para não esquecer. [p=0.4] {a}Três movimentos: [p=0.2] *troca,* [p=0.2] *sinal,* [p=0.2] "
        "*divide.* [p=0.4] {b}Troca na diagonal principal, [p=0.2] sinal na secundária. [p=0.4] {c}E feche sempre "
        "com a *conferência:* [p=0.2] multiplicou pela original, [p=0.2] tem que aparecer a identidade."),

    # ================= BLOCO F: CÓDIGOS =================
    dict(id="15", block="codigo", text=
        "{t}E para que serve isso? [p=0.4] {a}Para guardar segredos. [p=0.2] Cada letra vira um número, [p=0.2] e os "
        "números viram *colunas.* [p=0.4] {b}*Codificar* é trancar: [p=0.2] multiplicar a coluna pela *matriz-chave* "
        "A. [p=0.4] {c}*Decodificar* é destrancar: [p=0.2] quem recebe multiplica por *A inversa* [p=0.2] e recupera "
        "a mensagem. [p=0.4] {d}Errou um sinal na inversa? [p=0.2] A chave não serve, [p=0.2] e sai *lixo.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Calcule a inversa de *dois, um; três, dois* [p=0.2] e *confira.* [p=0.4] {b}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}a d menos b c: [p=0.2] dois vezes dois, menos um vezes três, [p=0.2] quatro "
        "menos três, [p=0.2] *um.* [p=0.4] {b}Troca a diagonal, [p=0.2] muda o sinal "
        "da secundária, [p=0.2] divide por um. [p=0.4] {c}A inversa é *dois, menos um; "
        "menos três, dois.* [p=0.4] {d}Conferindo: [p=0.2] o produto com a original dá *um, zero; zero, um.* [p=0.2] "
        "A identidade."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a ordem dos fatores altera o produto. [p=0.5] "
        "{b}Dois: [p=0.2] produto zero não exige fator zero. [p=0.5] {c}Três: [p=0.2] inversa dois por dois: [p=0.2] "
        "troca a diagonal, [p=0.2] muda o sinal da secundária, [p=0.2] divide por a d menos b c."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] supor que A vezes B *é igual* a B vezes A. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque nos números a ordem nunca importou. [p=0.4] {c}Mas com as matrizes "
        "do começo, [p=0.2] a primeira casa dá sete numa ordem [p=0.2] e *um* na outra."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] concluir de A vezes B igual a zero [p=0.2] que A ou B *é zero.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque nos números essa regra vale sempre. [p=0.4] {c}Nas matrizes, [p=0.2] o exemplo do gancho "
        "derruba: [p=0.2] o produto é nulo [p=0.2] e *nenhum fator é.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] calcular a inversa *só trocando a diagonal.* [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "troca é o movimento que mais aparece. [p=0.4] {c}Em dois, um; três, dois, [p=0.2] trocar a diagonal devolve "
        "*a própria matriz,* [p=0.2] e o produto dá sete, quatro; doze, sete: [p=0.2] *não é a identidade.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="22", block="q4", text=
        "{t}Questão no estilo do ENEM. [p=0.2] *Eu faço com você.* [p=0.4] {a}Considere as matrizes A, [p=0.2] um, "
        "dois; zero, um, [p=0.2] e B, [p=0.2] um, zero; três, um. [p=0.3] A matriz A vezes B, menos B vezes A, é: "
        "[p=0.3] {qa}A: [p=0.2] a matriz nula, pois A vezes B é igual a B vezes A. [p=0.2] {qb}B: [p=0.2] seis, zero; "
        "zero, menos seis. [p=0.2] {qc}C: [p=0.2] menos seis, zero; zero, seis. [p=0.2] {qd}D: [p=0.2] zero, dois; "
        "menos três, zero. [p=0.2] {qe}E: [p=0.2] um, zero; zero, um."),
    dict(id="23", block="q4", text=
        "{t}Vamos lá. [p=0.3] {a}Os dois produtos você já viu: [p=0.2] A B é sete, dois; três, um. [p=0.2] B A é um, "
        "dois; três, sete. [p=0.4] {b}Agora subtraia *casa a casa:* [p=0.2] sete menos um, *seis;* [p=0.2] dois menos "
        "dois, *zero;* [p=0.2] três menos três, *zero;* [p=0.2] um menos sete, *menos seis.* [p=0.4] {ok}*Letra B!*"),
    dict(id="24", block="q4", text=
        "{t}E as erradas? [p=0.3] {xa}A A supõe que A B é igual a B A, [p=0.2] *como nos números.* [p=0.4] {xc}A C "
        "faz a conta *ao contrário:* [p=0.2] B A menos A B. [p=0.4] {xd}A D é A menos B: [p=0.2] subtrai as matrizes "
        "*em vez de multiplicar.* [p=0.4] {xe}E a E é a identidade, [p=0.2] sem relação com a conta."),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="25", block="q9", text=
        "{t}Próxima, [p=0.2] *nós fazemos.* [p=0.4] {a}Um estudante listou afirmações sobre matrizes quadradas A e B "
        "de mesma ordem, [p=0.2] sendo I a identidade e zero a matriz nula. [p=0.3] A única afirmação verdadeira "
        "para quaisquer A e B é: [p=0.3] {qa}A: [p=0.2] A vezes I é igual a I vezes A, igual a A. [p=0.2] {qb}B: "
        "[p=0.2] A vezes B é igual a B vezes A. [p=0.2] {qc}C: [p=0.2] A mais B, ao quadrado, é igual a A ao "
        "quadrado mais dois A B mais B ao quadrado. [p=0.2] {qd}D: [p=0.2] A vezes B, transposta, é igual a A "
        "transposta vezes B transposta. [p=0.2] {qe}E: [p=0.2] se A vezes B é zero, então A é zero ou B é zero. "
        "[p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q9", text=
        "{t}Vamos juntos. [p=0.3] {a}A identidade é o número um das matrizes, [p=0.2] *dos dois lados.* [p=0.2] "
        "{ok}*Letra A!* [p=0.4] {xb}A B cai no bloco da meia e do sapato: [p=0.2] a ordem importa. [p=0.4] {xc}A C "
        "esquece que A B e B A *podem ser diferentes.* [p=0.4] {xd}A D tem a ordem errada: [p=0.2] o certo é B "
        "transposta vezes A transposta. [p=0.4] {xe}E a E cai no exemplo do gancho."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="27", block="q6", text=
        "{t}Agora, [p=0.2] *é com você.* [p=0.4] {a}Um sistema de mensagens converte cada par de letras em uma matriz "
        "coluna M com dois números [p=0.2] e envia E igual a A vezes M, [p=0.2] em que A é três, um; cinco, dois. "
        "[p=0.3] Uma mensagem chegou como E igual a dezessete; vinte e nove. [p=0.3] Os dois números originais, de "
        "cima para baixo, eram: [p=0.3] {qa}A: [p=0.2] dois e cinco. [p=0.2] {qb}B: [p=0.2] menos cinco e menos "
        "dois. [p=0.2] {qc}C: [p=0.2] sessenta e três e cento e setenta e dois. [p=0.2] {qd}D: [p=0.2] cinco e dois. "
        "[p=0.2] {qe}E: [p=0.2] oitenta e cento e quarenta e três. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q6", text=
        "{t}Vamos conferir. [p=0.3] {a}A chave você já conhece: [p=0.2] a inversa de três, um; cinco, dois [p=0.2] é "
        "dois, menos um; menos cinco, três. [p=0.4] {b}Para destrancar, [p=0.2] *A inversa vezes E.* [p=0.2] Dois "
        "vezes dezessete, menos vinte e nove: [p=0.2] *cinco.* [p=0.2] Menos cinco vezes dezessete, mais três vezes "
        "vinte e nove: [p=0.2] *dois.* [p=0.4] {c}Conferindo: [p=0.2] três vezes cinco mais dois dá dezessete; [p=0.2] "
        "cinco vezes cinco mais dois vezes dois dá vinte e nove. [p=0.3] {ok}*Letra D!*"),
    dict(id="29", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *inverte a ordem* dos números. [p=0.4] {xb}A B troca os sinais da "
        "diagonal *principal,* [p=0.2] em vez da secundária. [p=0.4] {xc}A C *só troca a diagonal,* [p=0.2] o erro "
        "três. [p=0.4] {xe}E a E multiplica de novo por A: [p=0.2] *tranca outra vez,* [p=0.2] em vez de destrancar."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a ordem dos fatores altera o produto. [p=0.5] "
        "{b}Dois: [p=0.2] produto zero não exige fator zero. [p=0.5] {c}Três: [p=0.2] inversa dois por dois: [p=0.2] "
        "troca a diagonal, [p=0.2] muda o sinal da secundária, [p=0.2] divide por a d menos b c."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] "
        "{c}e treinamos com *questões inéditas.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual regra dos números você mais se surpreendeu ao ver falhar nas "
        "matrizes? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
