# Estudativo · MAT-EST-021 — Praticando: análise crítica de dados (Matemática · Estatística · Análise crítica de gráficos · prática).
# Habilidade: dizer se uma conclusão se sustenta nos dados de um gráfico ou de uma pesquisa.
# Pré-requisitos: MAT-EST-019 (três olhares: eixo, escala, figura), MAT-EST-020 (três perguntas: quem foi ouvido, por cento de quanto, o que mais mudou junto). Usa MAT-EST-001 (amostra proporcional), MAT-EST-004 (setores somam 100%), MAT-POR-005 e MAT-POR-012.
# Fecha a trilha Estatística. Próxima na playlist Matemática do Zero: MAT-CNT-001.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Telas: s03 colunas aluguel médio bairro A R$ 1.000 e bairro B R$ 1.050, eixo começando em R$ 980 · s07 pizza: app X 60%, Y 45%, Z 30%
#        s11 pesquisa: 500 de 2.000 alunos sorteados, proporcional por turno, 60% a favor · s14 desemprego 10% → 12% · s17 incêndios: bombeiros × prejuízo.

TITULO = "Praticando: análise crítica de gráficos e pesquisas"

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
    dict(id="s01", block="gancho", text="{a}Cinco conclusões, criadas para esta aula. [p=0.2] Em cada uma, a pergunta é a mesma: [p=0.2] {b}ela se sustenta nos dados? [p=0.3] {c}Pause o vídeo e decida antes de ver a resposta. [p=0.2] E atenção: {d}nem toda conclusão está errada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}os três olhares do gráfico: [p=0.2] eixo no zero, escala com passo igual e figura proporcional. [p=0.3] E {b}as três perguntas da pesquisa: [p=0.2] quem foi ouvido, por cento de quanto [p=0.2] e o que mais mudou junto. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: eixo cortado
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Um gráfico de colunas mostra o aluguel médio em dois bairros. [p=0.2] {c}O eixo do lado começa em novecentos e oitenta reais. [p=0.2] As colunas marcam {d}mil [p=0.2] e mil e cinquenta reais. [p=0.3] Conclusão: {e}o aluguel no bairro bê é mais de três vezes o do bairro á."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Não se sustenta. [p=0.2] O eixo começa em novecentos e oitenta, então as colunas mostram só {b}mil menos novecentos e oitenta, que dá vinte, [p=0.2] e mil e cinquenta menos novecentos e oitenta, que dá setenta. [p=0.2] {c}Setenta dividido por vinte dá três vírgula cinco: [p=0.2] daí a impressão."),
    dict(id="s06", block="resposta1", text="Com os valores: [p=0.2] {a}mil e cinquenta menos mil dá cinquenta. [p=0.2] {b}Cinquenta dividido por mil dá zero vírgula zero cinco. [p=0.2] O aluguel em bê é {c}só cinco por cento maior."),
    # situação 2: pizza acima de 100%
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma pesquisa perguntou {b}quais aplicativos de transporte a pessoa usa. [p=0.3] {c}O resultado virou um gráfico de pizza, com as porcentagens na tela. [p=0.3] Conclusão: {d}o gráfico mostra bem como os usuários se dividem entre os aplicativos."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] {a}Não se sustenta. [p=0.2] Some as fatias: [p=0.2] {b}sessenta mais quarenta e cinco mais trinta dá cento e trinta e cinco por cento. [p=0.3] Mas a pizza inteira é {c}cem por cento. [p=0.2] A pergunta aceitava {d}mais de uma resposta: [p=0.2] quem usa dois aplicativos foi contado duas vezes. [p=0.2] Aqui, {e}o certo seria um gráfico de colunas."),
    dict(id="s10", block="atalho", text="Fica o atalho: {a}some as fatias antes de ler qualquer pizza. [p=0.3] Funciona porque {b}cada pessoa só pode estar em uma fatia. [p=0.2] Passou de cem, alguém foi contado duas vezes. [p=0.3] Não compensa {c}brigar por um ponto a mais ou a menos: [p=0.2] noventa e nove ou cento e um {d}costumam ser só arredondamento."),
    # situação 3: amostra boa
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Uma escola tem {b}dois mil alunos. [p=0.2] Ela sorteou {c}quinhentos, em amostra proporcional ao turno, [p=0.2] e perguntou se querem aula de reforço aos sábados. [p=0.3] {d}Sessenta por cento disseram sim. [p=0.2] Conclusão: {e}a maioria dos alunos da escola quer o reforço."),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Quem foi ouvido? [p=0.2] {a}Alunos sorteados entre todos, [p=0.2] com cada turno no seu peso. [p=0.2] É a panela mexida. [p=0.2] A amostra não precisa ser a escola inteira: [p=0.2] precisa parecer com ela. [p=0.3] {b}Quinhentos dividido por dois mil dá zero vírgula vinte e cinco: [p=0.2] um quarto da escola. [p=0.3] E sessenta por cento {c}passa bem da metade. [p=0.2] {d}Essa conclusão se sustenta."),
    # situação 4: ponto percentual
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] A taxa de desemprego de uma cidade passou de {b}dez por cento [p=0.2] para {c}doze por cento. [p=0.3] Manchete: {d}desemprego sobe dois por cento."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Não se sustenta como está escrita. [p=0.2] {b}Doze menos dez dá dois pontos percentuais. [p=0.3] Em variação percentual, {c}dois dividido por dez dá zero vírgula dois: [p=0.2] {d}vinte por cento. [p=0.3] A manchete certa seria: [p=0.2] {e}subiu dois pontos percentuais, ou vinte por cento. [p=0.2] Aqui, o erro deixou a notícia {f}menos grave do que é."),
    # situação 5: correlação
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] {b}Um levantamento de incêndios mostra: [p=0.2] quanto mais bombeiros foram chamados, [p=0.2] {c}maior foi o prejuízo. [p=0.3] Conclusão: {d}mandar mais bombeiros aumenta o prejuízo."),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] {a}Não se sustenta. [p=0.2] O que mais mudou junto? [p=0.2] {b}O tamanho do incêndio. [p=0.3] Incêndio grande {c}chama mais bombeiros [p=0.2] e {d}causa mais prejuízo. [p=0.3] É o terceiro fator. [p=0.2] Mandar menos bombeiros só deixaria o fogo crescer. [p=0.2] Os dados mostram {e}correlação, não causa."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.2] {a}olhe o eixo, a escala e a figura; [p=0.2] {b}some a pizza; [p=0.2] {c}pergunte quem foi ouvido, por cento de quanto e o que mais mudou junto. [p=0.3] Se tudo passar, {d}a conclusão pode ficar de pé."),
    dict(id="s21", block="fim", text="Com isso, {a}você fecha a trilha de estatística. [p=0.2] Na próxima aula, começa a {b}contagem: [p=0.2] {c}com três camisas e quatro calças, quantas roupas diferentes você monta? [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
