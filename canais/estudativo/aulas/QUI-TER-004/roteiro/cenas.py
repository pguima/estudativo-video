# Estudativo · QUI-TER-004 — Velocidade média de uma reação (Química · Termoquímica e Cinética · Cinética química).
# Habilidade: calcular a velocidade média de uma reação em mol/L por minuto a partir de uma tabela ou de um gráfico.
# Pré-requisitos: QUI-SOL-004, QUI-INO-008, MAT-RAZ-015. Próxima: QUI-TER-005 (colisões e fatores da velocidade).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso ("zero vírgula zero três"). Questão inédita, criada para esta aula.
# Primeira aula de Cinética: o cabeçalho do visual.py guarda a linguagem visual da trilha (tabela de tempo, gráfico de concentração).
# Dados ilustrativos (criados para a aula, coerentes com a estequiometria): 2 H₂O₂ → 2 H₂O + O₂; [H₂O₂] = 0,80 / 0,50 / 0,30 / 0,20
# mol/L em 0 / 10 / 20 / 30 min; [O₂] = 0 / 0,15 / 0,25 / 0,30. v(0–10) = 0,030; v(10–20) = 0,020; v(20–30) = 0,010.
# Fato: a água oxigenada se decompõe sozinha, devagar, e o ritmo cai com o tempo (cinética de primeira ordem).

