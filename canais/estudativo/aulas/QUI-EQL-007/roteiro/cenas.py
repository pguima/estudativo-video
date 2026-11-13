# Estudativo · QUI-EQL-007 — Produto de solubilidade: Kps (Química · Equilíbrio Químico · pH, hidrólise, tampão e Kps).
# Habilidade: escrever o Kps de BaSO₄ e CaF₂, calcular a solubilidade e dizer se vai formar precipitado.
# Pré-requisitos: QUI-EQL-001, QUI-SOL-002, MAT-POT-016. Próxima: QUI-EQL-008 (praticando o módulo).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; resultado de conta com "dá". Questão inédita, criada para esta aula.
# pH, bases e OH⁻ não estão em "Já ensinado" (a questão usa PbI₂). Leitura: Kps = "cá pê ésse", s = "ésse".
# Fatos: BaSO₄ é o contraste do raio X do estômago; Ba²⁺ solto é tóxico. Kps(BaSO₄) ≈ 1,1 × 10⁻¹⁰ ("perto de 10⁻¹⁰") ⇒ s ≈ 10⁻⁵.
# CaF₂: Kps = 4s³; com Kps = 3,2 × 10⁻¹¹ (tabela: 3,5 × 10⁻¹¹) ⇒ s³ = 8 × 10⁻¹², s = 2 × 10⁻⁴. Mistura Ba²⁺ 10⁻³ e SO₄²⁻ 10⁻³:
# Q = 10⁻⁶ > Kps ⇒ precipita. Questão: PbI₂ (iodeto de chumbo, sólido amarelo), Kps = 4 × 10⁻⁹
# (arredondado; tabela 9,8 × 10⁻⁹) ⇒ s³ = 10⁻⁹, s = 10⁻³; mistura Pb²⁺ 10⁻² e I⁻ 10⁻⁴ ⇒ Q = 10⁻¹⁰ < 4 × 10⁻⁹ ⇒ NÃO precipita.
# Bases e OH⁻ não estão em "Já ensinado" desta aula, por isso a questão usa um iodeto.

