# Estudativo · QUI-TER-002 — Lei de Hess (Química · Termoquímica e Cinética · Entalpia, Hess e energia de ligação).
# Habilidade: achar o ΔH de uma reação somando equações, invertendo ou multiplicando cada uma, inclusive com entalpias de formação.
# Pré-requisitos: QUI-TER-001, MAT-FRA-009, MAT-NUM-017. Próxima: QUI-TER-003 (energia de ligação).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Mol e substância simples não estão em "Já ensinado": a formação vale "para coeficiente um"; substância simples é explicada na hora.
# Valores de tabela (kJ, 25 °C): C + O₂ → CO₂ −394; CO + ½O₂ → CO₂ −283 ⇒ C + ½O₂ → CO −111 (tabela: −110,5).
# Formação: CH₄ −75, CO₂ −394, H₂O(l) −286 ⇒ combustão do metano −891 (tabela: −890). S + O₂ → SO₂ −297;
# 2 SO₃ → 2 SO₂ + O₂ +198 ⇒ S + 3/2 O₂ → SO₃ −396 (tabela: −395,7).

TITULO = "Lei de Hess"

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
    dict(id="s01", block="gancho", text="{a}Queimar carvão com pouco ar forma o monóxido de carbono, o cê ó. [p=0.2] Mas {b}ninguém consegue medir direto o calor dessa queima: [p=0.2] {c}junto com ele, sempre se forma um pouco de gás carbônico. [p=0.3] {d}Mesmo assim, o valor está em qualquer tabela. [p=0.2] Como?"),
    dict(id="s02", block="gancho", text="{a}Com a lei de Hess. [p=0.2] Até o fim da aula, você vai {b}somar equações, [p=0.1] {c}inverter e multiplicar cada uma [p=0.2] e {d}usar as entalpias de formação."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}delta agá é chegada menos partida, [p=0.2] {b}negativo libera calor, positivo absorve. [p=0.2] Você também vai {c}multiplicar por frações, como um meio, [p=0.1] e {d}usar a regra de sinais."),
    # a ideia
    dict(id="s04", block="ideia", text="{a}A lei de Hess diz: [p=0.1] o delta agá só depende do começo e do fim, [p=0.1] {b}não do caminho. [p=0.3] {c}Pense num prédio. [p=0.1] Do térreo ao quinto andar, {d}de escada ou de elevador, [p=0.1] {e}você sobe a mesma altura."),
    dict(id="s05", block="ideia", text="Com a reação é igual. [p=0.2] {a}Ir direto do carbono ao monóxido, [p=0.1] {b}ou passar pelo gás carbônico e voltar, [p=0.2] {c}dá o mesmo delta agá. [p=0.3] Então dá para {d}montar a reação que você quer com equações que já foram medidas."),
    # as três regras
    dict(id="s06", block="regras", text="{a}São três regras. [p=0.2] {b}Primeira: inverteu a equação, [p=0.1] troca o sinal do delta agá. [p=0.2] Faz sentido: {c}se a ida libera calor, a volta absorve a mesma quantidade."),
    dict(id="s07", block="regras", text="{a}Segunda: multiplicou a equação, [p=0.1] multiplica o delta agá pelo mesmo número. [p=0.2] {b}O dobro de reagentes troca o dobro de energia. [p=0.3] {c}Terceira: somou as equações, soma os delta agás. [p=0.2] {d}E o que aparece igual nos dois lados da seta se cancela."),
    # exemplo resolvido
    dict(id="s08", block="exemplo", text="Vamos ao monóxido. [p=0.2] {a}O alvo é cê mais meio ó dois formando cê ó. [p=0.3] {b}Primeira equação medida: cê mais ó dois forma cê ó dois, o gás carbônico, [p=0.1] delta agá de menos trezentos e noventa e quatro. [p=0.3] {c}Segunda: cê ó, o monóxido, mais meio ó dois forma gás carbônico, [p=0.1] menos duzentos e oitenta e três."),
    dict(id="s09", block="exemplo", text="{a}Olhe o cê do alvo: ele está nos reagentes, como na primeira. [p=0.2] {b}A primeira fica como está. [p=0.3] {c}O cê ó do alvo está nos produtos, [p=0.1] mas na segunda equação ele está nos reagentes. [p=0.2] {d}Então inverta a segunda, [p=0.1] e o sinal vira: {e}mais duzentos e oitenta e três."),
    dict(id="s10", block="exemplo", text="{a}Agora some. [p=0.2] {b}O cê ó dois aparece à direita na primeira e à esquerda na segunda: [p=0.1] cancela. [p=0.2] {c}Do ó dois, sobra um menos meio, que dá meio. [p=0.3] {d}Fica exatamente o alvo. [p=0.2] {e}Menos trezentos e noventa e quatro mais duzentos e oitenta e três {f}dá menos cento e onze quilojoules."),
    # entalpia de formação
    dict(id="s11", block="formacao", text="Muitas questões trazem uma tabela de {a}entalpias de formação. [p=0.2] {b}É o delta agá de formar uma substância, com coeficiente um, [p=0.1] a partir de substâncias simples, [p=0.1] {c}as feitas de um elemento só, como ó dois e agá dois. [p=0.3] {d}Por isso, a formação de uma substância simples, na sua forma comum, vale zero."),
    dict(id="s12", block="formacao", text="{a}Com a tabela, o delta agá sai numa conta só: [p=0.2] {b}as formações dos produtos menos as dos reagentes, [p=0.1] {c}cada uma vezes o seu coeficiente. [p=0.2] É o mesmo chegada menos partida."),
    dict(id="s13", block="formacao", text="{a}Na queima do metano, o gás natural, [p=0.1] cê agá quatro mais dois ó dois formam cê ó dois mais dois agá dois ó. [p=0.3] Formações: {b}metano, menos setenta e cinco. [p=0.1] {c}Gás carbônico, menos trezentos e noventa e quatro. [p=0.1] {d}Água líquida, menos duzentos e oitenta e seis. [p=0.1] {e}Ó dois, zero."),
    dict(id="s14", block="formacao", text="{a}Produtos: o gás carbônico, menos trezentos e noventa e quatro, [p=0.1] mais duas águas de menos duzentos e oitenta e seis cada, [p=0.1] {b}dá menos novecentos e sessenta e seis. [p=0.3] {c}Reagentes: menos setenta e cinco. [p=0.3] {d}Tirar menos setenta e cinco é somar setenta e cinco: [p=0.2] {e}menos novecentos e sessenta e seis mais setenta e cinco {f}dá menos oitocentos e noventa e um quilojoules."),
    # erro comum
    dict(id="s15", block="erro", text="{a}O erro mais comum: inverter a equação e esquecer de trocar o sinal. [p=0.2] {b}No monóxido, sairia menos trezentos e noventa e quatro menos duzentos e oitenta e três, [p=0.1] {c}que dá menos seiscentos e setenta e sete. [p=0.3] {d}Queimar só até o monóxido soltaria mais calor do que queimar até o gás carbônico, que solta trezentos e noventa e quatro. [p=0.2] {e}Não faz sentido."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho para montar: [p=0.2] {a}comece pelas substâncias que aparecem numa equação só. [p=0.2] {b}Está do lado errado? Inverta. [p=0.1] {c}Coeficiente diferente? Multiplique. [p=0.2] {d}Deixe o ó dois para o fim, [p=0.1] porque ele aparece em quase todas e se acerta sozinho na soma."),
    dict(id="s17", block="atalho", text="Funciona porque {a}cada substância que aparece uma vez só decide sozinha o que fazer com a sua equação. [p=0.3] {b}E, se a questão der a tabela de formação, nem monte nada: [p=0.1] {c}use a conta direta."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}O esse é o enxofre. [p=0.1] Ache o delta agá de esse mais três meios de ó dois formando esse ó três. [p=0.3] {b}Primeira equação: esse mais ó dois forma esse ó dois, [p=0.1] menos duzentos e noventa e sete. [p=0.3] {c}Segunda: dois esse ó três formam dois esse ó dois mais ó dois, [p=0.1] mais cento e noventa e oito."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="{a}O enxofre sozinho só aparece na primeira, e do lado certo: ela fica. [p=0.2] {b}O esse ó três está nos reagentes da segunda, [p=0.1] e o alvo quer um só, nos produtos. [p=0.2] {c}Inverta e divida por dois, que é multiplicar por meio: [p=0.1] {d}o mais cento e noventa e oito vira menos noventa e nove."),
    dict(id="s21", block="resposta", text="{a}Some: o esse ó dois cancela, [p=0.1] {b}e o ó dois fica um mais meio, três meios, igual ao alvo. [p=0.3] {c}Menos duzentos e noventa e sete menos noventa e nove {d}dá menos trezentos e noventa e seis quilojoules."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.1] {a}o delta agá não depende do caminho. [p=0.2] {b}Inverteu, troca o sinal. [p=0.1] {c}Multiplicou, multiplica. [p=0.1] {d}Somou, soma."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai achar o delta agá {a}pelas ligações: [p=0.2] {b}quanto se gasta para quebrar as ligações dos reagentes [p=0.1] e quanto se libera ao formar as dos produtos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
