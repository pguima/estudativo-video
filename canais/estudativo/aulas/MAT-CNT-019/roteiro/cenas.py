# Estudativo · MAT-CNT-019 — Praticando: probabilidade (Matemática · Contagem e Probabilidade · prática).
# Habilidade: escolher entre contar, usar o complementar, somar ou multiplicar e resolver questões de sorteio e de genética.
# Pré-requisitos: MAT-CNT-011 a MAT-CNT-018. Próxima: nenhuma na trilha; ponte para a próxima trilha de Matemática do Zero: MAT-ANA-001 (distância entre dois pontos).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; genética narrada como versão dominante e recessiva, com A e a na tela.
# Questões inéditas, criadas para esta aula. Termos das aulas anteriores: favoráveis sobre possíveis, complementar ("pelo menos um" → nenhum),
# "ou" → soma menos a parte em comum, independentes → multiplica, sem reposição, árvore (ao longo multiplica, entre caminhos soma).
# Guia (tela): pelo menos um → complementar · ou → somar e tirar o comum · e, em sequência → multiplicar · sabendo que → novo total.
# 1) 4 homens + 3 mulheres, sorteio de 2: combinação 7 × 6 = 42, ÷ 2 = 21 · mulheres 3 × 2 = 6, ÷ 2 = 3 → 3/21 = 1/7.
#    Atalho (sem reposição): 3/7 × 2/6 = 6/42 = 1/7. Não compensa em "um homem e uma mulher": 2 caminhos (4/7 × 3/6 + 3/7 × 4/6 = 24/42 = 4/7).
# 2) Chute em 3 questões de 4 alternativas: errar cada 3/4 → (3/4)³ = 27/64 · 1 − 27/64 = 37/64 ≈ 57,8% (pouco mais da metade).
# 3) 1 a 50: múltiplos de 4 (12), de 6 (8), de ambos = de 12 (MMC; 12, 24, 36, 48 = 4) → 12 + 8 − 4 = 16 → 16/50 = 8/25 = 32%. Armadilha: múltiplos de 24 (só 2).
# 4) Genética: mãe Aa, pai aa (tem a característica). Pai sempre passa a (chance 1) · mãe a 1/2 → 1 × 1/2 = 1/2 = 50% · dois filhos: 1/2 × 1/2 = 1/4.

