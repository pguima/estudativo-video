# Estudativo · MAT-RAZ-024 — Velocidade média em dois trechos (Matemática · Razão e Proporção).
# Habilidade: descobrir que 40 km/h na ida e 60 km/h na volta dão 48 km/h, e não 50, dividindo a distância total pelo tempo total.
# Pré-requisitos: MAT-RAZ-015 (taxas e velocidade média). Próxima: MAT-RAZ-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. MMC não está no "já ensinado": a distância é escolhida como múltiplo comum, dito por extenso.

TITULO = "Velocidade média em dois trechos"

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
    dict(id="s01", block="gancho", text="Um carro vai até uma cidade a {a}quarenta quilômetros por hora [p=0.2] e volta pelo mesmo caminho a {b}sessenta. [p=0.3] Qual é a velocidade média da viagem toda? [p=0.3] Se você disse {c}cinquenta, caiu na pegadinha. [p=0.2] A resposta é {d}quarenta e oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você entende por quê, [p=0.2] resolve qualquer viagem em trechos [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}velocidade média é a distância total dividida pelo tempo total. [p=0.3] Daí sai o tempo de cada trecho: {c}a distância dividida pela velocidade. [p=0.3] Se faltar, procure no canal."),
    # escolher a distância
    dict(id="s04", block="distancia", text="O enunciado não diz a distância. [p=0.2] Sem problema: {a}escolha uma que dê conta exata. [p=0.3] Um número que seja múltiplo de quarenta e também de sessenta: [p=0.2] {b}cento e vinte quilômetros."),
    dict(id="s05", block="trechos", text="{a}Ida: cento e vinte dividido por quarenta dá três horas. [p=0.3] {b}Volta: cento e vinte dividido por sessenta dá duas horas."),
    dict(id="s06", block="trechos", text="{a}Distância total: cento e vinte mais cento e vinte dá duzentos e quarenta quilômetros. [p=0.3] {b}Tempo total: três horas mais duas horas dá cinco horas. [p=0.3] {c}Duzentos e quarenta dividido por cinco dá quarenta e oito quilômetros por hora."),
    # por que não 50
    dict(id="s07", block="porque", text="Por que não cinquenta? [p=0.2] As distâncias são iguais, [p=0.2] mas {a}os tempos não são. [p=0.3] O carro passa {b}três horas no trecho lento [p=0.2] e só {c}duas horas no rápido. [p=0.3] A velocidade menor pesa mais, [p=0.2] e a média {d}fica abaixo de cinquenta."),
    dict(id="s08", block="porque", text="E a distância escolhida não muda nada. [p=0.2] Com {a}duzentos e quarenta quilômetros de ida, [p=0.2] são {b}seis horas para ir e quatro para voltar. [p=0.3] {c}Quatrocentos e oitenta quilômetros em dez horas: quarenta e oito de novo."),
    # quando a média simples funciona
    dict(id="s09", block="iguais", text="E quando a média simples funciona? [p=0.2] Quando {a}os tempos são iguais. [p=0.3] {b}Duas horas a quarenta, depois duas horas a sessenta. [p=0.2] {c}Oitenta mais cento e vinte dá duzentos quilômetros em quatro horas. [p=0.3] {d}Cinquenta, certinho. [p=0.2] Cada velocidade pesou o mesmo."),
    dict(id="s10", block="parada", text="Trechos de tamanhos diferentes, ou com parada no meio? [p=0.2] O método não muda: [p=0.2] {a}some as distâncias, [p=0.2] {b}some os tempos, inclusive o tempo parado, [p=0.2] e {c}divida."),
    dict(id="s11", block="parada", text="Um carro anda {a}cem quilômetros em duas horas. [p=0.2] {b}Faz uma parada de meia hora para o almoço. [p=0.2] Depois anda {c}mais cinquenta quilômetros em meia hora. [p=0.3] {d}Duas horas, mais meia parado, mais meia andando: três horas. [p=0.2] Cento e cinquenta quilômetros em três horas: [p=0.2] {e}cinquenta quilômetros por hora. [p=0.3] Sem contar a parada, seriam duas horas e meia, e daria sessenta."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}fazer a média das velocidades: [p=0.2] quarenta mais sessenta dá cem, dividido por dois. [p=0.3] {b}Cinquenta. [p=0.3] Essa conta só vale com tempos iguais. [p=0.2] Na ida e volta com velocidades diferentes, {c}o que é igual é a distância, não o tempo."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para {a}ida e volta com a mesma distância: [p=0.3] {b}o dobro do produto, dividido pela soma. [p=0.3] Ou seja: {c}duas vezes uma velocidade vezes a outra, [p=0.2] dividido por {d}uma velocidade mais a outra."),
    dict(id="s14", block="atalho", text="{a}Duas vezes quarenta vezes sessenta, quatro mil e oitocentos. [p=0.3] {b}Quarenta mais sessenta dá cem. [p=0.3] {c}Quatro mil e oitocentos dividido por cem dá quarenta e oito."),
    dict(id="s15", block="atalho", text="Funciona porque é {a}a mesma conta de antes, com uma letra no lugar da distância. [p=0.2] No caminho, essa letra se cancela. [p=0.3] {b}Não vale se as distâncias forem diferentes [p=0.2] ou se houver parada. [p=0.2] Aí, {c}distância total dividida pelo tempo total."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um ônibus vai de uma cidade a outra a {a}noventa quilômetros por hora [p=0.2] e volta pelo mesmo caminho a {b}sessenta. [p=0.3] {c}Qual é a velocidade média da ida e volta?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Escolha {a}cento e oitenta quilômetros, múltiplo de noventa e de sessenta. [p=0.3] {b}Ida: cento e oitenta dividido por noventa dá duas horas. [p=0.2] {c}Volta: cento e oitenta dividido por sessenta dá três horas. [p=0.3] {d}Trezentos e sessenta quilômetros em cinco horas: setenta e dois quilômetros por hora."),
    dict(id="s19", block="resposta", text="Pelo atalho: {a}duas vezes noventa vezes sessenta, dez mil e oitocentos. [p=0.3] {b}Dividido por cento e cinquenta dá setenta e dois. [p=0.3] E repare: {c}ficou abaixo dos setenta e cinco da média simples, como devia."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}velocidade média é distância total dividida pelo tempo total, [p=0.2] {b}nunca a média das velocidades, [p=0.2] a não ser com {c}tempos iguais."),
    dict(id="s21", block="fim", text="Na próxima aula, a mesma ideia de taxa vale para {a}massa e volume: [p=0.2] é {b}a densidade, que diz se um objeto boia ou afunda na água. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
