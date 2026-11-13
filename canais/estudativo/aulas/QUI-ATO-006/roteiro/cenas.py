# Estudativo · QUI-ATO-006 — Camada de valência e distribuição dos íons (Química · Átomo e Tabela Periódica).
# Habilidade: dizer quantos elétrons o enxofre tem na última camada e distribuir os elétrons do Fe²⁺ tirando-os da camada mais externa.
# Pré-requisitos: QUI-ATO-005. Próxima: QUI-ATO-007 (praticando: átomos e distribuição eletrônica).
# Questão inédita, criada para esta aula. Leitura: 4s² = "quatro esse dois".
# Contas: S (16) = 1s² 2s² 2p⁶ 3s² 3p⁴ → valência 3s² 3p⁴ = 6; S²⁻ = 18 e⁻ → ... 3p⁶; Fe (26) termina em 4s² 3d⁶ → valência 2;
# Fe²⁺ = 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ (24); o erro (tirar do 3d) dá ... 4s² 3d⁴ (também 24);
# Mn (25) = ... 4s² 3d⁵ → valência 2; Mn²⁺ = ... 3p⁶ 3d⁵ (23). Fe³⁺ (tira também do 3d) fica de fora de propósito.

TITULO = "Camada de valência e distribuição dos íons"

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
    dict(id="s01", block="gancho", text="{a}A distribuição do ferro termina em três dê seis. [p=0.3] Então ele tem seis elétrons na última camada? [p=0.3] {b}Não: tem dois. [p=0.2] {c}Última camada e último subnível escrito são coisas diferentes."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai achar {a}a camada de valência de um átomo [p=0.2] e {b}distribuir os elétrons de um íon sem cair na armadilha."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}a distribuição segue as diagonais de Pauling. [p=0.3] E da aula de íons: [p=0.1] {b}o cátion perdeu elétrons, [p=0.1] {c}o ânion ganhou."),
    # camada de valência
    dict(id="s04", block="valencia", text="{a}A camada de valência é a camada mais externa ocupada, [p=0.1] {b}a de número maior. [p=0.3] São os elétrons dela que {c}o átomo pode ceder, receber ou dividir com outro átomo. [p=0.2] {d}Como isso acontece é assunto de outra aula."),
    dict(id="s05", block="valencia", text="Vamos ao enxofre, {a}com dezesseis elétrons. [p=0.2] {b}Um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê seis, [p=0.1] três esse dois, [p=0.1] três pê quatro. [p=0.3] {c}O maior número de camada é o três. [p=0.2] {d}Na camada três, dois mais quatro dá seis elétrons."),
    dict(id="s06", block="valencia", text="No ferro, a distribuição termina em {a}quatro esse dois, três dê seis. [p=0.3] {b}O maior número de camada é o quatro, [p=0.1] e nela só está {c}o quatro esse dois. [p=0.2] {d}Dois elétrons na valência. [p=0.2] {e}O três dê é da camada três, mais de dentro."),
    # íons
    dict(id="s07", block="ions", text="{a}Para um ânion, é fácil: [p=0.1] {b}some os elétrons ganhos e distribua normalmente. [p=0.3] {c}O enxofre com carga dois menos tem dezesseis mais dois, que dá dezoito elétrons. [p=0.2] {d}A distribuição termina em três pê seis."),
    dict(id="s08", block="ions", text="{a}Para um cátion, a regra pega muita gente. [p=0.2] {b}Os elétrons saem da camada mais externa, [p=0.1] {c}e não do último subnível escrito. [p=0.3] {d}O ferro com carga dois mais perdeu dois elétrons. [p=0.2] {e}Eles saem do quatro esse, que é a camada quatro."),
    dict(id="s09", block="ions", text="{a}Sobra um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê seis, [p=0.1] três esse dois, [p=0.1] três pê seis, [p=0.1] três dê seis. [p=0.3] São {b}vinte e quatro elétrons, [p=0.1] e {c}o três dê seis ficou inteiro."),
    dict(id="s10", block="ions", text="Por que assim? [p=0.2] {a}O quatro esse entra primeiro porque tem menos energia. [p=0.2] Mas, {b}com o átomo pronto, ele está na camada de fora. [p=0.3] {c}Entra pela energia, sai pela camada."),
    # erro
    dict(id="s11", block="erro", text="O erro comum: [p=0.1] {a}tirar os dois elétrons do três dê, o último escrito. [p=0.3] {b}A distribuição terminaria em quatro esse dois, três dê quatro. [p=0.2] {c}O total também é vinte e quatro, [p=0.1] mas está errado: [p=0.1] {d}os elétrons saem do quatro esse."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}antes de tirar elétrons, reescreva a distribuição em ordem de camada. [p=0.3] {b}O três dê vem antes do quatro esse, que vai para o fim. [p=0.2] {c}Aí, é só tirar do final."),
    dict(id="s13", block="atalho", text="Funciona porque, {a}na ordem das camadas, a mais externa fica no fim. [p=0.3] {b}Não precisa disso para os ânions: [p=0.1] {c}eles ganham elétrons e seguem as diagonais."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}O manganês tem vinte e cinco elétrons, [p=0.1] e a distribuição termina em {b}quatro esse dois, três dê cinco. [p=0.3] {c}Quantos elétrons ele tem na valência? [p=0.2] E {d}como fica a distribuição do manganês com carga dois mais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}A camada mais externa é a quatro, com quatro esse dois: [p=0.1] {b}dois elétrons na valência. [p=0.3] {c}Carga dois mais: saem dois elétrons, do quatro esse. [p=0.2] {d}Fica um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê seis, [p=0.1] três esse dois, [p=0.1] três pê seis, [p=0.1] três dê cinco. [p=0.2] {e}Vinte e três elétrons."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}valência é a camada de número maior. [p=0.2] {b}No ânion, some e distribua. [p=0.1] {c}No cátion, tire da camada mais externa."),
    dict(id="s18", block="fim", text="Na próxima aula, você pratica {a}tudo do átomo, dos modelos à distribuição, [p=0.2] com {b}questões no estilo da prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
