# Estudativo · MAT-CNT-002 — Contar com restrições: comece pelo mais difícil (Matemática · Contagem e Probabilidade).
# Habilidade: contar quantos números de 3 algarismos distintos existem (648), preenchendo primeiro a casa com restrição, e saber quando somar casos.
# Pré-requisitos: MAT-CNT-001 (princípio multiplicativo, casinhas). Próxima: MAT-CNT-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Mesmos termos da MAT-CNT-001: casinhas, etapas, princípio multiplicativo.
# 3 algarismos distintos: centena 9 (1 a 9) · dezena 9 (10 − 1) · unidade 8 (10 − 2) → 9 × 9 = 81; 81 × 8 = 648.
# Começando pela unidade: 10 × 9 e a centena fica 8 (se o zero já saiu) ou 7 (se não saiu).
# Casos (terminam em 0 ou 5): termina em 0 → 9 × 8 = 72 · termina em 5 → 8 × 8 = 64 · 72 + 64 = 136.
# Erro: 10 × 9 × 8 = 720 (conta 047 etc.). Atalho: com zero na frente 1 × 9 × 8 = 72; 720 − 72 = 648.
# Questão: pares de 2 algarismos distintos: termina em 0 → 9 · termina em 2, 4, 6, 8 → 4 × 8 = 32 · 9 + 32 = 41.

