# Estudativo · MAT-CNT-014 — Probabilidade da união (Matemática · Contagem e Probabilidade · União, interseção e condicional).
# Habilidade: usar P(A ∪ B) = P(A) + P(B) − P(A ∩ B) e achar a chance de tirar rei ou copas num baralho (16/52).
# Pré-requisitos: MAT-CNT-011 (favoráveis sobre possíveis), MAT-CON-003 (Venn, n(A ∪ B)). Próxima: MAT-CNT-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, bê, pê, ene).
# Questão inédita, criada para esta aula. Soma de frações não está em "Já ensinado": as contas são feitas com quantidades
# (mesmo denominador, o total) e só divididas no fim. Mesmos termos de MAT-CON-003: de dentro para fora, ambos, interseção.
# Baralho: 52 cartas, 4 naipes × 13 (ás ao rei), 4 reis. E.venn: A = reis, B = copas, AB = rei de copas (1), A só 3, B só 12.
# 3 + 1 + 12 = 16 · 4 + 13 − 1 = 16 → 16/52 = 4/13 (≈ 30,8%, pouco menos de um terço).
# Fórmula na tela: P(A ∪ B) = P(A) + P(B) − P(A ∩ B) → 4/52 + 13/52 − 1/52 = 16/52.
# Sem interseção: rei ou dama 4 + 4 = 8 → 8/52 = 2/13. Erro: 4 + 13 = 17 → 17/52.
# Atalho: quantidades e divide no fim; não compensa com chances prontas: 60% + 50% − 30% = 80%.
# Questão: 1 a 30, múltiplo de 3 (10) ou de 5 (6), ambos {15, 30} (2) → 10 + 6 − 2 = 14 → 14/30 = 7/15.

TITULO = "Probabilidade da união"

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
    dict(id="s01", block="gancho", text="Tire {a}uma carta de um baralho. [p=0.3] Qual a chance de ser {b}um rei ou uma carta de copas? [p=0.3] Muita gente soma os reis com as copas [p=0.2] e responde {c}dezessete cinquenta e dois avos. [p=0.3] {d}Errou por uma carta só."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a chance de um evento {b}ou outro, [p=0.2] sem contar nada duas vezes, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}probabilidade é favoráveis sobre possíveis, [p=0.2] e {c}a fórmula da união do diagrama de Venn: [p=0.2] ene de á, mais ene de bê, menos ene da interseção. [p=0.3] Se faltar alguma, procure no canal."),
    # baralho
    dict(id="s04", block="baralho", text="Primeiro, o baralho. [p=0.2] São {a}cinquenta e duas cartas, em {b}quatro naipes: [p=0.2] copas, espadas, ouros e paus. [p=0.3] Cada naipe tem {c}treze cartas, do ás ao rei. [p=0.2] Então existem {d}quatro reis, um de cada naipe."),
    # Venn
    dict(id="s05", block="venn", text="Agora o diagrama de Venn. [p=0.2] O conjunto á são {a}os reis: quatro cartas. [p=0.2] O conjunto bê são {b}as cartas de copas: treze. [p=0.3] Uma carta está {c}em ambos ao mesmo tempo: [p=0.2] {d}o rei de copas. [p=0.2] Ela vai no meio."),
    dict(id="s06", block="venn", text="De dentro para fora. [p=0.2] {a}Só rei: quatro menos um dá três. [p=0.2] {b}Só copas: treze menos um dá doze. [p=0.3] Somando os pedaços: {c}três mais um mais doze dá dezesseis cartas."),
    dict(id="s07", block="venn", text="A chance é {a}dezesseis cinquenta e dois avos. [p=0.2] Divida em cima e embaixo por quatro: [p=0.2] {b}quatro treze avos. [p=0.3] Em por cento, dá {c}cerca de trinta e um por cento: [p=0.2] pouco menos de um terço."),
    # fórmula
    dict(id="s08", block="formula", text="A fórmula da união também vale para chances. [p=0.2] {a}Pê de á é a chance do evento á. [p=0.3] {b}A chance de á ou bê [p=0.2] é {c}a chance de á, mais a de bê, [p=0.2] {d}menos a chance de ambos juntos."),
    dict(id="s09", block="formula", text="No baralho: {a}quatro cinquenta e dois avos, [p=0.2] mais {b}treze cinquenta e dois avos, [p=0.2] menos {c}um cinquenta e dois avos. [p=0.3] Todas têm embaixo o mesmo número, o total de cartas. [p=0.2] Então a conta é só em cima: [p=0.2] {d}quatro mais treze menos um dá dezesseis. [p=0.2] De novo, {e}dezesseis cinquenta e dois avos."),
    dict(id="s10", block="formula", text="E quando {a}não existe parte em comum? [p=0.2] Rei {b}ou dama. [p=0.3] Nenhuma carta é rei e dama ao mesmo tempo: [p=0.2] a interseção é {c}vazia. [p=0.2] Não há nada contado duas vezes, [p=0.2] então não há nada para tirar. [p=0.2] Aí, é só somar: {d}quatro mais quatro dá oito. [p=0.2] A chance é {e}oito cinquenta e dois avos, ou dois treze avos."),
    # erro
    dict(id="s11", block="erro", text="Volte ao erro do começo. [p=0.2] {a}Quatro mais treze dá dezessete. [p=0.3] Mas o rei de copas foi contado {b}duas vezes: [p=0.2] uma entre os reis, outra entre as copas. [p=0.3] {c}Tire uma vez, e fica dezesseis. [p=0.2] A palavra ou pede soma, [p=0.2] mas antes pergunte: {d}dá para acontecer junto?"),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}faça a conta com quantidades e só divida no fim. [p=0.3] Contar cartas é mais fácil que lidar com frações, [p=0.2] e {b}o resultado é o mesmo, [p=0.2] porque todas as chances têm {c}o mesmo total embaixo."),
    dict(id="s13", block="atalho", text="Não compensa quando a questão {a}já dá as chances, em por cento. [p=0.2] Num mês, {b}sessenta por cento dos clientes de uma loja pagaram com cartão, [p=0.2] {c}cinquenta por cento com pix, [p=0.2] e {d}trinta por cento usaram ambos. [p=0.3] Qual a chance de um cliente sorteado ter usado cartão ou pix? [p=0.2] Use a fórmula direto: [p=0.2] {e}sessenta mais cinquenta menos trinta dá oitenta por cento."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma urna tem {a}trinta bolinhas, numeradas de um a trinta. [p=0.2] Uma é sorteada. [p=0.3] {b}Qual a chance de sair um múltiplo de três ou de cinco?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Múltiplos de três até trinta: dez números. [p=0.2] {b}Múltiplos de cinco: seis. [p=0.3] Múltiplos de três e de cinco ao mesmo tempo: [p=0.2] {c}quinze e trinta. [p=0.2] Eles entraram {d}em ambas as listas."),
    dict(id="s17", block="resposta", text="{a}Dez mais seis dá dezesseis. [p=0.2] {b}Tirando o quinze e o trinta, que estão em ambas as listas, dá catorze. [p=0.3] A chance é {c}catorze trinta avos. [p=0.2] Simplificando por dois: {d}sete quinze avos, [p=0.2] um pouco menos da metade."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}na palavra ou, some as chances [p=0.2] e {b}tire uma vez a parte em comum."),
    dict(id="s19", block="fim", text="Na próxima aula, a questão {a}dá uma pista antes de perguntar: [p=0.2] qual a chance de a pessoa sorteada ser mulher, [p=0.2] {b}sabendo que ela usa óculos? [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
