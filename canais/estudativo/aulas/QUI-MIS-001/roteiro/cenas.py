# Estudativo · QUI-MIS-001 — Átomos, moléculas e fórmulas (Química · Matéria e Misturas · Matéria, substâncias e estados físicos).
# Habilidade: dizer quantos átomos de cada elemento há em H₂O e em C₂H₆O e diferenciar átomo, elemento e molécula.
# Pré-requisitos: nenhum. Próxima: QUI-MIS-002 (substância pura ou mistura; O₂ e O₃ são alótropos).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula de Química: guarda a linguagem visual da matéria (veja o visual.py). Questão inédita, criada para esta aula.
# Fórmulas narradas letra a letra, como se lê em sala: H₂O = "agá dois ó", C₂H₆O = "cê dois agá seis ó", CO₂ = "cê ó dois".
# Fatos: 118 elementos conhecidos (IUPAC); Na vem de natrium; CO (monóxido de carbono) é tóxico, Co é o cobalto;
# um fio de cabelo (0,05 a 0,1 mm) tem a espessura de centenas de milhares de átomos (0,1 a 0,3 nm cada);
# H₂SO₄ = ácido sulfúrico, o eletrólito da bateria de chumbo do carro. Um copo de água (250 g) tem cerca de 2,5 × 10²⁵ átomos ("trilhões de trilhões"). Parênteses, como em Al₂(SO₄)₃, ficam
# para outra aula: a soma direta dos índices erra ali (dá 10, o certo é 17).

