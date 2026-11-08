# Estudativo · MAT-TOP-018 — Praticando: bases, medidas, troncos e homotetia (Matemática · Tópicos Avançados · prática).
# Habilidade: converter bases, respeitar os algarismos significativos, calcular troncos e usar a razão de homotetia.
# Pré-requisitos: MAT-TOP-014 (bases 2 e 60), MAT-TOP-015 (algarismos significativos), MAT-TOP-016 (troncos: inteiro − ponta, k³),
#   MAT-TOP-017 (homotetia: comprimentos × k, área × k²). Próxima: nenhuma (última aula da trilha).
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; algarismos da base dois
#   e números com zeros significativos lidos algarismo a algarismo.
# Contas: 1) 11010₂ = 16 + 8 + 2 = 26; 200 ÷ 60 = 3 r20 → 3 h 20 min.
#   2) 0,00250 → 3 significativos (2, 5, 0); 1,2 × 3,456 = 4,1472 → 2 significativos → 4,1.
#   3) k = 2/5, k³ = 8/125; 250 · 8/125 = 16; 250 − 16 = 234. Atalho: 1 − 8/125 = 117/125; 250 · 117/125 = 234.
#   4) k = 4: 5 cm → 20 cm; 12 cm² · 16 = 192 cm².

TITULO = "Praticando: bases, algarismos significativos, troncos e homotetia"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula, [p=0.2] com o que você viu nos dois últimos módulos: [p=0.2] {b}bases de contagem, algarismos significativos, {c}troncos e homotetia. [p=0.3] Em cada uma, {d}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}quatro ferramentas: [p=0.2] {b}na base dois, as casas dobram: um, dois, quatro, oito, dezesseis; [p=0.2] {c}ao multiplicar medidas, manda a que tem menos significativos; [p=0.2] {d}o tronco é o sólido inteiro menos a ponta, que encolhe com cá ao cubo; [p=0.2] e, {e}na homotetia, os comprimentos ficam vezes cá, e a área, vezes cá ao quadrado. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1
    dict(id="s03", block="questao1", text="Situação um. [p=0.2] Um computador guarda {a}um, um, zero, um, zero, na base dois. [p=0.2] {b}Que número é esse na base dez? [p=0.3] E {c}quanto é duzentos minutos, em horas e minutos?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}As casas, da esquerda para a direita: dezesseis, oito, quatro, dois, um. [p=0.2] As que têm um: {b}dezesseis, oito e dois. [p=0.2] {c}Vinte e seis."),
    dict(id="s06", block="resposta1", text="{a}Duzentos dividido por sessenta dá três, resto vinte. [p=0.2] O resultado vira hora, e o resto fica em minutos: [p=0.2] {b}três horas e vinte minutos."),
    # situação 2
    dict(id="s07", block="questao2", text="Situação dois. [p=0.2] {a}Quantos algarismos significativos tem zero vírgula zero, zero, dois, cinco, zero? [p=0.3] E {b}quanto dá um vírgula dois vezes três vírgula quatro, cinco, seis, [p=0.2] com os significativos certos?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}Os zeros da esquerda só marcam a vírgula. [p=0.2] Contam {b}o dois, o cinco e o zero do fim: [p=0.2] {c}três significativos."),
    dict(id="s10", block="resposta2", text="{a}A conta dá quatro vírgula um, quatro, sete, dois. [p=0.2] {b}Um vírgula dois tem dois significativos, [p=0.2] e {c}três vírgula quatro, cinco, seis tem quatro. [p=0.2] Manda o menor: dois. [p=0.3] {d}O algarismo seguinte é quatro, menos que cinco: [p=0.2] {e}fica quatro vírgula um."),
    # situação 3
    dict(id="s11", block="questao3", text="Situação três. [p=0.2] Uma pirâmide tem {a}volume duzentos e cinquenta. [p=0.2] Um corte paralelo à base é feito {b}a dois quintos da altura, contando do vértice. [p=0.3] {c}Qual é o volume do tronco?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] A ponta é uma pirâmide semelhante, {a}com cá igual a dois quintos. [p=0.2] {b}Dois quintos ao cubo: oito cento e vinte e cinco avos. [p=0.3] {c}Duzentos e cinquenta vezes oito cento e vinte e cinco avos: dezesseis. [p=0.2] {d}Tronco: duzentos e cinquenta menos dezesseis, duzentos e trinta e quatro. [p=0.3] A ponta ficou bem pequena, {e}nem um décimo do total: [p=0.2] faz sentido, porque o corte foi perto do vértice."),
    # atalho
    dict(id="s14", block="atalho", text="Agora um atalho: {a}a fração do tronco é um menos cá ao cubo. [p=0.3] {b}Um menos oito cento e vinte e cinco avos dá cento e dezessete cento e vinte e cinco avos. [p=0.2] {c}Duzentos e cinquenta vezes isso: duzentos e trinta e quatro, numa conta só."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o sólido inteiro é o todo, um inteiro, [p=0.2] e a ponta é a fração cá ao cubo dele. [p=0.3] {b}Não compensa quando a questão pede a ponta e o tronco: [p=0.2] aí, a ponta sai primeiro, e o tronco é a subtração."),
    # situação 4
    dict(id="s16", block="questao4", text="Última situação. [p=0.2] Uma lanterna projeta {a}a sombra de um recorte de papelão na parede, [p=0.2] numa homotetia de {b}razão quatro, com o centro na lanterna. [p=0.3] O recorte tem {c}cinco centímetros de largura {d}e área de doze centímetros quadrados. [p=0.2] {e}Qual é a largura e qual é a área da sombra?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] {a}A largura é um comprimento: vezes quatro. [p=0.2] {b}Cinco vezes quatro, vinte centímetros. [p=0.3] {c}A área é vezes cá ao quadrado: quatro ao quadrado, dezesseis. [p=0.2] {d}Doze vezes dezesseis: cento e noventa e dois centímetros quadrados. [p=0.3] Quem multiplica a área só por quatro {e}acha quarenta e oito, [p=0.2] e esquece que a sombra cresce {f}na largura e na altura ao mesmo tempo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}na base dois, some as casas com um; [p=0.2] {b}nas medidas, manda a mais pobre; [p=0.2] {c}no tronco, tire a ponta; [p=0.2] e, {d}na homotetia, a área usa cá ao quadrado."),
    dict(id="s20", block="fim", text="Com esta aula, {a}você fecha a trilha de Tópicos Avançados. [p=0.2] Se algum passo travou, procure a aula no canal e refaça. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
