# Estudativo · MAT-FUN-002 — O que é função: cada entrada, uma saída (Matemática · Funções · O que é função).
# Habilidade: apontar a entrada e a saída em P = 5 + 2,5d, o preço de um táxi, e dizer se uma tabela ou um diagrama de flechas representa uma função.
# Pré-requisitos: MAT-EQU-002 (valor numérico), MAT-CON-001 (conjuntos). Próxima: MAT-FUN-003.
# Questão inédita, criada para esta aula. Táxi de valores inventados. Plano cartesiano (MAT-FUN-001) fora da ficha: não usado.
# Contas: P(4) = 5 + 2,5 × 4 = 15 · P(10) = 5 + 25 = 30.
# Tabelas: x 1, 2, 3, 4 → y 3, 5, 7, 9 (função) · x 1, 2, 2, 3 → y 2, 4, 6, 8 (não: a entrada 2 dá 4 e 6).
# Diagramas A = {1, 2, 3} → B = {2, 4, 6, 8}: (1) 1→2, 2→4, 3→6, sobra o 8: função · (2) 1→2, 2→4, 2→6, 3→8: não · (3) 1→2, 2→4, 3 sem flecha: não.
# Erro: pessoas → mês do aniversário, Ana e Bruno → maio: ainda é função.
# Questão: C = 40 + 90m · C(3) = 270 + 40 = 310 · tabela x −1, 0, 1, −1 → y 2, 1, 2, 3: não é função (−1 dá 2 e 3); a saída 2 repetida não atrapalha.
# Visual: fórmula P = 5 + 2,5d com legendas; máquina entrada → saída; tabelas de duas colunas; três diagramas de flechas (ovais A e B); diagrama pessoas → meses.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras: pê, dê, á, bê, cê, eme.

