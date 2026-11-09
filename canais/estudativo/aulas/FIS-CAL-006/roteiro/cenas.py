# Estudativo · FIS-CAL-006 — Trocas de calor com gelo (Física · Calor e Termodinâmica · Calorimetria e mudanças de estado).
# Habilidade: decidir antes da conta se o calor disponível derrete todo o gelo e achar o estado final da mistura.
# Pré-requisitos: FIS-CAL-004 (Q = m·L, L fusão = 80 cal/g), FIS-CAL-005 (soma dos calores = 0). Próxima: FIS-CAL-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Calorímetro ideal; gelo sempre a 0 °C nos exemplos (gelo abaixo de zero só é citado, com a etapa a mais).
# Método da aula: (1) calor disponível = água quente até 0 °C; (2) calor necessário = derreter todo o gelo; (3) comparar.

TITULO = "Trocas de calor com gelo"

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
    dict(id="s01", block="gancho", text="{a}Duzentos gramas de gelo a zero grau, num copo com {b}cem gramas de água a quarenta graus. [p=0.3] Quem joga tudo na soma dos calores igual a zero [p=0.2] encontra {c}menos quarenta graus. [p=0.3] Água líquida a menos quarenta? [p=0.2] {d}Impossível."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai decidir, {b}antes da conta, [p=0.1] se o gelo derrete todo, [p=0.2] e achar {c}o estado final de qualquer mistura com gelo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}derreter gelo pede oitenta calorias por grama, quê igual a eme éle; [p=0.2] e {c}no calorímetro, a soma dos calores é zero. [p=0.3] Se faltar alguma, procure no canal."),
    # o problema
    dict(id="s04", block="ideia", text="Com gelo, a dúvida é: [p=0.2] {a}a água quente tem calor suficiente para derreter tudo? [p=0.3] Se tiver, {b}sobra só água, acima de zero. [p=0.2] Se não tiver, {c}a mistura para em zero grau, [p=0.2] com {d}gelo e água juntos."),
    dict(id="s05", block="ideia", text="Para decidir, {a}compare dois números antes de montar a equação. [p=0.3] {b}O calor disponível: [p=0.1] quanto a água quente cede até chegar a zero grau. [p=0.3] {c}O calor necessário: [p=0.1] quanto o gelo pede para derreter inteiro."),
    # caso 1
    dict(id="s06", block="caso1", text="Primeiro caso: {a}cem gramas de gelo a zero grau [p=0.1] com {b}trezentos gramas de água a quarenta. [p=0.3] {c}Disponível: trezentos vezes um vezes quarenta dá doze mil calorias. [p=0.2] {d}Necessário: cem vezes oitenta dá oito mil."),
    dict(id="s07", block="caso1", text="{a}Doze mil é mais que oito mil: [p=0.2] {b}o gelo derrete todo. [p=0.3] {c}Sobram quatro mil calorias, [p=0.2] que esquentam toda a água, {d}agora quatrocentos gramas, a partir de zero. [p=0.3] {e}Quatro mil dividido por quatrocentos: dez graus Celsius."),
    dict(id="s08", block="caso1", text="Se preferir a soma igual a zero, {a}agora ela funciona: [p=0.2] {b}oito mil para derreter o gelo, [p=0.1] mais cem tê para a água que veio do gelo ir de zero até tê, [p=0.1] mais trezentos vezes a variação, tê menos quarenta, [p=0.1] igual a zero. [p=0.3] {c}Tê igual a dez. [p=0.2] Bateu."),
    # caso 2
    dict(id="s09", block="caso2", text="Agora, o gancho: {a}duzentos gramas de gelo a zero grau [p=0.1] com {b}cem gramas de água a quarenta. [p=0.3] {c}Disponível: cem vezes quarenta dá quatro mil. [p=0.2] {d}Necessário: duzentos vezes oitenta dá dezesseis mil."),
    dict(id="s10", block="caso2", text="{a}Quatro mil é menos que dezesseis mil: [p=0.2] {b}não derrete tudo. [p=0.2] A mistura termina em {c}zero grau. [p=0.3] Quanto derrete? [p=0.2] {d}Quatro mil dividido por oitenta: cinquenta gramas. [p=0.3] No fim, {e}cento e cinquenta gramas de gelo e cento e cinquenta de água, a zero grau."),
    dict(id="s11", block="caso2", text="E se o gelo estiver abaixo de zero? [p=0.2] O necessário ganha {a}uma etapa antes: [p=0.2] esquentar o gelo até zero, {b}com o calor específico do gelo, zero vírgula cinco. [p=0.3] {c}Cem gramas de gelo a menos dez pedem mais quinhentas calorias. [p=0.3] {d}Some isso ao necessário, e compare do mesmo jeito."),
    # erro
    dict(id="s12", block="erro", text="Por isso, a conta do gancho deu {a}menos quarenta. [p=0.2] Ela supôs que {b}todo o gelo derreteu, [p=0.2] e o calor não dava para isso. [p=0.3] {c}Temperatura final abaixo de zero, com água líquida, [p=0.2] é o sinal de que você pulou a comparação."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o macete do oitenta. [p=0.2] {a}Um grama de água a oitenta graus, ao esfriar até zero, cede oitenta calorias. [p=0.2] {b}Exatamente o que derrete um grama de gelo. [p=0.3] Então, {c}água a oitenta graus derrete a mesma massa de gelo."),
    dict(id="s14", block="atalho", text="{a}Água a quarenta, metade disso: [p=0.1] derrete metade da sua massa. [p=0.3] No gancho, {b}cem gramas a quarenta derretem cinquenta gramas de gelo, [p=0.2] sem conta nenhuma. [p=0.3] {c}Não compensa se o gelo estiver abaixo de zero: [p=0.2] aí, antes, ele precisa de calor para chegar a zero."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Cem gramas de gelo a zero grau [p=0.1] caem em {b}cento e cinquenta gramas de água a trinta e dois graus. [p=0.3] {c}O gelo derrete todo? [p=0.2] {d}Como termina a mistura?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Disponível: cento e cinquenta vezes trinta e dois dá quatro mil e oitocentas calorias. [p=0.2] {b}Necessário: cem vezes oitenta dá oito mil. [p=0.3] {c}Falta calor: não derrete tudo, e a mistura para em zero grau."),
    dict(id="s18", block="resposta", text="{a}Quanto derrete? [p=0.1] {b}Quatro mil e oitocentos dividido por oitenta: sessenta gramas. [p=0.3] {c}Sobram quarenta gramas de gelo, [p=0.1] e a água fica com cento e cinquenta mais sessenta: {d}duzentos e dez gramas, tudo a zero grau."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}compare o calor disponível com o necessário; [p=0.2] {b}se sobra, derrete tudo e a temperatura passa de zero; [p=0.2] {c}se falta, a mistura para em zero, com gelo e água."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a pressão entra na história: [p=0.2] você vai ler {b}o diagrama de fases [p=0.1] e entender {c}a panela de pressão. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
