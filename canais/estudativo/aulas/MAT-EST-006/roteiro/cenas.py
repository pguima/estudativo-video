# Estudativo · MAT-EST-006 — Tabelas de dupla entrada, mapas e infográficos (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: cruzar linha e coluna, usar a legenda de cores de um mapa e tirar o dado certo de um infográfico.
# Pré-requisitos: MAT-EST-002 (tabela de frequência, total, classes), MAT-LEI-001 (pergunta primeiro, marcar só os números úteis). Próxima: MAT-EST-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Tabela, mapa, infográfico e questão inéditos, criados para esta aula (ditos como tal na fala).
# Tabela (inscritos de um curso):   presencial | a distância | total
#   manhã                               120    |     80      |  200
#   tarde                               100    |     50      |  150
#   noite                               140    |    210      |  350
#   total                               360    |    340      |  700
#   Erro: 210 / 700 = 30%. Certo (só a noite): 210 / 350 = 60%.
# Mapa: 5 bairros; legenda claro 0–40%, médio 40–70%, escuro 70–100% das casas com rede de esgoto. 2 escuros, 2 médios (um é o Centro), 1 claro.
# Infográfico: casa de 4 pessoas, 600 L de água por dia; banho 40% → 240 L → 60 L por pessoa.
# Questão: manhã lê 60, não lê 90, total 150; noite lê ?, não lê 50, total 200 → 150; 150/200 = 75%.

