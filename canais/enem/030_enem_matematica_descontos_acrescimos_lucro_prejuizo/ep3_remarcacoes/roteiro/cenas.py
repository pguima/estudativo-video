# Roteiro — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 3 de 4: remarcações, liquidações e o lucro que sobra
# Base: Estudos/Enem/estudos/01-matematica/15-descontos-acrescimos-lucro-prejuizo.html — seção 08 + estratégia 2 da
#   seção 09 ("trabalhe com um preço de 100") + Questões 9 e 4 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A RÉGUA DO CUSTO: comece no custo (= 1) e vá multiplicando os fatores até o preço final; o que passar de 1 é lucro,
#     o que faltar é prejuízo.
#   O CUSTO VALE 100: com 100 no começo, cada fator vira um número visível (100 → 160 → 112).
#   NO "LUCRO EM UM, PREJUÍZO EM OUTRO", o item do prejuízo era o mais caro: os mesmos p% pesam mais reais nele.
#   (Da série: TODA PORCENTAGEM TEM DONO, do episódio 1; fatores encadeados, do episódio 2.)
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Gancho: "33%" é o terço arredondado; o bloco a faz a conta exata com 1/3 (1,5 · 2/3 = 1), como o material.
# Exemplos do material/prompt: 1,5 · 2/3 = 1 · custo 100 → 150 → 100 · nós fazemos: 40 → 60 → 42 (1,5 · 0,7 = 1,05;
#   lucro R$ 2,00 = 5% de 40).
# Exemplo NOSSO no bloco c (a Questão 4 é "você faz" e usa R$ 600,00 e 20%): duas bicicletas usadas vendidas por
#   R$ 300,00 cada, uma com 50% de lucro e outra com 50% de prejuízo sobre o custo → custos 300 ÷ 1,5 = 200 e
#   300 ÷ 0,5 = 600; custo total 800, venda 600 → prejuízo de R$ 200,00 (ganhou 100, perdeu 300).
# Erro 3 com o fator do "nós fazemos" (1,05 = lucro de 5%, não 105%), para não entregar a Questão 9 antes do "eu faço".
#   Erro 2 usa 60% e 30% como o prompt pede, mas sem dar a resposta (fica para a Questão 9).
# Atalhos (NOSSOS, verde): "invente o custo 100" (bloco b) · "mesmo preço e mesma porcentagem: é sempre prejuízo;
#   risque 'empate' e 'lucro'" (bloco c) · "fator − 1 = lucro" (bloco a / erro 3).
# QUESTÃO 9 (eu faço): 1,6 · 0,7 = 1,12 → lucro de 12% (A); em reais 50 → 80 → 56, lucro 6 ÷ 50 = 12%. Erradas (material):
#   B 60 − 30 (bases diferentes); C 60 · 0,7 = 42 (desconto só sobre a margem); D ignora a liquidação; E lê 1,12 como 112%.
# QUESTÃO 4 (você faz): 600 ÷ 1,2 = 500 e 600 ÷ 0,8 = 750; custo 1.250, venda 1.200 → prejuízo de R$ 50,00 (E).
#   Erradas (material): A acha que se anulam; B valor certo com sinal trocado; C 600 · 0,96 = 576 → 24; D 1.200 · 0,96 =
#   1.152 → 48 (tratam como um produto reajustado duas vezes).
# Frases-chave (meio e fim, idênticas): 1. Leve tudo para a régua do custo e multiplique os fatores.
#   2. Desconto menor pode anular margem maior. 3. Lucro de p% e prejuízo de p% no mesmo preço dão prejuízo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A liquidação comeu o lucro? Remarcações e o lucro que sobra · Matemática ENEM, Descontos e Lucro episódio 3"

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
        "{a}Uma loja põe *cinquenta por cento de lucro* na etiqueta. [p=0.4] {b}Na liquidação, [p=0.2] dá só *trinta e "
        "três por cento* de desconto. [p=0.4] {c}Sobrou dezessete por cento de lucro? [p=0.5] {d}Sobrou *zero.* "
        "[p=0.3] Ela vendeu pelo *preço de custo.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber se uma remarcação seguida de liquidação *ainda dá lucro* "
        "[p=0.3] {b}e por que lucro e prejuízo de mesma porcentagem *não empatam.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] lucro sobre o custo [p=0.2] é o lucro em reais "
        "[p=0.2] *dividido pelo custo.* [p=0.4] {b}Do episódio dois: [p=0.2] porcentagens em sequência [p=0.2] "
        "*multiplicam os fatores.* [p=0.2] E para voltar, [p=0.2] *divida pelo fator.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pense numa loja de tênis em *queima de estoque.* [p=0.4] {b}A *etiqueta* é o preço marcado no produto. "
        "[p=0.2] A *remarcação* é trocar esse preço: [p=0.2] a etiqueta antiga fica riscada, [p=0.2] e a nova vem por "
        "cima. [p=0.4] {c}E a *liquidação* é o desconto [p=0.2] para esvaziar a loja."),
    dict(id="05", block="concreto", text=
        "{a}Agora, um lojista que vende *dois celulares usados* [p=0.2] pelo *mesmo preço.* [p=0.4] {b}Num, ele ganha "
        "vinte por cento. [p=0.2] No outro, perde vinte por cento. [p=0.4] {c}Empatou? [p=0.3] Guarde essa pergunta."),

    # ================= BLOCO A: A RÉGUA DO CUSTO =================
    dict(id="06", block="regua", text=
        "{t}Como saber se ainda sobra lucro? [p=0.4] {a}Use a *régua do custo.* [p=0.2] O custo vale *um.* [p=0.4] "
        "{b}Cada porcentagem vira um *fator sobre o custo:* [p=0.2] cinquenta por cento a mais [p=0.2] leva o preço a "
        "*um vírgula cinco.* [p=0.4] {c}Um terço de desconto [p=0.2] deixa *dois terços* da etiqueta. [p=0.2] Um "
        "vírgula cinco vezes dois terços: [p=0.2] *um.* [p=0.4] {d}Passou de um, [p=0.2] é lucro. [p=0.2] Faltou, "
        "[p=0.2] é prejuízo. [p=0.2] Deu um: [p=0.2] *empate.*"),
    dict(id="07", block="regua", text=
        "{t}Como um desconto *menor* apagou uma margem *maior?* [p=0.4] {a}Porque o desconto "
        "[p=0.2] incide sobre a *etiqueta,* [p=0.2] que já é maior que o custo. [p=0.4] {b}É a assimetria de sempre, "
        "[p=0.2] agora com *dinheiro de comerciante.*"),

    # ================= BLOCO B: O TRUQUE DO 100 =================
    dict(id="08", block="cem", text=
        "{t}E se fração te dá medo? [p=0.4] {a}Faça o *custo valer cem.* [p=0.4] {b}Cinquenta por cento a mais: "
        "[p=0.2] etiqueta de *cento e cinquenta.* [p=0.4] {c}Um terço de desconto: [p=0.2] tire cinquenta. [p=0.2] "
        "Volta para *cem.* [p=0.4] {d}Atalho de prova: [p=0.2] questão só com porcentagens? [p=0.2] "
        "*Invente o custo cem.*"),

    # ================= BLOCO C: LUCRO EM UM, PREJUÍZO EM OUTRO =================
    dict(id="09", block="dois", text=
        "{t}E o mesmo preço com lucro e prejuízo? [p=0.4] {a}Duas bicicletas usadas, [p=0.2] vendidas por *trezentos "
        "reais* cada. [p=0.2] Numa, *cinquenta por cento de lucro.* [p=0.2] Na outra, *cinquenta por cento de "
        "prejuízo.* [p=0.4] {b}Descubra cada custo [p=0.2] *dividindo o preço pelo fator.* [p=0.2] Trezentos por um "
        "vírgula cinco: [p=0.2] *duzentos.* [p=0.2] Trezentos por zero vírgula cinco: [p=0.2] *seiscentos.*"),
    dict(id="10", block="dois", text=
        "{t}Agora o *resultado global,* [p=0.2] que é a soma das duas vendas. [p=0.4] {a}Custou oitocentos. [p=0.2] "
        "Vendeu seiscentos. [p=0.2] *Prejuízo de duzentos reais.* [p=0.4] {b}O item do prejuízo *era o mais caro.* "
        "[p=0.2] Os mesmos cinquenta por cento [p=0.2] pesam *trezentos reais* nele, [p=0.2] e só cem no outro. "
        "[p=0.4] {c}Atalho: [p=0.2] mesmo preço e mesma porcentagem [p=0.2] dão *sempre prejuízo.* [p=0.2] Risque "
        "empate e risque lucro."),

    # ================= NÓS FAZEMOS =================
    dict(id="11", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um produto custa *quarenta reais,* [p=0.2] vai para a etiqueta com *cinquenta por cento "
        "sobre o custo* [p=0.2] e entra numa liquidação de *trinta por cento* sobre a etiqueta. [p=0.4] {b}Lucro ou "
        "prejuízo, [p=0.2] e de quanto sobre o custo? [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="12", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Na régua do custo: [p=0.2] um vírgula cinco vezes zero vírgula sete. [p=0.2] "
        "*Um vírgula zero cinco.* [p=0.2] Passou de um: [p=0.2] *lucro de cinco por cento.* [p=0.4] {b}Confira em "
        "reais: [p=0.2] quarenta, [p=0.2] sessenta, [p=0.2] *quarenta e dois.* [p=0.2] Lucro de *dois reais.* [p=0.4] "
        "{c}Dois dividido por quarenta: [p=0.2] *cinco por cento.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="13", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] leve tudo para a régua do custo e multiplique os "
        "fatores. [p=0.5] {b}Dois: [p=0.2] desconto menor pode anular margem maior. [p=0.5] {c}Três: [p=0.2] lucro de "
        "p por cento e prejuízo de p por cento no mesmo preço dão prejuízo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="14", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que lucro e prejuízo de mesma "
        "porcentagem *se anulam.* [p=0.4] {b}Parece certo, [p=0.2] porque mais vinte e menos vinte dá zero. [p=0.4] "
        "{c}Mas cada porcentagem tem o seu custo, [p=0.2] e os custos são *diferentes.*"),
    dict(id="15", block="erros", text=
        "{a}Segundo: [p=0.2] *subtrair as porcentagens.* [p=0.2] Margem de sessenta, [p=0.2] liquidação de trinta, "
        "[p=0.2] lucro de trinta. [p=0.4] {b}Parece certo: [p=0.2] os dois estão em por cento. [p=0.4] "
        "{c}Mas os sessenta são do *custo,* [p=0.2] e os trinta são da *etiqueta.* [p=0.2] Bases diferentes: [p=0.2] "
        "*multiplique os fatores.*"),
    dict(id="16", block="erros", text=
        "{a}Terceiro: [p=0.2] *ler o fator como lucro.* [p=0.2] Fator um vírgula zero cinco [p=0.2] virar lucro de "
        "cento e cinco por cento. [p=0.4] {b}Parece certo: [p=0.2] é só passar a vírgula. [p=0.4] {c}Mas o "
        "*um* é o próprio custo. [p=0.2] Lucro é o que *passa de um:* [p=0.2] *cinco por cento.*"),

    # ================= QUESTÃO 9 (EU FAÇO) =================
    dict(id="17", block="q9", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma loja compra um "
        "tênis por *cinquenta reais* [p=0.2] e o etiqueta com *sessenta por cento de lucro sobre o custo.* [p=0.2] Na "
        "liquidação, [p=0.2] dá *trinta por cento de desconto* sobre o preço da etiqueta. [p=0.2] Na venda feita "
        "durante a liquidação, [p=0.2] o lucro da loja em relação ao custo é de: [p=0.4] {qa}A: [p=0.2] doze por "
        "cento. [p=0.3] {qb}B: [p=0.2] trinta. [p=0.3] {qc}C: [p=0.2] quarenta e dois. [p=0.3] {qd}D: [p=0.2] sessenta. "
        "[p=0.3] {qe}E: [p=0.2] cento e doze por cento. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="18", block="q9", text=
        "{t}Eu resolvo com você. [p=0.3] {a}Os fatores: [p=0.2] *um vírgula seis* [p=0.2] e *zero "
        "vírgula sete.* [p=0.4] {b}Multiplique: [p=0.2] *um vírgula doze.* [p=0.2] *Lucro de doze por cento.* "
        " [p=0.4] {c}Confira em reais: [p=0.2] cinquenta, [p=0.2] oitenta, [p=0.2] "
        "*cinquenta e seis.* [p=0.2] Lucro de seis reais. [p=0.2] Seis sobre cinquenta: [p=0.2] doze por cento. "
        "[p=0.3] {ok}*Letra A!*"),
    dict(id="19", block="q9", text=
        "{t}E as outras? [p=0.3] {xb}A B subtrai sessenta menos trinta: [p=0.2] *bases diferentes.* [p=0.4] {xc}A C "
        "aplica o desconto *só sobre a margem:* [p=0.2] sessenta vezes zero vírgula sete. [p=0.4] {xd}A D *ignora a "
        "liquidação.* [p=0.4] {xe}E a E lê o fator um vírgula doze [p=0.2] como lucro de *cento e doze.*"),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="20", block="q4", text=
        "{t}Agora é com você: [p=0.2] o lojista do começo. [p=0.4] {a}Um lojista vendeu dois aparelhos por "
        "*seiscentos reais* cada. [p=0.2] No primeiro, [p=0.2] teve *lucro de vinte por cento* sobre o preço de custo. "
        "[p=0.2] No segundo, [p=0.2] *prejuízo de vinte por cento* sobre o preço de custo. [p=0.2] Considerando as duas "
        "vendas, [p=0.2] o lojista teve: [p=0.4] {qa}A: [p=0.2] nem lucro nem prejuízo. [p=0.3] {qb}B: [p=0.2] lucro "
        "de cinquenta reais. [p=0.3] {qc}C: [p=0.2] prejuízo de vinte e quatro reais. [p=0.3] {qd}D: [p=0.2] prejuízo "
        "de quarenta e oito reais. [p=0.3] {qe}E: [p=0.2] prejuízo de cinquenta reais. [p=0.4] {p}*Pause o vídeo e "
        "resolva sozinho.* [p=2.5]"),
    dict(id="21", block="q4", text=
        "{t}Vamos conferir. [p=0.3] {a}Cada custo: [p=0.2] seiscentos por um vírgula dois, [p=0.2] *quinhentos.* "
        "[p=0.2] Seiscentos por zero vírgula oito, [p=0.2] *setecentos e cinquenta.* [p=0.4] {b}Custo total, [p=0.2] "
        "*mil, duzentos e cinquenta.* [p=0.2] Venda total, [p=0.2] *mil e duzentos.* [p=0.4] {c}*Prejuízo de "
        "cinquenta reais.* [p=0.3] {ok}*Letra E!*"),
    dict(id="22", block="q4", text=
        "{t}E as pegadinhas? [p=0.3] {xa}A A é a intuição de que *se anulam.* [p=0.4] {xb}A B tem o valor certo [p=0.2] "
        "e o *sinal trocado.* [p=0.4] {xd}A D faz um vírgula dois vezes zero vírgula oito, [p=0.2] *zero vírgula "
        "noventa e seis,* [p=0.2] sobre os mil e duzentos. [p=0.4] {xc}E a C faz o mesmo sobre seiscentos. [p=0.4] "
        "{c}As duas tratam o caso como *um produto só.* [p=0.2] Mas são dois, [p=0.2] com custos diferentes."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="23", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] leve tudo para a régua do custo e multiplique "
        "os fatores. [p=0.5] {b}Dois: [p=0.2] desconto menor pode anular margem maior. [p=0.5] {c}Três: [p=0.2] lucro "
        "de p por cento e prejuízo de p por cento no mesmo preço dão prejuízo."),

    # ================= PONTE E CTA =================
    dict(id="24", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e "
        "treinamos com questões inéditas."),
    dict(id="25", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] etiqueta com cem por cento de lucro [p=0.2] e liquidação de "
        "cinquenta por cento. [p=0.2] Sobra lucro? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um "
        "link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para "
        "revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
