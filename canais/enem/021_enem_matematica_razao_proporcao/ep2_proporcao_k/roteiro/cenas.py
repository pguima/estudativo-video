# Roteiro — Razão, Proporção e Regra de Três, Episódio 2 de 6: Proporção, a propriedade que faz tudo funcionar e o truque do k
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seções 04 e 05 (+ Questão 7 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A MESMA RECEITA EM TAMANHOS DIFERENTES: 2 ovos : 3 xícaras = 4 ovos : 6 xícaras.
#   PONTAS E MIOLO: extremos (a, d) = pontas · meios (b, c) = miolo · pontas × pontas = miolo × miolo.
#   PACOTINHOS DE k: razão 2 para 3 → um recebe 2 pacotinhos, o outro 3; total ÷ nº de pacotinhos = k.
# Exemplos (todos conferidos): 2·6 = 3·4 = 12 · 2/3 = x/12 → x = 8 · 3/2 = 6/4 (inverteu as duas) · 3/2 ≠ 4/6 (18 ≠ 8) ·
#   (2+4)/(3+6) = 6/9 = 2/3 · sócias: R$ 10 000 em 2 para 3 → k = 2 000 → 4 000 e 6 000 · 60 balas em 1:2:3 → k = 10 →
#   10, 20, 30 · contínua 2/4 = 4/8 → 4² = 2·8 = 16.
#   DESVIO: o prompt usa no bloco f) "razão 3/5 e soma 64 → 24 e 40", que é a própria Questão 7 (R$ 64 000 em 3 para 5);
#   trocado pelas sócias (R$ 10 000 em 2 para 3) para não entregar a resposta antes da questão.
#   Não entra a propriedade "soma com o consequente" (a+b)/b = (c+d)/d da seção 05: o prompt não a lista nos blocos.
# Nós fazemos: x/12 = 5/4 → 4x = 60 → x = 15 · 90 na razão 2 para 7 → 9k = 90 → k = 10 → 20 e 70.
# QUESTÃO 7 do material (texto idêntico na tela): R$ 64 000 em 3 para 5 → 8k = 64 000 → k = 8 000 → 24 000 e 40 000 → D.
#   A (24 000) = a parte menor; B (32 000) = partes iguais (explicações do material).
#   Explicações NOSSAS (o material não explica C e E): C (38 400) = 3/5 de 64 000, tratou "3 para 5" como "3 quintos do
#   total" (são 3 partes de 8); E (48 000) não sai de nenhuma conta certa: sobrariam 16 000, e 48 000 para 16 000 é 3 para 1.
# Frases-chave (meio e fim, idênticas, do prompt):
#   1. Proporção é a mesma receita em tamanhos diferentes.
#   2. Pontas vezes pontas = miolo vezes miolo.
#   3. Razão e soma? Pacotinhos de k.
# Atalhos (verde): "multiplique a diagonal completa e divida pelo número da diagonal do x" · "some os números da razão,
#   divida o total por essa soma e multiplique" · conferência "as partes somam o total? estão na razão?".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Proporção: por que a regra de três funciona e o truque do k | Razão e Proporção Ep. 2"
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
        "{a}Toda regra de três que você já fez na vida [p=0.2] funciona por causa de *uma* propriedade. [p=0.5] {b}Hoje "
        "você vai entender *qual é,* [p=0.3] {c}e ganhar um *truque* [p=0.2] que resolve em uma linha [p=0.2] problemas que "
        "parecem difíceis."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber *por que a regra de três funciona,* [p=0.4] {b}e dividir qualquer "
        "valor [p=0.2] numa *razão* dada."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}*Razão,* do episódio anterior, [p=0.2] é comparar dividindo: [p=0.2] "
        "dois para três [p=0.2] é *dois terços.* [p=0.4] {b}E frações *equivalentes,* da série de Frações, [p=0.2] são o mesmo "
        "pedaço escrito de outro jeito: [p=0.2] {c}um meio, [p=0.2] dois quartos, [p=0.2] três sextos. [p=0.3] A mesma metade."),

    # ================= BLOCO A: PROPORÇÃO =================
    dict(id="04", block="receita", text=
        "{t}Uma receita de bolo leva *dois ovos* [p=0.2] para *três xícaras* de farinha. [p=0.4] {a}Você quer um bolo maior, "
        "[p=0.2] para uma festa. [p=0.3] Dobra tudo: [p=0.2] {b}*quatro ovos* [p=0.2] para *seis xícaras.* [p=0.4] {c}É outro "
        "bolo? [p=0.3] Não: [p=0.2] é *a mesma receita,* [p=0.2] em tamanho maior. [p=0.3] {d}O gosto não muda, [p=0.2] porque "
        "a comparação entre ovos e farinha [p=0.2] continua a mesma."),
    dict(id="05", block="receita", text=
        "{t}Em matemática, [p=0.2] isso tem nome. [p=0.3] {a}Dois para três [p=0.2] é igual a quatro para seis. [p=0.4] {b}Uma "
        "igualdade entre duas razões [p=0.2] se chama *proporção.* [p=0.4] {c}No geral, [p=0.2] *a sobre b [p=0.2] igual a c "
        "sobre d.* [p=0.4] {d}Guarde a imagem: [p=0.2] proporção é a mesma receita [p=0.2] em tamanhos diferentes."),

    # ================= BLOCO B: EXTREMOS E MEIOS =================
    dict(id="06", block="pontas", text=
        "{t}Agora, uma pergunta: [p=0.2] nessa igualdade, [p=0.2] quem está nas *pontas?* [p=0.4] {a}Escreva em linha: [p=0.2] "
        "a está para b, [p=0.2] assim como c está para d. [p=0.4] {b}O *a* e o *d* ficam nas pontas: [p=0.2] eles se chamam "
        "*extremos.* [p=0.4] {c}O *b* e o *c* ficam no miolo: [p=0.2] eles se chamam *meios.* [p=0.4] {d}Pontas [p=0.2] e miolo."),

    # ================= BLOCO C: A PROPRIEDADE FUNDAMENTAL =================
    dict(id="07", block="fundamental", text=
        "{t}E aqui está a propriedade que faz tudo funcionar. [p=0.4] {a}Multiplique as pontas: [p=0.2] dois vezes seis, "
        "[p=0.2] *doze.* [p=0.4] {b}Agora o miolo: [p=0.2] três vezes quatro, [p=0.2] *doze!* [p=0.5] {c}Deu igual. [p=0.2] E "
        "isso vale em *toda* proporção: [p=0.3] {d}*a vezes d [p=0.2] igual a b vezes c.* [p=0.4] {e}É a *propriedade "
        "fundamental.* [p=0.3] Pontas vezes pontas, [p=0.2] igual a miolo vezes miolo."),
    dict(id="08", block="fundamental", text=
        "{t}Com as frações empilhadas, [p=0.2] as pontas e o miolo ficam em *xis.* [p=0.3] {a}Por isso essa conta tem outro "
        "nome: [p=0.2] *produto cruzado,* [p=0.2] que é multiplicar em diagonal. [p=0.4] {b}E por que ela faz a regra de três "
        "funcionar? [p=0.4] {c}Porque, quando falta um número, [p=0.2] ela acha ele. [p=0.3] {d}Dois para três, [p=0.2] igual "
        "a *xis* para doze, [p=0.2] e o xis é o número que falta. [p=0.4] {e}Pontas: [p=0.2] dois vezes doze, [p=0.2] vinte e "
        "quatro. [p=0.2] Miolo: [p=0.2] três vezes xis. [p=0.4] {f}Três xis igual a vinte e quatro: [p=0.2] *xis igual a oito.*"),
    dict(id="09", block="fundamental", text=
        "{t}Atalho para achar o número que falta: [p=0.3] {a}multiplique a diagonal que está *completa,* [p=0.3] {b}e divida "
        "pelo número que está *na diagonal do xis.* [p=0.4] {c}Dois vezes doze, [p=0.2] vinte e quatro; [p=0.2] dividido por "
        "três, [p=0.2] *oito.* [p=0.4] {d}Confira na receita: [p=0.2] oito ovos para doze xícaras. [p=0.2] Faz sentido: [p=0.2] "
        "é a receita multiplicada por quatro."),

    # ================= BLOCO D: INVERTER AS DUAS =================
    dict(id="10", block="inverter", text=
        "{t}E se você virar as razões de cabeça para baixo? [p=0.4] {a}Vire *as duas:* [p=0.2] três meios [p=0.2] e seis "
        "quartos. [p=0.3] {b}Continuam iguais: [p=0.2] três vezes quatro, doze; [p=0.2] dois vezes seis, doze. [p=0.4] {c}Agora "
        "vire *só uma:* [p=0.2] três meios [p=0.2] contra quatro sextos. [p=0.3] {d}Pontas: [p=0.2] três vezes seis, [p=0.2] "
        "dezoito. [p=0.2] Miolo: [p=0.2] dois vezes quatro, [p=0.2] oito. [p=0.3] {e}Quebrou! [p=0.4] {f}Inverter *as duas* "
        "mantém a proporção. [p=0.2] Inverter só um lado, [p=0.2] *não.*"),

    # ================= BLOCO E: SOMA DOS ANTECEDENTES =================
    dict(id="11", block="soma", text=
        "{t}Mais uma propriedade, [p=0.2] e ela é poderosa. [p=0.3] {a}Junte as duas receitas na mesma tigela: [p=0.2] dois "
        "ovos mais quatro, [p=0.2] *seis ovos.* [p=0.3] {b}Três xícaras mais seis, [p=0.2] *nove xícaras.* [p=0.4] {c}Seis para "
        "nove [p=0.2] simplifica para *dois terços:* [p=0.2] a mesma receita! [p=0.4] {d}Somar os de cima [p=0.2] e somar os de "
        "baixo [p=0.2] *mantém* a proporção. [p=0.4] {e}É por isso que dá para dividir um total [p=0.2] conhecendo só a razão. "
        "[p=0.3] E isso vira um truque."),

    # ================= BLOCO F: O TRUQUE DO k =================
    dict(id="12", block="pacotes", text=
        "{t}Duas sócias, [p=0.2] Ana e Bia, [p=0.2] combinaram dividir um lucro de *dez mil reais* [p=0.2] na razão *dois para "
        "três.* [p=0.4] {a}Quanto fica para cada uma? [p=0.4] {b}Pense em *pacotinhos* iguais. [p=0.2] Ana recebe *dois* "
        "pacotinhos; [p=0.2] Bia, *três.* [p=0.4] {c}Ao todo, [p=0.2] *cinco* pacotinhos. [p=0.4] {d}Dez mil dividido por "
        "cinco: [p=0.2] cada pacotinho vale *dois mil.*"),
    dict(id="13", block="pacotes", text=
        "{t}Agora é só abrir os pacotinhos. [p=0.3] {a}Ana: [p=0.2] dois pacotinhos de dois mil, [p=0.2] *quatro mil.* [p=0.3] "
        "{b}Bia: [p=0.2] três de dois mil, [p=0.2] *seis mil.* [p=0.4] {c}O tamanho de cada pacotinho [p=0.2] a matemática "
        "chama de *k:* [p=0.2] a *constante,* [p=0.2] um número que não muda. [p=0.4] {d}Em conta: [p=0.2] dois k mais três k "
        "[p=0.2] igual a dez mil. [p=0.2] Cinco k, [p=0.2] dez mil. [p=0.2] *k igual a dois mil.*"),
    dict(id="14", block="pacotes", text=
        "{t}E funciona com quantas partes você quiser. [p=0.3] {a}Sessenta balas, [p=0.2] divididas entre três irmãos [p=0.2] "
        "na razão um, [p=0.2] dois [p=0.2] e três. [p=0.4] {b}Pacotinhos: [p=0.2] um mais dois mais três, [p=0.2] *seis.* "
        "[p=0.3] {c}Sessenta dividido por seis: [p=0.2] *k igual a dez.* [p=0.3] {d}Dez, [p=0.2] vinte [p=0.2] e trinta balas. "
        "[p=0.4] {e}Atalho: [p=0.2] *some os números da razão, [p=0.2] divida o total por essa soma, [p=0.2] e multiplique.*"),

    # ================= BLOCO G: PROPORÇÃO CONTÍNUA =================
    dict(id="15", block="continua", text=
        "{t}Para fechar a teoria, [p=0.2] um caso especial, [p=0.2] só para você reconhecer. [p=0.4] {a}Dois para quatro, "
        "[p=0.2] igual a quatro para oito. [p=0.3] {b}Repare: [p=0.2] o miolo tem o *mesmo número* duas vezes. [p=0.4] {c}Isso "
        "é uma *proporção contínua.* [p=0.3] {d}Pontas: [p=0.2] dois vezes oito, [p=0.2] dezesseis. [p=0.2] Miolo: [p=0.2] "
        "quatro vezes quatro, [p=0.2] dezesseis. [p=0.4] {e}Esse quatro do meio [p=0.2] se chama *média geométrica* de dois e "
        "oito: [p=0.2] o número que, ao quadrado, [p=0.2] dá o produto das pontas."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas contas. [p=0.3] {a}Primeira: [p=0.2] xis sobre doze [p=0.2] igual a cinco quartos. [p=0.3] "
        "Ache o xis. [p=0.4] {b}Segunda: [p=0.2] divida *noventa* [p=0.2] na razão dois para sete. [p=0.4] {c}*Pause o vídeo e "
        "resolva.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Primeira, [p=0.2] em xis: [p=0.2] quatro vezes xis [p=0.2] igual a doze vezes cinco, "
        "[p=0.2] sessenta. [p=0.3] Sessenta dividido por quatro: [p=0.2] *xis igual a quinze.* [p=0.4] {b}Segunda: [p=0.2] dois "
        "mais sete, [p=0.2] nove pacotinhos. [p=0.3] Noventa dividido por nove: [p=0.2] k igual a dez. [p=0.3] {c}*Vinte* "
        "[p=0.2] e *setenta.* [p=0.3] {d}Confira: [p=0.2] vinte mais setenta, [p=0.2] noventa."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] proporção é a mesma receita em tamanhos diferentes. [p=0.5] "
        "{b}Dois: [p=0.2] pontas vezes pontas, [p=0.2] igual a miolo vezes miolo. [p=0.5] {c}Três: [p=0.2] razão e soma? "
        "[p=0.2] Pacotinhos de k."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] inverter *só uma* das razões. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque as duas frações continuam ali, [p=0.2] com os mesmos números. [p=0.4] {c}Mas a igualdade "
        "quebra. [p=0.2] Virou uma? [p=0.2] Vire *as duas.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] dividir em *partes iguais,* [p=0.2] ignorando a razão. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "dividir ao meio é o jeito mais comum de repartir. [p=0.4] {c}Mas razão dois para três [p=0.2] quer dizer *dois "
        "pacotinhos* para um [p=0.2] e *três* para o outro."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] responder a parte *menor* [p=0.2] quando o enunciado pede a *maior.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a primeira parte calculada [p=0.2] já aparece prontinha nas alternativas. [p=0.4] {c}Antes de marcar, "
        "[p=0.2] releia: [p=0.2] *qual parte* a questão quer?"),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="22", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Dois sócios dividiram um "
        "lucro de *sessenta e quatro mil reais* [p=0.2] na razão de *três para cinco.* [p=0.3] O sócio que recebeu a *maior* "
        "parte ficou com: [p=0.4] {qa}A: [p=0.2] vinte e quatro mil reais. [p=0.3] {qb}B: [p=0.2] trinta e dois mil. [p=0.3] "
        "{qc}C: [p=0.2] trinta e oito mil e quatrocentos. [p=0.3] {qd}D: [p=0.2] quarenta mil. [p=0.3] {qe}E: [p=0.2] quarenta "
        "e oito mil. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="questao", text=
        "{t}Vamos resolver com os pacotinhos. [p=0.3] {a}Razão três para cinco: [p=0.2] um sócio recebe três pacotinhos, "
        "[p=0.2] o outro, cinco. [p=0.2] *Oito* ao todo. [p=0.4] {b}Sessenta e quatro mil dividido por oito: [p=0.2] *k igual "
        "a oito mil.* [p=0.4] {c}Três vezes oito mil, [p=0.2] vinte e quatro mil. [p=0.2] Cinco vezes oito mil, [p=0.2] "
        "*quarenta mil.* [p=0.4] {d}A questão pede a *maior* parte: [p=0.2] quarenta mil reais. [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="questao", text=
        "{t}E as outras? [p=0.3] {xa}A A é a parte *menor:* [p=0.2] a armadilha de quem não releu a pergunta. [p=0.4] {xb}A B "
        "dividiu em partes iguais, [p=0.2] ignorando a razão. [p=0.4] {xc}A C tratou três para cinco [p=0.2] como *três quintos "
        "do total.* [p=0.2] Mas são três partes de *oito,* [p=0.2] não de cinco. [p=0.4] {xe}E a E não sai de nenhuma conta "
        "certa: [p=0.2] sobrariam dezesseis mil para o outro sócio, [p=0.2] e quarenta e oito para dezesseis [p=0.2] é três "
        "para *um.*"),
    dict(id="25", block="conferir", text=
        "{t}E um atalho para conferir qualquer divisão numa razão. [p=0.3] {a}As partes *somam o total?* [p=0.2] Vinte e "
        "quatro mil mais quarenta mil, [p=0.2] sessenta e quatro mil. [p=0.4] {b}E estão *na razão?* [p=0.2] Divida as duas "
        "por oito mil: [p=0.2] três e cinco. [p=0.4] {c}Passou nos dois testes? [p=0.2] Pode marcar."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] proporção é a mesma receita em tamanhos diferentes. "
        "[p=0.5] {b}Dois: [p=0.2] pontas vezes pontas, [p=0.2] igual a miolo vezes miolo. [p=0.5] {c}Três: [p=0.2] razão e "
        "soma? [p=0.2] Pacotinhos de k."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}Antes de qualquer regra de três, [p=0.2] existe uma *decisão:* [p=0.3] {b}a relação é *direta* ou *inversa?* "
        "[p=0.4] {c}Quem erra regra de três [p=0.2] quase sempre erra aqui. [p=0.4] {d}Próximo episódio."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia o truque dos pacotinhos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
