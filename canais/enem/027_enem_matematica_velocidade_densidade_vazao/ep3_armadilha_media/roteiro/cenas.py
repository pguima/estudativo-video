# Roteiro — Velocidade, Densidade e Vazão, Episódio 3 de 6: a armadilha da média (ida a 60, volta a 40, média 48)
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seção 04 + Questão 2 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   QUEM MANDA NA MÉDIA É O RELÓGIO: o trecho lento dura mais, então pesa mais (barras de tempo 2 h × 3 h numa balança).
#   A DISTÂNCIA AMIGA: invente uma distância que as duas velocidades dividem (120 km para 60 e 40) e a conta sai de cabeça.
#   Distâncias iguais: média harmônica; tempos iguais: média simples.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: a Q2 é o próprio exemplo da seção 04 (60 e 40), por desenho do usuário: lida no gancho, desmontada nos blocos e
#   resolvida como "eu faço" no fim, pelos dois caminhos. Nós fazemos (prompt): ciclista 30 e 60 → 60 km amiga, 2 h + 1 h,
#   120 ÷ 3 = 40 km/h; fórmula 2 · 30 · 60 ÷ 90 = 40; média simples 45. Você faz (prompt): 1 h a 80 + 1 h a 60 → 140 km em
#   2 h = 70 km/h (tempos iguais: a média simples funciona; a harmônica daria 9 600 ÷ 140 ≈ 68,6, ERRADO aqui).
# QUESTÃO 2 (texto idêntico na tela): 120 km amiga → 2 h + 3 h = 5 h; 240 ÷ 5 = 48 → C. Harmônica: 4 800 ÷ 100 = 48.
#   Material: D (50) é a resposta instintiva (média simples).
#   Do PROMPT (o material não explica): A (44) e B (46) ficam abaixo de 48 e não saem de nenhum raciocínio correto;
#   E (52) é impossível: com distâncias iguais o resultado nunca passa da média simples.
# Atalhos (verde): distância amiga = um número que as duas velocidades dividem (o MMC delas é o menor; o produto sempre serve) ·
#   fórmula de bolso "dobro do produto sobre a soma" · conferência: com distâncias iguais a resposta fica ENTRE a menor
#   velocidade e a média simples.
# Frases-chave (meio e fim, idênticas): 1. Quem manda na média é o relógio. 2. Distâncias iguais: o resultado fica abaixo da
#   média simples. 3. Na dúvida, distância total sobre tempo total, sempre.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Ida a 60, volta a 40: por que a média NÃO é 50 · Matemática ENEM, Velocidade, densidade e vazão, episódio 3"

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
        "{a}Um motorista percorre o trajeto de ida entre duas cidades [p=0.2] a *sessenta* quilômetros por hora, [p=0.3] "
        "e faz a volta, [p=0.2] pelo mesmo caminho, [p=0.2] a *quarenta.* [p=0.3] Qual é a velocidade média da ida e "
        "volta? [p=0.4] {qa}Quarenta e quatro, [p=0.2] {qb}quarenta e seis, [p=0.2] {qc}quarenta e oito, [p=0.2] "
        "{qd}cinquenta [p=0.2] {qe}ou cinquenta e dois? [p=0.5] {p}*Pause e marque a sua resposta agora.* [p=0.3] "
        "Guarde. [p=0.3] No fim do vídeo a gente confere. [p=2.0]"),
    dict(id="02", block="hook2", text=
        "{a}Se você marcou *cinquenta,* [p=0.3] está com a maioria. [p=0.5] {b}E a maioria *erra* esta questão."),
    dict(id="03", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber por que a resposta é *quarenta e oito,* [p=0.3] {b}calcular de "
        "*dois jeitos* [p=0.3] {c}e reconhecer quando a média simples *funciona.*"),
    dict(id="04", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] velocidade média é a *distância total* "
        "[p=0.2] dividida pelo *tempo total.* [p=0.4] {b}E, do episódio um: [p=0.2] se você sabe a distância e a "
        "velocidade, [p=0.2] o tempo é *distância dividida por velocidade.* [p=0.2] Cento e vinte quilômetros a "
        "sessenta por hora: [p=0.2] *duas horas.*"),

    # ================= CONCRETO =================
    dict(id="05", block="concreto", text=
        "{t}Pense numa coisa do dia a dia. [p=0.3] {a}De manhã, [p=0.2] você vai para o trabalho com o *trânsito livre.* "
        "[p=0.2] Chega rapidinho. [p=0.4] {b}À tarde, [p=0.2] volta pelo *mesmo caminho,* [p=0.2] só que no "
        "*congestionamento.* [p=0.4] {c}Em qual dos dois trechos você passa *mais tempo* dentro do carro? [p=0.4] "
        "{d}No lento, [p=0.2] claro. [p=0.3] Guarde isso: [p=0.2] é a chave da aula inteira."),

    # ================= BLOCO A: A RESPOSTA INSTINTIVA =================
    dict(id="06", block="instinto", text=
        "{t}Então, de onde vem o cinquenta? [p=0.4] {a}Da *média simples:* [p=0.2] somar os valores [p=0.2] e dividir "
        "pela quantidade deles. [p=0.4] {b}Sessenta mais quarenta, [p=0.2] cem. [p=0.2] Dividido por dois, [p=0.2] "
        "*cinquenta.* [p=0.4] {c}E por que parece tão certo? [p=0.2] Porque a palavra *média* [p=0.2] dá vontade de "
        "somar e dividir. [p=0.2] E porque o cinquenta fica bem no meio, [p=0.2] bonitinho. [p=0.4] {d}Só que isso é "
        "a média das *velocidades.* [p=0.3] E a pergunta é a velocidade *média.* [p=0.3] Não é a mesma coisa."),

    # ================= BLOCO B: A DISTÂNCIA AMIGA =================
    dict(id="07", block="amiga", text=
        "{t}E como descobrir a resposta, [p=0.2] se o enunciado nem diz a distância? [p=0.4] {a}Truque: [p=0.2] "
        "*invente uma distância amiga.* [p=0.3] Um número que as *duas* velocidades dividem certinho. [p=0.4] {b}Sessenta "
        "e quarenta dividem *cento e vinte.* [p=0.3] {c}Então cada *trecho,* [p=0.2] cada pedaço do caminho, [p=0.2] "
        "a ida e a volta, [p=0.2] vai ter cento e vinte quilômetros."),
    dict(id="08", block="amiga", text=
        "{t}Agora é só fazer as contas de cabeça. [p=0.3] {a}Ida: [p=0.2] cento e vinte a sessenta por hora, [p=0.2] "
        "*duas horas.* [p=0.4] {b}Volta: [p=0.2] cento e vinte a quarenta por hora, [p=0.2] *três horas.* [p=0.4] "
        "{c}Distância total: [p=0.2] *duzentos e quarenta* quilômetros. [p=0.2] Tempo total: [p=0.2] *cinco* horas. "
        "[p=0.4] {d}Duzentos e quarenta dividido por cinco: [p=0.2] *quarenta e oito* quilômetros por hora. [p=0.3] "
        "Não cinquenta."),
    dict(id="09", block="atalho_amiga", text=
        "{t}E se você inventar outra distância? [p=0.3] {a}Dá o *mesmo* resultado. [p=0.2] Teste com duzentos e "
        "quarenta: [p=0.2] quatro horas mais seis, [p=0.2] quatrocentos e oitenta em dez horas, [p=0.2] quarenta e oito. "
        "[p=0.4] {b}Atalho para escolher a amiga: [p=0.2] o *produto* das velocidades sempre serve, [p=0.3] {c}mas o "
        "*menor* número que as duas dividem, [p=0.2] o *mínimo múltiplo comum* da série de MMC, [p=0.2] deixa a conta "
        "menor."),

    # ================= BLOCO C: A RAZÃO DO FENÔMENO =================
    dict(id="10", block="relogio", text=
        "{t}Mas *por que* deu menos que cinquenta? [p=0.4] {a}Olhe as barras de tempo. [p=0.2] A ida: [p=0.2] *dois* "
        "blocos de uma hora. [p=0.3] {b}A volta: [p=0.2] *três* blocos. [p=0.4] {c}As *distâncias* são iguais, [p=0.2] "
        "mas os *tempos* não. [p=0.3] Igualzinho ao trânsito: [p=0.2] você passa mais tempo no trecho lento."),
    dict(id="11", block="relogio", text=
        "{t}E o que isso faz com a média? [p=0.4] {a}O *peso* de um valor na média [p=0.2] é o quanto ele conta no "
        "resultado. [p=0.3] Aqui, [p=0.2] quem dá o peso é o *tempo.* [p=0.4] {b}O quarenta ficou três horas na balança. "
        "[p=0.2] O sessenta, [p=0.2] só duas. [p=0.4] {c}Então o quarenta *pesa mais* [p=0.2] e puxa a média para baixo: "
        "[p=0.2] de cinquenta [p=0.2] para quarenta e oito. [p=0.4] {d}*Quem manda na média é o relógio.*"),
    dict(id="12", block="relogio", text=
        "{t}E isso acontece sempre? [p=0.3] {a}Sempre. [p=0.2] Com distâncias iguais, [p=0.2] o trecho mais lento "
        "*sempre* dura mais. [p=0.4] {b}Então o resultado fica *sempre abaixo* da média simples. [p=0.3] Nunca acima. "
        "[p=0.4] {c}Guarde como conferência: [p=0.2] a resposta fica *entre* a velocidade menor [p=0.2] e a média "
        "simples. [p=0.2] Entre quarenta e cinquenta."),

    # ================= BLOCO D: A FÓRMULA =================
    dict(id="13", block="formula", text=
        "{t}Existe uma fórmula pronta para isso? [p=0.3] Existe. [p=0.4] {a}Quando as distâncias são iguais, [p=0.2] a "
        "velocidade média é a *média harmônica:* [p=0.3] o nome da média que dá mais peso aos valores *menores.* "
        "[p=0.4] {b}A conta é: [p=0.2] *duas vezes* uma velocidade [p=0.2] vezes a outra, [p=0.2] dividido pela *soma* "
        "delas. [p=0.4] {c}Duas vezes sessenta vezes quarenta: [p=0.2] *quatro mil e oitocentos.* [p=0.2] Sessenta mais "
        "quarenta: [p=0.2] *cem.* [p=0.3] {d}Quatro mil e oitocentos dividido por cem: [p=0.2] *quarenta e oito.* "
        "[p=0.2] O mesmo número."),
    dict(id="14", block="formula", text=
        "{t}Mas tem um aviso em letras grandes. [p=0.4] {a}Ela *só* vale para *distâncias iguais:* [p=0.2] ida e volta "
        "pelo mesmo caminho, [p=0.2] dois trechos do mesmo tamanho. [p=0.4] {b}Fora desse caso, [p=0.2] esqueça a "
        "fórmula [p=0.2] e volte para o que funciona *em qualquer situação:* [p=0.3] {c}distância total sobre tempo "
        "total. [p=0.4] {d}Atalho para lembrar a fórmula: [p=0.2] *o dobro do produto sobre a soma.*"),

    # ================= BLOCO E: TEMPOS IGUAIS =================
    dict(id="15", block="tempos", text=
        "{t}E a média simples? [p=0.2] Ela nunca funciona? [p=0.4] {a}Funciona, [p=0.2] quando os *tempos* são iguais. "
        "[p=0.3] *Tempos iguais* quer dizer: [p=0.2] o mesmo tanto de horas em cada velocidade. [p=0.4] {b}Duas horas a "
        "sessenta: [p=0.2] *cento e vinte* quilômetros. [p=0.2] Duas horas a quarenta: [p=0.2] *oitenta.* [p=0.4] "
        "{c}Total: [p=0.2] duzentos quilômetros em quatro horas. [p=0.2] *Cinquenta* quilômetros por hora. [p=0.4] "
        "{d}Agora cada velocidade ficou o mesmo tempo na balança, [p=0.2] pesou igual, [p=0.2] e o cinquenta voltou a "
        "valer."),
    dict(id="16", block="tempos", text=
        "{t}Então, a regra completa. [p=0.4] {a}*Distâncias iguais:* [p=0.2] média harmônica, [p=0.2] o resultado fica "
        "abaixo. [p=0.4] {b}*Tempos iguais:* [p=0.2] média simples. [p=0.4] {c}E na dúvida, [p=0.2] nenhuma das duas: "
        "[p=0.2] distância total sobre tempo total."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um ciclista vai a *trinta* quilômetros por hora [p=0.2] e volta pelo mesmo caminho a "
        "*sessenta.* [p=0.2] Qual é a velocidade média da ida e volta? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Mesmo caminho: [p=0.2] distâncias iguais. [p=0.2] Distância amiga: [p=0.2] "
        "*sessenta* quilômetros, [p=0.2] que trinta e sessenta dividem. [p=0.4] {b}Ida: [p=0.2] sessenta a trinta, "
        "[p=0.2] *duas horas.* [p=0.2] Volta: [p=0.2] sessenta a sessenta, [p=0.2] *uma hora.* [p=0.4] {c}Cento e vinte "
        "quilômetros em três horas: [p=0.2] *quarenta* quilômetros por hora. [p=0.4] {d}Pela fórmula: [p=0.2] duas vezes "
        "trinta vezes sessenta, [p=0.2] três mil e seiscentos, [p=0.2] dividido por noventa: [p=0.2] quarenta. [p=0.2] "
        "Bateu. [p=0.4] {e}E a média simples daria *quarenta e cinco:* [p=0.2] de novo, [p=0.2] acima da certa."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] quem manda na média é o relógio. [p=0.5] {b}Dois: "
        "[p=0.2] distâncias iguais: [p=0.2] o resultado fica abaixo da média simples. [p=0.5] {c}Três: [p=0.2] na dúvida, "
        "[p=0.2] distância total sobre tempo total, [p=0.2] sempre."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] fazer a *média das velocidades* [p=0.2] quando "
        "as distâncias são iguais. [p=0.4] {b}Parece certo, [p=0.2] porque são dois números [p=0.2] e a gente aprendeu "
        "a somar e dividir por dois. [p=0.4] {c}Mas o trecho lento dura mais [p=0.2] e pesa mais. [p=0.2] Use a "
        "distância amiga."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] usar a média harmônica com *distâncias diferentes.* [p=0.2] Cem quilômetros a sessenta "
        "[p=0.2] e só vinte a quarenta, [p=0.2] por exemplo. [p=0.4] {b}Parece certo, [p=0.2] porque a fórmula é "
        "rápida [p=0.2] e já funcionou antes. [p=0.4] {c}Mas ela só vale com trechos do mesmo tamanho. [p=0.2] Aqui, "
        "[p=0.2] volte à distância total sobre tempo total."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] usar a média harmônica quando os *tempos* são iguais. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque você acabou de aprender que a média simples é pegadinha. [p=0.4] {c}Mas, com o mesmo tempo em cada "
        "velocidade, [p=0.2] cada uma pesa igual. [p=0.2] Aí a média simples *é* a certa."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="23", block="q2", text=
        "{t}Agora, a questão do começo, [p=0.2] do nosso material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo com você. "
        "[p=0.4] {a}Ida a *sessenta,* [p=0.2] volta pelo mesmo caminho a *quarenta.* [p=0.2] A velocidade média da ida "
        "e volta é de: [p=0.4] {qa}A: [p=0.2] quarenta e quatro. [p=0.3] {qb}B: [p=0.2] quarenta e seis. [p=0.3] "
        "{qc}C: [p=0.2] quarenta e oito. [p=0.3] {qd}D: [p=0.2] cinquenta. [p=0.3] {qe}E: [p=0.2] cinquenta e dois "
        "quilômetros por hora."),
    dict(id="24", block="q2", text=
        "{t}Primeiro: [p=0.2] o caso. [p=0.2] Mesmo caminho: [p=0.2] *distâncias iguais.* [p=0.4] {a}Primeiro jeito, "
        "[p=0.2] a distância amiga: [p=0.2] cento e vinte. [p=0.2] Duas horas mais três horas, [p=0.2] duzentos e "
        "quarenta quilômetros em cinco horas: [p=0.2] *quarenta e oito.* [p=0.4] {b}Segundo jeito, [p=0.2] a média "
        "harmônica: [p=0.2] quatro mil e oitocentos sobre cem, [p=0.2] *quarenta e oito.* [p=0.4] {c}Plausível? "
        "[p=0.2] Ficou entre quarenta e cinquenta, [p=0.2] abaixo da média simples. [p=0.3] {ok}*Letra C!*"),
    dict(id="25", block="q2", text=
        "{t}E as outras? [p=0.3] {xd}A D, [p=0.2] cinquenta, [p=0.2] é a *média simples:* [p=0.2] a pegadinha. [p=0.4] "
        "{xa}A A [p=0.2] {xb}e a B [p=0.2] ficam abaixo de quarenta e oito [p=0.2] e não saem de nenhum raciocínio "
        "correto. [p=0.4] {xe}E a E, [p=0.2] cinquenta e dois, [p=0.2] é *impossível:* [p=0.2] com distâncias iguais, "
        "[p=0.2] o resultado nunca passa da média simples. [p=0.4] {f}Agora confira a resposta que você marcou no "
        "começo. [p=0.3] Se foi a C, [p=0.2] parabéns. [p=0.2] Se foi a D, [p=0.2] agora você sabe por quê."),

    # ================= VOCÊ FAZ =================
    dict(id="26", block="voce", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um carro anda *uma hora* a oitenta quilômetros por hora [p=0.2] e mais *uma hora* "
        "a sessenta. [p=0.2] Qual é a velocidade média? [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="27", block="voce", text=
        "{t}Conferindo. [p=0.2] Repare: [p=0.2] aqui o que é igual é o *tempo.* [p=0.4] {a}Uma hora a oitenta: [p=0.2] "
        "oitenta quilômetros. [p=0.2] Uma hora a sessenta: [p=0.2] sessenta. [p=0.4] {b}Cento e quarenta quilômetros "
        "em duas horas: [p=0.2] *setenta* quilômetros por hora. [p=0.4] {c}Tempos iguais: [p=0.2] a média simples "
        "*funciona.* [p=0.2] Oitenta mais sessenta, [p=0.2] dividido por dois, [p=0.2] setenta. [p=0.4] {d}Se você usou "
        "a fórmula da harmônica, [p=0.2] deu uns sessenta e oito e meio. [p=0.2] É o terceiro erro clássico."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] quem manda na média é o relógio. [p=0.5] "
        "{b}Dois: [p=0.2] distâncias iguais: [p=0.2] o resultado fica abaixo da média simples. [p=0.5] {c}Três: "
        "[p=0.2] na dúvida, [p=0.2] distância total sobre tempo total, [p=0.2] sempre."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Um objeto tem *cento e cinquenta e seis gramas* [p=0.2] e ocupa *vinte centímetros cúbicos.* [p=0.5] {b}Sem "
        "nenhum laboratório, [p=0.2] dá para saber de que metal ele é feito. [p=0.5] {c}Próximo episódio: [p=0.2] "
        "*densidade.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você marcou cinquenta no começo? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
