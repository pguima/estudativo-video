# Estudativo · QUI-CAL-006 — Reagente limitante e excesso (Química · Cálculos Químicos · Estequiometria).
# Habilidade: descobrir que, com 10 g de H₂ e 64 g de O₂, o oxigênio limita a reação, sobram 2 g de hidrogênio e formam-se
# 72 g de água. Pré-requisitos: QUI-CAL-005. Próxima: QUI-CAL-007 (pureza dos reagentes).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: 2 H₂ + O₂ → 2 H₂O = 4 g : 32 g : 36 g; 64 g O₂ pede 8 g H₂; 10 − 8 = 2 g sobram; água 2·36 = 72 g = 8 + 64.
# Atalho: 10/4 = 2,5 e 64/32 = 2 → O₂ limita. Questão: N₂ + 3 H₂ → 2 NH₃ (28 : 6 : 34); 28 g N₂ e 9 g H₂: 28/28 = 1,
# 9/6 = 1,5 → N₂ limita; gasta 6 g H₂, sobram 3 g; forma 34 g NH₃. Sanduíche: 10 pães e 3 queijos, 2 pães + 1 queijo.

TITULO = "Reagente limitante e excesso"

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
    dict(id="s01", block="gancho", text="{a}Cada sanduíche leva dois pães e uma fatia de queijo. [p=0.3] {b}Você tem dez pães e três fatias. [p=0.2] {c}Quantos sanduíches saem? [p=0.3] {d}Três. [p=0.2] O queijo acaba primeiro, {e}e sobram quatro pães. [p=0.3] {f}Numa reação química, acontece a mesma coisa."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai descobrir {b}qual reagente limita a reação, [p=0.2] {c}quanto sobra do outro [p=0.1] e {d}quanto produto se forma, [p=0.2] com um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa: [p=0.2] {b}a conta de massa para massa, com as massas escritas embaixo da equação. [p=0.3] Se faltar, procure no canal."),
    # conceito
    dict(id="s04", block="conceito", text="{a}Reagente limitante é o que acaba primeiro e faz a reação parar. [p=0.2] {b}O outro está em excesso: [p=0.1] parte dele sobra, sem reagir. [p=0.3] {c}O produto é sempre calculado pelo limitante."),
    # exemplo
    dict(id="s05", block="exemplo", text="{a}Dez gramas de agá dois e sessenta e quatro gramas de ó dois [p=0.1] reagem para formar água. [p=0.3] {b}A equação: dois agá dois mais ó dois forma dois agá dois ó. [p=0.2] {c}Embaixo, quatro gramas de hidrogênio, [p=0.1] {d}trinta e dois de oxigênio [p=0.1] {e}e trinta e seis de água."),
    dict(id="s06", block="exemplo", text="{a}Teste o oxigênio. [p=0.2] {b}Trinta e dois gramas de ó dois pedem quatro de agá dois. [p=0.2] {c}Sessenta e quatro é o dobro, então pedem oito gramas. [p=0.3] {d}Você tem dez gramas de hidrogênio: [p=0.1] {e}dá e sobra."),
    dict(id="s07", block="exemplo", text="{a}Então quem acaba primeiro é o oxigênio: [p=0.1] {b}ele é o limitante. [p=0.2] {c}O hidrogênio está em excesso: [p=0.1] {d}dez menos oito dá dois gramas que sobram."),
    dict(id="s08", block="exemplo", text="{a}A água sai pelo limitante. [p=0.2] {b}Trinta e dois gramas de oxigênio dão trinta e seis de água. [p=0.2] {c}Sessenta e quatro, o dobro: [p=0.1] {d}setenta e dois gramas. [p=0.3] {e}Confira: oito mais sessenta e quatro dá setenta e dois."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}achar que o limitante é o reagente de menor massa. [p=0.3] {b}Dez gramas é bem menos que sessenta e quatro, [p=0.1] e a pessoa calcula a água pelo hidrogênio: [p=0.1] {c}noventa gramas. [p=0.2] Mais do que os setenta e quatro gramas que entraram: impossível. [p=0.3] {d}Quem decide é a proporção da equação, não a massa sozinha."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho: [p=0.1] {a}divida a massa que você tem pela massa embaixo da equação. [p=0.3] {b}Hidrogênio: dez dividido por quatro dá dois e meio. [p=0.2] {c}Oxigênio: sessenta e quatro dividido por trinta e dois dá dois. [p=0.3] {d}O menor resultado é o limitante: o oxigênio."),
    dict(id="s11", block="atalho", text="{a}Funciona porque cada divisão conta quantas vezes a receita da equação cabe naquele reagente. [p=0.3] {b}O oxigênio dá para duas receitas, [p=0.1] o hidrogênio para duas e meia. [p=0.2] {c}A reação termina em duas. [p=0.3] {d}Não compensa se a prova já diz quem está em excesso: [p=0.1] aí, calcule direto pelo outro."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Na fabricação da amônia, {a}ene dois mais três agá dois forma dois ene agá três. [p=0.3] {b}Embaixo da equação ficam vinte e oito gramas de ene dois, [p=0.1] seis de agá dois e trinta e quatro de amônia. [p=0.3] {c}Misturam-se vinte e oito gramas de ene dois com nove de agá dois. [p=0.2] {d}Quem limita, quanto sobra e quanta amônia se forma?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Nitrogênio: vinte e oito dividido por vinte e oito dá um. [p=0.2] {b}Hidrogênio: nove dividido por seis dá um e meio. [p=0.3] {c}O menor é o do nitrogênio: ele limita. [p=0.3] {d}Uma receita gasta seis gramas de hidrogênio: [p=0.1] {e}nove menos seis dá três gramas que sobram. [p=0.2] {f}E formam-se trinta e quatro gramas de amônia."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}divida cada massa pela massa da equação; [p=0.1] {b}o menor resultado é o limitante; [p=0.2] {c}e o produto se calcula sempre por ele."),
    dict(id="s16", block="fim", text="Na próxima aula, o reagente vem {a}com impurezas, [p=0.2] como o calcário, que nunca é só carbonato de cálcio, [p=0.1] e você aprende a {b}descontar a parte que não reage. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
