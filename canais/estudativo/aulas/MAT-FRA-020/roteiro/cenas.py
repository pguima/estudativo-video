# Estudativo · MAT-FRA-020 — Dízimas: reconhecer e prever (Matemática · Frações e Decimais).
# Habilidade: apontar o período de 5/11 = 0,4545… e saber sem dividir que 7/40 é decimal exato e 7/30 é dízima, olhando a fatoração do denominador.
# Pré-requisitos: MAT-DIV-003 (primos e fatoração), MAT-FRA-019 (fração em decimal). Próxima: MAT-FRA-021.
# Questão inédita, criada para esta aula. Sem potências e sem converter dízima em fração (fora do módulo).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dízimas: reconhecer e prever"

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
    dict(id="s01", block="gancho", text="Faça {a}cinco dividido por onze. [p=0.3] Vem {b}zero vírgula quatro, cinco, quatro, cinco, quatro, cinco... [p=0.3] e a conta {c}não acaba nunca. [p=0.3] Será que dá para saber disso {d}antes de começar a dividir?"),
    dict(id="s02", block="gancho", text="Dá, sim. [p=0.2] {a}Até o fim desta aula, você vai apontar o trecho que se repete [p=0.2] e prever, só olhando o denominador, se a divisão acaba. [p=0.2] E ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}transformar fração em decimal, dividindo o de cima pelo de baixo, [p=0.2] e {c}fatorar um número, escrevendo ele como multiplicação de primos. [p=0.3] Se faltar alguma, procure no canal."),
    # por que repete
    dict(id="s04", block="repete", text="Por que a conta não acaba? [p=0.3] {a}Cinco é menor que onze: zero vírgula. [p=0.2] {b}Cinquenta dividido por onze dá quatro, e sobram seis. [p=0.2] {c}Sessenta dividido por onze dá cinco, e sobram cinco."),
    dict(id="s05", block="repete", text="Olhe o que sobrou: {a}voltou o cinco, o número do começo. [p=0.3] Daqui em diante, {b}a conta repete tudo igual, [p=0.2] quatro, cinco, quatro, cinco, para sempre."),
    # nomes
    dict(id="s06", block="nomes", text="Esse número tem nome: {a}dízima. [p=0.2] É um decimal com um grupo de algarismos que se repete sem fim. [p=0.3] {b}Os três pontinhos avisam que continua. [p=0.3] O grupo que se repete se chama {c}período. [p=0.2] Aqui, o período é {d}quarenta e cinco."),
    dict(id="s07", block="nomes", text="Quando a conta acaba, como em {a}um quarto, zero vírgula vinte e cinco, [p=0.3] o nome é {b}decimal exato."),
    # por que só 2 e 5
    dict(id="s08", block="porque", text="Como prever qual dos casos vai acontecer? [p=0.3] Todo decimal exato é uma fração com {a}um seguido de zeros embaixo: dez, cem, mil. [p=0.3] Fatore esses números: {b}dez é dois vezes cinco. [p=0.2] {c}Cem é dois vezes dois vezes cinco vezes cinco. [p=0.3] Só aparecem {d}os primos dois e cinco."),
    dict(id="s09", block="porque", text="Daí sai a regra, para a fração já simplificada. [p=0.2] {a}Denominador só com fatores dois e cinco: [p=0.2] dá para completar os fatores que faltam até chegar em dez, cem, mil ou mais, e {b}o decimal é exato. [p=0.3] {c}Apareceu outro primo, como três ou sete? [p=0.2] Esses números só têm fatores dois e cinco, então a fração nunca chega lá. [p=0.2] {d}Vira dízima."),
    # exemplos
    dict(id="s10", block="exemplos", text="Teste com {a}sete quarenta avos. [p=0.2] {b}Quarenta é dois vezes dois vezes dois vezes cinco. [p=0.2] Só dois e cinco: {c}decimal exato. [p=0.3] {d}Mil tem três fatores dois e três fatores cinco. [p=0.2] Aqui faltam dois fatores cinco, e cinco vezes cinco é vinte e cinco. [p=0.2] Então {e}multiplique em cima e embaixo por vinte e cinco: [p=0.2] {f}cento e setenta e cinco milésimos, [p=0.1] zero vírgula cento e setenta e cinco."),
    dict(id="s11", block="exemplos", text="Veja {a}sete trinta avos, que não simplifica. [p=0.2] {b}Trinta é dois vezes três vezes cinco. [p=0.2] Apareceu o {c}três: {d}dízima. [p=0.3] E de fato dá {e}zero vírgula dois, três, três, três... [p=0.3] O dois aparece uma vez só, então o período é {f}três. [p=0.3] E o onze do começo? [p=0.2] {g}Onze é primo e não é dois nem cinco: [p=0.2] por isso aquela conta nunca acabava."),
    # erro
    dict(id="s12", block="erro", text="Cuidado: a regra vale para a {a}fração na forma mais simples. [p=0.2] {b}Nove trinta avos tem o mesmo trinta embaixo, e parece dízima. [p=0.3] Só que nove e trinta se dividem por três: {c}três décimos, [p=0.2] {d}zero vírgula três, decimal exato."),
    dict(id="s13", block="erro", text="O três do denominador {a}sumiu na simplificação. [p=0.3] Então, {b}simplifique primeiro, [p=0.2] e só depois {c}olhe o denominador."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, com a fração já simplificada: {a}corte os zeros do fim do denominador. [p=0.3] Cada zero é um {b}dois vezes cinco, que não atrapalha nada. [p=0.3] {c}Sete quarenta avos: corta o zero do quarenta, sobra quatro, que é dois vezes dois. {d}Exato. [p=0.3] {e}Sete trinta avos: corta o zero do trinta, sobra três. {f}Dízima."),
    dict(id="s15", block="atalho", text="Não compensa quando {a}o denominador não termina em zero, como setenta e cinco. [p=0.2] Aí, {b}fatore normalmente: [p=0.2] {c}setenta e cinco é três vezes cinco vezes cinco."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Sem fazer a divisão, {a}classifique cada fração como decimal exato ou dízima: [p=0.2] {b}nove cinquenta avos, [p=0.2] {c}cinco doze avos [p=0.2] e {d}seis quinze avos."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Cinquenta é dois vezes cinco vezes cinco: [p=0.2] {b}decimal exato. [p=0.3] {c}Doze é dois vezes dois vezes três. [p=0.2] Cinco doze avos não simplifica e o três fica lá: {d}dízima."),
    dict(id="s19", block="resposta", text="{a}Seis quinze avos é a pegadinha. [p=0.2] Quinze tem fator três, mas a fração simplifica: [p=0.2] {b}divida em cima e embaixo por três. [p=0.2] {c}Dois quintos. [p=0.3] Embaixo ficou só o cinco: {d}decimal exato."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}simplifique, [p=0.2] {b}fatore o denominador. [p=0.3] {c}Só dois e cinco, decimal exato. [p=0.2] {d}Outro primo, dízima."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}pratica tudo de números decimais [p=0.2] em {b}problemas de dinheiro e de medida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
