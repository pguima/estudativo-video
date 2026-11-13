# Estudativo · QUI-CAL-001 — Massa atômica e massa molecular (Química · Cálculos Químicos · Mol e massa molar).
# Habilidade: calcular com a tabela periódica que a massa molecular de C₆H₁₂O₆ é 180 u.
# Pré-requisitos: QUI-MIS-001, QUI-ATO-008, MAT-FRA-016. Próxima: QUI-CAL-002 (mol, massa molar e Avogadro).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "u" é lido como a letra u.
# Primeira aula do módulo Cálculos Químicos: guarda a linguagem visual da trilha (veja o visual.py). Questão inédita.
# Fatos: H ≈ 1,67 × 10⁻²⁴ g (23 zeros depois da vírgula); u = 1/12 do carbono-12; Cl na natureza ≈ 75% de ³⁵Cl e 25% de ³⁷Cl,
# média 35,45 (a prova usa 35,5); (3·35 + 37)/4 = 35,5. Porcentagem ainda não foi ensinada: "três em cada quatro".

TITULO = "Massa atômica e massa molecular"

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
    dict(id="s01", block="gancho", text="{a}Cê seis agá doze ó seis. [p=0.3] É a glicose, o açúcar que corre no seu sangue. [p=0.3] Uma molécula dela tem {b}massa cento e oitenta. [p=0.3] {c}Cento e oitenta o quê? [p=0.2] E como se chega nesse número {d}em poucos segundos?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber {b}o que é a massa atômica, [p=0.2] {c}calcular a massa de qualquer molécula [p=0.2] e ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas. [p=0.2] {b}Ler o índice de uma fórmula: em agá dois ó, dois hidrogênios e um oxigênio. [p=0.2] {c}Achar um elemento na tabela periódica. [p=0.2] E {d}multiplicar decimais, como dois vezes trinta e cinco e meio. [p=0.3] Se faltar alguma, procure no canal."),
    # a unidade u
    dict(id="s04", block="unidade", text="O átomo é leve demais para a balança. [p=0.2] {a}Em gramas, a massa de um átomo de hidrogênio tem vinte e três zeros depois da vírgula. [p=0.3] {b}Por isso, a Química criou uma régua própria: [p=0.1] a unidade de massa atômica, {c}o u. [p=0.3] {d}Ela vale um doze avos da massa de um átomo de carbono doze, [p=0.2] o carbono com seis prótons e seis nêutrons."),
    dict(id="s05", block="unidade", text="Na prática, {a}cada próton e cada nêutron tem cerca de um u. [p=0.2] {b}Os elétrons são tão leves que quase não contam. [p=0.3] {c}Então o hidrogênio comum, com um próton, tem cerca de um u. [p=0.2] {d}O oxigênio, com oito prótons e oito nêutrons, cerca de dezesseis u."),
    # a massa na tabela
    dict(id="s06", block="tabela", text="Você não precisa contar prótons: [p=0.2] {a}a massa atômica vem escrita na casa de cada elemento da tabela periódica. [p=0.3] {b}No carbono, doze. [p=0.2] {c}No cloro, trinta e cinco e meio."),
    dict(id="s07", block="tabela", text="Por que meio? [p=0.2] {a}Porque o cloro da natureza é uma mistura de isótopos, [p=0.1] átomos do mesmo elemento com números de nêutrons diferentes. [p=0.3] {b}Três em cada quatro têm massa trinta e cinco. [p=0.2] {c}Um em cada quatro tem massa trinta e sete. [p=0.3] {d}A tabela mostra um valor entre trinta e cinco e trinta e sete, [p=0.1] mais perto do trinta e cinco, porque ele é a maioria."),
    dict(id="s08", block="tabela", text="{a}Na prova, os valores quase sempre vêm no enunciado, já arredondados: [p=0.2] {b}agá vale um, [p=0.1] {c}cê vale doze, [p=0.1] {d}ó vale dezesseis."),
    # massa molecular
    dict(id="s09", block="molecular", text="{a}A massa molecular é a soma das massas de todos os átomos da molécula. [p=0.3] Comece pela água, {b}agá dois ó. [p=0.2] {c}Dois hidrogênios: dois vezes um dá dois. [p=0.2] {d}Um oxigênio: dezesseis. [p=0.2] {e}Dois mais dezesseis dá dezoito u."),
    dict(id="s10", block="molecular", text="{a}O índice manda multiplicar. [p=0.2] No gás carbônico, {b}cê ó dois: [p=0.2] {c}um carbono, doze. [p=0.2] {d}Dois oxigênios: dois vezes dezesseis dá trinta e dois. [p=0.2] {e}Doze mais trinta e dois dá quarenta e quatro u. [p=0.3] {f}Com decimal é igual: [p=0.1] no gás cloro, cê ele dois, dois vezes trinta e cinco e meio dá setenta e um u."),
    # glicose
    dict(id="s11", block="glicose", text="Vamos à glicose, {a}cê seis agá doze ó seis. [p=0.3] Monte uma linha para cada elemento: [p=0.2] {b}quantos átomos, vezes a massa de um. [p=0.3] {c}Carbono: seis vezes doze dá setenta e dois. [p=0.2] {d}Hidrogênio: doze vezes um dá doze. [p=0.2] {e}Oxigênio: seis vezes dezesseis dá noventa e seis."),
    dict(id="s12", block="glicose", text="{a}Some as linhas: [p=0.1] setenta e dois mais doze mais noventa e seis [p=0.1] {b}dá cento e oitenta u. [p=0.3] {c}Aí está o cento e oitenta do começo."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}esquecer o índice e somar cada elemento uma vez só. [p=0.3] {b}Doze mais um mais dezesseis dá vinte e nove. [p=0.3] {c}Isso é a massa de um carbono, um hidrogênio e um oxigênio, [p=0.1] não a da glicose. [p=0.3] {d}Cada índice multiplica a massa do seu elemento."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho. [p=0.2] Repare nos índices da glicose: {a}seis, doze e seis. [p=0.2] {b}Todos se dividem por seis. [p=0.3] Então a glicose é {c}seis vezes o pedaço cê agá dois ó."),
    dict(id="s15", block="atalho", text="{a}Cê agá dois ó: doze mais dois mais dezesseis dá trinta. [p=0.2] {b}Vezes seis dá cento e oitenta. [p=0.3] {c}Funciona porque a molécula tem seis cópias desse pedaço. [p=0.3] {d}Não compensa quando nenhum número divide todos os índices, como em cê dois agá seis ó: [p=0.1] aí, faça a linha de cada elemento. [p=0.2] {e}Esse pedaço tem nome, e é assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] O álcool do posto é o etanol, {a}cê dois agá seis ó. [p=0.3] Use {b}cê doze, agá um e ó dezesseis. [p=0.2] {c}Qual é a massa molecular do etanol?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá, uma linha por elemento. [p=0.2] {a}Carbono: dois vezes doze dá vinte e quatro. [p=0.2] {b}Hidrogênio: seis vezes um dá seis. [p=0.2] {c}Oxigênio, sem índice: dezesseis. [p=0.3] {d}Vinte e quatro mais seis mais dezesseis [p=0.1] {e}dá quarenta e seis u. [p=0.3] {f}Quem esqueceu os índices chegou a vinte e nove."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}a massa atômica está na tabela, em u; [p=0.2] {b}a massa molecular soma todos os átomos, [p=0.1] {c}com cada índice multiplicando a massa do seu elemento."),
    dict(id="s20", block="fim", text="Na próxima aula, esse dezoito da água vira {a}dezoito gramas, [p=0.2] e você conhece {b}o mol, a dúzia da Química. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
