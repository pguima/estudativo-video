# Roteiro — Função Exponencial, Episódio 4 de 6: exponencial ou afim? O teste da razão
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seção 06, o hábito 2 da
#   seção 09 ("teste a lei em três pontos") + Questão 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A TARTARUGA E A LEBRE AO CONTRÁRIO: a reta sai na frente, mas a curva sempre alcança e passa.
#   SUBTRAÇÃO × DIVISÃO: na afim o que se repete é a subtração entre vizinhos; na exponencial, a divisão.
#   TRÊS PONTOS: duas leis podem concordar em dois pontos e brigar no terceiro.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: função afim (série de Função afim) e a lei Q₀ · aᵗ (episódio 2). Progressão geométrica: só citada.
# Bloco a = tabela da seção 06 (100, 150, 200, 250, 300 × 100, 150, 225, 337,5, 506,25). Bloco c = corrida da seção 06
#   (20 + 10t × 2ᵗ: 80 × 64 em t = 6; 90 × 128 em t = 7). Bloco d retoma a Questão 3 do episódio 2 ("eu faço" de lá):
#   a reta 50 000 − 10 000t acerta t = 0 e t = 1 e erra t = 2 (30 000 × 32 000).
# Exemplos NOSSOS (marcados): perfis do concreto (um ganha 100 por semana, outro dobra: 100, 200, 300, 400 × 100, 200, 400,
#   800); erro 1 usa 2ᵗ × 1 + t (concordam em t = 0 e t = 1, brigam em t = 2: 4 × 3); erro 2 usa a corrida (de t = 4 para
#   t = 5 a curva ganha 16 e a reta 10, mas o total é 32 contra 70), para não adiantar a Questão 5.
# Acréscimos NOSSOS (marcados): dois atalhos verdes — "o teste em 3 passos: divida vizinho por vizinho; razão igual = fator;
#   o primeiro valor é o Q₀" (cena 08) e "t = 0, t = 1, t = 2: três substituições antes de marcar" (cena 12); a razão da
#   afim mostrada caindo (1,5 · 1,33 · 1,25 · 1,2) para provar que não é constante.
# Nós fazemos (prompt): 80, 120, 180, 270 → diferenças 40, 60, 90; razões 1,5 → exponencial; próximo valor 405.
# QUESTÃO 5 ("nós fazemos", com pausa): gabarito C (5 semanas). Tabela t = 3, 4, 5: A 1 900, 2 200, 2 500; B 800, 1 600,
#   3 200. Erradas = material/prompt (A 3 semanas: ganho semanal × total, 400 contra 300; B 4 semanas: compara com os 1 000
#   iniciais de A; D 6 semanas: conta hoje como a primeira semana; E nunca: ignora que a exponencial sempre ultrapassa).
# Frases-chave (meio e fim, idênticas): 1. Diferença constante é afim; razão constante é exponencial.
#   2. Toda exponencial crescente acaba ultrapassando qualquer reta. 3. Teste sempre três pontos, não dois.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Exponencial ou afim? O teste da razão em segundos | Função Exponencial Ep. 4"
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
        "{a}Uma reta começa em *vinte* [p=0.2] e uma curva começa em *um.* [p=0.5] {b}Até o passo seis, [p=0.2] a reta "
        "está na frente: [p=0.2] *oitenta contra sessenta e quatro.* [p=0.5] {c}No passo sete, [p=0.2] a curva já "
        "passou: [p=0.2] *cento e vinte e oito contra noventa.* [p=0.5] {d}E *nunca mais perde.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Função exponencial.* [p=0.4] {a}Ao final, [p=0.2] você vai olhar "
        "uma *tabela* [p=0.2] e dizer em segundos [p=0.2] se o crescimento é *afim ou exponencial,* [p=0.4] {b}e achar "
        "o *fator.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Função afim: [p=0.2] a afim *soma sempre o mesmo valor.* "
        "[p=0.4] {b}Do episódio dois: [p=0.2] a exponencial é *Q zero vezes a elevado a t:* [p=0.2] *multiplica* pelo "
        "fator a cada passo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em dois perfis de uma *rede social.* [p=0.4] {a}O primeiro ganha sempre *cem seguidores* por semana: "
        "[p=0.2] cem, [p=0.2] duzentos, [p=0.2] trezentos. [p=0.4] {b}O segundo *dobra:* [p=0.2] cem, [p=0.2] "
        "duzentos, [p=0.2] quatrocentos. [p=0.4] {c}O primeiro é um *modelo afim:* [p=0.2] soma o mesmo número. "
        "[p=0.3] O segundo, [p=0.2] um *modelo exponencial:* [p=0.2] multiplica pelo mesmo número."),

    # ================= BLOCO A: A TABELA DA SEÇÃO 06 =================
    dict(id="05", block="tabela", text=
        "{t}E quando só aparece a *tabela?* [p=0.4] {a}As duas começam em *cem.* [p=0.4] {b}As duas dão o mesmo "
        "primeiro passo: [p=0.2] *cento e cinquenta.* [p=0.4] {c}Depois, [p=0.2] uma vai para duzentos, [p=0.2] "
        "trezentos. [p=0.4] {d}A outra, [p=0.2] para duzentos e vinte e cinco, [p=0.2] até *quinhentos e seis.* "
        "[p=0.4] Qual é qual?"),

    # ================= BLOCO B: DIFERENÇA E RAZÃO =================
    dict(id="06", block="diferenca", text=
        "{t}Primeiro teste: [p=0.2] *subtraia* os vizinhos. [p=0.4] {a}Na primeira, [p=0.2] cada valor menos o "
        "anterior [p=0.2] dá sempre *cinquenta.* [p=0.3] Isso é uma *diferença constante:* [p=0.2] o mesmo salto "
        "sempre. [p=0.4] {b}Diferença constante é *afim.* [p=0.4] {c}Na segunda, [p=0.2] os saltos são cinquenta, "
        "[p=0.2] setenta e cinco, [p=0.2] cento e doze e meio. [p=0.2] *Crescem.*"),
    dict(id="07", block="razao", text=
        "{t}Segundo teste: [p=0.2] *divida.* [p=0.4] {a}O *teste da razão* é dividir cada "
        "valor pelo *anterior.* [p=0.4] {b}Na segunda tabela: [p=0.2] cento e cinquenta dividido por cem, [p=0.2] "
        "*um e meio.* [p=0.2] O próximo, [p=0.2] *um e meio* de novo. [p=0.2] "
        "Sempre um e meio. [p=0.4] {c}Isso é uma *razão constante.* [p=0.2] Exponencial, [p=0.2] e o fator é *um e "
        "meio.* [p=0.4] {d}Na afim, [p=0.2] a razão vai *caindo:* [p=0.2] um e meio, [p=0.2] um vírgula trinta e "
        "três, [p=0.2] e assim por diante. [p=0.4] {e}Guarde: [p=0.2] na afim se repete a *subtração;* [p=0.2] "
        "na exponencial, [p=0.2] a *divisão.*"),
    dict(id="08", block="atalho_razao", text=
        "{t}Atalho em três passos. [p=0.4] {a}Um: [p=0.2] divida *vizinho por vizinho,* "
        "[p=0.2] nunca pelo primeiro valor. [p=0.4] {b}Dois: [p=0.2] razão sempre igual? [p=0.2] Ela é o *fator a.* "
        "[p=0.4] {c}Três: [p=0.2] o valor em t igual a zero [p=0.2] é o *Q zero.* [p=0.3] Aqui, [p=0.2] *cem vezes "
        "um e meio elevado a t.*"),

    # ================= BLOCO C: A CORRIDA =================
    dict(id="09", block="corrida", text=
        "{t}E quem vence no fim? [p=0.4] {a}Lembra da *tartaruga e da lebre?* [p=0.2] Aqui é *ao contrário.* [p=0.4] "
        "{b}A tartaruga anda numa *reta:* [p=0.2] vinte mais dez t. [p=0.4] {c}A lebre anda "
        "numa *curva:* [p=0.2] dois elevado a t. [p=0.4] {d}No passo seis: [p=0.2] *oitenta contra sessenta e quatro.* [p=0.2] A reta ainda na "
        "frente. [p=0.4] {e}No passo sete: [p=0.2] *noventa contra cento e vinte e oito.* [p=0.2] Ultrapassou!"),
    dict(id="10", block="corrida2", text=
        "{t}Por que ela nunca mais perde? [p=0.4] {a}A reta ganha sempre *dez.* [p=0.4] "
        "{b}A curva *dobra:* [p=0.2] do passo seis para o sete, [p=0.2] ela ganhou *sessenta e quatro* de uma vez. "
        "[p=0.4] {c}No passo dez, [p=0.2] a reta tem cento e vinte. [p=0.2] A curva tem *mil e vinte e quatro.* "
        "[p=0.4] {d}Por isso, [p=0.2] toda exponencial crescente [p=0.2] *ultrapassa qualquer reta.*"),

    # ================= BLOCO D: TRÊS PONTOS =================
    dict(id="11", block="tres", text=
        "{t}Basta conferir *dois* pontos? [p=0.4] {a}Lembra da Questão três do episódio dois? [p=0.2] Cinquenta mil, "
        "[p=0.2] quarenta mil, [p=0.2] trinta e dois mil. [p=0.4] {b}A reta "
        "*cinquenta mil menos dez mil t* [p=0.2] acerta t igual a zero [p=0.2] e acerta t igual a um. [p=0.4] {c}Em t "
        "igual a dois, [p=0.2] ela dá *trinta mil.* [p=0.2] A tabela diz *trinta e dois mil.* [p=0.4] {d}Duas leis podem "
        "*concordar em dois pontos* [p=0.2] e *brigar no terceiro.*"),
    dict(id="12", block="atalho_tres", text=
        "{t}Atalho: [p=0.2] antes de marcar uma lei, [p=0.2] substitua *t igual a zero,* [p=0.2] *um* [p=0.2] e "
        "*dois.* [p=0.4] {b}Zero confere o valor inicial; [p=0.2] um e dois, [p=0.2] o *fator.* [p=0.4] {c}Menos de "
        "um minuto."),

    # ================= BLOCO E: SÓ CITADO =================
    dict(id="13", block="pg", text=
        "{t}Esse padrão tem nome? [p=0.4] {a}Tem. [p=0.2] Os valores de uma exponencial em tempos iguais [p=0.2] "
        "formam uma *progressão geométrica:* [p=0.2] uma lista em que cada termo [p=0.2] é o anterior *vezes o mesmo "
        "número.* [p=0.4] {b}Ela tem *série própria.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}A tabela *oitenta,* [p=0.2] *cento e vinte,* [p=0.2] *cento e oitenta,* [p=0.2] "
        "*duzentos e setenta.* [p=0.4] {b}É afim ou exponencial? [p=0.2] E qual é o *próximo valor?* [p=0.4] "
        "{c}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Diferenças: [p=0.2] quarenta, [p=0.2] sessenta, [p=0.2] noventa. [p=0.2] *Não* "
        "são iguais. [p=0.2] Não é afim. [p=0.4] {b}Razões: [p=0.2] cento e vinte dividido por oitenta, [p=0.2] *um e "
        "meio.* [p=0.2] As outras, [p=0.2] também um e meio. [p=0.4] {c}Razão constante: [p=0.2] *exponencial,* [p=0.2] "
        "fator um e meio. [p=0.4] {d}Próximo valor: [p=0.2] duzentos e setenta vezes um e meio, [p=0.2] *quatrocentos "
        "e cinco.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] diferença constante é afim; [p=0.2] razão constante "
        "é exponencial. [p=0.5] {b}Dois: [p=0.2] toda exponencial crescente [p=0.2] acaba ultrapassando qualquer reta. "
        "[p=0.5] {c}Três: [p=0.2] teste sempre três pontos, [p=0.2] não dois."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *dois pontos certos* [p=0.2] "
        "garantem a lei certa. [p=0.4] {b}Parece certo, [p=0.2] porque dois pontos bastam para desenhar uma reta. "
        "[p=0.4] {c}Mas dois elevado a t [p=0.2] e um mais t [p=0.2] dão *um e dois* nos dois primeiros pontos. "
        "[p=0.2] Em t igual a dois, [p=0.2] *quatro contra três.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] confundir o *ganho de uma semana* [p=0.2] com o *total acumulado.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque quem ganha mais parece estar na frente. [p=0.4] {c}Na "
        "corrida, [p=0.2] do passo quatro para o cinco, [p=0.2] a curva ganha dezesseis [p=0.2] e a reta só dez. "
        "[p=0.2] Mas o total é *trinta e dois contra setenta.*"),

    # ================= QUESTÃO 5 (NÓS FAZEMOS) =================
    dict(id="19", block="q5", text=
        "{t}Questão no estilo do ENEM, [p=0.2] para fazermos juntos. [p=0.4] {a}Hoje, o perfil "
        "*A* tem *mil* seguidores [p=0.2] e ganha *trezentos* por semana, [p=0.2] sempre o mesmo número. [p=0.3] O "
        "perfil *B* tem hoje *cem* seguidores, [p=0.2] e esse número *dobra* a cada semana. [p=0.3] O menor número de "
        "semanas [p=0.2] ao fim do qual B terá mais seguidores que A é: [p=0.3] {qa}A: [p=0.2] três semanas. [p=0.2] "
        "{qb}B: [p=0.2] quatro. [p=0.2] {qc}C: [p=0.2] cinco. [p=0.2] {qd}D: [p=0.2] seis. [p=0.2] {qe}E: [p=0.2] "
        "nenhum: [p=0.2] B nunca ultrapassa A. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="20", block="q5", text=
        "{t}O A é afim: [p=0.2] *mil mais trezentos t.* [p=0.2] O B é exponencial: [p=0.2] *cem vezes dois elevado a "
        "t.* [p=0.4] {a}Semana três: [p=0.2] A tem mil e novecentos; [p=0.2] B tem oitocentos. [p=0.4] {b}Semana "
        "quatro: [p=0.2] A tem *dois mil e duzentos;* [p=0.2] B tem *mil e seiscentos.* [p=0.2] Ainda perde! [p=0.4] "
        "{c}Semana cinco: [p=0.2] A tem dois mil e quinhentos; [p=0.2] B tem *três mil e duzentos.* [p=0.2] "
        "Ultrapassou. [p=0.3] {ok}*Letra C!*"),
    dict(id="21", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A confunde *ganho com total:* [p=0.2] na terceira semana, [p=0.2] B já "
        "ganha quatrocentos contra trezentos, [p=0.2] mas tem bem menos. [p=0.4] {xb}A B compara o B "
        "com os *mil iniciais* do A, [p=0.2] esquecendo que o A também cresce. [p=0.4] {xd}A D conta *hoje* como a "
        "primeira semana. [p=0.4] {xe}E a E esquece a tartaruga e a lebre: [p=0.2] a exponencial *sempre* passa a "
        "reta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="22", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] diferença constante é afim; [p=0.2] razão "
        "constante é exponencial. [p=0.5] {b}Dois: [p=0.2] toda exponencial crescente [p=0.2] acaba ultrapassando "
        "qualquer reta. [p=0.5] {c}Três: [p=0.2] teste sempre três pontos, [p=0.2] não dois."),

    # ================= PONTE E CTA =================
    dict(id="23", block="ponte", text=
        "{a}Se *P de t* é igual a *mil vezes três elevado a t sobre dois,* [p=0.3] {b}quando a população chega a "
        "*oitenta e um mil?* [p=0.4] {c}Dá para achar t *sem tentar um por um.* [p=0.4] {d}Próximo episódio."),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já viu alguma coisa crescer como a lebre, [p=0.2] dobrando "
        "sem parar? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
