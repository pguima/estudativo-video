# Estudativo · FIS-CAL-001 — Temperatura e escalas termométricas (Física · Calor e Termodinâmica · Temperatura e dilatação).
# Habilidade: separar temperatura de calor e converter Celsius, Fahrenheit e Kelvin com TC/5 = (TF − 32)/9, e variações com ΔC/5 = ΔF/9.
# Pré-requisitos: QUI-CAL-010 (Kelvin), MAT-RAZ-002 (proporção), MAT-EQU-010 (equação com frações). Próxima: FIS-CAL-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula da trilha: guarda a linguagem visual de Calor e Termodinâmica (veja o visual.py). Questão inédita.
# Na tela, a fórmula sai com as letras C, F e K (TC, TF e TK da ficha), narradas como "a temperatura Celsius", "a Fahrenheit" e "a Kelvin" (letras isoladas soam como "você" e "cá"). Energia (joule) ainda não
# foi ensinada: "calor é energia que passa" fica no sentido do dia a dia. Zero absoluto ≈ −273 °C (−273,15 °C, arredondado).

TITULO = "Temperatura e escalas termométricas"

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
    dict(id="s01", block="gancho", text="{a}Numa cidade dos Estados Unidos, o painel da rua marca {b}cento e quatro graus. [p=0.3] Ninguém está fervendo. [p=0.2] Lá, a escala é outra: [p=0.1] {c}cento e quatro graus Fahrenheit [p=0.1] são {d}quarenta graus Celsius. [p=0.2] Um dia quente, só isso."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai separar {b}temperatura de calor [p=0.2] e passar de uma escala para outra: [p=0.1] {c}Celsius, Fahrenheit e Kelvin."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}resolver uma proporção, [p=0.2] e {c}a escala Kelvin, em que vinte e sete graus Celsius viram trezentos kelvins. [p=0.3] Se faltar alguma, procure no canal."),
    # temperatura e calor
    dict(id="s04", block="calor", text="Comece pela diferença que mais cai em prova. [p=0.2] {a}Temperatura mede o quanto as partículas de um corpo estão agitadas. [p=0.3] {b}No café quente, elas se agitam muito. [p=0.2] {c}Na água gelada, bem menos."),
    dict(id="s05", block="calor", text="{a}Calor é outra coisa. [p=0.2] Calor é a energia que {b}passa de um corpo para outro [p=0.2] por causa da diferença de temperatura. [p=0.3] E, sozinho, ele sempre vai {c}do mais quente para o mais frio. [p=0.3] Segure uma xícara de café: {d}o calor sai do café e entra na sua mão."),
    dict(id="s06", block="calor", text="A passagem para quando {a}as temperaturas ficam iguais. [p=0.2] Isso se chama {b}equilíbrio térmico. [p=0.3] É assim que o termômetro funciona: [p=0.2] ele fica encostado no corpo {c}até chegar à mesma temperatura, [p=0.2] e aí mostra a temperatura do corpo."),
    dict(id="s07", block="calor", text="Então, cuidado com a frase {a}esse corpo tem muito calor. [p=0.3] Na Física, {b}o corpo tem temperatura. [p=0.2] {c}Calor só existe passando de um corpo para outro."),
    # escalas
    dict(id="s08", block="escalas", text="Para medir a temperatura, cada escala escolhe {a}dois pontos fixos: [p=0.2] {b}o gelo derretendo [p=0.1] e {c}a água fervendo, ao nível do mar. [p=0.3] Na {d}Celsius, eles valem zero e cem."),
    dict(id="s09", block="escalas", text="Na {a}Fahrenheit, usada nos Estados Unidos, [p=0.2] o gelo derrete a {b}trinta e dois [p=0.1] e a água ferve a {c}duzentos e doze. [p=0.3] Na {d}Kelvin, a escala do Sistema Internacional, [p=0.2] são {e}duzentos e setenta e três [p=0.1] e trezentos e setenta e três."),
    dict(id="s10", block="escalas", text="O zero da Kelvin é o {a}zero absoluto: [p=0.2] a menor agitação possível das partículas, [p=0.2] perto de {b}menos duzentos e setenta e três graus Celsius. [p=0.3] Por isso, a Kelvin {c}não tem valor negativo. [p=0.2] E repare: {d}diz-se trezentos kelvins, sem a palavra grau."),
    # a fórmula
    dict(id="s11", block="formula", text="Como passar de uma escala para outra? [p=0.2] Com uma {a}proporção. [p=0.3] Se o líquido do termômetro subiu {b}um quarto do caminho entre o gelo e a fervura numa escala, [p=0.2] ele subiu {c}um quarto do caminho em todas."),
    dict(id="s12", block="formula", text="{a}Na Celsius, esse caminho tem cem graus. [p=0.2] {b}Na Fahrenheit, tem duzentos e doze menos trinta e dois: [p=0.1] cento e oitenta. [p=0.3] Então, {c}a temperatura Celsius dividida por cem [p=0.1] é igual à Fahrenheit menos trinta e dois, dividida por cento e oitenta."),
    dict(id="s13", block="formula", text="{a}Cem e cento e oitenta dá para dividir por vinte. [p=0.2] Fica {b}Celsius dividida por cinco igual a Fahrenheit menos trinta e dois, dividida por nove. [p=0.3] Na tela, {c}a letra cê é a temperatura em Celsius, [p=0.1] e {d}a letra efe, em Fahrenheit. [p=0.3] E, como a Kelvin é a Celsius somada a duzentos e setenta e três, [p=0.2] {e}a Kelvin menos duzentos e setenta e três, dividida por cinco, entra na mesma igualdade."),
    # exemplos
    dict(id="s14", block="exemplos", text="Vamos conferir o painel: [p=0.1] {a}cento e quatro graus Fahrenheit. [p=0.2] {b}Cento e quatro menos trinta e dois dá setenta e dois. [p=0.2] {c}Setenta e dois dividido por nove dá oito. [p=0.3] Então, {d}a Celsius dividida por cinco dá oito, [p=0.1] e a Celsius é {e}quarenta graus."),
    dict(id="s15", block="exemplos", text="{a}E vinte e cinco graus Celsius? [p=0.2] {b}Vinte e cinco dividido por cinco dá cinco. [p=0.2] Do outro lado, também tem que dar cinco: [p=0.2] {c}Fahrenheit menos trinta e dois é cinco vezes nove, que dá quarenta e cinco, [p=0.1] e a Fahrenheit é {d}setenta e sete graus. [p=0.3] Em Kelvin, é só somar: {e}duzentos e noventa e oito kelvins."),
    # variação
    dict(id="s16", block="variacao", text="Outra pergunta de prova: [p=0.2] {a}a temperatura subiu dez graus Celsius. [p=0.2] Quanto ela subiu em Fahrenheit? [p=0.3] Aqui você não converte uma temperatura, e sim {b}uma variação, [p=0.2] que a Física escreve com {c}a letra grega delta."),
    dict(id="s17", block="variacao", text="Na variação, {a}o trinta e dois some, [p=0.2] porque ele só marca onde a escala começa. [p=0.2] Fica {b}a variação em Celsius dividida por cinco igual à variação em Fahrenheit dividida por nove. [p=0.3] {c}Dez dividido por cinco dá dois; [p=0.1] {d}dois vezes nove dá dezoito. [p=0.2] Subiu {e}dezoito graus Fahrenheit. [p=0.3] Em Kelvin, {f}a variação é a mesma da Celsius: dez kelvins."),
    # erro
    dict(id="s18", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a fórmula da temperatura numa variação. [p=0.2] A pessoa lê subiu dez graus Celsius, [p=0.1] {b}converte o dez como se fosse uma temperatura [p=0.2] e responde {c}cinquenta graus Fahrenheit."),
    dict(id="s19", block="erro", text="Confira com um dia que esquenta {a}de vinte para trinta graus Celsius. [p=0.2] Em Fahrenheit, isso é {b}de sessenta e oito para oitenta e seis. [p=0.2] A subida foi de {c}dezoito, [p=0.1] e não de cinquenta."),
    # atalho
    dict(id="s20", block="atalho", text="Agora, o atalho: {a}conte de cinco em cinco. [p=0.3] {b}Cada cinco graus Celsius valem nove graus Fahrenheit, [p=0.2] partindo do {c}zero, que é trinta e dois. [p=0.3] Vinte e cinco graus Celsius são {d}cinco saltos de cinco. [p=0.2] {e}Cinco saltos de nove dão quarenta e cinco, [p=0.1] mais trinta e dois: {f}setenta e sete."),
    dict(id="s21", block="atalho", text="Funciona porque {a}é a própria proporção de cinco para nove. [p=0.3] E ainda dá um bônus: [p=0.1] {b}menos quarenta é igual nas duas escalas. [p=0.3] {c}Não compensa quando o número não é múltiplo de cinco, como trinta e sete: [p=0.2] aí, use a fórmula."),
    # questão
    dict(id="s22", block="questao", text="Hora de testar. [p=0.2] Um turista vê no termômetro da rua {a}cinquenta e nove graus Fahrenheit. [p=0.3] {b}Quanto é isso em Celsius? [p=0.3] À tarde, a temperatura {c}sobe dezoito graus Fahrenheit. [p=0.2] {d}Quanto ela subiu em Celsius e em kelvins?"),
    dict(id="s23", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s24", block="resposta", text="Vamos lá. [p=0.2] {a}Cinquenta e nove menos trinta e dois dá vinte e sete. [p=0.2] {b}Vinte e sete dividido por nove dá três. [p=0.2] Então, a Celsius dividida por cinco dá três, [p=0.1] e a Celsius é {c}quinze graus."),
    dict(id="s25", block="resposta", text="Na subida, {a}o trinta e dois não entra. [p=0.2] {b}Dezoito dividido por nove dá dois; [p=0.1] {c}dois vezes cinco dá dez. [p=0.2] Subiu {d}dez graus Celsius, [p=0.1] e também {e}dez kelvins."),
    # fechamento
    dict(id="s26", block="fim", text="Resumindo: {a}temperatura é agitação, e calor é energia passando; [p=0.2] {b}para converter, use a proporção de cinco para nove, com o trinta e dois na Fahrenheit; [p=0.2] e {c}na variação, o trinta e dois sai."),
    dict(id="s27", block="fim", text="Na próxima aula, você vai ver o que a temperatura faz com o tamanho das coisas: [p=0.2] {a}a dilatação, [p=0.1] e por que {b}pontes e trilhos têm frestas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
