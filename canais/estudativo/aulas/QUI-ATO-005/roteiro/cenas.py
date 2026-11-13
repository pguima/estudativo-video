# Estudativo · QUI-ATO-005 — Distribuição eletrônica: diagrama de Pauling (Química · Átomo e Tabela Periódica).
# Habilidade: distribuir os 26 elétrons do ferro pelo diagrama de Pauling, seguindo as diagonais.
# Pré-requisitos: QUI-ATO-003, QUI-ATO-004. Próxima: QUI-ATO-006 (camada de valência e distribuição dos íons).
# Questão inédita, criada para esta aula. Leitura: 2s² = "dois esse dois"; subníveis "esse, pê, dê, efe"; camadas "cá, éle...".
# Contas: Fe (26) = 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶; o erro de encher 3d antes de 4s dá ...3p⁶ 3d⁸ (também soma 26);
# Br (35) = ... 4s² 3d¹⁰ 4p⁵ (20 + 10 + 5). Capacidades s 2, p 6, d 10, f 14. Exceções (Cr, Cu) não entram.

TITULO = "Distribuição eletrônica: diagrama de Pauling"

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
    dict(id="s01", block="gancho", text="{a}O ferro tem vinte e seis elétrons. [p=0.3] {b}Onde fica cada um? [p=0.3] Um desenho simples responde isso em menos de um minuto: [p=0.1] {c}o diagrama de Pauling."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}desenhar o diagrama, [p=0.2] {b}seguir as diagonais [p=0.2] e {c}distribuir os elétrons do ferro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Das aulas anteriores: [p=0.1] {a}os elétrons ficam em camadas, numeradas de um a sete a partir do núcleo: [p=0.1] a um é a cá, a dois é a éle. [p=0.3] E, {b}num átomo neutro, o número de elétrons é igual ao zê."),
    # subníveis
    dict(id="s04", block="subniveis", text="{a}Cada camada se divide em partes menores, os subníveis. [p=0.2] Pense num prédio: [p=0.1] {b}a camada é o andar, [p=0.1] e {c}o subnível é um apartamento desse andar. [p=0.3] Os subníveis têm letras: {d}esse, pê, dê e efe."),
    dict(id="s05", block="subniveis", text="Cada subnível tem {a}um limite de elétrons. [p=0.2] {b}No esse cabem dois. [p=0.1] {c}No pê, seis. [p=0.1] {d}No dê, dez. [p=0.1] {e}No efe, catorze. [p=0.3] São os únicos números para decorar nesta aula."),
    dict(id="s06", block="subniveis", text="Para escrever, use {a}o número da camada, [p=0.1] {b}a letra do subnível [p=0.1] e, {c}no alto, quantos elétrons há ali. [p=0.3] {d}Dois esse dois: [p=0.1] camada dois, subnível esse, com dois elétrons."),
    # o diagrama
    dict(id="s07", block="diagrama", text="Os elétrons ocupam primeiro {a}os subníveis de menor energia. [p=0.2] Só que essa ordem {b}não é a ordem das camadas. [p=0.3] {c}O quatro esse, por exemplo, enche antes do três dê."),
    dict(id="s08", block="diagrama", text="O diagrama de Pauling mostra a ordem certa. [p=0.2] {a}Escreva uma linha por camada: [p=0.2] {b}um esse; [p=0.1] {c}dois esse, dois pê; [p=0.1] {d}três esse, três pê, três dê; [p=0.1] quatro esse, quatro pê, quatro dê, quatro efe; [p=0.1] {e}e assim até a sétima linha, como no desenho."),
    dict(id="s09", block="diagrama", text="{a}Trace diagonais paralelas, de cima à direita para baixo à esquerda. [p=0.3] Siga uma diagonal depois da outra: [p=0.1] {b}um esse, [p=0.15] dois esse, [p=0.15] dois pê, [p=0.15] três esse, [p=0.15] três pê, [p=0.15] {c}quatro esse, [p=0.15] três dê, [p=0.15] quatro pê. [p=0.3] {d}Essa é a ordem de encher."),
    # o ferro
    dict(id="s10", block="ferro", text="Vamos ao ferro, {a}com vinte e seis elétrons. [p=0.2] Encha cada subnível até o limite, na ordem das diagonais. [p=0.3] {b}Um esse dois: sobram vinte e quatro. [p=0.2] {c}Dois esse dois: sobram vinte e dois. [p=0.2] {d}Dois pê seis: sobram dezesseis."),
    dict(id="s11", block="ferro", text="{a}Três esse dois: sobram catorze. [p=0.2] {b}Três pê seis: sobram oito. [p=0.2] {c}Quatro esse dois: sobram seis. [p=0.3] {d}No três dê cabem dez, mas só sobraram seis: [p=0.1] {e}três dê seis. [p=0.2] Acabaram os elétrons."),
    dict(id="s12", block="ferro", text="{a}A distribuição do ferro termina em quatro esse dois, três dê seis. [p=0.3] O último subnível ficou incompleto, [p=0.1] {b}e isso é normal."),
    # erro
    dict(id="s13", block="erro", text="O erro comum: [p=0.1] {a}seguir a ordem das camadas e encher o três dê antes do quatro esse. [p=0.3] {b}O ferro terminaria em três dê oito, [p=0.1] com o quatro esse vazio. [p=0.3] {c}Está errado: pelas diagonais, o quatro esse vem antes."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho para conferir: [p=0.1] {a}some os números do alto. [p=0.3] {b}Dois mais dois mais seis, [p=0.15] mais dois mais seis, [p=0.15] mais dois mais seis, [p=0.1] {c}dá vinte e seis. [p=0.2] {d}Bateu com os elétrons do ferro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada número do alto conta elétrons, [p=0.1] e o total tem que fechar. [p=0.3] {b}Só não pega a troca de ordem: [p=0.1] o três dê oito errado {c}também soma vinte e seis. [p=0.2] Para a ordem, {d}confie nas diagonais."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O bromo tem trinta e cinco elétrons. [p=0.3] {b}Faça a distribuição pelo diagrama de Pauling [p=0.1] e {c}diga qual é o último subnível."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Até o quatro esse, é igual ao ferro: [p=0.1] são vinte elétrons. [p=0.2] {b}Sobram quinze. [p=0.2] {c}Três dê dez, o limite: [p=0.1] sobram cinco. [p=0.2] {d}Quatro pê cinco. [p=0.3] O último subnível é {e}o quatro pê, com cinco elétrons."),
    dict(id="s19", block="resposta", text="Conferindo: [p=0.1] {a}vinte mais dez mais cinco dá trinta e cinco. [p=0.2] {b}Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}no esse cabem dois, no pê seis, no dê dez, no efe catorze. [p=0.2] {b}Encha na ordem das diagonais [p=0.1] e {c}some os números do alto para conferir."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre {a}quantos elétrons ficam na última camada [p=0.2] e {b}como fica a distribuição de um íon. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
