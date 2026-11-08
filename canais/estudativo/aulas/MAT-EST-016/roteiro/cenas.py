# Estudativo · MAT-EST-016 — Desvio médio, variância e desvio padrão (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: calcular para 2, 4 e 6 que a média é 4, o desvio médio é 4/3, a variância é 8/3 e o desvio padrão é a raiz dela.
# Pré-requisitos: MAT-EST-008 (média; sobras e faltas se anulam), MAT-POT-016 (raiz de fração). Usa MAT-POT-002 (negativo ao quadrado) e MAT-POT-007 (cercar raiz não exata). Próxima: MAT-EST-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Dados criados para esta aula.
# Telas: s01/s13 turmas de média 4: notas 3 · 4 · 4 · 5 (DP ≈ 0,7) e 0 · 2 · 6 · 8 (DP ≈ 3,2) · s04 2 · 4 · 6 · s17 tempos (min) 2 · 4 · 5 · 6 · 8.

TITULO = "Desvio médio, variância e desvio padrão"

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
    dict(id="s01", block="gancho", text="{a}Duas turmas, criadas para esta aula, com a mesma média: quatro. [p=0.3] Numa, {b}as notas estão todas coladas no quatro. [p=0.2] Na outra, {c}vão de zero a oito. [p=0.3] A média {d}não enxerga essa diferença."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula três medidas que enxergam: [p=0.2] {b}desvio médio, variância e desvio padrão. [p=0.2] E leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a média, a soma dividida pela quantidade, [p=0.2] e {c}a raiz quadrada, inclusive de fração e quando ela não é exata. [p=0.3] Se faltar alguma, procure no canal."),
    # desvio
    dict(id="s04", block="desvio", text="Vamos usar só {a}três valores: dois [p=0.2] quatro [p=0.2] e seis. [p=0.3] {b}A soma dá doze. [p=0.2] {c}Doze dividido por três dá quatro. [p=0.2] A média é quatro."),
    dict(id="s05", block="desvio", text="O {a}desvio de um valor é quanto ele se afasta da média: [p=0.2] o valor menos a média. [p=0.3] {b}Dois menos quatro dá menos dois. [p=0.2] {c}Quatro menos quatro dá zero. [p=0.2] {d}Seis menos quatro dá dois."),
    dict(id="s06", block="desvio", text="A ideia natural seria fazer a média dos desvios. [p=0.2] Mas some: {a}menos dois mais zero mais dois dá zero. [p=0.3] E {b}sempre vai dar zero. [p=0.2] Lembra da aula de média? [p=0.2] {c}O que sobra num valor cobre o que falta em outro. [p=0.3] Para medir o espalhamento, {d}o sinal precisa sumir. [p=0.2] Existem dois jeitos."),
    # desvio médio
    dict(id="s07", block="medio", text="{a}Primeiro jeito: esquecer o sinal. [p=0.2] Use só {b}a distância até a média, que é sempre positiva. [p=0.3] As distâncias são {c}dois [p=0.2] zero [p=0.2] e dois."),
    dict(id="s08", block="medio", text="O {a}desvio médio é a média dessas distâncias. [p=0.2] {b}Dois mais zero mais dois dá quatro. [p=0.2] {c}Quatro dividido por três dá quatro terços, [p=0.2] cerca de um vírgula três. [p=0.3] Em média, {d}cada valor fica a quatro terços da média."),
    # variância
    dict(id="s09", block="variancia", text="{a}Segundo jeito: elevar cada desvio ao quadrado. [p=0.2] Negativo ao quadrado {b}vira positivo. [p=0.3] {c}Menos dois ao quadrado dá quatro. [p=0.2] {d}Zero ao quadrado dá zero. [p=0.2] {e}Dois ao quadrado dá quatro."),
    dict(id="s10", block="variancia", text="A {a}variância é a média desses quadrados. [p=0.2] {b}Quatro mais zero mais quatro dá oito. [p=0.2] {c}Oito dividido por três dá oito terços. [p=0.3] Na tela, a receita: [p=0.2] {d}cada valor menos a média, ao quadrado, [p=0.2] {e}somados [p=0.2] e {f}divididos pela quantidade de valores. [p=0.3] Alguns livros, quando os dados são só uma parte de um grupo maior, {g}dividem pela quantidade menos um. [p=0.2] Se a questão quiser essa versão, ela vai dizer. [p=0.2] Sem esse aviso, divida pela quantidade."),
    # desvio padrão
    dict(id="s11", block="padrao", text="A variância tem um defeito: [p=0.2] {a}ela muda a unidade. [p=0.2] Se os dados estão em metros, [p=0.2] {b}os quadrados ficam em metros quadrados. [p=0.3] Para voltar à unidade dos dados, {c}tire a raiz quadrada. [p=0.2] Esse é o {d}desvio padrão: a raiz da variância."),
    dict(id="s12", block="padrao", text="Aqui, {a}raiz de oito terços. [p=0.2] Não é exata, então cerque. [p=0.2] {b}Oito dividido por três dá cerca de dois vírgula sessenta e sete. [p=0.3] {c}Um vírgula seis ao quadrado dá dois vírgula cinquenta e seis. [p=0.2] {d}Um vírgula sete ao quadrado dá dois vírgula oitenta e nove. [p=0.3] Fica mais perto do primeiro: [p=0.2] {e}o desvio padrão é cerca de um vírgula seis."),
    dict(id="s13", block="padrao", text="E as turmas do começo? [p=0.2] Na turma colada no quatro, {a}o desvio padrão é pequeno. [p=0.2] Na turma de zero a oito, {b}é grande. [p=0.3] {c}Quanto maior o desvio padrão, mais espalhados os dados. [p=0.2] E se todos os valores forem iguais, {d}ele dá zero."),
    # erro
    dict(id="s14", block="erro", text="Agora, cuidado com um erro muito comum: [p=0.2] {a}escrever menos dois ao quadrado como menos quatro. [p=0.3] Aí a soma vira {b}menos quatro mais zero mais quatro, que dá zero. [p=0.2] E a pessoa conclui que {c}a variância é zero. [p=0.3] Impossível: {d}os valores são diferentes. [p=0.2] Menos dois vezes menos dois {e}dá quatro positivo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho de prova. [p=0.2] Um professor {a}soma um ponto na nota de todo mundo. [p=0.2] O que acontece com o desvio padrão? [p=0.3] {b}Nada. [p=0.2] Dois [p=0.2] quatro e seis viram {c}três [p=0.2] cinco e sete. [p=0.2] A média também sobe um, [p=0.2] e {d}os desvios continuam menos dois [p=0.2] zero e dois."),
    dict(id="s16", block="atalho", text="E se ele {a}dobrar todas as notas? [p=0.2] Cada desvio dobra, [p=0.2] então {b}o desvio padrão também dobra. [p=0.2] Mas {c}a variância fica quatro vezes maior, [p=0.2] porque o dobro de um desvio, ao quadrado, dá quatro vezes o quadrado dele. [p=0.3] Funciona porque {d}a dispersão só depende da distância até a média. [p=0.2] Não compensa quando {e}só alguns valores mudam: [p=0.2] aí, {f}refaça a conta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Os tempos de espera de cinco clientes, em minutos, estão na tela. [p=0.3] Calcule {b}a média, [p=0.2] {c}o desvio médio, [p=0.2] {d}a variância [p=0.2] e {e}o desvio padrão."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}A soma dá vinte e cinco. [p=0.2] {b}Vinte e cinco dividido por cinco dá cinco minutos de média. [p=0.3] {c}Os desvios são menos três [p=0.2] menos um [p=0.2] zero [p=0.2] um e três. [p=0.3] {d}As distâncias somam oito. [p=0.2] {e}Oito dividido por cinco dá um vírgula seis minuto de desvio médio."),
    dict(id="s20", block="resposta", text="Os quadrados: {a}nove [p=0.2] um [p=0.2] zero [p=0.2] um e nove. [p=0.2] {b}A soma dá vinte. [p=0.2] {c}Vinte dividido por cinco dá quatro: essa é a variância. [p=0.3] E {d}a raiz quadrada de quatro dá dois: [p=0.2] {e}o desvio padrão é de dois minutos."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.2] {a}desvio médio é a média das distâncias, [p=0.2] {b}variância é a média dos quadrados dos desvios [p=0.2] e {c}desvio padrão é a raiz da variância."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai {a}interpretar esses números: [p=0.2] {b}qual atleta é mais regular [p=0.2] e o que fazer quando as médias são diferentes, com o {c}coeficiente de variação. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
