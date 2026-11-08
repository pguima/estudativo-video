# Estudativo · MAT-CNT-015 — Probabilidade condicional (Matemática · Contagem e Probabilidade · União, interseção e condicional).
# Habilidade: reduzir o espaço amostral e, numa tabela, achar a chance de um aluno ser mulher sabendo que usa óculos.
# Pré-requisitos: MAT-CNT-014 (probabilidade da união). Próxima: MAT-CNT-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, bê, pê).
# Questão inédita, criada para esta aula. "Pista" = a informação dada; ela vira o novo total.
# Dado: P(6) = 1/6; sabendo que saiu par → {2, 4, 6} → 1/3.
# Tabela de dupla entrada (E.tabela é de fatoração: compor grade simples 3 × 3 com totais):
#            óculos  sem  total
#   homens      6     12    18
#   mulheres   10     12    22
#   total      16     24    40
# P(mulher | óculos) = 10/16 = 5/8 = 62,5% (destacar a coluna "óculos"). Erro: 10/40 = 1/4 (é "mulher e óculos").
# Ordem inversa: P(óculos | mulher) = 10/22 = 5/11 (linha das mulheres). Na tela: P(A | B) = n(A ∩ B) / n(B).
# Questão (pista escondida): manhã ônibus 18, carro 12 (30) · tarde ônibus 8, carro 12 (20) · total 50.
# Ônibus 18 + 8 = 26 → P(manhã | ônibus) = 18/26 = 9/13 ≈ 69%.

TITULO = "Probabilidade condicional"

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
    dict(id="s01", block="gancho", text="{a}Uma pessoa é sorteada numa turma. [p=0.2] Antes de dizer o nome, alguém dá uma pista: [p=0.2] {b}a pessoa sorteada usa óculos. [p=0.3] Essa pista {c}muda a chance de ter sido uma mulher? [p=0.3] Muda. [p=0.2] E quem ignora a pista {d}erra a conta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa a pista para encolher o espaço amostral, [p=0.2] faz isso numa {b}tabela [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}probabilidade é favoráveis sobre possíveis, [p=0.2] e {c}o espaço amostral é a lista de todos os resultados possíveis. [p=0.3] Se faltar alguma, procure no canal."),
    # dado
    dict(id="s04", block="dado", text="Comece com um dado. [p=0.2] A chance de sair {a}seis é {b}um sexto. [p=0.3] Agora, alguém olha o dado e avisa: {c}saiu número par. [p=0.2] E agora, qual a chance de ser seis?"),
    dict(id="s05", block="dado", text="Com a pista, o um, o três e o cinco {a}estão fora. [p=0.2] Sobram só {b}o dois, [p=0.2] o quatro [p=0.2] e o seis. [p=0.3] O espaço amostral {c}encolheu para três resultados. [p=0.2] A chance de ser seis subiu para {d}um terço."),
    # regra
    dict(id="s06", block="regra", text="Isso é {a}probabilidade condicional: [p=0.2] a chance de um evento, {b}sabendo que outro já aconteceu. [p=0.3] A regra é uma só: [p=0.2] {c}a pista vira o novo total. [p=0.2] O que está fora da pista {d}sai da conta."),
    dict(id="s07", block="regra", text="Na prova, aparece {a}pê de á, barra, bê. [p=0.2] A barra em pé se lê {b}dado que, ou sabendo que. [p=0.3] Embaixo vai {c}a quantidade de casos de bê, a pista. [p=0.2] Em cima, {d}os casos de á que também estão em bê: [p=0.2] a interseção."),
    # tabela
    dict(id="s08", block="tabela", text="Agora a turma, com {a}quarenta alunos. [p=0.2] São {b}dezoito homens: seis usam óculos e doze não usam. [p=0.3] E {c}vinte e duas mulheres: dez usam óculos e doze não usam."),
    dict(id="s09", block="tabela", text="Na tabela, {a}cada linha é homens ou mulheres. [p=0.2] {b}Cada coluna é com ou sem óculos. [p=0.3] Somando a coluna dos óculos: [p=0.2] {c}seis mais dez dá dezesseis alunos de óculos."),
    dict(id="s10", block="tabela", text="A pergunta: {a}chance de ser mulher, sabendo que usa óculos. [p=0.3] A pista é {b}usa óculos. [p=0.2] Então o novo total é {c}a coluna dos óculos: dezesseis. [p=0.2] Desses, {d}dez são mulheres."),
    dict(id="s11", block="tabela", text="A chance é {a}dez dezesseis avos. [p=0.2] Dividindo por dois: {b}cinco oitavos, [p=0.2] que dá {c}sessenta e dois e meio por cento."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}dividir pela turma inteira: [p=0.2] {b}dez quarenta avos, que dá um quarto. [p=0.3] Mas essa é outra pergunta: [p=0.2] a chance de sortear alguém que {c}é mulher e usa óculos, sem pista nenhuma. [p=0.3] Com a pista, {d}quem não usa óculos já saiu da conta."),
    dict(id="s13", block="erro", text="E a ordem importa. [p=0.2] {a}Chance de usar óculos, sabendo que é mulher? [p=0.3] Agora a pista é ser mulher: [p=0.2] o total vira {b}a linha das mulheres, vinte e duas. [p=0.2] Fica {c}dez vinte e dois avos, ou cinco onze avos. [p=0.2] {d}Outra pista, outra resposta."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}ache a pista na frase e cubra o resto da tabela. [p=0.3] Viu {b}sabendo que, [p=0.2] {c}dado que [p=0.2] ou {d}entre os que? [p=0.2] O que vem depois é o novo total. [p=0.2] Use só aquela linha ou coluna."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a pista elimina todo o resto. [p=0.3] Mas não confie só na palavra: [p=0.2] {b}às vezes a pista vem escondida, [p=0.2] como em {c}um aluno de óculos foi sorteado. [p=0.2] Aí, pergunte: {d}quem ainda pode ter sido sorteado?"),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma empresa tem {a}cinquenta funcionários. [p=0.2] {b}No turno da manhã, dezoito vão de ônibus e doze vão de carro. [p=0.2] {c}No da tarde, oito vão de ônibus e doze vão de carro. [p=0.3] Um funcionário que vai de ônibus é sorteado. [p=0.2] {d}Qual a chance de ele ser do turno da manhã?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A pista está escondida: {a}vai de ônibus. [p=0.2] O novo total é a coluna do ônibus: {b}dezoito mais oito dá vinte e seis. [p=0.3] Desses, {c}dezoito são da manhã. [p=0.2] A chance é {d}dezoito vinte e seis avos. [p=0.2] Dividindo por dois: {e}nove treze avos, [p=0.2] quase setenta por cento."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a pista vira o novo total. [p=0.2] {b}Em cima, só quem cumpre as duas condições ao mesmo tempo."),
    dict(id="s20", block="fim", text="E quando a pista {a}não muda nada? [p=0.2] Saber que a moeda deu cara muda a chance de o dado dar seis? [p=0.3] Na próxima aula: {b}eventos independentes, e por que aí você multiplica as chances. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