TITULO = "Contar com restrições: comece pelo mais difícil"

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
    dict(id="s01", block="gancho", text="{a}Quantos números de três algarismos têm {b}todos os algarismos diferentes? [p=0.3] Muita gente faz {c}dez vezes nove vezes oito, [p=0.2] que dá setecentos e vinte. [p=0.3] {d}Errou. [p=0.2] São {e}seiscentos e quarenta e oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta com regras no meio do caminho, [p=0.2] sabe {b}por qual casinha começar [p=0.2] e {c}quando somar em vez de multiplicar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre do {a}princípio multiplicativo: [p=0.2] {b}uma casinha para cada etapa, [p=0.2] {c}quantas opções cabem em cada uma, [p=0.2] e {d}multiplique. [p=0.3] Se faltar, procure no canal."),
    # as regras
    dict(id="s04", block="regras", text="Um número de três algarismos tem {a}três casinhas: [p=0.2] {b}centena, dezena e unidade. [p=0.3] E aqui há regras. [p=0.2] {c}Algarismo não pode repetir. [p=0.2] E {d}o zero não pode ficar na frente: [p=0.2] {e}zero quarenta e sete é só quarenta e sete, um número de dois algarismos."),
    # comece pelo mais difícil
    dict(id="s05", block="casinhas", text="Qual casinha tem mais regra? [p=0.2] {a}A da centena, [p=0.2] porque ela não aceita o zero. [p=0.3] Então {b}comece por ela. [p=0.2] Ela tem {c}nove opções: de um a nove."),
    dict(id="s06", block="casinhas", text="Depois, {a}a dezena. [p=0.2] Ela aceita o zero, [p=0.2] mas {b}não aceita o algarismo que foi para a centena. [p=0.3] Dez menos um dá {c}nove opções."),
    dict(id="s07", block="casinhas", text="Por último, {a}a unidade. [p=0.2] Já foi usado {b}um algarismo na centena e outro na dezena. [p=0.2] Dez menos dois dá {c}oito opções."),
    dict(id="s08", block="casinhas", text="{a}Nove vezes nove dá oitenta e um. [p=0.2] {b}Oitenta e um vezes oito dá seiscentos e quarenta e oito."),
    dict(id="s09", block="casinhas", text="E se você começasse pela unidade? [p=0.2] {a}Dez opções, [p=0.2] depois {b}nove na dezena. [p=0.3] Na centena, {c}a conta trava: [p=0.2] se o zero já foi usado, sobram oito; [p=0.2] se não foi, só sete. [p=0.3] Por isso, {d}comece pela casinha mais difícil."),
    # casos
    dict(id="s10", block="casos", text="Às vezes, nem começando pela difícil a conta fecha. [p=0.2] Veja: {a}números de três algarismos diferentes [p=0.2] {b}que terminam em zero ou em cinco."),
    dict(id="s11", block="casos", text="A casinha difícil é {a}a unidade: [p=0.2] só aceita zero ou cinco. [p=0.3] Mas a escolha dela {b}muda a centena. [p=0.2] Então {c}separe em casos."),
    dict(id="s12", block="casos", text="{a}Caso um: termina em zero. [p=0.2] A centena tem {b}nove opções, [p=0.2] e a dezena tem {c}oito. [p=0.2] Nove vezes oito dá {d}setenta e dois."),
    dict(id="s13", block="casos", text="{a}Caso dois: termina em cinco. [p=0.2] A centena não aceita {b}nem o zero nem o cinco: [p=0.2] fica com {c}oito opções. [p=0.2] A dezena aceita o zero, mas não os algarismos já usados: [p=0.2] {d}oito também. [p=0.2] Oito vezes oito dá {e}sessenta e quatro."),
    dict(id="s14", block="casos", text="Cada número cai {a}em um caso só: [p=0.2] ou termina em zero, ou termina em cinco. [p=0.3] Casos que não acontecem juntos {b}se somam. [p=0.2] {c}Setenta e dois mais sessenta e quatro dá cento e trinta e seis."),
    dict(id="s15", block="casos", text="A palavra {a}ou ajuda, mas não decide sozinha. [p=0.2] Pergunte: [p=0.2] {b}eu faço todas as etapas? Multiplique. [p=0.2] {c}Cada resultado cai em um caso só? Some os casos."),
    # erro
    dict(id="s16", block="erro", text="O erro do começo foi {a}deixar o zero ir para qualquer lugar. [p=0.3] Dez vezes nove vezes oito conta também os que começam com zero, [p=0.2] como {b}zero quarenta e sete. [p=0.3] Esses {c}não têm três algarismos de verdade."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}conte tudo e tire o que não pode. [p=0.3] {b}Sem a regra do zero, dá setecentos e vinte. [p=0.2] Os que começam com zero têm {c}uma opção na centena, nove na dezena e oito na unidade: [p=0.2] dá {d}setenta e dois. [p=0.3] {e}Setecentos e vinte menos setenta e dois dá seiscentos e quarenta e oito."),
    dict(id="s18", block="atalho", text="Funciona porque {a}cada número da conta grande ou é proibido, ou não é. [p=0.3] Compensa quando {b}o proibido é fácil de contar. [p=0.2] {c}Quando o proibido se espalha em muitos casos, conte direto."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}Quantos números de dois algarismos diferentes são pares? [p=0.3] Lembre: número par termina em {b}zero, [p=0.2] dois, [p=0.2] quatro, [p=0.2] seis ou oito."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] A unidade é a casinha difícil, e o zero muda a dezena: [p=0.2] {a}separe em casos. [p=0.3] {b}Termina em zero: [p=0.2] a dezena tem nove opções, de um a nove. [p=0.2] São {c}nove números."),
    dict(id="s22", block="resposta", text="{a}Termina em dois, [p=0.2] quatro, [p=0.2] seis ou oito: [p=0.2] quatro opções na unidade. [p=0.2] A dezena não aceita {b}o zero nem o algarismo da unidade: [p=0.2] {c}oito opções. [p=0.2] Quatro vezes oito dá {d}trinta e dois. [p=0.3] Os casos não acontecem juntos: [p=0.2] {e}nove mais trinta e dois dá quarenta e um."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}comece pela casinha mais difícil. [p=0.3] {b}Se ela muda as outras, separe em casos e some."),
    dict(id="s24", block="fim", text="Na próxima aula, as casinhas servem para outra coisa: [p=0.2] {a}contar quantos divisores um número tem, [p=0.2] como o {b}setenta e dois, sem listar nenhum. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
