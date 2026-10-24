# Roteiro — Determinantes e Sistemas Lineares, Episódio 3 de 5: o sistema como A · X = B e a regra de Cramer
# Base: Estudos/Enem/estudos/01-matematica/34-determinantes-sistemas-lineares.html — seções 06 e 07 + Questão 6
#   (seção 12) + a QUESTÃO NOVA do prompt (camisetas e bonés, texto exato). A Questão 1 do material NÃO é usada como
#   questão (repete a série de Sistemas): os números dela (250 ingressos, R$ 7 400) aparecem só como demonstração do
#   método, que é o exemplo da seção 07.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   D_x é TROCA DE FIGURINHA: a coluna de x sai e entra a coluna das respostas.
#   o D principal é o CHÃO de todas as frações: fica sempre embaixo.
#   Cramer é FERRAMENTA DE PRECISÃO: se a questão pede UMA incógnita, bastam dois determinantes.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Revisão rápida: montar sistema "quantidades e valores" (série de Sistemas), linha por coluna (série de Matrizes),
#   determinante 2 × 2 e Sarrus (episódio 1).
# Exemplo da seção 07 (só método): D = 20 − 40 = −20; D_x = 5 000 − 7 400 = −2 400 → x = 120; D_y = 7 400 − 10 000 =
#   −2 600 → y = 130; conferência 120 + 130 = 250 e 4 800 + 2 600 = 7 400.
# Nós fazemos (prompt): 2x + y = 7 e x − y = 2 → D = −3; D_x = −9 → x = 3; D_y = −3 → y = 1; 6 + 1 = 7 e 3 − 1 = 2.
# Erros clássicos com os números da seção 07 (já resolvidos), NOSSOS (marcados):
#   trocar a LINHA: |250 7 400 / 40 20| = 5 000 − 296 000 = −291 000 → "x" = 14 550 ingressos, mais que os 250;
#   x = D ÷ D_x = −20 ÷ (−2 400) ≈ 0,008 ingresso.
# QUESTÃO NOVA (eu faço, texto exato do prompt): x + y = 50 e 30x + 25y = 1 400; D = 25 − 30 = −5; D_y = 1 400 − 1 500
#   = −100; y = 20 (C). A 25 divide ao meio; B 30 = camisetas; D ≈ 47 = 1 400 ÷ 30 (todos camiseta); E 56 = 1 400 ÷ 25.
# QUESTÃO 6 (nós fazemos): x + y + z = 16, 2x + y = 15, x + 2z = 14 (zeros nas casas vazias); D por Sarrus: 2 − 5 = −3;
#   D_z (pausa): 29 − 44 = −15; z = 5 (C); conferência com suco 4 e sanduíche 7: 16, 15 e 14. Erradas = material
#   (A = módulo de D; E = módulo de D_z sem dividir; B = suco; D = sanduíche).
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "a coluna da incógnita é a posição dela na ordem x, y, z" e
#   o teste de plausibilidade (contagem inteira e menor que o total) nos erros clássicos.
# Contas conferidas em Python (trabalho/conferir_contas.py).
# Frases-chave (meio e fim, idênticas): 1. D_x: a coluna de x sai, entra a coluna das respostas.
#   2. x é D_x dividido por D: o D principal fica embaixo. 3. Pediu uma incógnita só? Calcule só D e o dela.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Regra de Cramer do zero: o sistema como A · X = B · Matemática ENEM, Determinantes episódio 3"

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
        "{a}Numa lanchonete com *suco,* *sanduíche* e *salada,* [p=0.3] {b}a questão pede *só o preço da salada.* "
        "[p=0.4] {c}Com *dois determinantes* você chega lá, [p=0.2] {d}sem descobrir os outros preços."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai escrever um sistema como *multiplicação de matrizes* [p=0.3] {b}e vai achar a "
        "incógnita pedida pela *regra de Cramer,* [p=0.2] sabendo *quando ela compensa.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Da série de Sistemas: [p=0.2] *quantidades* numa equação, "
        "[p=0.2] *valores* na outra. [p=0.4] {b}Da série de Matrizes: [p=0.2] multiplicar é *linha por coluna.* "
        "[p=0.4] {c}E do episódio um: [p=0.2] dois por dois é *principal menos secundária;* [p=0.2] três por três, "
        "[p=0.2] *Sarrus.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine a bilheteria de um teatro. [p=0.4] {a}Foram vendidos *duzentos e cinquenta* ingressos: [p=0.2] "
        "inteiras a *quarenta* reais [p=0.2] e meias a *vinte.* [p=0.2] O caixa fechou com *sete mil e quatrocentos.* "
        "[p=0.4] {b}É o mesmo tipo do problema dos ingressos da série de Sistemas, [p=0.2] *agora por outro caminho.* "
        "[p=0.4] {c}E na lanchonete, [p=0.2] com três itens, [p=0.2] são *três* incógnitas."),

    # ================= BLOCO A: FORMA MATRICIAL =================
    dict(id="05", block="forma", text=
        "{t}Dá para escrever um sistema como *uma multiplicação?* [p=0.4] {a}Inteiras são *x,* meias são *y.* [p=0.2] "
        "x mais y, [p=0.2] duzentos e cinquenta. [p=0.2] Quarenta x mais vinte y, [p=0.2] sete mil e quatrocentos. "
        "[p=0.4] {b}A *matriz dos coeficientes,* [p=0.2] *A,* [p=0.2] guarda os números que multiplicam as letras. "
        "[p=0.4] {c}A *coluna das incógnitas,* [p=0.2] *X,* [p=0.2] guarda as letras. [p=0.4] {d}E a *coluna dos "
        "termos independentes,* [p=0.2] *B,* [p=0.2] guarda as respostas."),
    dict(id="06", block="forma", text=
        "{t}Agora, a mágica. [p=0.4] {a}A vezes X [p=0.2] igual a B. [p=0.2] Essa é a *forma matricial.* [p=0.4] "
        "{b}Multiplique linha por coluna: [p=0.2] um vezes x, mais um vezes y. [p=0.2] *A primeira equação "
        "reaparece.* [p=0.2] {c}A segunda linha devolve a segunda. [p=0.4] {d}E com a coluna B "
        "*ao lado* de A, [p=0.2] você tem a *matriz completa,* [p=0.2] ou *ampliada,* [p=0.2] do sistema."),

    # ================= BLOCO B: SOLUÇÃO ÚNICA =================
    dict(id="07", block="unica", text=
        "{t}E por que escrever assim? [p=0.4] {a}Lembra do teste da chave? [p=0.2] Se o determinante de A é "
        "*diferente de zero,* [p=0.2] A tem inversa. [p=0.4] {b}E aí a solução é *única:* [p=0.2] X igual à inversa "
        "de A, [p=0.2] vezes B. [p=0.4] {c}A *regra de Cramer* [p=0.2] faz essa conta "
        "[p=0.2] *sem montar a inversa.*"),

    # ================= BLOCO C: A REGRA =================
    dict(id="08", block="regra", text=
        "{t}Como funciona? [p=0.4] {a}Primeiro, [p=0.2] o *D:* [p=0.2] o determinante da própria matriz A. [p=0.4] "
        "{b}Depois, o *D x.* [p=0.2] Pegue A [p=0.2] e faça uma *troca de figurinha:* [p=0.2] a *coluna de x sai,* "
        "[p=0.2] e *entra a coluna das respostas.* [p=0.4] {c}A regra: [p=0.2] *x é igual a D x dividido por D.* "
        "[p=0.4] {d}E repare onde o D ficou: [p=0.2] *embaixo.* [p=0.2] O D principal é o *chão* da fração."),
    dict(id="09", block="regra", text=
        "{t}E o y? [p=0.3] {a}No *D y,* [p=0.2] sai a *coluna de y.* [p=0.4] {b}y é D y dividido por D: [p=0.2] o "
        "mesmo chão. [p=0.4] {c}Com *z,* [p=0.2] o *D z* troca a terceira coluna. [p=0.2] O D principal [p=0.2] é *sempre o mesmo,* "
        "[p=0.2] e sempre embaixo."),
    dict(id="10", block="regra", text=
        "{t}Um atalho para nunca trocar a coluna errada. [p=0.4] {a}A coluna da incógnita [p=0.2] é a *posição dela* "
        "na ordem x, y, z: [p=0.2] primeira, [p=0.2] segunda, [p=0.2] terceira. [p=0.4] {b}Antes de calcular, "
        "[p=0.2] *pinte* a coluna que vai sair: [p=0.2] {c}ela sai inteira, [p=0.2] de cima a baixo."),

    # ================= BLOCO D: O EXEMPLO =================
    dict(id="11", block="exemplo", text=
        "{t}Vamos ao teatro. [p=0.4] {a}D é o determinante de *um, um, quarenta, vinte.* [p=0.4] {b}Principal: "
        "[p=0.2] um vezes vinte, [p=0.2] vinte. [p=0.2] Secundária: [p=0.2] um vezes quarenta, [p=0.2] quarenta. "
        "[p=0.4] {c}Vinte menos quarenta: [p=0.2] *menos vinte.* [p=0.2] Esse é o chão."),
    dict(id="12", block="exemplo", text=
        "{t}Agora o D x. [p=0.4] {a}A coluna de x, [p=0.2] *um e quarenta,* [p=0.2] sai. [p=0.2] Entram as "
        "*respostas.* [p=0.4] {b}Duzentos e cinquenta vezes vinte, "
        "[p=0.2] cinco mil. [p=0.2] Menos um vezes sete mil e quatrocentos. [p=0.2] *Menos dois mil e quatrocentos.* "
        "[p=0.4] {c}x é menos dois mil e quatrocentos, [p=0.2] dividido por menos vinte. [p=0.2] *Negativo dividido "
        "por negativo dá positivo:* [p=0.2] *cento e vinte* inteiras."),
    dict(id="13", block="exemplo", text=
        "{t}E as meias? [p=0.4] {a}No D y, [p=0.2] sai a coluna de y. [p=0.2] Um vezes sete mil e quatrocentos, "
        "[p=0.2] menos duzentos e cinquenta vezes quarenta: [p=0.2] *menos dois mil e seiscentos.* [p=0.4] {b}Dividido "
        "pelo mesmo chão, [p=0.2] menos vinte: [p=0.2] *cento e trinta* meias. [p=0.4] {c}Conferindo nas equações "
        "originais: [p=0.2] cento e vinte mais cento e trinta, [p=0.2] *duzentos e cinquenta.* [p=0.2] Quatro mil e "
        "oitocentos mais dois mil e seiscentos, [p=0.2] *sete mil e quatrocentos.*"),

    # ================= BLOCO E: QUANDO VALE A PENA =================
    dict(id="14", block="quando", text=
        "{t}Então Cramer é sempre o melhor caminho? [p=0.4] {a}Não. [p=0.2] Num três por três, [p=0.2] Cramer completo "
        "exige *quatro determinantes.* [p=0.4] {b}Mas Cramer é *ferramenta de precisão.* "
        "[p=0.2] Se a pergunta é *uma incógnita só,* [p=0.2] calcule o D e o determinante dela: [p=0.2] *dois "
        "Sarrus.* [p=0.4] {c}Se a questão pede *todas,* [p=0.2] substituição ou escalonamento [p=0.2] costumam ser "
        "mais rápidos."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}No sistema *dois x mais y igual a sete* [p=0.2] e *x menos y igual a dois,* [p=0.2] "
        "calcule o D, [p=0.2] o D x, [p=0.2] e o x. [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A é *dois, um, um, menos um.* [p=0.2] D: [p=0.2] dois vezes menos um, [p=0.2] "
        "menos dois, [p=0.2] menos um vezes um: [p=0.2] *menos três.* [p=0.4] {b}D x: [p=0.2] sai a coluna de x, "
        "[p=0.2] entram o sete e o dois. [p=0.2] Sete vezes menos um, [p=0.2] menos sete, [p=0.2] menos dois: "
        "[p=0.2] *menos nove.* [p=0.4] {c}x é menos nove dividido por menos três: [p=0.2] negativo dividido por "
        "negativo, [p=0.2] *três.* [p=0.4] {d}E o D y dá menos três: [p=0.2] *y é um.* "
        "[p=0.2] Seis mais um, sete; [p=0.2] três menos um, dois."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] D x: [p=0.2] a coluna de x sai, [p=0.2] entra a "
        "coluna das respostas. [p=0.5] {b}Dois: [p=0.2] x é D x dividido por D: [p=0.2] o D principal fica embaixo. "
        "[p=0.5] {c}Três: [p=0.2] pediu uma incógnita só? [p=0.2] Calcule só D e o dela."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] trocar a *linha* de x [p=0.2] em vez da "
        "*coluna.* [p=0.4] {b}Parece certo, [p=0.2] porque a gente lê a equação *na horizontal.* "
        "[p=0.4] {c}Mas no teatro isso dá *catorze mil, quinhentos e cinquenta* ingressos, [p=0.2] "
        "num total de duzentos e cinquenta. [p=0.2] O x mora numa *coluna:* [p=0.2] é ela que sai."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] escrever *x igual a D dividido por D x.* [p=0.4] {b}Parece certo, [p=0.2] porque o D "
        "principal [p=0.2] parece o mais importante. [p=0.4] {c}Mas assim o x "
        "vira *zero vírgula zero zero oito* ingresso. [p=0.2] O D principal é o *chão:* [p=0.2] fica *embaixo.*"),

    # ================= QUESTÃO NOVA (EU FAÇO) =================
    dict(id="20", block="qnova", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, *eu faço.* [p=0.4] {a}Uma loja vendeu, em um dia, "
        "[p=0.2] *cinquenta peças* [p=0.2] entre camisetas, a trinta reais cada, [p=0.2] e bonés, a vinte e cinco "
        "reais cada, [p=0.2] arrecadando *mil e quatrocentos reais.* [p=0.2] O número de *bonés* vendidos foi: "
        "[p=0.4] {qa}A: [p=0.2] vinte e cinco. [p=0.3] {qb}B: [p=0.2] trinta. [p=0.3] {qc}C: [p=0.2] vinte. [p=0.3] "
        "{qd}D: [p=0.2] cerca de quarenta e sete. [p=0.3] {qe}E: [p=0.2] cinquenta e seis."),
    dict(id="21", block="qnova", text=
        "{t}Nomeando: [p=0.2] *x* camisetas, [p=0.2] *y* bonés. [p=0.4] {a}x mais y, [p=0.2] cinquenta. [p=0.2] Trinta "
        "x mais vinte e cinco y, [p=0.2] mil e quatrocentos. [p=0.4] {b}Pediu só o y: [p=0.2] *D e D y.* [p=0.4] {c}D: [p=0.2] um vezes vinte e cinco, [p=0.2] menos um vezes trinta: "
        "[p=0.2] *menos cinco.* [p=0.4] {d}D y: [p=0.2] sai a coluna de y. [p=0.2] Um vezes mil e quatrocentos, "
        "[p=0.2] menos trinta vezes cinquenta: [p=0.2] *menos cem.* [p=0.4] {e}y é menos cem dividido por menos "
        "cinco: [p=0.2] negativo dividido por negativo, [p=0.2] *vinte.* [p=0.2] Conferindo: [p=0.2] novecentos das camisetas "
        "mais quinhentos dos bonés: [p=0.2] *mil e quatrocentos.* [p=0.3] {ok}*Letra C!*"),
    dict(id="22", block="qnova", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] dividiu as peças *ao meio.* [p=0.4] {xb}A B [p=0.2] é o número de "
        "*camisetas:* [p=0.2] a incógnita trocada. [p=0.4] {xd}A D [p=0.2] supõe que *todos* compraram camiseta: "
        "[p=0.2] mil e quatrocentos dividido por trinta. [p=0.4] {xe}E a E [p=0.2] supõe que todos compraram *boné:* "
        "[p=0.2] mil e quatrocentos dividido por vinte e cinco."),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="23", block="q6", text=
        "{t}Agora a lanchonete do começo, [p=0.2] do nosso material de estudo. [p=0.2] Esta, *nós fazemos.* [p=0.4] "
        "{a}Os preços do suco, do sanduíche e da salada são fixos. [p=0.2] *Um suco, um sanduíche e uma salada:* "
        "[p=0.2] dezesseis reais. [p=0.2] *Dois sucos e um sanduíche:* [p=0.2] quinze. [p=0.2] *Um suco e duas "
        "saladas:* [p=0.2] catorze. [p=0.2] O preço de *uma salada* é: [p=0.4] {qa}A: [p=0.2] três. [p=0.3] {qb}B: "
        "[p=0.2] quatro. [p=0.3] {qc}C: [p=0.2] cinco. [p=0.3] {qd}D: [p=0.2] sete. [p=0.3] {qe}E: [p=0.2] quinze."),
    dict(id="24", block="q6", text=
        "{t}Suco *x,* [p=0.2] sanduíche *y,* [p=0.2] salada *z.* [p=0.4] {a}x mais y mais z, [p=0.2] dezesseis. "
        "[p=0.2] Dois x mais y, [p=0.2] quinze. [p=0.2] x mais dois z, [p=0.2] catorze. [p=0.4] {b}Cuidado: [p=0.2] "
        "no segundo pedido *não tem salada,* [p=0.2] no terceiro *não tem sanduíche.* [p=0.2] Essas casas levam "
        "*zero.* [p=0.4] {c}D por Sarrus: [p=0.2] o time verde soma *dois.* [p=0.2] O "
        "vermelho soma *cinco.* [p=0.2] Dois menos cinco: [p=0.2] *menos três.*"),
    dict(id="25", block="q6", text=
        "{t}Agora é com você. [p=0.3] {a}A pergunta é só a salada, [p=0.2] o *z.* [p=0.2] Troque a terceira coluna "
        "pelas respostas, [p=0.2] *dezesseis, quinze, catorze,* [p=0.2] e calcule o *D z.* [p=0.4] {p}*Pause e "
        "calcule.* [p=2.0]"),
    dict(id="26", block="q6", text=
        "{t}Conferindo. [p=0.3] {a}Time verde: [p=0.2] catorze, [p=0.2] quinze [p=0.2] e zero: [p=0.2] *vinte e "
        "nove.* [p=0.4] {b}Time vermelho: [p=0.2] dezesseis, [p=0.2] zero [p=0.2] e vinte e oito: [p=0.2] *quarenta e "
        "quatro.* [p=0.2] Vinte e nove menos quarenta e quatro: [p=0.2] *menos quinze.* [p=0.4] {c}z é menos quinze "
        "dividido por menos três: [p=0.2] *cinco reais.* [p=0.4] {d}Com suco a quatro e sanduíche a sete, [p=0.2] os "
        "três pedidos dão dezesseis, quinze e catorze. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A [p=0.2] é o tamanho do *D,* [p=0.2] sem o sinal. [p=0.4] {xe}A E [p=0.2] é "
        "o D z *sem dividir* pelo chão. [p=0.4] {xb}E a B [p=0.2] e {xd}a D [p=0.2] são o *suco* e o *sanduíche:* "
        "[p=0.2] as outras incógnitas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] D x: [p=0.2] a coluna de x sai, [p=0.2] entra a "
        "coluna das respostas. [p=0.5] {b}Dois: [p=0.2] x é D x dividido por D: [p=0.2] o D principal fica embaixo. "
        "[p=0.5] {c}Três: [p=0.2] pediu uma incógnita só? [p=0.2] Calcule só D e o dela."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}E quando *D dá zero?* [p=0.3] A divisão por zero não existe. [p=0.4] {b}Isso quer dizer que o sistema *não "
        "tem solução?* [p=0.3] {c}Nem sempre: [p=0.2] às vezes ele tem *infinitas.* [p=0.3] {d}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha usado a regra de Cramer? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
