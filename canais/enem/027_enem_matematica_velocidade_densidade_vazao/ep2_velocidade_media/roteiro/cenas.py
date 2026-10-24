# Roteiro — Velocidade, Densidade e Vazão, Episódio 2 de 6: velocidade média, distância total dividida por tempo total
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seção 03 + Questão 1 (seção 12)
#   + a questão do atleta (Questão 2 do material 06, Razão), transcrita no prompt e lida IGUAL.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Velocidade média é o RITMO CONSTANTE IMAGINÁRIO: se a viagem inteira tivesse ritmo igual, qual seria?
#   O CRONÔMETRO NÃO PARA NO POSTO: tempo parado também é tempo.
#   O RELÓGIO conta de 60 em 60, não de 10 em 10: 2,5 h é 2 h 30 min, e 30 min é 0,5 h, não 0,30 h.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: o trem (180 km em 2 h 30 min) é a Questão 1, resolvida como "eu faço" (pode repetir).
#   Exemplo NOSSO da parada: ônibus a 90 km/h por 1 h, 30 min no posto, mais 1 h a 90 km/h → 180 km em 2,5 h = 72 km/h
#   (o mesmo 72 do trem: a parada derruba a média de 90 para 72).
#   Exemplo NOSSO do fator 3,6: 54 km/h ÷ 3,6 = 15 m/s (não usa os números do atleta nem os da série de Unidades).
# Nós fazemos (prompt): 270 km em 3 h + 30 min de parada → 3,5 h → 270 ÷ 3,5 ≈ 77 km/h (contra 90 de quem esquece a parada).
# QUESTÃO 1 (texto idêntico na tela): 2 h 30 min = 2,5 h; 180 ÷ 2,5 = 72 km/h → C.
#   O material diz que a B (66) é de quem usou 2,3 h. ERRADO: 180 ÷ 2,3 ≈ 78,3 (não está nas alternativas). O vídeo diz (prompt):
#   E (90) = usou só as 2 h; A (60) = usou 3 h; B (66) e D (75) = valores vizinhos, sem erro comum; e avisa que 2,3 h dá ≈ 78.
# QUESTÃO DO ATLETA (texto do prompt, idêntico): 100 m ÷ 12,5 s = 8 m/s; × 3,6 = 28,8 km/h → C.
#   A (8) parou em m/s · B (12,5) repete o tempo · D (36 = 10 m/s) arredondou para 100 m em 10 s · E (80) multiplicou por 10.
#   Plausibilidade: velocista ≈ 29 km/h; corrida comum ≈ 12 km/h; 8 km/h seria uma caminhada rápida.
# Atalhos (verde): minutos ÷ 60 com as frações do relógio (15 = 0,25 · 30 = 0,5 · 45 = 0,75 · 6 min = 0,1 h) ·
#   dividir por 2,5 = dobrar os dois e dividir por 5 · m/s é sempre o número MENOR.
# Frases-chave (meio e fim, idênticas): 1. Velocidade média é distância total sobre tempo total.
#   2. Tempo parado também é tempo. 3. Trinta minutos são 0,5 hora, não 0,30.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Velocidade média do zero: o erro do relógio que o ENEM cobra · Matemática ENEM, Velocidade episódio 2"

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
        "{a}Um trem faz *cento e oitenta quilômetros* [p=0.2] em *duas horas e trinta minutos.* [p=0.4] {b}Quem divide "
        "cento e oitenta por *dois vírgula trinta* [p=0.2] *erra.* [p=0.4] {c}Quem divide por *dois vírgula cinco* "
        "[p=0.2] acerta: [p=0.2] *setenta e dois quilômetros por hora.* [p=0.4] {d}A diferença está no *relógio,* "
        "[p=0.2] não na conta."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular a *velocidade média* de qualquer viagem, [p=0.2] com parada "
        "ou sem parada, [p=0.3] {b}e passar de *quilômetros por hora* para *metros por segundo* [p=0.2] sem inverter."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] uma *taxa* é quanto de uma coisa [p=0.2] "
        "por unidade de outra. [p=0.2] Quilômetros *por hora.* [p=0.4] {b}Da série de Unidades: [p=0.2] minutos viram "
        "hora *dividindo por sessenta.* [p=0.4] {c}E o *três vírgula seis:* [p=0.2] de quilômetros por hora para metros "
        "por segundo, [p=0.2] *divide;* [p=0.2] no sentido contrário, [p=0.2] *multiplica.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine uma viagem de ônibus. [p=0.3] {a}Na estrada, [p=0.2] o velocímetro marca *noventa quilômetros por "
        "hora.* [p=0.4] {b}No meio do caminho, [p=0.2] uma *parada no posto:* [p=0.2] trinta minutos. [p=0.4] {c}Depois, "
        "[p=0.2] noventa de novo. [p=0.4] {d}E o aplicativo de mapas, [p=0.2] antes de sair, [p=0.2] já mostrava o "
        "*tempo estimado* da viagem. [p=0.4] {e}Pergunta: [p=0.2] a velocidade da viagem *inteira* [p=0.2] foi noventa?"),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}Para responder, [p=0.2] a gente precisa de uma ideia nova. [p=0.4] {a}A *velocidade média.* [p=0.3] {b}É o "
        "*ritmo constante imaginário:* [p=0.2] se a viagem inteira tivesse um ritmo igual, [p=0.2] do começo ao fim, "
        "[p=0.2] qual seria esse ritmo? [p=0.4] {c}A conta é: [p=0.2] *distância total* [p=0.2] dividida pelo *tempo "
        "total.*"),
    dict(id="06", block="definicao", text=
        "{t}E o que entra em cada parte? [p=0.4] {a}*Distância total* [p=0.2] é tudo o que foi percorrido, [p=0.2] do "
        "ponto de partida até a chegada. [p=0.4] {b}*Tempo total* [p=0.2] é tudo o que o relógio marcou, [p=0.2] da "
        "saída até a chegada, [p=0.2] *sem pular nada.* [p=0.4] {c}Repare na palavra que se repete: [p=0.2] *total.* "
        "[p=0.2] Ela não é enfeite. [p=0.2] Ela é a *definição inteira.*"),

    # ================= BLOCO B: O TEMPO ANTES =================
    dict(id="07", block="relogio", text=
        "{t}Agora, por que dois vírgula trinta está errado? [p=0.4] {a}Porque o *relógio* não conta de dez em dez. "
        "[p=0.2] Conta de *sessenta em sessenta.* [p=0.4] {b}Trinta minutos são *meia volta* do ponteiro: [p=0.2] "
        "*metade* de uma hora. [p=0.4] {c}E metade, [p=0.2] escrita com vírgula, [p=0.2] é *zero vírgula cinco.* "
        "[p=0.2] Não zero vírgula três. [p=0.4] {d}Escrever a hora com vírgula assim [p=0.2] tem nome: [p=0.2] *hora "
        "decimal.*"),
    dict(id="08", block="relogio", text=
        "{t}E como se faz a conversão? [p=0.4] {a}Minutos dividido por *sessenta.* [p=0.3] Trinta dividido por "
        "sessenta: [p=0.2] *zero vírgula cinco.* [p=0.4] {b}Então duas horas e trinta minutos [p=0.2] são *dois vírgula "
        "cinco horas.* [p=0.4] {c}E a regra de ouro: [p=0.2] converta o tempo [p=0.2] *antes* de dividir."),
    dict(id="09", block="atalho_rel", text=
        "{t}Tem um atalho para não fazer essa conta toda vez. [p=0.4] {a}Pense nas *fatias* do relógio. [p=0.3] {b}Quinze "
        "minutos: [p=0.2] um quarto, [p=0.2] *zero vírgula vinte e cinco.* [p=0.3] Trinta: [p=0.2] metade, [p=0.2] *zero "
        "vírgula cinco.* [p=0.3] Quarenta e cinco: [p=0.2] três quartos, [p=0.2] *zero vírgula setenta e cinco.* [p=0.4] "
        "{c}E um curinga: [p=0.2] *seis minutos* [p=0.2] são *um décimo* de hora, [p=0.2] zero vírgula um."),

    # ================= BLOCO C: O TREM =================
    dict(id="10", block="trem", text=
        "{t}Agora o trem do começo. [p=0.3] {a}Distância total: [p=0.2] *cento e oitenta quilômetros.* [p=0.2] Tempo "
        "total, [p=0.2] já convertido: [p=0.2] *dois vírgula cinco horas.* [p=0.4] {b}Cento e oitenta dividido por dois "
        "vírgula cinco: [p=0.2] *setenta e dois quilômetros por hora.* [p=0.4] {c}E quem dividiu por dois vírgula "
        "três? [p=0.2] Chegou a quase *setenta e oito.* [p=0.2] Uma resposta que parece boa [p=0.2] e está errada."),
    dict(id="11", block="trem", text=
        "{t}Dividir por dois vírgula cinco de cabeça parece difícil? [p=0.3] {a}Atalho: [p=0.2] *dobre os dois.* "
        "[p=0.2] A divisão não muda. [p=0.4] {b}Cento e oitenta vira *trezentos e sessenta;* [p=0.2] dois vírgula cinco "
        "vira *cinco.* [p=0.4] {c}Trezentos e sessenta dividido por cinco: [p=0.2] *setenta e dois.* [p=0.2] Sem "
        "vírgula nenhuma."),

    # ================= BLOCO D: A PARADA =================
    dict(id="12", block="parada", text=
        "{t}E a parada no posto, [p=0.2] entra na conta? [p=0.4] {a}Volte ao ônibus. [p=0.2] Uma hora a noventa: "
        "[p=0.2] *noventa quilômetros.* [p=0.4] {b}Meia hora parado: [p=0.2] *zero quilômetro.* [p=0.2] Mas o "
        "cronômetro continua correndo. [p=0.4] {c}Mais uma hora a noventa: [p=0.2] mais *noventa quilômetros.* [p=0.4] "
        "{d}O cronômetro *não para no posto.*"),
    dict(id="13", block="parada", text=
        "{t}Somando tudo: [p=0.3] {a}distância total, [p=0.2] *cento e oitenta quilômetros.* [p=0.2] Tempo total, "
        "[p=0.2] uma hora, [p=0.2] mais meia, [p=0.2] mais uma: [p=0.2] *dois vírgula cinco horas.* [p=0.4] {b}Cento e "
        "oitenta dividido por dois vírgula cinco: [p=0.2] *setenta e dois.* [p=0.4] {c}O velocímetro marcou noventa, "
        "[p=0.2] mas a média da viagem foi *setenta e dois.* [p=0.2] A parada *puxou para baixo.* [p=0.4] {d}*Tempo "
        "parado também é tempo.* [p=0.2] Quando a pergunta é sobre o percurso completo, [p=0.2] ele entra."),

    # ================= BLOCO E: O FATOR 3,6 =================
    dict(id="14", block="fator", text=
        "{t}E quando a questão pede outra unidade? [p=0.4] {a}*Metros por segundo:* [p=0.2] quantos metros você anda a "
        "cada segundo. [p=0.4] {b}De quilômetros por hora para metros por segundo, [p=0.2] *divida por três vírgula "
        "seis.* [p=0.2] Cinquenta e quatro quilômetros por hora [p=0.2] viram *quinze metros por segundo.* [p=0.4] "
        "{c}No sentido contrário, [p=0.2] *multiplique.* [p=0.2] Quinze vezes três vírgula seis: [p=0.2] cinquenta e "
        "quatro de novo."),
    dict(id="15", block="fator", text=
        "{t}E como nunca mais inverter? [p=0.4] {a}Atalho: [p=0.2] o número em *metros por segundo* [p=0.2] é sempre o "
        "*menor.* [p=0.4] {b}Um segundo é muito pouco tempo: [p=0.2] em um segundo [p=0.2] você anda poucos metros. "
        "[p=0.4] {c}Indo para metros por segundo, [p=0.2] o número *diminui:* [p=0.2] divida. [p=0.2] Voltando para "
        "quilômetros por hora, [p=0.2] *aumenta:* [p=0.2] multiplique."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um ônibus percorre *duzentos e setenta quilômetros* [p=0.2] em *três horas* de estrada "
        "[p=0.2] e faz uma *parada de trinta minutos.* [p=0.2] Qual é a velocidade média da viagem completa? [p=0.4] "
        "{b}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Tempo total: [p=0.2] três horas de estrada [p=0.2] mais meia hora parado: [p=0.2] "
        "*três vírgula cinco horas.* [p=0.4] {b}Duzentos e setenta dividido por três vírgula cinco. [p=0.2] Dobre os "
        "dois: [p=0.2] quinhentos e quarenta dividido por sete: [p=0.2] *cerca de setenta e sete quilômetros por "
        "hora.* [p=0.4] {c}Quem esquece a parada [p=0.2] divide só por três [p=0.2] e acha *noventa.* [p=0.4] {d}Faz "
        "sentido o resultado ser menor que noventa? [p=0.2] Faz: [p=0.2] a parada puxa a média para baixo."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] velocidade média é distância total sobre tempo total. "
        "[p=0.5] {b}Dois: [p=0.2] tempo parado também é tempo. [p=0.5] {c}Três: [p=0.2] trinta minutos são zero vírgula "
        "cinco hora, [p=0.2] não zero vírgula trinta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler *dois vírgula cinco horas* como *duas "
        "horas e cinquenta minutos,* [p=0.2] ou trinta minutos como zero vírgula trinta. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque no dinheiro e no metro a vírgula funciona assim. [p=0.4] {c}Mas o relógio conta de sessenta em "
        "sessenta. [p=0.2] Divida os minutos por sessenta."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *ignorar o tempo de parada* [p=0.2] quando a pergunta é sobre o percurso completo. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque parado o ônibus não andou nada. [p=0.4] {c}Mas o relógio andou. [p=0.2] O "
        "tempo parado entra no tempo total."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] tratar quilômetros por hora e metros por segundo como *iguais,* [p=0.2] ou usar o três "
        "vírgula seis no *sentido errado.* [p=0.4] {b}Parece certo, [p=0.2] porque as duas são velocidade. [p=0.4] "
        "{c}Mas metros por segundo é sempre o número *menor.* [p=0.2] Diminuindo, divide; [p=0.2] aumentando, "
        "multiplica."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="22", block="q1", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta primeira, [p=0.2] do nosso material de estudo, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Um trem percorre *cento e oitenta quilômetros* entre duas estações [p=0.2] em "
        "*duas horas e trinta minutos.* [p=0.2] A velocidade média desse trem, em quilômetros por hora, é de: [p=0.4] "
        "{qa}A: [p=0.2] sessenta. [p=0.3] {qb}B: [p=0.2] sessenta e seis. [p=0.3] {qc}C: [p=0.2] setenta e dois. "
        "[p=0.3] {qd}D: [p=0.2] setenta e cinco. [p=0.3] {qe}E: [p=0.2] noventa."),
    dict(id="23", block="q1", text=
        "{t}O que a questão pede? [p=0.2] Velocidade média: [p=0.2] distância total sobre tempo total. [p=0.4] {a}Primeiro "
        "o tempo, [p=0.2] *antes* de dividir: [p=0.2] trinta minutos são meia hora. [p=0.2] Duas horas e trinta são "
        "*dois vírgula cinco horas.* [p=0.4] {b}Cento e oitenta dividido por dois vírgula cinco: [p=0.2] dobre os dois, "
        "[p=0.2] trezentos e sessenta dividido por cinco: [p=0.2] *setenta e dois.* [p=0.4] {c}Plausível? [p=0.2] "
        "Setenta e dois quilômetros por hora: [p=0.2] uma velocidade normal de trem. [p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q1", text=
        "{t}E as outras? [p=0.3] {xe}A E, [p=0.2] noventa, [p=0.2] é de quem usou *só as duas horas* [p=0.2] e jogou "
        "fora os trinta minutos. [p=0.4] {xa}A A, [p=0.2] sessenta, [p=0.2] é de quem arredondou para *três horas.* "
        "[p=0.4] {xb}A B [p=0.2] {xd}e a D [p=0.2] são valores vizinhos, [p=0.2] que não saem de nenhum erro comum. "
        "[p=0.4] {f}E atenção: [p=0.2] quem lê trinta minutos como zero vírgula trinta [p=0.2] divide por dois vírgula "
        "três [p=0.2] e acha *cerca de setenta e oito,* [p=0.2] que nem está entre as alternativas."),

    # ================= QUESTÃO DO ATLETA (VOCÊ FAZ) =================
    dict(id="25", block="q2", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um atleta percorre *cem metros* [p=0.2] em *doze vírgula cinco segundos.* [p=0.2] "
        "A velocidade média desse atleta, *em quilômetros por hora,* é de: [p=0.4] {qa}A: [p=0.2] oito. [p=0.3] {qb}B: "
        "[p=0.2] doze vírgula cinco. [p=0.3] {qc}C: [p=0.2] vinte e oito vírgula oito. [p=0.3] {qd}D: [p=0.2] trinta e "
        "seis. [p=0.3] {qe}E: [p=0.2] oitenta. [p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="26", block="q2", text=
        "{t}Conferindo. [p=0.3] {a}Distância sobre tempo, [p=0.2] nas unidades do enunciado: [p=0.2] cem metros dividido "
        "por doze vírgula cinco segundos. [p=0.2] *Oito metros por segundo.* [p=0.4] {b}Mas a pergunta é em quilômetros "
        "por hora. [p=0.2] O número tem que *aumentar:* [p=0.2] multiplique por três vírgula seis. [p=0.2] *Vinte e oito "
        "vírgula oito.* [p=0.4] {c}Plausível? [p=0.2] Uma corrida comum fica perto de doze quilômetros por hora. "
        "[p=0.2] Um velocista, [p=0.2] perto de trinta. [p=0.2] Faz sentido. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q2", text=
        "{t}E as erradas? [p=0.3] {xa}A A, [p=0.2] oito, [p=0.2] *parou em metros por segundo* [p=0.2] e não converteu. "
        "[p=0.2] Oito quilômetros por hora [p=0.2] seria uma caminhada rápida. [p=0.4] {xb}A B só repete o *tempo* do "
        "enunciado. [p=0.4] {xd}A D, [p=0.2] trinta e seis, [p=0.2] é de quem arredondou para *cem metros em dez "
        "segundos.* [p=0.4] {xe}E a E, [p=0.2] oitenta, [p=0.2] multiplicou por *dez* [p=0.2] em vez de três vírgula "
        "seis."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] velocidade média é distância total sobre tempo "
        "total. [p=0.5] {b}Dois: [p=0.2] tempo parado também é tempo. [p=0.5] {c}Três: [p=0.2] trinta minutos são zero "
        "vírgula cinco hora, [p=0.2] não zero vírgula trinta."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Um carro vai a *sessenta quilômetros por hora* [p=0.2] e volta pelo mesmo caminho a *quarenta.* [p=0.4] "
        "{b}A média é *cinquenta?* [p=0.4] {c}Quase todo mundo marca cinquenta. [p=0.2] *E está errado.* [p=0.4] "
        "{d}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no erro do dois vírgula trinta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
