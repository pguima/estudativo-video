# Estudativo · MAT-EST-012 — Média, mediana e moda numa tabela (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: achar as três medidas a partir de uma tabela com notas e número de alunos, sem escrever a lista inteira.
# Pré-requisitos: MAT-EST-009 (média ponderada), MAT-EST-011 (moda e mediana; posição do meio). Usa MAT-EST-002 (frequência acumulada). Próxima: MAT-EST-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Tabelas só na tela.
# Dados (tela): nota 4: 2 alunos · 6: 4 · 7: 5 · 8: 6 · 9: 3 → total 20.
#   Média: 4·2 + 6·4 + 7·5 + 8·6 + 9·3 = 8 + 24 + 35 + 48 + 27 = 142; 142/20 = 7,1 (nota 4, não 5, para não repetir o 7,2 da MAT-EST-009).
#   Mediana: (20 + 1)/2 = 10,5 → 10º e 11º; acumulada 2, 6, 11, 17, 20 → ambos na nota 7 → 7.
#   Moda: nota 8 (6 alunos). Erro: responder 6 (o número de alunos).
#   Atalho (base 7): −3·2 − 1·4 + 0 + 1·6 + 2·3 = −6 − 4 + 6 + 6 = 2; 2/20 = 0,1; 7 + 0,1 = 7,1.
#   Questão: filhos 0: 2 famílias · 1: 7 · 2: 5 · 3: 4 · 4: 2 → total 20; soma 0 + 7 + 10 + 12 + 8 = 37; 37/20 = 1,85.
#     Acumulada 2, 9, 14, 18, 20 → 10º e 11º na linha 2 → mediana 2. Moda 1 (7 famílias).
#     Base 2: −2·2 − 1·7 + 0 + 1·4 + 2·2 = −3; −3/20 = −0,15; 2 − 0,15 = 1,85.
# Visual:
#   s01: E.tabela nota × alunos; ao lado, a lista de vinte notas se desenrolando e sendo riscada.
#   s04-s06: E.tabela com coluna "nota × alunos" entrando linha a linha; soma 142; 142 ÷ 20.
#   s07-s08: coluna de frequência acumulada; seta nas posições 10ª e 11ª caindo na linha da nota 7.
#   s09-s10: linha da nota 8 acesa (moda); "6" em vermelho e "8" em verde.
#   s11-s12: coluna "nota − 7" com os desvios; soma 2; 2 ÷ 20 = 0,1.

