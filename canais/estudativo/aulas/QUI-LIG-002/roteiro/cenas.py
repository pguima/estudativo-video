# Estudativo · QUI-LIG-002 — Ligação covalente e estrutura de Lewis (Química · Ligações Químicas · Ligações iônica, covalente e metálica).
# Habilidade: desenhar a estrutura de Lewis de H₂O, CO₂ e N₂ com ligações simples, duplas e triplas.
# Pré-requisitos: QUI-ATO-006, QUI-ATO-009. Próxima: QUI-LIG-003 (ligação metálica e ligas).
# Atenção: a QUI-LIG-001 NÃO está em "Já ensinado": a regra do octeto é explicada de novo, a partir dos gases nobres.
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Leituras: HCN = "agá cê ene", CO₂ = "cê ó dois", N₂ = "ene dois", H₂ = "agá dois".
# Fatos: N₂ é a maior parte do ar (≈ 78 %); a tripla N≡N é muito forte, e o N₂ quase não reage; HCN (ácido cianídrico) é
# um gás muito tóxico; BF₃: o boro fica com 6 elétrons (foge do octeto). Valência: H 1, C 4, N 5, O 6.
# Contas: H₂O, O = 4 (ligações) + 4 (pares livres) = 8; CO₂, C = 2 duplas = 8, O = 4 + 4 = 8; N₂, N = 6 + 2 = 8;
# HCN: C = 2 + 6 = 8, N = 6 + 2 = 8; erro O–C–O: C com 4.

