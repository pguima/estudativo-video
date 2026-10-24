# Roteiro — Progressão Geométrica, Episódio 4 de 5: a PG disfarçada (juros compostos, meia-vida e depreciação)
# Base: Estudos/Enem/estudos/01-matematica/32-progressao-geometrica-soma-infinita.html — tabela e exemplo de meia-vida da
#   seção 08 + estratégia 1 (e a 2, como pergunta de leitura) da seção 09 + questão NOVA do carro (texto do roteiros.md,
#   não está no material). Questão 2 do material NÃO usada.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A MÁQUINA ×q (episódio 1): juros compostos passam pela ×(1 + i), a meia-vida pela ×1/2, a depreciação pela ×(1 − i).
#   CONTE OS PERÍODOS ANTES DE QUALQUER CONTA: tempo total ÷ duração de um período.
#   O FATOR É O QUE SOBRA: quem perde 20% fica com 80%.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida (sem reensinar): M = C(1 + i)^t (série de Juros Compostos), meia-vida (série de Função Exponencial) e o
#   termo contado do instante zero, a₀ · q^t (episódio 1).
# Bloco b = exemplo da seção 08 (80 g, meia-vida de 5 anos, 20 anos → 4 meias-vidas → 5 g), como revisão.
# Bloco c = estratégia 1 da seção 09 (meia-vida de 8 h, em 2 dias → 48 ÷ 8 = 6 meias-vidas).
# DESVIO do prompt (para não entregar a questão do carro, "você faz", com pausa):
#   bloco d (percentual × linear) usa um carro NOSSO: R$ 40.000,00 perdendo 25% ao ano → 30 000, 22 500, 16 875 (tira
#     10 000, 7 500, 5 625) contra o linear que tira sempre 10 000 → 30 000, 20 000, 10 000.
#   a animação das barras 80 000 → 64 000 → 51 200 → 40 960 com a reta tracejada da queda linear (direção visual) aparece
#     SÓ na resolução da questão, depois da pausa.
#   as três esteiras (cofre ×1,05, frasco ×1/2, carro ×0,8) começam todas em 100 (100 → 105 → 110,25; 100 → 50 → 25;
#     100 → 80 → 64), sem o preço do carro da questão.
#   erros clássicos usam os números do "nós fazemos" (já resolvido) e do bloco c: taxa no lugar do fator 50 000 · 0,1² =
#     500; linear 50 000 − 2 · 5 000 = 40 000 (certo 40 500); período a menos/mais em "8 h, 2 dias": 5 ou 7 (certo 6).
# Acréscimos NOSSOS (marcados): atalhos verdes "o fator é o que sobra: ganha i → 1 + i; perde i → 1 − i" (cena 06) e
#   "tempo total ÷ duração de um período, na mesma unidade" (cena 09); a conferência ano a ano na questão.
# Nós fazemos (prompt): carro de R$ 50.000,00 perdendo 10% ao ano → q = 0,9; 50 000 · 0,81 = R$ 40.500,00.
# QUESTÃO NOVA, CARRO ("você faz", com pausa): gabarito C (R$ 40.960,00). Erradas = roteiros.md (A 80 000 · 0,2³ = 640,
#   taxa como fator; B 32 000, linear tirando 16 000 por ano; D 51 200, aplicou o n − 1 e parou em 2 anos; E 64 000, a
#   queda uma vez só).
# Frases-chave (meio e fim, idênticas): 1. Porcentagem fixa por período é PG.
#   2. Conte os períodos: tempo total dividido pela duração de um período.
#   3. O fator é o que sobra: perder 20% é multiplicar por 0,8.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A PG disfarçada: juros, meia-vida e carro usado · Matemática ENEM, PG episódio 4"

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
        "{a}Você já estudou PG *sem saber:* [p=0.3] {b}na série de Juros Compostos, [p=0.2] um saldo que *dobra* a cada "
        "sete anos [p=0.2] ficava *oito vezes maior* em vinte e um anos, [p=0.2] *não três.* [p=0.5] {c}Hoje você vê a "
        "*mesma máquina* [p=0.2] em remédios, [p=0.2] populações [p=0.2] e carros usados."),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Progressão geométrica.* [p=0.4] {a}Ao final, [p=0.2] você vai "
        "*reconhecer a PG* em qualquer enunciado de crescimento ou queda percentual [p=0.4] {b}e *contar os períodos* "
        "sem errar."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Juros Compostos: [p=0.2] *M é igual a C vezes um mais i, "
        "elevado a t.* [p=0.2] O *montante* é o saldo final. [p=0.4] {b}Da série de Função Exponencial: [p=0.2] "
        "*meia-vida* é o tempo para uma quantidade cair *à metade.* [p=0.4] {c}E do episódio um: [p=0.2] contando do "
        "instante zero, [p=0.2] o valor é *a zero vezes q elevado a t.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três coisas do dia a dia. [p=0.4] {a}Um *extrato de poupança.* [p=0.3] {b}A *bula* de um remédio: "
        "[p=0.2] meia-vida de oito horas. [p=0.3] {c}E o *anúncio* de um carro usado. [p=0.4] {d}O que têm em comum? "
        "[p=0.4] A cada período, [p=0.2] o valor é *multiplicado pelo mesmo número.*"),

    # ================= BLOCO A: A TABELA DA SEÇÃO 08 =================
    dict(id="05", block="maquinas", text=
        "{t}Que máquina é essa? [p=0.4] {a}É a *máquina vezes q* do episódio um. [p=0.4] {b}No cofre, [p=0.2] os "
        "*juros compostos,* [p=0.2] que são juros sobre juros: [p=0.2] a máquina é *um mais i.* [p=0.4] "
        "{c}No remédio, [p=0.2] *vezes um meio* [p=0.2] a cada "
        "meia-vida. [p=0.4] {d}No carro, [p=0.2] a *depreciação percentual:* [p=0.2] perder uma porcentagem fixa do "
        "valor por período. [p=0.2] A máquina é *um menos i.* [p=0.4] {e}População crescendo i por cento ao "
        "ano? [p=0.2] *Um mais i.*"),
    dict(id="06", block="atalho_fator", text=
        "{t}Atalho para achar a máquina. [p=0.4] {a}*O fator é o que sobra.* [p=0.4] {b}Ganhou i por cento? [p=0.2] "
        "Fica com *um mais i.* [p=0.4] {c}Perdeu i por cento? [p=0.2] Fica com *um menos i:* [p=0.2] quem perde vinte "
        "por cento [p=0.2] *fica com oitenta.*"),

    # ================= BLOCO B: MEIA-VIDA (REVISÃO) =================
    dict(id="07", block="meiavida", text=
        "{t}E a meia-vida, [p=0.2] como fica? [p=0.4] {a}Oitenta gramas de uma substância, [p=0.2] meia-vida de *cinco "
        "anos.* [p=0.2] Quanto sobra em *vinte anos?* [p=0.4] {b}Primeiro, conte: [p=0.2] vinte dividido por cinco, "
        "[p=0.2] *quatro meias-vidas.* [p=0.4] {c}A máquina age quatro vezes: [p=0.2] oitenta vezes um meio *elevado a "
        "quatro.* [p=0.4] {d}Oitenta dividido por dezesseis: [p=0.2] *cinco gramas.* [p=0.4] {e}O mesmo raciocínio "
        "da série de Função Exponencial."),

    # ================= BLOCO C: CONTAR PERÍODOS =================
    dict(id="08", block="periodos", text=
        "{t}E quando as unidades são diferentes? [p=0.4] {a}Meia-vida de *oito horas.* [p=0.2] Em *dois dias,* [p=0.2] "
        "quantas meias-vidas? [p=0.4] {b}Não dá para dividir dois por oito. [p=0.2] Primeiro, [p=0.2] tudo em horas: "
        "[p=0.2] dois dias são *quarenta e oito horas.* [p=0.4] {c}Quarenta e oito dividido por oito: [p=0.2] *seis "
        "meias-vidas.* [p=0.4] {d}O expoente é *quantas vezes o fator age:* [p=0.2] seis."),
    dict(id="09", block="atalho_periodos", text=
        "{t}Atalho antes de qualquer conta. [p=0.4] {a}*Conte os períodos:* [p=0.2] tempo total [p=0.2] dividido pela "
        "duração de *um* período. [p=0.4] {b}E sempre *na mesma unidade.* [p=0.4] {c}É o "
        "*expoente.*"),

    # ================= BLOCO D: PERCENTUAL × LINEAR =================
    dict(id="10", block="linear", text=
        "{t}Perder uma porcentagem é perder sempre *o mesmo valor?* [p=0.4] {a}Um carro de *quarenta mil reais* "
        "[p=0.2] perde *vinte e cinco por cento* ao ano. [p=0.4] {b}No primeiro ano, [p=0.2] perde dez mil: [p=0.2] "
        "vai a *trinta mil.* [p=0.4] {c}No segundo, [p=0.2] vinte e cinco por cento de trinta mil: [p=0.2] perde *sete "
        "mil e quinhentos.* [p=0.4] {d}Perder sempre dez mil [p=0.2] "
        "seria uma *queda linear,* [p=0.2] uma PA, [p=0.2] da série de Função Afim. [p=0.4] {e}A porcentagem *tira "
        "cada vez menos:* [p=0.2] é PG."),

    # ================= BLOCO E: TERMO, SOMA FINITA OU INFINITA =================
    dict(id="11", block="leitura", text=
        "{t}E qual é a pergunta da questão? [p=0.4] {a}*Quanto vale no fim?* [p=0.2] É *termo.* [p=0.4] {b}*Quanto ao "
        "todo?* [p=0.2] É *soma finita.* [p=0.4] {c}*Se continuar para sempre?* [p=0.2] *Soma infinita.* [p=0.4] "
        "{d}Hoje, [p=0.2] é quase sempre *termo.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um carro de *cinquenta mil reais* [p=0.2] perde *dez por cento* do valor ao ano. "
        "[p=0.4] {b}Qual é a *razão* da PG? [p=0.2] E quanto ele vale em *dois anos?* [p=0.4] {c}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Perde dez por cento, [p=0.2] *fica com noventa.* [p=0.2] A razão é *zero vírgula "
        "nove.* [p=0.4] {b}Dois anos, [p=0.2] *dois períodos.* [p=0.2] Zero vírgula nove ao quadrado: [p=0.2] *zero "
        "vírgula oitenta e um.* [p=0.4] {c}Cinquenta mil vezes zero vírgula oitenta e um: [p=0.2] *quarenta mil e "
        "quinhentos reais.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] porcentagem fixa por período é PG. [p=0.5] {b}Dois: "
        "[p=0.2] conte os períodos: [p=0.2] tempo total dividido pela duração de um período. [p=0.5] {c}Três: [p=0.2] "
        "o fator é o que sobra: [p=0.2] perder vinte por cento é multiplicar por zero vírgula oito."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar a *taxa* no lugar do *fator.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque é o número que está no enunciado. [p=0.4] {c}Mas cinquenta "
        "mil vezes zero vírgula um ao quadrado [p=0.2] dá *quinhentos reais.* [p=0.2] "
        "Use o que *sobra:* [p=0.2] zero vírgula nove."),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] tratar a queda percentual como *linear.* [p=0.4] {b}Parece certo, [p=0.2] porque no "
        "primeiro ano a perda é mesmo cinco mil. [p=0.4] {c}Tirar cinco mil duas vezes [p=0.2] dá quarenta mil. "
        "[p=0.2] O certo é *quarenta mil e quinhentos:* [p=0.2] no segundo ano, [p=0.2] a perda é menor."),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] contar *um período a mais ou a menos.* [p=0.4] {b}Parece certo, [p=0.2] porque a gente "
        "conta os momentos, [p=0.2] e não os intervalos. [p=0.4] {c}Em dois dias, [p=0.2] com meia-vida de "
        "oito horas, [p=0.2] não são cinco nem sete: [p=0.2] são *seis.*"),

    # ================= QUESTÃO NOVA (VOCÊ FAZ) =================
    dict(id="18", block="q", text=
        "{t}Questão no estilo do ENEM, [p=0.2] *para você fazer.* [p=0.4] {a}Um carro novo custa *oitenta mil "
        "reais* [p=0.2] e, segundo uma projeção, [p=0.2] perde *vinte por cento* do seu valor a cada ano, [p=0.2] "
        "sempre em relação ao valor do ano anterior. [p=0.3] Três anos após a compra, [p=0.2] o valor projetado do "
        "carro será de: [p=0.3] {qa}A: [p=0.2] seiscentos e quarenta reais. [p=0.2] {qb}B: [p=0.2] trinta e dois mil "
        "reais. [p=0.2] {qc}C: [p=0.2] quarenta mil, novecentos e sessenta reais. [p=0.2] {qd}D: [p=0.2] cinquenta e "
        "um mil e duzentos reais. [p=0.2] {qe}E: [p=0.2] sessenta e quatro mil reais. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="19", block="q", text=
        "{t}Vamos conferir. [p=0.3] {a}O fator é o que sobra: [p=0.2] um menos zero vírgula dois, [p=0.2] *zero "
        "vírgula oito.* [p=0.4] {b}Três anos, [p=0.2] *três períodos,* [p=0.2] contados do instante zero. [p=0.4] "
        "{c}Oitenta mil vezes zero vírgula oito ao cubo, [p=0.2] que é zero vírgula quinhentos e doze: [p=0.2] "
        "*quarenta mil, novecentos e sessenta.* [p=0.4] {d}Ano a ano: [p=0.2] sessenta e quatro mil, [p=0.2] cinquenta "
        "e um mil e duzentos, [p=0.2] quarenta mil, novecentos e sessenta. [p=0.3] {ok}*Letra C!*"),
    dict(id="20", block="q", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A usa a *taxa* como fator: [p=0.2] zero vírgula dois ao cubo. [p=0.4] {xb}A "
        "B faz a queda *linear,* [p=0.2] tirando dezesseis mil todo ano. [p=0.4] {xd}A D aplica o *n menos um* onde "
        "ele não cabe [p=0.2] e para em dois anos. [p=0.4] {xe}E a E aplica a queda *uma vez só.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="21", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] porcentagem fixa por período é PG. [p=0.5] "
        "{b}Dois: [p=0.2] conte os períodos: [p=0.2] tempo total dividido pela duração de um período. [p=0.5] {c}Três: "
        "[p=0.2] o fator é o que sobra: [p=0.2] perder vinte por cento é multiplicar por zero vírgula oito."),

    # ================= PONTE E CTA =================
    dict(id="22", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] "
        "{c}e treinamos para o ENEM."),
    dict(id="23", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] em que outro lugar do seu dia a dia [p=0.2] você já viu essa "
        "máquina de multiplicar? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você "
        "adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso "
        "em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
