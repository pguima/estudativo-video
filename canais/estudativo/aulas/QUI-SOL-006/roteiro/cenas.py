# Estudativo · QUI-SOL-006 — Titulação: descobrir a concentração (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: achar a concentração de um ácido pelo volume de NaOH gasto, inclusive quando a proporção não é 1:1, e dizer o
# que é ponto de viragem.
# Pré-requisitos: QUI-SOL-004, QUI-CAL-005, QUI-INO-003, QUI-INO-005. Próxima: QUI-SOL-007 (praticando).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: fenolftaleína é incolor em meio ácido e neutro e rosa em meio básico (vira por volta de pH 8 a 10). Bureta mede o volume
# gota a gota; o ácido fica no erlenmeyer. Vinagre comum: cerca de 4% de ácido acético, perto de 0,7 a 0,8 mol/L.
# Contas: 1:1 → 0,1 × 25 = 2,5 = Ma × 20 → Ma = 0,125 mol/L.
# 1:2 (H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O): 0,1 mol/L × 0,020 L = 0,002 mol de NaOH → 0,001 mol de H₂SO₄ ÷ 0,010 L = 0,1 mol/L;
# sem o fator, 0,2 mol/L (erro). Atalho: 2 × Ma × 10 = 1 × 0,1 × 20 → Ma = 0,1.
# Questão: CH₃COOH (1 H ionizável) 10 mL, 16 mL de NaOH 0,5 mol/L → 0,5 × 16 = 8 = Ma × 10 → 0,8 mol/L.

