# Estudativo · MAT-CNT-017 — Sorteios sucessivos com e sem reposição (Matemática · Contagem e Probabilidade · União, interseção e condicional).
# Habilidade: achar a chance de tirar duas bolas azuis de uma urna com 3 azuis e 2 vermelhas: 9/25 com reposição e 3/10 sem.
# Pré-requisitos: MAT-CNT-016 (eventos independentes: multiplicar). Próxima: MAT-CNT-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Combinação não está em "Já ensinado": tudo por multiplicação de chances; "pista" como em MAT-CNT-015.
# Urna 3 azuis + 2 vermelhas (desenhar as bolas; sem reposição, a bola que sai fica de lado).
# Com: 3/5 × 3/5 = 9/25 = 36%. Sem: 3/5 × 2/4 = 6/20 = 3/10 = 30%.
# Duas vermelhas: com 2/5 × 2/5 = 4/25 = 16% · sem 2/5 × 1/4 = 2/20 = 1/10 = 10%.
# Erro: só o total desce: 3/5 × 3/4 = 9/20 (45%).
# Atalho (mesma cor): desce um em cima e um embaixo: 3/5 × 2/4 × 1/3 = 6/60 = 1/10. Cor muda: azul e vermelha 3/5 × 2/4 = 3/10 (só o total desce).
# Questão: 10 lâmpadas, 3 queimadas (7 boas): com 7/10 × 7/10 = 49/100 = 49% · sem 7/10 × 6/9 = 42/90 = 7/15 ≈ 46,7%.

TITULO = "Sorteios sucessivos com e sem reposição"

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
    dict(id="s01", block="gancho", text="Uma urna tem {a}três bolas azuis e duas vermelhas. [p=0.2] Você tira {b}duas bolas. [p=0.3] A chance de ambas serem azuis depende de um detalhe: [p=0.2] {c}a primeira bola volta para a urna antes da segunda? [p=0.3] Se volta, a chance dá {d}trinta e seis por cento. [p=0.2] Se não volta, dá {e}trinta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula sorteios em sequência, [p=0.2] devolvendo ou não, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}eventos independentes multiplicam as chances, [p=0.2] e {c}na probabilidade condicional, a pista vira o novo total. [p=0.3] Se faltar alguma, procure no canal."),
    # com reposição
    dict(id="s04", block="com", text="Primeiro, {a}com reposição. [p=0.2] Repor quer dizer {b}devolver a bola à urna antes do próximo sorteio. [p=0.3] Na primeira tirada, são {c}três azuis em cinco bolas: [p=0.2] {d}três quintos."),
    dict(id="s05", block="com", text="A bola volta, [p=0.2] e a urna fica {a}igualzinha ao começo. [p=0.2] Na segunda, de novo {b}três quintos. [p=0.3] A primeira tirada não muda a segunda: [p=0.2] {c}são independentes. [p=0.2] {d}Três quintos vezes três quintos dá nove vinte e cinco avos, [p=0.2] que são {e}trinta e seis por cento."),
    # sem reposição
    dict(id="s06", block="sem", text="Agora, {a}sem reposição: [p=0.2] a primeira bola {b}fica fora da urna. [p=0.3] Na primeira tirada, a urna ainda está completa: {c}três quintos."),
    dict(id="s07", block="sem", text="Saiu azul, [p=0.2] e essa é a pista. [p=0.2] Na urna, sobram {a}quatro bolas, [p=0.2] e só {b}duas azuis. [p=0.3] A chance da segunda azul, sabendo que a primeira foi azul, é {c}dois quartos."),
    dict(id="s08", block="sem", text="Multiplique: {a}três quintos vezes dois quartos dá seis vinte avos. [p=0.2] Dividindo por dois: {b}três décimos, [p=0.2] que são {c}trinta por cento. [p=0.3] Caiu porque {d}cada azul que sai deixa a urna com menos azuis."),
    dict(id="s09", block="sem", text="Teste com {a}duas vermelhas. [p=0.2] Com reposição: {b}dois quintos vezes dois quintos dá quatro vinte e cinco avos, [p=0.2] dezesseis por cento. [p=0.3] Sem reposição: {c}dois quintos vezes um quarto dá dois vinte avos, [p=0.2] que é {d}um décimo: [p=0.2] dez por cento. [p=0.3] Sem reposição, a segunda tirada depende da primeira: [p=0.2] {e}os eventos são dependentes."),
    # regra
    dict(id="s10", block="regra", text="A regra vale sempre: {a}multiplique as chances de cada tirada. [p=0.2] O que muda é {b}a urna. [p=0.2] {c}Com reposição, ela fica igual. [p=0.2] {d}Sem reposição, ela perde a bola que saiu."),
    dict(id="s11", block="regra", text="E um detalhe de prova: [p=0.2] {a}tirar duas bolas de uma vez [p=0.2] é o mesmo que {b}sem reposição. [p=0.2] A primeira bola não volta para a urna antes da segunda."),
    # erro
    dict(id="s12", block="erro", text="O erro comum aparece no sem reposição. [p=0.2] A pessoa lembra que a urna perdeu uma bola, [p=0.2] mas tira só {a}do total. [p=0.2] Faz {b}três quintos vezes três quartos, [p=0.2] que dá {c}nove vinte avos. [p=0.3] Só que a bola que saiu era {d}azul. [p=0.2] Ela sai {e}de cima e de baixo: [p=0.2] dois quartos."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho. [p=0.2] Sem reposição, tirando sempre {a}a mesma cor, [p=0.2] cada fração nova {b}desce um em cima e um embaixo. [p=0.3] {c}Três azuis seguidas: [p=0.2] {d}três quintos, [p=0.2] dois quartos [p=0.2] e um terço."),
    dict(id="s14", block="atalho", text="{a}Em cima, três vezes dois vezes um dá seis. [p=0.2] {b}Embaixo, cinco vezes quatro vezes três dá sessenta. [p=0.2] {c}Seis sessenta avos, que é um décimo."),
    dict(id="s15", block="atalho", text="Funciona porque cada bola que sai {a}é daquela cor e faz parte do total. [p=0.3] {b}Não vale quando a cor muda. [p=0.2] {c}Azul e depois vermelha [p=0.2] é três quintos vezes {d}dois quartos, [p=0.2] porque nenhuma vermelha saiu: [p=0.2] {e}só o total desceu."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma caixa tem {a}dez lâmpadas, [p=0.2] e {b}três estão queimadas. [p=0.2] Você tira {c}duas, uma depois da outra. [p=0.3] {d}Qual a chance de ambas funcionarem, com reposição e sem reposição?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Funcionam {a}sete das dez. [p=0.3] {b}Com reposição: [p=0.2] sete décimos vezes sete décimos dá {c}quarenta e nove centésimos, [p=0.2] ou {d}quarenta e nove por cento."),
    dict(id="s19", block="resposta", text="{a}Sem reposição: [p=0.2] na segunda tirada, sobram {b}seis boas em nove lâmpadas. [p=0.2] {c}Sete décimos vezes seis nonos dá quarenta e dois noventa avos. [p=0.3] Dividindo por seis: {d}sete quinze avos, [p=0.2] um pouco menos de quarenta e sete por cento."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}multiplique as chances de cada tirada. [p=0.2] {b}Sem reposição, a bola que saiu sai do total e da sua cor."),
    dict(id="s21", block="fim", text="Na próxima aula, essas contas viram {a}uma árvore de probabilidades: [p=0.2] você multiplica ao longo de cada caminho, [p=0.2] {b}soma os caminhos [p=0.2] e calcula até {c}a chance de um filho herdar uma característica dos pais. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
