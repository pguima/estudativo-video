# Estudativo · MAT-CNT-016 — Eventos independentes: multiplicar as chances (Matemática · Contagem e Probabilidade · União, interseção e condicional).
# Habilidade: dizer se dois eventos são independentes e calcular a chance de cara na moeda e 6 no dado (1/12).
# Pré-requisitos: MAT-CNT-015 (probabilidade condicional: a pista vira o novo total), MAT-FRA-009 (multiplicar frações). Próxima: MAT-CNT-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Princípio multiplicativo não está em "Já ensinado": os 12 resultados saem de uma tabela 2 × 6.
# Moeda e dado: tabela 2 linhas (cara, coroa) × 6 colunas = 12 casas; 1 favorável → 1/12. Com a pista "cara": linha de 6 → 1/6 = P(6).
# Regra: independentes → P(A e B) = P(A) × P(B): 1/2 × 1/6 = 1/12.
# Dependentes (turma de MAT-CNT-015): P(mulher) = 22/40 = 55% · P(mulher | óculos) = 10/16 = 62,5%.
# Erro: "a coroa está devendo" depois de 5 caras; a sexta continua 1/2.
# Atalho: chance repetida vira potência: (1/2)³ = 1/8 · (1/2)⁶ = 1/64. Não compensa quando a chance muda (sem devolver: MAT-CNT-017).
# Questão: semáforos independentes 2/5 × 1/3 = 2/15 ≈ 13,3%.

TITULO = "Eventos independentes: multiplicar as chances"

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
    dict(id="s01", block="gancho", text="Uma moeda deu {a}cara cinco vezes seguidas. [p=0.3] Na sexta jogada, {b}coroa ficou mais provável? [p=0.3] Muita gente aposta que sim. [p=0.2] Mas a chance continua {c}um meio. [p=0.2] A moeda {d}não tem memória."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece eventos independentes, [p=0.2] calcula a chance de {b}ambos acontecerem [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}a probabilidade condicional, em que a pista vira o novo total, [p=0.2] e {c}multiplicar frações: em cima vezes em cima, embaixo vezes embaixo. [p=0.3] Se faltar alguma, procure no canal."),
    # moeda e dado
    dict(id="s04", block="tabela", text="Você lança {a}uma moeda e um dado. [p=0.2] Qual a chance de sair {b}cara na moeda e seis no dado? [p=0.3] Monte uma tabela: [p=0.2] {c}uma linha para cara, outra para coroa, [p=0.2] e {d}uma coluna para cada face do dado. [p=0.2] {e}Duas vezes seis dá doze casas."),
    dict(id="s05", block="tabela", text="Só {a}uma casa tem cara e seis. [p=0.2] A chance é {b}um doze avos, [p=0.2] pouco mais de oito por cento."),
    dict(id="s06", block="tabela", text="Agora use a pista. [p=0.2] Sabendo que deu cara, a chance do seis muda? [p=0.3] O novo total é {a}a linha da cara: seis casas. [p=0.2] Só uma tem seis: {b}um sexto. [p=0.3] Sem pista nenhuma, o seis também tinha {c}um sexto. [p=0.2] {d}A pista não mudou nada."),
    # regra
    dict(id="s07", block="regra", text="Quando saber de um evento {a}não muda a chance do outro, [p=0.2] eles são {b}independentes. [p=0.3] E aí vale a regra: [p=0.2] {c}a chance de ambos é o produto das chances. [p=0.2] {d}Um meio vezes um sexto dá um doze avos. [p=0.2] O mesmo resultado da tabela, sem desenhar nada."),
    dict(id="s08", block="regra", text="Por que vezes? [p=0.2] {a}Metade dos resultados tem cara. [p=0.2] E, dessa metade, {b}um sexto tem seis. [p=0.3] É {c}um sexto de um meio, [p=0.2] e, como nas frações, a palavra de vira vezes."),
    # dependentes
    dict(id="s09", block="dependentes", text="Nem todo par de eventos é assim. [p=0.2] Lembre da turma da aula anterior: [p=0.2] {a}vinte e duas mulheres em quarenta alunos. [p=0.3] Sem pista, a chance de sortear uma mulher dá {b}cinquenta e cinco por cento. [p=0.3] Sabendo que a pessoa usa óculos, {c}sobe para sessenta e dois e meio por cento."),
    dict(id="s10", block="dependentes", text="A pista mudou a chance: [p=0.2] {a}esses eventos são dependentes, e não basta multiplicar. [p=0.3] O teste é este: [p=0.2] {b}a chance com a pista é igual à chance sem a pista? [p=0.2] {c}Igual: independentes, multiplique. [p=0.2] {d}Diferente: dependentes. [p=0.3] Moedas, dados e coisas sem ligação nenhuma entre si já são independentes. [p=0.2] Na dúvida, como numa tabela, faça a conta antes de decidir."),
    # erro
    dict(id="s11", block="erro", text="Volte à moeda do começo. [p=0.2] O erro é achar que, {a}depois de cinco caras, a coroa está devendo. [p=0.3] Mas cada jogada é {b}independente da anterior. [p=0.2] A moeda não sabe o que saiu antes. [p=0.2] Na sexta jogada, {c}cara e coroa continuam com um meio cada."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}a mesma chance repetida vira potência. [p=0.3] {b}Três caras seguidas? [p=0.2] {c}Um meio vezes um meio vezes um meio [p=0.2] é {d}um meio elevado a três, que dá um oitavo."),
    dict(id="s13", block="atalho", text="Funciona porque as jogadas são independentes, [p=0.2] e {a}potência é multiplicação repetida. [p=0.3] {b}Seis caras seguidas, vistas antes de começar: [p=0.2] um meio elevado a seis dá {c}um sessenta e quatro avos. [p=0.2] É raro. [p=0.2] Mas, com cinco caras já na mesa, {d}só falta uma jogada: um meio."),
    dict(id="s14", block="atalho", text="{a}Não compensa quando a chance muda de uma vez para outra, [p=0.2] como ao {b}tirar bolas de uma urna sem devolver. [p=0.2] Aí, cada fração tem que ser calculada de novo."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] No caminho do trabalho há {a}dois semáforos, em ruas distantes, [p=0.2] que funcionam sem ligação um com o outro. [p=0.3] Você pega o primeiro verde {b}em dois quintos das vezes [p=0.2] e o segundo, {c}em um terço. [p=0.3] {d}Qual a chance de pegar ambos verdes?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Os semáforos funcionam sem ligação: [p=0.2] saber de um não muda o outro. [p=0.2] São {a}independentes, então multiplique. [p=0.3] {b}Em cima, dois vezes um dá dois. [p=0.2] {c}Embaixo, cinco vezes três dá quinze. [p=0.3] A chance é {d}dois quinze avos, [p=0.2] um pouco mais de treze por cento."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}se a pista não muda a chance, os eventos são independentes. [p=0.2] {b}Aí, a chance de ambos é o produto."),
    dict(id="s19", block="fim", text="Na próxima aula, você tira {a}duas bolas de uma urna: [p=0.2] {b}devolvendo a primeira, ou não. [p=0.3] E descobre por que isso muda a conta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
