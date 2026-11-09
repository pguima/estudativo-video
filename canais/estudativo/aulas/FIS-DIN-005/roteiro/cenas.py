# Estudativo · FIS-DIN-005 — Tração e força elástica (Física · Dinâmica · Leis de Newton).
# Habilidade: desenhar o diagrama de forças com fios e molas e usar a lei de Hooke F = k·x no dinamômetro.
# Pré-requisitos: FIS-DIN-004 (peso e normal). Próxima: FIS-DIN-006.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². Fio ideal: sem massa e sem esticar (a mesma tração nas duas pontas). Conversão cm → m: MAT-MED-001.

TITULO = "Tração e força elástica"

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
    dict(id="s01", block="gancho", text="{a}Na feira, o peixe é pesado numa balança de gancho. [p=0.2] {b}Dentro dela, só existe uma mola. [p=0.3] {c}Como uma mola consegue medir força?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}desenhar as forças de fios e molas [p=0.2] e usar a {c}lei de Hooke [p=0.1] para entender essa balança."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o peso, pê igual a eme vezes gê, com gê igual a dez; [p=0.2] e {c}corpo parado tem resultante zero. [p=0.3] Se faltar alguma, procure no canal."),
    # tração
    dict(id="s04", block="tracao", text="{a}Um fio esticado puxa o que está preso nele. [p=0.2] Essa força se chama {b}tração, letra tê. [p=0.3] {c}Fio só puxa, nunca empurra: [p=0.2] {d}a tração sai do corpo e vai ao longo do fio."),
    dict(id="s05", block="tracao", text="Nas questões, o fio é {a}ideal: [p=0.2] não tem massa e não estica. [p=0.2] Assim, {b}a tração é a mesma do começo ao fim do fio. [p=0.3] {c}Um lustre de dois quilogramas pendurado e parado: [p=0.2] peso de vinte newtons para baixo, [p=0.2] {d}tração de vinte newtons para cima."),
    # diagrama
    dict(id="s06", block="diagrama", text="Para não esquecer nenhuma força, use o {a}diagrama de corpo livre. [p=0.3] {b}Um: desenhe o corpo sozinho, separado do resto. [p=0.2] {c}Dois: o peso, sempre, para baixo. [p=0.2] {d}Três: uma força para cada coisa que toca o corpo: [p=0.2] fio, chão ou mola."),
    dict(id="s07", block="diagrama", text="{a}Um vaso de três quilogramas pendurado por dois fios, um em cada lado, [p=0.2] retos para cima. [p=0.3] {b}Peso de trinta newtons. [p=0.2] {c}Duas trações para cima. [p=0.2] Se os fios são iguais, {d}cada um puxa quinze newtons."),
    dict(id="s08", block="diagrama", text="{a}Uma caixa num chão liso, sem atrito, puxada por um fio na horizontal. [p=0.2] {b}O peso, para baixo. [p=0.2] Duas coisas tocam a caixa: [p=0.1] {c}o chão, que faz a normal para cima, [p=0.2] e {d}o fio, que faz a tração para o lado dele. [p=0.3] {e}Três forças, nem mais, nem menos."),
    # força elástica
    dict(id="s09", block="hooke", text="Agora, a mola. [p=0.2] {a}Estique uma mola, e ela puxa de volta. [p=0.2] {b}Aperte, e ela empurra de volta. [p=0.3] Essa é a {c}força elástica: [p=0.2] ela sempre {d}tenta devolver a mola ao tamanho natural."),
    dict(id="s10", block="hooke", text="A lei de Hooke diz quanto: [p=0.2] {a}efe é igual a cá vezes xis. [p=0.3] {b}Xis é a deformação: quanto a mola esticou ou encolheu, em metros. [p=0.2] {c}Cá é a constante elástica, em newtons por metro: [p=0.2] {d}mola dura tem cá grande."),
    dict(id="s11", block="hooke", text="{a}Uma mola de cá igual a duzentos newtons por metro, esticada {b}dez centímetros. [p=0.3] Primeiro, para metros: {c}dez centímetros são zero vírgula um metro. [p=0.2] {d}Duzentos vezes zero vírgula um: [p=0.1] {e}vinte newtons."),
    # dinamômetro
    dict(id="s12", block="dinamometro", text="A balança de gancho é um {a}dinamômetro. [p=0.2] {b}Pendure um peixe de três quilogramas: [p=0.2] {c}a mola estica até a força dela igualar o peso, trinta newtons. [p=0.3] {d}Se cá vale quinhentos newtons por metro, [p=0.1] {e}xis é trinta dividido por quinhentos: [p=0.2] {f}zero vírgula zero seis metro, seis centímetros. [p=0.3] {g}A escala marca a força pelo quanto a mola esticou."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar o tamanho da mola no lugar da deformação. [p=0.3] {b}Uma mola de vinte centímetros passa a vinte e cinco. [p=0.2] {c}Xis não é vinte e cinco: [p=0.2] {d}é vinte e cinco menos vinte, cinco centímetros, [p=0.2] {e}zero vírgula zero cinco metro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}na mesma mola, força e deformação são diretamente proporcionais. [p=0.3] {b}Se dois quilogramas esticam quatro centímetros, [p=0.2] {c}cinco quilogramas esticam dez, [p=0.2] {d}sem calcular o cá."),
    dict(id="s15", block="atalho", text="Funciona porque {a}efe igual a cá vezes xis é uma proporção direta. [p=0.3] {b}Não compensa quando a questão pede o próprio cá, [p=0.2] ou {c}troca de mola no meio do caminho: [p=0.2] aí, calcule."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma mola tem trinta centímetros. [p=0.2] {b}Pendurado um bloco de quatro quilogramas, [p=0.2] ela passa a {c}trinta e oito centímetros. [p=0.3] {d}Qual é a constante elástica da mola?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Parado: {a}força da mola igual ao peso, quarenta newtons. [p=0.3] Deformação: {b}trinta e oito menos trinta, oito centímetros, [p=0.2] {c}zero vírgula zero oito metro. [p=0.3] {d}Cá é efe dividido por xis: [p=0.1] {e}quarenta dividido por zero vírgula zero oito. [p=0.2] {f}Quinhentos newtons por metro."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}fio só puxa, com a mesma tração em todo o fio; [p=0.2] {b}no diagrama, o peso e uma força para cada contato; [p=0.2] e {c}na mola, efe é cá vezes xis, com xis em metros."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar as três leis de Newton [p=0.2] em {b}questões do trânsito e do dia a dia. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
