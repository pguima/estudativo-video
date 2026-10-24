# Roteiro — Divisão Proporcional, Episódio 4 de 5: o que parece divisão proporcional e não é, e as conferências que pegam o erro
# Base: Estudos/Enem/estudos/01-matematica/08-divisao-proporcional.html — seções 08 e 09 (+ Questão 7 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A parte fixa é como a BANDEIRADA do táxi (série de Grandezas Proporcionais): separe o fixo primeiro, divida só o resto,
#   devolva o fixo no fim.
#   Conferir a soma das partes é FECHAR O CAIXA: se não bate com o total, tem erro.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos dos blocos (NOSSOS, nenhum usa os números da Questão 7):
#   Gincana: R$ 6 000 para três equipes; cada uma ganha R$ 1 000 fixos e o restante (R$ 3 000) vai em 1 : 2 : 3 → k = 500 →
#   500 · 1 000 · 1 500 de proporção → com o fixo, 1 500 · 2 000 · 2 500 (soma 6 000).
#   Errado 1 (proporção sobre o total): 6 000 ÷ 6 = 1 000 → 1 000 · 2 000 · 3 000 (a soma fecha, mas o regulamento não foi seguido:
#   a equipe 1 perde R$ 500). Errado 2 (esqueceu de devolver o fixo): 500 + 1 000 + 1 500 = 3 000 ≠ 6 000 (o caixa não fecha).
#   Conferência 2 (ordem): direta → 1 500 < 2 000 < 2 500 ✓ (inversa: o bônus do episódio 2).
#   Conferência 3 (o que foi pedido): "quanto a equipe 3 recebeu a mais que a 1?" = 2 500 − 1 500 = 1 000.
#   Não arredonde o k: R$ 2 000 em 1, 2 e 4 → k = 2 000/7 = 285,714… → exato: 285,71 · 571,43 · 1 142,86 (soma 2 000,00);
#   com k arredondado para 286: 286 · 572 · 1 144 → soma 2 002 (o caixa não fecha).
#   Partes iguais = pesos 1, 1, 1 (R$ 900 entre 3 amigos → k = 300).
# Seção 09, sem regras legais nem tributárias (uma frase cada): imposto por faixas (cada faixa com a sua alíquota, sem k único) ·
#   rateio com valor mínimo (parcela fixa de todos) · herança com legítima ("por lei, uma parte é reservada aos herdeiros
#   necessários": só o restante segue outra regra) · desconto escalonado (o percentual muda com a quantidade).
# Nós fazemos (prompt): R$ 5 000 entre duas pessoas; R$ 500 fixos para cada e o resto em 1 : 3 → resto 4 000 → k = 1 000 →
#   1 500 e 3 500 (soma 5 000).
# QUESTÃO 7 do material (texto idêntico na tela): 10 000 − 3 000 = 7 000 → pesos 2, 3, 5 (soma 10) → k = 700 → terceira: 5 · 700 =
#   3 500 + 1 000 = 4 500 → C. Material: A (3 500) esqueceu de somar o fixo; D (5 000) aplicou a proporção sobre os 10 000.
#   Explicações NOSSAS: E (6 000) = proporção sobre o total E ainda somou o fixo (5 000 + 1 000); B (4 000) não sai de nenhuma
#   conta que siga o regulamento.
# Atalhos (verde): "separe, divida, devolva" · "feche o caixa: some as partes" · "sublinhe o que foi pedido antes de calcular" ·
#   "k quebrado? deixe como fração até o fim".
# Frases-chave (meio e fim, idênticas): 1. Parte fixa? Separe antes, devolva depois.
#   2. A soma das partes tem que fechar o caixa. 3. Releia o que foi pedido antes de marcar.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Divisão proporcional com parte fixa e as 3 conferências que pegam o erro · Matemática ENEM, episódio 4"

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
        "{a}Você calcula todas as partes *certinho* [p=0.3] {b}e erra a questão. [p=0.5] {c}Ou porque havia uma *parte fixa* "
        "escondida, [p=0.4] {d}ou porque respondeu a *parte errada.* [p=0.5] {e}Hoje você fecha essas *duas portas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai reconhecer as questões em que a proporção *não vale sobre o total* [p=0.4] "
        "{b}e ter *três conferências* que pegam quase qualquer erro."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] some os pesos, [p=0.2] divida o total, [p=0.2] "
        "e cada *pacotinho* vale k. [p=0.4] {b}Do episódio dois: [p=0.2] na divisão *inversa,* [p=0.2] o menor número leva a "
        "maior parte. [p=0.4] {c}E da série de Grandezas Proporcionais: [p=0.2] a *bandeirada* do táxi, [p=0.2] um valor "
        "*fixo* que não entra na proporção."),

    # ================= CONCRETO: A GINCANA =================
    dict(id="04", block="gincana", text=
        "{t}Imagine uma *gincana* com três equipes [p=0.2] e um prêmio de *seis mil reais.* [p=0.4] {a}O regulamento diz: "
        "[p=0.2] cada equipe ganha *mil reais* só por participar. [p=0.4] {b}E o *resto* é dividido conforme os pontos: "
        "[p=0.2] *um, dois e três.* [p=0.4] {c}A tentação é dividir os seis mil direto em um, dois e três. [p=0.3] {d}Mas "
        "repare: [p=0.2] a proporção *não vale sobre o total.* [p=0.2] Ela vale só sobre o *resto.*"),
    dict(id="05", block="gincana", text=
        "{t}Esses mil reais têm nome: [p=0.2] *parte fixa.* [p=0.3] {a}É um valor que todo mundo recebe igual, [p=0.2] "
        "*antes* de qualquer proporção. [p=0.4] {b}E o *restante* é o que sobra depois que você tira os fixos. [p=0.4] "
        "{c}Lembra da bandeirada? [p=0.2] Ela é cobrada *uma vez,* [p=0.2] e não dobra junto com os quilômetros. [p=0.3] "
        "{d}A parte fixa é igual: [p=0.2] *fica fora* da divisão."),

    # ================= BLOCO A: SEPARE, DIVIDA, DEVOLVA =================
    dict(id="06", block="fixa", text=
        "{t}O caminho tem três passos. [p=0.3] {a}Primeiro: [p=0.2] *separe* o fixo. [p=0.2] Três equipes, [p=0.2] mil cada: "
        "[p=0.2] *três mil.* [p=0.3] Seis mil menos três mil: [p=0.2] sobram *três mil.* [p=0.4] {b}Segundo: [p=0.2] *divida* "
        "o restante. [p=0.2] Pesos um, dois e três, [p=0.2] soma *seis.* [p=0.2] Três mil dividido por seis: [p=0.2] k igual a "
        "*quinhentos.* [p=0.4] {c}As partes da proporção: [p=0.2] *quinhentos, mil e mil e quinhentos.*"),
    dict(id="07", block="fixa", text=
        "{t}E o terceiro passo, [p=0.2] o que mais se esquece: [p=0.3] {a}*devolva* o fixo. [p=0.4] {b}Equipe um: [p=0.2] mil "
        "mais quinhentos, [p=0.2] *mil e quinhentos.* [p=0.3] Equipe dois: [p=0.2] *dois mil.* [p=0.3] Equipe três: [p=0.2] "
        "*dois mil e quinhentos.* [p=0.4] {c}Somando, [p=0.2] *seis mil.* [p=0.2] Fecha! [p=0.4] {d}Atalho: [p=0.2] *separe, "
        "divida, devolva.*"),
    dict(id="08", block="fixa", text=
        "{t}E se você dividisse os seis mil *direto?* [p=0.3] {a}Seis mil dividido por seis, [p=0.2] mil. [p=0.2] Partes: "
        "[p=0.2] *mil, dois mil e três mil.* [p=0.4] {b}A soma até fecha, [p=0.2] mas a equipe um levou *quinhentos a menos* "
        "do que o regulamento manda. [p=0.4] {c}E se você esquecesse de *devolver* o fixo? [p=0.3] Quinhentos, mil e mil e "
        "quinhentos [p=0.2] somam só *três mil.* [p=0.3] {d}Aí o caixa *não fecha.*"),

    # ================= BLOCO B: O QUE PARECE E NÃO É =================
    dict(id="09", block="parece", text=
        "{t}A parte fixa não é a única pegadinha. [p=0.3] {a}Existem situações com *cara* de divisão proporcional [p=0.2] que "
        "não são. [p=0.4] {b}O *imposto por faixas:* [p=0.2] cada faixa de renda tem a sua *alíquota,* [p=0.2] que é a "
        "porcentagem cobrada. [p=0.3] Não existe um k único. [p=0.4] {c}E o *rateio com valor mínimo:* [p=0.2] todo mundo paga "
        "uma parcela fixa [p=0.2] antes de qualquer proporção. [p=0.2] É a nossa parte fixa de novo."),
    dict(id="10", block="parece", text=
        "{a}Na *herança,* [p=0.2] por lei, [p=0.2] uma parte é reservada aos herdeiros necessários. [p=0.3] Essa parte se "
        "chama *legítima,* [p=0.2] e só o restante segue outra regra. [p=0.4] {b}E o *desconto escalonado:* [p=0.2] "
        "escalonado quer dizer *em degraus.* [p=0.2] O percentual muda conforme a quantidade comprada. [p=0.4] {c}Em todas, "
        "[p=0.2] a mesma lição: [p=0.2] *leia a regra antes de dividir.*"),
    dict(id="11", block="iguais", text=
        "{t}E dividir em partes *iguais?* [p=0.2] É outra regra? [p=0.3] {a}Não! [p=0.2] É a mesma, [p=0.2] com todos os pesos "
        "iguais: [p=0.2] *um, um e um.* [p=0.4] {b}Novecentos reais entre três amigos: [p=0.2] soma dos pesos, três. [p=0.2] "
        "k igual a *trezentos.* [p=0.2] Cada um leva um pacotinho."),

    # ================= AS TRÊS CONFERÊNCIAS =================
    dict(id="12", block="conf1", text=
        "{t}Agora, as *três conferências.* [p=0.3] Conferir é checar a resposta antes de marcar. [p=0.4] {a}A primeira é "
        "*fechar o caixa:* [p=0.2] como numa loja no fim do dia. [p=0.4] {b}Some as partes. [p=0.2] Deu o total? [p=0.2] O "
        "caixa fecha. [p=0.4] {c}Não deu? [p=0.2] Tem erro no k ou nos pesos, [p=0.2] e ainda dá tempo de refazer."),
    dict(id="13", block="conf2", text=
        "{t}Segunda conferência: [p=0.2] a *ordem* das partes faz sentido? [p=0.4] {a}Na divisão *direta,* [p=0.2] o maior "
        "peso leva mais. [p=0.2] Na gincana, [p=0.2] mil e quinhentos, [p=0.2] dois mil, [p=0.2] dois mil e quinhentos. "
        "[p=0.2] Certo! [p=0.4] {b}Na *inversa,* [p=0.2] o *menor número* leva mais. [p=0.3] {c}Se a ordem saiu ao "
        "contrário, [p=0.2] você trocou o método."),
    dict(id="14", block="conf3", text=
        "{t}Terceira: [p=0.2] *releia o que foi pedido.* [p=0.4] {a}Pediram a menor parte? [p=0.2] A do segundo? [p=0.2] A "
        "*diferença?* [p=0.4] {b}Se a pergunta for quanto a equipe três recebeu a mais que a equipe um, [p=0.2] a resposta é "
        "dois mil e quinhentos menos mil e quinhentos: [p=0.2] *mil.* [p=0.4] {c}Atalho: [p=0.2] *sublinhe o que foi pedido "
        "antes de calcular.*"),
    dict(id="15", block="arred", text=
        "{t}E um cuidado extra: [p=0.2] *não arredonde o k* no meio do caminho. [p=0.4] {a}Dois mil reais em um, dois e quatro: "
        "[p=0.2] soma sete. [p=0.2] Dois mil dividido por sete [p=0.2] dá *duzentos e oitenta e cinco vírgula sete, um, "
        "quatro...* [p=0.4] {b}Arredondou para duzentos e oitenta e seis? [p=0.2] As partes somam *dois mil e dois.* [p=0.2] O "
        "caixa não fecha. [p=0.4] {c}Atalho: [p=0.2] k quebrado? [p=0.2] Deixe como *fração* até o fim, [p=0.2] e só arredonde "
        "as partes."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Cinco mil reais* entre duas pessoas. [p=0.3] Cada uma recebe *quinhentos reais,* [p=0.2] e o "
        "resto é dividido na razão *um para três.* [p=0.4] {b}Quanto recebe cada uma? [p=0.3] {c}*Pause o vídeo e calcule.* "
        "[p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Separe o fixo: [p=0.2] quinhentos mais quinhentos, [p=0.2] mil. [p=0.2] Cinco mil menos "
        "mil, [p=0.2] *quatro mil.* [p=0.4] {b}Divida: [p=0.2] pesos um e três, [p=0.2] soma quatro. [p=0.2] k igual a *mil.* "
        "[p=0.4] {c}Devolva: [p=0.2] quinhentos mais mil, [p=0.2] *mil e quinhentos.* [p=0.3] Quinhentos mais três mil, [p=0.2] "
        "*três mil e quinhentos.* [p=0.4] {d}Somando, [p=0.2] *cinco mil.* [p=0.2] O caixa fecha!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] parte fixa? [p=0.2] Separe antes, [p=0.2] devolva depois. "
        "[p=0.5] {b}Dois: [p=0.2] a soma das partes tem que fechar o caixa. [p=0.5] {c}Três: [p=0.2] releia o que foi pedido "
        "antes de marcar."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] aplicar a proporção sobre o *total* [p=0.2] quando "
        "há parte fixa. [p=0.4] {b}Parece certo, [p=0.2] porque a soma até fecha. [p=0.4] {c}Mas o regulamento manda dividir "
        "só o *resto.* [p=0.3] Separe o fixo primeiro."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] esquecer de *devolver* a parte fixa no fim. [p=0.4] {b}Parece certo, [p=0.2] porque as contas da "
        "proporção estão perfeitas. [p=0.4] {c}Mas a soma dá só o restante. [p=0.3] O caixa denuncia: [p=0.2] some o fixo de "
        "volta."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *arredondar o k* no meio do caminho. [p=0.4] {b}Parece certo, [p=0.2] porque a diferença é de "
        "centavos. [p=0.4] {c}Mas os centavos se multiplicam, [p=0.2] e a soma não fecha. [p=0.3] Arredonde só no fim."),
    dict(id="22", block="erros", text=
        "{a}Quarto: [p=0.2] calcular tudo certo [p=0.2] e responder a *parte errada.* [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "número que você achou está lá, [p=0.2] nas alternativas. [p=0.4] {c}Mas ele é a resposta de *outra* pergunta. "
        "[p=0.3] Releia o que foi pedido."),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="23", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma quantia de *dez mil "
        "reais* será distribuída entre três pessoas da seguinte forma: [p=0.3] cada uma recebe inicialmente *mil reais,* "
        "[p=0.2] e o restante é dividido em partes diretamente proporcionais a *dois, três e cinco.* [p=0.4] {b}A *terceira "
        "pessoa* receberá, no total: [p=0.4] {qa}A: [p=0.2] três mil e quinhentos reais. [p=0.3] {qb}B: [p=0.2] quatro mil. "
        "[p=0.3] {qc}C: [p=0.2] quatro mil e quinhentos. [p=0.3] {qd}D: [p=0.2] cinco mil. [p=0.3] {qe}E: [p=0.2] seis mil. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q7", text=
        "{t}Vamos resolver. [p=0.3] {a}Separe o fixo: [p=0.2] três pessoas, [p=0.2] mil cada, [p=0.2] *três mil.* [p=0.2] Dez "
        "mil menos três mil: [p=0.2] *sete mil* para dividir. [p=0.4] {b}Pesos dois, três e cinco, [p=0.2] soma *dez.* [p=0.2] "
        "Sete mil dividido por dez: [p=0.2] k igual a *setecentos.* [p=0.4] {c}A terceira tem peso cinco: [p=0.2] cinco vezes "
        "setecentos, [p=0.2] *três mil e quinhentos.* [p=0.4] {d}Devolva o fixo: [p=0.2] mais mil, [p=0.2] *quatro mil e "
        "quinhentos.* [p=0.3] {ok}*Letra C!*"),
    dict(id="25", block="q7", text=
        "{t}Fechando o caixa: [p=0.2] {a}as partes são dois mil e quatrocentos, [p=0.2] três mil e cem [p=0.2] e quatro mil e "
        "quinhentos. [p=0.3] Somam *dez mil.* [p=0.2] Fecha! [p=0.4] {xa}A A é de quem *esqueceu de devolver* o fixo. [p=0.4] "
        "{xd}A D é de quem aplicou a proporção sobre os *dez mil* inteiros. [p=0.4] {xe}A E fez a proporção sobre o total "
        "[p=0.2] e ainda somou o fixo. [p=0.4] {xb}E a B não segue o regulamento por nenhum caminho."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] parte fixa? [p=0.2] Separe antes, [p=0.2] devolva "
        "depois. [p=0.5] {b}Dois: [p=0.2] a soma das partes tem que fechar o caixa. [p=0.5] {c}Três: [p=0.2] releia o que foi "
        "pedido antes de marcar."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e treinamos "
        "com *questões novas.*"),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha esquecido de devolver a parte fixa? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
