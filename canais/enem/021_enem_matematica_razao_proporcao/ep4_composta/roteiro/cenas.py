# Roteiro — Razão, Proporção e Regra de Três, Episódio 4 de 6: Regra de três composta e o atalho dos homens-hora
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seção 08 (+ Questão 6 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   INTERROGATÓRIO: cada coluna é interrogada SOZINHA, frente a frente com a incógnita; as outras ficam fora da sala.
#   PACOTE DE TRABALHO: a obra sempre precisa da mesma quantidade de pessoa-hora; muda quem trabalha e quanto, o pacote não.
# Desvio consciente: o prompt usava o muro (12 op., 8 h/dia, 15 dias → 18 op., 10 h/dia) no "eu faço" do bloco b) E na
#   Questão 6. Os blocos b) e d) usam outra obra, uma CALÇADA: 10 pedreiros, 6 h/dia, 12 dias → 15 pedreiros, 8 h/dia.
#   Método: 12/x = (15/10)·(8/6) = 1,5 · 4/3 = 2 → x = 6. Atalho: 10·6·12 = 720 = 15·8·x → x = 6.
#   O muro fica só na Questão 6, resolvida pelos dois caminhos.
# Pré-requisito (inversa simples): 10 pintores em 6 dias → 20 pintores em 3 dias (10·6 = 20·3 = 60).
# Nós fazemos (do prompt): 5 pintores, 6 h/dia, 8 dias → 4 pintores, 8 h/dia: 5·6·8 = 240 = 4·8·x → x = 7,5 dias.
# QUESTÃO 6 do material (texto idêntico na tela): 15/x = (18/12)·(10/8) = 1,875 → x = 8; 12·8·15 = 1440 = 18·10·x → 8 → B.
#   O material não explica as erradas. Explicações NOSSAS:
#   C (10) = 15·12/18: só interrogou os operários, esqueceu as horas · D (12) = 15·8/10: só as horas, esqueceu os operários ·
#   E (18) = 15·(18/12)·(8/10): tratou os operários como DIRETA (esqueceu de inverter uma coluna) · A (6) não fecha o pacote:
#   18·10·6 = 1080 < 1440, o muro não fica pronto.
# Erro 3 (atalho com quantidade que muda): calçada com o DOBRO do comprimento → o pacote dobra: 720 → 1440.
# Frases-chave (meio e fim, idênticas, do prompt): 1. Composta é a simples repetida. 2. Cada coluna frente a frente com a
#   incógnita, uma de cada vez. 3. Obra fixa? O pacote de pessoa-hora não muda.
# Atalhos (verde): "na hora do interrogatório, pergunte sempre: e os DIAS?" · "mais gente e mais horas → menos dias" ·
#   "obra fixa: multiplique tudo de um lado e iguale ao outro" · conferência do pacote na alternativa.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Regra de três composta sem medo (e o atalho dos homens-hora) | Razão e Proporção Ep. 4"
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
        "{a}Três grandezas ao mesmo tempo *assustam.* [p=0.5] {b}Mas a regra de três composta [p=0.2] é só a *simples "
        "repetida,* [p=0.4] {c}e existe um *atalho* [p=0.2] que dispensa até a decisão de direta ou inversa."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resolver *qualquer* regra de três composta [p=0.3] {b}de *dois jeitos.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio passado: [p=0.2] o *teste do dobro.* [p=0.4] {a}Dez pintores pintam um "
        "prédio em *seis dias.* [p=0.3] E vinte pintores? [p=0.4] {b}Dobrou a equipe, [p=0.2] o tempo vira *metade:* "
        "[p=0.2] três dias. [p=0.3] Então é *inversa.* [p=0.4] {c}E na inversa, [p=0.2] o produto não muda: [p=0.2] dez "
        "vezes seis, [p=0.2] sessenta. [p=0.2] Vinte vezes três, [p=0.2] *sessenta.*"),

    # ================= A HISTÓRIA DA OBRA =================
    dict(id="04", block="historia", text=
        "{t}Agora, uma obra. [p=0.3] {a}*Dez pedreiros,* [p=0.2] trabalhando *seis horas por dia,* [p=0.2] fazem uma calçada "
        "em *doze dias.* [p=0.5] {b}A prefeitura tem pressa. [p=0.2] Contrata *quinze pedreiros* [p=0.2] e pede *oito horas* "
        "por dia. [p=0.4] {c}Em quantos dias sai a mesma calçada? [p=0.5] {d}Agora são *três* grandezas mudando juntas. "
        "[p=0.3] {e}Isso tem nome: [p=0.2] *regra de três composta,* [p=0.2] a regra de três com três ou mais grandezas."),
    dict(id="05", block="tabela", text=
        "{t}Primeiro passo: [p=0.2] organizar. [p=0.3] {a}Cada grandeza vira uma *coluna,* [p=0.2] uma fileira em pé com "
        "os seus dois valores. [p=0.4] {b}Pedreiros: [p=0.2] dez e quinze. [p=0.3] {c}Horas por dia: [p=0.2] seis e oito. "
        "[p=0.3] {d}Dias: [p=0.2] doze e *x.* [p=0.4] {e}Esse *x* é a *incógnita:* [p=0.2] o valor que a gente procura."),
    dict(id="06", block="metodo", text=
        "{t}E o método tem *quatro passos.* [p=0.4] {a}Um: [p=0.2] uma coluna por grandeza, [p=0.2] já feito. [p=0.3] "
        "{b}Dois: [p=0.2] comparar *cada* coluna com a da incógnita, [p=0.2] *uma de cada vez.* [p=0.3] {c}Três: [p=0.2] "
        "inverter as que forem inversas. [p=0.3] {d}Quatro: [p=0.2] a razão da incógnita [p=0.2] é o *produto* das outras "
        "razões."),

    # ================= O INTERROGATÓRIO =================
    dict(id="07", block="interroga", text=
        "{t}O passo dois é um *interrogatório.* [p=0.3] {a}Cada coluna entra na sala *sozinha,* [p=0.2] frente a frente "
        "com a incógnita. [p=0.2] As outras ficam do lado de fora. [p=0.5] {b}Primeiro suspeito: [p=0.2] *pedreiros.* "
        "[p=0.3] As horas ficam paradas. [p=0.4] {c}Teste do dobro: [p=0.2] o dobro de pedreiros [p=0.2] faz a calçada em "
        "*metade* dos dias. [p=0.3] {d}*Inversa.*"),
    dict(id="08", block="interroga", text=
        "{a}Segundo suspeito: [p=0.2] *horas por dia.* [p=0.3] Agora são os pedreiros que esperam lá fora. [p=0.4] {b}O "
        "dobro de horas por dia [p=0.2] também faz a calçada em *metade* dos dias. [p=0.3] {c}*Inversa* também. [p=0.4] "
        "{d}Atalho: [p=0.2] na hora do interrogatório, [p=0.2] a pergunta é sempre a mesma: [p=0.2] *e os dias?*"),
    dict(id="09", block="montar", text=
        "{t}Passo três: [p=0.2] as duas são inversas, [p=0.2] então as duas *viram de cabeça para baixo.* [p=0.4] {a}Dez "
        "quinze avos [p=0.2] vira *quinze décimos.* [p=0.3] {b}Seis oitavos [p=0.2] vira *oito sextos.* [p=0.5] {c}Passo "
        "quatro: [p=0.2] doze sobre *x* [p=0.2] é igual a quinze décimos *vezes* oito sextos."),
    dict(id="10", block="montar", text=
        "{t}Agora é conta. [p=0.3] {a}Quinze décimos é *um e meio.* [p=0.3] {b}Oito sextos, [p=0.2] simplificando, [p=0.2] "
        "*quatro terços.* [p=0.3] {c}Um e meio vezes quatro terços: [p=0.2] *dois.* [p=0.4] {d}Doze sobre *x* igual a "
        "dois: [p=0.2] *x* é doze dividido por dois. [p=0.3] {e}*Seis dias!* [p=0.4] {f}E faz sentido: [p=0.2] mais gente, "
        "[p=0.2] mais horas, [p=0.2] *menos dias.*"),
    dict(id="11", block="regra", text=
        "{t}Agora, a regra que evita a confusão. [p=0.4] {a}*Nunca* compare as colunas entre si. [p=0.3] {b}Pedreiros "
        "contra horas por dia? [p=0.2] Não interessa. [p=0.4] {c}Tentar pensar em tudo ao mesmo tempo [p=0.2] é o que faz a "
        "questão parecer impossível. [p=0.4] {d}Um suspeito de cada vez, [p=0.2] sempre contra a incógnita."),

    # ================= O ATALHO DOS HOMENS-HORA =================
    dict(id="12", block="pacote", text=
        "{t}E o atalho? [p=0.3] {a}Pense no que a calçada *exige:* [p=0.2] uma quantidade fixa de trabalho. [p=0.4] {b}Um "
        "*homem-hora,* [p=0.2] ou pessoa-hora, [p=0.2] é uma pessoa trabalhando durante *uma hora.* [p=0.4] {c}Dez pedreiros, "
        "[p=0.2] seis horas, [p=0.2] doze dias: [p=0.2] dez vezes seis vezes doze, [p=0.2] *setecentos e vinte* pessoa-hora. "
        "[p=0.4] {d}Esse é o *trabalho total:* [p=0.2] o pacote que a calçada precisa."),
    dict(id="13", block="pacote", text=
        "{t}E o pacote *não muda.* [p=0.3] Muda quem trabalha, [p=0.2] e quanto trabalha. [p=0.4] {a}Então a nova equipe "
        "precisa fechar os mesmos setecentos e vinte: [p=0.2] quinze vezes oito vezes *x.* [p=0.4] {b}Quinze vezes oito, "
        "[p=0.2] cento e vinte. [p=0.2] Cento e vinte *x* igual a setecentos e vinte. [p=0.3] {c}*x* igual a *seis.* [p=0.4] "
        "{d}A mesma resposta, [p=0.2] sem decidir nada sobre direta ou inversa."),
    dict(id="14", block="quando", text=
        "{t}Quando usar esse atalho? [p=0.4] {a}Quando a história tem *trabalhadores,* [p=0.2] um *ritmo,* [p=0.2] como "
        "horas por dia, [p=0.2] e um *tempo,* [p=0.3] {b}produzindo uma quantidade *fixa:* [p=0.2] o mesmo muro, [p=0.2] a "
        "mesma calçada, [p=0.2] a mesma casa. [p=0.4] {c}Atalho: [p=0.2] obra fixa? [p=0.2] Multiplique tudo de um lado "
        "[p=0.2] e iguale ao outro."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez, [p=0.2] pelo atalho. [p=0.3] {a}*Cinco pintores,* [p=0.2] seis horas por dia, [p=0.2] pintam uma casa "
        "em *oito dias.* [p=0.4] {b}Em quantos dias *quatro pintores,* [p=0.2] oito horas por dia, [p=0.2] pintam a mesma "
        "casa? [p=0.4] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O pacote: [p=0.2] cinco vezes seis vezes oito, [p=0.2] *duzentos e quarenta.* "
        "[p=0.4] {b}A nova equipe: [p=0.2] quatro vezes oito vezes *x,* [p=0.2] trinta e dois *x.* [p=0.4] {c}Trinta e dois "
        "*x* igual a duzentos e quarenta: [p=0.2] *x* igual a *sete e meio.* [p=0.3] Sete dias e meio. [p=0.4] {d}Faz "
        "sentido? [p=0.2] Por dia, [p=0.2] a equipe nova trabalha trinta e duas horas, [p=0.2] contra trinta da antiga. "
        "[p=0.3] Um pouco mais por dia, [p=0.2] um pouco *menos dias.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] composta é a simples repetida. [p=0.5] {b}Dois: [p=0.2] "
        "cada coluna frente a frente com a incógnita, [p=0.2] uma de cada vez. [p=0.5] {c}Três: [p=0.2] obra fixa? [p=0.2] "
        "O pacote de pessoa-hora não muda."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *comparar as colunas entre si.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque todas estão na mesma tabela, [p=0.2] uma do lado da outra. [p=0.4] {c}Mas só a incógnita "
        "interessa: [p=0.2] cada coluna contra ela, [p=0.2] uma de cada vez."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] *esquecer de inverter* uma das colunas inversas. [p=0.4] {b}Parece certo, [p=0.2] porque você "
        "decidiu direitinho [p=0.2] e só esqueceu um detalhe na hora de montar. [p=0.4] {c}Mas uma coluna sem inverter muda "
        "a resposta inteira. [p=0.3] Na dúvida, [p=0.2] confira pelo pacote."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] usar o atalho quando a *quantidade produzida muda.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "continuam sendo pedreiros, [p=0.2] horas e dias. [p=0.4] {c}Mas se a calçada tiver o *dobro* do comprimento, "
        "[p=0.2] o pacote também dobra: [p=0.2] de setecentos e vinte [p=0.2] para *mil quatrocentos e quarenta.*"),

    # ================= QUESTÃO 6 DO MATERIAL =================
    dict(id="21", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}*Doze operários,* "
        "[p=0.2] trabalhando *oito horas* por dia, [p=0.2] constroem um muro em *quinze dias.* [p=0.4] {b}Mantido o mesmo "
        "ritmo, [p=0.2] *dezoito operários* trabalhando *dez horas* por dia [p=0.2] construirão um muro idêntico em: [p=0.4] "
        "{qa}A: [p=0.2] seis dias. [p=0.3] {qb}B: [p=0.2] oito dias. [p=0.3] {qc}C: [p=0.2] dez dias. [p=0.3] {qd}D: "
        "[p=0.2] doze dias. [p=0.3] {qe}E: [p=0.2] dezoito dias. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q6", text=
        "{t}Primeiro caminho: [p=0.2] o interrogatório. [p=0.3] {a}Operários contra dias: [p=0.2] mais operários, [p=0.2] "
        "menos dias. [p=0.2] *Inversa.* [p=0.3] {b}Horas contra dias: [p=0.2] mais horas, [p=0.2] menos dias. [p=0.2] "
        "*Inversa.* [p=0.4] {c}Invertendo as duas: [p=0.2] quinze sobre *x* [p=0.2] igual a dezoito doze avos [p=0.2] vezes "
        "dez oitavos. [p=0.4] {d}Um e meio vezes um e um quarto: [p=0.2] *um vírgula oito, sete, cinco.* [p=0.3] {e}Quinze "
        "dividido por isso: [p=0.2] *oito dias.*"),
    dict(id="23", block="q6", text=
        "{t}Segundo caminho: [p=0.2] o pacote. [p=0.3] {a}Doze vezes oito vezes quinze: [p=0.2] *mil quatrocentos e "
        "quarenta.* [p=0.4] {b}Dezoito vezes dez vezes *x:* [p=0.2] cento e oitenta *x.* [p=0.3] {c}Mil quatrocentos e "
        "quarenta dividido por cento e oitenta: [p=0.2] *oito.* [p=0.3] {ok}*Letra B!* [p=0.4] {d}E faz sentido: [p=0.2] mais "
        "operários e mais horas, [p=0.2] menos dias. [p=0.2] Oito é menor que quinze."),
    dict(id="24", block="q6", text=
        "{t}E as outras? [p=0.3] {xe}A E, dezoito, [p=0.2] tratou os operários como *direta:* [p=0.2] esqueceu de inverter "
        "uma coluna. [p=0.2] E mais dias com mais gente não faz sentido. [p=0.4] {xc}A C só interrogou os operários. [p=0.3] "
        "{xd}A D só interrogou as horas. [p=0.4] {xa}E a A não fecha o pacote: [p=0.2] dezoito vezes dez vezes seis [p=0.2] "
        "dá mil e oitenta, [p=0.2] e o muro fica pela metade do caminho."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] composta é a simples repetida. [p=0.5] {b}Dois: "
        "[p=0.2] cada coluna frente a frente com a incógnita, [p=0.2] uma de cada vez. [p=0.5] {c}Três: [p=0.2] obra fixa? "
        "[p=0.2] O pacote de pessoa-hora não muda."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}O ENEM às vezes monta uma questão *com cara de regra de três* [p=0.2] em que aplicá-la dá *errado.* [p=0.5] "
        "{b}Dois gatos, [p=0.2] dois ratos, [p=0.2] dois minutos… [p=0.5] {c}Próximo episódio."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você prefere o interrogatório ou o pacote? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
