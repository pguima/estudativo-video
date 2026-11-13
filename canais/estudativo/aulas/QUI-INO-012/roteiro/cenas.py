# Estudativo · QUI-INO-012 — Praticando: reações e balanceamento (Química · Funções e Reações Inorgânicas · Reações e balanceamento).
# Habilidade: balancear equações e prever o produto de cada tipo de reação.
# Pré-requisitos: QUI-INO-007, 008, 009, 010, 011. Próxima: nenhuma na trilha (última aula da trilha).
# Aula de prática: cinco questões inéditas, cobrindo o módulo. Q5: 2 H₂ + O₂ → 2 H₂O, 4 g + 32 g = 36 g; C com pouco O₂ → CO.
# Fatos e contas: 2 C₄H₁₀ + 13 O₂ → 8 CO₂ + 10 H₂O (soma 33; o oxigênio dá 13, ímpar, e se dobra).
# CaCO₃ → CaO + CO₂ (análise); 2 H₂ + O₂ → 2 H₂O (síntese); Zn + 2 HCl → ZnCl₂ + H₂ (simples troca);
# AgNO₃ + NaCl → AgCl + NaNO₃ (dupla troca). Fe + 2 HCl → FeCl₂ + H₂ (ferro antes do H: reage); Cu + Zn²⁺: não reage.
# KCl + AgNO₃ → AgCl↓ + KNO₃ (reage); Na₂SO₄ + KNO₃: não reage (NaNO₃ e K₂SO₄ solúveis).

TITULO = "Praticando: reações e balanceamento"

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
    dict(id="s01", block="gancho", text="{a}Equação para balancear, [p=0.1] {b}reações para classificar [p=0.1] {c}e misturas para prever. [p=0.3] {d}Hoje são cinco questões que juntam o módulo inteiro."),
    # lembrete
    dict(id="s02", block="lembrete", text="As ferramentas: [p=0.1] {a}balancear na ordem metal, ametal, carbono, hidrogênio e oxigênio. [p=0.2] {b}Na simples troca, a fila de reatividade. [p=0.2] {c}Na dupla troca, um precipitado, um gás ou água."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] {a}Balanceie a queima completa do butano, o gás do isqueiro: [p=0.2] {b}cê quatro agá dez, mais ó dois, produz cê ó dois mais agá dois ó. [p=0.3] {c}Qual é a soma dos coeficientes?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Vamos lá. [p=0.2] {a}Carbono: quatro à esquerda, quatro cê ó dois. [p=0.2] {b}Hidrogênio: dez à esquerda, cinco águas. [p=0.3] {c}Oxigênio à direita: quatro vezes dois, oito, mais cinco, dá treze. [p=0.2] {d}Treze é ímpar, e o ó dois vem de dois em dois."),
    dict(id="s06", block="r1", text="{a}Use o atalho: dobre quem deu ímpar, as cinco águas, que viram dez. [p=0.2] {b}Refaça: dez águas pedem dois butanos, e dois butanos, oito cê ó dois. [p=0.2] {c}Oxigênio à direita: dezesseis mais dez, vinte e seis, [p=0.1] {d}e treze ó dois dão vinte e seis. [p=0.3] {e}Dois, mais treze, mais oito, mais dez: [p=0.1] a soma dá trinta e três."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] Classifique cada reação. [p=0.2] {a}Calcário aquecido vira cal e gás carbônico. [p=0.2] {b}Hidrogênio e oxigênio formam água. [p=0.2] {c}Zinco no ácido clorídrico solta hidrogênio. [p=0.2] {d}Nitrato de prata com cloreto de sódio forma cloreto de prata."),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="Vamos lá. [p=0.2] {a}Uma vira duas: análise. [p=0.2] {b}Duas viram uma: síntese, e também uma queima. [p=0.3] {c}O zinco, sozinho, tomou o lugar do hidrogênio: simples troca. [p=0.3] {d}Dois compostos trocaram de parceiros: dupla troca."),
    # questão 3
    dict(id="s10", block="q3", text="Questão três. [p=0.2] Use a fila de reatividade da tela. [p=0.2] {a}Um prego de ferro no ácido clorídrico reage? [p=0.3] {b}E um fio de cobre numa solução com íons de zinco?"),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="Vamos lá. [p=0.2] {a}O ferro está antes do hidrogênio: reage. [p=0.1] {b}Forma o íon de ferro e solta gás hidrogênio. [p=0.3] {c}O cobre está depois do zinco: é menos reativo. [p=0.1] {d}Não toma o lugar dele, e não há reação."),
    # questão 4
    dict(id="s13", block="q4", text="Questão quatro. [p=0.2] Diga se há reação. [p=0.2] {a}Cloreto de potássio com nitrato de prata. [p=0.3] {b}E sulfato de sódio com nitrato de potássio."),
    dict(id="s14", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="r4", text="Vamos lá. [p=0.2] {a}Na primeira, os produtos seriam cloreto de prata e nitrato de potássio. [p=0.2] {b}O nitrato de potássio se dissolve, [p=0.1] {c}mas o cloreto de prata não: [p=0.1] {d}precipita, e há reação."),
    dict(id="s16", block="r4", text="{a}Na segunda, os produtos seriam nitrato de sódio e sulfato de potássio. [p=0.2] {b}Os dois são de sódio, de potássio ou nitrato: [p=0.1] {c}os dois se dissolvem. [p=0.2] {d}Sem precipitado, sem gás e sem água: não há reação."),
    # questão 5
    dict(id="s17", block="q5", text="Questão cinco. [p=0.2] {a}Num frasco fechado, quatro gramas de hidrogênio queimam com trinta e dois gramas de oxigênio, [p=0.1] e não sobra nada. [p=0.3] {b}Qual é a massa de água formada? [p=0.3] E {c}se o carvão queimar com pouco oxigênio, qual gás tóxico pode sair?"),
    dict(id="s18", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="r5", text="Vamos lá. [p=0.2] {a}Frasco fechado: vale Lavoisier. [p=0.2] {b}Quatro mais trinta e dois dá trinta e seis gramas de água. [p=0.3] {c}E com pouco oxigênio a queima é incompleta: [p=0.1] {d}sai o monóxido de carbono, cê ó."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}conte os átomos para balancear, [p=0.1] {b}conte as substâncias e veja quem troca de lugar para classificar, [p=0.1] e {c}procure a fila ou o precipitado para prever."),
    dict(id="s21", block="fim", text="Com isso, você fechou a trilha de ácidos, bases, sais e reações. [p=0.2] {a}Agora você já lê, balanceia e prevê uma reação. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
