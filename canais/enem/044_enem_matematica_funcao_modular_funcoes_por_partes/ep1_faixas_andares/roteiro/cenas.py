# Roteiro — Função Modular e Funções por Partes, Episódio 1 de 5: funções por partes (ache a faixa antes de calcular)
# Base: Estudos/Enem/estudos/01-matematica/29-funcao-modular-funcoes-por-partes.html — seção 03 + Questão 8 (seção 12)
#   + questão NOVA do frete (texto do prompt, não está no material). A Questão 5 do material fica de fora (duplica a Q2 de
#   Conceito de Função).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   O PRÉDIO DE ANDARES: a função por partes é um prédio; primeiro descubra em que andar o valor mora (o 26 sobe de
#     elevador até o 3º andar, que acende), só depois use a regra daquele andar.
#   CADA FAIXA PARTE DE ONDE A ANTERIOR PAROU: o 100 da 3ª linha é a conta exatamente em 20 m³ (40 + 6 · 10).
#   A CATRACA: "hora ou fração" — encostou na hora seguinte, pagou a hora inteira.
# Frases do usuário mantidas IGUAIS: gancho, promessa (com "Ao final desta aula", como nos outros episódios), as 3
#   frases-chave e a ponte.
# Exemplos:
#   Blocos b–e: conta de água da seção 03 (26 m³ → 154) e estacionamento de 2 h 05 min (→ R$ 18,00), como pede o prompt.
#   Nós fazemos (prompt): academia R$ 80,00 até 12 aulas + R$ 7,00 por aula a mais; 17 aulas → 80 + 5 · 7 = 115.
#   ERROS com números já resolvidos na aula (nada da Q8 nem do frete):
#     1) 26 m³ pela 2ª linha: 40 + 6 · 16 = 136 (certo 154; 26 > 20 → 3ª linha).
#     2) estacionamento 2 h 30 min proporcional: 10 + 4 · 1,5 = 16 (certo 10 + 2 · 4 = 18).
#     3) academia sem a parte fixa: 7 · 5 = 35 (certo 80 + 35 = 115).
# QUESTÃO 8 (eu faço): C = 50 se 0 ≤ x ≤ 10; 50 + 8(x − 10) se x > 10. Conferência f(10) = 50 pelas duas linhas (sem salto),
#   f(15) = 90. Erradas (material, com a CORREÇÃO da E do roteiros.md): A cobra todos os GB (50 + 8x); B esquece os R$ 50
#   (com 11 GB a fatura cairia para R$ 8,00); D usa R$ 0,80 por GB; E vale para todo x: com 5 GB daria R$ 10,00 e com
#   consumo zero, 50 + 8 · (0 − 10) = −30, fatura NEGATIVA (o material diz "R$ 10,00 para quem não consome nada": errado).
# QUESTÃO NOVA (você faz, texto do prompt): excedente 8,3 − 5 = 3,3 kg → "ou fração" → 4 kg · 6 = 24 → 25 + 24 = R$ 49,00 (C).
#   A 43 = 25 + 18 (ignora a fração) · B 44,80 = 25 + 6 · 3,3 (proporcional) · D 49,80 = 6 · 8,3 (esquece a tarifa fixa)
#   · E 79 = 25 + 6 · 9 (arredonda para 9 kg e cobra todos como adicionais).
# Atalhos (verde): "comece na fronteira de baixo e some só o pedaço que passou" (100 + 9 · 6) · catraca: tire a parte já
#   paga, ARREDONDE O RESTO PARA CIMA, multiplique pela tarifa adicional e some a parte fixa.
# Frases-chave (meio e fim, idênticas): 1. Primeiro descubra a faixa; depois use só a regra dela. 2. Cada faixa parte de
#   onde a anterior parou. 3. Hora ou fração: começou, pagou inteira.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Gastou o dobro e pagou mais que o dobro? Funções por partes | Função Modular Ep. 1"
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
        "{a}Uma casa gastou *dez metros cúbicos* de água [p=0.2] e pagou *quarenta reais.* [p=0.5] {b}A vizinha gastou o "
        "dobro, [p=0.2] vinte metros cúbicos. [p=0.4] {c}Ela pagou *oitenta reais?* [p=0.5] {d}Não: [p=0.2] pagou *cem "
        "reais.* [p=0.5] {e}A regra mudou no meio do caminho."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai ler qualquer *tarifa por faixas,* [p=0.3] {b}montar a lei de um plano "
        "com *franquia* [p=0.3] {c}e reconhecer o *gráfico* de cada uma."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Conceito de Função: [p=0.2] *f de x* é uma regra que "
        "recebe um número [p=0.2] e devolve outro. [p=0.4] {b}E da Função Afim: [p=0.2] *parte fixa mais valor "
        "por unidade* [p=0.2] tem gráfico em *reta.* [p=0.3] {c}Quanto mais caro cada unidade, [p=0.2] mais inclinada."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três coisas que você conhece. [p=0.3] {a}A conta de água tem a *tarifa mínima:* [p=0.2] o valor pago "
        "mesmo gastando pouco. [p=0.4] {b}O plano do celular tem a *franquia,* [p=0.2] os gigas que vêm no preço; "
        "[p=0.2] o que passa dela é o *excedente.* [p=0.4] {c}E o estacionamento: [p=0.2] primeira hora de um jeito, "
        "[p=0.2] as outras de outro. [p=0.4] {d}Nas três, [p=0.2] a regra *muda* conforme o uso."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}Isso tem nome. [p=0.3] {a}Uma *função definida por partes* [p=0.2] usa uma lei diferente em cada *faixa.* "
        "[p=0.4] {b}Faixa, [p=0.2] ou *intervalo,* [p=0.2] é um trecho de números, [p=0.2] como de dez a vinte. "
        "[p=0.4] {c}Onde uma faixa termina e a outra começa [p=0.2] é a *fronteira.* [p=0.4] {d}No papel, [p=0.2] uma "
        "*chave:* [p=0.2] cada linha com a sua regra [p=0.2] e a sua condição."),

    # ================= BLOCO B: A CONTA DE ÁGUA =================
    dict(id="06", block="agua", text=
        "{t}Vamos ler a conta de água. [p=0.3] {a}Primeira linha: [p=0.2] até dez metros cúbicos, [p=0.2] *quarenta "
        "reais,* [p=0.2] fixo. [p=0.2] É a tarifa mínima. [p=0.4] {b}Segunda: [p=0.2] de dez a vinte, [p=0.2] *quarenta "
        "mais seis vezes x menos dez.* [p=0.4] {c}O x menos dez [p=0.2] é o que passou de dez. [p=0.2] Cada metro "
        "cúbico desses custa seis reais. [p=0.4] {d}Terceira: [p=0.2] acima de vinte, [p=0.2] *cem mais nove vezes x "
        "menos vinte.*"),
    dict(id="07", block="cem", text=
        "{t}E de onde saiu esse *cem?* [p=0.4] {a}É a conta *exatamente* em vinte: [p=0.2] quarenta [p=0.2] mais seis "
        "vezes dez. [p=0.2] *Cem reais.* [p=0.4] {b}Cada faixa *parte de onde a anterior parou.* [p=0.4] {c}Por isso "
        "a vizinha pagou cem, [p=0.2] e não oitenta."),

    # ================= BLOCO C: O MÉTODO (PRÉDIO) =================
    dict(id="08", block="predio", text=
        "{t}Quanto paga quem gastou *vinte e seis* metros cúbicos? [p=0.4] {a}Pense num *prédio* de três andares: "
        "[p=0.2] cada andar, uma faixa. [p=0.4] {b}Passo um: [p=0.2] descubra *em que andar* o valor mora. [p=0.2] "
        "Vinte e seis passa de vinte: [p=0.2] *terceiro andar.* [p=0.4] {c}Passo dois: [p=0.2] use *só* a regra "
        "daquele andar. [p=0.3] Cem mais nove vezes seis: [p=0.2] *cento e cinquenta e quatro reais.*"),
    dict(id="09", block="fronteira", text=
        "{t}E quem gastou *exatamente* vinte? [p=0.4] {a}Aí, olhe o sinal de cada linha. [p=0.2] *Menor ou igual* inclui "
        "a fronteira; [p=0.2] *menor* não inclui. [p=0.4] {b}A segunda linha diz *x menor ou igual a vinte:* [p=0.2] o "
        "vinte mora no segundo andar. [p=0.2] Quarenta mais seis vezes dez, [p=0.2] cem. [p=0.4] {c}A terceira linha "
        "também daria cem: [p=0.2] as faixas se *encostam* sem salto."),
    dict(id="10", block="atalho_faixa", text=
        "{t}Atalho: [p=0.3] {a}comece no valor da *fronteira de baixo* do andar [p=0.2] e some *só "
        "o pedaço que passou.* [p=0.4] {b}Vinte e seis: [p=0.2] a fronteira vinte vale cem, [p=0.2] e passaram seis, a nove reais. "
        "[p=0.3] {c}Cem mais cinquenta e quatro: [p=0.2] *cento e cinquenta e quatro.*"),

    # ================= BLOCO D: O GRÁFICO =================
    dict(id="11", block="grafico", text=
        "{t}E como fica o desenho dessa conta? [p=0.4] {a}Até dez, [p=0.2] a conta não muda: [p=0.2] um trecho "
        "*horizontal,* [p=0.2] deitado, em quarenta. [p=0.4] {b}De dez a vinte, [p=0.2] sobe seis reais por metro "
        "cúbico: [p=0.2] uma reta *inclinada.* [p=0.4] {c}Acima de vinte, [p=0.2] sobe nove por metro cúbico: [p=0.2] "
        "*mais inclinada* ainda. [p=0.4] {d}Como na Função Afim, [p=0.2] a inclinação de cada pedaço "
        "[p=0.2] é o *preço por unidade* daquela faixa."),

    # ================= BLOCO E: A ESCADA =================
    dict(id="12", block="escada", text=
        "{t}E quando o gráfico *pula?* [p=0.4] {a}O estacionamento: [p=0.2] dez reais a primeira hora [p=0.2] e "
        "quatro por hora adicional *ou fração.* [p=0.4] {b}Essa regra você já viu na série de Conceito de Função; "
        "[p=0.2] o novo aqui é o *desenho da escada.* [p=0.4] {c}Dentro de cada hora, [p=0.2] o preço fica parado; "
        "[p=0.2] começou a seguinte, [p=0.2] ele *salta.* [p=0.4] {d}Duas horas e cinco minutos [p=0.2] custam o "
        "mesmo que três horas: [p=0.2] *dezoito reais.*"),
    dict(id="13", block="bolinhas", text=
        "{t}E na beirada de cada degrau? [p=0.4] {a}A *bolinha cheia* [p=0.2] marca o valor que *vale* na fronteira. "
        "[p=0.3] {b}A *bolinha vazia* [p=0.2] marca o que *não vale.* [p=0.4] {c}Exatamente uma hora: [p=0.2] dez, "
        "bolinha cheia. [p=0.3] {d}Uma hora e um minuto: [p=0.2] já são *catorze;* [p=0.2] o degrau de cima começa "
        "vazio."),
    dict(id="14", block="atalho_catraca", text=
        "{t}O atalho do *ou fração* é uma *catraca.* [p=0.3] {a}Encostou na hora seguinte, [p=0.2] pagou a hora "
        "inteira. [p=0.4] {b}Na conta: [p=0.2] tire o que a parte fixa já cobre, [p=0.2] *arredonde o resto para cima,* "
        "[p=0.2] multiplique pela tarifa adicional [p=0.2] e some a parte fixa. [p=0.4] {c}Duas horas e cinco: [p=0.2] "
        "sobra uma hora e cinco, [p=0.2] vira *duas.* [p=0.2] Dez mais oito, [p=0.2] dezoito."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Agora você. [p=0.3] {a}Uma academia cobra *oitenta reais* por mês [p=0.2] para até *doze aulas* [p=0.2] e "
        "*sete reais* por aula que passar de doze. [p=0.4] {b}Quem fez *dezessete aulas* [p=0.2] paga quanto? [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Primeiro, o andar: [p=0.2] dezessete passa de doze, [p=0.2] *segunda faixa.* "
        "[p=0.4] {b}Passaram cinco aulas, [p=0.2] a sete reais: [p=0.2] trinta e cinco. [p=0.4] {c}E a parte fixa "
        "*continua:* [p=0.2] oitenta mais trinta e cinco, [p=0.2] *cento e quinze reais.*"),

    # ================= MINI-RECAP =================
    dict(id="17", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] primeiro descubra a faixa; [p=0.2] depois use só a regra "
        "dela. [p=0.5] {b}Dois: [p=0.2] cada faixa parte de onde a anterior parou. [p=0.5] {c}Três: [p=0.2] hora ou "
        "fração: [p=0.2] começou, pagou inteira."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{a}Primeiro erro: [p=0.2] calcular os vinte e seis metros cúbicos [p=0.2] pela *segunda linha.* [p=0.2] Dá "
        "cento e trinta e seis. [p=0.4] {b}Parece certo porque vinte e seis *passa de dez.* [p=0.4] {c}Mas a segunda "
        "linha vai só até vinte: [p=0.2] confira o *menor ou igual* da fronteira. [p=0.2] Terceiro andar: [p=0.2] "
        "*cento e cinquenta e quatro.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] cobrar o *ou fração* de forma *proporcional.* [p=0.2] Duas horas e meia [p=0.2] viram dez "
        "mais quatro vezes um e meio: [p=0.2] dezesseis. [p=0.4] {b}Parece justo pagar só pelo tempo usado. [p=0.4] "
        "{c}Mas *ou fração* é catraca: [p=0.2] a meia hora conta como hora inteira. [p=0.2] Dez mais duas vezes quatro, "
        "[p=0.2] *dezoito.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *esquecer a parte fixa* quando entra o excedente. [p=0.2] Na academia, [p=0.2] cobrar só "
        "as cinco aulas a mais: [p=0.2] trinta e cinco reais. [p=0.4] {b}Parece certo porque a conta nova [p=0.2] é "
        "sobre o que passou. [p=0.4] {c}Mas os oitenta *continuam* sendo cobrados. [p=0.2] Oitenta mais trinta e cinco, "
        "[p=0.2] *cento e quinze.*"),

    # ================= QUESTÃO 8 (EU FAÇO) =================
    dict(id="21", block="q8", text=
        "{t}Questão no estilo do ENEM: [p=0.2] eu faço. [p=0.3] {a}Um plano de internet custa "
        "*cinquenta reais* por mês [p=0.2] e inclui *dez gigas.* [p=0.2] Cada giga além da franquia custa *oito reais.* "
        "[p=0.2] Qual é a lei da fatura? [p=0.3] {qa}As cinco leis estão na tela. [p=0.2] {qb}{qc}{qd}{qe}Repare: [p=0.2] "
        "três têm *chave,* [p=0.2] duas valem para todo x. [p=0.4] {p}*Leia com calma.* [p=0.8]"),
    dict(id="22", block="q8", text=
        "{t}Faixas primeiro. [p=0.3] {a}Até dez gigas, [p=0.2] *primeiro andar:* [p=0.2] só os cinquenta fixos. [p=0.4] "
        "{b}Acima de dez, [p=0.2] *segundo andar:* [p=0.2] os cinquenta continuam, [p=0.2] e cada giga que passou de dez "
        "custa oito. [p=0.3] Cinquenta mais oito vezes x menos dez. [p=0.4] {c}Conferindo na fronteira: [p=0.2] em dez "
        "gigas, [p=0.2] as duas linhas dão *cinquenta.* [p=0.2] Não há salto. [p=0.3] {d}E com quinze gigas: [p=0.2] "
        "cinquenta mais quarenta, [p=0.2] *noventa.* [p=0.3] {ok}*Letra C!*"),
    dict(id="23", block="q8", text=
        "{t}E as erradas? [p=0.3] {xa}A A cobra *todos* os gigas, [p=0.2] até os da franquia. [p=0.4] {xb}A B esquece "
        "os cinquenta fixos: [p=0.2] com onze gigas, [p=0.2] a fatura *cairia* para oito reais. [p=0.4] {xd}A D cobra "
        "*oitenta centavos* por giga. [p=0.4] {xe}A E vale para todo x: [p=0.2] com cinco gigas daria dez reais, "
        "[p=0.3] {xe2}e com consumo zero, [p=0.2] cinquenta menos oitenta: [p=0.2] *menos trinta.* [p=0.3] Fatura "
        "*negativa.*"),

    # ================= QUESTÃO NOVA (VOCÊ FAZ) =================
    dict(id="24", block="qfrete", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma transportadora cobra *vinte e cinco reais* para entregar pacotes de até *cinco "
        "quilos* [p=0.2] e *seis reais* por quilograma adicional *ou fração* de quilograma adicional. [p=0.3] O valor "
        "cobrado para entregar um pacote de *oito vírgula três quilos* é: [p=0.4] {qa}A: [p=0.2] quarenta e três reais. "
        "[p=0.3] {qb}B: [p=0.2] quarenta e quatro e oitenta. [p=0.3] {qc}C: [p=0.2] quarenta e nove reais. [p=0.3] "
        "{qd}D: [p=0.2] quarenta e nove e oitenta. [p=0.3] {qe}E: [p=0.2] setenta e nove reais. [p=0.4] {p}*Pause o "
        "vídeo e resolva.* [p=2.0]"),
    dict(id="25", block="qfrete", text=
        "{t}Conferindo. [p=0.3] {a}Oito vírgula três passa de cinco: [p=0.2] *segunda faixa.* [p=0.2] Os primeiros cinco "
        "quilos [p=0.2] já estão nos vinte e cinco. [p=0.4] {b}O excedente é oito vírgula três menos cinco: [p=0.2] *três "
        "vírgula três quilos.* [p=0.4] {c}E a catraca: [p=0.2] os zero vírgula três [p=0.2] contam como um quilo "
        "inteiro. [p=0.2] *Quatro quilos adicionais.* [p=0.4] {d}Quatro vezes seis, [p=0.2] vinte e quatro; [p=0.2] mais "
        "vinte e cinco, [p=0.2] *quarenta e nove reais.* [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="qfrete", text=
        "{t}E as erradas? [p=0.3] {xa}A A cobra só três quilos: [p=0.2] *ignorou* a fração. [p=0.4] {xb}A B cobra "
        "proporcional, [p=0.2] seis vezes três vírgula três; [p=0.2] o *ou fração* não permite. [p=0.4] {xd}A D cobra "
        "os oito vírgula três quilos a seis reais [p=0.2] e esquece a *tarifa fixa.* [p=0.4] {xe}A E arredonda para "
        "nove [p=0.2] e cobra todos como adicionais, [p=0.2] esquecendo os cinco que já estão nos vinte e cinco."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro descubra a faixa; [p=0.2] depois use só "
        "a regra dela. [p=0.5] {b}Dois: [p=0.2] cada faixa parte de onde a anterior parou. [p=0.5] {c}Três: [p=0.2] hora "
        "ou fração: [p=0.2] começou, pagou inteira."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Uma taxa cobra *dez por cento* sobre a parte do lucro entre dois mil e cinco mil reais [p=0.2] e *vinte por "
        "cento* sobre o que passar disso. [p=0.4] {b}Quem lucrou *sete mil reais* [p=0.2] paga vinte por cento de sete "
        "mil? [p=0.5] {c}Se você respondeu *mil e quatrocentos reais,* [p=0.2] pagou o dobro. [p=0.5] {d}Próximo "
        "episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] a sua conta de água tem tarifa mínima? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
