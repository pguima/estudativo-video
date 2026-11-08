# Estudativo · MAT-EST-002 — Tabela de frequência e classes (Matemática · Estatística · Dados, tabelas e gráficos).
# Habilidade: montar uma tabela com frequência absoluta, relativa e acumulada e agrupar idades em classes de 10 em 10 anos.
# Pré-requisitos: MAT-EST-001 (variável qualitativa e quantitativa). Usa MAT-POR-003 (parte dividida pelo total; atalho "faça o total virar cem"). Próxima: MAT-EST-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Listas de idades só na tela (vírgula entre números funde a leitura da voz).
# Dados (tela): transporte de 20 pessoas: ônibus 8, carro 5, bicicleta 4, a pé 3 → 40%, 25%, 20%, 15% (soma 100%).
#   Idades de 20 pessoas: 18, 23, 25, 31, 34, 19, 42, 27, 36, 30, 22, 45, 29, 38, 51, 26, 33, 40, 24, 37.
#   Classes 10 ⊢ 20: 2 · 20 ⊢ 30: 7 · 30 ⊢ 40: 7 · 40 ⊢ 50: 3 · 50 ⊢ 60: 1. Acumulada 2, 9, 16, 19, 20. Relativa 10%, 35%, 35%, 15%, 5%.
#   Erro: o 30 na classe 20 ⊢ 30 → 8 e 6.
#   Questão: 17, 22, 35, 28, 40, 19, 31, 20, 26, 45 → 2, 4, 2, 2; acumulada 2, 6, 8, 10; menos de 30: 6 de 10 = 60%.
# Visual:
#   s01: lista solta de 20 respostas virando tabela (E.tabela).
#   s04-s06: E.tabela transporte com colunas absoluta e relativa entrando no tempo da fala.
#   s07-s11: lista das 20 idades; E.tabela de classes com "20 ⊢ 30" e as colunas absoluta e acumulada.
#   s12: o 30 indo para a classe errada (vermelho) e depois para 30 ⊢ 40 (verde).
#   s15-s18: lista das 10 idades na tela; tabela da resposta.

