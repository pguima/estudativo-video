# Estudativo · QUI-EQL-003 — Produto iônico da água, pH e pOH (Química · Equilíbrio Químico · pH, hidrólise, tampão e Kps).
# Habilidade: calcular o pH de HCl 0,001 mol/L, usar pH + pOH = 14 e achar um pH com log 2.
# Pré-requisitos: QUI-EQL-001, QUI-INO-005, MAT-EXP-010, MAT-EXP-014. Próxima: QUI-EQL-004 (ácidos fracos: Ka e α).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; resultado de conta com "dá". Questão inédita, criada para esta aula.
# Primeira aula do módulo pH: o cabeçalho do visual.py guarda a linguagem visual (escala de pH, íons H⁺ e OH⁻).
# Leitura: pH = "pê agá", pOH = "pê ó agá", Kw = "cá dáblio", H⁺ = "agá mais", OH⁻ = "ó agá menos". Só potências de 10 exatas e
# log 2 = 0,3, como a ficha pede. Fatos (25 °C): Kw = 10⁻¹⁴; água pura [H⁺] = 10⁻⁷ (1 L ≈ 55,5 mol de água ⇒ ~1 em 550 milhões);
# limão pH ≈ 2 ⇒ 10⁵ vezes mais H⁺ que a água pura. HCl 0,001 ⇒ pH 3; NaOH 0,01 ⇒ pOH 2, pH 12; 2·10⁻³ ⇒ pH 2,7;
# questão 2·10⁻⁴ ⇒ pH 3,7, pOH 10,3.

