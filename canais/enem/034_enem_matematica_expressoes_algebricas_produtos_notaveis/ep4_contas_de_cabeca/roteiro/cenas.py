# Roteiro — Expressões Algébricas e Produtos Notáveis, Episódio 4 de 5: contas de cabeça com produtos notáveis
# Base: Estudos/Enem/estudos/01-matematica/19-expressoes-algebricas-produtos-notaveis.html — seção 08 + Questão 3 (seção 12).
#   A Questão 8 (+30% e −30%) NÃO aparece como questão: só como exemplo narrado da conexão com Porcentagem (bloco d).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   OS GÊMEOS: dois números à mesma distância de um redondo (49 e 51 moram a 1 passo do 50). Multiplicar gêmeos é
#     "redondo ao quadrado menos passo ao quadrado".
#   O ALARME: conta grande demais para a prova é um aviso de que tem produto notável escondido (alarme verde "ATALHO!").
#   PERTO DO REDONDO: o quadrado é redondo ao quadrado, mais (ou menos) o dobro, mais o passinho ao quadrado.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt (seção 08): 101² = 10 201 · 998² = 996 004 · 49 · 51 = 2 499 · 87² − 13² = 7 400 ·
#   2 025² − 2 024² = 4 049 · conexão: 1,3 · 0,7 = 1 − 0,09 = 0,91 (9% ABAIXO) e 0,2² = 0,04 (série de Porcentagem).
#   Nós fazemos: 48 · 52 = 2 500 − 4 = 2 496 · 103² = 10 000 + 600 + 9 = 10 609.
# DESVIOS DO PROMPT (para não entregar a Questão 3, que é "você faz"):
#   - A reta numérica dos gêmeos usa 49 e 51 em volta do 50 no bloco b; a reta com 997 e 1 003 em volta do 1 000 (a
#     animação principal pedida) aparece na RESOLUÇÃO da Q3, depois da pausa.
#   - O depósito do concreto só faz a pergunta (sem conta); a resposta fica para a Q3.
#   - Erros 1 e 2 usam números NOSSOS, 503 · 497 (certo 250 000 − 9 = 249 991; erro 1 aproxima para 250 000; erro 2
#     subtrai 2 · 3 = 6 e dá 249 994). Erro 3 usa o 998² do bloco a (esquecer o +4 dá 996 000). Conferido em Python.
# Conexão com Porcentagem, exemplo NOSSO: R$ 100,00 → +30% → R$ 130,00 → −30% → R$ 91,00.
# QUESTÃO 3 (você faz, texto idêntico): 1 003 · 997 = (1 000 + 3)(1 000 − 3) = 1 000 000 − 9 = 999 991 → A.
#   Erradas (material): D 1 000 000 = aproxima e ignora o 3² · E 1 000 009 = troca o sinal do 9 · B 999 994 = subtrai
#   2 · 3 = 6 (termo do meio de um quadrado) · C 999 997 = subtrai só 3.
# CTA (comentários): 99² de cabeça = 10 000 − 200 + 1 = 9 801.
# Atalhos (verde): "perto do redondo: redondo², ± o dobro, + passo²" · "gêmeos: redondo² − passo²" · "vizinhos: a diferença
#   de quadrados é a soma deles" · "taxa p para cima e para baixo: perde p²".
# Frases-chave (meio e fim, idênticas): 1. Gêmeos ao redor do redondo: redondo ao quadrado menos o passo ao quadrado.
#   2. Diferença de quadrados vira soma vezes diferença. 3. Conta grande demais é aviso de atalho.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "1 003 × 997 de cabeça? Contas grandes com produtos notáveis · Matemática ENEM, Álgebra episódio 4"

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
        "{a}Quanto é *oitenta e sete ao quadrado menos treze ao quadrado?* [p=0.5] {b}Pela conta direta, [p=0.2] sete "
        "mil, quinhentos e sessenta e nove [p=0.2] menos cento e sessenta e nove. [p=0.5] {c}Pelo produto notável, "
        "[p=0.2] *cem vezes setenta e quatro* [p=0.2] igual a *sete mil e quatrocentos,* [p=0.3] {d}em *três "
        "segundos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *reconhecer na hora* [p=0.2] quando uma conta grande *tem atalho.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes. [p=0.3] {a}Do episódio dois: [p=0.2] o *quadrado da soma* e o *da "
        "diferença* [p=0.2] têm o termo do meio, *duas vezes a vezes b.* [p=0.4] {b}E a *soma pela diferença* dá "
        "*a ao quadrado menos b ao quadrado,* [p=0.2] sem termo do meio. [p=0.4] {c}Da série de Porcentagem: "
        "[p=0.2] aumentar *p* é multiplicar por *um mais p;* [p=0.2] descontar *p* é multiplicar por *um menos p.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Um depósito recebe *mil e três caixas,* [p=0.2] cada uma com *novecentos e noventa e sete parafusos.* "
        "[p=0.4] {b}Quem faria essa conta *sem calculadora?* [p=0.4] {c}Com o atalho certo, [p=0.2] são *cinco segundos.* "
        "[p=0.4] {d}Guarde essa conta: [p=0.2] ela volta no fim, [p=0.2] e quem resolve é *você.*"),
    dict(id="05", block="defs", text=
        "{t}Duas palavras. [p=0.3] {a}*Número redondo* [p=0.2] é o que termina em zeros: [p=0.2] "
        "cinquenta, cem, mil. [p=0.4] {b}*Distância até o redondo* [p=0.2] é quantos passos faltam ou sobram: "
        "[p=0.2] o noventa e oito está a *dois passos* do cem. [p=0.4] {c}E guarde o *alarme:* [p=0.2] conta grande "
        "demais para a prova [p=0.2] é *aviso de produto notável escondido.*"),

    # ================= BLOCO A: QUADRADO PERTO DO REDONDO =================
    dict(id="06", block="quadrado", text=
        "{t}Quanto é *cento e um ao quadrado?* [p=0.4] {a}Cento e um é *cem mais um:* [p=0.2] o quadrado da soma. "
        "[p=0.4] {b}Cem ao quadrado: [p=0.2] *dez mil.* [p=0.3] {c}Duas vezes cem vezes um: [p=0.2] *duzentos.* "
        "[p=0.3] {d}Um ao quadrado: [p=0.2] *um.* [p=0.4] {e}Somando: [p=0.2] *dez mil, duzentos e um.*"),
    dict(id="07", block="quadrado", text=
        "{t}E *novecentos e noventa e oito ao quadrado?* [p=0.4] {a}É *mil menos dois:* [p=0.2] o quadrado da "
        "diferença. [p=0.4] {b}Mil ao quadrado, [p=0.2] *um milhão.* [p=0.3] {c}*Menos* duas vezes mil vezes dois, "
        "[p=0.2] *quatro mil.* [p=0.3] {d}E *mais* dois ao quadrado, [p=0.2] *quatro.* [p=0.4] {e}Resultado: "
        "[p=0.2] *novecentos e noventa e seis mil e quatro.* [p=0.4] {f}Atalho: [p=0.2] perto do redondo, [p=0.2] o "
        "quadrado é *redondo ao quadrado, [p=0.2] mais ou menos o dobro, [p=0.2] mais o passinho ao quadrado.*"),

    # ================= BLOCO B: GÊMEOS =================
    dict(id="08", block="gemeos", text=
        "{t}E quanto é *quarenta e nove vezes cinquenta e um?* [p=0.4] {a}Olhe a reta: [p=0.2] os dois estão a *um "
        "passo* do cinquenta, [p=0.2] um de cada lado. [p=0.4] {b}São *gêmeos:* [p=0.2] moram à mesma distância de um "
        "redondo. [p=0.4] {c}Quarenta e nove é *cinquenta menos um.* [p=0.2] Cinquenta e um é *cinquenta mais um.* "
        "[p=0.2] Soma pela diferença!"),
    dict(id="09", block="gemeos", text=
        "{t}E aqui não tem termo do meio. [p=0.4] {a}Cinquenta ao quadrado: [p=0.2] *dois mil e "
        "quinhentos.* [p=0.3] {b}Menos um ao quadrado: [p=0.2] *menos um.* [p=0.4] {c}Resultado: [p=0.2] *dois mil, "
        "quatrocentos e noventa e nove.* [p=0.4] {d}Atalho: [p=0.2] multiplicar gêmeos é *redondo ao quadrado [p=0.2] "
        "menos passo ao quadrado.*"),

    # ================= BLOCO C: DIFERENÇA DE DOIS QUADRADOS =================
    dict(id="10", block="difquad", text=
        "{t}E a conta do começo? [p=0.4] {a}*Diferença de dois quadrados* [p=0.2] é um quadrado *menos* outro. [p=0.4] {b}É a soma pela diferença *ao contrário:* [p=0.2] vira *soma vezes diferença.* [p=0.4] "
        "{c}Oitenta e sete mais treze, [p=0.2] *cem.* [p=0.2] Oitenta e sete menos treze, [p=0.2] *setenta e quatro.* "
        "[p=0.4] {d}Cem vezes setenta e quatro: [p=0.2] *sete mil e quatrocentos.*"),
    dict(id="11", block="difquad", text=
        "{t}E esta? [p=0.3] {a}*Dois mil e vinte e cinco ao quadrado, [p=0.2] menos dois mil e "
        "vinte e quatro ao quadrado.* [p=0.4] {b}Alarme: [p=0.2] *conta grande demais!* [p=0.4] {c}Soma: [p=0.2] "
        "*quatro mil e quarenta e nove.* [p=0.2] Diferença: [p=0.2] *um.* [p=0.2] {d}Vezes um, [p=0.2] *a própria soma.* "
        "[p=0.4] {e}Atalho: [p=0.2] quando os dois números são *vizinhos,* [p=0.2] a diferença dos "
        "quadrados é *a soma deles.*"),

    # ================= BLOCO D: CONEXÃO COM PORCENTAGEM =================
    dict(id="12", block="porcent", text=
        "{t}Por que subir e descer a *mesma porcentagem* dá prejuízo? [p=0.4] {a}Um preço sobe *trinta por "
        "cento* [p=0.2] e depois cai *trinta por cento.* [p=0.4] {b}Subir é multiplicar por *um vírgula três.* "
        "[p=0.2] Descer é multiplicar por *zero vírgula sete.* [p=0.4] {c}Um mais zero vírgula três, [p=0.2] vezes um "
        "menos zero vírgula três: [p=0.2] *soma pela diferença!* [p=0.4] {d}Dá *um menos zero vírgula zero nove,* "
        "[p=0.2] *zero vírgula noventa e um.* [p=0.4] {e}Cem reais viram *noventa e um:* [p=0.2] *nove por cento "
        "abaixo* do original."),
    dict(id="13", block="porcent", text=
        "{a}Na série de Porcentagem você viu que *mais vinte* e *menos vinte por cento* [p=0.2] dão *menos quatro.* "
        "[p=0.4] {b}Zero vírgula dois ao quadrado: [p=0.2] *zero vírgula zero quatro.* [p=0.4] {c}Agora você sabe *de "
        "onde vem:* [p=0.2] sobra sempre uma perda de *p ao quadrado.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Calcule de cabeça: [p=0.2] *quarenta e oito vezes cinquenta e dois.* [p=0.4] {b}E "
        "*cento e três ao quadrado.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Quarenta e oito e cinquenta e dois são *gêmeos:* [p=0.2] *dois passos* do "
        "cinquenta. [p=0.2] Dois mil e quinhentos *menos quatro:* [p=0.2] *dois mil, quatrocentos e noventa e seis.* "
        "[p=0.4] {b}Cento e três é *cem mais três.* [p=0.2] Dez mil, [p=0.2] mais seiscentos, [p=0.2] mais nove: "
        "[p=0.2] *dez mil, seiscentos e nove.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] gêmeos ao redor do redondo: [p=0.2] redondo ao "
        "quadrado menos o passo ao quadrado. [p=0.5] {b}Dois: [p=0.2] diferença de quadrados vira soma vezes "
        "diferença. [p=0.5] {c}Três: [p=0.2] conta grande demais é aviso de atalho."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] em *quinhentos e três vezes quatrocentos e noventa "
        "e sete,* [p=0.2] aproximar para *duzentos e cinquenta mil.* [p=0.4] {b}Parece certo: [p=0.2] um sobe três, "
        "o outro desce três: [p=0.2] se compensam? [p=0.4] {c}Mas sobra o *menos três ao quadrado:* "
        "[p=0.2] o certo é *duzentos e quarenta e nove mil, novecentos e noventa e um.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] na mesma conta, subtrair *seis,* duas vezes três. [p=0.4] {b}Parece certo: [p=0.2] é o "
        "termo do meio do quadrado. [p=0.4] {c}Mas gêmeos *não têm termo do meio.* [p=0.2] Sai o *passo ao quadrado:* "
        "[p=0.2] *nove,* não seis."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] em novecentos e noventa e oito ao quadrado, [p=0.2] *esquecer o mais quatro* do final. "
        "[p=0.4] {b}Parece certo: [p=0.2] é *menos* dois, tudo parece de menos. [p=0.4] {c}Mas o quadrado "
        "do passo é *sempre positivo:* [p=0.2] menos dois vezes menos dois, [p=0.2] *mais quatro.*"),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="20", block="q3", text=
        "{t}Agora é com você, [p=0.2] numa questão do nosso material. [p=0.4] {a}Um depósito recebeu *mil e "
        "três caixas,* [p=0.2] cada uma com *novecentos e noventa e sete parafusos.* [p=0.2] O número total de "
        "parafusos recebidos é: [p=0.4] {qa}A: [p=0.2] novecentos e noventa e nove mil, novecentos e noventa e um. "
        "[p=0.3] {qb}B: [p=0.2] novecentos e noventa e nove mil, novecentos e noventa e quatro. [p=0.3] {qc}C: [p=0.2] "
        "novecentos e noventa e nove mil, novecentos e noventa e sete. [p=0.3] {qd}D: [p=0.2] um milhão. [p=0.3] "
        "{qe}E: [p=0.2] um milhão e nove. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="21", block="q3", text=
        "{t}Vamos conferir. [p=0.3] {a}Na reta, [p=0.2] o mil fica no meio. [p=0.2] O novecentos e noventa e sete "
        "*desce três passos;* [p=0.2] o mil e três *sobe três.* [p=0.2] São gêmeos! [p=0.4] {b}Redondo ao quadrado: "
        "[p=0.2] *um milhão.* [p=0.2] Menos o passo ao quadrado: [p=0.2] *nove.* [p=0.4] {c}Resultado: [p=0.2] "
        "*novecentos e noventa e nove mil, novecentos e noventa e um.* [p=0.3] {ok}*Letra A!*"),
    dict(id="22", block="q3", text=
        "{t}E as pegadinhas? [p=0.3] {xd}A D aproxima tudo e *ignora o três ao quadrado.* [p=0.4] {xe}A E *troca o "
        "sinal* do nove. [p=0.4] {xb}A B subtrai *seis,* [p=0.2] como se fosse o termo do meio de um quadrado. "
        "[p=0.4] {xc}E a C subtrai *só três.* [p=0.4] {c}Confira: [p=0.2] quase mil caixas de quase mil "
        "parafusos, [p=0.2] *pouco menos* de um milhão."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="23", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] gêmeos ao redor do redondo: [p=0.2] redondo ao "
        "quadrado menos o passo ao quadrado. [p=0.5] {b}Dois: [p=0.2] diferença de quadrados vira soma vezes "
        "diferença. [p=0.5] {c}Três: [p=0.2] conta grande demais é aviso de atalho."),

    # ================= PONTE E CTA =================
    dict(id="24", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e "
        "treinamos com questões inéditas."),
    dict(id="25", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto é *noventa e nove ao quadrado,* de cabeça? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