TITULO = "Tabelas de dupla entrada, mapas e infográficos"

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
    dict(id="s01", block="gancho", text="{a}Dos alunos da noite, quantos por cento estudam a distância? [p=0.2] A resposta está {b}nesta tabela. [p=0.3] Muita gente responde {c}trinta por cento. [p=0.2] O certo é {d}sessenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você cruza linha e coluna, lê a legenda de um mapa, tira o dado certo de um infográfico [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a tabela de frequência, com o total no fim, [p=0.2] e {c}ler a pergunta antes do texto, marcando só os números que entram na conta. [p=0.3] Se faltar alguma, procure no canal."),
    # dupla entrada
    dict(id="s04", block="dupla", text="Numa tabela de dupla entrada, {a}cada número depende de duas coisas ao mesmo tempo. [p=0.2] Nesta, criada para a aula, {b}as linhas são os turnos de um curso: manhã, tarde e noite. [p=0.2] {c}As colunas são o jeito de estudar: presencial ou a distância. [p=0.2] E {d}a última linha e a última coluna trazem os totais."),
    dict(id="s05", block="dupla", text="Para ler, {a}cruze a linha com a coluna. [p=0.2] Quantos estudam à noite, a distância? [p=0.2] {b}Dedo na linha da noite. [p=0.2] {c}Dedo na coluna a distância. [p=0.2] Onde eles se encontram: {d}duzentos e dez alunos."),
    dict(id="s06", block="dupla", text="E os totais? [p=0.2] {a}Na linha da noite, cento e quarenta mais duzentos e dez dá trezentos e cinquenta alunos. [p=0.2] {b}Na coluna a distância, oitenta mais cinquenta mais duzentos e dez dá trezentos e quarenta. [p=0.2] {c}E o total geral é setecentos."),
    # mapa
    dict(id="s07", block="mapa", text="Agora, um {a}mapa. [p=0.2] Este, também criado para a aula, mostra {b}os bairros de uma cidade. [p=0.2] A cor de cada bairro diz {c}quantos por cento das casas têm rede de esgoto."),
    dict(id="s08", block="mapa", text="O segredo é {a}a legenda, o quadrinho que explica as cores. [p=0.2] {b}Clarinho: de zero a quarenta por cento. [p=0.2] {c}Médio: de quarenta a setenta. [p=0.2] {d}Escuro: de setenta a cem. [p=0.3] Cada cor é {e}uma faixa, como as classes da tabela de frequência."),
    dict(id="s09", block="mapa", text="Quantos bairros têm setenta por cento ou mais das casas com esgoto? [p=0.2] {a}Conte os escuros: dois. [p=0.3] E o centro tem quantos por cento? [p=0.2] {b}A cor não dá o número exato, [p=0.2] {c}só a faixa: de quarenta a setenta. [p=0.3] E {d}leia a legenda antes de tudo: nem todo mapa usa a cor escura para o maior valor."),
    # infográfico
    dict(id="s10", block="info", text="Por fim, o {a}infográfico: números, desenhos e texto juntos. [p=0.2] Neste, criado para a aula, {b}uma casa com quatro pessoas gasta seiscentos litros de água por dia. [p=0.2] {c}O banho leva quarenta por cento."),
    dict(id="s11", block="info", text="A pergunta: {a}quantos litros cada pessoa gasta no banho, por dia? [p=0.2] Os desenhos enfeitam. [p=0.2] {b}O dado está no número e na unidade: [p=0.2] os seiscentos litros são da casa toda, num dia. [p=0.3] {c}Quarenta por cento de seiscentos dá duzentos e quarenta litros, ainda para a casa toda. [p=0.2] Quem para aqui erra. [p=0.2] Por pessoa: {d}duzentos e quarenta dividido por quatro dá sessenta litros."),
    # erro
    dict(id="s12", block="erro", text="Volte ao erro do começo. [p=0.2] {a}Dos alunos da noite, quantos por cento estudam a distância? [p=0.2] A pessoa pega os duzentos e dez e {b}divide pelo total geral, setecentos. [p=0.2] Dá {c}trinta por cento."),
    dict(id="s13", block="erro", text="Mas a pergunta fala {a}só dos alunos da noite. [p=0.2] O total deles é {b}trezentos e cinquenta. [p=0.2] {c}Duzentos e dez dividido por trezentos e cinquenta dá zero vírgula seis, [p=0.2] que são {d}sessenta por cento. [p=0.3] Antes de dividir, {e}pergunte: quem é o cem por cento aqui?"),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}a tabela se confere sozinha. [p=0.2] {b}Cada linha soma o total da linha, e cada coluna soma o total da coluna. [p=0.3] Se a prova apaga um número, {c}tire as outras células do total. [p=0.2] Sem o duzentos e dez, por exemplo: {d}trezentos e cinquenta menos cento e quarenta dá duzentos e dez."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o total é só a soma das partes. [p=0.2] {b}Não compensa quando a tabela não traz os totais: [p=0.2] aí, não há de onde tirar."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] A tabela, criada para esta questão, mostra {a}quantos alunos de uma escola leem por gosto, em cada turno. [p=0.3] {b}De manhã, sessenta leem e noventa não leem. [p=0.2] Total da manhã: cento e cinquenta. [p=0.3] {c}À noite, o número de quem lê está apagado. [p=0.2] Cinquenta não leem, e o total da noite é duzentos."),
    dict(id="s17", block="questao", text="{a}Quantos alunos da noite leem? [p=0.2] E {b}entre os alunos da noite, quantos por cento leem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Pelo atalho, {a}duzentos menos cinquenta dá cento e cinquenta. [p=0.2] {b}Cento e cinquenta alunos da noite leem."),
    dict(id="s20", block="resposta", text="A pergunta fala {a}só da noite, então o cem por cento é duzentos. [p=0.2] {b}Cento e cinquenta dividido por duzentos dá zero vírgula setenta e cinco, [p=0.2] que são {c}setenta e cinco por cento. [p=0.3] Dividir pelo total da escola, {d}cento e cinquenta mais duzentos, daria a resposta errada."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}cruze linha e coluna, [p=0.2] {b}leia a legenda antes do mapa, [p=0.2] {c}confira a unidade do infográfico [p=0.2] e {d}ache o cem por cento antes de dividir."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica {a}tudo desta parte do curso: [p=0.2] tabelas, gráficos de barras, de linhas e de setores, e histogramas, [p=0.2] {b}com porcentagens e variações. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
