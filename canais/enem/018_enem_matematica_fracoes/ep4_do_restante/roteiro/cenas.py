# Roteiro — Frações, Decimais e Dízimas, Episódio 4 de 8: A armadilha do "do restante" (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — quadro "A armadilha do 'do restante'" (seção 06)
#   + o problema em duas etapas (seção 01) + Questões 7 e 1 da seção 12 (nesta ordem).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a PIZZA QUE ENCOLHE — você come 1/3; seu irmão come 1/4 do QUE SOBROU; o 1/4 dele é de uma pizza menor.
# Certo e errado SEMPRE lado a lado com o mesmo desenho (barra/pizza que encolhe × barra inteira com X vermelho).
# Contas conferidas (reais e frações batem):
#   R$ 1 200 → aluguel 1/3 = R$ 400 → sobram R$ 800 = 2/3 → transporte 1/4 de 800 = R$ 200 (NÃO 1/4 de 1 200 = R$ 300)
#   → sobram R$ 600 = 1/2 do salário. Em frações: 1 − 1/3 = 2/3 · 1/4 · 2/3 = 2/12 = 1/6 (= 200/1 200) ·
#   gasto total 1/3 + 1/6 = 1/2 (= 600) · errado: 1/3 + 1/4 = 7/12 (= 700) · atalho: sobra 3/4 de 2/3 = 6/12 = 1/2.
#   Q7 (material): sobra 1/2 → B · A = 5/12 = 1 − 7/12 (somou 1/3 + 1/4).
#   Q1 (material): sobra 3/4 · 3/5 = 9/20 → C · A = 7/20 = 3/5 − 1/4 (tirou 1/4 do total).
# Frases-chave (meio e fim, idênticas):
#   1. "Do restante" é fração do que sobrou, não do total.
#   2. Primeiro descubra o que sobrou; depois tire a fração dele.
#   3. Atalho: multiplique o que sobra em cada etapa.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A armadilha do \"do restante\": o erro que mais custa ponto em frações | Frações Ep. 4"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte "
            "às palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Este é o erro que *mais custa ponto* em frações. [p=0.5] {b}E a resposta errada *sempre* está entre as "
        "alternativas, [p=0.3] {c}esperando por você."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai identificar o *do restante* no enunciado, [p=0.4] {b}e resolver *em um "
        "passo,* [p=0.2] com um atalho."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] *de* é vezes. [p=0.2] Um quarto de oitocentos "
        "é oitocentos dividido por quatro: [p=0.2] duzentos. [p=0.4] {b}E do episódio três: [p=0.2] para multiplicar frações, "
        "[p=0.2] é *em cima vezes em cima, [p=0.2] embaixo vezes embaixo.* [p=0.3] {c}Um meio vezes um terço [p=0.2] dá um sexto."),

    # ================= ANALOGIA: A PIZZA QUE ENCOLHE =================
    dict(id="04", block="encolhe", text=
        "{t}Imagine uma pizza. [p=0.3] {a}Você come *um terço* dela. [p=0.4] {b}Aí seu irmão chega [p=0.2] e come *um quarto "
        "do que sobrou.* [p=0.5] {c}Repare: [p=0.2] o um quarto dele [p=0.2] é de uma pizza *menor,* [p=0.3] {d}não da pizza "
        "inteira. [p=0.4] {e}A pizza *encolheu* antes de ele chegar."),
    dict(id="05", block="encolhe", text=
        "{t}Duas palavras para guardar. [p=0.3] {a}O *total* é o tudo do começo: [p=0.2] a pizza inteira. [p=0.4] {b}E o "
        "*restante* é o que sobrou [p=0.2] depois de uma parte sair."),

    # ================= BLOCO A: O SALÁRIO EM REAIS =================
    dict(id="06", block="salario", text=
        "{t}Agora com dinheiro de verdade. [p=0.3] {a}Um salário de *mil e duzentos reais.* [p=0.4] {b}O problema tem duas "
        "*etapas,* [p=0.2] ou seja, [p=0.2] dois passos, [p=0.2] um depois do outro. [p=0.4] {c}Primeira etapa: [p=0.2] paga um "
        "terço de aluguel. [p=0.3] {d}Mil e duzentos dividido por três: [p=0.2] *quatrocentos reais.*"),
    dict(id="07", block="salario", text=
        "{a}Sobram, na carteira, [p=0.2] *oitocentos reais.* [p=0.4] {b}Segunda etapa: [p=0.2] do que sobrou, [p=0.2] gasta um "
        "quarto com transporte. [p=0.4] {c}Um quarto *de oitocentos:* [p=0.2] oitocentos dividido por quatro, [p=0.2] *duzentos "
        "reais.*"),
    dict(id="08", block="salario", text=
        "{t}E agora o erro, [p=0.2] lado a lado. [p=0.3] {a}Muita gente faz um quarto de *mil e duzentos:* [p=0.2] trezentos "
        "reais. [p=0.4] {b}Parece certo, [p=0.2] porque o um quarto *parece* ser do salário. [p=0.4] {c}Mas o transporte veio "
        "*do que sobrou.* [p=0.2] O certo é duzentos. [p=0.5] {d}No fim, [p=0.2] sobram seiscentos reais: [p=0.2] *metade* do "
        "salário."),

    # ================= BLOCO B: A MESMA CONTA EM FRAÇÕES =================
    dict(id="09", block="fracoes", text=
        "{t}Agora a mesma conta, [p=0.2] só com frações. [p=0.4] {a}Depois do aluguel, [p=0.2] quanto sobra? [p=0.3] O que falta "
        "para completar o inteiro. [p=0.3] {b}Isso se chama *complemento:* [p=0.2] um menos um terço, [p=0.2] *dois terços.* "
        "[p=0.4] {c}E confere: [p=0.2] oitocentos é dois terços de mil e duzentos."),
    dict(id="10", block="fracoes", text=
        "{t}O transporte é um quarto *de* dois terços. [p=0.3] {a}De é vezes: [p=0.2] um quarto vezes dois terços. [p=0.4] {b}Em "
        "cima, [p=0.2] um vezes dois, [p=0.2] dois. [p=0.2] Embaixo, [p=0.2] quatro vezes três, [p=0.2] doze. [p=0.4] {c}Dois "
        "doze avos, [p=0.2] que simplifica para *um sexto* do salário. [p=0.4] {d}Um sexto, [p=0.2] e *não* um quarto. [p=0.3] "
        "E um sexto de mil e duzentos [p=0.2] são os mesmos duzentos reais."),

    # ================= BLOCO C: O ERRO DE SOMAR DIRETO =================
    dict(id="11", block="somar", text=
        "{t}E aqui está a armadilha que *sempre* aparece nas alternativas. [p=0.4] {a}Somar um terço com um quarto, [p=0.2] direto. "
        "[p=0.3] {b}Dá *sete doze avos.* [p=0.4] {c}Parece certo, [p=0.2] porque foram dois gastos, [p=0.2] e gastos se somam. "
        "[p=0.4] {d}Mas sete doze avos de mil e duzentos [p=0.2] dá setecentos reais. [p=0.3] {e}E o gasto de verdade foi "
        "*seiscentos:* [p=0.2] um terço mais um sexto, [p=0.2] *metade.*"),

    # ================= BLOCO D: O ATALHO =================
    dict(id="12", block="atalho", text=
        "{t}E agora, [p=0.2] o atalho que resolve em um passo. [p=0.4] {a}Em vez de olhar o que *sai,* [p=0.2] olhe o que *fica.* "
        "[p=0.4] {b}No aluguel saiu um terço: [p=0.2] *ficaram dois terços.* [p=0.3] {c}No transporte saiu um quarto do que havia: "
        "[p=0.2] *ficaram três quartos* do que havia. [p=0.4] {d}Multiplique o que fica: [p=0.2] três quartos vezes dois terços, "
        "[p=0.2] seis doze avos, [p=0.2] *um meio.* [p=0.4] {e}Metade do salário: [p=0.2] os mesmos seiscentos reais. [p=0.3] Em "
        "um passo."),

    # ================= BLOCO E: AS PALAVRAS DE ALERTA =================
    dict(id="13", block="alerta", text=
        "{t}E como saber que a armadilha está ali? [p=0.4] {a}Algumas palavras *acendem o alerta.* [p=0.4] {b}*Do restante.* "
        "[p=0.3] {c}*Do que sobrou.* [p=0.3] {d}*Do que havia.* [p=0.3] {e}*Do volume que havia.* [p=0.5] {f}Viu uma dessas? "
        "[p=0.2] A segunda fração é de uma pizza *menor.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] *do restante* é fração do que sobrou, [p=0.2] não do total. "
        "[p=0.5] {b}Dois: [p=0.2] primeiro descubra o que sobrou; [p=0.2] depois tire a fração dele. [p=0.5] {c}Três: [p=0.2] "
        "atalho: [p=0.2] multiplique o que sobra em cada etapa."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar* as duas frações: [p=0.2] um terço mais um quarto, "
        "[p=0.2] sete doze avos. [p=0.4] {b}Parece certo, [p=0.2] porque gastos se somam. [p=0.4] {c}Mas a segunda fração é de "
        "uma pizza menor. [p=0.2] Primeiro descubra o que sobrou."),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] *subtrair* a segunda fração do total, [p=0.2] como três quintos menos um quarto. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque tirar é subtrair. [p=0.4] {c}Mas o um quarto é *do que havia,* [p=0.2] não do total. [p=0.2] Ele "
        "precisa ser calculado sobre a parte que sobrou."),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] responder *o que foi gasto* [p=0.2] quando a pergunta é *o que sobrou,* [p=0.2] ou o contrário. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a conta estava certa. [p=0.4] {c}Mas a alternativa do gasto está lá, [p=0.2] "
        "esperando. [p=0.2] Releia a pergunta no fim."),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="18", block="q7", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.3] Esta eu resolvo com você. [p=0.4] {a}Um trabalhador gasta um terço do "
        "salário com moradia [p=0.2] e, do que resta, [p=0.2] gasta um quarto com transporte. [p=0.4] {b}Que fração do salário "
        "sobra depois desses dois gastos? [p=0.4] {c}A: [p=0.2] cinco doze avos. [p=0.3] {d}B: [p=0.2] um meio. [p=0.3] {e}C: "
        "[p=0.2] sete doze avos. [p=0.3] {f}D: [p=0.2] dois terços. [p=0.3] {g}E: [p=0.2] três quartos."),
    dict(id="19", block="q7", text=
        "{t}Olha o alerta: [p=0.2] *do que resta.* [p=0.4] {a}Caminho longo: [p=0.2] depois da moradia sobram dois terços. [p=0.4] "
        "{b}O transporte é um quarto de dois terços: [p=0.2] um sexto do salário. [p=0.4] {c}Sobra: [p=0.2] dois terços menos um "
        "sexto. [p=0.3] Dois terços são quatro sextos; [p=0.2] quatro sextos menos um sexto, [p=0.2] três sextos, [p=0.2] *um meio.*"),
    dict(id="20", block="q7", text=
        "{t}Agora pelo atalho: [p=0.2] sobram três quartos de dois terços. [p=0.4] {a}Três quartos vezes dois terços, [p=0.2] *um "
        "meio.* [p=0.2] Mesmo resultado, [p=0.2] em um passo. [p=0.3] {ok}*Letra B!* [p=0.4] {x}E a A, [p=0.2] cinco doze avos, "
        "[p=0.2] é de quem somou um terço mais um quarto, [p=0.2] sete doze avos, [p=0.2] e tirou de um. [p=0.3] A armadilha, "
        "[p=0.2] esperando."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="21", block="q1", text=
        "{t}Agora é com você. [p=0.4] {a}Um reservatório está com três quintos de sua capacidade total. [p=0.4] {b}Para a limpeza, "
        "[p=0.2] retira-se um quarto do volume que havia no reservatório. [p=0.4] {c}Após a retirada, [p=0.2] que fração da "
        "capacidade total permanece com água? [p=0.4] {d}A: [p=0.2] sete vinte avos. [p=0.3] {e}B: [p=0.2] dois quintos. [p=0.3] "
        "{f}C: [p=0.2] nove vinte avos. [p=0.3] {g}D: [p=0.2] um meio. [p=0.3] {h}E: [p=0.2] três quartos. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {a}O alerta: [p=0.2] *do volume que havia.* [p=0.4] {b}Saiu um quarto do que havia, [p=0.2] "
        "então *ficaram três quartos* do que havia. [p=0.4] {c}Três quartos vezes três quintos: [p=0.2] *nove vinte avos.* "
        "[p=0.3] {ok}*Letra C!* [p=0.4] {x}E a A, [p=0.2] sete vinte avos, [p=0.2] é de quem fez três quintos menos um quarto: "
        "[p=0.2] tirou um quarto *do total,* [p=0.2] em vez de um quarto do que havia."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="23", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] *do restante* é fração do que sobrou, [p=0.2] não do total. "
        "[p=0.5] {b}Dois: [p=0.2] primeiro descubra o que sobrou; [p=0.2] depois tire a fração dele. [p=0.5] {c}Três: [p=0.2] "
        "atalho: [p=0.2] multiplique o que sobra em cada etapa."),

    # ================= PONTE E CTA =================
    dict(id="24", block="ponte", text=
        "{a}Agora vamos sair das frações [p=0.2] e ir para a *vírgula:* [p=0.3] {b}somar, [p=0.2] multiplicar e dividir decimais "
        "sem calculadora, [p=0.3] {c}incluindo uma divisão cujo resultado *assusta,* [p=0.2] mas está certo. [p=0.4] {d}Próximo "
        "episódio."),
    dict(id="25", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no *do restante?* "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
