# Estudativo · FIS-DIN-002 — Segunda lei de Newton: F = m·a (Física · Dinâmica · Leis de Newton).
# Habilidade: calcular força resultante, massa ou aceleração e ler a fórmula como proporção.
# Pré-requisitos: FIS-DIN-001 (resultante, inércia), FIS-CIN-007 (aceleração, v = v0 + a·t). Próxima: FIS-DIN-003.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Peso e P = m·g (FIS-DIN-004) não estão em "Já ensinado": nenhuma conta usa peso; as forças são empurrões e puxões.
# Proporção direta e inversa: MAT-RAZ-004 e MAT-RAZ-011 (ler fórmula como proporção) estão em "Já ensinado".

TITULO = "Segunda lei de Newton: F = m·a"

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
    dict(id="s01", block="gancho", text="Empurre, com a mesma força, {a}um carrinho de supermercado vazio [p=0.2] e {b}um cheio. [p=0.3] {c}O vazio dispara; o cheio mal sai do lugar. [p=0.3] Dá para dizer {d}exatamente quanto cada um acelera."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}força, massa ou aceleração [p=0.2] e ler a fórmula {c}como uma proporção, quase sem conta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a força resultante, que é a soma de todas as forças no corpo; [p=0.2] e a {c}aceleração, quanto a velocidade muda a cada segundo, em metros por segundo ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="Na aula passada, resultante zero mantinha a velocidade. [p=0.2] {a}Resultante diferente de zero muda a velocidade: [p=0.2] o corpo {b}acelera. [p=0.3] A segunda lei de Newton diz quanto: [p=0.2] {c}efe é igual a eme vezes á."),
    dict(id="s05", block="lei", text="{a}Efe é a força resultante, em newtons. [p=0.2] {b}Eme é a massa, em quilogramas. [p=0.2] {c}Á é a aceleração, em metros por segundo ao quadrado. [p=0.3] E {d}a aceleração aponta para onde aponta a resultante."),
    dict(id="s06", block="lei", text="Daqui sai o que é {a}um newton: [p=0.2] a força que dá a {b}um quilograma [p=0.1] uma aceleração de {c}um metro por segundo ao quadrado. [p=0.3] Por isso, {d}newton é o mesmo que quilograma vezes metro por segundo ao quadrado."),
    # exemplos
    dict(id="s07", block="exemplo", text="Vamos usar. [p=0.2] Um carro de {a}mil quilogramas recebe uma força resultante de {b}três mil newtons. [p=0.3] {c}Á é efe dividido por eme: [p=0.2] {d}três mil dividido por mil, [p=0.1] {e}três metros por segundo ao quadrado. [p=0.3] A cada segundo, ele ganha três metros por segundo."),
    dict(id="s08", block="exemplo", text="{a}Uma caixa de cinco quilogramas é puxada com {b}trinta newtons para a direita [p=0.2] e {c}dez newtons para a esquerda. [p=0.3] Primeiro, a resultante: {d}trinta menos dez, vinte newtons para a direita. [p=0.3] Depois, {e}vinte dividido por cinco: [p=0.1] {f}quatro metros por segundo ao quadrado, para a direita."),
    # proporção
    dict(id="s09", block="proporcao", text="Agora, a leitura como proporção. [p=0.2] {a}Mesma massa, força dobrada: [p=0.2] {b}a aceleração dobra. [p=0.2] Força e aceleração são {c}diretamente proporcionais."),
    dict(id="s10", block="proporcao", text="{a}Mesma força, massa dobrada: [p=0.2] {b}a aceleração cai pela metade. [p=0.2] Massa e aceleração são {c}inversamente proporcionais. [p=0.3] É o carrinho cheio: {d}mais massa, menos aceleração com o mesmo empurrão."),
    dict(id="s11", block="proporcao", text="{a}Com números: sessenta newtons de resultante. [p=0.2] {b}No carrinho vazio, de vinte quilogramas: três metros por segundo ao quadrado. [p=0.2] {c}No cheio, de sessenta quilogramas: um. [p=0.3] {d}Três vezes a massa, um terço da aceleração."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar uma força só, em vez da resultante. [p=0.3] Na caixa de cinco quilogramas, {b}trinta dividido por cinco daria seis metros por segundo ao quadrado. [p=0.3] {c}Errado: os dez newtons para a esquerda também agem na caixa. [p=0.2] {d}O certo é quatro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a questão mudou só uma coisa? [p=0.2] Use a proporção, sem refazer a conta. [p=0.3] {b}Força três vezes maior, mesma massa: {c}aceleração três vezes maior. [p=0.3] {d}Massa quatro vezes maior, mesma força: {e}aceleração dividida por quatro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}efe igual a eme vezes á é uma multiplicação: [p=0.2] o que multiplica de um lado multiplica do outro. [p=0.3] {b}Não compensa quando a questão muda só uma entre várias forças: [p=0.2] a resultante não cresce na mesma proporção. [p=0.2] Aí, {c}calcule a nova resultante."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma caixa de vinte quilogramas, parada, é puxada com {b}cem newtons para a direita [p=0.2] e {c}quarenta newtons para a esquerda. [p=0.3] {d}Qual é a aceleração? [p=0.2] E {e}qual é a velocidade depois de quatro segundos?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Resultante primeiro: {a}cem menos quarenta, sessenta newtons para a direita. [p=0.3] {b}Sessenta dividido por vinte: [p=0.1] {c}três metros por segundo ao quadrado."),
    dict(id="s18", block="resposta", text="A caixa partiu do repouso: {a}vê zero é zero. [p=0.2] {b}Vê é igual a zero mais três vezes quatro: [p=0.2] {c}doze metros por segundo. [p=0.3] E se a caixa tivesse quarenta quilogramas? [p=0.2] {d}O dobro da massa, metade da aceleração: um vírgula cinco metro por segundo ao quadrado."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}força resultante é massa vezes aceleração, [p=0.2] {b}sempre com a resultante, não com uma força só, [p=0.2] e {c}a fórmula é uma proporção: [p=0.1] dobra a força, dobra a aceleração; dobra a massa, a aceleração cai pela metade."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver que {a}força nunca vem sozinha: [p=0.2] quando você {b}empurra a parede, ela empurra você de volta. [p=0.2] É a {c}terceira lei, ação e reação. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