TITULO = "Tabela de frequência e classes"

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
    dict(id="s01", block="gancho", text="{a}Vinte pessoas responderam como vão ao trabalho. [p=0.2] Numa lista solta, {b}ninguém entende nada. [p=0.3] Numa tabela, {c}você lê tudo de uma olhada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta uma tabela de frequência, [p=0.2] agrupa idades de dez em dez anos [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}o que é uma variável, qualitativa ou quantitativa, [p=0.2] e {c}quantos por cento uma parte é do total. [p=0.3] Se faltar alguma, procure no canal."),
    # absoluta e relativa
    dict(id="s04", block="absoluta", text="Na lista, aparecem {a}ônibus, carro, bicicleta e a pé, misturados. [p=0.2] Conte quantas vezes cada um aparece: [p=0.2] {b}ônibus, oito vezes; [p=0.2] carro, cinco; [p=0.2] bicicleta, quatro; [p=0.2] a pé, três. [p=0.3] Essa contagem é a {c}frequência absoluta. [p=0.2] {d}A soma tem que dar o total: vinte."),
    dict(id="s05", block="relativa", text="A {a}frequência relativa diz quanto cada resposta é do total, em porcentagem. [p=0.2] É {b}a absoluta dividida pelo total. [p=0.3] {c}Ônibus: oito dividido por vinte dá zero vírgula quatro, [p=0.2] que são quarenta por cento."),
    dict(id="s06", block="relativa", text="Do mesmo jeito, {a}cinco de vinte dá vinte e cinco por cento para o carro. [p=0.2] {b}Quatro de vinte dá vinte por cento para a bicicleta. [p=0.2] {c}Três de vinte dá quinze por cento para quem vai a pé. [p=0.3] {d}A soma da relativa dá cem por cento."),
    # classes
    dict(id="s07", block="classes", text="E quando a resposta é {a}idade? [p=0.2] Com vinte pessoas, podem sair {b}quase vinte idades diferentes. [p=0.2] Uma linha para cada idade não resume nada. [p=0.3] A saída é {c}agrupar em classes: faixas de dez em dez anos."),
    dict(id="s08", block="classes", text="As classes são {a}de dez a vinte anos, de vinte a trinta, de trinta a quarenta, e assim por diante. [p=0.3] Na tela, {b}o sinal entre os números quer dizer: o primeiro entra, o último não. [p=0.2] {c}A classe de vinte a trinta vai de vinte até vinte e nove anos."),
    dict(id="s09", block="classes", text="Contando as vinte idades: [p=0.2] {a}duas pessoas na classe de dez a vinte. [p=0.2] {b}Sete na de vinte a trinta. [p=0.2] {c}Sete na de trinta a quarenta. [p=0.2] {d}Três na de quarenta a cinquenta. [p=0.2] {e}E uma na de cinquenta a sessenta."),
    # acumulada
    dict(id="s10", block="acumulada", text="Falta a {a}frequência acumulada: [p=0.2] quantos estão {b}até aquela classe, somando de cima para baixo. [p=0.3] {c}Começa em duas. [p=0.2] {d}Duas mais sete dá nove. [p=0.2] {e}Nove mais sete dá dezesseis. [p=0.2] Dezesseis mais três dá dezenove, [p=0.2] e {f}dezenove mais uma dá vinte, o total."),
    dict(id="s11", block="acumulada", text="Ela responde rápido {a}quantos têm menos de quarenta anos: [p=0.2] {b}dezesseis, direto da tabela. [p=0.3] {c}A última acumulada sempre dá o total. [p=0.2] Se não der, {d}faltou contar alguém."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum está {a}na borda das classes. [p=0.2] Na lista, tem {b}alguém de trinta anos, [p=0.2] e a pessoa põe na classe de vinte a trinta. [p=0.3] A tabela sai com {c}oito numa classe e seis na outra, no lugar de sete e sete. [p=0.3] Mas o trinta {d}fica fora da classe de vinte a trinta. [p=0.2] {e}Trinta anos entra na classe de trinta a quarenta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho da relativa, que você já viu na porcentagem: {a}faça o total virar cem. [p=0.2] Total vinte? {b}Multiplique por cinco. [p=0.3] {c}Sete pessoas viram trinta e cinco em cada cem: trinta e cinco por cento. [p=0.2] {d}Duas viram dez por cento."),
    dict(id="s14", block="atalho", text="Funciona porque a fração equivalente {a}não muda o valor. [p=0.2] Com cem embaixo, {b}o de cima já é a porcentagem. [p=0.3] {c}Não compensa com um total como trinta e sete. [p=0.2] Aí, {d}divida a absoluta pelo total."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}As idades de dez alunos de um curso estão na tela. [p=0.3] {b}Monte a tabela em classes de dez em dez anos, [p=0.2] com a frequência absoluta e a acumulada. [p=0.2] E diga {c}quantos por cento têm menos de trinta anos."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Duas pessoas na classe de dez a vinte. [p=0.2] {b}Quatro na de vinte a trinta, contando o aluno de vinte anos. [p=0.2] {c}Duas na de trinta a quarenta. [p=0.2] {d}E duas na de quarenta a cinquenta, porque o aluno de quarenta anos entra nela."),
    dict(id="s18", block="resposta", text="Acumulada: {a}começa em duas. [p=0.2] Duas mais quatro dá seis. [p=0.2] Seis mais duas dá oito. [p=0.2] {b}Oito mais duas dá dez, o total. [p=0.3] Menos de trinta anos é a acumulada até a classe de vinte a trinta: {c}seis. [p=0.2] Total dez? {d}Multiplique por dez: seis vezes dez dá sessenta por cento."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a absoluta conta, [p=0.2] {b}a relativa divide pelo total, [p=0.2] {c}a acumulada vai somando. [p=0.2] E na classe, {d}o primeiro número entra e o último não."),
    dict(id="s20", block="fim", text="Na próxima aula, essas tabelas viram {a}gráficos de barras e de linhas. [p=0.2] Você vai ler cada um, achar {b}o período de maior alta [p=0.2] e calcular {c}a variação em porcentagem. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
