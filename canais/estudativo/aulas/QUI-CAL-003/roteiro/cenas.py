# Estudativo · QUI-CAL-003 — Composição percentual e fórmula mínima (Química · Cálculos Químicos · Mol e massa molar).
# Habilidade: calcular que o NH₄NO₃ tem 35% de nitrogênio e chegar à fórmula mínima CH₂O da glicose.
# Pré-requisitos: QUI-CAL-002, MAT-POR-003. Próxima: QUI-CAL-004 (lei de Proust e proporção em mols).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: NH₄NO₃ = 2·14 + 4·1 + 3·16 = 80; 28/80 = 0,35; erro 14/80 = 17,5%. Glicose: 40% C, 6,7% H, 53,3% O (soma 100);
# 40/12 ≈ 3,33; 6,7/1 = 6,7; 53,3/16 ≈ 3,33 → 1 : 2 : 1 → CH₂O = 30; 180/30 = 6. Questão: C₄H₁₀ → C₂H₅; CH₄: 12/16 = 75%.
# Fatos: nitrato de amônio é adubo nitrogenado; o butano está no gás de cozinha (GLP, com o propano).

TITULO = "Composição percentual e fórmula mínima"

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
    dict(id="s01", block="gancho", text="{a}No saco de adubo está escrito: nitrato de amônio, [p=0.1] {b}ene agá quatro ene ó três. [p=0.3] {c}Quanto desse pó é nitrogênio, o nutriente que a planta quer? [p=0.2] {d}Trinta e cinco por cento. [p=0.3] E você vai chegar nesse número sozinho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a porcentagem de cada elemento numa substância, [p=0.2] {c}achar a fórmula mais simples dela, a fórmula mínima, [p=0.2] e ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a massa molar, como os dezoito gramas por mol da água, [p=0.2] e {c}descobrir quantos por cento uma parte é do total: [p=0.1] trinta de cento e vinte são vinte e cinco por cento. [p=0.3] Se faltar alguma, procure no canal."),
    # composição percentual
    dict(id="s04", block="percentual", text="{a}A composição percentual diz quanto da massa de uma substância vem de cada elemento. [p=0.3] {b}É a massa do elemento dividida pela massa toda, [p=0.1] {c}vezes cem."),
    dict(id="s05", block="percentual", text="Comece pela massa molar do nitrato de amônio. [p=0.2] {a}Conte os átomos com cuidado: [p=0.1] {b}tem um ene no começo [p=0.1] e {c}outro ene no meio. [p=0.2] {d}Dois nitrogênios, quatro hidrogênios e três oxigênios. [p=0.3] {e}Na tabela, ene vale catorze, agá vale um e ó vale dezesseis."),
    dict(id="s06", block="percentual", text="{a}Nitrogênio: dois vezes catorze dá vinte e oito. [p=0.2] {b}Hidrogênio: quatro vezes um dá quatro. [p=0.2] {c}Oxigênio: três vezes dezesseis dá quarenta e oito. [p=0.3] {d}Somando, oitenta gramas por mol."),
    dict(id="s07", block="percentual", text="{a}Desses oitenta gramas, vinte e oito são de nitrogênio. [p=0.3] {b}Vinte e oito dividido por oitenta dá zero vírgula trinta e cinco. [p=0.2] {c}Vezes cem dá trinta e cinco por cento de nitrogênio."),
    # erro
    dict(id="s08", block="erro", text="O erro mais comum aqui é {a}contar o nitrogênio uma vez só. [p=0.3] {b}Catorze de oitenta dá dezessete e meio por cento: [p=0.1] {c}a metade do certo. [p=0.3] {d}Antes de calcular, procure o mesmo símbolo em mais de um lugar da fórmula."),
    # fórmula mínima
    dict(id="s09", block="minima", text="Outra pergunta de prova: [p=0.1] {a}qual é a fórmula mínima? [p=0.2] {b}É a fórmula com a menor proporção inteira entre os átomos. [p=0.3] {c}Na glicose, cê seis agá doze ó seis, [p=0.2] {d}os índices seis, doze e seis se dividem por seis. [p=0.2] {e}Sobra cê agá dois ó: [p=0.1] um carbono para dois hidrogênios e um oxigênio."),
    dict(id="s10", block="minima", text="{a}A fórmula mínima mostra a proporção, não a molécula. [p=0.2] {b}A molécula de glicose tem seis vezes esse pedaço."),
    # das porcentagens à fórmula
    dict(id="s11", block="cem", text="E se a prova der só as porcentagens? [p=0.2] Uma substância tem {a}quarenta por cento de carbono, [p=0.1] {b}seis vírgula sete por cento de hidrogênio [p=0.1] {c}e cinquenta e três vírgula três por cento de oxigênio."),
    dict(id="s12", block="cem", text="{a}Passo um: imagine cem gramas da substância. [p=0.2] {b}Aí, cada porcentagem vira grama: [p=0.1] {c}quarenta gramas de carbono, [p=0.1] seis vírgula sete de hidrogênio [p=0.1] e cinquenta e três vírgula três de oxigênio."),
    dict(id="s13", block="cem", text="{a}Passo dois: divida cada massa pela massa molar do elemento. [p=0.2] Isso dá quantos mols de cada elemento há. [p=0.3] {b}Quarenta dividido por doze dá cerca de três vírgula três. [p=0.2] {c}Seis vírgula sete dividido por um dá seis vírgula sete. [p=0.2] {d}Cinquenta e três vírgula três dividido por dezesseis dá cerca de três vírgula três."),
    dict(id="s14", block="cem", text="{a}Passo três: divida tudo pelo menor, três vírgula três. [p=0.3] {b}Carbono, um. [p=0.1] {c}Hidrogênio, cerca de dois. [p=0.1] {d}Oxigênio, um. [p=0.3] {e}Cê agá dois ó, a fórmula mínima da glicose."),
    dict(id="s15", block="cem", text="{a}Se a prova der a massa molar, cento e oitenta, [p=0.2] {b}divida pela massa do pedaço, trinta: [p=0.1] {c}dá seis. [p=0.2] {d}Multiplique os índices por seis e volta a cê seis agá doze ó seis."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho é {a}a base de cem gramas. [p=0.2] {b}Com cem gramas, a porcentagem já é a massa em gramas, [p=0.1] sem conta nenhuma. [p=0.3] {c}Funciona porque a proporção entre os átomos não depende de quanto você pega. [p=0.3] {d}Não compensa quando a prova já dá as massas de uma amostra: [p=0.1] aí, divida essas massas direto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}O gás de cozinha tem butano, cê quatro agá dez. [p=0.2] {b}Qual é a fórmula mínima do butano? [p=0.3] E no metano, {c}cê agá quatro, [p=0.1] {d}quantos por cento da massa é carbono?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}No butano, quatro e dez se dividem por dois. [p=0.2] {b}A fórmula mínima é cê dois agá cinco. [p=0.3] {c}No metano: doze mais quatro dá dezesseis gramas por mol. [p=0.2] {d}Doze dividido por dezesseis dá zero vírgula setenta e cinco: [p=0.1] {e}setenta e cinco por cento de carbono."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}a porcentagem é a massa do elemento dividida pela massa molar, vezes cem; [p=0.2] {b}a fórmula mínima é a menor proporção inteira; [p=0.2] {c}e, com porcentagens, comece por cem gramas."),
    dict(id="s21", block="fim", text="Na próxima aula, começa a estequiometria: [p=0.2] você vai {a}ler uma equação em mols [p=0.1] e ver por que {b}a proporção das massas numa reação nunca muda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
