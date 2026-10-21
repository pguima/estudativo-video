# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 6 de 7: MMC ou MDC? A decisão em 10 segundos (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seções 09 e 10 + Questões 9 e 8 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: REPETE ou REPARTE? REPETE (ciclos que se reencontram no futuro) → MMC → resposta GRANDE.
#   REPARTE (algo cortado em pedaços iguais) → MDC → resposta PEQUENA. Retoma: MMC = o reencontro; MDC = a maior régua.
# Lidos EXATAMENTE como no material: tabela de decisão da seção 09 (cenas 06–08), a régua (09–10), a relação e o limite da
#   seção 10 (11–12), enunciados e alternativas das Questões 9 e 8.
# Treino rápido (cenas 14–19): 6 situações INÉDITAS, marcadas "situações elaboradas para fins didáticos"; ordem
#   REPETE, REPARTE, REPARTE, REPETE, REPARTE, REPETE. Só a decisão, sem contas.
# Limite com três números (cena 12): 4, 6 e 10 (os da Questão 5 do ep. 4): MDC 2 · MMC 60 = 120 ≠ 4 · 6 · 10 = 240.
# Questão 9: gabarito C (14). A = 7 = 84 ÷ 12 (esqueceu de dobrar); B = 12 = parou no MDC. O material diz que a D (16) é de
#   quem somou 1 estaca, mas 14 + 1 = 15: a aula diz que somar 1 daria 15 e não atribui a D nem a E a um erro.
# Questão 8: gabarito B (30). Cada alternativa errada falha na conferência: 24 e 60 dão MDC 12, 90 dá MDC 18, 42 dá MMC 252.
# Frases-chave (meio e fim, idênticas):
#   1. Repete: MMC, resposta grande. Reparte: MDC, resposta pequena.
#   2. MDC ≤ menor ≤ maior ≤ MMC.
#   3. MDC vezes MMC é igual a a vezes b, só para dois números.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "MMC ou MDC? A decisão em 10 segundos — Matemática ENEM, Divisibilidade episódio 6"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Nas contas, fale devagar e com clareza, como quem raciocina junto com o aluno. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "MMC": "M M C",
    "MDC": "M D C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quem erra esta questão no ENEM [p=0.2] quase nunca erra a *conta.* [p=0.4] {b}Erra a *escolha,* [p=0.3] {c}e "
        "resolve perfeitamente [p=0.2] o problema *errado.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai bater o olho no enunciado [p=0.2] e saber em *dez segundos* se é MMC ou MDC, "
        "[p=0.4] {b}e ainda vai ter uma *régua* para conferir a resposta."),

    # ================= DUAS CENAS DO COTIDIANO =================
    dict(id="03", block="cenas", text=
        "{t}Olha estas duas cenas. [p=0.3] {a}Dois amigos correm numa pista, [p=0.2] cada um no seu ritmo. [p=0.3] Eles largaram "
        "juntos. [p=0.2] Quando passam juntos pela largada *de novo?* [p=0.5] {b}Agora, um bolo. [p=0.3] Você quer cortar em "
        "fatias *iguais,* [p=0.2] sem sobrar nada. [p=0.5] {c}Na primeira, [p=0.2] uma coisa *se repete* e se reencontra. "
        "[p=0.3] {d}Na segunda, [p=0.2] uma coisa é *repartida.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="04", block="prereq", text=
        "{t}Lembrando, em quarenta e cinco segundos. [p=0.3] {a}MMC é o *reencontro:* [p=0.2] o primeiro número em que as "
        "tabuadas se encontram. [p=0.3] {b}Pela fatoração: [p=0.2] todos os fatores, com o maior expoente. [p=0.3] {c}De setenta "
        "e dois e cento e vinte, [p=0.2] o MMC é trezentos e sessenta. [p=0.5] {d}MDC é a *maior régua:* [p=0.2] a maior medida "
        "que cabe certinho em todos. [p=0.3] {e}Pela fatoração: [p=0.2] fatores comuns, com o menor expoente. [p=0.3] {f}De "
        "setenta e dois e cento e vinte, [p=0.2] o MDC é vinte e quatro."),

    # ================= A ÂNCORA =================
    dict(id="05", block="ancora", text=
        "{t}Então, [p=0.2] diante de qualquer enunciado, [p=0.2] faça uma pergunta só: [p=0.3] *repete ou reparte?* [p=0.5] "
        "{a}Repete: [p=0.2] coisas em ciclo, [p=0.2] que se reencontram no futuro. [p=0.3] {b}É MMC, [p=0.2] e a resposta é "
        "*grande.* [p=0.5] {c}Reparte: [p=0.2] algo cortado em pedaços iguais. [p=0.3] {d}É MDC, [p=0.2] e a resposta é "
        "*pequena.*"),

    # ================= BLOCO A: A TABELA DE DECISÃO =================
    dict(id="06", block="tabela", text=
        "{t}O material organiza essa decisão numa tabela. [p=0.3] Linha por linha. [p=0.4] {a}O que acontece no problema? "
        "[p=0.3] {a1}No MMC, [p=0.2] coisas se repetem em ciclos. [p=0.3] {a2}No MDC, [p=0.2] algo é repartido em pedaços. "
        "[p=0.5] {b}O que se procura? [p=0.3] {b1}No MMC, [p=0.2] quando voltam a coincidir. [p=0.3] {b2}No MDC, [p=0.2] que "
        "tamanho cada parte terá."),
    dict(id="07", block="tabela", text=
        "{c}As palavras-chave. [p=0.3] {c1}No MMC: [p=0.2] juntos, [p=0.2] ao mesmo tempo, [p=0.2] novamente. [p=0.4] {c2}No "
        "MDC: [p=0.2] iguais, [p=0.2] sem sobra, [p=0.2] o maior possível. [p=0.5] {d}E a resposta é... [p=0.3] {d1}no MMC, "
        "[p=0.2] maior que todos os dados. [p=0.3] {d2}No MDC, [p=0.2] menor ou igual ao menor dado."),
    dict(id="08", block="tabela", text=
        "{e}Por fim, os exemplos típicos. [p=0.3] {e1}MMC: [p=0.2] ônibus, [p=0.2] lâmpadas, [p=0.2] engrenagens, [p=0.2] "
        "remédios. [p=0.4] {e2}MDC: [p=0.2] tábuas, [p=0.2] grupos, [p=0.2] ladrilhos, [p=0.2] estacas."),

    # ================= BLOCO B: A RÉGUA DE CONFERÊNCIA =================
    dict(id="09", block="regua", text=
        "{t}E depois de calcular, [p=0.2] como saber se escolheu certo? [p=0.4] {a}Existe uma régua: [p=0.3] {b}o MDC, [p=0.2] "
        "{c}depois o menor dado, [p=0.2] {d}depois o maior dado, [p=0.2] {e}e o MMC lá na frente. [p=0.4] {f}Com setenta e dois "
        "e cento e vinte: [p=0.2] vinte e quatro, [p=0.2] setenta e dois, [p=0.2] cento e vinte, [p=0.2] trezentos e sessenta. "
        "[p=0.3] Tudo no lugar."),
    dict(id="10", block="regua", text=
        "{t}Agora imagine que alguém achou um MDC de *noventa.* [p=0.4] {a}Noventa é maior que setenta e dois: [p=0.2] "
        "*fora do lugar.* [p=0.4] {b}Ou um MMC de *sessenta,* [p=0.2] menor que cento e vinte: [p=0.2] também fora. [p=0.4] "
        "{c}Quase sempre, [p=0.2] o erro não é a conta: [p=0.2] é o método trocado. [p=0.3] {d}Se ele não couber onde deveria, "
        "[p=0.2] você escolheu o método errado, [p=0.2] e ainda dá tempo de trocar."),

    # ================= BLOCO C: A RELAÇÃO MDC × MMC =================
    dict(id="11", block="relacao", text=
        "{t}E tem mais uma ferramenta. [p=0.3] {a}Para *dois* números, [p=0.2] o MDC vezes o MMC [p=0.2] é igual a um número "
        "vezes o outro. [p=0.4] {b}Conferindo: [p=0.2] vinte e quatro vezes trezentos e sessenta [p=0.2] dá oito mil seiscentos "
        "e quarenta. [p=0.3] {c}E setenta e dois vezes cento e vinte? [p=0.2] Oito mil seiscentos e quarenta! [p=0.4] {d}Ela "
        "serve para dois usos: [p=0.2] conferir se você calculou os dois corretamente, [p=0.2] {e}e achar o que falta, [p=0.2] "
        "quando o enunciado dá três dos quatro valores."),

    # ================= BLOCO D: O LIMITE =================
    dict(id="12", block="limite", text=
        "{t}Mas cuidado com o limite. [p=0.3] {a}Ela vale apenas para dois números. [p=0.4] {b}Teste com quatro, seis e dez. "
        "[p=0.3] O MDC é dois. [p=0.2] O MMC é sessenta. [p=0.3] {c}Dois vezes sessenta: [p=0.2] cento e vinte. [p=0.3] "
        "{d}Quatro vezes seis vezes dez: [p=0.2] duzentos e quarenta. [p=0.4] {e}Não bate. [p=0.3] Com três, [p=0.2] a "
        "igualdade simplesmente quebra."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="13", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] repete: MMC, resposta grande. [p=0.2] Reparte: MDC, resposta "
        "pequena. [p=0.5] {b}Dois: [p=0.2] MDC, menor ou igual ao menor, [p=0.2] menor ou igual ao maior, [p=0.2] menor ou "
        "igual ao MMC. [p=0.5] {c}Três: [p=0.2] MDC vezes MMC é igual a a vezes b, [p=0.2] só para dois números."),

    # ================= TREINO RÁPIDO =================
    dict(id="14", block="treino", text=
        "{t}Agora, [p=0.2] treino rápido: [p=0.2] *repete ou reparte?* [p=0.3] Seis situações, [p=0.2] cinco segundos cada. "
        "[p=0.2] Sem conta, [p=0.2] só a decisão. [p=0.4] {q}Um: [p=0.2] dois faróis piscam a cada quinze e a cada vinte "
        "segundos. [p=0.2] Piscaram juntos agora. [p=0.2] Quando piscam juntos de novo? [p=0.3] {p}Decida! [p=5.0] "
        "{r}*Repete:* [p=0.2] MMC. [p=0.3] {w}Entregou: [p=0.2] juntos de novo."),
    dict(id="15", block="treino", text=
        "{q}Dois: [p=0.2] um piso de dois metros e quarenta por três metros e sessenta [p=0.2] vai ser coberto com ladrilhos "
        "quadrados, [p=0.2] os maiores possíveis, [p=0.2] sem cortar nenhum. [p=0.3] {p}Decida! [p=5.0] {r}*Reparte:* [p=0.2] "
        "MDC. [p=0.3] {w}Entregou: [p=0.2] os maiores possíveis."),
    dict(id="16", block="treino", text=
        "{q}Três: [p=0.2] uma professora tem quarenta e oito lápis e sessenta borrachas [p=0.2] e quer montar o maior número possível de kits "
        "[p=0.2] iguais, sem sobrar nada. [p=0.3] {p}Decida! [p=5.0] {r}*Reparte:* [p=0.2] MDC. [p=0.3] {w}Entregou: [p=0.2] o maior "
        "número de kits iguais, sem sobrar."),
    dict(id="17", block="treino", text=
        "{q}Quatro: [p=0.2] duas engrenagens; [p=0.2] uma completa a volta a cada oito segundos, [p=0.2] a outra a cada doze. "
        "[p=0.2] Quando as marcas voltam ao início ao mesmo tempo? [p=0.3] {p}Decida! [p=5.0] {r}*Repete:* [p=0.2] MMC. "
        "[p=0.3] {w}Entregou: [p=0.2] ao mesmo tempo."),
    dict(id="18", block="treino", text=
        "{q}Cinco: [p=0.2] um marceneiro quer cortar tábuas de noventa e de cento e cinquenta centímetros [p=0.2] em pedaços "
        "iguais, [p=0.2] do maior tamanho possível. [p=0.3] {p}Decida! [p=5.0] {r}*Reparte:* [p=0.2] MDC. [p=0.3] "
        "{w}Entregou: [p=0.2] pedaços iguais, [p=0.2] o maior possível."),
    dict(id="19", block="treino", text=
        "{q}Seis: [p=0.2] uma pessoa vai à academia a cada quatro dias, [p=0.2] e uma amiga, a cada seis. [p=0.2] Hoje as duas "
        "se encontraram lá. [p=0.2] Quando se encontram novamente? [p=0.3] {p}Decida! [p=5.0] {r}*Repete:* [p=0.2] MMC. "
        "[p=0.3] {w}Entregou: [p=0.2] novamente."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] escolher o método errado [p=0.2] e fazer a conta "
        "*certa.* [p=0.4] {b}Parece certo, [p=0.2] porque cada passo da conta confere. [p=0.4] {c}Mas antes da conta vem a "
        "pergunta: [p=0.2] repete ou reparte? [p=0.2] E depois, a régua."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] usar MDC vezes MMC igual a a vezes b vezes c, [p=0.2] com três números. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque com dois números funciona. [p=0.4] {c}Mas com três, [p=0.2] a igualdade quebra: [p=0.2] cento e vinte "
        "não é duzentos e quarenta."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] na questão de estacas, [p=0.2] esquecer de *dobrar* o perímetro. [p=0.3] Perímetro é a volta "
        "inteira da figura. [p=0.4] {b}Parece certo [p=0.2] somar vinte e quatro com sessenta: [p=0.2] oitenta e quatro metros. "
        "[p=0.4] {c}Mas o retângulo tem *quatro* lados: [p=0.2] dois de cada. [p=0.2] São cento e sessenta e oito metros."),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] na figura fechada, [p=0.2] *somar uma estaca* no final. [p=0.3] Figura fechada é a que termina "
        "onde começou. [p=0.4] {b}Parece certo, [p=0.2] porque numa linha reta [p=0.2] tem uma estaca a mais que espaços. "
        "[p=0.4] {c}Mas na figura fechada, [p=0.2] a última estaca coincide com a primeira: [p=0.2] estacas e espaços são "
        "*iguais.*"),

    # ================= QUESTÃO 9 =================
    dict(id="24", block="q9", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}Um terreno retangular mede vinte e quatro metros por sessenta metros "
        "[p=0.2] e será cercado com estacas igualmente espaçadas, [p=0.2] obrigatoriamente com uma estaca em cada um dos quatro "
        "cantos. [p=0.3] {b}Adotando a maior distância possível entre estacas consecutivas, [p=0.2] quantas estacas serão "
        "usadas? [p=0.4] {c}A: [p=0.2] sete. [p=0.3] {d}B: [p=0.2] doze. [p=0.3] {e}C: [p=0.2] quatorze. [p=0.3] {f}D: "
        "[p=0.2] dezesseis. [p=0.3] {g}E: [p=0.2] vinte e oito. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="25", block="q9", text=
        "{t}Primeiro, a decisão, em voz alta. [p=0.3] {a}Repete ou reparte? [p=0.3] Os lados vão ser repartidos em partes "
        "iguais, [p=0.2] a maior possível, [p=0.2] com encaixe exato nos cantos. [p=0.3] {b}*Reparte:* [p=0.2] MDC. [p=0.4] "
        "{c}Vinte e quatro é dois ao cubo vezes três. [p=0.3] {d}Sessenta é dois ao quadrado vezes três vezes cinco. [p=0.4] "
        "{e}Fatores comuns, menor expoente: [p=0.2] dois ao quadrado vezes três: [p=0.2] *doze metros* entre estacas. [p=0.3] "
        "{f}Régua: [p=0.2] doze é menor que vinte e quatro. [p=0.2] Passou."),
    dict(id="26", block="q9", text=
        "{t}Agora o perímetro, [p=0.2] e é aqui que a questão derruba. [p=0.4] {a}Duas vezes vinte e quatro mais sessenta: "
        "[p=0.2] duas vezes oitenta e quatro, [p=0.2] *cento e sessenta e oito metros.* [p=0.4] {b}Cento e sessenta e oito "
        "dividido por doze: [p=0.2] *quatorze estacas.* [p=0.4] {c}Repare no desenho: [p=0.2] numa figura fechada, [p=0.2] o "
        "número de estacas é igual ao número de espaços. [p=0.3] A última coincide com a primeira. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q9", text=
        "{xa}E as armadilhas? [p=0.3] Sete é de quem esqueceu de dobrar: [p=0.2] oitenta e quatro dividido por doze. [p=0.4] "
        "{xb}Doze é de quem parou no MDC: [p=0.2] respondeu a distância, [p=0.2] e não as estacas. [p=0.4] {xd}E quem soma uma "
        "estaca no final [p=0.2] chega a quinze, [p=0.2] que nem está nas alternativas. [p=0.3] Dezesseis e vinte e oito não "
        "saem da conta certa."),

    # ================= QUESTÃO 8 =================
    dict(id="28", block="q8", text=
        "{t}Próxima. [p=0.3] {a}O máximo divisor comum de dois números naturais é seis [p=0.2] e o mínimo múltiplo comum deles "
        "é cento e oitenta. [p=0.3] {b}Sabendo que um dos números é trinta e seis, [p=0.2] qual é o outro? [p=0.4] {c}A: "
        "[p=0.2] vinte e quatro. [p=0.3] {d}B: [p=0.2] trinta. [p=0.3] {e}C: [p=0.2] quarenta e dois. [p=0.3] {f}D: [p=0.2] "
        "sessenta. [p=0.3] {g}E: [p=0.2] noventa. [p=0.4] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="29", block="q8", text=
        "{t}São dois números: [p=0.2] vale a relação. [p=0.3] {a}MDC vezes MMC [p=0.2] é igual a um número vezes o outro. "
        "[p=0.4] {b}Seis vezes cento e oitenta [p=0.2] é igual a trinta e seis vezes o número que falta. [p=0.4] {c}Mil e "
        "oitenta igual a trinta e seis vezes b. [p=0.3] {d}Mil e oitenta dividido por trinta e seis: [p=0.2] *trinta.*"),
    dict(id="30", block="q8", text=
        "{t}Conferindo pela fatoração. [p=0.3] {a}Trinta e seis é dois ao quadrado vezes três ao quadrado. [p=0.3] {b}Trinta "
        "é dois vezes três vezes cinco. [p=0.4] {c}MDC: [p=0.2] comuns, menor expoente: [p=0.2] dois vezes três, [p=0.2] seis. "
        "[p=0.3] Confere! [p=0.4] {d}MMC: [p=0.2] todos, maior expoente: [p=0.2] quatro vezes nove vezes cinco, [p=0.2] cento e "
        "oitenta. [p=0.3] Confere! [p=0.3] {ok}*Letra B!*"),
    dict(id="31", block="q8", text=
        "{x}E as outras? [p=0.3] Todas falham na conferência. [p=0.4] {xa}Com vinte e quatro, [p=0.2] o MDC daria doze. "
        "[p=0.3] {xc}Com quarenta e dois, [p=0.2] o MMC daria duzentos e cinquenta e dois. [p=0.3] {xd}Com sessenta, [p=0.2] o "
        "MDC daria doze. [p=0.3] {xe}E com noventa, [p=0.2] o MDC daria dezoito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] repete: MMC, resposta grande. [p=0.2] Reparte: MDC, "
        "resposta pequena. [p=0.5] {b}Dois: [p=0.2] MDC, menor ou igual ao menor, [p=0.2] menor ou igual ao maior, [p=0.2] "
        "menor ou igual ao MMC. [p=0.5] {c}Três: [p=0.2] MDC vezes MMC é igual a a vezes b, [p=0.2] só para dois números."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.3] {c}caçamos as *pegadinhas* [p=0.3] {d}e "
        "treinamos com *questões novas.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das seis você acertou no repete ou reparte? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
