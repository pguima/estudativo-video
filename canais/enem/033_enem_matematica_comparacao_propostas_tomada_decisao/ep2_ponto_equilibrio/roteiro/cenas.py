# Roteiro — Comparação de Propostas e Tomada de Decisão, Episódio 2 de 5: planos com parte fixa e parte variável,
#   o ponto de equilíbrio
# Base: Estudos/Enem/estudos/01-matematica/18-comparacao-propostas-tomada-decisao.html — seções 04 e 08 + Questões 1, 6
#   e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   O PONTO DE EQUILÍBRIO É O CRUZAMENTO DAS RETAS: antes vence o fixo baixo; depois, o preço por unidade baixo.
#   A DIFERENÇA DOS FIXOS É UMA DÍVIDA: os R$ 30,00 a mais do plano B são recuperados a R$ 0,30 por minuto (cofrinho).
#   NO EMPATE, NINGUÉM GANHA: "mais barato" começa no primeiro número depois.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: telefonia A = 50 + 0,5x, B = 80 + 0,2x → 0,3x = 30 → 100 min, R$ 100,00 · 60 min: A 80,
#   B 92 · 150 min: A 125, B 110 · nós fazemos (táxi): 6 + 2,5x × 12 + 2x → 6 ÷ 0,5 = 12 km; teste 20 km: A 56, B 52.
# Exemplos NOSSOS (para não entregar a Q9, "você faz"): bloco e, empate inteiro em 20 dias → 21 e empate em 16,7 → 17;
#   erro 3, passe mensal de R$ 150,00 × R$ 4,40 por viagem: 150 ÷ 4,4 ≈ 34,1 → 35 viagens (com 34: 149,60, a tarifa
#   ainda ganha; com 35: 154,00, o passe ganha).
# Atalhos (verde): equilíbrio = diferença dos fixos ÷ diferença dos preços por unidade · "dividir por 0,3 = tirar a vírgula
#   dos dois" (30 ÷ 0,3 = 300 ÷ 3) · 180 ÷ 0,75 = 180 × 4 ÷ 3 (0,75 = 3/4).
# QUESTÃO 1 (eu faço): B, superior a 100 min. Erradas (material): A = 30 ÷ 0,5 = 60 · C = 30 ÷ 0,2 = 150 ·
#   D = 130 ÷ 0,5 = 260 · E = 80 ÷ 0,2 = 400.
# QUESTÃO 6 (nós fazemos): A = 3 · 120 = 360; B = 3 · 60 + 0,75x = 180 + 0,75x → 0,75x = 180 → 240 km (C);
#   teste 300 km: B 405, A 360. Erradas (material): A = 60 ÷ 0,75 = 80 (um dia só) · B = 120 ÷ 0,75 = 160 e
#   D = 360 ÷ 0,75 = 480 (esquecem a diária de B) · E = 540 ÷ 0,75 = 720 (soma as diárias das duas).
# QUESTÃO 9 (você faz): 25d = 300 → 12 dias (empate: R$ 300,00 nas duas) → resposta 13 dias (C); 13 dias de diária = 325.
#   Erradas (material): B = o empate · A = 300 ÷ 30 = 10 (custo diário da mensalidade) · D = 20 dias úteis (o
#   enunciado não diz) · E = 25 (o valor da diária lido como número de dias).
# Frases-chave (meio e fim, idênticas): 1. Iguale os custos para achar o ponto de equilíbrio. 2. Abaixo do equilíbrio
#   vence o fixo baixo; acima, o preço por unidade baixo. 3. No empate, os dois custam o mesmo: "mais barato" começa depois.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Qual plano vale mais a pena? O ponto de equilíbrio | Comparar Propostas Ep. 2"
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
        "{a}Qual plano de celular é melhor, [p=0.2] o de *cinquenta reais* [p=0.2] ou o de *oitenta reais?* [p=0.5] "
        "{b}Para quem fala *sessenta minutos,* [p=0.2] o primeiro. [p=0.4] {c}Para quem fala *cento e cinquenta,* "
        "[p=0.2] o segundo. [p=0.5] {d}O ENEM quer o *número exato* [p=0.2] em que a resposta muda."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai encontrar o *ponto de equilíbrio* entre dois planos [p=0.3] "
        "{b}e dizer qual vale em cada faixa de uso, [p=0.3] {c}sem errar o *a partir de.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Primeiro: [p=0.2] o custo de vários itens é o *preço vezes a "
        "quantidade.* [p=0.2] Cinquenta centavos por minuto, [p=0.2] em sessenta minutos, [p=0.2] *trinta reais.* "
        "[p=0.4] {b}Segundo: [p=0.2] numa igualdade, [p=0.2] *o que eu faço de um lado, faço do outro.* [p=0.2] É "
        "assim que se isola o x."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pegue o folheto da operadora. [p=0.2] Plano A: [p=0.2] *cinquenta reais por mês,* [p=0.2] mais *cinquenta "
        "centavos* por minuto. [p=0.2] Plano B: [p=0.2] *oitenta reais,* [p=0.2] mais *vinte centavos* por minuto. "
        "[p=0.4] {b}A *parte fixa* [p=0.2] é o que você paga mesmo sem usar nada. [p=0.4] {c}A *parte variável* [p=0.2] "
        "cresce com o uso: [p=0.2] o *preço por unidade* [p=0.2] vezes o *consumo,* [p=0.2] que é quanto você usou."),
    dict(id="05", block="concreto", text=
        "{t}E isso não é só celular. [p=0.3] {a}Duas locadoras de carro para o feriado: [p=0.2] diária cara e "
        "quilometragem livre, [p=0.2] ou diária barata e preço por quilômetro. [p=0.4] {b}Um estacionamento: "
        "[p=0.2] *diária* [p=0.2] ou *mensalidade.* [p=0.4] {c}Sempre a mesma briga: [p=0.2] *fixo baixo* "
        "contra *preço por unidade baixo.*"),

    # ================= BLOCO A: A FÓRMULA DO CUSTO =================
    dict(id="06", block="formula", text=
        "{t}Como se calcula o custo de um plano? [p=0.4] {a}Custo [p=0.2] é igual a *parte fixa* [p=0.2] mais *preço "
        "por unidade vezes x.* [p=0.2] O x é o consumo. [p=0.4] {b}No plano A: [p=0.2] cinquenta [p=0.2] mais zero "
        "vírgula cinco x. [p=0.4] {c}No plano B: [p=0.2] oitenta [p=0.2] mais zero vírgula dois x. [p=0.4] {d}Quem "
        "fala sessenta minutos no A paga [p=0.2] cinquenta mais trinta: [p=0.2] *oitenta reais.*"),

    # ================= BLOCO B: O EMPATE =================
    dict(id="07", block="empate", text=
        "{t}E em que consumo os dois custam *o mesmo?* [p=0.4] {a}É o *ponto de equilíbrio,* [p=0.2] ou *empate:* "
        "[p=0.2] o consumo em que os dois planos têm o mesmo custo. [p=0.4] {b}Para achar, [p=0.2] *iguale os "
        "custos:* [p=0.2] cinquenta mais zero vírgula cinco x [p=0.2] igual a oitenta mais zero vírgula dois x. "
        "[p=0.4] {c}Tire zero vírgula dois x *dos dois lados:* [p=0.2] cinquenta mais zero vírgula três x [p=0.2] "
        "igual a oitenta."),
    dict(id="08", block="empate", text=
        "{a}Tire cinquenta dos dois lados: [p=0.2] *zero vírgula três x* [p=0.2] igual a *trinta.* [p=0.4] {b}Divida "
        "os dois lados por zero vírgula três: [p=0.2] x igual a *cem minutos.* [p=0.4] {c}E o custo no empate? "
        "[p=0.2] Nos dois planos, [p=0.2] *cem reais.*"),
    dict(id="09", block="grafico", text=
        "{t}Por que esse número decide tudo? [p=0.4] {a}Desenhe os dois custos. [p=0.2] O A começa em *cinquenta* "
        "[p=0.2] e sobe *mais inclinado.* [p=0.2] O B começa em *oitenta* [p=0.2] e sobe *devagar.* [p=0.4] {b}Eles "
        "se cruzam [p=0.2] em *cem minutos, cem reais.* [p=0.4] {c}Antes do cruzamento, [p=0.2] vence o plano de *fixo "
        "baixo.* [p=0.4] {d}Depois dele, [p=0.2] vence o de *preço por minuto baixo.*"),

    # ================= BLOCO C: O TESTE =================
    dict(id="10", block="teste", text=
        "{t}Vamos conferir dos dois lados? [p=0.4] {a}Com *sessenta minutos:* [p=0.2] o A custa *oitenta,* [p=0.2] o "
        "B custa oitenta mais doze, [p=0.2] *noventa e dois.* [p=0.2] O A é melhor. [p=0.4] {b}Com *cento e "
        "cinquenta:* [p=0.2] o A custa *cento e vinte e cinco,* [p=0.2] o B, *cento e dez.* [p=0.2] O B é melhor. "
        "[p=0.4] {c}Regra de ouro: [p=0.2] depois de achar o empate, [p=0.2] *teste sempre um valor acima dele.*"),

    # ================= BLOCO D: O COFRINHO E O ATALHO =================
    dict(id="11", block="cofrinho", text=
        "{t}Dá para achar os cem minutos *de cabeça?* [p=0.4] {a}Dá. [p=0.2] O B começa com *trinta reais a "
        "mais:* [p=0.2] uma *dívida.* [p=0.4] {b}A cada minuto, [p=0.2] o B cobra *trinta centavos a "
        "menos* que o A [p=0.2] e vai pagando a dívida aos pouquinhos. [p=0.4] {c}Trinta reais, [p=0.2] "
        "pagos de trinta em trinta centavos: [p=0.2] a dívida *zera no minuto cem.*"),
    dict(id="12", block="cofrinho", text=
        "{t}Esse é o atalho. [p=0.3] {a}Ponto de equilíbrio [p=0.2] é igual à *diferença dos fixos* [p=0.2] dividida "
        "pela *diferença dos preços por unidade.* [p=0.4] {b}Oitenta menos cinquenta, [p=0.2] *trinta.* [p=0.2] "
        "Cinquenta centavos menos vinte, [p=0.2] *trinta centavos.* [p=0.2] Trinta dividido por zero vírgula três: "
        "[p=0.2] *cem.* [p=0.4] {c}E para dividir por zero vírgula três, [p=0.2] *ande a vírgula nos dois:* [p=0.2] "
        "trezentos dividido por três."),

    # ================= BLOCO E: O "A PARTIR DE" =================
    dict(id="13", block="apartir", text=
        "{t}A partir de quantos minutos o B é mais barato? [p=0.4] {a}Com cem minutos, [p=0.2] os dois custam cem. "
        "[p=0.2] *No empate, ninguém ganha.* [p=0.4] {b}*Mais barato* [p=0.2] começa *depois* do empate: [p=0.2] "
        "acima de cem minutos."),
    dict(id="14", block="apartir", text=
        "{t}E quando a resposta tem que ser um número inteiro? [p=0.4] {a}Dias, unidades, viagens: [p=0.2] é uma "
        "*variável inteira,* [p=0.2] que não aceita vírgula. [p=0.4] {b}Se o empate dá *vinte dias,* [p=0.2] a "
        "resposta é o primeiro inteiro depois: [p=0.2] *vinte e um.* [p=0.4] {c}Se o empate dá *dezesseis vírgula "
        "sete,* [p=0.2] *arredonde para cima:* [p=0.2] *dezessete.*"),

    # ================= BLOCO F: DECISÕES QUE DEPENDEM DO USO =================
    dict(id="15", block="uso", text=
        "{t}Onde mais aparece essa conta? [p=0.4] {a}No estacionamento, [p=0.2] decidem os *dias de uso.* "
        "[p=0.3] {b}Na locadora, [p=0.2] os *quilômetros.* [p=0.3] {c}No transporte, [p=0.2] as *viagens.* [p=0.3] "
        "{d}Num aparelho econômico, [p=0.2] as *horas de uso.*"),
    dict(id="16", block="uso", text=
        "{a}A pergunta é sempre a mesma: [p=0.2] *em que consumo as opções se igualam?* [p=0.4] {b}Se o enunciado não diz "
        "o consumo, [p=0.2] a resposta certa costuma ser: [p=0.2] *depende do uso.* [p=0.2] Uma até tal ponto, "
        "[p=0.2] a outra a partir dele."),
    dict(id="17", block="uso", text=
        "{t}E se a escolha não for só dinheiro? [p=0.4] {a}Na vida real pesam *risco e conveniência.* "
        "[p=0.4] {b}Na prova, [p=0.2] o enunciado define o critério, [p=0.2] como *menor custo.* [p=0.2] Responda "
        "por ele, [p=0.2] não pelo que você preferiria."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}O táxi A cobra *seis reais fixos* [p=0.2] mais *dois e cinquenta por quilômetro.* "
        "[p=0.2] O táxi B, [p=0.2] *doze reais fixos* [p=0.2] mais *dois reais por quilômetro.* [p=0.4] {b}A partir "
        "de quantos quilômetros o táxi B é mais barato? [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Diferença dos fixos: [p=0.2] doze menos seis, [p=0.2] *seis reais.* [p=0.2] "
        "Diferença por quilômetro: [p=0.2] *cinquenta centavos.* [p=0.4] {b}Seis dividido por zero vírgula cinco: "
        "[p=0.2] *doze quilômetros.* [p=0.2] É o empate. [p=0.4] {c}Teste com vinte: [p=0.2] o A custa seis mais "
        "cinquenta, [p=0.2] *cinquenta e seis.* [p=0.2] O B, doze mais quarenta, [p=0.2] *cinquenta e dois.* [p=0.4] "
        "{d}Acima de *doze quilômetros,* [p=0.2] o B é mais barato."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] iguale os custos para achar o ponto de equilíbrio. "
        "[p=0.5] {b}Dois: [p=0.2] abaixo do equilíbrio vence o fixo baixo; [p=0.2] acima, o preço por unidade baixo. "
        "[p=0.5] {c}Três: [p=0.2] no empate, os dois custam o mesmo: [p=0.2] mais barato começa depois."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *escolher um plano sem olhar o consumo.* [p=0.2] "
        "O A tem o fixo menor, [p=0.2] então é sempre melhor. [p=0.4] {b}Parece certo, [p=0.2] porque cinquenta é "
        "menos que oitenta. [p=0.4] {c}Mas a resposta *depende do uso:* [p=0.2] acima de cem minutos, o A perde."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] dividir a diferença dos fixos [p=0.2] por *um preço só.* [p=0.2] Trinta dividido por "
        "zero vírgula cinco, [p=0.2] *sessenta.* [p=0.4] {b}Parece certo, [p=0.2] porque zero vírgula cinco está "
        "ali, no plano A. [p=0.4] {c}Mas o que paga a dívida é a *diferença dos preços:* [p=0.2] cinquenta menos "
        "vinte, [p=0.2] trinta centavos. [p=0.2] Dá *cem.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] *arredondar o empate para baixo.* [p=0.2] Passe de *cento e cinquenta reais* [p=0.2] ou "
        "*quatro e quarenta* por viagem: [p=0.2] empate em *trinta e quatro vírgula um.* [p=0.2] Trinta e quatro? [p=0.4] {b}Parece certo, [p=0.2] porque é o inteiro mais perto. [p=0.4] {c}Mas trinta e "
        "quatro viagens custam *cento e quarenta e nove e sessenta:* [p=0.2] o passe ainda não compensa. [p=0.2] "
        "Resposta: [p=0.2] *trinta e cinco.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="24", block="q1", text=
        "{t}Questão do nosso material, [p=0.2] no estilo do ENEM. [p=0.2] Eu faço. "
        "[p=0.4] {a}Uma operadora oferece dois planos. [p=0.2] No A, [p=0.2] *cinquenta reais fixos* mais *cinquenta "
        "centavos* por minuto. [p=0.2] No B, [p=0.2] *oitenta reais fixos* mais *vinte centavos* por minuto. [p=0.2] O "
        "plano B passa a ser mais vantajoso [p=0.2] quando o consumo, em minutos, for superior a: [p=0.4] {qa}A: "
        "[p=0.2] sessenta. [p=0.3] {qb}B: [p=0.2] cem. [p=0.3] {qc}C: [p=0.2] cento e cinquenta. [p=0.3] {qd}D: "
        "[p=0.2] duzentos e sessenta. [p=0.3] {qe}E: [p=0.2] quatrocentos."),
    dict(id="25", block="q1", text=
        "{t}São os mesmos planos. [p=0.3] {a}Iguale: [p=0.2] zero vírgula três x igual a trinta, [p=0.2] "
        "*x igual a cem.* [p=0.4] {b}Teste acima: [p=0.2] com cento e cinquenta minutos, [p=0.2] A custa cento e "
        "vinte e cinco, [p=0.2] B custa cento e dez. [p=0.2] Acima de cem, o B ganha. [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q1", text=
        "{t}E as outras? [p=0.3] {xa}A A divide os trinta *só pelo preço do A,* [p=0.2] zero vírgula cinco. [p=0.4] "
        "{xc}A C divide *só pelo preço do B,* [p=0.2] zero vírgula dois. [p=0.4] {xd}A D divide a *soma dos fixos,* "
        "[p=0.2] cento e trinta, [p=0.2] por zero vírgula cinco. [p=0.4] {xe}E a E divide o fixo do B pelo preço "
        "dele, [p=0.2] *sem comparar com o A.*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="27", block="q6", text=
        "{t}Agora, juntos. [p=0.4] {a}Para uma viagem de *três dias,* [p=0.2] uma família compara duas "
        "locadoras. [p=0.2] A locadora A cobra *cento e vinte reais por dia,* [p=0.2] com quilometragem livre. [p=0.2] "
        "A locadora B cobra *sessenta reais por dia* [p=0.2] mais *setenta e cinco centavos* por quilômetro rodado. "
        "[p=0.2] A locadora A será mais vantajosa se a família rodar mais de: [p=0.4] {qa}A: [p=0.2] oitenta "
        "quilômetros. [p=0.3] {qb}B: [p=0.2] cento e sessenta. [p=0.3] {qc}C: [p=0.2] duzentos e quarenta. [p=0.3] "
        "{qd}D: [p=0.2] quatrocentos e oitenta. [p=0.3] {qe}E: [p=0.2] setecentos e vinte. [p=0.4] {p}*Pause e "
        "monte a tabela.* [p=2.0]"),
    dict(id="28", block="q6", text=
        "{t}Montou? [p=0.3] {a}São *três dias.* [p=0.2] A: [p=0.2] três vezes cento e vinte, [p=0.2] *trezentos e "
        "sessenta.* [p=0.2] B: [p=0.2] três vezes sessenta, [p=0.2] *cento e oitenta,* [p=0.2] mais zero vírgula "
        "setenta e cinco x. [p=0.4] {b}Iguale: [p=0.2] zero vírgula setenta e cinco x [p=0.2] igual a cento e "
        "oitenta. [p=0.2] *x igual a duzentos e quarenta.* [p=0.4] {c}Teste com trezentos quilômetros: [p=0.2] o B "
        "custa *quatrocentos e cinco,* [p=0.2] o A, *trezentos e sessenta.* [p=0.2] O A ganha. [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A faz a conta de *um dia só.* [p=0.4] {xb}A B e a D [p=0.2] *esquecem a "
        "diária do B:* [p=0.2] dividem cento e vinte, [p=0.2] ou trezentos e sessenta, [p=0.2] direto por zero "
        "vírgula setenta e cinco. [p=0.4] {xe}E a E *soma as diárias* das duas locadoras. [p=0.4] {c}Atalho: [p=0.2] "
        "dividir por zero vírgula setenta e cinco [p=0.2] é *vezes quatro, dividido por três.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="30", block="q9", text=
        "{t}Agora é com você. [p=0.4] {a}Um estacionamento cobra *vinte e cinco reais por dia de uso* [p=0.2] ou "
        "*trezentos reais* pela mensalidade, [p=0.2] que permite usar todos os dias do mês. [p=0.2] O número *mínimo* "
        "de dias de uso no mês [p=0.2] para que a mensalidade seja *mais barata* que as diárias é: [p=0.4] {qa}A: "
        "[p=0.2] dez. [p=0.3] {qb}B: [p=0.2] doze. [p=0.3] {qc}C: [p=0.2] treze. [p=0.3] {qd}D: [p=0.2] vinte. [p=0.3] "
        "{qe}E: [p=0.2] vinte e cinco. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="31", block="q9", text=
        "{t}Vamos conferir. [p=0.3] {a}Iguale: [p=0.2] vinte e cinco d igual a trezentos. [p=0.2] *d igual a doze.* "
        "[p=0.4] {b}Mas com doze dias, [p=0.2] as duas opções custam *trezentos reais.* [p=0.2] Empate: [p=0.2] a "
        "mensalidade *ainda não é mais barata.* [p=0.4] {c}Teste com treze: [p=0.2] as diárias custam *trezentos e "
        "vinte e cinco.* [p=0.2] Agora a mensalidade ganha. [p=0.3] {ok}*Letra C, treze dias!*"),
    dict(id="32", block="q9", text=
        "{t}E as pegadinhas? [p=0.3] {xb}A B é o *próprio empate:* [p=0.2] a armadilha principal. [p=0.4] {xa}A A "
        "divide trezentos por trinta dias: [p=0.2] o custo diário da mensalidade. [p=0.4] "
        "{xd}A D supõe *vinte dias úteis,* [p=0.2] que o enunciado não deu. [p=0.4] {xe}E a E confunde o *valor da "
        "diária* com o número de dias."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] iguale os custos para achar o ponto de "
        "equilíbrio. [p=0.5] {b}Dois: [p=0.2] abaixo do equilíbrio vence o fixo baixo; [p=0.2] acima, o preço por "
        "unidade baixo. [p=0.5] {c}Três: [p=0.2] no empate, os dois custam o mesmo: [p=0.2] mais barato começa "
        "depois."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Uma aplicação rende *doze por cento ao ano* com imposto; [p=0.3] {b}outra rende *dez por cento,* "
        "*isenta.* [p=0.4] {c}A de doze por cento ganha? [p=0.4] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual plano você usa hoje, [p=0.2] e ele vale a pena para o seu "
        "consumo? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