TITULO = "Átomos, moléculas e fórmulas"

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
    dict(id="s01", block="gancho", text="{a}Agá dois ó. [p=0.3] É a fórmula da água, e nela aparece {b}um número só: o dois. [p=0.3] Mas a menor partícula de água tem {c}três átomos. [p=0.3] {d}De onde vem o terceiro?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai separar {b}átomo, elemento e molécula, [p=0.2] e contar os átomos de qualquer fórmula, como a do {c}álcool, cê dois agá seis ó. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Esta é a primeira aula de Química, então {a}você não precisa de nada antes. [p=0.2] Só saber {b}contar e multiplicar."),
    # átomo
    dict(id="s04", block="atomo", text="Comece pelo menor pedaço. [p=0.2] {a}Tudo o que você vê é feito de partículas minúsculas, os {b}átomos. [p=0.3] A água, o ar, a sua mão. [p=0.3] Eles são tão pequenos que, {c}na espessura de um fio de cabelo, [p=0.1] cabem centenas de milhares deles, lado a lado."),
    dict(id="s05", block="atomo", text="Ninguém enxerga um átomo a olho nu. [p=0.2] Por isso, aqui, {a}cada átomo vira uma bolinha."),
    # elemento
    dict(id="s06", block="elemento", text="Só num copo de água há {a}trilhões de trilhões de átomos. [p=0.3] Mas tipos de átomo, existem {b}poucos. [p=0.2] Cada tipo é um {c}elemento químico, [p=0.2] e hoje se conhecem {d}cento e dezoito. [p=0.3] O que faz um tipo ser diferente do outro {e}é assunto de outra aula."),
    dict(id="s07", block="elemento", text="Cada elemento tem um {a}símbolo, de uma ou duas letras. [p=0.2] {b}Agá é o hidrogênio. [p=0.1] {c}Ó é o oxigênio. [p=0.1] {d}Cê é o carbono. [p=0.3] Alguns vêm do nome em latim: [p=0.1] {e}o sódio é ene á, de natrium."),
    dict(id="s08", block="elemento", text="E repare na regra das letras: [p=0.2] {a}a primeira é sempre maiúscula, [p=0.1] a segunda, minúscula. [p=0.3] Por isso, {b}cê com ó minúsculo é um elemento só: o cobalto. [p=0.3] {c}Cê maiúsculo e ó maiúsculo são dois elementos, carbono e oxigênio: [p=0.1] é o monóxido de carbono, um gás tóxico. [p=0.3] {d}Cada letra maiúscula começa um elemento novo."),
    # molécula
    dict(id="s09", block="molecula", text="Em muitas substâncias, como a água, os átomos se prendem uns aos outros. [p=0.2] {a}Um grupo de átomos presos se chama molécula. [p=0.3] {b}A água é assim: [p=0.1] {c}dois hidrogênios presos a {d}um oxigênio. [p=0.3] {e}Como eles se prendem, e por que nem toda substância forma moléculas, [p=0.1] é assunto de outra aula, a de ligações químicas."),
    dict(id="s10", block="molecula", text="A molécula é {a}a menor parte da água que ainda é água. [p=0.3] Separe os átomos, e {b}o que sobra é hidrogênio e oxigênio, não água."),
    dict(id="s11", block="molecula", text="Para não confundir as três palavras, pense na escrita. [p=0.2] {a}Átomo é cada letra escrita. [p=0.2] {b}Elemento é o tipo: qual letra é, á ou erre. [p=0.2] {c}Molécula é a palavra. [p=0.3] Na palavra {d}arara, há cinco letras, [p=0.2] mas {e}só dois tipos: á e erre."),
    dict(id="s12", block="molecula", text="Na água é igual: [p=0.2] {a}três átomos, [p=0.2] {b}dois elementos [p=0.2] e, tudo junto, {c}uma molécula."),
    # fórmula
    dict(id="s13", block="formula", text="{a}A fórmula escreve a substância com símbolos e números. [p=0.2] {b}Os símbolos dizem quais elementos estão lá. [p=0.2] {c}O número pequeno, embaixo e à direita, se chama índice, [p=0.1] e diz quantos átomos daquele elemento há ali."),
    dict(id="s14", block="formula", text="Em agá dois ó, {a}o dois está colado no agá: dois hidrogênios. [p=0.3] {b}Já o ó, do oxigênio, não tem número. [p=0.2] Quando não há índice, {c}vale um. [p=0.3] Dois mais um: {d}três átomos. [p=0.2] Aí está o terceiro do começo."),
    dict(id="s15", block="formula", text="Vamos ao álcool comum, {a}cê dois agá seis ó. [p=0.3] Leia símbolo por símbolo. [p=0.2] {b}Cê dois: dois carbonos. [p=0.2] {c}Agá seis: seis hidrogênios. [p=0.2] {d}E o ó, sem número: um oxigênio. [p=0.3] São {e}três elementos [p=0.1] e, somando, {f}nove átomos em cada molécula."),
    # coeficiente
    dict(id="s16", block="coeficiente", text="E quando aparece {a}um número de tamanho normal, na frente da fórmula? [p=0.2] Ele se chama {b}coeficiente e conta moléculas inteiras. [p=0.3] {c}Dois agá dois ó são duas moléculas de água. [p=0.3] Cada uma tem dois hidrogênios, então são {d}quatro hidrogênios [p=0.1] e {e}dois oxigênios."),
    # erro
    dict(id="s17", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o índice vale para a fórmula toda. [p=0.3] No gás carbônico, {b}cê ó dois, [p=0.2] a pessoa lê {c}dois carbonos e dois oxigênios."),
    dict(id="s18", block="erro", text="Mas {a}o índice só vale para o símbolo que vem logo antes dele. [p=0.3] O dois está colado no ó: [p=0.1] {b}dois oxigênios. [p=0.2] {c}O cê não tem número: um carbono. [p=0.3] {d}Um carbono e dois oxigênios, três átomos. [p=0.3] Quem vale para a fórmula toda é {e}o coeficiente, o número da frente."),
    # atalho
    dict(id="s19", block="atalho", text="Agora, o atalho de prova para o total de átomos: [p=0.2] {a}some os índices, contando um onde não há número, [p=0.2] e {b}multiplique pelo coeficiente. [p=0.3] {c}Dois cê dois agá seis ó: [p=0.1] dois mais seis mais um dá {d}nove, [p=0.1] {e}vezes dois, dezoito."),
    dict(id="s20", block="atalho", text="Funciona porque {a}cada índice conta os átomos de um elemento, [p=0.2] e o coeficiente repete a molécula inteira. [p=0.3] {b}Não compensa quando a questão pede cada elemento separado: [p=0.2] aí, leia símbolo por símbolo, [p=0.1] e, se o mesmo símbolo aparecer duas vezes, {c}some as duas partes."),
    dict(id="s21", block="atalho", text="E {a}se a fórmula tiver parênteses, a soma direta pode errar: [p=0.2] isso fica para outra aula."),
    # questão
    dict(id="s22", block="questao", text="Hora de testar. [p=0.2] O ácido da bateria de carro tem a fórmula {a}agá dois esse ó quatro. [p=0.2] {b}O esse é o enxofre. [p=0.3] {c}Quantos átomos de cada elemento há em uma molécula? [p=0.2] {d}Quantos elementos? [p=0.2] E {e}quantos átomos no total?"),
    dict(id="s23", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s24", block="resposta", text="Vamos lá, símbolo por símbolo. [p=0.2] {a}Agá dois: dois hidrogênios. [p=0.2] {b}Esse sem número: um enxofre. [p=0.2] {c}Ó quatro: quatro oxigênios. [p=0.3] São {d}três elementos: hidrogênio, enxofre e oxigênio."),
    dict(id="s25", block="resposta", text="Para o total, o atalho: [p=0.1] {a}dois mais um mais quatro, [p=0.1] {b}sete átomos. [p=0.3] Quem esqueceu o um do enxofre {c}chegou a seis. [p=0.3] {d}Sete átomos, três elementos, uma molécula."),
    # fechamento
    dict(id="s26", block="fim", text="Resumindo: [p=0.1] {a}átomo é a partícula, [p=0.1] {b}elemento é o tipo de átomo, [p=0.1] {c}molécula é o grupo de átomos presos, [p=0.2] e {d}o índice conta os átomos do símbolo que vem antes dele."),
    dict(id="s27", block="fim", text="Na próxima aula, você vai usar as fórmulas para separar {a}substância pura de mistura, [p=0.2] e descobrir por que {b}ó dois e ó três, feitos do mesmo elemento, são substâncias diferentes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