TITULO = "Titulação: descobrir a concentração"

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
    dict(id="s01", block="gancho", text="{a}Quanto ácido tem neste vinagre? [p=0.3] Não existe régua de ácido. [p=0.2] {b}Mas existe um jeito: [p=0.1] {c}pingar uma base, gota a gota, [p=0.2] {d}até a cor mudar de repente. [p=0.3] {e}O volume gasto conta a resposta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai fazer {b}a conta da titulação, [p=0.2] {c}inclusive com ácidos de dois hidrogênios, [p=0.2] e {d}saber o que é o ponto de viragem."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de três coisas. [p=0.2] {a}Ácido com base dá sal e água: é a neutralização. [p=0.3] {b}Mols são a concentração vezes o volume em litros. [p=0.3] {c}E a fenolftaleína é incolor no ácido e rosa na base."),
    # a montagem
    dict(id="s04", block="montagem", text="{a}Titular é descobrir a concentração de uma solução fazendo ela reagir com outra que você conhece. [p=0.3] {b}No frasco de baixo, o erlenmeyer, fica o ácido, [p=0.1] com volume medido [p=0.1] {c}e umas gotas de fenolftaleína. [p=0.3] {d}Em cima, num tubo com torneira e marcas de volume, a bureta, [p=0.1] {e}fica a base de concentração conhecida."),
    dict(id="s05", block="montagem", text="{a}Abra a torneira. [p=0.2] Cada gota de base neutraliza um pouco do ácido. [p=0.3] {b}Enquanto sobra ácido, a fenolftaleína fica incolor. [p=0.3] {c}Quando o ácido acaba, a gota seguinte deixa o meio básico, e o líquido fica rosa. [p=0.3] {d}Esse instante em que a cor muda é o ponto de viragem. [p=0.2] Feche a torneira e leia o volume gasto."),
    dict(id="s06", block="montagem", text="{a}O ponto exato em que ácido e base se igualam, sem sobra, se chama ponto de equivalência. [p=0.3] {b}Com o indicador certo, a cor vira praticamente nele."),
    # conta 1:1
    dict(id="s07", block="conta", text="Agora, a conta. [p=0.2] {a}Ácido clorídrico com soda cáustica: [p=0.1] {b}um para um. [p=0.2] {c}Cada partícula de ácido gasta uma de base. [p=0.3] {d}Então, no ponto de equivalência, os mols de ácido são iguais aos mols de base."),
    dict(id="s08", block="conta", text="{a}Mols são concentração vezes volume, [p=0.1] então {b}a concentração do ácido vezes o volume do ácido [p=0.1] {c}é igual à da base vezes o volume da base."),
    dict(id="s09", block="conta", text="{a}Vinte mililitros de ácido gastaram vinte e cinco de soda com zero vírgula um mol por litro. [p=0.3] {b}Zero vírgula um vezes vinte e cinco dá dois vírgula cinco. [p=0.2] {c}Dois vírgula cinco dividido por vinte [p=0.1] {d}dá zero vírgula cento e vinte e cinco mol por litro. [p=0.3] {e}Os volumes ficam em mililitros, porque estão dos dois lados."),
    # proporção diferente
    dict(id="s10", block="dois", text="{a}E o ácido sulfúrico? [p=0.2] Ele tem {b}dois hidrogênios que saem. [p=0.3] {c}A equação balanceada mostra: [p=0.1] {d}cada partícula de ácido sulfúrico gasta duas de soda. [p=0.3] {e}A proporção é um para dois."),
    dict(id="s11", block="dois", text="{a}Dez mililitros de ácido sulfúrico gastaram vinte de soda com zero vírgula um mol por litro. [p=0.3] {b}Com os volumes em mililitros, como antes: [p=0.1] zero vírgula um vezes vinte dá dois. [p=0.3] {c}O ácido gasta a metade das partículas de soda: [p=0.1] a metade de dois dá um. [p=0.3] {d}Um dividido pelos dez mililitros de ácido [p=0.1] {e}dá zero vírgula um mol por litro."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum: [p=0.2] {a}usar um para um em tudo. [p=0.3] {b}Quem esquece o dois do ácido sulfúrico faz zero vírgula um vezes vinte, dividido por dez, [p=0.1] {c}e marca zero vírgula dois mol por litro. [p=0.3] {d}O dobro do certo. [p=0.2] {e}Escreva a equação balanceada antes da conta."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}conte os hidrogênios que saem do ácido [p=0.1] e {b}as hidroxilas, os ó agá, da base. [p=0.3] {c}O número de hidrogênios vai na frente do lado do ácido, [p=0.1] {d}o de hidroxilas, na frente do lado da base. [p=0.3] {e}Para o ácido sulfúrico: [p=0.1] dois vezes a concentração vezes dez é igual a um vezes zero vírgula um vezes vinte. [p=0.3] {f}Vinte vezes a concentração é igual a dois: [p=0.1] a concentração dá zero vírgula um."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada hidrogênio do ácido encontra um ó agá da base e vira água. [p=0.3] {b}Cuidado quando nem todo hidrogênio sai. [p=0.2] {c}O ácido do vinagre tem quatro hidrogênios, [p=0.1] {d}mas só um se solta na água. [p=0.3] Conte só os que saem, [p=0.1] e, na dúvida, escreva a equação."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Dez mililitros de vinagre, com fenolftaleína, [p=0.1] {b}gastaram dezesseis mililitros de soda com zero vírgula cinco mol por litro [p=0.1] {c}até ficar rosa. [p=0.3] O ácido do vinagre é o ácido acético. [p=0.2] {d}Qual é a concentração dele, em mol por litro?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}O ácido acético solta só um hidrogênio, e a soda tem um ó agá: [p=0.1] {b}é um para um. [p=0.3] {c}Zero vírgula cinco vezes dezesseis dá oito. [p=0.2] {d}Oito dividido por dez [p=0.1] {e}dá zero vírgula oito mol por litro. [p=0.3] {f}Quem contou os quatro hidrogênios chegou a zero vírgula dois, errado."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}na titulação, a base conhecida descobre o ácido; [p=0.2] {b}a cor vira no ponto de viragem; [p=0.1] e {c}os hidrogênios do ácido e as hidroxilas da base entram na conta."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai {a}praticar tudo do módulo: [p=0.2] {b}rótulos, laudos de água, curvas, diluição e titulação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
