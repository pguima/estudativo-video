# Roteiro — Matrizes e Operações, Episódio 3 de 5: multiplicação de matrizes, linha por coluna
# Base: Estudos/Enem/estudos/01-matematica/33-matrizes-operacoes.html — seção 05 e a parte da seção 08 sobre a matriz de
#   ligações (A² conta rotas com uma escala) + Questões 3, 2 e 7 (seção 12). AB ≠ BA e a inversa ficam para o episódio 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   LINHA VEZES COLUNA É O CAIXA DO SUPERMERCADO: cada quantidade encontra o seu preço, e o caixa soma tudo num número só.
#   A REGRA DO DOMINÓ: em (2 × 3) · (3 × 2), os números de DENTRO encaixam como peças; os de FORA dão o tamanho.
#   O ENDEREÇO DO RESULTADO diz quem multiplica quem: c_21 é a linha 2 da primeira com a coluna 1 da segunda.
#   (retomadas: o ASSENTO DO CINEMA do ep. 1 — fileira, depois poltrona — e as FOLHAS TRANSPARENTES do ep. 2, casa a casa)
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula"
#   (o resto da frase é o do prompt).
# Blocos = seção 05: filial (10, 5, 4) × fornecedor (5, 9, 8) = 127 (o gancho e o bloco a usam o c_11 da Q2, que é
#   "nós fazemos" — desenho do prompt, mantido); (1 2 3 / 0 1 4) · (2 4 / 1 0 / 0 5) = (4 19 / 1 20).
# Exemplos NOSSOS (marcados), para não entregar a Questão 7 ("você faz"):
#   bloco e: voos 1→2, 1→4, 2→3, 3→1, 4→2 → (B²)_13 = 0 + 1·1 + 0 + 1·0 = 1 (rota 1→2→3; a 4 recebe voo da 1, mas não voa
#   para a 3). O mapa da Q7, com as rotas 1→2→4 e 1→3→4 acendendo, só aparece na resolução, depois da pausa.
#   bloco d: "quanto a filial 2 gasta no fornecedor 1" só como endereço (c_21 = linha 2 com coluna 1), sem números.
#   erro 1: (1 2 / 3 4) · (5 6 / 7 8): casa a casa daria (5 12 / 21 32); o certo é (19 22 / 43 50).
# Nós fazemos (prompt): (2 1 / 0 3) · (1 / 4) → (2 × 2)(2 × 1) = 2 × 1 → (6 / 12).
# Atalhos (verde): o dominó ANTES da conta (escreva as ordens: dentro iguais? fora = tamanho) · calcule só a casa pedida ·
#   em A², deite a linha i sobre a coluna j e conte os encontros 1 com 1 · conferência de plausibilidade em contexto.
# QUESTÃO 3 (texto idêntico na tela): (2 × 3)(3 × 4) = 2 × 4; (2 × 4)(4 × 2) = 2 × 2 → E. Material: A para no primeiro
#   produto; D supõe ordens iguais. Explicação NOSSA das B e C (o material só diz "usa os de dentro" e "B e C trocados"):
#   B (3 × 3) = os números de dentro do 1º produto; C (4 × 4) = os de dentro do 2º produto.
# QUESTÃO 2 (texto idêntico): Q · P = (127 131 / 110 108); filial 1 em X (127), filial 2 em Y (108): 235 → B.
#   Erradas como o material: A (215 = 117 + 98) mistura fornecedores, o que o enunciado PROÍBE; C (237) manda as duas para X;
#   D (239) as duas para Y; E (241) soma as piores opções.
# QUESTÃO 7 (texto idêntico): (A²)_14 = 0·0 + 1·1 + 1·1 + 0·0 = 2 (rotas 1→2→4 e 1→3→4) → C. Erradas como o material e os
#   "Cuidados": A (0) lê o voo direto a_14; B (1) é o número de rotas com DUAS escalas (1→2→3→4); D (3) soma as rotas com
#   uma e com duas escalas; E (4) soma a linha 1 inteira de A².
# Frases-chave (meio e fim, idênticas): 1. Linha da primeira vezes coluna da segunda, e soma.
#   2. Os números de dentro encaixam; os de fora dão o tamanho. 3. c_ij é a linha i com a coluna j.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Multiplicar matrizes do zero: linha por coluna · Matemática ENEM, Matrizes episódio 3"

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
        "{a}Dez vezes cinco, [p=0.2] mais cinco vezes nove, [p=0.2] mais quatro vezes oito: [p=0.2] *cento e vinte e "
        "sete.* [p=0.4] {b}É o gasto de uma filial de restaurante num fornecedor. [p=0.4] {c}Essa conta de *cupom de "
        "supermercado* [p=0.2] é, sozinha, [p=0.2] *toda a multiplicação de matrizes.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber se um produto de matrizes *existe,* [p=0.3] {b}qual o *tamanho* "
        "dele [p=0.3] {c}e o que cada número do resultado *significa* no problema."),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete do episódio um. [p=0.3] {a}O endereço *a, i, j* é o assento do cinema: [p=0.2] primeiro "
        "a *fileira,* a linha; [p=0.2] depois a *poltrona,* a coluna. [p=0.4] {b}E numa tabela, [p=0.2] a *linha* diz "
        "*quem;* [p=0.2] a *coluna* diz *o quê.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense no caixa do supermercado. [p=0.3] {a}Dez quilos de arroz, [p=0.2] cinco de feijão, [p=0.2] quatro "
        "litros de óleo. [p=0.4] {b}Preços: [p=0.2] cinco, [p=0.2] nove [p=0.2] e oito reais. [p=0.4] {c}Cada "
        "quantidade encontra o *seu* preço: [p=0.2] dez vezes cinco, [p=0.2] cinco vezes nove, [p=0.2] quatro vezes "
        "oito. [p=0.4] {d}E o caixa *soma tudo* num número só: [p=0.2] *cento e vinte e sete reais.*"),

    # ================= BLOCO A: POR QUE A REGRA É ESTRANHA =================
    dict(id="05", block="estranha", text=
        "{t}E onde estão as matrizes nisso? [p=0.4] {a}A compra, *deitada:* [p=0.2] uma *linha.* [p=0.4] {b}Os preços, "
        "*em pé:* [p=0.2] uma *coluna.* [p=0.4] {c}O cupom é *linha vezes coluna:* [p=0.2] primeiro com primeiro, "
        "[p=0.2] segundo com segundo, [p=0.2] e soma. [p=0.4] {d}Não é casa com casa, [p=0.2] como as folhas "
        "transparentes da soma. [p=0.2] É o *caixa do supermercado.*"),

    # ================= BLOCO B: A REGRA =================
    dict(id="06", block="regra", text=
        "{t}Então, qual é a regra? [p=0.4] {a}O *produto de matrizes* [p=0.2] é a multiplicação de uma matriz por "
        "outra: [p=0.2] *A vezes B.* [p=0.4] {b}Cada casa do resultado, [p=0.2] a *c, i, j,* [p=0.2] é a *linha i* de A "
        "[p=0.2] vezes a *coluna j* de B, [p=0.2] termo a termo, e soma. [p=0.4] {c}O caixa, [p=0.2] feito para cada "
        "casa."),
    dict(id="07", block="regra", text=
        "{t}Vamos ver funcionando, [p=0.2] com as duas matrizes da tela. [p=0.4] {a}A primeira é dois por três; [p=0.2] "
        "a segunda, três por dois. [p=0.4] {b}Casa *c um um:* [p=0.2] linha um com coluna um. [p=0.2] Um vezes dois, "
        "[p=0.2] mais dois vezes um, [p=0.2] mais três vezes zero: [p=0.2] *quatro.* [p=0.4] {c}Casa *c um dois:* "
        "[p=0.2] a mesma linha, [p=0.2] com a coluna dois. [p=0.2] Um vezes quatro, [p=0.2] mais dois vezes zero, "
        "[p=0.2] mais três vezes cinco: [p=0.2] *dezenove.*"),
    dict(id="08", block="regra", text=
        "{t}Agora a segunda linha. [p=0.3] {a}Casa *c dois um:* [p=0.2] zero vezes dois, [p=0.2] mais um vezes um, "
        "[p=0.2] mais quatro vezes zero: [p=0.2] *um.* [p=0.4] {b}Casa *c dois dois:* [p=0.2] zero vezes quatro, "
        "[p=0.2] mais um vezes zero, [p=0.2] mais quatro vezes cinco: [p=0.2] *vinte.* [p=0.4] {c}Resultado: [p=0.2] "
        "*quatro, dezenove; [p=0.2] um, vinte.* [p=0.4] {d}Repare: [p=0.2] o endereço diz *quem multiplica quem.* "
        "[p=0.2] *C dois um* [p=0.2] é a linha dois da primeira [p=0.2] com a coluna um da segunda."),

    # ================= BLOCO C: QUANDO EXISTE E QUE TAMANHO TEM =================
    dict(id="09", block="ordem", text=
        "{t}Dá para multiplicar *qualquer* matriz por *qualquer* outra? [p=0.4] {a}Não. [p=0.2] Olhe as *ordens:* "
        "[p=0.2] *dois por três* [p=0.2] e *três por dois.* [p=0.4] {b}Ponha lado a lado, [p=0.2] como peças de "
        "*dominó.* [p=0.2] Os números de *dentro* [p=0.2] precisam ser iguais para encaixar. [p=0.4] {c}E os de *fora* "
        "[p=0.2] dão o *tamanho* do resultado: [p=0.2] dois por dois. [p=0.2] Exatamente o que deu."),
    dict(id="10", block="ordem", text=
        "{t}Por que os de dentro têm que ser iguais? [p=0.4] {a}Porque cada quantidade da linha [p=0.2] precisa do seu "
        "preço na coluna. [p=0.4] {b}Tente *três por dois* [p=0.2] vezes *três por dois.* [p=0.2] Dentro: [p=0.2] dois "
        "e três. [p=0.4] {c}Sobra um preço *sem quantidade:* [p=0.2] esse produto *não existe.*"),
    dict(id="11", block="ordem", text=
        "{t}Atalho. [p=0.3] {a}*Antes* de qualquer conta, [p=0.2] escreva as duas ordens lado a lado. [p=0.4] {b}Os de "
        "dentro são diferentes? [p=0.2] Pare: [p=0.2] não existe. [p=0.4] {c}São iguais? [p=0.2] Risque os de dentro: "
        "[p=0.2] os de fora são o tamanho do resultado. [p=0.2] Dez segundos."),

    # ================= BLOCO D: SÓ O ELEMENTO PEDIDO =================
    dict(id="12", block="pedido", text=
        "{t}E se a questão pedir *um* número só? [p=0.4] {a}Compras de duas filiais [p=0.2] vezes preços de dois "
        "fornecedores. [p=0.4] {b}Quanto a *filial dois* gasta no *fornecedor um?* [p=0.4] {c}É a casa *c dois um:* "
        "[p=0.2] linha dois com coluna um. [p=0.4] {d}Atalho: [p=0.2] leia o endereço [p=0.2] e calcule *só* a casa "
        "pedida. [p=0.2] Uma conta, [p=0.2] não quatro."),

    # ================= BLOCO E: MATRIZ DE LIGAÇÕES =================
    dict(id="13", block="ligacoes", text=
        "{t}Agora, uma matriz que conta caminhos. [p=0.4] {a}Quatro cidades e alguns voos diretos. [p=0.4] {b}Na "
        "*matriz de ligações,* [p=0.2] a casa *a, i, j* vale *um* [p=0.2] se tem voo direto de *i* para *j,* [p=0.2] e "
        "*zero* se não tem. [p=0.4] {c}Aqui, a um voa para a dois e para a quatro; [p=0.2] a dois, para a três; [p=0.2] "
        "a três, para a um; [p=0.2] a quatro, para a dois."),
    dict(id="14", block="ligacoes", text=
        "{t}Quantas rotas vão da um à três [p=0.2] com *uma escala,* [p=0.2] uma parada no meio do caminho? [p=0.4] "
        "{b}Quem conta é *A ao quadrado,* [p=0.2] a matriz vezes ela mesma. [p=0.2] Casa um três: [p=0.2] linha um com "
        "coluna três. [p=0.4] {c}Zero vezes zero, [p=0.2] mais *um vezes um,* [p=0.2] mais zero vezes zero, [p=0.2] "
        "mais um vezes zero. [p=0.4] {d}O *um vezes um* é a rota um, dois, três. [p=0.2] A quatro recebe voo da um, "
        "[p=0.2] mas *não* voa para a três: [p=0.2] zero. [p=0.2] *Uma* rota."),
    dict(id="15", block="ligacoes", text=
        "{t}Atalho para as rotas. [p=0.3] {a}*Deite* a linha da partida em cima da coluna da chegada [p=0.2] {b}e "
        "*conte* os encontros de *um* com *um.* [p=0.2] Cada encontro é uma escala. [p=0.4] {c}A casa de *A* é o voo "
        "*direto;* [p=0.2] a de *A ao quadrado* [p=0.2] conta as rotas com *uma* escala."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto é a matriz *dois, um; zero, três* [p=0.2] vezes a coluna *um, quatro?* [p=0.4] "
        "{b}E qual é a *ordem* do resultado? [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O dominó: [p=0.2] dois por *dois* vezes *dois* por um. [p=0.2] Encaixa, [p=0.2] e "
        "o resultado é *dois por um,* [p=0.2] uma coluna. [p=0.4] {b}Linha um: [p=0.2] dois vezes um, [p=0.2] mais um "
        "vezes quatro: [p=0.2] *seis.* [p=0.4] {c}Linha dois: [p=0.2] zero vezes um, [p=0.2] mais três vezes quatro: "
        "[p=0.2] *doze.* [p=0.4] {d}A coluna *seis, doze.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] linha da primeira vezes coluna da segunda, e soma. "
        "[p=0.5] {b}Dois: [p=0.2] os números de dentro encaixam; [p=0.2] os de fora dão o tamanho. [p=0.5] {c}Três: "
        "[p=0.2] *c i j* é a linha *i* com a coluna *j.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] multiplicar *posição com posição.* [p=0.2] Um, "
        "dois; três, quatro [p=0.2] vezes cinco, seis; sete, oito [p=0.2] daria cinco, doze; vinte e um, trinta e dois. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque na *soma* é casa com casa. [p=0.4] {c}Mas o produto é linha vezes "
        "coluna: [p=0.2] o certo está na tela."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *dois por três* vezes *dois por três* existe. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque as duas têm o *mesmo tamanho,* [p=0.2] como a soma exige. [p=0.4] {c}Mas olhe o dominó: [p=0.2] dentro, "
        "*três* e *dois.* [p=0.2] Não encaixa."),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="21", block="q3", text=
        "{t}Agora, questões do nosso material, no estilo do ENEM. [p=0.2] Esta, eu resolvo com você. [p=0.4] {a}Um "
        "programa de planilhas guarda três tabelas como matrizes: [p=0.2] *A,* com duas linhas e três colunas; [p=0.2] "
        "*B,* com três linhas e quatro colunas; [p=0.2] e *C,* com quatro linhas e duas colunas. [p=0.2] Um usuário "
        "pede o produto *A vezes B vezes C,* [p=0.2] nessa ordem. [p=0.2] O resultado será: [p=0.4] {qa}A: [p=0.2] uma "
        "matriz dois por quatro. [p=0.3] {qb}B: [p=0.2] três por três. [p=0.3] {qc}C: [p=0.2] quatro por quatro. "
        "[p=0.3] {qd}D: [p=0.2] inexistente, [p=0.2] pois as ordens não são compatíveis. [p=0.3] {qe}E: [p=0.2] uma "
        "matriz dois por dois."),
    dict(id="22", block="q3", text=
        "{t}Uma peça de cada vez. [p=0.4] {a}*A vezes B:* [p=0.2] dois por *três* com *três* por quatro. [p=0.2] "
        "Encaixa, [p=0.2] e dá *dois por quatro.* [p=0.4] {b}Isso vezes *C:* [p=0.2] dois por *quatro* com *quatro* por "
        "dois. [p=0.2] Encaixa de novo: [p=0.2] *dois por dois.* [p=0.3] {ok}*Letra E!*"),
    dict(id="23", block="q3", text=
        "{t}E as outras? [p=0.3] {xa}A A, dois por quatro, [p=0.2] *parou no primeiro produto.* [p=0.4] {xb}A B usou os "
        "de *dentro* do primeiro produto; [p=0.2] {xc}a C, os de dentro do segundo. [p=0.2] O tamanho vem dos de "
        "*fora.* [p=0.4] {xd}E a D exige a mesma ordem para as três. [p=0.2] Basta os *vizinhos* encaixarem."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="24", block="q2", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Duas filiais de um restaurante compram arroz, feijão e óleo. "
        "[p=0.2] As quantidades estão na matriz *Q:* [p=0.2] filial um, [p=0.2] dez, cinco, quatro; [p=0.2] filial "
        "dois, [p=0.2] oito, seis, dois. [p=0.4] {b}Os preços de dois fornecedores, *X* e *Y,* [p=0.2] estão nas "
        "colunas da matriz *P:* [p=0.2] X, cinco, nove, oito; [p=0.2] Y, seis, sete, nove. [p=0.4] {c}Cada filial "
        "compra tudo em *um único* fornecedor, [p=0.2] o que lhe sai mais barato. [p=0.2] O gasto total das duas "
        "filiais é: [p=0.4] {qa}A: [p=0.2] duzentos e quinze reais. [p=0.3] {qb}B: [p=0.2] duzentos e trinta e cinco. "
        "[p=0.3] {qc}C: [p=0.2] duzentos e trinta e sete. [p=0.3] {qd}D: [p=0.2] duzentos e trinta e nove. [p=0.3] "
        "{qe}E: [p=0.2] duzentos e quarenta e um. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q2", text=
        "{t}O dominó: [p=0.2] dois por *três* vezes *três* por dois [p=0.2] dá *dois por dois.* [p=0.4] {a}Linha da "
        "*filial,* [p=0.2] coluna do *fornecedor:* [p=0.2] *c i j* é o gasto da filial *i* no fornecedor *j.* [p=0.4] "
        "{b}Filial um no X: [p=0.2] *cento e vinte e sete,* a conta do gancho. [p=0.2] No Y: [p=0.2] *cento e trinta e "
        "um.* [p=0.4] {c}Filial dois no X: [p=0.2] *cento e dez.* [p=0.2] No Y: [p=0.2] quarenta e oito, mais quarenta "
        "e dois, mais dezoito: [p=0.2] *cento e oito.*"),
    dict(id="26", block="q2", text=
        "{t}Cada filial escolhe o *seu* mais barato: [p=0.4] {a}a um no X, cento e vinte e sete; [p=0.2] a dois no Y, "
        "cento e oito. [p=0.4] {b}Total: [p=0.2] *duzentos e trinta e cinco.* [p=0.3] {ok}*Letra B!* [p=0.4] {xa}A "
        "armadilha é a A, [p=0.2] duzentos e quinze: [p=0.2] mistura os fornecedores, [p=0.2] pegando o item mais "
        "barato de cada um, [p=0.2] e o enunciado *proíbe.* [p=0.4] {xc}A C manda as duas para o X; [p=0.2] {xd}a D, "
        "para o Y; [p=0.2] {xe}a E soma as *piores* opções."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="27", block="q7", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma companhia aérea atende quatro cidades. [p=0.2] Na matriz A, [p=0.2] a casa "
        "*a i j* vale um [p=0.2] se há voo direto da cidade *i* para a cidade *j,* [p=0.2] e zero caso contrário. "
        "[p=0.4] {b}O elemento da linha um e coluna quatro de *A ao quadrado* [p=0.2] indica o número de maneiras de ir "
        "da cidade um à quatro [p=0.2] com exatamente *uma escala.* [p=0.2] Esse número é: [p=0.4] {qa}A: [p=0.2] zero. "
        "[p=0.3] {qb}B: [p=0.2] um. [p=0.3] {qc}C: [p=0.2] dois. [p=0.3] {qd}D: [p=0.2] três. [p=0.3] {qe}E: [p=0.2] "
        "quatro. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q7", text=
        "{t}Conferindo: [p=0.2] linha um de A com a coluna quatro de A. [p=0.4] {a}Zero vezes zero, [p=0.2] mais *um "
        "vezes um,* [p=0.2] mais *um vezes um,* [p=0.2] mais zero vezes zero: [p=0.2] *dois.* [p=0.4] {b}No mapa: "
        "[p=0.2] *um, dois, quatro* [p=0.3] {c}e *um, três, quatro.* [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A, zero, [p=0.2] leu o voo *direto,* a casa de A. [p=0.4] {xb}A B, um, [p=0.2] "
        "conta as rotas com *duas* escalas: [p=0.2] um, dois, três, quatro. [p=0.4] {xd}A D soma as duas contagens. "
        "[p=0.4] {xe}E a E, quatro, [p=0.2] somou a linha um inteira de A ao quadrado: [p=0.2] rotas para *qualquer* "
        "destino."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] linha da primeira vezes coluna da segunda, e "
        "soma. [p=0.5] {b}Dois: [p=0.2] os números de dentro encaixam; [p=0.2] os de fora dão o tamanho. [p=0.5] "
        "{c}Três: [p=0.2] *c i j* é a linha *i* com a coluna *j.*"),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Com números, [p=0.2] dois vezes três é igual a três vezes dois. [p=0.2] Com matrizes, [p=0.2] *A B* é igual "
        "a *B A?* [p=0.5] {b}E dá para *desfazer* uma multiplicação, [p=0.2] como a divisão desfaz a multiplicação? "
        "[p=0.5] {c}Próximo episódio."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já sabia que o cupom do mercado é uma multiplicação de matrizes? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
