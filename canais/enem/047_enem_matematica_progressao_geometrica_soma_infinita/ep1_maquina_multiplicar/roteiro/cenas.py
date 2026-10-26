# Roteiro — Progressão Geométrica, Episódio 1 de 5: o que é PG, a razão como fator e o termo geral
# Base: Estudos/Enem/estudos/01-matematica/32-progressao-geometrica-soma-infinita.html — seções 02, 03 e 04 + Questões 7 e 9
#   (seção 12) + questão NOVA das algas (texto do roteiros.md, não está no material). Questões 1 e 2 do material NÃO usadas.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A MÁQUINA ×q: cada termo passa pela mesma máquina de multiplicar.
#   QUANTAS VEZES A MÁQUINA AGE: do 1º ao n-ésimo, n − 1 vezes; contando do instante zero, t vezes.
#   NA PA A DISTÂNCIA SE DIVIDE; NA PG SE TIRA A RAIZ.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# DESVIOS do prompt (para não entregar questões com pausa):
#   bloco f: o prompt usa a₂ = 6 e a₅ = 162 → q = 3, que é a montagem da questão das algas ("nós fazemos", com pausa).
#     O bloco usa um exemplo NOSSO: a₂ = 3 e a₅ = 24 → q³ = 8 → q = 2. O 6 → 162 só aparece na questão das algas.
#   bloco g (teste da tabela): o material usa 1 000, 1 200, 1 440, 1 728, que é a Questão 9 ("você faz"). O bloco usa
#     tabelas NOSSAS: 200, 300, 450, 675 (quociente 1,5 → PG) × 200, 300, 400, 500 (diferença 100 → PA).
#   termo geral: exemplo NOSSO (3, 6, 12, …): a₅ = 3 · 2⁴ = 48 (erro 1: 3 · 2⁵ = 96).
#   bloco e (500 bactérias, 2⁶ = 32 000): só citado como "você já viu isso na série de Função Exponencial", sem questão.
# Nós fazemos (prompt): app com 2 000 usuários, 10% ao mês, 3 meses → q = 1,1; 2 000 · 1,331 = 2 662.
# Erros clássicos: a₅ de (3, 6, 12, …) com q⁵ (96 em vez de 48); razão de (80, 40, 20) = −40; 500 · 2 · 6 = 6 000 em vez
#   de 32 000 (o exemplo citado); 5% com q = 0,05 (1 000 · 0,05 = 50: a população cairia). Nada da Q7, das algas nem da Q9.
# QUESTÃO 7 ("eu faço"): gabarito D (48 620). Erradas = material (A 8 000 só o aumento linear; B 42 000, um ano;
#   C 48 000, crescimento linear; E 168 000, × 1,05 e × 4).
# QUESTÃO NOVA, ALGAS ("nós fazemos"): gabarito D (1 458 g). Erradas = roteiros.md (A PA, r = 52 → 266; B uma
#   multiplicação só, 6ª semana, 486; C 162 · 3 · 2 = 972; E três multiplicações, 8ª semana, 4 374).
# QUESTÃO 9 ("você faz", com pausa): gabarito E (1 000 · 1,2ⁿ). Erradas = material (A linear, acerta n = 1 e erra n = 2:
#   1 400 ≠ 1 440; B 1,2 vezes n: 0 clientes no ano 0; C usa a taxa 0,2 e faz cair; D esquece o valor inicial).
# Acréscimos NOSSOS (marcados): atalho verde "fator = 1 ± taxa" (cena 07); atalho verde "escreva fator e quantas vezes ele
#   age antes da potência" (cena 09); atalho verde "teste da tabela" (cena 12); atalho verde "conte as vezes pelos índices
#   ou pelos períodos" (cena 10).
# Frases-chave (meio e fim, idênticas): 1. Na PG, o que se repete é a divisão de um termo pelo anterior.
#   2. Crescer i% é multiplicar por 1 + i. 3. O expoente é o número de vezes que o fator age.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Progressão geométrica do zero: a máquina de multiplicar | PG Ep. 1"
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
        "{a}Duas sequências começam no *dois.* [p=0.4] {b}Uma *soma seis* a cada passo: [p=0.2] dois, oito, quatorze, "
        "vinte, vinte e seis. [p=0.4] {c}A outra só *dobra:* [p=0.2] dois, quatro, oito, dezesseis, trinta e dois. "
        "[p=0.4] {d}No quinto termo, [p=0.2] *quem dobra já passou na frente.* [p=0.3] {e}E *nunca mais é alcançada.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Progressão geométrica.* [p=0.4] {a}Ao final, [p=0.2] você vai "
        "*reconhecer uma PG,* [p=0.3] {b}*transformar porcentagem em razão* [p=0.3] {c}e *achar qualquer termo* sem "
        "listar os anteriores."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}*Potência* é multiplicação repetida: [p=0.2] dois elevado a seis, "
        "[p=0.2] seis vezes o dois, [p=0.2] *sessenta e quatro.* [p=0.4] {b}Crescer cinco por cento [p=0.2] é "
        "*multiplicar por um vírgula zero cinco.* [p=0.4] {c}E da PA: [p=0.2] do primeiro termo ao de posição n, "
        "[p=0.2] são *n menos um* passos."),

    # ================= BLOCO A: O QUE É PG =================
    dict(id="04", block="folha", text=
        "{t}O que acontece quando você dobra uma folha ao meio, [p=0.2] e de novo, [p=0.2] e de novo? [p=0.4] {a}*Duas* "
        "camadas. [p=0.2] *Quatro.* [p=0.2] *Oito.* [p=0.2] *Dezesseis.* [p=0.4] {b}Cada número é o anterior *vezes "
        "dois.* [p=0.4] {c}Uma cidade que cresce cinco por cento ao ano [p=0.2] faz igual: [p=0.2] cada ano, *vezes um "
        "vírgula zero cinco.* [p=0.4] {d}Isso é uma *progressão geométrica,* [p=0.2] a PG: [p=0.2] cada termo é o "
        "anterior *vezes o mesmo número.*"),
    dict(id="05", block="tipos", text=
        "{t}E esse número fixo? [p=0.4] {a}É a *razão,* [p=0.2] a letra *q.* [p=0.2] Pense numa *máquina de "
        "multiplicar:* [p=0.2] cada termo entra, [p=0.2] passa pela máquina vezes q [p=0.2] e sai o seguinte. [p=0.4] "
        "{b}Com q igual a dois, [p=0.2] a PG *cresce.* [p=0.3] {c}Com um meio, [p=0.2] *decresce:* [p=0.2] oitenta, "
        "quarenta, vinte. [p=0.3] {d}Com q *negativo,* [p=0.2] os sinais se revezam: [p=0.2] *alternante.* [p=0.3] "
        "{e}Com q igual a um, [p=0.2] *constante:* [p=0.2] cinco, cinco, cinco."),

    # ================= BLOCO B: QUOCIENTE, NÃO DIFERENÇA =================
    dict(id="06", block="quociente", text=
        "{t}Como descobrir a razão? [p=0.4] {a}*Divida* um termo pelo anterior. [p=0.2] O resultado da divisão "
        "[p=0.2] é o *quociente.* [p=0.4] {b}Em oitenta, quarenta, vinte: [p=0.2] quarenta dividido por oitenta, "
        "[p=0.2] *zero vírgula cinco.* [p=0.4] {c}Não é *menos quarenta:* [p=0.2] isso é a *diferença,* [p=0.2] coisa "
        "de PA. [p=0.4] {d}Na PG, [p=0.2] o que se repete é a *divisão.*"),

    # ================= BLOCO C: PORCENTAGEM VIRA RAZÃO =================
    dict(id="07", block="fator", text=
        "{t}E quando a questão dá uma *porcentagem?* [p=0.4] {a}Ela vira razão. [p=0.2] *Fator* é o número que "
        "multiplica. [p=0.4] {b}Atalho: [p=0.2] crescer i por cento [p=0.2] é multiplicar por *um mais i.* [p=0.2] "
        "Cinco por cento: [p=0.2] *um vírgula zero cinco.* [p=0.4] {c}Cair i por cento [p=0.2] é multiplicar por *um "
        "menos i.* [p=0.2] Um carro que perde quinze por cento: [p=0.2] *zero vírgula oitenta e cinco.* [p=0.4] {d}Você "
        "multiplica pelo que *fica,* [p=0.2] não pela porcentagem."),

    # ================= BLOCO D: TERMO GERAL =================
    dict(id="08", block="termo", text=
        "{t}E como achar o vigésimo termo sem listar todos? [p=0.4] {a}Pense na máquina. [p=0.2] Até o segundo termo, "
        "[p=0.2] ela age *uma* vez. [p=0.2] Até o terceiro, *duas.* [p=0.2] Até o de posição n, [p=0.2] *n menos um* "
        "vezes. [p=0.4] {b}Daí o *termo geral,* [p=0.2] a fórmula que dá qualquer termo: [p=0.2] *a ene é igual a a "
        "um, vezes q elevado a n menos um.* [p=0.4] {c}Em três, seis, doze: [p=0.2] o quinto termo é três vezes dois "
        "elevado a quatro, [p=0.2] *quarenta e oito.* [p=0.4] {d}Partindo de outro termo, o de posição k: [p=0.2] *q "
        "elevado a n menos k.*"),
    dict(id="09", block="zero", text=
        "{t}E quando a questão fala em *tempo?* [p=0.4] {a}Conte a partir do *instante zero.* [p=0.2] O valor inicial "
        "vira o *termo zero,* [p=0.2] a zero. [p=0.2] Depois de t períodos: [p=0.2] *a zero vezes q elevado a t.* "
        "[p=0.4] {b}Você já viu isso na série de Função Exponencial: [p=0.2] *quinhentas bactérias* que dobram a cada "
        "vinte minutos. [p=0.2] Em duas horas, [p=0.2] *seis* duplicações: [p=0.2] *trinta e dois mil.* [p=0.4] {c}É a "
        "mesma conta. [p=0.2] Só muda *quem é o primeiro.* [p=0.4] {d}Atalho: [p=0.2] antes de qualquer potência, "
        "[p=0.2] escreva *o fator* [p=0.2] e *quantas vezes ele age.*"),

    # ================= BLOCO E: RAZÃO POR DOIS TERMOS =================
    dict(id="10", block="doistermos", text=
        "{t}E se a questão dá dois termos soltos? [p=0.4] {a}O segundo termo é *três,* [p=0.2] e o quinto é *vinte e "
        "quatro.* [p=0.4] {b}Atalho: [p=0.2] conte as vezes pelos índices: [p=0.2] cinco menos dois, [p=0.2] *três "
        "vezes.* [p=0.4] {c}Então q ao cubo [p=0.2] é vinte e quatro dividido por três, [p=0.2] *oito.* [p=0.2] Que "
        "número, três vezes, dá oito? [p=0.2] *Dois.* [p=0.4] {d}Na PA, [p=0.2] a distância entre os termos *se "
        "divide.* [p=0.2] Na PG, [p=0.2] *se tira a raiz.*"),

    # ================= BLOCO F: PG É EXPONENCIAL =================
    dict(id="11", block="corrida", text=
        "{t}Por que quem dobra nunca mais é alcançada? [p=0.4] {a}Coloque as duas para correr. [p=0.2] A PA anda em "
        "*passos iguais,* [p=0.2] numa reta. [p=0.4] {b}A PG sobe por uma *curva.* [p=0.2] No quarto termo, ainda "
        "perde: [p=0.2] dezesseis contra vinte. [p=0.4] {c}No quinto, [p=0.2] *trinta e dois contra vinte e seis.* "
        "[p=0.2] No sexto, [p=0.2] *sessenta e quatro contra trinta e dois.* [p=0.4] {d}A PG é uma *função "
        "exponencial* [p=0.2] calculada só em um, dois, três… [p=0.2] Com razão maior que um, [p=0.2] passa *qualquer* "
        "PA."),
    dict(id="12", block="tabela", text=
        "{t}E como saber se uma tabela é PA ou PG? [p=0.4] {a}Atalho: [p=0.2] *o teste da tabela.* [p=0.4] {b}Divida "
        "cada valor pelo anterior. [p=0.2] Duzentos, trezentos, quatrocentos e cinquenta: [p=0.2] quociente sempre *um "
        "vírgula cinco.* [p=0.2] *PG.* [p=0.4] {c}Duzentos, trezentos, quatrocentos: [p=0.2] *diferença* sempre cem. "
        "[p=0.2] *PA.* [p=0.4] {d}Quociente constante: [p=0.2] *exponencial.* [p=0.2] Diferença constante: [p=0.2] "
        "*afim.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um aplicativo tem *dois mil usuários* [p=0.2] e cresce *dez por cento ao mês.* [p=0.3] "
        "Qual é a razão, [p=0.2] e quantos usuários terá *daqui a três meses?* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Crescer dez por cento: [p=0.2] fator *um vírgula um.* [p=0.4] {b}Quantas vezes ele "
        "age? [p=0.2] *Três,* [p=0.2] uma por mês. [p=0.4] {c}Um vírgula um ao cubo [p=0.2] é *um vírgula trezentos e "
        "trinta e um.* [p=0.2] Vezes dois mil: [p=0.2] *dois mil seiscentos e sessenta e dois* usuários."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] na PG, o que se repete é a divisão de um termo pelo "
        "anterior. [p=0.5] {b}Dois: [p=0.2] crescer i por cento é multiplicar por um mais i. [p=0.5] {c}Três: [p=0.2] "
        "o expoente é o número de vezes que o fator age."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar *q elevado a n,* [p=0.2] sem o menos "
        "um. [p=0.2] O quinto termo de três, seis, doze vira *noventa e seis.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "é o quinto, [p=0.2] então parece expoente cinco. [p=0.4] {c}Mas o primeiro termo *já está lá.* [p=0.2] A "
        "máquina age *quatro* vezes: [p=0.2] quarenta e oito."),
    dict(id="17", block="erros", text=
        "{a}Segundo: [p=0.2] dizer que a razão de oitenta, quarenta, vinte [p=0.2] é *menos quarenta.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque na PA era assim: [p=0.2] um menos o outro. [p=0.4] {c}Mas na PG você *divide.* [p=0.2] "
        "Quarenta dividido por oitenta: [p=0.2] *zero vírgula cinco.*"),
    dict(id="18", block="erros", text=
        "{a}Terceiro: [p=0.2] *dobrar seis vezes* virar *vezes dois vezes seis:* [p=0.2] *seis mil* bactérias. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque tem um dois e tem um seis. [p=0.4] {c}Mas seis vezes é o *expoente:* [p=0.2] "
        "dois elevado a seis, [p=0.2] *trinta e dois mil.*"),
    dict(id="19", block="erros", text=
        "{a}Quarto: [p=0.2] usar *zero vírgula zero cinco* como razão para cinco por cento. [p=0.2] Mil pessoas viram "
        "*cinquenta.* [p=0.4] {b}Parece certo, [p=0.2] porque zero vírgula zero cinco *é* cinco por cento. [p=0.4] "
        "{c}Mas isso é só o *aumento.* [p=0.2] O fator é *um vírgula zero cinco.*"),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="20", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}A população de "
        "um município é de *quarenta mil habitantes* [p=0.2] e deve crescer *cinco por cento ao ano.* [p=0.2] Use um "
        "vírgula zero cinco elevado a quatro [p=0.2] aproximadamente igual a um vírgula dois um cinco cinco. [p=0.3] "
        "*Daqui a quatro anos,* [p=0.2] a população será de aproximadamente: [p=0.3] {qa}A: [p=0.2] oito mil. [p=0.2] "
        "{qb}B: [p=0.2] quarenta e dois mil. [p=0.2] {qc}C: [p=0.2] quarenta e oito mil. [p=0.2] {qd}D: [p=0.2] quarenta "
        "e oito mil seiscentos e vinte. [p=0.2] {qe}E: [p=0.2] cento e sessenta e oito mil. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="21", block="q7", text=
        "{t}Fator e vezes. [p=0.3] {a}Cinco por cento ao ano: [p=0.2] fator *um vírgula zero cinco.* [p=0.2] Ele age "
        "*quatro vezes.* [p=0.4] {b}A potência o enunciado já deu: [p=0.2] um vírgula dois um cinco cinco. [p=0.4] "
        "{c}Quarenta mil vezes isso: [p=0.2] *quarenta e oito mil seiscentos e vinte.* [p=0.3] {d}Faz sentido: [p=0.2] "
        "pouco mais de vinte por cento em quatro anos. [p=0.2] {ok}*Letra D!*"),
    dict(id="22", block="q7", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é só o *aumento,* [p=0.2] e linear: [p=0.2] quatro vezes dois mil. "
        "[p=0.4] {xb}A B é *um ano só.* [p=0.4] {xc}A C soma dois mil por ano: [p=0.2] crescimento *linear,* [p=0.2] "
        "esquecendo que os cinco por cento incidem sobre a população já aumentada. [p=0.4] {xe}E a E multiplica por um "
        "vírgula zero cinco *e por quatro,* [p=0.2] em vez de elevar a quatro."),

    # ================= QUESTÃO NOVA: ALGAS (NÓS FAZEMOS) =================
    dict(id="23", block="algas", text=
        "{t}Agora fazemos juntos. [p=0.3] {a}Em um tanque de cultivo, [p=0.2] a massa de algas é medida ao fim de cada "
        "semana, [p=0.2] e os valores formam uma progressão geométrica. [p=0.2] Ao fim da *segunda semana* havia *seis "
        "gramas* de algas [p=0.2] e, ao fim da *quinta semana,* [p=0.2] *cento e sessenta e dois gramas.* [p=0.2] "
        "Mantido esse padrão, [p=0.2] ao fim da *sétima semana* a massa de algas será de: [p=0.3] {qa}A: [p=0.2] "
        "duzentos e sessenta e seis gramas. [p=0.2] {qb}B: [p=0.2] quatrocentos e oitenta e seis gramas. [p=0.2] {qc}C: "
        "[p=0.2] novecentos e setenta e dois gramas. [p=0.2] {qd}D: [p=0.2] mil quatrocentos e cinquenta e oito gramas. "
        "[p=0.2] {qe}E: [p=0.2] quatro mil trezentos e setenta e quatro gramas. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="algas", text=
        "{t}Primeiro, a razão. [p=0.3] {a}Da segunda à quinta semana, [p=0.2] o fator age *três vezes.* [p=0.2] Q ao "
        "cubo [p=0.2] é cento e sessenta e dois dividido por seis, [p=0.2] *vinte e sete.* [p=0.2] Q é *três.* [p=0.4] "
        "{b}Da quinta à sétima, [p=0.2] mais *duas vezes:* [p=0.2] cento e sessenta e dois vezes nove, [p=0.4] {c}*mil "
        "quatrocentos e cinquenta e oito gramas.* [p=0.3] {ok}*Letra D!*"),
    dict(id="25", block="algas", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A trata como *PA:* [p=0.2] soma cinquenta e dois por semana. [p=0.4] {xb}A B "
        "multiplica *uma vez só:* [p=0.2] sexta semana. [p=0.4] {xc}A C faz três vezes dois, [p=0.2] em vez de elevar. "
        "[p=0.4] {xe}E a E multiplica *três vezes:* [p=0.2] oitava semana."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="26", block="q9", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma loja virtual registrou os clientes cadastrados no início de cada ano, "
        "[p=0.2] a partir do ano de lançamento, [p=0.2] o *ano zero.* [p=0.2] Ano zero: [p=0.2] *mil.* [p=0.2] Ano um: "
        "[p=0.2] *mil e duzentos.* [p=0.2] Ano dois: [p=0.2] *mil quatrocentos e quarenta.* [p=0.2] Ano três: [p=0.2] "
        "*mil setecentos e vinte e oito.* [p=0.3] A expressão que dá os clientes no ano n é: [p=0.3] {qa}A: [p=0.2] mil "
        "mais duzentos n. [p=0.2] {qb}B: [p=0.2] mil vezes um vírgula dois n. [p=0.2] {qc}C: [p=0.2] mil vezes zero "
        "vírgula dois elevado a n. [p=0.2] {qd}D: [p=0.2] mil e duzentos elevado a n. [p=0.2] {qe}E: [p=0.2] mil vezes "
        "um vírgula dois elevado a n. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Teste da tabela: [p=0.2] divida cada valor pelo anterior. [p=0.2] Dá *um vírgula "
        "dois,* sempre. [p=0.2] É PG. [p=0.4] {b}O valor inicial é do *ano zero:* [p=0.2] mil. [p=0.2] O fator age *n "
        "vezes.* [p=0.4] {c}Mil vezes um vírgula dois elevado a n. [p=0.2] Teste no ano dois: [p=0.2] mil vezes um "
        "vírgula quatro quatro, [p=0.2] *mil quatrocentos e quarenta.* [p=0.2] Bate. [p=0.2] {ok}*Letra E!*"),
    dict(id="28", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é *linear:* [p=0.2] acerta o ano um, [p=0.2] mas no ano dois dá mil e "
        "quatrocentos. [p=0.4] {xb}A B multiplica *por n:* [p=0.2] zero clientes no ano zero. [p=0.4] {xc}A C usa a "
        "*taxa* no lugar do fator: [p=0.2] a loja encolheria. [p=0.4] {xd}E a D *esquece o valor inicial.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] na PG, o que se repete é a divisão de um termo "
        "pelo anterior. [p=0.5] {b}Dois: [p=0.2] crescer i por cento é multiplicar por um mais i. [p=0.5] {c}Três: "
        "[p=0.2] o expoente é o número de vezes que o fator age."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Uma mensagem vai para *três pessoas* no primeiro dia, [p=0.2] e cada uma repassa para *três novas* no dia "
        "seguinte. [p=0.4] {b}Em seis dias, [p=0.2] quantas pessoas receberam *ao todo?* [p=0.4] {c}Não é três elevado "
        "a seis. [p=0.4] {d}Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas vezes você consegue dobrar uma folha de papel? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
