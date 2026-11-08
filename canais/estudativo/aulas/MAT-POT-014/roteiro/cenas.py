# Estudativo · MAT-POT-014 — Ordem de grandeza (Matemática · Potências e Raízes).
# Habilidade: dizer que a ordem de grandeza de 5.000 é 10⁴, usando a referência de 3,16.
# Pré-requisitos: MAT-POT-007 (raiz quadrada), MAT-POT-012 (notação científica). Próxima: MAT-POT-015.
# Questão inédita, criada para esta aula. A cidade de 25 mil habitantes é invenção.
# Fatos: população mundial cerca de 8 bilhões (ONU, World Population Prospects 2024: 8,2 bilhões em 2024; a revisão seguinte ainda não saiu).
# Referência: √10 ≈ 3,162 como ponto de virada (Toda Matéria, Prepara ENEM). Referência 5,5, a média aritmética entre 1 e 10, confirmada em Quero Bolsa.
# Com 5,5, o 5.000 ficaria em 10³; por isso o aviso da cena s13 manda seguir a prova quando ela indicar a referência.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ordem de grandeza"

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
    dict(id="s01", block="gancho", text="{a}Cinco mil está mais perto de {b}mil ou de {c}dez mil? [p=0.3] Pela subtração, de mil: a diferença é de quatro mil, contra cinco mil do outro lado. [p=0.3] Mas em {d}ordem de grandeza, a resposta é {e}dez mil."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender por quê, [p=0.2] vai achar a ordem de grandeza de qualquer número [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}escrever em notação científica [p=0.2] e {c}saber o que é raiz quadrada. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="oque", text="{a}Ordem de grandeza é a potência de dez mais próxima de um número. [p=0.3] Ela serve para dizer o tamanho da coisa, sem o valor exato. [p=0.3] Uma plateia tem {b}dezenas de pessoas? [p=0.2] {c}Centenas? [p=0.2] {d}Milhares?"),
    # medir em vezes
    dict(id="s05", block="vezes", text="Mas o que é mais próxima? [p=0.2] Entre potências de dez, cada degrau é um {a}vezes dez. [p=0.3] Então a distância se mede {b}em vezes, não em subtração. [p=0.3] De {c}mil até cinco mil, são {d}cinco vezes. [p=0.2] De {e}cinco mil até dez mil, só {f}duas vezes."),
    dict(id="s06", block="vezes", text="Duas vezes é menos que cinco vezes. [p=0.2] Por isso, {a}cinco mil está mais perto de dez mil. [p=0.3] A ordem de grandeza de cinco mil é {b}dez elevado a quatro."),
    # ponto de virada
    dict(id="s07", block="virada", text="E onde o número muda de lado? [p=0.2] Procure o {a}meio do caminho entre um e dez, medido em vezes. [p=0.3] Do um até ele, multiplicamos por {b}um certo número. [p=0.2] Dele até o dez, multiplicamos pelo {c}mesmo número. [p=0.3] Ou seja, {d}esse número vezes ele mesmo dá dez."),
    dict(id="s08", block="virada", text="Número vezes ele mesmo dando dez é a {a}raiz quadrada de dez, [p=0.2] que vale {b}cerca de três vírgula dezesseis. [p=0.3] Confira: {c}três vírgula dezesseis vezes três vírgula dezesseis dá {d}quase dez."),
    dict(id="s09", block="virada", text="Esse é o {a}ponto de virada. [p=0.2] {b}Até três vírgula dezesseis, a frente está mais perto do um. [p=0.2] {c}Depois dele, mais perto do dez. [p=0.3] E trocar a frente por dez é o mesmo que subir o expoente em um."),
    # método
    dict(id="s10", block="metodo", text="O método tem {a}dois passos. [p=0.2] {b}Passo um: escreva em notação científica. [p=0.2] {c}Cinco mil é cinco vezes dez elevado a três."),
    dict(id="s11", block="metodo", text="{a}Passo dois: compare o número da frente com três vírgula dezesseis. [p=0.2] {b}Se passar, o expoente sobe um. [p=0.2] {c}Se não passar, o expoente fica. [p=0.3] Cinco passa: {d}dez elevado a quatro."),
    dict(id="s12", block="metodo", text="Veja a virada acontecendo. [p=0.2] {a}Três mil é três vezes dez elevado a três. [p=0.2] Três não passa: {b}dez elevado a três. [p=0.3] {c}Quatro mil é quatro vezes dez elevado a três. [p=0.2] Quatro passa: {d}dez elevado a quatro."),
    # aviso
    dict(id="s13", block="aviso", text="Um aviso: {a}alguns materiais usam cinco vírgula cinco no lugar de três vírgula dezesseis. [p=0.2] Esse é o meio medido por subtração. [p=0.2] Por esse critério, cinco mil ficaria em dez ao cubo. [p=0.3] Então, {b}se a prova disser qual usar, siga a prova. [p=0.2] {c}Se não disser, fique com três vírgula dezesseis."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com os números pequenos. [p=0.2] Veja {a}zero vírgula zero zero zero sete, [p=0.2] que é {b}sete vezes dez elevado a menos quatro. [p=0.3] Sete passa, então o expoente sobe. [p=0.3] O erro é ir para {c}menos cinco, porque cinco parece mais que quatro."),
    dict(id="s15", block="erro", text="Mas {a}menos cinco é descer. [p=0.2] Subir é somar um: {b}menos quatro mais um dá menos três. [p=0.3] A ordem de grandeza é {c}dez elevado a menos três, ou zero vírgula zero zero um, [p=0.2] que está {d}pertinho de zero vírgula zero zero zero sete."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}olhe só o primeiro algarismo. [p=0.3] {b}Um ou dois: o expoente fica. [p=0.2] {c}De quatro a nove: sobe. [p=0.2] {d}Três: olhe o algarismo seguinte. [p=0.2] Depois do três, zero fica, e de dois para cima sobe."),
    dict(id="s17", block="atalho", text="Funciona porque o ponto de virada está {a}entre três e quatro. [p=0.3] {b}Não compensa quando a frente começa com três vírgula um: [p=0.2] aí, compare com três vírgula dezesseis com calma."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] O mundo tem {a}cerca de oito bilhões de pessoas. [p=0.3] Uma cidade tem {b}vinte e cinco mil habitantes. [p=0.3] {c}Qual é a ordem de grandeza de cada número?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Oito bilhões é oito vezes dez elevado a nove. [p=0.2] Oito passa, o expoente sobe: {b}dez elevado a dez."),
    dict(id="s21", block="resposta", text="{a}Vinte e cinco mil é dois vírgula cinco vezes dez elevado a quatro. [p=0.2] Dois vírgula cinco não passa, o expoente fica: {b}dez elevado a quatro."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}escreva em notação científica, [p=0.2] {b}compare a frente com três vírgula dezesseis [p=0.2] e {c}suba o expoente se passar."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai {a}praticar tudo isso, [p=0.2] fazendo contas e comparando medidas enormes e minúsculas, [p=0.2] como {b}a distância até o Sol. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
