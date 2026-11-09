# Estudativo · FIS-OPT-007 — Equação das lentes e dioptria (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: usar a mesma equação dos espelhos nas lentes, com o sinal do foco, e calcular o grau com V = 1/f, com f em metros.
# Pré-requisitos: FIS-OPT-006 (lentes e raios notáveis), FIS-OPT-011 (Gauss, aumento, atalho p' = f·p/(p − f)). Próxima: FIS-OPT-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Na lente: p' > 0 imagem real, do outro lado; p' < 0 virtual, do lado do objeto.
# "Grau" da receita = dioptria (di). Associação de lentes (somar vergências) fica fora: não está na habilidade.

TITULO = "Equação das lentes e o grau dos óculos"

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
    dict(id="s01", block="gancho", text="Na receita de óculos aparece {a}mais dois graus. [p=0.3] Esse grau é {b}uma conta: [p=0.2] {c}um dividido pela distância focal, em metros. [p=0.3] {d}Mais dois graus é uma lente convergente com foco a cinquenta centímetros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a imagem de uma lente [p=0.2] e {c}o grau dela."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a equação dos espelhos, um dividido por efe igual a um dividido por pê mais um dividido por pê linha, e o aumento; [p=0.2] e {c}a diferença entre lente convergente e divergente. [p=0.3] Se faltar alguma, procure no canal."),
    # a equação nas lentes
    dict(id="s04", block="equacao", text="A boa notícia: {a}a equação das lentes é a mesma dos espelhos. [p=0.3] {b}Pê é a distância do objeto até a lente, [p=0.1] {c}pê linha, a da imagem, [p=0.1] e {d}efe, a distância focal. [p=0.3] {e}O aumento também é o mesmo: menos pê linha dividido por pê."),
    dict(id="s05", block="equacao", text="Só os sinais ganham outra leitura. [p=0.2] {a}Lente convergente: efe positivo. [p=0.2] {b}Divergente: efe negativo. [p=0.3] {c}Pê linha positivo: imagem real, do outro lado da lente. [p=0.2] {d}Negativo: virtual, do mesmo lado do objeto."),
    # exemplo da lupa
    dict(id="s06", block="exemplo", text="Uma lupa com {a}foco de dez centímetros [p=0.2] e {b}um selo a seis centímetros dela. [p=0.3] {c}Um dividido por pê linha é igual a um décimo menos um sexto. [p=0.3] {d}MMC de dez e seis é trinta: [p=0.2] {e}três trinta avos menos cinco trinta avos, [p=0.2] {f}menos dois trinta avos, que é menos um quinze avos."),
    dict(id="s07", block="exemplo", text="{a}Pê linha é menos quinze centímetros: [p=0.2] {b}imagem virtual, do lado do selo. [p=0.3] {c}No aumento, o menos da fórmula com o menos do pê linha dá mais: [p=0.2] {d}quinze dividido por seis, dois vírgula cinco. [p=0.3] {e}Imagem direita e duas vezes e meia maior."),
    dict(id="s08", block="exemplo", text="Veja {a}uma divergente com foco de quinze centímetros: [p=0.2] {b}efe é menos quinze. [p=0.2] {c}Objeto a trinta. [p=0.3] Pelo atalho dos espelhos, {d}menos quinze vezes trinta, menos quatrocentos e cinquenta, [p=0.2] {e}dividido por trinta mais quinze, quarenta e cinco: [p=0.2] {f}pê linha é menos dez. [p=0.3] {g}Virtual, direita e menor, como toda imagem da divergente."),
    # vergência
    dict(id="s09", block="grau", text="Falta o grau. [p=0.2] O nome técnico é {a}vergência, vê: [p=0.2] {b}vê é igual a um dividido por efe, [p=0.2] {c}com efe em metros. [p=0.3] {d}A unidade é a dioptria, que a receita chama de grau."),
    dict(id="s10", block="grau", text="{a}Foco de cinquenta centímetros é zero vírgula cinco metro. [p=0.2] {b}Um dividido por zero vírgula cinco: [p=0.2] {c}mais duas dioptrias. [p=0.3] {d}Uma divergente com foco de vinte e cinco centímetros: [p=0.2] {e}um dividido por menos zero vírgula vinte e cinco, [p=0.2] {f}menos quatro dioptrias."),
    dict(id="s11", block="grau", text="{a}O sinal do grau é o sinal do foco: [p=0.2] {b}positivo, convergente; [p=0.1] {c}negativo, divergente. [p=0.3] E {d}quanto mais curto o foco, mais forte a lente, [p=0.2] seja qual for o sinal."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}deixar o foco em centímetros. [p=0.3] {b}Um dividido por cinquenta dá zero vírgula zero dois. [p=0.3] {c}Zero vírgula zero dois grau não existe numa receita de óculos. [p=0.2] {d}A conta do grau é sempre com efe em metros."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}efe em centímetros é cem dividido pelo grau. [p=0.3] {b}Mais quatro graus: cem dividido por quatro, vinte e cinco centímetros. [p=0.2] {c}Menos dois vírgula cinco: cem dividido por dois vírgula cinco, quarenta centímetros, e divergente."),
    dict(id="s14", block="atalho", text="Funciona porque {a}um metro tem cem centímetros: [p=0.2] {b}a conversão já vem dentro da conta. [p=0.3] {c}E, como você viu na divergente, o atalho dos espelhos também vale aqui: [p=0.2] {d}pê linha é efe vezes pê, dividido por pê menos efe."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma lente tem {a}mais quatro graus. [p=0.3] {b}Qual é a distância focal, [p=0.2] e {c}ela é convergente ou divergente? [p=0.3] {d}Com um objeto a cinquenta centímetros dela, onde se forma a imagem?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Cem dividido por quatro: vinte e cinco centímetros. [p=0.2] {b}O sinal é positivo: convergente. [p=0.3] {c}Pê linha é vinte e cinco vezes cinquenta, mil duzentos e cinquenta, [p=0.2] {d}dividido por cinquenta menos vinte e cinco, vinte e cinco: [p=0.2] {e}cinquenta centímetros."),
    dict(id="s18", block="resposta", text="{a}Positivo: imagem real, do outro lado da lente. [p=0.3] {b}O aumento é menos cinquenta dividido por cinquenta, menos um: [p=0.2] {c}invertida e do mesmo tamanho, [p=0.2] porque o objeto estava a duas distâncias focais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a equação das lentes é a dos espelhos, com efe positivo na convergente e negativo na divergente; [p=0.2] e {b}o grau é um dividido por efe, com efe em metros."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}o olho humano: [p=0.2] {b}onde a imagem se forma na miopia e na hipermetropia, [p=0.2] e {c}qual lente corrige cada uma. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
