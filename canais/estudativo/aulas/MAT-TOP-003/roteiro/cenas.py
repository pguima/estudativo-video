# Estudativo · MAT-TOP-003 — Distribuição binomial (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: achar a chance de exatamente 2 caras em 5 lançamentos de uma moeda (10/32 = 5/16).
# Pré-requisitos: MAT-CNT-017 (sorteios sucessivos: multiplicar as chances), MAT-TOP-001 (binomiais e triângulo de Pascal). Próxima: MAT-TOP-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem "1 − p": subtrair frações (MAT-FRA-007) não está na ficha; a chance de fracasso
# sai contando os casos (cinco faces em seis; três alternativas em quatro).

TITULO = "Distribuição binomial"

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
    dict(id="s01", block="gancho", text="Você joga {a}uma moeda cinco vezes. [p=0.2] Qual a chance de sair {b}exatamente duas caras? [p=0.3] Muita gente responde {c}dois quintos. [p=0.2] Mas a chance é {d}cinco dezesseis avos, [p=0.2] pouco mais de trinta e um por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a chance de algo acontecer um número exato de vezes, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}chances de jogadas independentes se multiplicam, [p=0.2] e {c}o binomial conta de quantos jeitos dá para escolher alguns entre vários. [p=0.3] Se faltar alguma, procure no canal."),
    # uma ordem
    dict(id="s04", block="ordem", text="Comece por {a}uma ordem só: [p=0.2] {b}cara, cara, coroa, coroa, coroa. [p=0.3] Cada jogada tem chance {c}um meio, [p=0.2] e uma jogada não muda a outra. [p=0.2] {d}Um meio, multiplicado cinco vezes, [p=0.2] dá {e}um trinta e dois avos."),
    dict(id="s05", block="ordens", text="Mas as duas caras podem cair {a}em qualquer par de jogadas: [p=0.2] {b}na primeira e na terceira, [p=0.2] {c}na quarta e na quinta, e assim por diante. [p=0.3] Quantas ordens? [p=0.2] É escolher {d}duas jogadas entre cinco: [p=0.2] {e}binomial de cinco sobre dois, que dá dez."),
    dict(id="s06", block="ordens", text="Cada ordem tem a mesma chance, um trinta e dois avos. [p=0.2] {a}Dez vezes um trinta e dois avos dá dez trinta e dois avos. [p=0.2] {b}Dividindo em cima e embaixo por dois: cinco dezesseis avos."),
    # regra
    dict(id="s07", block="regra", text="Essa conta tem nome: {a}distribuição binomial. [p=0.2] Ela vale quando você repete {b}a mesma tentativa várias vezes, [p=0.2] {c}sempre com a mesma chance, sem uma mudar a outra, [p=0.2] e cada tentativa tem {d}só dois resultados: sucesso ou fracasso."),
    dict(id="s08", block="regra", text="A chance de {a}exatamente cá sucessos em ene tentativas tem três partes. [p=0.2] Primeiro, {b}o binomial de ene sobre cá. [p=0.2] Depois, {c}a chance de sucesso, elevada a cá. [p=0.2] Por fim, {d}a chance de fracasso, elevada a ene menos cá, que é o número de fracassos. [p=0.2] Multiplique as três. [p=0.3] {e}Nos livros, pê é a chance de sucesso, e quê, a de fracasso."),
    # dado
    dict(id="s09", block="dado", text="Agora, com chances diferentes. [p=0.2] Você joga {a}um dado três vezes. [p=0.2] Qual a chance de sair {b}exatamente um seis? [p=0.3] Sucesso é o seis: {c}um sexto. [p=0.2] Fracasso é qualquer outra face: [p=0.2] {d}cinco faces em seis, cinco sextos."),
    dict(id="s10", block="dado", text="{a}Binomial de três sobre um dá três: [p=0.2] o seis pode vir na primeira, na segunda ou na terceira jogada. [p=0.3] {b}Um sexto, uma vez. [p=0.2] {c}Cinco sextos, duas vezes: vinte e cinco trinta e seis avos. [p=0.3] {d}Três vezes um sexto vezes vinte e cinco trinta e seis avos [p=0.2] dá setenta e cinco duzentos e dezesseis avos. [p=0.2] Dividindo em cima e embaixo por três: {e}vinte e cinco setenta e dois avos, [p=0.2] quase trinta e cinco por cento."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}esquecer o binomial. [p=0.2] Nas cinco moedas, a pessoa calcula a chance de {b}uma ordem só, [p=0.2] um trinta e dois avos, [p=0.2] e responde {c}pouco mais de três por cento. [p=0.3] Mas existem {d}dez ordens com duas caras, [p=0.2] e todas contam. [p=0.2] {e}Multiplique pelo número de ordens."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, quando a chance é {a}um meio, como na moeda. [p=0.2] Toda ordem tem a mesma chance: {b}um meio elevado a ene. [p=0.3] Então a resposta é {c}o número da linha ene do triângulo, [p=0.2] dividido por {d}dois elevado a ene."),
    dict(id="s13", block="atalho", text="Cinco moedas: a linha cinco é {a}um, cinco, dez, dez, cinco, um, [p=0.2] e dois elevado a cinco é trinta e dois. [p=0.3] {b}Nenhuma cara: um trinta e dois avos. [p=0.2] {c}Duas caras: dez trinta e dois avos. [p=0.2] {d}Três caras: dez trinta e dois avos também. [p=0.3] Funciona porque a linha soma {e}dois elevado a ene, o total de ordens. [p=0.2] {f}Com chance diferente de um meio, como no dado, use a regra completa."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma prova tem {a}três questões, cada uma com quatro alternativas. [p=0.2] Alguém {b}chuta todas. [p=0.3] {c}Qual a chance de acertar exatamente duas?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Acertar é {a}uma alternativa em quatro: um quarto. [p=0.2] Errar é {b}três em quatro: três quartos. [p=0.3] {c}Binomial de três sobre dois dá três."),
    dict(id="s17", block="resposta", text="{a}Um quarto, duas vezes: um dezesseis avos. [p=0.2] {b}Três quartos, uma vez. [p=0.3] {c}Três vezes um dezesseis avos vezes três quartos [p=0.2] dá {d}nove sessenta e quatro avos, [p=0.2] uns catorze por cento."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}conte as ordens com o binomial [p=0.2] e {b}multiplique pela chance de uma ordem."),
    dict(id="s19", block="fim", text="Na próxima aula, uma ideia simples que garante resultados sem calcular chance nenhuma: [p=0.2] {a}o princípio da casa dos pombos. [p=0.2] Com ele, você mostra que, {b}entre treze pessoas, duas fazem aniversário no mesmo mês. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
