# Estudativo · MAT-EXP-003 — Tempo de duplicação e meia-vida (Matemática · Exponencial e Logaritmo).
# Habilidade: calcular quanto resta de 80 mg após 3 meias-vidas e usar Q = Q₀ · 2^(t/T) com bactérias que dobram a cada 20 minutos.
# Pré-requisitos: MAT-EXP-002 (crescimento e decaimento). Próxima: MAT-EXP-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Material da questão é fictício.

TITULO = "Tempo de duplicação e meia-vida"

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
    dict(id="s01", block="gancho", text="Uma dose de {a}oitenta miligramas de remédio. [p=0.2] A cada seis horas, {b}metade sai do corpo. [p=0.3] Muita gente pensa: metade de oitenta é quarenta. [p=0.2] {c}Tira quarenta, tira quarenta de novo, [p=0.2] e em doze horas {d}acabou."),
    dict(id="s02", block="gancho", text="Mas em doze horas ainda sobram {a}vinte miligramas. [p=0.3] {b}Até o fim desta aula, você calcula quanto resta e quanto cresce, contando metades e dobras, [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de uma coisa: [p=0.2] {a}a lei do crescimento que multiplica, [p=0.2] {b}quantidade inicial vezes o fator elevado ao tempo. [p=0.3] Se faltar, procure no canal."),
    # meia-vida
    dict(id="s04", block="meiavida", text="O tempo que uma quantidade leva para {a}cair pela metade se chama {b}meia-vida. [p=0.3] Nesse remédio, a meia-vida é de {c}seis horas."),
    dict(id="s05", block="meiavida", text="Cada meia-vida corta pela metade {a}o que sobrou, e não a dose inicial. [p=0.3] {b}Oitenta. [p=0.2] Seis horas depois, {c}quarenta. [p=0.2] Mais seis horas, e restam {d}vinte. [p=0.2] Mais seis horas, e restam {e}dez miligramas. [p=0.3] Em doze horas, sobram vinte. [p=0.2] Não zero. [p=0.2] E nunca chega a zero: sempre resta a metade de alguma coisa."),
    dict(id="s06", block="meiavida", text="Em conta: cada meia-vida multiplica por {a}um meio. [p=0.2] Três meias-vidas: {b}oitenta vezes um meio ao cubo. [p=0.2] Um meio ao cubo é {c}um oitavo, [p=0.2] e {d}oitenta dividido por oito dá dez."),
    # duplicação
    dict(id="s07", block="dobra", text="O caminho contrário é o {a}tempo de duplicação: o tempo que leva para dobrar. [p=0.3] Uma colônia começa com {b}quinhentas bactérias e dobra a cada {c}vinte minutos."),
    dict(id="s08", block="dobra", text="Em uma hora, quantas vezes ela dobrou? [p=0.2] {a}Sessenta dividido por vinte dá três. [p=0.3] Então são {b}quinhentas vezes dois ao cubo. [p=0.2] {c}Quinhentos vezes oito dá quatro mil bactérias."),
    # fórmula
    dict(id="s09", block="formula", text="Daí sai a fórmula: {a}quê igual a quê zero vezes dois elevado a tê dividido por tê maiúsculo, com a divisão toda no expoente. [p=0.3] {b}Quê zero é a quantidade inicial. [p=0.2] {c}Tê minúsculo é o tempo que passou. [p=0.2] {d}Tê maiúsculo é o tempo de uma duplicação. [p=0.3] E {e}tê dividido por tê maiúsculo conta quantas vezes dobrou."),
    dict(id="s10", block="formula", text="Em duas horas, são {a}cento e vinte minutos. [p=0.2] {b}Cento e vinte dividido por vinte dá seis. [p=0.2] {c}Dois elevado a seis dá sessenta e quatro. [p=0.2] {d}Quinhentos vezes sessenta e quatro dá trinta e dois mil bactérias."),
    dict(id="s11", block="formula", text="Para a meia-vida, é a mesma fórmula com {a}um meio no lugar do dois, [p=0.2] e tê maiúsculo passa a ser {b}a meia-vida. [p=0.3] No remédio, {c}dezoito horas dividido por seis dá três: as mesmas três metades."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com um erro muito comum: {a}misturar unidades. [p=0.2] Duas horas de colônia, com duplicação de vinte minutos. [p=0.2] A pessoa faz {b}dois dividido por vinte, [p=0.2] e acha que a colônia dobrou {c}só um décimo de vez em duas horas."),
    dict(id="s13", block="erro", text="O tempo e o tempo de duplicação precisam estar {a}na mesma unidade. [p=0.2] Duas horas são cento e vinte minutos, [p=0.2] e {b}cento e vinte dividido por vinte dá seis dobras."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}dez dobras multiplicam por cerca de mil. [p=0.3] Em duzentos minutos, a colônia dobra {b}dez vezes. [p=0.2] Quinhentas bactérias viram {c}cerca de quinhentas mil. [p=0.3] E depois de dez meias-vidas, sobra {d}cerca de um milésimo: [p=0.2] de mil miligramas de remédio, resta cerca de um miligrama."),
    dict(id="s15", block="atalho", text="Funciona porque {a}dois elevado a dez dá mil e vinte e quatro, quase mil. [p=0.3] Não compensa quando a prova pede o valor exato: [p=0.2] aí, são {b}quinhentas e doze mil bactérias."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar, com um material inventado para esta aula. [p=0.2] Ele tem meia-vida de {a}cinco anos, e a amostra tem {b}cento e sessenta gramas. [p=0.3] {c}Quanto resta depois de vinte anos? [p=0.2] {d}E depois de quantos anos restam cinco gramas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Vinte dividido por cinco dá quatro meias-vidas. [p=0.2] Um meio elevado a quatro é {b}um dezesseis avos. [p=0.2] {c}Cento e sessenta dividido por dezesseis dá dez gramas."),
    dict(id="s19", block="resposta", text="Para os cinco gramas, conte as metades. [p=0.2] {a}Cento e sessenta. [p=0.1] Oitenta. [p=0.1] Quarenta. [p=0.1] Vinte. [p=0.1] Dez. [p=0.1] Cinco. [p=0.3] Foram {b}cinco meias-vidas. [p=0.2] {c}Cinco vezes cinco anos dá vinte e cinco anos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}divida o tempo pelo tempo de dobrar ou de cair pela metade, [p=0.2] e {b}esse número vai no expoente."),
    dict(id="s21", block="fim", text="Na última pergunta, o número procurado estava no expoente. [p=0.2] Na próxima aula, isso vira equação: [p=0.2] {a}dois elevado a xis mais um, com o xis mais um todo no expoente, igual a trinta e dois. [p=0.3] Você resolve {b}escrevendo tudo na mesma base. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
