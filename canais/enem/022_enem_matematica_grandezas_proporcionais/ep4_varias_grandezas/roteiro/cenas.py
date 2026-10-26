# Roteiro — Grandezas Proporcionais, Episódio 4 de 6: Várias grandezas ao mesmo tempo (como ler qualquer fórmula de Física e Química)
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seções 06 e 09 (+ Questões 7 e 9 da seção 12).
# A energia cinética (quadrática) fica para o episódio 5: aqui, só citada.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A FRAÇÃO-GUIA: o que é direto vai EM CIMA; o que é inverso vai EMBAIXO.
#   Efeitos se MULTIPLICAM, não se somam: o de cima dobra e o de baixo triplica → × 2 e ÷ 3.
#   Toda fórmula de Física é uma frase sobre proporcionalidade: aprenda a lê-la em voz alta.
# Concreto: a mangueira (mais comprida atrapalha o fluxo; mais grossa facilita) → a resistência do fio.
# Exemplo do fio nos blocos (NÃO usa os números da Q7): 6 m, 2 mm², 6 Ω → k = 6 · 2/6 = 2 → 12 m, 3 mm² → 2 · 12/3 = 8 Ω.
#   Pelos efeitos: comprimento × 2, área × 1,5 → 6 × 2 ÷ 1,5 = 8 Ω. Várias mudanças: y = 12, a dobra e b triplica → 12 · 2/3 = 8.
# Fórmulas conferidas: v = d/t · F = m · a · P = U · i (potência elétrica) · P · V = k (Boyle, temperatura constante) ·
#   d = m/V (para o mesmo material, massa e volume são diretas e o k é a densidade) · E = m · v²/2 (só citada).
# Nós fazemos: y = k · a/b, a triplica e b dobra → × 3/2 = 1,5 vez.
# QUESTÃO 7 do material (texto idêntico na tela): R = k · L/A → 5 = k · 10/2 → k = 1 → R = 30/3 = 10 Ω → C.
#   Pelos efeitos: 5 · 3 ÷ 1,5 = 10. Explicações NOSSAS (o material não explica as erradas):
#   A (5) = achou que os efeitos se anulam ("tudo cresceu, nada muda") · B (7,5) = SOMOU os efeitos: 5 · (3 − 1,5) ·
#   D (15) = esqueceu a área (só triplicou) · E (45) = pôs a área em cima e ainda leu 3 mm² como "triplicou": 5 · 3 · 3.
# QUESTÃO 9 do material (texto idêntico): P · V constante → 2 · 6 = 12 = 3 · V → V = 4 L → C. Pelos efeitos: pressão × 1,5 →
#   volume ÷ 1,5 → 6 ÷ 1,5 = 4. Material: D e E dão volumes MAIORES e caem pelo bom senso (comprimir diminui o volume).
#   Explicações NOSSAS: D (9) = tratou como direta, 6 · 3/2 · E (12) = parou no k (12 é o produto, não o volume) ·
#   A (2) = dividiu os 6 L pela nova pressão · B (3) = dividiu os 6 L pela pressão antiga.
# Frases-chave (meio e fim, idênticas): 1. Direto em cima, inverso embaixo. 2. Várias mudanças? Multiplique os efeitos.
#   3. Toda fórmula é uma frase sobre proporção.
# Atalhos (verde): "aumenta o resultado? em cima. diminui? embaixo" ·
#   "cada mudança vira um fator: multiplique os fatores" · "leia a fração: em cima direto, embaixo inverso" ·
#   "comprimiu? o volume TEM de diminuir".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Várias grandezas ao mesmo tempo: leia fórmulas de Física e Química | Grandezas Proporcionais Ep. 4"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática e de Física: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
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
    # ================= GANCHO E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Metade das fórmulas de *Física* e *Química* do ENEM [p=0.2] é uma *frase sobre proporcionalidade.* [p=0.5] "
        "{b}Quem aprende a ler essas frases [p=0.3] {c}para de *decorar* [p=0.3] {d}e passa a *raciocinar.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *montar a fórmula* a partir de um enunciado, [p=0.4] {b}e saber o que "
        "acontece quando *várias grandezas mudam ao mesmo tempo.* [p=0.4] {c}Sem medo de fórmula: [p=0.2] a gente vai *ler* cada uma."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}O *k,* do episódio um: [p=0.2] o número que não muda. [p=0.3] Na direta, "
        "[p=0.2] y é igual a k vezes x. [p=0.3] Na inversa, [p=0.2] y é igual a k dividido por x. [p=0.5] {b}E da série de "
        "Frações: [p=0.2] multiplicar por *dois terços* [p=0.2] é multiplicar por dois [p=0.2] e dividir por três."),

    # ================= CONCRETO: A MANGUEIRA =================
    dict(id="04", block="mangueira", text=
        "{t}Pense numa *mangueira* de jardim. [p=0.3] {a}*Mais comprida:* [p=0.2] a água tem mais caminho, [p=0.2] o comprimento *atrapalha.* [p=0.4] {b}*Mais grossa:* [p=0.2] a água passa com folga, [p=0.2] a grossura *facilita.* [p=0.4] {c}Duas causas, [p=0.2] puxando para lados contrários. [p=0.3] Como colocar as duas numa conta só?"),

    # ================= BLOCO A: A FRAÇÃO-GUIA =================
    dict(id="05", block="guia", text=
        "{t}Com uma *fração-guia.* [p=0.3] {a}Uma fração tem dois andares. [p=0.2] O de cima é o *numerador;* [p=0.2] o de "
        "baixo, [p=0.2] o *denominador.* [p=0.4] {b}A regra é uma só: [p=0.2] o que é *direto* sobe para o andar de *cima.* "
        "[p=0.4] {c}O que é *inverso* desce para o andar de *baixo.* [p=0.4] {d}E o k fica na frente: [p=0.2] *y é igual a k "
        "vezes a sobre b.*"),
    dict(id="06", block="guia", text=
        "{t}Por que funciona? [p=0.3] {a}Se o *a,* lá em cima, dobra, [p=0.2] a fração inteira dobra: [p=0.2] *direta.* "
        "[p=0.4] {b}Se o *b,* lá embaixo, dobra, [p=0.2] a fração cai à "
        "*metade:* [p=0.2] *inversa.* [p=0.4] {c}Atalho: [p=0.2] pergunte se a grandeza *aumenta* ou *diminui* o resultado. "
        "[p=0.3] Aumenta? [p=0.2] Em cima. [p=0.2] Diminui? [p=0.2] Embaixo."),

    # ================= BLOCO B: O FIO CONDUTOR =================
    dict(id="07", block="fio", text=
        "{t}Agora troque a mangueira por um *fio elétrico.* [p=0.3] {a}A *resistência elétrica* [p=0.2] é o quanto o fio "
        "*atrapalha* a passagem da eletricidade. [p=0.4] {b}Fio *mais comprido:* [p=0.2] atrapalha mais. [p=0.2] O "
        "comprimento é *direto.* [p=0.4] {c}Fio *mais grosso:* [p=0.2] atrapalha menos. [p=0.4] {d}A grossura se mede pela "
        "*área da seção transversal:* [p=0.2] o tamanho da *boca* do fio, [p=0.2] se você cortar ele ao meio. [p=0.3] Essa "
        "área é *inversa.*"),
    dict(id="08", block="fio", text=
        "{t}Fração-guia: [p=0.2] {a}comprimento em cima, [p=0.2] área embaixo. [p=0.3] *R é igual a k vezes L sobre A.* "
        "[p=0.4] {b}E essa é *exatamente* a fórmula que aparece na Física: [p=0.2] *R igual a rô vezes L sobre A.* [p=0.4] "
        "{c}O *rô* é a *resistividade:* [p=0.2] o quanto o *material* atrapalha. [p=0.3] {d}Ou seja: [p=0.2] o rô é o nosso k, [p=0.2] com outro nome."),
    dict(id="09", block="fio", text=
        "{t}Vamos usar. [p=0.3] {a}Um fio de *seis metros* e *dois milímetros quadrados* de seção [p=0.2] tem resistência de "
        "*seis ohms.* [p=0.4] {b}Achando o k: [p=0.2] seis é igual a k vezes seis sobre dois, [p=0.2] ou seja, [p=0.2] k vezes "
        "três. [p=0.3] *k igual a dois.* [p=0.4] {c}Outro fio, do mesmo material: [p=0.2] *doze metros* e *três milímetros "
        "quadrados.* [p=0.3] {d}Dois vezes doze sobre três: [p=0.2] dois vezes quatro, [p=0.2] *oito ohms.*"),
    dict(id="10", block="fio", text=
        "{t}Agora o *segundo caminho,* [p=0.2] sem calcular o k. [p=0.3] {a}O comprimento foi de seis para doze: [p=0.2] "
        "*dobrou.* [p=0.2] Está em cima: [p=0.2] *vezes dois.* [p=0.4] {b}A área foi de dois para três: [p=0.2] *uma vez e "
        "meia.* [p=0.2] Está embaixo: [p=0.2] *dividido por um vírgula cinco.* [p=0.4] {c}Seis vezes dois, [p=0.2] doze. "
        "[p=0.2] Dividido por um vírgula cinco, [p=0.2] *oito ohms.* [p=0.3] O mesmo resultado. [p=0.4] {d}Atalho: [p=0.2] "
        "*cada mudança vira um fator,* [p=0.2] e você multiplica os fatores."),

    # ================= BLOCO C: VÁRIAS MUDANÇAS AO MESMO TEMPO =================
    dict(id="11", block="efeitos", text=
        "{t}E se tudo muda ao mesmo tempo? [p=0.3] {a}Na fórmula y igual a k vezes a sobre b, [p=0.2] o *a dobra* [p=0.2] e o "
        "*b triplica.* [p=0.4] {b}Aplique *uma mudança de cada vez.* [p=0.3] O a dobrou, em cima: [p=0.2] *vezes dois.* "
        "[p=0.3] O b triplicou, embaixo: [p=0.2] *dividido por três.* [p=0.4] {c}Juntando: [p=0.2] vezes dois terços. "
        "[p=0.3] {d}Se o y valia *doze,* [p=0.2] passa a valer doze vezes dois terços: [p=0.2] *oito.*"),
    dict(id="12", block="efeitos", text=
        "{t}E repare na palavra: [p=0.2] *multiplicar.* [p=0.4] {a}Os efeitos se *multiplicam,* [p=0.2] não se *somam.* "
        "[p=0.4] {b}Vezes dois e dividido por três não é *dois menos três.* [p=0.3] São duas ações, [p=0.2] uma depois da "
        "outra. [p=0.4] {c}Como uma receita que você dobra [p=0.2] e depois divide em três potes."),

    # ================= BLOCO D: A TABELA DAS FÓRMULAS =================
    dict(id="13", block="formulas", text=
        "{t}Agora, as fórmulas que mais caem, [p=0.2] lidas *em voz alta.* [p=0.4] {a}*Velocidade é distância sobre "
        "tempo.* [p=0.3] {b}Distância em cima: [p=0.2] mais distância no mesmo tempo, [p=0.2] mais velocidade. [p=0.2] "
        "*Direta.* [p=0.3] {c}Tempo embaixo: [p=0.2] mais tempo para a mesma distância, [p=0.2] menos velocidade. [p=0.2] "
        "*Inversa.*"),
    dict(id="14", block="formulas", text=
        "{a}*Força é massa vezes aceleração.* [p=0.3] Tudo em cima: [p=0.2] "
        "a força é *direta* às duas. [p=0.4] {b}*Potência elétrica é tensão vezes corrente.* [p=0.3] A *tensão* é o empurrão "
        "que a tomada dá; [p=0.2] a *corrente,* [p=0.2] quanto de eletricidade passa. [p=0.3] {c}Também tudo em cima: [p=0.2] "
        "*direta* às duas."),
    dict(id="15", block="boyle", text=
        "{t}Na Química, [p=0.2] a *lei de Boyle.* [p=0.3] {a}Uma seringa tampada, [p=0.2] cheia de ar. [p=0.3] "
        "{b}Você empurra o êmbolo: [p=0.2] aumenta a *pressão,* [p=0.2] que é a força apertando cada pedacinho do gás. "
        "[p=0.3] {c}E o *volume* diminui. [p=0.4] {d}Com a temperatura constante, [p=0.2] *pressão vezes volume dá sempre o "
        "mesmo k.* [p=0.3] Produto constante: [p=0.2] *inversa.*"),
    dict(id="16", block="formulas", text=
        "{a}E a *densidade:* [p=0.2] *massa sobre volume.* [p=0.3] Para o mesmo material, [p=0.2] o dobro de volume tem o "
        "dobro de massa: [p=0.2] massa e volume são *diretas,* [p=0.2] e o k é a própria densidade. [p=0.5] {b}E a *energia "
        "cinética,* [p=0.2] a energia do movimento: [p=0.2] *massa vezes velocidade ao quadrado, sobre dois.* [p=0.4] {c}Essa "
        "tem um *quadrado:* [p=0.3] é o próximo episódio."),

    # ================= BLOCO E: A LEITURA RÁPIDA =================
    dict(id="17", block="leitura", text=
        "{t}Percebeu o padrão? [p=0.3] {a}Numa fração, [p=0.2] o que está *em cima* é *direto.* [p=0.3] {b}O que está "
        "*embaixo* é *inverso.* [p=0.4] {c}Sem decorar nada, [p=0.2] você já sabe o que acontece se uma grandeza dobrar. "
        "[p=0.4] {d}E é *isso* que o ENEM pergunta."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Na fórmula *y igual a k vezes a sobre b,* [p=0.3] {b}o *a triplica* [p=0.2] e o *b dobra.* "
        "[p=0.4] {c}O que acontece com o y? [p=0.4] {d}*Pause o vídeo e pense.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O a está em cima e triplicou: [p=0.2] *vezes três.* [p=0.4] {b}O b está embaixo e "
        "dobrou: [p=0.2] *dividido por dois.* [p=0.4] {c}Juntando: [p=0.2] vezes três meios, [p=0.2] ou seja, [p=0.2] o y "
        "fica *uma vez e meia* maior."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] direto em cima, [p=0.2] inverso embaixo. [p=0.5] {b}Dois: "
        "[p=0.2] várias mudanças? [p=0.2] Multiplique os efeitos. [p=0.5] {c}Três: [p=0.2] toda fórmula é uma frase sobre "
        "proporção."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar* os efeitos em vez de multiplicar. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque são várias mudanças, [p=0.2] e somar parece juntar tudo. [p=0.4] {c}Mas cada mudança "
        "age sobre o resultado da anterior: [p=0.2] *vezes um, dividido pelo outro.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] colocar a grandeza *inversa no numerador.* [p=0.4] {b}Parece certo, [p=0.2] porque ela também "
        "aparece no enunciado, [p=0.2] e a gente escreve na ordem em que lê. [p=0.4] {c}Mas o que *diminui* o resultado vai "
        "*embaixo.* [p=0.3] Sempre."),
    dict(id="23", block="erros", text=
        "{a}Terceiro, na lei de Boyle: [p=0.2] achar que o volume *aumenta* quando a pressão aumenta. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque os dois números crescem juntos em muita fórmula. [p=0.4] {c}Mas use o bom senso: [p=0.2] *comprimir* "
        "um gás [p=0.2] diminui o espaço que ele ocupa. [p=0.3] Mais pressão, [p=0.2] *menos* volume."),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="24", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}A resistência elétrica de um "
        "fio é diretamente proporcional ao seu comprimento [p=0.2] e inversamente proporcional à área de sua seção "
        "transversal. [p=0.4] {b}Um fio de *dez metros* de comprimento [p=0.2] e *dois milímetros quadrados* de seção [p=0.2] "
        "tem resistência de *cinco ohms.* [p=0.4] {c}Outro fio, do mesmo material, [p=0.2] com *trinta metros* de comprimento "
        "[p=0.2] e *três milímetros quadrados* de seção, [p=0.2] terá resistência de: [p=0.4] {qa}A: [p=0.2] cinco ohms. "
        "[p=0.3] {qb}B: [p=0.2] sete vírgula cinco. [p=0.3] {qc}C: [p=0.2] dez. [p=0.3] {qd}D: [p=0.2] quinze. [p=0.3] "
        "{qe}E: [p=0.2] quarenta e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q7", text=
        "{t}Vamos resolver, [p=0.2] pelos dois caminhos. [p=0.3] {a}Fração-guia: [p=0.2] comprimento em cima, [p=0.2] área "
        "embaixo. [p=0.2] *R igual a k vezes L sobre A.* [p=0.4] {b}Primeiro fio: [p=0.2] cinco é igual a k vezes dez sobre "
        "dois, [p=0.2] que é k vezes cinco. [p=0.3] *k igual a um.* [p=0.4] {c}Segundo fio: [p=0.2] um vezes trinta sobre três, "
        "[p=0.2] *dez ohms.* [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q7", text=
        "{t}Pelos efeitos: [p=0.2] {a}o comprimento foi de dez para trinta, [p=0.2] *vezes três.* [p=0.3] {b}A área foi de "
        "dois para três, [p=0.2] *dividido por um vírgula cinco.* [p=0.3] {c}Cinco vezes três, [p=0.2] quinze, [p=0.2] "
        "dividido por um vírgula cinco, [p=0.2] *dez.* [p=0.4] {d}Bom senso: [p=0.2] bem mais comprido, [p=0.2] pouco mais grosso: [p=0.2] tinha que *subir.*"),
    dict(id="27", block="q7", text=
        "{t}E as outras? [p=0.3] {xd}A D esqueceu a área: [p=0.2] só triplicou. [p=0.4] {xb}A B *somou* os efeitos: [p=0.2] "
        "fez três menos um vírgula cinco. [p=0.4] {xe}A E pôs a área *em cima,* [p=0.2] e ainda leu os três milímetros como se "
        "a área tivesse triplicado. [p=0.4] {xa}E a A achou que os efeitos se anulam."),

    # ================= QUESTÃO 9 DO MATERIAL =================
    dict(id="28", block="q9", text=
        "{t}Mais uma do material, [p=0.2] agora de Química. [p=0.3] {a}A uma temperatura constante, [p=0.2] o volume ocupado "
        "por certa massa de gás [p=0.2] é inversamente proporcional à pressão exercida sobre ele. [p=0.4] {b}Um gás ocupa *seis "
        "litros* [p=0.2] sob pressão de *duas atmosferas.* [p=0.4] {c}Ao ser comprimido até a pressão de *três atmosferas,* "
        "[p=0.2] mantida a temperatura, [p=0.2] esse gás passará a ocupar: [p=0.4] {qa}A: [p=0.2] dois litros. [p=0.3] {qb}B: "
        "[p=0.2] três litros. [p=0.3] {qc}C: [p=0.2] quatro litros. [p=0.3] {qd}D: [p=0.2] nove litros. [p=0.3] {qe}E: "
        "[p=0.2] doze litros. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Primeiro, o *bom senso:* [p=0.2] {a}o gás foi *comprimido,* [p=0.2] o volume tem que *diminuir.* [p=0.3] {b}Nove e doze litros já caem. [p=0.4] {c}Agora o k: [p=0.2] inversa, [p=0.2] produto constante. "
        "[p=0.2] Duas vezes seis, [p=0.2] *doze.* [p=0.4] {d}Três vezes o volume dá doze: [p=0.2] *quatro litros.* [p=0.3] "
        "{ok}*Letra C!* [p=0.4] {e}Pelos efeitos: [p=0.2] a pressão subiu uma vez e meia; [p=0.2] o volume cai uma vez e meia. "
        "[p=0.2] Seis dividido por um vírgula cinco, [p=0.2] *quatro.*"),
    dict(id="30", block="q9", text=
        "{t}E as outras? [p=0.3] {xd}A D tratou como *direta:* [p=0.2] o volume cresceu junto com a pressão. [p=0.4] {xe}A E "
        "*parou no k:* [p=0.2] doze é o produto, [p=0.2] não o volume. [p=0.4] {xa}A A dividiu os seis litros pela pressão "
        "nova, [p=0.3] {xb}e a B, [p=0.2] pela antiga."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] direto em cima, [p=0.2] inverso embaixo. [p=0.5] "
        "{b}Dois: [p=0.2] várias mudanças? [p=0.2] Multiplique os efeitos. [p=0.5] {c}Três: [p=0.2] toda fórmula é uma frase "
        "sobre proporção."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}E quando a fórmula tem um *quadrado,* [p=0.2] como na *área,* [p=0.2] na *energia* [p=0.2] ou na *luz de uma "
        "lâmpada?* [p=0.4] {b}Aí *dobrar não dobra,* [p=0.3] e é aí que se erra. [p=0.4] {c}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual fórmula de Física você vai ler em voz alta primeiro? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