TITULO = "Média, mediana e moda numa tabela"

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
    dict(id="s01", block="gancho", text="{a}Vinte alunos, cinco notas diferentes, tudo numa tabela. [p=0.3] Muita gente {b}escreve a lista inteira, nota por nota, [p=0.2] para achar a mediana. [p=0.3] {c}Não precisa. [p=0.2] A tabela já entrega as três medidas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você tira média, mediana e moda direto da tabela [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a média ponderada, em que cada valor tem um peso, [p=0.2] e {c}a moda e a mediana, com a posição do meio. [p=0.3] Se faltar alguma, procure no canal."),
    # média
    dict(id="s04", block="media", text="Comece pela média. [p=0.2] Na tabela, {a}cinco alunos tiraram sete. [p=0.2] É como se o sete aparecesse cinco vezes na lista. [p=0.3] Então {b}o número de alunos é o peso de cada nota. [p=0.2] É uma média ponderada."),
    dict(id="s05", block="media", text="Multiplique {a}cada nota pelo número de alunos. [p=0.2] {b}Quatro vezes dois dá oito. [p=0.2] {c}Seis vezes quatro dá vinte e quatro. [p=0.2] {d}Sete vezes cinco dá trinta e cinco. [p=0.2] {e}Oito vezes seis dá quarenta e oito. [p=0.2] {f}Nove vezes três dá vinte e sete."),
    dict(id="s06", block="media", text="{a}Somando tudo, dá cento e quarenta e dois. [p=0.3] Agora divida pelo {b}total de alunos, vinte, [p=0.2] e não pelo número de linhas. [p=0.2] {c}Cento e quarenta e dois dividido por vinte dá sete vírgula um. [p=0.3] Confira se faz sentido: [p=0.2] {d}a média ficou entre a menor nota e a maior. [p=0.2] Se sair fora disso, a conta está errada."),
    # mediana
    dict(id="s07", block="mediana", text="Agora a mediana. [p=0.2] São vinte alunos: {a}vinte mais um dá vinte e um, e vinte e um dividido por dois dá dez e meio. [p=0.3] A mediana é a média do {b}décimo e do décimo primeiro aluno, com as notas em ordem. [p=0.3] E a tabela {c}já vem em ordem, da menor nota para a maior. [p=0.2] Ela faz o papel da lista ordenada."),
    dict(id="s08", block="mediana", text="Quem diz onde eles estão é {a}a frequência acumulada. [p=0.2] {b}Até a nota seis, são seis alunos. [p=0.2] {c}Até a nota sete, são onze. [p=0.3] Então {d}do sétimo ao décimo primeiro aluno, todos tiraram sete. [p=0.2] {e}A mediana é sete. [p=0.3] Se os alunos do meio caíssem em linhas diferentes, {f}você faria a média das duas notas."),
    # moda
    dict(id="s09", block="moda", text="E a moda? [p=0.2] É {a}a nota que mais alunos tiraram. [p=0.2] A maior frequência é {b}seis alunos, na linha da nota oito. [p=0.3] {c}A moda é oito. [p=0.3] Basta procurar {d}o maior número da coluna de alunos e olhar a nota ao lado."),
    # erro
    dict(id="s10", block="erro", text="E aqui mora o erro mais comum: [p=0.2] responder {a}seis, que é o número de alunos. [p=0.3] A moda é sempre {b}um valor dos dados, a nota, [p=0.2] e não {c}quantas vezes ela aparece."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho da média: [p=0.2] {a}escolha uma nota do meio como base. [p=0.2] Vamos usar o sete. [p=0.3] Anote quanto cada nota {b}passa ou falta para o sete, vezes o número de alunos. [p=0.2] {c}As notas abaixo de sete somam menos dez. [p=0.2] As notas acima somam mais doze. [p=0.3] {d}No total, dá dois."),
    dict(id="s12", block="atalho", text="{a}Dois dividido por vinte dá zero vírgula um. [p=0.2] {b}Sete mais zero vírgula um dá sete vírgula um. [p=0.3] Funciona porque {c}tirar sete de todas as notas tira sete da média. [p=0.2] No fim, é só devolver. [p=0.3] {d}Com valores pequenos, como número de filhos, não compensa: faça a conta direta."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}A tabela mostra quantos filhos têm vinte famílias de uma rua. [p=0.3] {b}Calcule a média, a mediana e a moda do número de filhos."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Média: {a}multiplique cada número de filhos pelo número de famílias. [p=0.2] {b}Somando os produtos, dá trinta e sete. [p=0.2] {c}Trinta e sete dividido por vinte dá um vírgula oitenta e cinco filhos por família."),
    dict(id="s16", block="resposta", text="Mediana: o décimo e o décimo primeiro. [p=0.2] {a}Até um filho, são nove famílias. [p=0.2] {b}Até dois filhos, nove mais cinco dá catorze. [p=0.2] {c}As famílias do meio têm dois filhos: a mediana é dois. [p=0.3] Moda: a maior frequência é sete, [p=0.2] na linha de um filho. [p=0.2] {d}A moda é um filho, não sete."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.2] {a}média, cada valor vezes a frequência, dividido pelo total; [p=0.2] {b}mediana, pela acumulada; [p=0.2] {c}moda, o valor da linha mais frequente."),
    dict(id="s18", block="fim", text="Na próxima aula, a pergunta que decide questões: {a}qual medida usar? [p=0.2] Você vai ver por que {b}um salário muito alto puxa a média e quase não mexe na mediana. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
