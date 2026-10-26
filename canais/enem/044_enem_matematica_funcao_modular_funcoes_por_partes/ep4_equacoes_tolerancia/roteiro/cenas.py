# Roteiro — Função Modular e Funções por Partes, Episódio 4 de 5: equações e inequações modulares — dois casos, "entre"
#   e "fora", e a tolerância
# Base: Estudos/Enem/estudos/01-matematica/29-funcao-modular-funcoes-por-partes.html — seções 06 e 07 + Questões 4, 2 e 9.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A DISTÂNCIA (a mesma do ep. 3): módulo é distância até o zero; se a distância é 7, você está no 7 ou no −7.
#   ENTRE × FORA: menor que fica ENTRE; maior que fica FORA.
#   O ELÁSTICO: tolerância é um elástico preso no centro, que estica k para cada lado.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: |2x − 5| = 7 → 6 e −1 (bloco b; é a Q4, "eu faço": repetição permitida) · |x − 1| = |x − 7|
#   → 4 · |x − 2| = 2x − 1 → descarta −1, fica 1 · nós fazemos |3x − 6| = 9 → 5 e −1 · tabela da seção 07.
# Exemplo NOSSO (marcado): a regra do elástico (bloco e) usa a PEÇA DE 50 mm ± 2 mm (48 a 52), e não o café: o café
#   (492 a 508) é a Q2, que tem pausa. O café aparece no concreto só como "tolerância de 8 g", sem conta; a animação do
#   alfinete no 500 fica na resolução da Q2.
# Atalhos (NOSSOS, verde): "dois casos, depois substitua os dois na equação original" · "lado direito com letra: ele
#   precisa ser zero ou positivo" · "tolerância: centro menos o raio, centro mais o raio; ≤ inclui as pontas".
# QUESTÃO 4 (eu faço): {−1, 6} (C). Erradas (material): A esquece o caso negativo · B troca os sinais das duas soluções
#   · D erra o 2º caso (2x = 7 − 5 em vez de 2x = −7 + 5) · E confunde com |A| = −7.
# QUESTÃO 2 (nós fazemos, com pausa): 492 ≤ m ≤ 508 (D). Erradas (material): A só o limite de cima (aprovaria 300 g) ·
#   B exclui as pontas · C divide a tolerância por 2 · E é |m − 500| ≥ 8.
# QUESTÃO 9 (você faz, com pausa): t = 2 h e t = 4 h (E). Erradas (material): A e B ficam com um caso só · C inclui
#   t = 3 h, quando a distância é zero · D erra a conta do caso negativo (chega a 4t = 4 em vez de 4t = 8) — a forma de
#   dizer o erro da D é nossa; o material diz "esquecendo de somar 12".
# Frases-chave (meio e fim, idênticas): 1. Módulo igual a k: o de dentro vale k ou −k. 2. Menor que fica entre; maior
#   que fica fora. 3. Tolerância: centro mais ou menos o raio.
# CTA: |x − 3| ≤ 5 → de −2 a 8. Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação e inequação modular do zero: dois casos, entre e fora, e a tolerância | Função Modular Ep. 4"
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
        "{a}Um ciclista está a *quatro quilômetros* de um posto de apoio. [p=0.4] {b}Ele já passou pelo posto [p=0.2] "
        "ou ainda vai chegar? [p=0.4] {c}As duas coisas podem ser verdade, [p=0.2] em horários diferentes, [p=0.4] "
        "{d}e o ENEM coloca nas alternativas *quem esqueceu uma delas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resolver equações e inequações com módulo *desenhando a reta,* "
        "[p=0.3] {b}e traduzir qualquer *tolerância* em intervalo."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio três: [p=0.2] *módulo é distância até o zero.* [p=0.2] "
        "Módulo de menos sete é sete. [p=0.4] {b}E da série de Equações: [p=0.2] em dois x menos cinco igual a sete, "
        "[p=0.2] você soma cinco dos dois lados [p=0.2] e divide por dois. [p=0.2] *x igual a seis.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense numa fábrica de café. [p=0.3] {a}O pacote tem *quinhentos gramas,* [p=0.2] e ela aceita *tolerância "
        "de oito gramas.* [p=0.4] {b}Ou numa peça de *cinquenta milímetros* [p=0.2] que pode variar *dois "
        "milímetros.* [p=0.4] {c}Nos dois casos, [p=0.2] a pergunta é a mesma: [p=0.2] *a que distância do certo* "
        "você pode estar? [p=0.4] {d}E distância, você já sabe, [p=0.2] se escreve com *duas barrinhas.*"),

    # ================= BLOCO A: A REGRA =================
    dict(id="05", block="termos", text=
        "{t}Primeiro, as palavras. [p=0.4] {a}*Equação modular* é uma igualdade com o x dentro das barrinhas. "
        "[p=0.2] Por exemplo, módulo de x igual a sete. [p=0.4] {b}O *conjunto solução* é a lista de todos os x que "
        "funcionam. [p=0.4] {c}E quais funcionam? [p=0.2] Se a distância até o zero é sete, [p=0.2] você está no "
        "*sete* [p=0.2] ou no *menos sete.*"),
    dict(id="06", block="regra", text=
        "{t}Isso vira a regra. [p=0.4] {a}Módulo de A igual a k, [p=0.2] com k positivo: [p=0.2] *A vale k, ou A vale "
        "menos k.* [p=0.2] O primeiro é o *caso positivo;* [p=0.2] o segundo, o *caso negativo.* [p=0.4] {b}Se k é "
        "*zero,* [p=0.2] só A igual a zero. [p=0.4] {c}E se k é *negativo?* [p=0.2] Não há solução. [p=0.2] "
        "Distância *nunca* é negativa."),

    # ================= BLOCO B: |2x − 5| = 7 =================
    dict(id="07", block="exemplo", text=
        "{t}Vamos resolver módulo de *dois x menos cinco* igual a sete. [p=0.4] {a}Caso positivo: [p=0.2] dois x menos "
        "cinco igual a sete. [p=0.2] Dois x igual a doze, [p=0.2] *x igual a seis.* [p=0.4] {b}Caso negativo: [p=0.2] "
        "dois x menos cinco igual a *menos sete.* [p=0.2] Dois x igual a menos dois, [p=0.2] *x igual a menos um.* "
        "[p=0.4] {c}Conferindo: [p=0.2] doze menos cinco, sete. [p=0.2] Menos dois menos cinco, menos sete, [p=0.2] "
        "e o módulo dá sete. [p=0.4] {d}Atalho: [p=0.2] *dois casos, e substitua os dois* na equação original."),

    # ================= BLOCO C: MÓDULO IGUAL A MÓDULO =================
    dict(id="08", block="dois_mod", text=
        "{t}E quando os *dois lados* têm barrinhas? [p=0.4] {a}Módulo de x menos um igual a módulo de x menos sete. "
        "[p=0.4] {b}Leia como distância: [p=0.2] x está *à mesma distância* do um e do sete. [p=0.4] {c}Só um ponto "
        "faz isso: [p=0.2] o *ponto médio.* [p=0.2] *x igual a quatro.* [p=0.2] Três para cada lado."),

    # ================= BLOCO D: LADO DIREITO COM LETRA =================
    dict(id="09", block="letra", text=
        "{t}E se o lado direito tem *letra?* [p=0.4] {a}Módulo de x menos dois igual a *dois x menos um.* [p=0.4] "
        "{b}Caso positivo: [p=0.2] x menos dois igual a dois x menos um. [p=0.2] Dá *x igual a menos um.* [p=0.4] "
        "{c}Mas aí o lado direito vira dois vezes menos um, menos um: [p=0.2] *menos três.* [p=0.2] Um módulo igual a "
        "um número negativo? [p=0.2] Impossível. [p=0.2] *Descarte.*"),
    dict(id="10", block="letra", text=
        "{t}O outro caso. [p=0.3] {a}x menos dois igual a *menos* dois x mais um. [p=0.2] Três x igual a três, [p=0.2] "
        "*x igual a um.* [p=0.4] {b}Confere: [p=0.2] módulo de menos um é um, [p=0.2] e dois menos um também é um. "
        "[p=0.4] {c}Atalho: [p=0.2] o lado direito com letra precisa dar *zero ou positivo.* [p=0.2] *Toda resposta "
        "se confere substituindo.*"),

    # ================= BLOCO E: INEQUAÇÕES =================
    dict(id="11", block="inequacao", text=
        "{t}E quando aparece *menor* ou *maior* no lugar do igual? [p=0.4] {a}Isso é uma *inequação modular.* [p=0.4] "
        "{b}Módulo de x *menor que* quatro: [p=0.2] a distância até o zero é menor que quatro. [p=0.2] O x mora "
        "*entre* menos quatro e quatro. [p=0.4] {c}Com o menor ou igual, [p=0.2] as pontas entram. [p=0.2] Isso é um "
        "*intervalo fechado:* [p=0.2] as bolinhas ficam *cheias.*"),
    dict(id="12", block="inequacao", text=
        "{t}E o *maior que?* [p=0.4] {a}Módulo de x maior que quatro: [p=0.2] a distância passa de quatro. [p=0.4] "
        "{b}O x está *fora:* [p=0.2] antes do menos quatro, [p=0.2] ou depois do quatro. [p=0.2] Duas semirretas, "
        "[p=0.2] e o meio *apagado.* [p=0.4] {c}Guarde assim: [p=0.2] *menor que fica entre; [p=0.2] maior que fica "
        "fora.*"),
    dict(id="13", block="elastico", text=
        "{t}E a *tolerância?* [p=0.4] {a}*Tolerância* é quanto se pode errar para cada lado. [p=0.2] O valor certo é "
        "o *centro;* [p=0.2] a tolerância é o *raio.* [p=0.4] {b}Pense num *elástico preso no centro:* [p=0.2] ele "
        "estica o raio para cada lado. [p=0.4] {c}A peça de cinquenta milímetros, com dois de tolerância: [p=0.2] "
        "módulo de x menos cinquenta, menor ou igual a dois. [p=0.4] {d}De *quarenta e oito* a *cinquenta e dois "
        "milímetros.*"),

    # ================= BLOCO F: TRADUÇÃO DIRETA =================
    dict(id="14", block="traducao", text=
        "{t}Como o ENEM escreve isso em palavras? [p=0.4] {a}*Difere de a em no máximo k:* [p=0.2] módulo de x menos a, "
        "menor ou igual a k. [p=0.2] Fica *entre.* [p=0.4] {b}*Difere em mais de k:* [p=0.2] módulo de x menos a, maior "
        "que k. [p=0.2] Fica *fora.* [p=0.4] {c}Atalho: [p=0.2] *centro menos o raio, centro mais o raio.* [p=0.2] E "
        "com o menor ou igual, [p=0.2] *as pontas entram.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva *módulo de três x menos seis igual a nove.* [p=0.4] {b}Os dois casos, [p=0.2] "
        "e a conferência. [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Caso positivo: [p=0.2] três x menos seis igual a nove. [p=0.2] Três x igual a "
        "quinze, [p=0.2] *x igual a cinco.* [p=0.4] {b}Caso negativo: [p=0.2] três x menos seis igual a menos nove. "
        "[p=0.2] Três x igual a menos três, [p=0.2] *x igual a menos um.* [p=0.4] {c}Conferindo: [p=0.2] quinze menos "
        "seis, nove. [p=0.2] Menos três menos seis, menos nove, [p=0.2] módulo nove. [p=0.4] {d}Solução: [p=0.2] "
        "*menos um e cinco.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] módulo igual a k: [p=0.2] o de dentro vale k ou menos "
        "k. [p=0.5] {b}Dois: [p=0.2] menor que fica entre; [p=0.2] maior que fica fora. [p=0.5] {c}Três: [p=0.2] "
        "tolerância: [p=0.2] centro mais ou menos o raio."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] módulo de x igual a cinco, [p=0.2] e responder *só "
        "o cinco.* [p=0.4] {b}Parece certo: [p=0.2] cinco é o número que está na conta. [p=0.4] {c}Mas o menos cinco "
        "também está a cinco do zero. [p=0.2] São *dois* valores."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] módulo de x igual a *menos três,* [p=0.2] e responder *mais ou menos três.* [p=0.4] "
        "{b}Parece certo: [p=0.2] é a regra de sempre, [p=0.2] o de dentro vale k ou menos k. [p=0.4] {c}Mas a regra "
        "pede k *positivo.* [p=0.2] Distância nunca é negativa: [p=0.2] *não há solução.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] módulo de x menor que quatro, [p=0.2] e escrever *x menor que mais ou menos quatro.* "
        "[p=0.4] {b}Parece certo: [p=0.2] é a mesma ideia dos dois casos da equação. [p=0.4] {c}Mas menor que fica "
        "*entre:* [p=0.2] o certo é *menos quatro menor que x, menor que quatro.*"),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="21", block="q4", text=
        "{t}Agora uma questão do nosso material de estudo, [p=0.2] e eu faço com você. [p=0.4] {a}Num jogo de "
        "tabuleiro, [p=0.2] a casa de um peão é um número inteiro x, [p=0.2] e uma regra exige que *módulo de dois x "
        "menos cinco seja igual a sete.* [p=0.2] Quais valores de x cumprem a regra? [p=0.4] {qa}A: [p=0.2] só o "
        "seis. [p=0.3] {qb}B: [p=0.2] menos seis e um. [p=0.3] {qc}C: [p=0.2] menos um e seis. [p=0.3] {qd}D: "
        "[p=0.2] um e seis. [p=0.3] {qe}E: [p=0.2] nenhum valor."),
    dict(id="22", block="q4", text=
        "{t}Você já viu essa conta. [p=0.3] {a}Caso positivo: [p=0.2] *x igual a seis.* [p=0.2] Caso negativo: "
        "[p=0.2] *x igual a menos um.* [p=0.4] {b}Os dois são inteiros, [p=0.2] e os dois conferem: [p=0.2] *sete e "
        "sete.* [p=0.3] {ok}*Letra C!*"),
    dict(id="23", block="q4", text=
        "{t}E as pegadinhas? [p=0.3] {xa}A A *esquece o caso negativo.* [p=0.4] {xb}A B troca os sinais das duas "
        "soluções. [p=0.4] {xd}A D erra o segundo caso: [p=0.2] faz dois x igual a sete menos cinco, [p=0.2] em vez "
        "de menos sete mais cinco. [p=0.4] {xe}E a E confunde com módulo igual a menos sete. [p=0.2] Aqui o sete é "
        "*positivo.*"),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="24", block="q2", text=
        "{t}Agora a gente faz junto. [p=0.4] {a}Uma máquina embala café com massa de *quinhentos gramas.* [p=0.2] O "
        "controle aprova o pacote de massa m [p=0.2] quando *módulo de m menos quinhentos é menor ou igual a oito.* "
        "[p=0.2] Os aprovados são: [p=0.4] {qa}A: [p=0.2] m até quinhentos e oito. [p=0.3] {qb}B: [p=0.2] m entre "
        "quatrocentos e noventa e dois e quinhentos e oito, sem as pontas. [p=0.3] {qc}C: [p=0.2] de quatrocentos e "
        "noventa e seis a quinhentos e quatro. [p=0.3] {qd}D: [p=0.2] de quatrocentos e noventa e dois a quinhentos e "
        "oito, com as pontas. [p=0.3] {qe}E: [p=0.2] até quatrocentos e noventa e dois, ou a partir de quinhentos e "
        "oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q2", text=
        "{t}Vamos juntos. [p=0.3] {a}O alfinete vai no centro: [p=0.2] *quinhentos.* [p=0.2] O raio é *oito.* [p=0.4] "
        "{b}O elástico estica oito para cada lado: [p=0.2] de *quatrocentos e noventa e dois* [p=0.2] a *quinhentos e "
        "oito.* [p=0.4] {c}E o sinal é menor ou igual: [p=0.2] *as pontas entram.* [p=0.3] {ok}*Letra D!*"),
    dict(id="26", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A só usa o limite de cima: [p=0.2] aprovaria um pacote de *trezentos gramas.* "
        "[p=0.4] {xb}A B tira as pontas, [p=0.2] mas um pacote de quinhentos e oito é aprovado. [p=0.4] {xc}A C "
        "divide a tolerância por dois, [p=0.2] como se oito fosse a largura toda. [p=0.4] {xe}E a E responde o "
        "contrário: [p=0.2] os pacotes de *fora.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="27", block="q9", text=
        "{t}Agora é com você. [p=0.4] {a}Um ciclista parte do *quilômetro zero* de uma ciclovia reta [p=0.2] e pedala "
        "a *quatro quilômetros por hora.* [p=0.2] O posto de apoio fica no *quilômetro doze.* [p=0.2] A distância "
        "até o posto, depois de t horas, [p=0.2] é *módulo de quatro t menos doze,* [p=0.2] para t de zero a seis. "
        "[p=0.2] Quando essa distância vale *quatro quilômetros?* [p=0.4] {qa}A: [p=0.2] só em duas horas. [p=0.3] "
        "{qb}B: [p=0.2] só em quatro horas. [p=0.3] {qc}C: [p=0.2] em duas e em três horas. [p=0.3] {qd}D: [p=0.2] em "
        "uma e em quatro horas. [p=0.3] {qe}E: [p=0.2] em duas e em quatro horas. [p=0.4] {p}*Pause o vídeo e "
        "resolva sozinho.* [p=2.5]"),
    dict(id="28", block="q9", text=
        "{t}Vamos conferir. [p=0.3] {a}Caso positivo: [p=0.2] quatro t menos doze igual a quatro. [p=0.2] Quatro t "
        "igual a dezesseis, [p=0.2] *t igual a quatro.* [p=0.2] Ele está no quilômetro dezesseis: [p=0.2] *já passou* "
        "do posto. [p=0.4] {b}Caso negativo: [p=0.2] quatro t menos doze igual a menos quatro. [p=0.2] Quatro t igual "
        "a oito, [p=0.2] *t igual a dois.* [p=0.2] Quilômetro oito: [p=0.2] *ainda vai chegar.* [p=0.4] {c}As duas "
        "horas estão entre zero e seis. [p=0.3] {ok}*Letra E!*"),
    dict(id="29", block="q9", text=
        "{t}E as erradas? [p=0.3] {xa}A A e a B ficam com *um caso só:* [p=0.2] o ciclista está a quatro do posto uma "
        "vez antes e outra depois. [p=0.4] {xc}A C inclui as *três horas.* [p=0.2] Mas é a hora em que ele *está no "
        "posto:* [p=0.2] distância zero. [p=0.4] {xd}E a D erra a conta do caso negativo: [p=0.2] chega a quatro t "
        "igual a quatro, [p=0.2] em vez de quatro t igual a oito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] módulo igual a k: [p=0.2] o de dentro vale k "
        "ou menos k. [p=0.5] {b}Dois: [p=0.2] menor que fica entre; [p=0.2] maior que fica fora. [p=0.5] {c}Três: "
        "[p=0.2] tolerância: [p=0.2] centro mais ou menos o raio."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *tarifas,* *faixas progressivas* e *módulo,* [p=0.3] "
        "{b}caçamos as pegadinhas [p=0.2] e treinamos para o ENEM."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] módulo de x menos três, menor ou igual a cinco: [p=0.2] de onde "
        "até onde vai o x? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir "
        "os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