TITULO = "O que é função: cada entrada, uma saída"

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
    dict(id="s01", block="gancho", text="Um táxi cobra {a}cinco reais só para começar a corrida, [p=0.2] e mais {b}dois reais e cinquenta centavos por quilômetro. [p=0.3] Você pode rodar dois quilômetros ou vinte. [p=0.2] Mas, para cada distância, {c}o taxímetro mostra um preço só. [p=0.3] Essa ideia simples tem nome: {d}função."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você aponta a entrada e a saída de uma fórmula, [p=0.2] diz se uma tabela ou um desenho com flechas é função [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}trocar a letra por um número entre parênteses e fazer a conta, [p=0.2] e {c}conjunto, um grupo de elementos entre chaves. [p=0.3] Se faltar alguma, procure no canal."),
    # fórmula
    dict(id="s04", block="formula", text="O preço do táxi cabe numa fórmula: [p=0.2] {a}pê igual a cinco mais dois vírgula cinco vezes dê. [p=0.3] {b}Pê é o preço, em reais. [p=0.2] {c}Dê é a distância, em quilômetros. [p=0.2] {d}O cinco é a parte fixa, que você paga mesmo sem rodar. [p=0.2] E {e}dois vírgula cinco é quanto custa cada quilômetro."),
    dict(id="s05", block="formula", text="Uma corrida de {a}quatro quilômetros: [p=0.2] {b}dois vírgula cinco vezes quatro dá dez. [p=0.2] {c}Cinco mais dez dá quinze reais. [p=0.3] Uma de {d}dez quilômetros: [p=0.2] {e}dois vírgula cinco vezes dez dá vinte e cinco. [p=0.2] {f}Mais cinco dá trinta reais."),
    # entrada e saída
    dict(id="s06", block="maquina", text="Repare no caminho. [p=0.2] {a}Você escolhe a distância. [p=0.2] {b}A fórmula devolve o preço. [p=0.3] A distância é a {c}entrada: o número que entra na conta. [p=0.2] O preço é a {d}saída: o número que sai dela. [p=0.3] {e}O preço depende da distância, e não o contrário."),
    dict(id="s07", block="maquina", text="Pense numa {a}máquina. [p=0.2] Entra o quatro, {b}sai o quinze. [p=0.2] Entra o dez, {c}sai o trinta. [p=0.3] Uma regra assim é uma função [p=0.2] quando cumpre uma condição: [p=0.2] {d}cada entrada dá exatamente uma saída. [p=0.3] Nenhuma entrada fica sem saída, [p=0.2] e {e}nenhuma entrada dá duas saídas."),
    dict(id="s08", block="maquina", text="Na fórmula, a pista é {a}a letra sozinha de um lado do igual: [p=0.2] ela costuma ser a saída. [p=0.2] {b}A letra que está na conta, do outro lado, é a entrada. [p=0.3] {c}É pista, não é regra. [p=0.2] Na dúvida, pergunte {d}quem depende de quem."),
    # tabela
    dict(id="s09", block="tabela", text="Às vezes a função vem numa {a}tabela, [p=0.2] com as entradas numa coluna e as saídas na outra. [p=0.3] Nesta, {b}cada entrada aparece uma vez, com o seu resultado: é função. [p=0.3] {c}Nesta outra, a entrada dois aparece duas vezes: [p=0.2] {d}uma com saída quatro, outra com saída seis. [p=0.2] A mesma entrada deu {e}duas saídas. [p=0.2] {f}Não é função."),
    # flechas
    dict(id="s10", block="flechas", text="Também pode vir em {a}diagrama de flechas: [p=0.2] {b}o conjunto das entradas à esquerda, [p=0.2] {c}o das saídas à direita, [p=0.2] e uma flecha liga cada entrada à sua saída. [p=0.3] {d}O conjunto á tem um, dois e três. [p=0.2] {e}O conjunto bê tem dois, quatro, seis e oito."),
    dict(id="s11", block="flechas", text="Para ser função, olhe o lado de á: [p=0.2] {a}de cada elemento sai exatamente uma flecha. [p=0.3] {b}No primeiro desenho, o um vai para o dois. [p=0.2] O dois vai para o quatro. [p=0.2] O três vai para o seis. [p=0.2] {c}É função. [p=0.3] O oito ficou sem flecha, e tudo bem: [p=0.2] {d}em bê, pode sobrar elemento."),
    dict(id="s12", block="flechas", text="{a}No segundo desenho, do elemento dois saem duas flechas. [p=0.2] {b}Não é função. [p=0.3] {c}No terceiro, o três não solta flecha nenhuma. [p=0.2] Uma entrada ficou sem saída: [p=0.2] {d}também não é função."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}duas flechas chegando no mesmo elemento estragam a função. [p=0.3] Pense em {b}pessoas e o mês do aniversário. [p=0.2] {c}Ana e Bruno fazem aniversário em maio: [p=0.2] {d}duas flechas chegam em maio. [p=0.3] Mas {e}cada pessoa tem um mês só. [p=0.2] Então {f}é função. [p=0.3] O problema é {g}sair mais de uma flecha, e não chegar."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}olhe só o lado das entradas. [p=0.3] Na tabela, {b}procure entrada repetida com saídas diferentes. [p=0.2] No diagrama, {c}conte as flechas que saem de cada elemento de á. [p=0.3] {d}Nenhuma entrada com duas saídas e nenhuma esquecida? É função."),
    dict(id="s15", block="atalho", text="Funciona porque só duas coisas derrubam uma função: [p=0.2] {a}uma entrada com duas respostas, [p=0.2] ou {b}uma entrada sem resposta. [p=0.2] O lado das saídas não derruba nada. [p=0.3] Cuidado com a tabela que {c}repete a linha inteira, [p=0.2] como dois e quatro, escrito duas vezes. [p=0.2] É a mesma informação de novo, [p=0.2] e {d}ainda é função."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma academia cobra {a}quarenta reais de matrícula e noventa reais por mês. [p=0.2] A fórmula é {b}cê igual a quarenta mais noventa vezes eme. [p=0.3] {c}Qual letra é a entrada e qual é a saída? [p=0.2] {d}Quanto custam três meses? [p=0.3] E {e}esta tabela é função?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] O custo depende de quantos meses você fica: [p=0.2] {a}a entrada é eme, os meses. [p=0.2] {b}A saída é cê, o custo. [p=0.3] Para três meses: {c}noventa vezes três dá duzentos e setenta. [p=0.2] {d}Mais quarenta dá trezentos e dez reais."),
    dict(id="s19", block="resposta", text="Na tabela, olhe a coluna de entrada: [p=0.2] {a}o menos um aparece duas vezes, [p=0.2] {b}uma com saída dois, outra com saída três. [p=0.2] {c}Não é função. [p=0.3] E repare: {d}a saída dois também se repete, [p=0.2] com o menos um e com o um. [p=0.2] Isso, sozinho, {e}não atrapalharia."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a entrada é o que você escolhe, a saída é o que depende dela, [p=0.2] e {b}função é cada entrada com uma saída só."),
    dict(id="s21", block="fim", text="Na próxima aula, você aprende a escrita das provas: [p=0.2] {a}efe de xis. [p=0.2] Vai {b}calcular a saída de uma entrada [p=0.2] e fazer {c}o caminho de volta, da saída para a entrada. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
