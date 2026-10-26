# Roteiro — Frações, Decimais e Dízimas, Episódio 7 de 8: A tabela que vale ouro (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seção 10 (tabela e as quatro conversões)
#   + Questão 8 da seção 12. SÓ conversão: nada de fator de multiplicação, aumentos ou descontos (série própria).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: fração, decimal e porcentagem são três IDIOMAS do mesmo número ("meia dúzia" e "seis").
# Tabela (conferida): 1/2 = 0,5 = 50% · 1/4 = 0,25 = 25% · 3/4 = 0,75 = 75% · 1/3 = 0,333… ≈ 33,3% · 2/3 = 0,666… ≈ 66,7% ·
#   1/6 = 0,1666… ≈ 16,7% · 1/5 = 0,2 = 20% · 2/5 = 0,4 = 40% · 3/5 = 0,6 = 60% · 1/8 = 0,125 = 12,5% · 3/8 = 0,375 = 37,5% ·
#   5/8 = 0,625 = 62,5% · 7/8 = 0,875 = 87,5% · 1/10 = 0,1 = 10% · 1/20 = 0,05 = 5% · 1/100 = 0,01 = 1%.
#   Terços e sextos são dízimas: a porcentagem é APROXIMADA (≈).
# Conversões: 7/20 = 7 ÷ 20 = 0,35 (= 35/100) · 0,35 × 100 = 35% · 37,5% = 37,5/100 = 375/1000 = 3/8 (÷ 125) ·
#   0,24 = 24/100 = 6/25 (÷ 4).
# Jogo "nós fazemos": 3/4 = 0,75 = 75% · 0,2 = 1/5 = 20% · 62,5% = 5/8 = 0,625 · 1/20 = 0,05 = 5%.
# Q8 (material): 3/8 = 0,375 = 37,5% → C · E = 62,5% = complemento (material) · A 3,8% e D 38% = leram 3/8 como 3,8
#   (erro clássico do prompt) · B 24% = 3 × 8 (explicação nossa; o material só explica a E).
# Frases-chave (meio e fim, idênticas):
#   1. "Fração, decimal e porcentagem: três idiomas do mesmo número."
#   2. "Cada quinto vale 20%; cada oitavo vale 12,5%."
#   3. "Para virar porcentagem, multiplique o decimal por 100."
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A tabela que vale ouro: fração, decimal e porcentagem de cabeça | Frações Ep. 7"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte "
            "às palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Se você só pudesse decorar *uma* coisa deste assunto, [p=0.3] {b}seria *esta tabela.* [p=0.5] {c}Ela economiza "
        "minutos em porcentagem, [p=0.2] probabilidade [p=0.2] e estatística."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai transitar entre fração, [p=0.2] decimal [p=0.2] e porcentagem [p=0.2] "
        "*de cabeça.* [p=0.4] {b}Sem decorar tudo: [p=0.2] usando *padrões.*"),

    # ================= CONCRETO ANTES DO ABSTRATO =================
    dict(id="03", block="concreto", text=
        "{a}*Metade* de uma pizza. [p=0.3] {b}*Meio* quilo. [p=0.3] {c}*Cinquenta por cento* "
        "de desconto. [p=0.3] {d}*Zero vírgula cinco* na calculadora. [p=0.5] {e}É tudo o *mesmo número.* [p=0.5] "
        "{f}E a bateria do celular em vinte e cinco por cento? [p=0.3] É *um quarto* da carga."),
    dict(id="04", block="idiomas", text=
        "{a}*Meia dúzia* [p=0.2] e *seis* [p=0.2] são o mesmo tanto, [p=0.2] dito de dois jeitos. "
        "[p=0.5] {b}Fração, [p=0.2] decimal [p=0.2] e porcentagem [p=0.2] são *três idiomas* do mesmo número. [p=0.5] {c}O ENEM "
        "troca de idioma no meio do enunciado. [p=0.3] {d}E quem é fluente nos três [p=0.2] *ganha tempo.* [p=0.4] {e}Traduzir de "
        "um idioma para outro [p=0.2] tem nome: [p=0.2] *conversão.*"),
    dict(id="05", block="porcento", text=
        "{t}Mas o que quer dizer *por cento?* [p=0.4] {a}Quer dizer *de cada cem.* [p=0.4] {c}*Porcentagem* é uma fração com o cem embaixo. "
        "[p=0.4] {d}Cinquenta por cento [p=0.2] é cinquenta sobre cem."),
    dict(id="06", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] fração é *divisão.* [p=0.2] Um meio é "
        "um dividido por dois: [p=0.2] zero vírgula cinco. [p=0.4] {b}E do episódio cinco: [p=0.2] multiplicar por cem [p=0.2] "
        "é andar com a vírgula *duas casas para a direita.* [p=0.3] {c}Zero vírgula cinco vezes cem [p=0.2] dá cinquenta."),

    # ================= FAMÍLIA A: METADES E QUARTOS =================
    dict(id="07", block="fam_quartos", text=
        "{t}Primeira família: [p=0.2] *metades e quartos.* [p=0.3] {a}Um meio: [p=0.2] zero vírgula cinco, [p=0.2] cinquenta por "
        "cento. [p=0.4] {b}Um quarto é a metade da metade: [p=0.2] zero vírgula vinte e cinco, [p=0.2] vinte e cinco por cento. "
        "[p=0.4] {c}Três quartos: [p=0.2] zero vírgula setenta e cinco, [p=0.2] setenta e cinco por cento."),
    dict(id="08", block="fam_quartos", text=
        "{t}E um padrão para não decorar. [p=0.3] {a}*Cada quarto vale vinte e cinco por cento.* [p=0.2] Três quartos, [p=0.2] "
        "três vezes vinte e cinco. [p=0.4] {b}E um quarto mais três quartos [p=0.2] completam o inteiro. [p=0.3] "
        "{c}Um é o *complemento* do outro: [p=0.2] o que falta para *cem por cento.*"),

    # ================= FAMÍLIA B: TERÇOS E SEXTOS =================
    dict(id="09", block="fam_tercos", text=
        "{t}Segunda família: [p=0.2] *terços e sextos.* [p=0.3] {a}Um terço: [p=0.2] zero vírgula três, três, três, [p=0.2] "
        "sem fim. [p=0.4] {b}É uma *dízima,* [p=0.2] como no episódio seis. [p=0.3] {c}Por isso a porcentagem é *aproximada:* "
        "[p=0.2] cerca de trinta e três vírgula três por cento. [p=0.4] {d}Dois terços: [p=0.2] cerca de sessenta e seis vírgula "
        "sete."),
    dict(id="10", block="fam_tercos", text=
        "{t}O atalho dessa família: [p=0.3] {a}dois terços é o *dobro* de um terço. [p=0.4] {b}E um sexto é a *metade* de um "
        "terço: [p=0.2] metade de trinta e três vírgula três, [p=0.2] cerca de dezesseis vírgula sete. [p=0.4] {c}Viu esse "
        "*cerca de* na alternativa? [p=0.2] Pense em terços e sextos."),

    # ================= FAMÍLIA C: QUINTOS =================
    dict(id="11", block="fam_quintos", text=
        "{t}Terceira família: [p=0.2] *quintos.* [p=0.3] {a}Um quinto: [p=0.2] zero vírgula dois, [p=0.2] vinte por cento. "
        "[p=0.4] {b}O padrão: [p=0.2] cinco quintos fazem cem por cento, [p=0.2] então *cada quinto vale vinte "
        "por cento.* [p=0.4] {c}Dois quintos, [p=0.2] quarenta. [p=0.3] {d}Três quintos, [p=0.2] sessenta. [p=0.3] É só contar de "
        "vinte em vinte."),

    # ================= FAMÍLIA D: OITAVOS =================
    dict(id="12", block="fam_oitavos", text=
        "{t}Quarta família, [p=0.2] a queridinha do ENEM: [p=0.2] *oitavos.* [p=0.4] {a}Um oitavo é a metade de um quarto. "
        "[p=0.3] Metade de vinte e cinco: [p=0.2] *doze vírgula cinco por cento.* [p=0.2] Em decimal, [p=0.2] zero vírgula cento "
        "e vinte e cinco. [p=0.4] {b}E então, [p=0.2] *cada oitavo vale doze vírgula cinco.* [p=0.4] {c}Três oitavos, [p=0.2] "
        "trinta e sete vírgula cinco. [p=0.3] {d}Cinco oitavos, [p=0.2] sessenta e dois vírgula cinco. [p=0.3] {e}Sete oitavos, "
        "[p=0.2] oitenta e sete vírgula cinco."),

    # ================= FAMÍLIA E: DÉCIMOS, VIGÉSIMOS E CENTÉSIMOS =================
    dict(id="13", block="fam_decimos", text=
        "{t}Última família: [p=0.2] *décimos, [p=0.2] vigésimos e centésimos.* [p=0.4] {a}Um décimo: [p=0.2] zero vírgula um, "
        "[p=0.2] dez por cento. [p=0.4] {b}Um vigésimo é a metade de um décimo: [p=0.2] zero vírgula zero cinco, [p=0.2] cinco "
        "por cento. [p=0.4] {c}E um centésimo: [p=0.2] zero vírgula zero um, [p=0.2] *um por cento.* [p=0.3] {d}Literalmente: "
        "[p=0.2] um de cada cem."),

    # ================= AS QUATRO CONVERSÕES =================
    dict(id="14", block="conv", text=
        "{t}E quando o número *não está* na tabela? [p=0.4] Quatro traduções. [p=0.3] {a}Primeira: [p=0.2] de fração para decimal, "
        "[p=0.2] *divida* o de cima pelo de baixo. [p=0.4] {b}Sete vinte avos: [p=0.2] sete dividido por vinte, [p=0.2] zero "
        "vírgula trinta e cinco. [p=0.4] {c}Atalho: [p=0.2] se der, faça o de baixo virar *cem:* [p=0.2] vezes cinco, "
        "[p=0.2] trinta e cinco centésimos."),
    dict(id="15", block="conv", text=
        "{t}Segunda: [p=0.2] de decimal para porcentagem, [p=0.2] *multiplique por cem.* [p=0.4] {a}Zero vírgula trinta e cinco, "
        "[p=0.2] trinta e cinco por cento. [p=0.4] {b}Atalho: [p=0.2] é só andar com a vírgula *duas casas para a direita.*"),
    dict(id="16", block="conv", text=
        "{t}Terceira: [p=0.2] de porcentagem para fração, [p=0.2] *ponha sobre cem e simplifique.* [p=0.4] {a}Trinta e sete "
        "vírgula cinco por cento [p=0.2] é trinta e sete vírgula cinco sobre cem. [p=0.4] {b}Para tirar a vírgula, [p=0.2] vezes "
        "dez em cima e embaixo: [p=0.2] trezentos e setenta e cinco sobre mil. [p=0.4] {c}Simplificar é dividir em cima e embaixo "
        "pelo mesmo número. [p=0.2] Por cento e vinte e cinco: [p=0.2] *três oitavos.* [p=0.4] {d}Atalho: [p=0.2] terminou em "
        "*vírgula cinco?* [p=0.2] Desconfie dos oitavos."),
    dict(id="17", block="conv", text=
        "{t}Quarta: [p=0.2] de decimal exato para fração. [p=0.4] {a}Escreva o número *sem vírgula* sobre dez, [p=0.2] cem ou "
        "mil. [p=0.3] {b}Zero vírgula vinte e quatro: [p=0.2] vinte e quatro sobre cem. [p=0.4] {c}Simplifica por quatro: "
        "[p=0.2] *seis vinte e cinco avos.* [p=0.4] {d}Atalho: [p=0.2] *conte as casas* depois da vírgula. [p=0.2] Duas casas, "
        "[p=0.2] dois zeros: [p=0.2] cem."),

    # ================= NÓS FAZEMOS: O JOGO DAS CARTAS =================
    dict(id="18", block="jogo", text=
        "{t}Agora, [p=0.2] um jogo. [p=0.3] Eu mostro um idioma; [p=0.2] você diz os outros dois. [p=0.4] {a}*Três quartos.* "
        "[p=0.3] {p1}Pause e diga. [p=2.0] {r1}Zero vírgula setenta e cinco, [p=0.2] setenta e cinco por cento. [p=0.5] "
        "{b}*Zero vírgula dois.* [p=0.3] {p2}Pause e diga. [p=2.0] {r2}Um quinto, [p=0.2] vinte por cento."),
    dict(id="19", block="jogo", text=
        "{a}*Sessenta e dois vírgula cinco por cento.* [p=0.3] {p1}Pause e diga. [p=2.0] {r1}Terminou em vírgula cinco: "
        "[p=0.2] oitavos. [p=0.2] Cinco oitavos, [p=0.2] zero vírgula seiscentos e vinte e cinco. [p=0.5] {b}*Um vigésimo.* "
        "[p=0.3] {p2}Pause e diga. [p=2.0] {r2}Zero vírgula zero cinco, [p=0.2] cinco por cento."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] fração, [p=0.2] decimal e porcentagem: [p=0.2] três idiomas "
        "do mesmo número. [p=0.5] {b}Dois: [p=0.2] cada quinto vale vinte por cento; [p=0.2] cada oitavo vale doze vírgula cinco "
        "por cento. [p=0.5] {c}Três: [p=0.2] para virar porcentagem, [p=0.2] multiplique o decimal por cem."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler três oitavos [p=0.2] como *três vírgula oito por "
        "cento,* [p=0.2] ou trinta e oito. [p=0.4] {b}Parece certo, [p=0.2] porque os algarismos são os mesmos. "
        " [p=0.4] {c}Mas a barra da fração é *divisão:* [p=0.2] três dividido por oito, [p=0.2] trinta e sete vírgula cinco."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] responder o *complemento,* [p=0.2] quem *não* escolheu, [p=0.2] em vez do que foi pedido. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a conta estava certa. [p=0.4] {c}Mas a alternativa do complemento está lá, "
        "[p=0.2] esperando. [p=0.2] Releia a pergunta no fim."),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] voltar de porcentagem para fração [p=0.2] e *esquecer de simplificar.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque vinte e quatro sobre cem *é* o mesmo número. [p=0.4] {c}Mas a alternativa vem simplificada: [p=0.2] seis "
        "vinte e cinco avos. [p=0.2] Simplifique até o fim."),

    # ================= QUESTÃO 8 =================
    dict(id="24", block="q8", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Numa pesquisa de opinião, [p=0.2] três oitavos dos entrevistados "
        "escolheram a opção A. [p=0.4] {b}Esse valor corresponde a que porcentagem do total de entrevistados? [p=0.4] {c}A: "
        "[p=0.2] três vírgula oito por cento. [p=0.3] {d}B: [p=0.2] vinte e quatro por cento. [p=0.3] {e}C: [p=0.2] trinta e sete "
        "vírgula cinco por cento. [p=0.3] {f}D: [p=0.2] trinta e oito por cento. [p=0.3] {g}E: [p=0.2] sessenta e dois vírgula "
        "cinco por cento. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q8", text=
        "{t}Vamos conferir. [p=0.3] {a}Pela divisão: [p=0.2] três dividido por oito, [p=0.2] zero vírgula trezentos e setenta e "
        "cinco. [p=0.3] Vezes cem: [p=0.2] trinta e sete vírgula cinco por cento. [p=0.4] {b}Pelo atalho: [p=0.2] cada oitavo vale "
        "doze vírgula cinco. [p=0.2] Três vezes doze vírgula cinco, [p=0.2] trinta e sete vírgula cinco, [p=0.2] *sem dividir "
        "nada.* [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q8", text=
        "{e}E a *E,* [p=0.2] sessenta e dois vírgula cinco, [p=0.2] é o *complemento:* [p=0.2] a "
        "porcentagem de quem *não* escolheu A. [p=0.4] {a}As letras *A* e *D* [p=0.2] leram três oitavos como três vírgula oito. "
        "[p=0.4] {b}E a *B* [p=0.2] multiplicou três por oito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] fração, [p=0.2] decimal e porcentagem: [p=0.2] três "
        "idiomas do mesmo número. [p=0.5] {b}Dois: [p=0.2] cada quinto vale vinte por cento; [p=0.2] cada oitavo vale doze "
        "vírgula cinco por cento. [p=0.5] {c}Três: [p=0.2] para virar porcentagem, [p=0.2] multiplique o decimal por cem."),

    # ================= A TABELA COMPLETA =================
    dict(id="28", block="tabela", text=
        "{a}E aqui está ela, [p=0.2] *a tabela que vale ouro,* [p=0.2] inteira. [p=0.4] {b}*Tire um print* [p=0.2] e deixe no "
        "celular. [p=0.3] {c}E revise uma família por dia. [p=2.5]"),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.3] {c}caçamos as *pegadinhas* [p=0.3] {d}e treinamos "
        "com *questões novas.* [p=0.4] {e}Te vejo lá."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual família da tabela você já sabia de cabeça? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
