# Roteiro — Logaritmos, Episódio 4 de 5: equações logarítmicas e a condição de existência
# Base: Estudos/Enem/estudos/01-matematica/27-logaritmos-propriedades-equacoes.html — seção 08, o hábito 3 da seção 09
#   ("desconfie da alternativa com duas raízes") + Questão 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O SEGURANÇA NA PORTA DO LOG: a condição de existência só deixa entrar número positivo.
#   O DOCUMENTO: toda raiz mostra documento — substitua nos logaritmandos ORIGINAIS antes de aceitar.
#   JUNTAR PEÇAS: junte os logs como quem junta peças, até sobrar um só de cada lado.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: definição e condições (ep. 1), log M + log N = log(M · N) (ep. 2), x² + 3x − 10 = 0 (série de
#   Equação do 2º grau, pela soma e produto). As condições de existência ficam num quadro no canto da tela desde o começo
#   de cada resolução e são usadas no fim.
# Blocos = tabela da seção 08 (log₃(x − 1) = 2 → 10; log₂(3x − 1) = log₂(x + 5) → 3; log x + log(x + 3) = 1 → {2}).
# Nós fazemos (prompt): log₂(x + 3) = 4 → x + 3 = 16 → x = 13 (confere: 16 > 0).
# Erros (prompt): aceitar x = −5 em log x + log(x + 3) = 1; somar os logaritmandos. Exemplo NOSSO no erro 2 (marcado),
#   para não adiantar a alternativa D da Questão 3: no tipo 3, somar dá log(2x + 3) = 1 → x = 3,5, e a conferência
#   log 3,5 + log 6,5 = log 22,75 ≠ 1 desmente.
# Acréscimos NOSSOS (marcados): duas cenas verdes de ATALHO — "a base pula para o outro lado e leva o número como
#   expoente" (cena 09) e "o teste do documento: só os logaritmandos, um por um, em segundos" (cena 13, com o hábito 3 da
#   seção 09: desconfie da alternativa com duas raízes). Definições de raiz, raiz estranha, conjunto solução e conjunto
#   vazio em uma frase cada.
# QUESTÃO 3 ("você faz", com pausa): gabarito B ({4}). Condições x > 0 e x > 2. x² − 2x = 8 → 4 ou −2; só 4 vale.
#   Conferência log₂ 4 + log₂ 2 = 2 + 1 = 3. Erradas = material/prompt (C {−2, 4} esquece de verificar; A {−2} fica com
#   a raiz proibida; D {5} soma os logaritmandos, log₂(2x − 2) = 3; E ∅ descarta também a raiz válida).
# Frases-chave (meio e fim, idênticas): 1. Escreva as condições de existência antes de começar.
#   2. Junte os logs até sobrar um só de cada lado. 3. Toda raiz precisa passar no teste do logaritmando positivo.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação logarítmica: a raiz proibida que derruba no ENEM | Logaritmos Ep. 4"
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
        "{a}Numa equação logarítmica [p=0.2] que vira equação do *segundo grau,* [p=0.4] {b}a alternativa com as *duas "
        "raízes* [p=0.2] *sempre* está lá. [p=0.5] {c}E quase sempre [p=0.2] *está errada.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Logaritmos.* [p=0.4] {a}Ao final, [p=0.2] você vai resolver equações "
        "logarítmicas em *quatro passos* [p=0.4] {b}e nunca mais aceitar uma *raiz proibida.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] o *logaritmando,* [p=0.2] o número de dentro do "
        "log, [p=0.2] tem que ser *positivo.* [p=0.4] {b}Do episódio dois: [p=0.2] *log de M mais log de N* [p=0.2] é o "
        "log de *M vezes N.* [p=0.4] {c}E da série de Equação do segundo grau: [p=0.2] *x ao quadrado mais três x menos "
        "dez igual a zero.* [p=0.2] Soma menos três, [p=0.2] produto menos dez: [p=0.2] *dois* e *menos cinco.* [p=0.3] "
        "São as *raízes:* [p=0.2] os valores de x que deixam a equação verdadeira."),

    # ================= CONCRETO =================
    dict(id="04", block="porta", text=
        "{t}Imagine uma porta com um *segurança.* [p=0.4] {a}Na placa está escrito: [p=0.2] *log de x.* [p=0.2] E o "
        "segurança só deixa entrar *número positivo.* [p=0.4] {b}Chega o *três.* [p=0.2] Documento em dia: [p=0.2] "
        "*pode entrar.* [p=0.4] {c}Chega o *menos dois.* [p=0.3] *Barrado.* [p=0.2] Log de menos dois não existe. "
        "[p=0.4] {d}Esse segurança é a *condição de existência:* [p=0.2] a regra de quem pode ficar dentro do log."),
    dict(id="05", block="definicoes", text=
        "{t}E onde ele trabalha? [p=0.4] {a}Numa *equação logarítmica:* [p=0.2] uma equação em que o x aparece *dentro "
        "de um log.* [p=0.4] {b}A raiz que aparece na conta [p=0.2] mas *não passa* pelo segurança [p=0.2] é a *raiz "
        "estranha.* [p=0.4] {c}As que sobram formam o *conjunto "
        "solução:* [p=0.2] a lista das respostas que valem. [p=0.4] {d}E se ninguém passar, [p=0.2] o conjunto é "
        "*vazio:* [p=0.2] nenhuma resposta."),

    # ================= BLOCO A: O ROTEIRO =================
    dict(id="06", block="roteiro", text=
        "{t}Existe um caminho que funciona sempre? [p=0.4] Existe, [p=0.2] em *quatro passos.* [p=0.4] {a}Um: [p=0.2] "
        "escreva as *condições de existência.* [p=0.4] {b}Dois: [p=0.2] *junte os logs* com as propriedades. [p=0.4] "
        "{c}Três: [p=0.2] *elimine o log,* [p=0.2] pela definição [p=0.2] ou igualando o que está dentro. [p=0.4] "
        "{d}Quatro: [p=0.2] resolva [p=0.2] e *descarte* o que o segurança barrar."),

    # ================= BLOCO B: PELA DEFINIÇÃO =================
    dict(id="07", block="tipo1", text=
        "{t}Primeiro tipo: [p=0.2] o log é igual a um *número.* [p=0.4] {a}Log de x menos um, [p=0.2] na base três, "
        "[p=0.2] igual a dois. [p=0.4] {b}Passo um: [p=0.2] x menos um tem que ser *positivo,* [p=0.2] então x maior "
        "que um. [p=0.3] Fica anotado no canto. [p=0.4] {c}Pela definição: [p=0.2] três elevado a dois dá x menos um. "
        "[p=0.2] *Nove* igual a x menos um. [p=0.4] {d}Então x igual a *dez.* [p=0.3] {e}Dez é maior que um? [p=0.2] "
        "*É.* [p=0.2] Entra."),

    # ================= BLOCO C: MESMA BASE =================
    dict(id="08", block="tipo2", text=
        "{t}Segundo tipo: [p=0.2] *log dos dois lados,* [p=0.2] na mesma base. [p=0.4] {a}Log de três x menos um "
        "[p=0.2] igual a log de x mais cinco, [p=0.2] os dois na base dois. [p=0.4] {b}Condições: [p=0.2] *os dois* "
        "de dentro positivos. [p=0.4] {c}Se os logs são iguais e a base é a mesma, [p=0.2] o que está dentro também é "
        "igual. [p=0.2] *Três x menos um igual a x mais cinco.* [p=0.4] {d}Dois x igual a seis: [p=0.2] *x igual a "
        "três.* [p=0.4] {e}Documento: [p=0.2] *oito* e *oito,* [p=0.2] positivos. [p=0.2] Entra."),
    dict(id="09", block="atalho_base", text=
        "{t}Atalho para o primeiro tipo. [p=0.4] {a}Log de alguma coisa na base b igual a c? [p=0.4] {b}A *base pula* "
        "para o outro lado [p=0.2] e leva o número *como expoente.* [p=0.4] {c}Log de algo na base três igual a dois "
        "[p=0.2] vira *algo igual a três ao quadrado.*"),

    # ================= BLOCO D: JUNTANDO =================
    dict(id="10", block="tipo3", text=
        "{t}Terceiro tipo: [p=0.2] *vários logs* de um lado. [p=0.4] {a}Log de x mais log de x mais três [p=0.2] igual "
        "a um. [p=0.2] Sem base escrita: [p=0.2] *base dez.* [p=0.4] {b}Condições: [p=0.2] x positivo [p=0.2] e x mais "
        "três positivo. [p=0.4] {c}Agora, [p=0.2] *junte as peças:* [p=0.2] soma de logs vira o log do *produto.* "
        "[p=0.2] Log de x vezes x mais três, [p=0.2] igual a um. [p=0.4] {d}Pela definição: [p=0.2] x vezes x mais três "
        "[p=0.2] igual a *dez elevado a um,* [p=0.2] dez. [p=0.4] {e}Fica x ao quadrado mais três x menos dez igual a "
        "zero. [p=0.2] Raízes: [p=0.2] *dois* e *menos cinco.*"),
    dict(id="11", block="tipo3b", text=
        "{t}Hora do *documento.* [p=0.4] {a}O *dois:* [p=0.2] log de dois e log de cinco. [p=0.2] Dois e cinco são "
        "positivos. [p=0.2] *Entra.* [p=0.4] {b}O *menos cinco:* [p=0.2] log de menos cinco. [p=0.3] *Não existe.* "
        "[p=0.2] Barrado: [p=0.2] é uma raiz estranha. [p=0.4] {c}Conjunto solução: [p=0.2] *só o dois.* [p=0.4] "
        "{d}Conferindo: [p=0.2] log de dois mais log de cinco [p=0.2] é log de dez: [p=0.2] *um.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva: [p=0.2] *log de x mais três, na base dois, igual a quatro.* [p=0.4] {b}Comece "
        "pela condição. [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Condição: [p=0.2] x mais três positivo, [p=0.2] então *x maior que menos três.* "
        "[p=0.4] {b}A base pula: [p=0.2] x mais três [p=0.2] igual a *dois elevado a quatro,* [p=0.2] dezesseis. "
        "[p=0.4] {c}x igual a *treze.* [p=0.4] {d}Documento: [p=0.2] treze mais três dá dezesseis, [p=0.2] positivo. "
        "[p=0.2] *Entra.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] escreva as condições de existência [p=0.2] antes de "
        "começar. [p=0.5] {b}Dois: [p=0.2] junte os logs [p=0.2] até sobrar um só de cada lado. [p=0.5] {c}Três: "
        "[p=0.2] toda raiz precisa passar [p=0.2] no teste do logaritmando positivo."),

    # ================= ATALHO: O TESTE DO DOCUMENTO =================
    dict(id="15", block="atalho_doc", text=
        "{t}Atalho para a prova. [p=0.4] {a}Viu uma alternativa com *duas raízes?* [p=0.2] *Desconfie.* [p=0.4] {b}Teste "
        "cada raiz [p=0.2] só nos *logaritmandos originais,* [p=0.2] um por um. [p=0.4] {c}Positivo entra; [p=0.2] zero ou negativo é barrado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="16", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] aceitar o *menos cinco* [p=0.2] em log de x "
        "mais log de x mais três igual a um. [p=0.4] {b}Parece certo, [p=0.2] porque menos cinco é raiz de verdade da "
        "equação do segundo grau. [p=0.4] {c}Mas a pergunta tem *log,* [p=0.2] e log de menos cinco *não existe.*"),
    dict(id="17", block="erros", text=
        "{a}Segundo: [p=0.2] *somar* os de dentro [p=0.2] em vez de *multiplicar.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque do lado de fora está escrito *mais.* [p=0.4] {c}No mesmo exemplo, [p=0.2] somando dá log de dois x mais "
        "três igual a um, [p=0.2] e x igual a *três e meio.* [p=0.2] Que *não confere.* [p=0.2] Soma de logs vira "
        "log do *produto.*"),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="18", block="q3", text=
        "{t}E esta [p=0.2] *você faz.* [p=0.4] {a}O conjunto solução, nos reais, [p=0.2] da equação *log de x na base "
        "dois [p=0.2] mais log de x menos dois na base dois [p=0.2] igual a três* [p=0.2] é: [p=0.3] {qa}A: [p=0.2] só o "
        "menos dois. [p=0.2] {qb}B: [p=0.2] só o quatro. [p=0.2] {qc}C: [p=0.2] menos dois e quatro. [p=0.2] {qd}D: "
        "[p=0.2] só o cinco. [p=0.2] {qe}E: [p=0.2] o conjunto vazio. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="19", block="q3", text=
        "{t}Condições: [p=0.2] *x maior que zero* [p=0.2] e *x maior que dois.* [p=0.2] Juntas: [p=0.2] x maior que "
        "dois. [p=0.4] {a}Junte as peças: [p=0.2] log de x vezes x menos dois, [p=0.2] igual a três. [p=0.4] {b}A base "
        "pula: [p=0.2] x ao quadrado menos dois x [p=0.2] igual a *dois ao cubo,* [p=0.2] oito. [p=0.4] {c}Raízes: "
        "[p=0.2] *quatro* e *menos dois.* [p=0.4] {d}Documento: [p=0.2] o quatro dá log de quatro e log de dois, "
        "[p=0.2] positivos. [p=0.2] *Entra.* [p=0.3] {e}O menos dois dá log de menos dois. [p=0.2] *Barrado.* [p=0.4] "
        "{f}Conferindo: [p=0.2] *dois mais um, três.* [p=0.3] {ok}*Letra B!*"),
    dict(id="20", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C pega as duas raízes [p=0.2] e *esquece de verificar.* [p=0.4] {xa}A A "
        "fica justamente com a *raiz proibida.* [p=0.4] {xd}A D *soma* os de dentro: [p=0.2] log de dois x menos dois "
        "igual a três [p=0.2] dá x igual a cinco. [p=0.4] {xe}E a E descarta *também* a raiz que valia."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="21", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] escreva as condições de existência [p=0.2] antes "
        "de começar. [p=0.5] {b}Dois: [p=0.2] junte os logs [p=0.2] até sobrar um só de cada lado. [p=0.5] {c}Três: "
        "[p=0.2] toda raiz precisa passar [p=0.2] no teste do logaritmando positivo."),

    # ================= PONTE E CTA =================
    dict(id="22", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.2] *caçamos as pegadinhas* [p=0.4] {b}e "
        "treinamos com *tempos de crescimento,* [p=0.2] *decaimento* [p=0.4] {c}e contas com *log de dois* e *log de "
        "três.*"),
    dict(id="23", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha marcado a alternativa com as duas raízes? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
