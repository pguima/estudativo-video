# Roteiro — Função Quadrática, Episódio 3 de 5: otimização, área máxima e receita máxima
# Base: Estudos/Enem/estudos/01-matematica/25-funcao-quadratica-vertice-raizes.html — seção 05 + Questões 3 e 2 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O CABO DE GUERRA: duas grandezas que se multiplicam e andam em sentidos opostos (preço sobe, vendas caem; lateral
#     cresce, frente encolhe) têm um produto com TOPO.
#   O ROTEIRO DE QUATRO PASSOS: escolher o x, escrever a grandeza em função dele, achar o vértice, responder o pedido.
#   RAÍZES DE CABEÇA, VÉRTICE NO MEIO: em x(60 − 2x), as raízes são 0 e 30, e o vértice está em 15 (o espelho do ep. 2).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: xV = −b/2a e "vértice no meio das raízes" (episódio 2); área do retângulo = base × altura; distributiva
#   (série de Expressões algébricas).
# Blocos b e d = exemplos 1 e 2 da seção 05 (60 m de tela → 450 m²; R$ 20,00 com 100 vendas, −4 por real → R$ 22,50,
#   90 vendas, R$ 2.025,00).
# Exemplos e acréscimos NOSSOS (marcados):
#   bloco f (vértice fora do problema): ônibus de 40 lugares, 30 passageiros a R$ 50,00, cada R$ 1,00 de desconto traz 2
#     passageiros → R = (50 − x)(30 + 2x), xV = 17,5 pediria 65 passageiros > 40 lugares → o ótimo fica na borda:
#     x = 5, preço R$ 45,00, ônibus cheio, receita R$ 1.800,00 (contra R$ 1.500,00 sem desconto).
#   atalho verde "raízes de cabeça, vértice no meio" também na receita: (20 + x)(100 − 4x) zera em −20 e 25 → meio 2,5.
#   erro 3 com 60 m (não 80 m), para não entregar a alternativa E da Q3 antes do "eu faço": A = x(60 − x) dá 30 × 30 =
#     900 m², mas a tela usada seria 30 + 30 + 30 = 90 m (só há 60).
#   erro 4 com o exemplo 2: sinal de xV trocado (−2,5) → preço R$ 17,50, 110 vendas, receita R$ 1.925,00 (menor).
#   conferência da Q3 pela tela gasta (20 + 20 + 40 = 80) e do "nós fazemos" (10 + 10 + 20 = 40).
# Nós fazemos (prompt): 40 m de tela e muro → A(x) = x(40 − 2x), raízes 0 e 20, x = 10, frente 20 m, área 200 m².
# QUESTÃO 3 ("eu faço", com pausa): gabarito C (800 m²). Erradas = material (A quadrado de 20 m cercando os 4 lados;
#   B 80 ÷ 3 ≈ 26,7 → ≈ 711; D lateral 20 e frente 80 − 20 = 60 → 1 200; E A = x(80 − x) → quadrado de 40 m → 1 600).
# QUESTÃO 2 ("você faz", com pausa): gabarito C (R$ 45,00). R = (60 − x)(300 + 10x) = −10x² + 300x + 18 000, xV = 15
#   (raízes 60 e −30, meio 15); 450 ingressos ≤ 500 lugares; receita R$ 20.250,00. Erradas = material (A responde o
#   desconto; B metade do preço, sem modelagem; D mantém o preço; E erra o sinal: aumento de 15).
# Frases-chave (meio e fim, idênticas): 1. Escolha o x, monte a função, ache o vértice, responda o pedido.
#   2. Com muro, o melhor retângulo não é o quadrado. 3. Confira se o vértice cabe no problema.
# Contas conferidas em trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Área máxima e receita máxima: otimização com a parábola | Função Quadrática Ep. 3"
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
        "{a}Com *sessenta metros de tela* [p=0.2] e um *muro* de um lado, [p=0.4] {b}o quadrado de vinte metros por "
        "vinte metros [p=0.2] usa toda a tela [p=0.2] e dá *quatrocentos metros quadrados.* [p=0.5] {c}Mas o retângulo "
        "de quinze metros por trinta metros [p=0.2] dá *quatrocentos e cinquenta.* [p=0.5] {d}O muro mudou a resposta, "
        "[p=0.2] e o ENEM *adora* isso."),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Função quadrática.* [p=0.4] {a}Ao final, [p=0.2] você vai montar a "
        "função da *área* ou da *receita* a partir do texto, [p=0.3] {b}achar o *máximo* [p=0.3] {c}e responder "
        "*exatamente* o que foi perguntado."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] o x do vértice é *menos b sobre dois a,* "
        "[p=0.2] e ele fica *no meio das raízes.* [p=0.4] {b}A área do retângulo é *base vezes altura.* [p=0.4] {c}E da "
        "série de Expressões algébricas, [p=0.2] a *distributiva:* [p=0.2] cada termo do primeiro parêntese multiplica "
        "cada termo do segundo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Duas cenas do dia a dia. [p=0.4] {a}Um rolo de tela [p=0.2] para cercar uma *horta* encostada num muro. "
        "[p=0.2] Lateral comprida demais? [p=0.2] Sobra pouca tela para a frente. [p=0.4] {b}Um vendedor de *picolé* "
        "[p=0.2] que sobe o preço. [p=0.2] Cada picolé rende mais, [p=0.2] só que ele vende menos. [p=0.4] {c}É um *cabo "
        "de guerra:* [p=0.2] duas grandezas que se multiplicam [p=0.2] e puxam para *lados opostos.* [p=0.4] {d}E todo "
        "cabo de guerra assim [p=0.2] tem um *topo:* [p=0.2] o ponto de equilíbrio perfeito."),

    # ================= BLOCO A: O ROTEIRO =================
    dict(id="05", block="roteiro", text=
        "{t}Como achar esse topo? [p=0.4] {a}*Otimizar* é procurar o melhor valor possível: [p=0.2] *maximizar* é achar o "
        "maior, [p=0.2] *minimizar* é achar o menor. [p=0.4] {b}E o roteiro tem *quatro passos.* [p=0.3] Um: [p=0.2] "
        "escolher o x, [p=0.2] a *variável de decisão,* [p=0.2] aquilo que você pode mudar. [p=0.4] {c}Dois: [p=0.2] "
        "escrever a grandeza em função dele. [p=0.3] Três: [p=0.2] achar o *vértice.* [p=0.4] {d}Quatro: [p=0.2] "
        "*responder o que foi pedido.* [p=0.3] Guarde esse quatro: [p=0.2] é nele que o ENEM derruba."),

    # ================= BLOCO B: EXEMPLO 1, ÁREA COM MURO =================
    dict(id="06", block="area", text=
        "{t}Sessenta metros de tela, [p=0.2] um lado no muro. [p=0.4] {a}Passo um: [p=0.2] chame de *x* cada uma das "
        "duas *laterais.* [p=0.4] {b}A frente usa o que sobra: [p=0.2] sessenta menos *duas* laterais, [p=0.2] *sessenta "
        "menos dois x.* [p=0.4] {c}Passo dois: [p=0.2] área é base vezes altura. [p=0.2] *A de x igual a x vezes, [p=0.2] "
        "sessenta menos dois x.* [p=0.4] {d}Pela distributiva: [p=0.2] *menos dois x ao quadrado [p=0.2] mais sessenta "
        "x.* [p=0.3] O a é negativo: [p=0.2] a parábola tem *topo.*"),
    dict(id="07", block="area", text=
        "{t}Veja o cercado mudando de forma. [p=0.4] {a}Lateral de *cinco:* [p=0.2] frente de cinquenta, [p=0.2] "
        "*duzentos e cinquenta* metros quadrados. [p=0.3] {b}Lateral de *dez:* [p=0.2] *quatrocentos.* [p=0.3] {c}Lateral "
        "de *quinze:* [p=0.2] frente de trinta, [p=0.2] *quatrocentos e cinquenta.* [p=0.3] {d}Lateral de *vinte:* "
        "[p=0.2] volta para quatrocentos. [p=0.2] Vinte e cinco: [p=0.2] duzentos e cinquenta. [p=0.4] {e}Sobe, [p=0.2] "
        "chega ao topo [p=0.2] e desce. [p=0.2] O cabo de guerra."),
    dict(id="08", block="area", text=
        "{t}Passo três: [p=0.2] o vértice. [p=0.4] {a}Pela fórmula: [p=0.2] menos b sobre dois a, [p=0.2] menos sessenta "
        "sobre menos quatro, [p=0.2] *quinze.* [p=0.4] {b}Agora o atalho: [p=0.2] *raízes de cabeça, [p=0.2] vértice no "
        "meio.* [p=0.3] {c}x vezes, [p=0.2] sessenta menos dois x, [p=0.2] zera quando x é *zero* [p=0.2] e quando x é "
        "*trinta.* [p=0.3] O meio entre zero e trinta: [p=0.2] *quinze.* [p=0.4] {d}Passo quatro: [p=0.2] A de quinze, "
        "[p=0.2] quinze vezes trinta, [p=0.2] *quatrocentos e cinquenta metros quadrados.*"),
    dict(id="09", block="quadrado", text=
        "{t}Mas espera: [p=0.2] o melhor retângulo não era o *quadrado?* [p=0.4] {a}*Sem* muro, [p=0.2] com o perímetro "
        "fixo, [p=0.2] é sim. [p=0.2] Só fica citado aqui. [p=0.4] {b}*Com* muro, não. [p=0.2] O muro faz um lado "
        "*de graça.* [p=0.3] Então vale esticar a frente, [p=0.2] que só gasta tela uma vez. [p=0.4] {c}No ótimo, [p=0.2] "
        "a frente, *trinta,* [p=0.2] é o *dobro* da lateral, *quinze.* [p=0.4] {d}O quadrado de vinte [p=0.2] fica "
        "cinquenta metros quadrados *atrás.*"),

    # ================= BLOCO D/E: EXEMPLO 2, RECEITA =================
    dict(id="10", block="receita", text=
        "{t}E o vendedor que sobe o preço? [p=0.4] {a}Um produto custa *vinte reais* [p=0.2] e vende *cem* por dia. "
        "[p=0.2] Cada real de *aumento* [p=0.2] faz perder *quatro vendas.* [p=0.4] {b}A *receita* é o dinheiro que "
        "entra: [p=0.2] *preço vezes quantidade vendida.* [p=0.4] {c}Passo um: [p=0.2] x é o *aumento,* em reais. "
        "[p=0.2] O preço vira *vinte mais x.* [p=0.2] As vendas viram *cem menos quatro x.* [p=0.4] {d}Passo dois: "
        "[p=0.2] *R de x igual a, [p=0.2] vinte mais x, [p=0.2] vezes, [p=0.2] cem menos quatro x.*"),
    dict(id="11", block="receita", text=
        "{t}Abrindo pela distributiva. [p=0.4] {a}Vinte vezes cem, [p=0.2] *dois mil.* [p=0.2] Vinte vezes menos quatro "
        "x, [p=0.2] *menos oitenta x.* [p=0.2] x vezes cem, [p=0.2] *cem x.* [p=0.2] x vezes menos quatro x, [p=0.2] "
        "*menos quatro x ao quadrado.* [p=0.4] {b}Juntando: [p=0.2] *menos quatro x ao quadrado, [p=0.2] mais vinte x, "
        "[p=0.2] mais dois mil.* [p=0.4] {c}Passo três: [p=0.2] menos vinte sobre menos oito, [p=0.2] *dois vírgula "
        "cinco.* [p=0.4] {d}Atalho conferindo: [p=0.2] o preço zera em x igual a menos vinte; [p=0.2] as vendas zeram em "
        "x igual a vinte e cinco. [p=0.2] O meio: [p=0.2] *dois e meio.* [p=0.2] Bateu."),
    dict(id="12", block="comando", text=
        "{t}E agora, [p=0.2] o passo que mais derruba: [p=0.2] *o que foi pedido?* [p=0.4] {a}Dois e cinquenta [p=0.2] "
        "é o *aumento.* [p=0.3] {b}O *preço ótimo,* [p=0.2] o preço que dá a maior receita, [p=0.2] é vinte mais dois e "
        "cinquenta: [p=0.2] *vinte e dois e cinquenta.* [p=0.3] {c}As vendas: [p=0.2] cem menos dez, [p=0.2] "
        "*noventa.* [p=0.3] {d}E a receita: [p=0.2] vinte e dois e cinquenta vezes noventa, [p=0.2] *dois mil e vinte "
        "e cinco reais.* [p=0.4] {e}Quatro números certos. [p=0.2] A prova pode pedir *qualquer um.* [p=0.2] Leia o "
        "comando [p=0.2] e circule só o dele."),

    # ================= BLOCO F: O VÉRTICE PRECISA CABER =================
    dict(id="13", block="borda", text=
        "{t}O vértice sempre vale? [p=0.4] {a}Um ônibus de *quarenta lugares* [p=0.2] leva trinta passageiros a "
        "*cinquenta reais.* [p=0.2] Cada real de *desconto* [p=0.2] traz *dois* passageiros a mais. [p=0.4] {b}A conta "
        "dá o vértice em *dezessete e meio* de desconto. [p=0.2] Só que isso pediria *sessenta e cinco* passageiros. "
        "[p=0.4] {c}O ônibus tem quarenta! [p=0.3] O *intervalo permitido* [p=0.2] são os valores de x que fazem sentido "
        "no problema. [p=0.2] Aqui, [p=0.2] desconto de zero até cinco reais. [p=0.4] {d}Fora dele, [p=0.2] o ótimo "
        "fica na *borda:* [p=0.2] cinco de desconto, [p=0.2] ônibus cheio, [p=0.2] *mil e oitocentos reais.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Agora com *quarenta metros* de tela [p=0.2] e um muro. [p=0.2] Laterais x. [p=0.4] "
        "{b}Qual é a *área máxima?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A frente é quarenta menos *dois* x. [p=0.2] *A de x igual a x vezes, [p=0.2] "
        "quarenta menos dois x.* [p=0.4] {b}Raízes de cabeça: [p=0.2] *zero* e *vinte.* [p=0.2] Vértice no meio: [p=0.2] "
        "*x igual a dez.* [p=0.4] {c}A frente: [p=0.2] quarenta menos vinte, [p=0.2] *vinte metros.* [p=0.2] Conferindo a "
        "tela: [p=0.2] dez, mais dez, mais vinte, [p=0.2] quarenta. [p=0.4] {d}Área: [p=0.2] dez vezes vinte, [p=0.2] "
        "*duzentos metros quadrados.* [p=0.2] E a frente, de novo, [p=0.2] é o dobro da lateral."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] escolha o x, [p=0.2] monte a função, [p=0.2] ache o "
        "vértice, [p=0.2] responda o pedido. [p=0.5] {b}Dois: [p=0.2] com muro, [p=0.2] o melhor retângulo não é o "
        "quadrado. [p=0.5] {c}Três: [p=0.2] confira se o vértice cabe no problema."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] supor que, com muro, [p=0.2] o ótimo é o "
        "*quadrado.* [p=0.4] {b}Parece certo, [p=0.2] porque você aprendeu que o quadrado é o retângulo mais "
        "eficiente. [p=0.4] {c}Mas isso vale *sem* muro. [p=0.2] Com sessenta metros e muro, [p=0.2] o quadrado dá "
        "quatrocentos; [p=0.2] o ótimo dá *quatrocentos e cinquenta.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] responder o *aumento* [p=0.2] quando pedem o *preço.* [p=0.2] Dois e cinquenta. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque é o número que acabou de sair da fórmula do vértice. [p=0.4] {c}Mas o x era o "
        "aumento. [p=0.2] O preço é vinte mais x: [p=0.2] *vinte e dois e cinquenta.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] esquecer a *segunda lateral.* [p=0.2] Escrever a frente como sessenta menos x, [p=0.2] e "
        "chegar a um quadrado de trinta, [p=0.2] *novecentos* metros quadrados. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a lateral que você desenhou é *uma.* [p=0.4] {c}Mas são duas. [p=0.2] Confira a tela: [p=0.2] trinta, mais "
        "trinta, mais trinta, [p=0.2] *noventa metros.* [p=0.2] Só havia sessenta."),
    dict(id="20", block="erros", text=
        "{a}Quarto: [p=0.2] errar o *sinal* do x do vértice. [p=0.2] Menos vinte sobre menos oito [p=0.2] vira *menos* "
        "dois e meio. [p=0.4] {b}Parece certo, [p=0.2] porque a fórmula começa com um sinal de menos. [p=0.4] {c}Mas "
        "menos com menos dá *mais.* [p=0.2] Com o sinal trocado, [p=0.2] o aumento vira *desconto:* [p=0.2] preço de "
        "dezessete e cinquenta, [p=0.2] receita de mil novecentos e vinte e cinco. [p=0.2] *Menor.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="21", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um sitiante tem "
        "*oitenta metros de tela* [p=0.2] para cercar uma horta retangular. [p=0.2] Um dos lados fica encostado num "
        "*muro* [p=0.2] e não recebe tela. [p=0.3] A maior área possível, em metros quadrados, é: [p=0.3] {qa}A: [p=0.2] "
        "quatrocentos. [p=0.2] {qb}B: [p=0.2] setecentos e onze. [p=0.2] {qc}C: [p=0.2] oitocentos. [p=0.2] {qd}D: "
        "[p=0.2] mil e duzentos. [p=0.2] {qe}E: [p=0.2] mil e seiscentos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q3", text=
        "{t}Roteiro. [p=0.3] {a}Laterais x. [p=0.2] Frente: [p=0.2] *oitenta menos dois x.* [p=0.2] Área: [p=0.2] x "
        "vezes, [p=0.2] oitenta menos dois x. [p=0.4] {b}Raízes de cabeça: [p=0.2] *zero* e *quarenta.* [p=0.2] Vértice "
        "no meio: [p=0.2] *vinte.* [p=0.4] {c}Área: [p=0.2] vinte vezes quarenta, [p=0.2] *oitocentos metros "
        "quadrados.* [p=0.3] Tela: [p=0.2] vinte, mais vinte, mais quarenta, [p=0.2] oitenta. [p=0.2] Cabe. [p=0.3] "
        "{ok}*Letra C!*"),
    dict(id="23", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A cerca os *quatro lados:* [p=0.2] quadrado de vinte, [p=0.2] e desperdiça o "
        "muro. [p=0.4] {xb}A B divide a tela em *três partes iguais,* [p=0.2] mas o ótimo não tem lados iguais. [p=0.4] "
        "{xd}A D usa frente oitenta menos vinte, [p=0.2] *esquecendo a segunda lateral.* [p=0.4] {xe}E a E escreve x "
        "vezes, oitenta menos x, [p=0.2] e chega ao quadrado de quarenta."),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="24", block="q2", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um teatro de *quinhentos lugares* [p=0.2] vende, em média, *trezentos* "
        "ingressos [p=0.2] a *sessenta reais.* [p=0.2] Para cada real de *desconto,* [p=0.2] vende *dez* ingressos a "
        "mais. [p=0.3] Para a receita ser a maior possível, [p=0.2] o *preço* do ingresso deve ser: [p=0.3] {qa}A: "
        "[p=0.2] quinze reais. [p=0.2] {qb}B: [p=0.2] trinta. [p=0.2] {qc}C: [p=0.2] quarenta e cinco. [p=0.2] {qd}D: "
        "[p=0.2] sessenta. [p=0.2] {qe}E: [p=0.2] setenta e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q2", text=
        "{t}Conferindo. [p=0.3] {a}x é o *desconto.* [p=0.2] Preço: [p=0.2] sessenta menos x. [p=0.2] Público: "
        "[p=0.2] trezentos mais dez x. [p=0.2] Receita: [p=0.2] *menos dez x ao quadrado, [p=0.2] mais trezentos x, "
        "[p=0.2] mais dezoito mil.* [p=0.4] {b}Vértice: [p=0.2] menos trezentos sobre menos vinte, [p=0.2] *quinze.* "
        "[p=0.2] Pelo atalho: [p=0.2] raízes sessenta e menos trinta, [p=0.2] meio quinze. [p=0.4] {c}Cabe? [p=0.2] "
        "Trezentos mais cento e cinquenta: [p=0.2] *quatrocentos e cinquenta* ingressos, [p=0.2] e há quinhentos "
        "lugares. [p=0.2] Cabe. [p=0.4] {d}Pediram o *preço:* [p=0.2] sessenta menos quinze, [p=0.2] *quarenta e cinco "
        "reais.* [p=0.2] Receita de vinte mil duzentos e cinquenta. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A responde o *desconto,* [p=0.2] não o preço. [p=0.4] {xb}A B é a *metade* "
        "do preço, [p=0.2] sem nenhuma conta. [p=0.4] {xd}A D *mantém* o preço, [p=0.2] ignorando que o desconto "
        "aumenta a receita. [p=0.4] {xe}E a E erra o *sinal:* [p=0.2] transforma o desconto de quinze [p=0.2] em aumento "
        "de quinze."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] escolha o x, [p=0.2] monte a função, [p=0.2] ache "
        "o vértice, [p=0.2] responda o pedido. [p=0.5] {b}Dois: [p=0.2] com muro, [p=0.2] o melhor retângulo não é o "
        "quadrado. [p=0.5] {c}Três: [p=0.2] confira se o vértice cabe no problema."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}O arco de uma ponte tem pés a *quarenta metros* um do outro [p=0.2] e *dez metros* de altura no meio. "
        "[p=0.3] Qual é a lei dessa parábola? [p=0.4] {b}E para que valores [p=0.2] o lucro de uma fábrica é "
        "*positivo?* [p=0.4] {c}Próximo episódio: [p=0.2] as *três formas* da função [p=0.2] e o *estudo do sinal.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] se você tivesse sessenta metros de tela, [p=0.2] o que cercaria? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você "
        "adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em "
        "poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
