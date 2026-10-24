# Roteiro — Porcentagem, Episódio 2 de 6: O fator de multiplicação, a ferramenta que resolve quase tudo
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seção 04 (+ Questão 2 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O fator é uma MÁQUINA: entra o preço antigo, sai o preço novo, numa multiplicação só.
#   O "1" do fator é o valor que você JÁ TINHA; o que vem depois da vírgula é o que entra ou sai:
#   1,25 = o que eu tinha + um quarto; 0,75 = o que eu tinha − um quarto.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos dos blocos (NÃO usam R$ 80 com +25%, que é a Questão 2): reajuste de 25% num produto de R$ 60 (15 → 75 · fator
#   1,25 → 75); desconto de 40% num tênis de R$ 200 (80 → 120 · fator 0,60 → 120); salário de R$ 1 500 que dobrou (fator 2 →
#   R$ 3 000); +200% sobre R$ 1 500 (fator 3 → R$ 4 500). Caminho longo e curto sempre lado a lado.
# Tabela da seção 04 (jogo): +5% 1,05 · +10% 1,10 · +20% 1,20 · +25% 1,25 · +50% 1,50 · +100% 2 · +200% 3 · +300% 4 ·
#   −5% 0,95 · −10% 0,90 · −25% 0,75 · −40% 0,60.
# Caminho de volta: 1,5 → +50% · 0,65 → −35% (1 − 0,65 = 0,35).
# Nós fazemos (prompt): fator de +15% = 1,15 · −30% = 0,70 · +150% = 2,5; variação de 1,08 = +8% · 0,85 = −15% · 2,5 = +150%.
# QUESTÃO 2 do material (texto idêntico na tela): R$ 80 com reajuste de 25% → 80 · 1,25 = R$ 100 → C. Caminho longo:
#   25% de 80 = 20 → 80 + 20 = 100. Atalho: 25% é um quarto → 80 ÷ 4 = 20.
#   O material não explica as erradas; explicações NOSSAS: D (105) = somou 25 REAIS em vez de 25% · B (96) = usou 20%
#   (fator 1,20) · E (120) = usou 50% (fator 1,50) · A (85) = não sai de conta coerente (aumento de só R$ 5).
#   Conferência de bom senso: 25% de 80 são 20 reais, então só pode ser 100.
# Atalhos (verde): "desconto: o fator é o que SOBRA (100 − 40 = 60 → 0,60)" · "aumento de 5% é 1,05, não 1,5: a taxa ocupa
#   duas casas depois da vírgula" · "maior que 1? aumento: o que passa do 1. Menor que 1? desconto: o que falta para o 1".
# Frases-chave (meio e fim, idênticas): 1. Aumento: 1 + a taxa. Desconto: 1 − a taxa. 2. O 1 é o que você já tinha.
#   3. Aumentar 200% é triplicar.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Fator de multiplicação: aumentos e descontos numa conta só (aumentar 200% é triplicar) · Matemática ENEM, episódio 2"

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
        "{a}Aumentar *duzentos por cento* é dobrar? [p=0.5] {b}Não: [p=0.2] é *triplicar.* [p=0.5] {c}E a ferramenta que "
        "explica isso [p=0.2] também resolve as questões mais difíceis de porcentagem [p=0.3] {d}com uma *única "
        "multiplicação.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai escrever o *fator* de qualquer aumento ou desconto [p=0.2] *sem pensar* "
        "[p=0.3] {b}e ler um fator *ao contrário.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio um. [p=0.3] {a}Porcentagem é *por cem:* [p=0.2] vinte e cinco por cento "
        "é vinte e cinco de cem, [p=0.2] *zero vírgula vinte e cinco.* [p=0.4] {b}Dez por cento, [p=0.2] *zero vírgula um.* "
        "[p=0.3] Cinco por cento, [p=0.2] *zero vírgula zero cinco.* [p=0.4] {c}Essa é a *forma decimal,* [p=0.2] e hoje ela "
        "vira uma máquina."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Você já viu essas placas. [p=0.3] {a}*Vinte e cinco por cento de reajuste.* [p=0.3] {b}*Quarenta por cento de "
        "desconto.* [p=0.3] {c}E aquele salário que *dobrou.* [p=0.4] {d}Em todas, [p=0.2] a pergunta é a mesma: [p=0.2] "
        "*quanto fica o valor novo?*"),
    dict(id="05", block="concreto", text=
        "{t}Um produto custa *sessenta reais* [p=0.2] e tem reajuste de vinte e cinco por cento. [p=0.4] {a}O caminho que "
        "todo mundo faz: [p=0.2] primeiro a parte. [p=0.2] Vinte e cinco por cento de sessenta, [p=0.2] *quinze.* [p=0.4] "
        "{b}Depois soma: [p=0.2] sessenta mais quinze, [p=0.2] *setenta e cinco.* [p=0.4] {c}Duas contas. [p=0.3] E se desse "
        "para fazer em *uma só?*"),

    # ================= BLOCO A: O FATOR DE AUMENTO =================
    dict(id="06", block="aumento", text=
        "{t}Dá. [p=0.2] Com o *fator de multiplicação:* [p=0.3] o número que, vezes o valor antigo, [p=0.2] já entrega o "
        "valor novo. [p=0.4] {a}Pense numa *máquina.* [p=0.3] {b}Entra o preço antigo, [p=0.2] *sessenta.* [p=0.3] {c}A "
        "máquina multiplica por *um vírgula vinte e cinco.* [p=0.3] {d}E sai o preço novo: [p=0.2] *setenta e cinco.* "
        "[p=0.3] Mesmo resultado, [p=0.2] numa conta só."),
    dict(id="07", block="aumento", text=
        "{t}Mas por que *um vírgula vinte e cinco?* [p=0.3] {a}O *um* é o que você *já tinha:* [p=0.2] os sessenta inteiros. "
        "[p=0.4] {b}O *zero vírgula vinte e cinco* é o que *entra:* [p=0.2] um quarto a mais. [p=0.4] {c}Juntando: [p=0.2] "
        "aumento de x por cento, [p=0.2] fator igual a *um mais a taxa.* [p=0.3] A taxa em decimal, [p=0.2] que é o x "
        "dividido por cem."),

    # ================= BLOCO B: O FATOR DE DESCONTO =================
    dict(id="08", block="desconto", text=
        "{t}E no desconto? [p=0.3] {a}Um tênis de *duzentos reais* [p=0.2] com quarenta por cento de desconto. [p=0.4] "
        "{b}Caminho longo: [p=0.2] quarenta por cento de duzentos, [p=0.2] *oitenta.* [p=0.2] Duzentos menos oitenta, "
        "[p=0.2] *cento e vinte.* [p=0.4] {c}Caminho curto: [p=0.2] o fator é *um menos zero vírgula quatro,* [p=0.2] *zero "
        "vírgula seis.* [p=0.3] Duzentos vezes zero vírgula seis, [p=0.2] *cento e vinte.* [p=0.3] Bateu!"),
    dict(id="09", block="desconto", text=
        "{t}O zero vírgula seis tem um significado. [p=0.3] {a}Do que você tinha, [p=0.2] *saem* quarenta por cento [p=0.2] e "
        "*ficam* sessenta. [p=0.4] {b}Desconto de x por cento: [p=0.2] fator igual a *um menos a taxa.* [p=0.4] {c}Atalho: "
        "[p=0.2] no desconto, [p=0.2] o fator é *o que sobra.* [p=0.3] Cem menos quarenta, [p=0.2] sessenta: [p=0.2] *zero "
        "vírgula seis.*"),
    dict(id="10", block="desconto", text=
        "{t}Um cuidado com os números pequenos. [p=0.3] {a}Aumento de *cinco* por cento [p=0.2] não é um vírgula cinco. "
        "[p=0.4] {b}Cinco por cento é *zero vírgula zero cinco.* [p=0.3] Então o fator é *um vírgula zero cinco.* [p=0.4] "
        "{c}Atalho: [p=0.2] a taxa sempre ocupa *duas casas* depois da vírgula."),

    # ================= BLOCO C: A TABELA EM RITMO DE JOGO =================
    dict(id="11", block="jogo", text=
        "{t}Agora, em ritmo de jogo: [p=0.2] eu falo a variação, [p=0.2] você diz o fator. [p=0.4] {a}Mais cinco por cento? "
        "[p=0.8] *Um vírgula zero cinco.* [p=0.3] {b}Mais dez? [p=0.8] *Um vírgula um.* [p=0.3] {c}Mais vinte? [p=0.8] *Um "
        "vírgula dois.* [p=0.3] {d}Mais vinte e cinco? [p=0.8] *Um vírgula vinte e cinco.* [p=0.3] {e}Mais cinquenta? "
        "[p=0.8] *Um vírgula cinco.*"),
    dict(id="12", block="jogo", text=
        "{t}Agora os descontos. [p=0.3] {a}Menos cinco por cento? [p=0.8] *Zero vírgula noventa e cinco.* [p=0.3] {b}Menos "
        "dez? [p=0.8] *Zero vírgula nove.* [p=0.3] {c}Menos vinte e cinco? [p=0.8] *Zero vírgula setenta e cinco.* [p=0.3] "
        "{d}Menos quarenta? [p=0.8] *Zero vírgula seis.* [p=0.4] {e}E repare: [p=0.2] zero vírgula setenta e cinco [p=0.2] é o "
        "que você tinha, [p=0.2] *menos um quarto.*"),

    # ================= BLOCO D: 100% E 200% =================
    dict(id="13", block="dobra", text=
        "{t}E os aumentos *grandes?* [p=0.3] {a}Um salário de *mil e quinhentos reais* [p=0.2] aumenta *cem por cento.* "
        "[p=0.4] {b}Fator: [p=0.2] um mais um, [p=0.2] *dois.* [p=0.3] Mil e quinhentos vezes dois, [p=0.2] *três mil.* "
        "[p=0.4] {c}Aumentar cem por cento [p=0.2] é *dobrar.*"),
    dict(id="14", block="dobra", text=
        "{t}E *duzentos* por cento? [p=0.3] {a}Fator: [p=0.2] um mais dois, [p=0.2] *três.* [p=0.3] Mil e quinhentos vezes "
        "três, [p=0.2] *quatro mil e quinhentos.* [p=0.4] {b}É o que você tinha, [p=0.2] *mais duas vezes ele.* [p=0.4] "
        "{c}Aumentar duzentos por cento [p=0.2] é *triplicar.* [p=0.3] {d}E trezentos por cento? [p=0.2] Fator *quatro.* "
        "[p=0.2] Quadruplica."),

    # ================= BLOCO E: O CAMINHO DE VOLTA =================
    dict(id="15", block="volta", text=
        "{t}E se a questão der o *fator* [p=0.2] e perguntar a variação? [p=0.3] É ler o fator *ao contrário.* [p=0.4] "
        "{a}Um vírgula cinco: [p=0.2] o um é o que você tinha. [p=0.2] Passou zero vírgula cinco: [p=0.2] *aumento de "
        "cinquenta por cento.* [p=0.4] {b}Zero vírgula sessenta e cinco: [p=0.2] faltam zero vírgula trinta e cinco para "
        "chegar no um. [p=0.3] *Desconto de trinta e cinco por cento.*"),
    dict(id="16", block="volta", text=
        "{t}Guarde a regra do caminho de volta. [p=0.3] {a}Fator *maior* que um? [p=0.2] É aumento: [p=0.2] *o que passa do "
        "um.* [p=0.4] {b}Fator *menor* que um? [p=0.2] É desconto: [p=0.2] *o que falta para o um.*"),

    # ================= BLOCO F: POR QUE O FATOR É MELHOR =================
    dict(id="17", block="melhor", text=
        "{t}Por que trocar o caminho de sempre pelo fator? [p=0.3] {a}Primeiro: [p=0.2] é *uma* operação, [p=0.2] não duas. "
        "[p=0.2] Menos conta, [p=0.2] menos erro. [p=0.4] {b}Segundo, [p=0.2] e mais importante: [p=0.2] o fator deixa "
        "*encadear* máquinas. [p=0.3] {c}Aumento, [p=0.2] depois desconto, [p=0.2] depois outro aumento: [p=0.2] é só ligar "
        "uma máquina na outra. [p=0.3] Isso é o próximo episódio."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez, [p=0.2] em ritmo de jogo. [p=0.3] {a}Diga o fator: [p=0.2] *mais quinze por cento,* [p=0.2] *menos "
        "trinta por cento,* [p=0.2] *mais cento e cinquenta por cento.* [p=0.4] {b}*Pause o vídeo e responda.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Mais quinze: [p=0.2] *um vírgula quinze.* [p=0.3] {b}Menos trinta: [p=0.2] sobram "
        "setenta, [p=0.2] *zero vírgula sete.* [p=0.3] {c}Mais cento e cinquenta: [p=0.2] um mais um vírgula cinco, [p=0.2] "
        "*dois vírgula cinco.*"),
    dict(id="20", block="exercicio2", text=
        "{t}Agora ao contrário. [p=0.3] {a}Diga a variação: [p=0.2] fator *um vírgula zero oito,* [p=0.2] *zero vírgula "
        "oitenta e cinco,* [p=0.2] *dois vírgula cinco.* [p=0.4] {b}*Pause o vídeo e responda.* [p=2.0]"),
    dict(id="21", block="exercicio2", text=
        "{t}Conferindo. [p=0.3] {a}Um vírgula zero oito: [p=0.2] passou zero vírgula zero oito, [p=0.2] *aumento de oito por "
        "cento.* [p=0.3] {b}Zero vírgula oitenta e cinco: [p=0.2] faltam quinze, [p=0.2] *desconto de quinze por cento.* "
        "[p=0.3] {c}Dois vírgula cinco: [p=0.2] passou um vírgula cinco, [p=0.2] *aumento de cento e cinquenta por cento.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] aumento, [p=0.2] um mais a taxa. [p=0.2] Desconto, [p=0.2] "
        "um menos a taxa. [p=0.5] {b}Dois: [p=0.2] o um é o que você já tinha. [p=0.5] {c}Três: [p=0.2] aumentar duzentos por "
        "cento é triplicar."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que aumentar *duzentos por cento* é dobrar. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque duzentos lembra *duas vezes.* [p=0.4] {c}Mas o fator é um mais dois, "
        "[p=0.2] *três.* [p=0.3] Dobrar é cem por cento."),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] usar *zero vírgula vinte e cinco* como fator de um aumento de vinte e cinco por cento. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque zero vírgula vinte e cinco *é* vinte e cinco por cento. [p=0.4] {c}Mas sessenta "
        "vezes zero vírgula vinte e cinco dá *quinze:* [p=0.2] o preço teria *despencado.* [p=0.3] Faltou o um, [p=0.2] o que "
        "você já tinha."),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] ler o fator *zero vírgula sessenta e cinco* [p=0.2] como desconto de sessenta e cinco por cento. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o sessenta e cinco está ali, [p=0.2] bem à vista. [p=0.4] {c}Mas sessenta e "
        "cinco é o que *fica.* [p=0.3] O desconto é o que *sai:* [p=0.2] trinta e cinco por cento."),

    # ================= QUESTÃO 2 DO MATERIAL =================
    dict(id="26", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um produto que custava "
        "*oitenta reais* [p=0.2] sofreu reajuste de *vinte e cinco por cento.* [p=0.3] {b}O novo preço do produto é: [p=0.4] "
        "{qa}A: [p=0.2] oitenta e cinco reais. [p=0.3] {qb}B: [p=0.2] noventa e seis. [p=0.3] {qc}C: [p=0.2] cem. [p=0.3] "
        "{qd}D: [p=0.2] cento e cinco. [p=0.3] {qe}E: [p=0.2] cento e vinte. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q2", text=
        "{t}Vamos resolver. [p=0.3] {a}Pelo fator: [p=0.2] aumento de vinte e cinco por cento, [p=0.2] *um vírgula vinte e "
        "cinco.* [p=0.3] Oitenta vezes um vírgula vinte e cinco: [p=0.2] *cem.* [p=0.4] {b}Pelo caminho longo: [p=0.2] vinte "
        "e cinco por cento de oitenta é vinte, [p=0.2] e oitenta mais vinte, [p=0.2] *cem.* [p=0.4] {c}E o atalho: [p=0.2] "
        "vinte e cinco por cento é *um quarto.* [p=0.2] Oitenta dividido por quatro, [p=0.2] vinte. [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="q2", text=
        "{t}E as outras? [p=0.3] {xd}A D somou *vinte e cinco reais,* [p=0.2] e não vinte e cinco por cento. [p=0.4] {xb}A B "
        "usou vinte por cento, [p=0.2] {xe}e a E, [p=0.2] cinquenta. [p=0.4] {xa}E a A não sai de nenhuma conta certa. "
        "[p=0.4] {chk}Conferência de bom senso: [p=0.2] um quarto de oitenta são vinte reais. [p=0.2] Só pode dar *cem.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] aumento, [p=0.2] um mais a taxa. [p=0.2] Desconto, "
        "[p=0.2] um menos a taxa. [p=0.5] {b}Dois: [p=0.2] o um é o que você já tinha. [p=0.5] {c}Três: [p=0.2] aumentar "
        "duzentos por cento é triplicar."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Um aumento de *dez por cento* [p=0.2] e depois outro de *vinte.* [p=0.3] {b}Deu trinta por cento? [p=0.4] "
        "{c}*Não.* [p=0.4] {d}É aqui que está a maior parte dos pontos deste assunto. [p=0.3] Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achava que aumentar duzentos por cento era dobrar? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