TITULO = "Produto de solubilidade: Kps"

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
    dict(id="s01", block="gancho", text="{a}Para o raio X do estômago, o paciente bebe sulfato de bário, [p=0.1] {b}e o bário solto no sangue é venenoso. [p=0.3] {c}Mesmo assim, o exame é seguro. [p=0.2] {d}O segredo: quase nada desse sal se dissolve. [p=0.2] {e}Quanto é esse quase nada?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}escrever o cá pê ésse do sulfato de bário e do fluoreto de cálcio, [p=0.2] {b}calcular a solubilidade [p=0.1] e {c}dizer se vai se formar precipitado."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar: [p=0.1] {a}a solução saturada, a que não dissolve mais nada e fica com sólido no fundo; [p=0.2] {b}a constante de equilíbrio, sem os sólidos; [p=0.2] {c}e a raiz quadrada e a cúbica de potências de dez. [p=0.2] Se faltar alguma, procure no canal."),
    # o Kps
    dict(id="s04", block="kps", text="{a}Numa solução saturada, o sal do fundo continua se dissolvendo, [p=0.1] {b}e os íons dissolvidos continuam voltando ao sólido, na mesma velocidade. [p=0.2] {c}É um equilíbrio. [p=0.3] {d}Sulfato de bário sólido, em equilíbrio com os íons bário dois mais e sulfato dois menos, dissolvidos."),
    dict(id="s05", block="kps", text="{a}A constante dele se chama produto de solubilidade, o cá pê ésse. [p=0.2] {b}O sólido fica de fora, [p=0.1] {c}então sobra só o produto dos íons: [p=0.1] {d}bário vezes sulfato. [p=0.3] {e}O fluoreto de cálcio, cê á éfe dois, solta um cálcio e dois fluoretos: [p=0.1] {f}cálcio vezes fluoreto ao quadrado."),
    # solubilidade
    dict(id="s06", block="solub", text="{a}Solubilidade é quanto do sal se dissolve, em mol por litro, até saturar. [p=0.2] {b}Chame de ésse. [p=0.3] {c}No sulfato de bário, cada unidade que se dissolve solta um bário e um sulfato: [p=0.1] {d}cada íon vale ésse."),
    dict(id="s07", block="solub", text="{a}Cá pê ésse é ésse vezes ésse, ésse ao quadrado. [p=0.2] {b}O do sulfato de bário é perto de dez elevado a menos dez. [p=0.2] {c}Ésse é a raiz: dez elevado a menos cinco mol por litro. [p=0.3] {d}Cem mil vezes menos que um mol em cada litro. [p=0.1] Quase nada, mesmo."),
    dict(id="s08", block="solub", text="{a}No fluoreto de cálcio, cada unidade solta um cálcio e dois fluoretos. [p=0.2] {b}O cálcio vale ésse; [p=0.1] {c}o fluoreto, dois ésse. [p=0.2] {d}Cá pê ésse: ésse vezes o quadrado de dois ésse. [p=0.2] Dois ésse ao quadrado dá quatro ésse ao quadrado; [p=0.1] {e}vezes ésse, quatro ésse ao cubo."),
    dict(id="s09", block="solub", text="{a}Com cá pê ésse igual a três vírgula dois vezes dez elevado a menos onze: [p=0.2] {b}ésse ao cubo é três vírgula dois vezes dez elevado a menos onze, dividido por quatro: [p=0.1] dá zero vírgula oito vezes dez elevado a menos onze, [p=0.1] que é oito vezes dez elevado a menos doze. [p=0.3] {c}A raiz cúbica de oito dá dois; [p=0.1] {d}a de dez elevado a menos doze dá dez elevado a menos quatro. [p=0.2] {e}Ésse dá dois vezes dez elevado a menos quatro mol por litro."),
    # precipitado
    dict(id="s10", block="precip", text="{a}E o precipitado? [p=0.2] É o sólido que se forma quando os íons passam do limite. [p=0.2] {b}Misture as soluções e calcule o produto dos íons, montado do mesmo jeito que o cá pê ésse, [p=0.1] {c}com as concentrações da mistura."),
    dict(id="s11", block="precip", text="{a}Produto maior que o cá pê ésse: passou do limite, [p=0.1] {b}forma precipitado. [p=0.2] {c}Menor: tudo continua dissolvido. [p=0.2] {d}Igual: está no limite, saturada."),
    dict(id="s12", block="precip", text="{a}Bário a dez elevado a menos três e sulfato a dez elevado a menos três, na mistura. [p=0.2] {b}O produto dá dez elevado a menos seis, [p=0.1] {c}bem maior que dez elevado a menos dez. [p=0.2] {d}Forma precipitado."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro comum é esquecer que o fluoreto conta em dobro. [p=0.2] {b}Quem escreve ésse vezes ésse ao quadrado acha ésse ao cubo, sem o quatro. [p=0.3] {c}Aí a solubilidade sai perto de três vezes dez elevado a menos quatro, e não dois. [p=0.2] {d}São dois fluoretos para cada cálcio: [p=0.1] {e}o fluoreto vale dois ésse."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho: [p=0.2] {a}decore dois formatos. [p=0.2] {b}Um íon de cada, como o sulfato de bário: [p=0.1] {c}cá pê ésse igual a ésse ao quadrado. [p=0.2] {d}Um íon de um tipo e dois do outro, como o fluoreto de cálcio: [p=0.1] {e}quatro ésse ao cubo."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o íon que aparece em dobro entra como dois ésse, ao quadrado, [p=0.1] {b}e dois ao quadrado dá quatro."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O iodeto de chumbo, um sólido amarelo, é pê bê i dois: [p=0.1] um chumbo e dois iodetos. [p=0.3] {b}Use cá pê ésse igual a quatro vezes dez elevado a menos nove. [p=0.3] {c}Qual é a solubilidade? [p=0.2] {d}E forma precipitado numa mistura com chumbo a dez elevado a menos dois [p=0.2] e iodeto a dez elevado a menos quatro?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}Um chumbo e dois iodetos: formato quatro ésse ao cubo. [p=0.2] {b}Quatro ésse ao cubo igual a quatro vezes dez elevado a menos nove: [p=0.1] {c}ésse ao cubo dá dez elevado a menos nove. [p=0.2] {d}Ésse dá dez elevado a menos três mol por litro."),
    dict(id="s19", block="resposta", text="{a}Na mistura: o chumbo, dez elevado a menos dois, [p=0.1] {b}vezes o iodeto ao quadrado, dez elevado a menos oito. [p=0.2] {c}O produto dá dez elevado a menos dez. [p=0.2] {d}É menor que quatro vezes dez elevado a menos nove: [p=0.1] {e}não forma precipitado, tudo continua dissolvido."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}cá pê ésse é o produto dos íons, com os coeficientes no expoente; [p=0.2] {b}dele sai a solubilidade, [p=0.1] {c}e, se o produto da mistura passar dele, forma precipitado."),
    dict(id="s21", block="fim", text="{a}Na próxima aula, você pratica o equilíbrio todo em questões de prova: [p=0.1] {b}deslocamento, pê agá e solubilidade. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
