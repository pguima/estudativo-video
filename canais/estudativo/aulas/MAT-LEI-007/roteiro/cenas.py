# Estudativo · MAT-LEI-007 — Praticando: da leitura à decisão (Matemática · Leitura de Problemas · prática).
# Habilidade: ler enunciados longos, estimar o resultado e escolher a melhor opção.
# Pré-requisitos: MAT-LEI-001, MAT-LEI-002, MAT-LEI-003, MAT-LEI-004, MAT-LEI-005, MAT-LEI-006. Próxima: MAT-CON-001 (fim da trilha).
# Questões inéditas, criadas para esta aula. Preços e tarifas inventados.

TITULO = "Praticando: da leitura à decisão"

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
    dict(id="s01", block="gancho", text="{a}Cinco problemas de enunciado comprido, [p=0.2] criados para esta aula. [p=0.3] Em cada um, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] É assim que a leitura vira hábito."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as ferramentas da trilha: [p=0.2] {a}pergunta primeiro, [p=0.2] {b}palavras que mudam a conta, [p=0.2] {c}barras e tabelas, [p=0.2] {d}estimativa, [p=0.2] {e}faixas [p=0.2] e {f}comparar opções. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: dados úteis e no mínimo
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma festa terá {b}cento e trinta convidados. [p=0.2] O salão abre às {c}sete da noite. [p=0.2] Cada mesa tem {d}oito lugares, [p=0.1] e o aluguel de uma mesa custa {e}vinte e cinco reais. [p=0.3] {f}No mínimo, quantas mesas precisam ser alugadas?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] A pergunta pede {a}mesas. [p=0.2] Úteis: {b}cento e trinta convidados e oito lugares. [p=0.2] {c}O horário e o aluguel: risque. [p=0.3] Pela tabuada, {d}dezesseis mesas dão cento e vinte e oito lugares: [p=0.2] dois convidados ficam em pé. [p=0.2] {e}Dezessete mesas dão cento e trinta e seis. [p=0.3] Resposta: {f}dezessete mesas. [p=0.3] Repare: {g}cento e trinta dividido por oito dá dezesseis vírgula vinte e cinco, [p=0.2] e a regra do cinco mandaria descer. [p=0.2] Mas a pergunta diz {h}no mínimo, e ninguém fica sem lugar: sobe."),
    # situação 2: do restante com barra
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Uma pessoa leu {b}um terço de um livro no primeiro dia [p=0.1] e {c}um quarto do restante no segundo. [p=0.3] Ainda faltam {d}cento e oitenta páginas. [p=0.3] {e}Quantas páginas tem o livro?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá, com uma barra de {a}doze quadradinhos, [p=0.2] porque doze dá para dividir por três e depois por quatro. [p=0.3] Primeiro dia: {b}um terço, quatro quadradinhos. [p=0.2] Restam oito. [p=0.2] Segundo dia: {c}um quarto de oito, dois quadradinhos."),
    dict(id="s09", block="resposta2", text="Faltam {a}seis quadradinhos, que valem cento e oitenta páginas. [p=0.3] {b}Cento e oitenta dividido por seis dá trinta páginas cada. [p=0.2] O livro tem {c}doze vezes trinta: trezentas e sessenta páginas. [p=0.3] Repare: {d}faltam seis de doze, metade do livro. [p=0.2] Cento e oitenta é metade de trezentos e sessenta. [p=0.2] Bateu."),
    # situação 3: estimativa
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma loja vendeu {b}cinquenta e dois kits por dia, [p=0.1] a {c}dezenove reais cada, [p=0.1] durante {d}trinta dias. [p=0.3] O valor recebido foi de aproximadamente: [p=0.2] {e}três mil, [p=0.2] {f}trinta mil [p=0.2] ou {g}trezentos mil reais?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] A pergunta diz {a}aproximadamente, e as opções estão longe uma da outra. [p=0.2] Estimativa basta. [p=0.3] {b}Cinquenta e dois desce para cinquenta. [p=0.2] {c}Dezenove sobe para vinte. [p=0.3] {d}Cinquenta vezes vinte dá mil por dia. [p=0.2] {e}Vezes trinta dias, trinta mil reais. [p=0.3] A conta exata dá {f}vinte e nove mil seiscentos e quarenta: [p=0.2] perto. [p=0.3] Quem perde um zero no caminho marca {g}três mil, [p=0.2] dez vezes menos."),
    # situação 4: faixas
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Um estacionamento cobra {b}seis reais por hora nas duas primeiras horas [p=0.2] e {c}quatro reais por hora depois disso. [p=0.3] {d}Quanto paga quem fica cinco horas?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] Corte o tempo nas faixas: {a}duas horas na primeira, [p=0.2] {b}três horas na segunda. [p=0.3] {c}Duas vezes seis dá doze. [p=0.2] {d}Três vezes quatro dá doze. [p=0.2] Total: {e}vinte e quatro reais. [p=0.3] Quem cobrou tudo a seis reais pagou {f}trinta: [p=0.2] o preço da primeira faixa só vale para as duas primeiras horas."),
    # situação 5: melhor opção com tabela
    dict(id="s16", block="questao5", text="{a}Última situação. [p=0.2] Um táxi cobra {b}cinco reais fixos para começar a corrida, [p=0.1] mais {c}três reais por quilômetro. [p=0.2] Um aplicativo cobra {d}quatro reais por quilômetro, sem valor fixo. [p=0.3] {e}Para uma corrida de oito quilômetros, qual sai mais barato?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] Táxi: {a}cinco mais três vezes oito, vinte e nove reais. [p=0.2] Aplicativo: {b}quatro vezes oito dá trinta e dois reais. [p=0.3] Para oito quilômetros, {c}o táxi ganha por três reais."),
    dict(id="s19", block="resposta5", text="E dá para decidir qualquer corrida com uma tabela. [p=0.2] A cada quilômetro, o aplicativo fica {a}um real mais caro que o táxi. [p=0.3] Os cinco reais fixos se pagam em {b}cinco quilômetros: [p=0.2] aí os preços empatam, {c}vinte reais cada. [p=0.3] {d}Abaixo de cinco quilômetros, aplicativo. [p=0.2] {e}Acima, táxi."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}pergunta primeiro, [p=0.2] {b}desenhe ou monte a tabela, [p=0.2] {c}estime antes de calcular [p=0.2] e {d}confira se a resposta faz sentido."),
    dict(id="s21", block="fim", text="Com isso, você fecha a trilha de leitura de problemas. [p=0.3] A próxima aula abre os {a}conjuntos: [p=0.2] escrever um grupo entre chaves e saber {b}o que pertence a ele. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
