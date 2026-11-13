# Estudativo · QUI-EQL-006 — Solução tampão (Química · Equilíbrio Químico · pH, hidrólise, tampão e Kps).
# Habilidade: explicar como um ácido fraco com seu sal segura o pH, como no sangue, e calcular o pH quando ácido e sal têm a
# mesma concentração.
# Pré-requisitos: QUI-EQL-002, QUI-EQL-005. Próxima: QUI-EQL-007 (produto de solubilidade, Kps).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Leitura: Ka = "cá á", pKa = "pê cá á", HA = "agá á", A⁻ = "o ânion á". Sem Henderson-Hasselbalch: com [A⁻] = [HA], o Ka vira [H⁺].
# Fatos: pH do sangue 7,35–7,45, tampão H₂CO₃/HCO₃⁻; acidose e alcalose; ácido acético Ka ≈ 1,8 × 10⁻⁵ ("perto de 2 × 10⁻⁵")
# ⇒ pH ≈ 4,7 (real 4,74). HCl + NaCl não é tampão (Cl⁻ não captura H⁺). Questão: Ka = 10⁻⁴, iguais ⇒ pH 4.

TITULO = "Solução tampão"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}O pê agá do seu sangue fica entre sete vírgula trinta e cinco e sete vírgula quarenta e cinco. [p=0.3] {b}Você come limão, toma refrigerante, faz exercício, [p=0.1] {c}e ele quase não sai dessa faixa. [p=0.3] {d}Quem segura? [p=0.1] Uma solução tampão."),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}explicar como um ácido fraco com o seu sal segura o pê agá [p=0.2] e {b}calcular o pê agá quando ácido e sal têm a mesma concentração."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar: [p=0.1] {a}o ácido fraco e o seu cá á; [p=0.2] {b}a base conjugada, o que sobra do ácido depois de soltar o agá mais; [p=0.2] {c}e o princípio de Le Chatelier: o equilíbrio foge da perturbação. [p=0.2] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="oque", text="{a}Tampão é a mistura de um ácido fraco com um sal desse mesmo ácido. [p=0.2] {b}Exemplo: o ácido acético, o do vinagre, com o acetato de sódio. [p=0.3] {c}O sal entrega muito acetato, a base conjugada do ácido. [p=0.2] {d}Então a solução tem duas defesas: [p=0.1] {e}o ácido, contra base, [p=0.1] {f}e a base conjugada, contra ácido. [p=0.2] {g}Também vale uma base fraca com um sal dela."),
    # como segura
    dict(id="s05", block="como", text="{a}Pingue um ácido forte. [p=0.1] {b}O agá mais que chegou encontra o acetato [p=0.1] {c}e vira ácido acético, que é fraco e quase não se ioniza. [p=0.2] {d}O agá mais some, e o pê agá quase não muda."),
    dict(id="s06", block="como", text="{a}Pingue uma base forte. [p=0.1] {b}O ó agá menos encontra o ácido acético [p=0.1] {c}e vira água e acetato. [p=0.2] {d}O ó agá menos some, e o pê agá, de novo, quase não muda."),
    dict(id="s07", block="como", text="{a}Pelo Le Chatelier, é a mesma história. [p=0.2] {b}No equilíbrio, o ácido agá á se divide em agá mais e no ânion á. [p=0.2] {c}Chegou agá mais? [p=0.1] Ele vai para a esquerda e consome. [p=0.2] {d}A base levou agá mais embora? [p=0.1] Ele vai para a direita e repõe."),
    dict(id="s08", block="como", text="{a}Mas o tampão tem limite. [p=0.2] {b}Ácido ou base demais esgota as defesas, [p=0.1] {c}e aí o pê agá muda de vez."),
    # o sangue
    dict(id="s09", block="sangue", text="{a}No sangue, o par é o ácido carbônico, agá dois cê ó três, [p=0.1] {b}e o bicarbonato, agá cê ó três menos. [p=0.3] {c}Abaixo de sete vírgula trinta e cinco, o sangue está ácido demais: é a acidose. [p=0.2] Acima de sete vírgula quarenta e cinco, é a alcalose. [p=0.2] {d}Ambas são perigosas."),
    # a conta
    dict(id="s10", block="conta", text="{a}Agora, a conta. [p=0.2] {b}Escreva o cá á: agá mais vezes o ânion á, dividido pelo ácido agá á. [p=0.3] {c}O ânion á vem quase todo do sal; [p=0.1] {d}o ácido agá á, do ácido que quase não se ioniza. [p=0.2] {e}Com ácido e sal na mesma concentração, eles ficam iguais [p=0.1] {f}e se cancelam na fração. [p=0.2] {g}Sobra cá á igual a agá mais."),
    dict(id="s11", block="conta", text="{a}Então o pê agá é o pê cá á: menos o log do cá á. [p=0.3] {b}Com cá á igual a dez elevado a menos cinco, {c}pê agá cinco. [p=0.3] {d}O ácido acético tem cá á perto de dois vezes dez elevado a menos cinco. [p=0.2] O log de dois é zero vírgula três, e o dois na frente tira zero vírgula três do cinco. [p=0.2] {e}Cinco menos zero vírgula três {f}dá pê agá perto de quatro vírgula sete."),
    # erro comum
    dict(id="s12", block="erro", text="{a}O erro comum é achar que todo tampão tem pê agá sete. [p=0.2] {b}Tampão não quer dizer neutro: quer dizer estável. [p=0.3] {c}O de acetato segura o pê agá perto de quatro vírgula sete; [p=0.1] {d}o do sangue, perto de sete vírgula quatro. [p=0.2] No sangue, há bem mais bicarbonato que ácido carbônico, [p=0.1] por isso o pê agá dele não é o pê cá á."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho: [p=0.2] {a}ácido e sal na mesma concentração, pê agá igual a pê cá á. [p=0.2] {b}Com cá á igual a dez elevado a menos um número, o pê agá é esse número. [p=0.3] {c}E, para reconhecer um tampão, procure um ácido fraco junto com um sal do mesmo ácido. [p=0.2] {d}Ácido forte com o seu sal, como o clorídrico com o cloreto de sódio, não é tampão: [p=0.1] {e}o cloreto não segura agá mais."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um tampão tem um ácido fraco com cá á igual a dez elevado a menos quatro [p=0.1] {b}e o sal desse ácido, ambos a zero vírgula um mol por litro. [p=0.3] {c}Qual é o pê agá? [p=0.2] {d}E, se você pingar um pouco de ácido clorídrico, quem consome o agá mais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Mesma concentração: pê agá igual a pê cá á. [p=0.1] {b}Dez elevado a menos quatro dá pê agá quatro. [p=0.3] {c}O agá mais do clorídrico é consumido pela base conjugada, o ânion á do sal, [p=0.1] {d}que vira o ácido fraco, agá á. [p=0.2] {e}O pê agá fica perto de quatro."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}tampão é ácido fraco com o seu sal; [p=0.1] {b}a base conjugada consome ácido, e o ácido consome base; [p=0.2] {c}com as concentrações iguais, pê agá igual a pê cá á."),
    dict(id="s18", block="fim", text="Na próxima aula, o equilíbrio dos sais que quase não se dissolvem: [p=0.1] {a}o produto de solubilidade, cá pê ésse, [p=0.1] {b}e como saber se vai se formar um precipitado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
