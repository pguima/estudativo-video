# Estudativo · QUI-EQL-008 — Praticando: equilíbrio, pH e Kps (Química · Equilíbrio Químico · prática).
# Habilidade: prever deslocamentos e calcular pH e solubilidade em questões de prova.
# Pré-requisitos: QUI-EQL-001 a QUI-EQL-007 e QUI-EQL-009. Próxima: nenhuma na trilha.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; resultado de conta com "dá". Cinco questões inéditas.
# Q1 CO(g) + 2 H₂(g) ⇌ CH₃OH(g), ΔH < 0 (síntese do metanol): pressão ↑ ⇒ direita (3 → 1); aquecer ⇒ esquerda; catalisador ⇒ nada.
# Q2 PCl₅ ⇌ PCl₃ + Cl₂ em 1 L: início 1,0; equilíbrio Cl₂ 0,5 ⇒ 0,5 / 0,5 / 0,5 ⇒ Kc = 0,25 / 0,5 = 0,5; α = 50%.
# Q3 KOH 2 × 10⁻³ mol/L, log 2 = 0,3 ⇒ pOH 2,7, pH 11,3. Q4 acetato de sódio: base forte + ácido fraco ⇒ básico;
# tampão acético + acetato iguais, Ka = 2 × 10⁻⁵ ⇒ pH 4,7. Q5 AgCl, Kps = 1,0 × 10⁻¹⁰ (arredondado; tabela 1,8 × 10⁻¹⁰) ⇒ s = 10⁻⁵;
# mistura Ag⁺ 10⁻⁴ e Cl⁻ 10⁻⁴ ⇒ Q = 10⁻⁸ > Kps ⇒ precipita.

TITULO = "Praticando: equilíbrio, pH e Kps"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões para fechar o equilíbrio. [p=0.2] {b}Deslocamento, cá cê, pê agá, tampão e solubilidade. [p=0.3] {c}Em cada uma, pause, tente, e só depois veja a resolução."),
    # lembrete: a caixa de ferramentas
    dict(id="s02", block="lembrete", text="{a}A caixa de ferramentas: [p=0.2] {b}o equilíbrio foge da perturbação. [p=0.2] {c}No cá cê, só entra a linha do equilíbrio. [p=0.2] {d}Pê agá mais pê ó agá dá catorze. [p=0.2] {e}O forte vence na hidrólise, [p=0.1] e o tampão com ácido e sal iguais tem pê agá igual ao pê cá á. [p=0.2] {f}E o cá pê ésse é o produto dos íons."),
    # questão 1: Le Chatelier
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] {b}O metanol se forma no equilíbrio: [p=0.1] cê ó mais dois agá dois, formando cê agá três ó agá, [p=0.1] tudo gás, com delta agá negativo. [p=0.3] Para que lado o equilíbrio vai [p=0.1] {c}se a pressão aumentar? [p=0.2] {d}Se esquentar? [p=0.2] {e}E com um catalisador?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="{a}Pressão: são três moléculas de gás à esquerda e uma à direita. [p=0.1] {b}Pressão alta vai para o lado de menos gás: direita, mais metanol. [p=0.3] {c}Temperatura: delta agá negativo, a ida libera calor. [p=0.1] {d}Esquentar favorece a volta, que absorve calor: esquerda. [p=0.3] {e}Catalisador: não desloca, só faz chegar mais rápido."),
    # questão 2: Kc pelo quadro
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] {b}Num frasco de um litro, há um mol de pê cê éle cinco, [p=0.1] que se decompõe em pê cê éle três e cê éle dois. [p=0.3] {c}No equilíbrio, há zero vírgula cinco mol de cê éle dois. [p=0.2] {d}Calcule o cá cê e o grau de equilíbrio."),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="r2", text="{a}Um litro: os mols já são mol por litro. [p=0.2] {b}Formou zero vírgula cinco de cê éle dois; [p=0.1] {c}os coeficientes são todos um, [p=0.1] então também se formou zero vírgula cinco de pê cê éle três, [p=0.1] {d}e reagiu zero vírgula cinco de pê cê éle cinco. [p=0.2] {e}Sobra zero vírgula cinco dele."),
    dict(id="s09", block="r2", text="{a}Cá cê: zero vírgula cinco vezes zero vírgula cinco dá zero vírgula vinte e cinco. [p=0.2] {b}Dividido por zero vírgula cinco, {c}dá zero vírgula cinco. [p=0.3] {d}Grau: reagiu zero vírgula cinco de um, {e}cinquenta por cento."),
    # questão 3: pH de base com log 2
    dict(id="s10", block="q3", text="{a}Questão três. [p=0.2] {b}Uma solução de hidróxido de potássio, uma base forte, [p=0.1] tem dois vezes dez elevado a menos três mol por litro. [p=0.3] {c}Use log de dois igual a zero vírgula três. [p=0.2] {d}Qual é o pê agá?"),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="{a}Base forte libera tudo: o ó agá menos é dois vezes dez elevado a menos três. [p=0.3] {b}Isso dá o pê ó agá, não o pê agá: [p=0.1] {c}três menos zero vírgula três dá dois vírgula sete. [p=0.3] {d}Pê agá: catorze menos dois vírgula sete {e}dá onze vírgula três. [p=0.2] {f}Acima de sete, como toda base."),
    # questão 4: hidrólise e tampão
    dict(id="s13", block="q4", text="{a}Questão quatro. [p=0.2] {b}O acetato de sódio deixa a água ácida, neutra ou básica? [p=0.3] {c}E uma mistura de ácido acético com acetato de sódio, na mesma concentração, [p=0.1] {d}com cá á igual a dois vezes dez elevado a menos cinco: qual é o pê agá? [p=0.2] Use de novo log de dois igual a zero vírgula três."),
    dict(id="s14", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="r4", text="{a}Os pais do acetato de sódio: hidróxido de sódio, forte, e ácido acético, fraco. [p=0.1] {b}O forte vence: básica. [p=0.3] {c}A mistura é um tampão: ácido fraco com o seu sal, na mesma concentração. [p=0.2] {d}Pê agá igual a pê cá á: [p=0.1] {e}cinco menos zero vírgula três {f}dá quatro vírgula sete."),
    # questão 5: Kps
    dict(id="s16", block="q5", text="{a}Questão cinco. [p=0.2] {b}O cloreto de prata, á gê cê éle, tem cá pê ésse igual a um vezes dez elevado a menos dez. [p=0.3] {c}Qual é a solubilidade? [p=0.2] {d}E forma precipitado numa mistura com prata e cloreto, cada um a dez elevado a menos quatro?"),
    dict(id="s17", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="r5", text="{a}Um íon de cada: cá pê ésse igual a ésse ao quadrado. [p=0.2] {b}Ésse é a raiz de dez elevado a menos dez: [p=0.1] {c}dez elevado a menos cinco mol por litro. [p=0.3] {d}Na mistura, o produto dá dez elevado a menos oito. [p=0.2] {e}Maior que dez elevado a menos dez: [p=0.1] {f}forma precipitado."),
    # fechamento
    dict(id="s19", block="fim", text="{a}Se você acertou três das cinco, o equilíbrio está no lugar. [p=0.2] {b}Errou alguma? [p=0.1] Volte na aula daquela ferramenta e refaça a questão."),
    dict(id="s20", block="fim", text="{a}Com isso, a trilha de equilíbrio químico termina. [p=0.2] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