TITULO = "Produto iônico da água, pH e pOH"

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
    dict(id="s01", block="gancho", text="{a}O suco de limão tem pê agá perto de dois. [p=0.2] {b}A água pura, sete. [p=0.3] {c}Parece pouca diferença, [p=0.1] {d}mas o limão tem cem mil vezes mais íons agá mais. [p=0.3] {e}De onde sai esse número?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}calcular o pê agá de uma solução de ácido, [p=0.2] {b}usar pê agá mais pê ó agá igual a catorze [p=0.2] e {c}achar um pê agá com o log de dois."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar: [p=0.1] {a}a escala de pê agá, de zero a catorze, com o sete neutro; [p=0.2] {b}o ácido forte, que se ioniza todo na água; [p=0.2] {c}o logaritmo: log de dez elevado a menos três dá menos três; [p=0.2] {d}e o log de dois, perto de zero vírgula três. [p=0.2] Se faltar alguma, procure no canal."),
    # a água se ioniza
    dict(id="s04", block="agua", text="{a}Até a água pura se ioniza, só um pouquinho. [p=0.2] {b}Agá dois ó, em equilíbrio com agá mais e ó agá menos. [p=0.3] {c}Em cada litro, há só dez elevado a menos sete mol de cada íon. [p=0.2] {d}É mais ou menos uma molécula ionizada em cada quinhentos e cinquenta milhões."),
    dict(id="s05", block="agua", text="{a}É um equilíbrio, então tem constante. [p=0.2] {b}A água líquida fica de fora, [p=0.1] {c}e sobra o produto iônico da água, o cá dáblio: [p=0.1] {d}a concentração do íon agá mais, vezes a do íon ó agá menos. [p=0.3] {e}A vinte e cinco graus Celsius, ele vale dez elevado a menos catorze."),
    dict(id="s06", block="agua", text="{a}A vinte e cinco graus, esse produto vale para qualquer solução em água. [p=0.2] {b}Se o agá mais sobe, o ó agá menos desce, [p=0.1] {c}e a multiplicação continua dando dez elevado a menos catorze."),
    # pH e pOH
    dict(id="s07", block="ph", text="{a}Para não escrever potências o tempo todo, existe o pê agá: [p=0.1] {b}menos o log da concentração de agá mais. [p=0.3] {c}Com uma potência de dez exata, é fácil: [p=0.1] {d}agá mais igual a dez elevado a menos três dá pê agá três. [p=0.2] {e}O menos do log cancela o menos do expoente."),
    dict(id="s08", block="ph", text="{a}Do mesmo jeito, o pê ó agá é menos o log da concentração do íon ó agá menos. [p=0.3] {b}O produto dos dois íons dá dez elevado a menos catorze, [p=0.1] {c}e, quando se multiplicam potências de dez, os expoentes se somam. [p=0.2] {d}Por isso, pê agá mais pê ó agá dá sempre catorze."),
    # exemplos
    dict(id="s09", block="exemplo", text="{a}Agora, o ácido clorídrico, agá cê éle, a zero vírgula zero zero um mol por litro. [p=0.3] {b}É um ácido forte: ioniza tudo. [p=0.2] {c}Então o agá mais também é zero vírgula zero zero um, [p=0.1] {d}que é dez elevado a menos três. [p=0.2] {e}Pê agá três."),
    dict(id="s10", block="exemplo", text="{a}Agora uma base forte, o hidróxido de sódio, a zero vírgula zero um mol por litro. [p=0.3] {b}Ela libera ó agá menos: [p=0.1] dez elevado a menos dois. [p=0.2] {c}Isso dá o pê ó agá: dois. [p=0.2] {d}O pê agá é catorze menos dois, {e}que dá doze. [p=0.1] Básico, como deve ser."),
    # erro comum
    dict(id="s11", block="erro", text="{a}É aqui que mora o erro comum: [p=0.1] {b}fazer a conta com o ó agá menos e chamar o resultado de pê agá. [p=0.2] {c}A pessoa acha pê agá dois para o hidróxido de sódio, [p=0.1] {d}o que seria uma solução bem ácida. [p=0.3] {e}Base dá o pê ó agá primeiro; [p=0.1] o pê agá vem de catorze menos ele."),
    # com log 2
    dict(id="s12", block="log", text="{a}E quando o número não é uma potência de dez exata? [p=0.2] {b}A concentração de agá mais é dois vezes dez elevado a menos três. [p=0.3] {c}O log de um produto é a soma dos logs: [p=0.1] {d}log de dois, zero vírgula três, [p=0.1] {e}mais o log de dez elevado a menos três, menos três. [p=0.2] {f}Dá menos dois vírgula sete. [p=0.2] {g}O pê agá é o oposto: dois vírgula sete."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho: [p=0.2] {a}concentração de um vezes dez elevado a menos ene dá pê agá ene. [p=0.2] {b}Na forma decimal, conte as casas depois da vírgula até o um: [p=0.1] {c}zero vírgula zero zero um tem três casas, pê agá três. [p=0.3] {d}Com dois na frente, tire zero vírgula três: [p=0.1] {e}dois vezes dez elevado a menos três dá pê agá dois vírgula sete."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o pê agá conta as potências de dez. [p=0.2] {b}Com outro número na frente, como três ou cinco, [p=0.1] use o log que a questão der."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma solução tem concentração de agá mais igual a dois vezes dez elevado a menos quatro mol por litro. [p=0.3] {b}Use log de dois igual a zero vírgula três. [p=0.2] {c}Qual é o pê agá? [p=0.2] {d}E o pê ó agá?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}Sem o dois, seria pê agá quatro. [p=0.2] {b}Com o dois na frente, tire zero vírgula três: [p=0.1] {c}pê agá três vírgula sete. [p=0.3] {d}Pê ó agá: catorze menos três vírgula sete {e}dá dez vírgula três. [p=0.2] {f}Solução ácida, porque o pê agá ficou abaixo de sete."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}na água, a concentração do íon agá mais, vezes a do íon ó agá menos, dá dez elevado a menos catorze; [p=0.2] {b}o pê agá conta as potências de dez [p=0.1] {c}e pê agá mais pê ó agá dá catorze."),
    dict(id="s19", block="fim", text="Na próxima aula, os ácidos que não se ionizam por inteiro: {a}os ácidos fracos, [p=0.1] {b}com o cá á e o grau de ionização. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