TITULO = "Velocidade média de uma reação"

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
    dict(id="s01", block="gancho", text="{a}A água oxigenada do armário vira água e gás oxigênio sozinha, bem devagar. [p=0.3] {b}E ela não se decompõe sempre no mesmo ritmo: [p=0.1] {c}começa mais rápido e vai desacelerando. [p=0.3] {d}Como medir a rapidez de uma reação que muda o tempo todo?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai calcular {a}a velocidade média de uma reação, em mol por litro por minuto, [p=0.2] {b}a partir de uma tabela [p=0.1] {c}ou de um gráfico."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar duas ideias. [p=0.2] {a}Concentração em mol por litro: quantos mols há em cada litro. [p=0.2] {b}E velocidade média: quanto mudou, dividido pelo tempo que levou. [p=0.1] {c}Cento e oitenta quilômetros em duas horas dá noventa quilômetros por hora. [p=0.2] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Na reação é igual, só que {a}o que muda é a concentração. [p=0.2] {b}Os reagentes vão sumindo, [p=0.1] {c}os produtos vão aparecendo. [p=0.3] {d}A velocidade média é quanto a concentração mudou, dividido pelo tempo."),
    dict(id="s05", block="ideia", text="{a}Na fórmula, a concentração vem entre colchetes, esses sinais quadrados. [p=0.2] {b}Agá dois ó dois entre colchetes se lê: concentração da água oxigenada. [p=0.3] {c}A velocidade média é a variação da concentração dividida pela variação do tempo. [p=0.2] {d}Ela é sempre positiva: [p=0.1] você usa quanto mudou, sem sinal."),
    # tabela
    dict(id="s06", block="tabela", text="Veja a água oxigenada se decompondo. [p=0.2] {a}No minuto zero, há zero vírgula oito mol por litro. [p=0.1] {b}No minuto dez, zero vírgula cinco. [p=0.1] {c}No vinte, zero vírgula três. [p=0.1] {d}No trinta, zero vírgula dois."),
    dict(id="s07", block="tabela", text="{a}Do minuto zero ao dez, caiu de zero vírgula oito para zero vírgula cinco: [p=0.1] {b}uma queda de zero vírgula três. [p=0.3] {c}Zero vírgula três dividido por dez minutos {d}dá zero vírgula zero três mol por litro por minuto."),
    dict(id="s08", block="tabela", text="{a}Do dez ao vinte, caiu zero vírgula dois: [p=0.1] {b}dá zero vírgula zero dois mol por litro por minuto. [p=0.2] {c}Do vinte ao trinta, dá zero vírgula zero um. [p=0.3] {d}A velocidade cai: é a desaceleração do começo da aula. [p=0.2] O motivo você entende na próxima aula."),
    # gráfico
    dict(id="s09", block="grafico", text="{a}No gráfico, a conta é a mesma. [p=0.2] {b}O eixo deitado é o tempo; [p=0.1] {c}o de pé, a concentração. [p=0.2] {d}A curva do reagente desce; [p=0.1] {e}a do produto sobe. [p=0.3] {f}Leia dois pontos, veja quanto mudou e divida pelo tempo entre eles."),
    dict(id="s10", block="grafico", text="{a}Olhe o gás oxigênio, a curva que sobe. [p=0.2] {b}Nos dez primeiros minutos, ele vai de zero a zero vírgula quinze: [p=0.1] {c}dá zero vírgula zero quinze por minuto, [p=0.1] {d}a metade da velocidade da água oxigenada. [p=0.2] Por quê?"),
    # coeficientes
    dict(id="s11", block="coef", text="{a}Olhe a equação balanceada: [p=0.1] dois agá dois ó dois formam dois agá dois ó mais ó dois. [p=0.3] {b}Para cada duas moléculas de água oxigenada que somem, nasce uma de ó dois. [p=0.2] {c}As velocidades seguem os coeficientes."),
    dict(id="s12", block="coef", text="{a}Para ter um número só, a velocidade da reação, [p=0.1] divida a velocidade de cada substância pelo seu coeficiente. [p=0.2] {b}Zero vírgula zero três dividido por dois {c}dá zero vírgula zero quinze. [p=0.2] {d}O mesmo valor sai para todas as substâncias."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro comum é dividir pelo minuto final, e não pelo intervalo. [p=0.2] {b}Do dez ao vinte, a queda foi zero vírgula dois. [p=0.1] {c}Quem divide por vinte acha zero vírgula zero um. [p=0.2] {d}Mas passaram só dez minutos: [p=0.1] {e}o certo é zero vírgula zero dois."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho: [p=0.2] {a}achou a velocidade de uma substância, achou a de todas. [p=0.2] {b}Multiplique pelo coeficiente da que você quer, dividido pelo da que você tem. [p=0.2] {c}A água oxigenada some a zero vírgula zero três. [p=0.1] {d}Para o ó dois, vezes um meio: [p=0.1] {e}zero vírgula zero quinze. [p=0.3] {f}E deixe a unidade guiar: mol por litro dividido por minuto dá mol por litro por minuto."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a equação balanceada fixa a proporção entre o que some e o que aparece. [p=0.2] {b}Por isso, não vale com a equação sem balancear: [p=0.1] {c}balanceie antes."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Na produção da amônia, ene dois mais três agá dois formam dois ene agá três. [p=0.3] {b}Em cinco minutos, a amônia vai de zero a zero vírgula quatro mol por litro. [p=0.3] {c}Qual a velocidade média de formação da amônia? [p=0.2] {d}A de consumo do agá dois? [p=0.2] E a da reação?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}Amônia: zero vírgula quatro dividido por cinco {b}dá zero vírgula zero oito mol por litro por minuto. [p=0.3] {c}Agá dois: coeficiente três, contra dois da amônia. [p=0.2] {d}Zero vírgula zero oito vezes três meios {e}dá zero vírgula doze."),
    dict(id="s19", block="resposta", text="{a}E a velocidade da reação, dividindo pelo coeficiente: [p=0.1] {b}zero vírgula zero oito dividido por dois {c}dá zero vírgula zero quatro."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}velocidade média é quanto a concentração mudou, dividido pelo tempo, [p=0.2] {b}e os coeficientes ligam a velocidade de cada substância."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai descobrir {a}por que umas reações são rápidas e outras lentas: [p=0.2] {b}por que o comprimido em pó reage antes do inteiro [p=0.1] e {c}por que a geladeira conserva. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