TITULO = "Ligação covalente e estrutura de Lewis"

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
    dict(id="s01", block="gancho", text="A maior parte do ar que você respira é {a}gás nitrogênio, ene dois: [p=0.2] {b}dois átomos de nitrogênio presos por três ligações ao mesmo tempo. [p=0.3] {c}Como átomos iguais se seguram, se ambos querem ganhar elétrons e nenhum quer perder?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai desenhar a {b}estrutura de Lewis [p=0.1] da água, do gás carbônico e do nitrogênio, [p=0.2] com ligações {c}simples, duplas e triplas. [p=0.2] E leva um {d}atalho para saber quantas ligações cada átomo faz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Duas ideias de aulas anteriores. [p=0.2] {a}Os elétrons de valência são os da última camada, [p=0.1] e a família diz quantos são: [p=0.1] {b}na família quinze, cinco; na dezesseis, seis; na dezessete, sete. [p=0.3] E {c}os gases nobres, com oito, são estáveis; [p=0.1] só o hélio tem dois. [p=0.2] Daí vem uma regra: [p=0.1] {d}os outros átomos tendem a chegar a oito também. [p=0.2] Ela se chama regra do octeto, porque octeto quer dizer grupo de oito. [p=0.2] Se alguma ideia travar, procure no canal."),
    # compartilhar
    dict(id="s04", block="covalente", text="Entre dois ametais, {a}ninguém quer perder elétron: [p=0.1] ambos querem ganhar. [p=0.3] {b}A saída é dividir. [p=0.2] Cada átomo põe um elétron no meio, [p=0.1] e {c}esse par passa a contar para os dois átomos ao mesmo tempo. [p=0.3] {d}Um par de elétrons compartilhado é uma ligação covalente. [p=0.2] É assim que os átomos de uma molécula ficam presos."),
    dict(id="s05", block="covalente", text="Para desenhar, use a {a}estrutura de Lewis: [p=0.2] o símbolo do elemento com {b}os elétrons de valência em volta, como bolinhas. [p=0.3] {c}Hidrogênio, um. [p=0.1] {d}Carbono, quatro. [p=0.1] {e}Nitrogênio, cinco. [p=0.1] {f}Oxigênio, seis."),
    dict(id="s06", block="covalente", text="O caso mais simples é o {a}gás hidrogênio, agá dois. [p=0.2] {b}Cada hidrogênio tem um elétron. [p=0.2] {c}Juntos no meio, eles formam um par, [p=0.1] e cada átomo fica com dois, como o hélio. [p=0.3] {d}O par compartilhado se desenha como um traço: [p=0.1] agá, traço, agá."),
    # água
    dict(id="s07", block="agua", text="Na água, {a}o oxigênio tem seis e precisa de mais dois. [p=0.2] {b}Cada hidrogênio forma um par com ele: [p=0.1] {c}são duas ligações. [p=0.3] Sobram {d}dois pares no oxigênio, que não participam de ligação: [p=0.1] são os {e}pares livres. [p=0.3] Conte os elétrons do oxigênio: [p=0.1] {f}quatro nas ligações e quatro nos pares livres, oito."),
    # gás carbônico
    dict(id="s08", block="dupla", text="E se faltar mais de um? [p=0.2] No gás carbônico, {a}cê ó dois, [p=0.2] {b}o carbono tem quatro e precisa de mais quatro. [p=0.2] {c}Cada oxigênio precisa de dois. [p=0.3] A solução: {d}o carbono divide dois pares com cada oxigênio. [p=0.2] {e}Dois pares compartilhados são uma ligação dupla, dois traços. [p=0.3] {f}Ó, dupla, cê, dupla, ó."),
    dict(id="s09", block="dupla", text="Confira. [p=0.2] {a}O carbono tem duas ligações duplas: quatro pares, oito elétrons. [p=0.3] {b}Cada oxigênio tem uma dupla e dois pares livres: [p=0.1] quatro mais quatro, oito."),
    # nitrogênio
    dict(id="s10", block="tripla", text="E o nitrogênio do ar. [p=0.2] {a}Cada átomo tem cinco e precisa de três. [p=0.2] {b}Eles dividem três pares: [p=0.1] {c}uma ligação tripla, três traços. [p=0.3] Sobra {d}um par livre em cada nitrogênio. [p=0.2] Conta: {e}seis da tripla mais dois do par livre, oito. [p=0.3] {f}Essa tripla é tão forte que o nitrogênio do ar quase não reage."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}ligar tudo com traço simples. [p=0.2] {b}Ó, traço, cê, traço, ó. [p=0.3] {c}Conte o carbono: duas ligações simples, quatro elétrons. [p=0.2] {d}Faltam quatro para o octeto. [p=0.3] Sempre confira: {e}cada átomo, menos o hidrogênio, precisa fechar oito."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}o número de ligações que o átomo faz é o que falta para oito. [p=0.3] {b}Hidrogênio, uma, porque fecha com dois. [p=0.1] {c}Oxigênio, duas. [p=0.1] {d}Nitrogênio, três. [p=0.1] {e}Carbono, quatro. [p=0.3] Na prova, distribua os traços até cada átomo ter a sua conta: [p=0.1] {f}a dupla vale duas, a tripla vale três."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada ligação traz para a conta do átomo um elétron do vizinho. [p=0.3] {b}Não vale para os átomos que fogem do octeto, como o boro: [p=0.1] {c}esses ficam para outra aula."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] O {a}ácido cianídrico, agá cê ene, é uma substância muito tóxica. [p=0.2] {b}Desenhe a estrutura de Lewis. [p=0.2] {c}Que ligação fica entre o carbono e o nitrogênio, [p=0.1] e {d}quantos pares livres sobram?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá, com o atalho. [p=0.2] {a}O hidrogênio faz uma ligação só: fica na ponta, preso ao carbono. [p=0.3] {b}O carbono precisa de quatro: já tem uma, faltam três. [p=0.2] {c}O nitrogênio precisa de três. [p=0.2] Então, {d}entre carbono e nitrogênio, uma tripla. [p=0.3] {e}Agá, traço, cê, tripla, ene."),
    dict(id="s17", block="resposta", text="Os pares livres: [p=0.1] {a}o carbono já tem oito nas ligações, nenhum livre. [p=0.2] {b}O nitrogênio tem seis da tripla: [p=0.1] {c}sobra um par livre. [p=0.3] Resposta: {d}ligação tripla, e um par livre, no nitrogênio."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}ligação covalente é um par de elétrons compartilhado, [p=0.1] {b}cada traço é um par, [p=0.1] e {c}cada átomo faz as ligações que faltam para chegar a oito."),
    dict(id="s19", block="fim", text="Na próxima aula, a ligação entre metais: [p=0.2] {a}por que o cobre conduz eletricidade e dobra sem quebrar, [p=0.2] e {b}do que são feitos o bronze e o aço. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
