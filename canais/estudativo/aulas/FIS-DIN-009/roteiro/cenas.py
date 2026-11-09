# Estudativo · FIS-DIN-009 — Blocos ligados e polias (Física · Dinâmica · Atrito, plano inclinado e sistemas).
# Habilidade: achar a aceleração de blocos ligados com o atalho de tratar tudo como um corpo só e depois calcular a tração.
# Pré-requisitos: FIS-DIN-007 (atrito), FIS-DIN-005 (tração). Próxima: FIS-DIN-010.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². Fio e polia ideais. Plano inclinado (FIS-DIN-008) não está em "Já ensinado": só mesa horizontal e blocos
# pendurados. Atrito na mesa usa o cinético (o sistema já está andando).

TITULO = "Blocos ligados e polias"

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
    dict(id="s01", block="gancho", text="{a}Um bloco em cima da mesa, [p=0.1] {b}um fio, uma roldana [p=0.1] e {c}outro bloco pendurado. [p=0.3] Parece um problema de três equações. [p=0.2] {d}Com o atalho certo, a aceleração sai numa linha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar {b}a aceleração de blocos ligados [p=0.2] tratando tudo como {c}um corpo só, [p=0.2] e depois {d}a tração no fio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a tração, que é a mesma em todo o fio ideal; [p=0.2] {c}o atrito cinético, mi vezes ene; [p=0.2] e {d}força resultante igual a massa vezes aceleração. [p=0.3] Se faltar alguma, procure no canal."),
    # um corpo só
    dict(id="s04", block="junto", text="{a}Dois blocos numa mesa lisa, sem atrito, ligados por um fio: [p=0.2] {b}o de trás tem dois quilogramas, [p=0.1] e {c}o da frente, três. [p=0.3] {d}Uma força de vinte newtons puxa o da frente. [p=0.3] {e}O fio esticado obriga os dois a andar juntos, com a mesma aceleração."),
    dict(id="s05", block="junto", text="Então, {a}olhe os dois como um corpo só, de cinco quilogramas. [p=0.3] {b}A tração do fio some dessa conta: [p=0.2] ela puxa o de trás para a frente e o da frente para trás, [p=0.2] e {c}as duas se cancelam dentro do conjunto. [p=0.3] {d}Á é vinte dividido por cinco: [p=0.1] {e}quatro metros por segundo ao quadrado."),
    dict(id="s06", block="junto", text="Agora, a tração. [p=0.2] {a}Escolha o bloco mais simples: o de trás, que só tem o fio puxando. [p=0.3] {b}Tê é igual a dois vezes quatro: [p=0.1] {c}oito newtons. [p=0.3] {d}Confira no da frente: vinte menos oito, doze, [p=0.2] e {e}doze dividido por três dá quatro. [p=0.2] Bateu."),
    # polia
    dict(id="s07", block="polia", text="{a}Agora, com polia. [p=0.2] {b}Um bloco de seis quilogramas na mesa lisa. [p=0.2] {c}Outro, de quatro, pendurado. [p=0.3] {d}A polia ideal só muda a direção do fio, [p=0.2] e {e}os dois continuam com a mesma aceleração."),
    dict(id="s08", block="polia", text="{a}Quem puxa o conjunto é o peso do bloco pendurado: quarenta newtons. [p=0.3] {b}O peso do bloco da mesa é segurado pela normal e não entra. [p=0.3] {c}Á é quarenta dividido por dez quilogramas: [p=0.1] {d}quatro metros por segundo ao quadrado. [p=0.3] {e}Tração, pelo bloco da mesa: seis vezes quatro, {f}vinte e quatro newtons."),
    # com atrito
    dict(id="s09", block="atrito", text="{a}E se a mesa tem atrito, com mi cinético de zero vírgula cinco, e o sistema já está andando? [p=0.3] {b}A normal do bloco da mesa é sessenta, [p=0.1] e o atrito é {c}trinta newtons contra o movimento. [p=0.3] {d}Força a favor menos força contra: [p=0.1] {e}quarenta menos trinta, dez. [p=0.2] {f}Dez dividido por dez: um metro por segundo ao quadrado."),
    dict(id="s10", block="atrito", text="{a}Tração, de novo pelo bloco da mesa: [p=0.2] o fio vence o atrito e ainda acelera o bloco. [p=0.2] {b}Tê menos trinta é igual a seis vezes um: [p=0.1] {c}tê vale trinta e seis newtons."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a tração é o peso do bloco pendurado. [p=0.3] {b}Sem atrito, o peso do bloco pendurado é quarenta, [p=0.1] mas {c}a tração é vinte e quatro. [p=0.3] {d}Se a tração fosse quarenta, a resultante no bloco pendurado seria zero, [p=0.2] e {e}ele não desceria acelerando."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho, numa linha: [p=0.2] {a}á é igual a forças a favor, menos forças contra, [p=0.2] {b}dividido pela soma das massas. [p=0.3] {c}Depois, a tração sai do bloco com menos forças."),
    dict(id="s13", block="atalho", text="Funciona porque {a}as trações são forças internas do conjunto, [p=0.2] e somem quando você olha tudo junto. [p=0.3] {b}Não compensa quando os blocos não andam juntos, [p=0.2] como {c}fio frouxo ou polia que se move: [p=0.2] aí, cada bloco tem a sua aceleração."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Uma polia presa no teto, [p=0.2] com {b}um bloco de três quilogramas de um lado [p=0.1] e {c}um de dois quilogramas do outro, [p=0.2] os dois pendurados. [p=0.3] {d}Qual é a aceleração? [p=0.2] E {e}a tração no fio?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O de três desce, e o de dois sobe. [p=0.2] {b}A favor: o peso do de três, trinta. [p=0.1] {c}Contra: o peso do de dois, vinte. [p=0.3] {d}Á é trinta menos vinte, dividido por cinco: [p=0.1] {e}dois metros por segundo ao quadrado."),
    dict(id="s17", block="resposta", text="{a}Tração, pelo bloco de dois, que sobe: [p=0.2] {b}tê menos vinte é igual a dois vezes dois. [p=0.2] {c}Tê vale vinte e quatro newtons. [p=0.3] Confira no de três: {d}trinta menos vinte e quatro, seis, [p=0.2] e seis dividido por três dá dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}blocos ligados andam com a mesma aceleração; [p=0.2] {b}junte todos num corpo só, onde a tração some; [p=0.2] e {c}depois isole o bloco mais simples para achar a tração."),
    dict(id="s19", block="fim", text="Na próxima aula, o movimento {a}faz curva: [p=0.2] você vai ver {b}a força que aponta para o centro [p=0.2] e calcular {c}a aceleração centrípeta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
