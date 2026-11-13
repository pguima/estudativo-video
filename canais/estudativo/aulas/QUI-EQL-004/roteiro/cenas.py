# Estudativo · QUI-EQL-004 — Ácidos fracos: Ka e grau de ionização (Química · Equilíbrio Químico · pH, hidrólise, tampão e Kps).
# Habilidade: usar Ka e grau de ionização para achar o pH de um ácido fraco.
# Pré-requisitos: QUI-EQL-003, MAT-POR-002, QUI-INO-013. Próxima: QUI-EQL-005 (hidrólise salina).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; resultado de conta com "dá". Questão inédita, criada para esta aula.
# Leitura: Ka = "cá á", HA = "o ácido agá á", A⁻ = "o ânion á" (não "á menos", que se confunde com "elevado a menos"), M (concentração do ácido) = "ême", α = "alfa", pH = "pê agá".
# Fatos: ácido acético 0,1 mol/L tem α ≈ 1,3% e pH ≈ 2,9 ("perto de três"); HCl 0,1 mol/L, pH 1.
# Exemplo com Ka = 10⁻⁵ (ilustrativo; o acético real é 1,8 × 10⁻⁵): M = 10⁻¹ ⇒ α² = 10⁻⁴, α = 1%, [H⁺] = 10⁻³, pH 3.
# Lei de Ostwald (α pequeno): Ka ≈ α²·M; [H⁺] = α·M = √(Ka·M), válida até α ≈ 5%.
# Questão: M = 10⁻², Ka = 10⁻⁶ ⇒ α² = 10⁻⁴, α = 1%; [H⁺] = √10⁻⁸ = 10⁻⁴; pH 4.

TITULO = "Ácidos fracos: Ka e grau de ionização"

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
    dict(id="s01", block="gancho", text="{a}O ácido acético, o do vinagre, e o ácido clorídrico, na mesma concentração, [p=0.1] {b}não têm o mesmo pê agá. [p=0.3] {c}A zero vírgula um mol por litro, o clorídrico dá pê agá um. [p=0.2] {d}O acético fica perto de três. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai usar {a}o cá á [p=0.1] e {b}o grau de ionização [p=0.1] para {c}achar o pê agá de um ácido fraco."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar: [p=0.1] {a}o pê agá: agá mais igual a dez elevado a menos três dá pê agá três; [p=0.2] {b}o ácido fraco, que se ioniza pouco; [p=0.2] {c}porcentagem; [p=0.1] {d}e raiz quadrada de potências de dez. [p=0.2] Se faltar alguma, procure no canal."),
    # grau de ionização
    dict(id="s04", block="grau", text="{a}O ácido forte se ioniza todo. [p=0.2] {b}O fraco, só uma parte, e o resto fica inteiro. [p=0.3] {c}O grau de ionização mede essa parte: [p=0.1] {d}moléculas ionizadas divididas pelas dissolvidas. [p=0.2] {e}Se, de cada cem moléculas, uma se ioniza, o grau é um por cento."),
    dict(id="s05", block="grau", text="{a}Com o grau, sai o agá mais: [p=0.1] {b}a concentração do ácido vezes o grau. [p=0.3] {c}O ácido acético a zero vírgula um mol por litro tem grau perto de um por cento. [p=0.2] {d}Zero vírgula um vezes zero vírgula zero um {e}dá zero vírgula zero zero um, [p=0.1] {f}dez elevado a menos três: pê agá três."),
    # Ka
    dict(id="s06", block="ka", text="{a}Como é um equilíbrio, o ácido fraco tem constante: o cá á. [p=0.2] {b}Escreva o ácido como agá á, [p=0.1] {c}que solta agá mais e o ânion á. [p=0.3] {d}Cá á é agá mais vezes o ânion á, dividido pelo ácido agá á que ficou inteiro. [p=0.3] {e}Na mesma concentração, quanto maior o cá á, mais o ácido se ioniza, e mais forte ele é."),
    dict(id="s07", block="ka", text="{a}Pelo jeito de Brønsted, o ânion á é a base conjugada: [p=0.1] {b}o que sobra do ácido depois de soltar o agá mais. [p=0.2] Ele volta nas próximas aulas."),
    # Ostwald
    dict(id="s08", block="ostwald", text="{a}Dá para ligar o cá á com o grau, que se escreve alfa. [p=0.2] {b}Se o ácido tem concentração ême, [p=0.1] {c}o agá mais e o ânion á valem ême vezes alfa cada um. [p=0.2] {d}O que ficou inteiro é quase ême, porque alfa é pequeno. [p=0.3] {e}Então cá á é quase alfa ao quadrado vezes ême. [p=0.2] É a lei de Ostwald."),
    dict(id="s09", block="ostwald", text="{a}Exemplo: um ácido com cá á igual a dez elevado a menos cinco, [p=0.1] a zero vírgula um mol por litro, que é dez elevado a menos um. [p=0.3] {b}Alfa ao quadrado é cá á dividido por ême. [p=0.1] {c}Dez elevado a menos cinco dividido por dez elevado a menos um {d}dá dez elevado a menos quatro. [p=0.2] {e}Alfa é a raiz: dez elevado a menos dois, um por cento."),
    dict(id="s10", block="ostwald", text="{a}Agá mais: ême vezes alfa. [p=0.1] {b}Dez elevado a menos um vezes dez elevado a menos dois {c}dá dez elevado a menos três. [p=0.2] {d}Pê agá três, perto do ácido acético."),
    # erro comum
    dict(id="s11", block="erro", text="{a}O erro comum é tratar o ácido fraco como forte. [p=0.2] {b}Para o ácido do exemplo, a dez elevado a menos um mol por litro, isso daria pê agá um. [p=0.3] {c}Mas só um por cento se ionizou: [p=0.1] {d}o agá mais é cem vezes menor, e o pê agá é três."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.2] {a}o agá mais é a raiz de cá á vezes ême. [p=0.2] {b}Dez elevado a menos cinco vezes dez elevado a menos um dá dez elevado a menos seis; [p=0.1] {c}a raiz dá dez elevado a menos três. [p=0.3] {d}Com potência de dez de expoente par, tirar a raiz é só dividir o expoente por dois."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o agá mais é alfa vezes ême, [p=0.1] e alfa ao quadrado é cá á dividido por ême. [p=0.3] {b}Só vale para ácido fraco, com grau pequeno, até uns cinco por cento."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um ácido fraco está a zero vírgula zero um mol por litro, que é dez elevado a menos dois, [p=0.2] {b}com cá á igual a dez elevado a menos seis. [p=0.3] {c}Ache o grau de ionização [p=0.1] {d}e o pê agá."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Alfa ao quadrado: dez elevado a menos seis dividido por dez elevado a menos dois {b}dá dez elevado a menos quatro. [p=0.2] {c}Alfa: dez elevado a menos dois, um por cento. [p=0.3] {d}Agá mais: a raiz de dez elevado a menos seis vezes dez elevado a menos dois, [p=0.1] {e}que é a raiz de dez elevado a menos oito, [p=0.1] {f}dá dez elevado a menos quatro. [p=0.2] {g}Pê agá quatro."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}o ácido fraco se ioniza pouco; [p=0.1] {b}o agá mais é ême vezes alfa, [p=0.1] {c}e cá á é quase alfa ao quadrado vezes ême."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai ver que {a}até um sal pode deixar a água ácida ou básica: [p=0.2] {b}é a hidrólise salina, com a regra do forte vence. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