TITULO = "Praticando: probabilidade"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações de probabilidade, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, o mais difícil é {b}escolher a ferramenta. [p=0.3] {c}Pause o vídeo e resolva antes de ver a resposta."),
    # lembrete: o guia
    dict(id="s02", block="lembrete", text="Use as palavras da pergunta como pista. [p=0.2] {a}Pelo menos um? Calcule o nenhum e tire de um. [p=0.3] {b}A palavra ou? Some e tire a parte em comum. [p=0.3] {c}A palavra e, em sequência? Multiplique. [p=0.3] {d}Sabendo que? A pista vira o novo total. [p=0.3] Nenhuma dessas? Conte favoráveis e possíveis. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: contar
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um grupo tem {b}quatro homens e três mulheres. [p=0.2] {c}Duas pessoas são sorteadas para uma comissão. [p=0.3] {d}Qual a chance de serem ambas mulheres?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá, contando. [p=0.2] Na comissão, a ordem não importa: [p=0.2] é {a}combinação. [p=0.3] Possíveis: {b}sete vezes seis dá quarenta e dois, [p=0.2] e dividido por dois dá {c}vinte e uma comissões. [p=0.3] Favoráveis: {d}três vezes dois dá seis, [p=0.2] e dividido por dois dá {e}três comissões só de mulheres. [p=0.3] A chance é {f}três vinte e um avos, [p=0.2] que simplifica para {g}um sétimo."),
    dict(id="s06", block="atalho", text="Agora um atalho: {a}trate como sorteio sem reposição. [p=0.3] A primeira mulher: {b}três sétimos. [p=0.2] A segunda: {c}dois sextos. [p=0.2] {d}Três sétimos vezes dois sextos dá seis quarenta e dois avos: um sétimo. [p=0.3] Funciona porque sortear duas de uma vez {e}é o mesmo que sem reposição."),
    dict(id="s07", block="atalho", text="{a}Não compensa quando a pergunta mistura, [p=0.2] como {b}um homem e uma mulher. [p=0.3] Aí, são {c}dois caminhos na árvore: [p=0.2] homem antes ou mulher antes. [p=0.2] E quem esquece um deles {d}erra pela metade."),
    # situação 2: complementar
    dict(id="s08", block="questao2", text="{a}Situação dois. [p=0.2] Uma pessoa chuta {b}três questões, [p=0.2] cada uma com {c}quatro alternativas e só uma certa. [p=0.3] {d}Qual a chance de acertar pelo menos uma?"),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] Pelo menos uma: {a}calcule o nenhum. [p=0.2] Errar uma questão tem chance de {b}três quartos. [p=0.2] As questões são independentes, então multiplique: [p=0.2] {c}três quartos elevado a três dá vinte e sete sessenta e quatro avos."),
    dict(id="s11", block="resposta2", text="Tire de um: {a}sessenta e quatro menos vinte e sete dá trinta e sete. [p=0.2] A chance é {b}trinta e sete sessenta e quatro avos, [p=0.2] {c}pouco mais da metade. [p=0.3] Contar direto pediria {d}uma, [p=0.2] duas [p=0.2] ou três certas: [p=0.2] três contas no lugar de uma."),
    # situação 3: união
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Uma urna tem {b}cinquenta bolinhas, numeradas de um a cinquenta. [p=0.3] {c}Qual a chance de sortear um múltiplo de quatro ou de seis?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] A palavra ou: {a}some e tire a parte em comum. [p=0.3] {b}Múltiplos de quatro até cinquenta: doze. [p=0.2] {c}Múltiplos de seis: oito. [p=0.3] Múltiplos de quatro e de seis ao mesmo tempo são {d}os múltiplos do MMC, que é doze: [p=0.2] {e}doze, [p=0.2] vinte e quatro, [p=0.2] trinta e seis [p=0.2] e quarenta e oito."),
    dict(id="s15", block="resposta3", text="{a}Doze mais oito dá vinte. [p=0.2] {b}Vinte menos os quatro números em comum dá dezesseis. [p=0.3] A chance é {c}dezesseis cinquenta avos, [p=0.2] ou {d}trinta e dois por cento. [p=0.3] Cuidado com a armadilha: [p=0.2] a parte em comum {e}não são os múltiplos de quatro vezes seis, [p=0.2] e sim os do MMC."),
    # situação 4: genética
    dict(id="s16", block="questao4", text="{a}Última situação: genética. [p=0.2] A característica só aparece com {b}a versão recessiva do pai e da mãe. [p=0.3] {c}A mãe tem uma versão dominante e uma recessiva. [p=0.2] {d}O pai tem duas recessivas, e mostra a característica. [p=0.3] {e}Qual a chance de um filho do casal nascer com ela? [p=0.2] {f}E, se o casal tiver dois filhos, qual a chance de ambos nascerem com ela?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá, pela árvore. [p=0.2] O pai só tem a recessiva para passar: [p=0.2] {a}um galho só, com chance de um inteiro. [p=0.3] A mãe passa a recessiva com {b}um meio. [p=0.2] Ao longo do caminho, multiplique: [p=0.2] {c}um vezes um meio dá um meio. [p=0.2] {d}Cinquenta por cento."),
    dict(id="s19", block="resposta4", text="Para dois filhos, cada nascimento é {a}independente do outro. [p=0.2] {b}Um meio vezes um meio dá um quarto. [p=0.3] Repare: {c}o primeiro filho não muda a chance do segundo, [p=0.2] como a moeda que não tem memória."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}leia a palavra que manda na pergunta [p=0.2] e {b}escolha a ferramenta antes de fazer conta."),
    dict(id="s21", block="fim", text="Com isso, você fecha a trilha de contagem e probabilidade. [p=0.3] A próxima trilha é {a}geometria analítica. [p=0.2] Na primeira aula, você calcula {b}a distância entre dois pontos do plano [p=0.2] usando {c}um triângulo retângulo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
