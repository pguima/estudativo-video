# Roteiro — Matrizes e Operações, Episódio 1 de 5: matriz é uma tabela com endereço
# Base: Estudos/Enem/estudos/01-matematica/33-matrizes-operacoes.html — seções 02, 03 e a parte da 08 sobre tabelas de
#   distâncias, de jogos e imagens digitais + Questões 1 e 5 (seção 12). A² (rotas com escala) fica para o episódio 3.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   a_ij é o ASSENTO DO CINEMA: primeiro a FILEIRA (linha), depois a POLTRONA (coluna).
#   Tabela de estrada de mão dupla é um ESPELHO: a diagonal principal é o espelho.
#   No campeonato, a LINHA conta o que o time fez; a COLUNA conta o que fizeram contra ele.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula"
#   (o resto da frase é o do prompt).
# Exemplos NOSSOS (para não usar os números das questões antes da hora):
#   cinema/endereço: matriz 3 × 4 com a_23 = 9 e a_32 = 3 (os valores que o material cita do cabeçalho, numa matriz nossa);
#   distâncias: 3 cidades, d_13 apagado = 120 pelo espelho (a Q5 é "você faz");
#   gols: 3 times, G = (0 3 2 / 1 0 0 / 1 2 0) → saldos +3, −4, +1 (soma zero); "3 a 1" = g_12 e g_21.
#   pixels: figura em L 5 × 5 (inverter e transpor).
#   Erro 1 usa a matriz da lei 2i − j: na 2 × 3 nem existe a_32. Erro 3 usa os 3 times.
# O gancho usa a Q1 (time 3: saldo −3; "coluna − linha" dá +3), que é a "eu faço" — permitido.
# Nós fazemos (prompt): a_ij = i + 2j → a_21 = 4, a_12 = 5.
# Atalhos (verde): lei de formação andando pela linha (2i − j: na linha cai 1, na coluna sobe 2) · transposta: a 1ª linha
#   vira a 1ª coluna · simetria: só precisa da metade · rotule antes de somar (linha = feitos) · conferência "saldos somam zero".
# QUESTÃO 1 (texto idêntico na tela): saldos +2, 0, −3, +1 (soma zero) → A. Material: B = só quem mais marcou;
#   C = "coluna − linha" (time 3 com +3); E = compara só os gols marcados de 1 e 4. Explicação da D é NOSSA (o material só
#   diz "erra a coluna 4"): quem esquece o 2 da coluna 4 acha que o time 4 sofreu só 2 gols e fica com +3.
# QUESTÃO 5 (texto idêntico): x = d_31 = 150, y = d_42 = 140; 150 + 90 + 140 = 380 → C. Erradas como o material e o prompt:
#   A (240) trata y como zero; B (350) copia o vizinho da linha (120); D (440) usa a distância 1–4 (200); E (580) soma a volta.
# Frases-chave (meio e fim, idênticas): 1. Primeiro a linha, depois a coluna. 2. Tabela de mão dupla é simétrica: a diagonal
#   é o espelho. 3. Linha é o que o time fez; coluna é o que ele sofreu.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Matriz do zero: a tabela com endereço · Matemática ENEM, Matrizes episódio 1"

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
        "{a}Numa tabela de gols, [p=0.2] quem troca *linha* por *coluna* [p=0.3] {b}transforma o time com o *pior* saldo "
        "do campeonato, [p=0.2] *menos três,* [p=0.3] {c}num líder com *mais três.* [p=0.5] {d}A conta estava certa; "
        "[p=0.3] a *leitura,* não."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai ler qualquer tabela em forma de matriz [p=0.2] *sem trocar o "
        "endereço* [p=0.3] {b}e vai reconhecer os *tipos de matriz* que aparecem nos enunciados."),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido. [p=0.3] {a}Da série de Operações: [p=0.2] conta com sinal. [p=0.2] Dois menos "
        "cinco [p=0.2] dá *menos três:* [p=0.2] quando tira mais do que tem, [p=0.2] o resultado fica *negativo.* "
        "[p=0.4] {b}Vai servir já já, [p=0.2] porque saldo de gols [p=0.2] pode ser negativo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três coisas do dia a dia. [p=0.3] {a}A *tabela de classificação* de um campeonato. [p=0.4] {b}A "
        "*tabela de distâncias* entre cidades, [p=0.2] daquelas de guia rodoviário. [p=0.4] {c}E uma *foto do "
        "celular* ampliada [p=0.2] até aparecerem os quadradinhos. [p=0.4] {d}As três são números "
        "arrumados em *linhas e colunas.* [p=0.3] E isso tem nome: [p=0.2] *matriz.*"),

    # ================= BLOCO A: DA TABELA À MATRIZ =================
    dict(id="05", block="definicao", text=
        "{t}E o que é, exatamente, uma matriz? [p=0.4] {a}*Matriz* é uma tabela de números [p=0.2] arrumados em "
        "linhas e colunas. [p=0.4] {b}*Linha* é a fileira deitada, [p=0.2] na horizontal. [p=0.2] *Coluna* é a "
        "fileira em pé, [p=0.2] na vertical. [p=0.4] {c}E a *ordem* da matriz [p=0.2] diz o tamanho dela: [p=0.2] "
        "*m por n,* [p=0.2] *m* linhas e *n* colunas. [p=0.4] {d}Esta tem duas linhas e três colunas: [p=0.2] é uma "
        "*dois por três.* [p=0.2] Sempre as linhas primeiro."),

    # ================= BLOCO B: O ENDEREÇO =================
    dict(id="06", block="endereco", text=
        "{t}E como se aponta para um número lá dentro? [p=0.4] {a}Cada número da matriz é um *elemento,* [p=0.2] e "
        "tem um endereço: [p=0.2] *a, i, j.* [p=0.4] {b}O *i* é a linha. [p=0.2] O *j* é a coluna. [p=0.4] {c}Pense "
        "no *assento do cinema:* [p=0.2] primeiro a *fileira,* [p=0.2] depois a *poltrona.* [p=0.4] {d}*A dois três* "
        "[p=0.2] é fileira dois, [p=0.2] poltrona três. [p=0.2] Aqui, [p=0.2] o *nove.*"),
    dict(id="07", block="endereco", text=
        "{t}E se eu trocar a ordem? [p=0.4] {a}*A três dois* [p=0.2] é fileira três, [p=0.2] poltrona dois. [p=0.2] "
        "Outro lugar, [p=0.2] outro número: [p=0.2] o *três.* [p=0.4] {b}Fileira dois, poltrona três [p=0.2] *não é* "
        "o mesmo lugar que fileira três, poltrona dois. [p=0.4] {c}Por isso, [p=0.2] em todo endereço: [p=0.2] "
        "*primeiro a linha, depois a coluna.*"),

    # ================= BLOCO C: LEI DE FORMAÇÃO =================
    dict(id="08", block="lei", text=
        "{t}E quando a matriz vem sem os números, [p=0.2] só com uma fórmula? [p=0.4] {a}Essa fórmula é a *lei de "
        "formação:* [p=0.2] a receita que diz quanto vale cada endereço. [p=0.4] {b}Exemplo: [p=0.2] *a i j igual a "
        "dois i menos j,* [p=0.2] numa matriz dois por três. [p=0.4] {c}É só trocar o i pela linha [p=0.2] e o j "
        "pela coluna. [p=0.2] *A um um:* [p=0.2] dois vezes um, [p=0.2] menos um: [p=0.2] *um.* [p=0.2] *A um dois:* "
        "[p=0.2] dois menos dois, [p=0.2] *zero.* [p=0.2] *A um três:* [p=0.2] *menos um.* "
        "[p=0.4] {d}Na linha dois, [p=0.2] o dois i vale quatro: [p=0.2] *três, dois, um.*"),
    dict(id="09", block="lei", text=
        "{t}Tem um jeito de montar mais rápido? [p=0.3] Tem. [p=0.3] {a}Atalho: [p=0.2] calcule *só o primeiro,* "
        "[p=0.2] e ande pela regra. [p=0.4] {b}Em dois i menos j, [p=0.2] cada passo para a *direita* [p=0.2] aumenta "
        "o j: [p=0.2] o valor *cai um.* [p=0.4] {c}Cada passo para *baixo* [p=0.2] aumenta o i: [p=0.2] o valor *sobe "
        "dois.* [p=0.4] {d}Um, zero, menos um; [p=0.2] e embaixo, [p=0.2] três, dois, um. [p=0.2] A mesma matriz, "
        "[p=0.2] quase sem conta."),

    # ================= BLOCO D: OS TIPOS =================
    dict(id="10", block="tipos", text=
        "{t}E aqueles nomes que aparecem nos enunciados? [p=0.4] {a}*Matriz quadrada* [p=0.2] tem o mesmo número de "
        "linhas e de colunas. [p=0.4] {b}Ela tem a *diagonal principal:* [p=0.2] a que desce da esquerda para a "
        "direita, [p=0.2] onde a linha é igual à coluna. [p=0.4] {c}E a *diagonal secundária:* [p=0.2] a outra, "
        "[p=0.2] que sobe."),
    dict(id="11", block="tipos", text=
        "{t}E as famílias de matriz quadrada? [p=0.3] {a}*Nula:* [p=0.2] todos os elementos "
        "iguais a zero. [p=0.4] {b}*Diagonal:* [p=0.2] zero em tudo fora da diagonal principal. [p=0.4] "
        "{c}*Identidade:* [p=0.2] uma diagonal com *um* em toda a diagonal principal. [p=0.4] {d}E *triangular:* "
        "[p=0.2] zeros de *um* dos lados da diagonal principal."),
    dict(id="12", block="tipos", text=
        "{t}E a tal da transposta? [p=0.4] {a}A *transposta* [p=0.2] troca as linhas pelas colunas. [p=0.4] {b}Esta "
        "matriz tem as linhas um, dois, três [p=0.2] e quatro, cinco, seis. [p=0.2] Na transposta, [p=0.2] elas viram "
        "as *colunas.* [p=0.4] {c}Atalho: [p=0.2] a *primeira linha* vira a *primeira coluna.* [p=0.4] {d}Repare no "
        "tamanho: [p=0.2] a dois por três [p=0.2] virou uma *três por dois.*"),
    dict(id="13", block="tipos", text=
        "{t}E quando a transposta dá a mesma matriz? [p=0.4] {a}Aí ela é *simétrica:* [p=0.2] igual à própria "
        "transposta. [p=0.4] {b}Olhe: [p=0.2] oito acima da diagonal, [p=0.2] oito abaixo. [p=0.2] Cinco e cinco. "
        "[p=0.2] Três e três. [p=0.4] {c}A diagonal principal funciona como um *espelho:* [p=0.2] o que está de um "
        "lado [p=0.2] se repete do outro."),

    # ================= BLOCO E: O ENDEREÇO TEM SIGNIFICADO =================
    dict(id="14", block="contexto", text=
        "{t}E onde esse espelho aparece na prova? [p=0.4] {a}Na tabela de *distâncias.* [p=0.2] *D um três* [p=0.2] "
        "é a distância da cidade um até a cidade três. [p=0.4] {b}Estrada de mão dupla: [p=0.2] de um até três "
        "[p=0.2] é o mesmo que de três até um. [p=0.2] A tabela é *simétrica.* [p=0.4] {c}A diagonal é *zero:* "
        "[p=0.2] de uma cidade até ela mesma. [p=0.4] {d}E se um valor sumiu, [p=0.2] *copie do espelho:* [p=0.2] o "
        "d um três apagado [p=0.2] é o d três um, [p=0.2] *cento e vinte.*"),
    dict(id="15", block="contexto", text=
        "{t}E a tabela de gols? [p=0.2] Também é um espelho? [p=0.4] {a}*G i j* [p=0.2] são os gols que o time *i* "
        "marcou contra o time *j.* [p=0.4] {b}Então a *linha* conta o que o time *fez,* [p=0.2] e a *coluna* conta o "
        "que fizeram *contra ele.* [p=0.4] {c}O *saldo* é linha menos coluna. [p=0.2] Time um: [p=0.2] marcou cinco, "
        "sofreu dois: [p=0.2] *mais três.* [p=0.4] {d}E ela *não* é simétrica: [p=0.2] o time um fez três no dois, "
        "[p=0.2] o dois fez um no um. [p=0.2] Três a um [p=0.2] *não é* um a três."),
    dict(id="16", block="contexto", text=
        "{t}Antes de somar, [p=0.2] um atalho. [p=0.4] {a}*Rotule:* [p=0.2] escreva ao lado da "
        "matriz [p=0.2] o que é linha [p=0.2] e o que é coluna. [p=0.4] {b}E confira no fim: [p=0.2] todo gol "
        "marcado por um time [p=0.2] é sofrido por outro. [p=0.2] Então os saldos [p=0.2] *somam zero.* [p=0.4] {c}Mais "
        "três, [p=0.2] menos quatro, [p=0.2] mais um: [p=0.2] zero. [p=0.2] Fechou."),

    # ================= BLOCO F: IMAGEM DIGITAL =================
    dict(id="17", block="pixels", text=
        "{t}E a foto ampliada do começo? [p=0.4] {a}Cada quadradinho é um *pixel:* [p=0.2] o menor ponto da imagem. "
        "[p=0.2] E cada pixel é um elemento da matriz. [p=0.4] {b}Numa imagem em preto e branco, [p=0.2] *um* é "
        "pixel aceso; [p=0.2] *zero,* apagado. [p=0.4] {c}Trocar todo um por zero [p=0.2] *inverte as cores.* "
        "[p=0.4] {d}E a transposta [p=0.2] *espelha a figura* na diagonal: [p=0.2] a primeira linha vira a primeira "
        "coluna."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Na matriz dois por dois [p=0.2] com *a i j igual a i mais dois j,* [p=0.2] quanto "
        "vale *a dois um?* [p=0.2] E *a um dois?* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}*A dois um:* [p=0.2] linha dois, coluna um. [p=0.2] Dois mais duas vezes um: "
        "[p=0.2] *quatro.* [p=0.4] {b}*A um dois:* [p=0.2] linha um, coluna dois. [p=0.2] Um mais duas vezes dois: "
        "[p=0.2] *cinco.* [p=0.4] {c}Endereços trocados, [p=0.2] valores *diferentes.* [p=0.2] Primeiro a linha, "
        "[p=0.2] sempre."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primeiro a linha, depois a coluna. [p=0.5] {b}Dois: "
        "[p=0.2] tabela de mão dupla é simétrica: [p=0.2] a diagonal é o espelho. [p=0.5] {c}Três: [p=0.2] linha é o "
        "que o time fez; [p=0.2] coluna é o que ele sofreu."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler *a dois três* [p=0.2] como linha três, "
        "coluna dois. [p=0.4] {b}Parece certo, [p=0.2] porque os dois números estão ali, [p=0.2] e a ordem parece "
        "detalhe. [p=0.4] {c}Mas na nossa matriz dois por três, [p=0.2] *nem existe* linha três. [p=0.2] O primeiro "
        "índice é *sempre* a linha."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] achar que a transposta de uma dois por três [p=0.2] continua *dois por três.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque os números são os mesmos. [p=0.4] {c}Mas as linhas viraram colunas: [p=0.2] "
        "o tamanho *gira junto.* [p=0.2] Vira três por dois."),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] tomar a *coluna* como gols marcados. [p=0.4] {b}Parece certo, [p=0.2] porque a soma "
        "da coluna parece tão boa quanto a da linha. [p=0.4] {c}Mas aí o time um, [p=0.2] que fez cinco e "
        "sofreu dois, [p=0.2] ficaria com *menos três.* [p=0.2] Rotule antes: [p=0.2] *linha é o que o time fez.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="24", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta primeira, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Em um torneio entre quatro times, [p=0.2] os gols foram registrados na matriz "
        "*G,* [p=0.2] em que *g i j* é o número de gols que o time *i* marcou contra o time *j.* [p=0.2] A diagonal é "
        "zero, [p=0.2] pois um time não joga contra si mesmo. [p=0.2] O saldo de gols é a diferença entre gols "
        "marcados e gols sofridos. [p=0.2] O time com o maior saldo de gols é: [p=0.4] {qa}A: [p=0.2] o time um. "
        "[p=0.3] {qb}B: [p=0.2] o time dois. [p=0.3] {qc}C: [p=0.2] o time três. [p=0.3] {qd}D: [p=0.2] o time "
        "quatro. [p=0.3] {qe}E: [p=0.2] os times um e quatro, empatados."),
    dict(id="25", block="q1", text=
        "{t}Primeiro, os rótulos. [p=0.2] {a}Linha: [p=0.2] gols *marcados.* [p=0.2] Coluna: [p=0.2] gols "
        "*sofridos.* [p=0.4] {b}Time um: [p=0.2] a linha soma cinco, [p=0.2] a coluna soma três. [p=0.2] Saldo *mais "
        "dois.* [p=0.4] {c}Time dois: [p=0.2] sete e sete, [p=0.2] *zero.* [p=0.2] Time três: [p=0.2] dois e cinco, "
        "[p=0.2] *menos três.* [p=0.2] Time quatro: [p=0.2] cinco e quatro, [p=0.2] *mais um.* [p=0.4] {d}Conferência: "
        "[p=0.2] mais dois, zero, menos três, mais um: [p=0.2] soma *zero.* [p=0.2] O maior saldo é do time um. [p=0.3] "
        "{ok}*Letra A!*"),
    dict(id="26", block="q1", text=
        "{t}E as outras? [p=0.3] {xc}A C [p=0.2] fez *coluna menos linha:* [p=0.2] trocou o endereço, [p=0.2] e o "
        "time três, [p=0.2] o pior do torneio, [p=0.2] virou *mais três.* [p=0.4] {xb}A B "
        "[p=0.2] escolheu só quem *mais marcou,* [p=0.2] o time dois, [p=0.2] e esqueceu os gols sofridos. [p=0.4] "
        "{xe}A E [p=0.2] comparou só os gols marcados dos times um e quatro, [p=0.2] cinco a cinco. [p=0.4] {xd}E a D "
        "[p=0.2] esqueceu um número da coluna quatro: [p=0.2] o time quatro sofreu quatro gols, [p=0.2] não dois."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="27", block="q5", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma transportadora registra as distâncias rodoviárias, em quilômetros, entre "
        "quatro cidades na matriz *D,* [p=0.2] em que *d i j* é a distância entre as cidades *i* e *j.* [p=0.2] As "
        "estradas são de mão dupla, [p=0.2] e dois valores foram apagados. [p=0.2] Um caminhão faz o trajeto [p=0.2] "
        "*um, três, dois, quatro,* [p=0.2] sem voltar. [p=0.2] A distância percorrida, em quilômetros, é: [p=0.4] "
        "{qa}A: [p=0.2] duzentos e quarenta. [p=0.3] {qb}B: [p=0.2] trezentos e cinquenta. [p=0.3] {qc}C: [p=0.2] "
        "trezentos e oitenta. [p=0.3] {qd}D: [p=0.2] quatrocentos e quarenta. [p=0.3] {qe}E: [p=0.2] quinhentos e "
        "oitenta. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{t}Conferindo. [p=0.2] {a}Mão dupla: [p=0.2] a matriz é *simétrica.* [p=0.2] O x está na linha um, coluna "
        "três: [p=0.2] *copie do espelho,* [p=0.2] o d três um, [p=0.2] *cento e cinquenta.* [p=0.4] {b}O y está na "
        "linha dois, coluna quatro: [p=0.2] o espelho é o d quatro dois, [p=0.2] *cento e quarenta.* [p=0.4] {c}O "
        "trajeto: [p=0.2] de um a três, cento e cinquenta; [p=0.2] de três a dois, noventa; [p=0.2] de dois a "
        "quatro, cento e quarenta. [p=0.2] Total: [p=0.2] *trezentos e oitenta.* [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q5", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] achou o x, [p=0.2] mas tratou o y apagado como *zero.* [p=0.4] "
        "{xb}A B [p=0.2] copiou o x do *vizinho da linha,* [p=0.2] cento e vinte, [p=0.2] em vez do espelho. [p=0.4] "
        "{xd}A D [p=0.2] usou a distância de um a quatro, [p=0.2] duzentos, [p=0.2] no lugar do y. [p=0.4] {xe}E a E "
        "[p=0.2] somou a *volta* de quatro para um, [p=0.2] que o enunciado proibiu."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro a linha, depois a coluna. [p=0.5] "
        "{b}Dois: [p=0.2] tabela de mão dupla é simétrica: [p=0.2] a diagonal é o espelho. [p=0.5] {c}Três: [p=0.2] "
        "linha é o que o time fez; [p=0.2] coluna é o que ele sofreu."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Se uma matriz tem as notas da *prova um* [p=0.2] e outra as da *prova dois,* [p=0.3] {b}dá para calcular "
        "as médias da turma inteira *de uma vez?* [p=0.5] {c}Dá, [p=0.2] e a conta é *casa com casa.* [p=0.4] "
        "{d}Próximo episódio."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha trocado linha por coluna numa tabela? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
