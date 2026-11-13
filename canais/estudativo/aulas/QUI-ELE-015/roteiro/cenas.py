# Estudativo · QUI-ELE-015 — Balancear por oxirredução (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: igualar os elétrons perdidos e ganhos para acertar a equação de uma oxirredução.
# Pré-requisitos: QUI-ELE-002. Próxima: QUI-ELE-003 (pilha de Daniell).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Leituras: Al³⁺ = "alumínio três mais", Cu²⁺ = "cobre dois mais", Fe₂O₃ = "fé dois ó três", CO = "cê ó, o monóxido", O₂ = "ó dois".
# MMC não está em "Já ensinado": o cruzamento é explicado pelos elétrons (seis perdidos, seis ganhos), sem citar MMC.
# Contas: Al 0 → +3 (perde 3) · Cu²⁺ +2 → 0 (ganha 2) → 2 Al + 3 Cu²⁺ → 2 Al³⁺ + 3 Cu (6 e⁻; carga +6 = +6).
# Alto-forno: Fe +3 → 0, 3 × 2 átomos = 6 · C +2 → +4, 2 × 1 = 2 → 2 Fe₂O₃ e 6 CO → ÷2 → Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂ (O: 6 = 6).
# Erro (sem a atomicidade): 2 Fe₂O₃ + 3 CO → 4 Fe + 3 CO₂ dá O: 9 contra 6. Questão: 4 Fe + 3 O₂ → 2 Fe₂O₃ (Fe: 3; O: 2 × 2 = 4).

TITULO = "Balancear por oxirredução"

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
    dict(id="s01", block="gancho", text="{a}Alumínio mais cobre dois mais, [p=0.1] dá alumínio três mais e cobre. [p=0.3] {b}Um alumínio de cada lado, um cobre de cada lado. [p=0.2] Parece balanceada. [p=0.3] {c}Mas está errada."),
    dict(id="s02", block="gancho", text="{a}O alumínio perde três elétrons, [p=0.1] {b}e o cobre só recebe dois. [p=0.2] {c}Sobra elétron. [p=0.3] {d}Até o fim desta aula, você vai igualar os elétrons perdidos e ganhos [p=0.1] para acertar qualquer oxirredução, [p=0.2] e ainda leva um {e}atalho para conferir."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Quem se oxida perde elétrons, e o Nox sobe; [p=0.1] {b}quem se reduz ganha, e o Nox desce. [p=0.3] E {c}balancear por tentativas, contando os átomos de cada lado. [p=0.2] Se faltar alguma, procure no canal."),
    # regra
    dict(id="s04", block="regra", text="A regra é uma só: [p=0.2] {a}os elétrons não somem nem aparecem do nada. [p=0.3] {b}Todo elétron que um perde, o outro ganha. [p=0.2] Então, {c}na equação certa, elétrons perdidos e ganhos são iguais."),
    dict(id="s05", block="regra", text="Na conta do alumínio: [p=0.2] {a}cada alumínio perde três. [p=0.1] {b}Cada cobre ganha dois. [p=0.3] Quantos de cada, para empatar? [p=0.2] {c}Com dois alumínios, saem seis elétrons. [p=0.2] {d}Com três cobres, entram seis. [p=0.3] {e}Seis de cada lado: fechou."),
    dict(id="s06", block="regra", text="{a}O dois foi para o alumínio, [p=0.1] e o três, para o cobre. [p=0.2] {b}O número de elétrons de um virou o coeficiente do outro. [p=0.3] Isso tem nome: {c}cruzar."),
    dict(id="s07", block="regra", text="{a}Dois alumínios mais três íons cobre dois mais [p=0.1] dão dois íons alumínio três mais e três cobres."),
    # método
    dict(id="s08", block="metodo", text="O método tem quatro passos. [p=0.2] {a}Um: calcule o Nox e ache quem sobe e quem desce. [p=0.3] {b}Dois: conte os elétrons por fórmula, nos reagentes, do lado esquerdo: [p=0.1] a variação do Nox vezes quantos átomos daquele elemento a fórmula tem. [p=0.3] {c}Três: cruze. [p=0.2] {d}Quatro: feche o resto por tentativas."),
    # alto-forno
    dict(id="s09", block="forno", text="Teste com o alto-forno. [p=0.2] {a}Fé dois ó três mais cê ó, o monóxido de carbono, [p=0.1] dá ferro e cê ó dois. [p=0.3] {b}O ferro desce de mais três para zero: três elétrons por átomo. [p=0.2] {c}Mas o minério tem dois ferros: [p=0.1] {d}três vezes dois, seis elétrons por fórmula."),
    dict(id="s10", block="forno", text="{a}O carbono sobe de mais dois para mais quatro: [p=0.1] dois elétrons, com um carbono só. [p=0.3] {b}Cruze: o dois vai para o minério, {c}o seis vai para o monóxido. [p=0.3] {d}Dois e seis são pares: divida por dois. [p=0.2] {e}Fica um minério e três monóxidos."),
    dict(id="s11", block="forno", text="{a}Feche por tentativas. [p=0.2] Um minério tem dois ferros: {b}dois ferros do outro lado. [p=0.2] Três carbonos: {c}três cê ó dois. [p=0.3] {d}Confira o oxigênio: [p=0.1] três mais três, seis de um lado; [p=0.1] três vezes dois, seis do outro."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer quantos átomos a fórmula tem. [p=0.3] A pessoa usa {b}três elétrons para o minério, em vez de seis, [p=0.1] e cruza: {c}dois minérios e três monóxidos."),
    dict(id="s13", block="erro", text="{a}Aí, o oxigênio não fecha: [p=0.1] {b}nove de um lado, seis do outro. [p=0.3] {c}A variação vale por átomo. [p=0.2] {d}Multiplique sempre pelo índice do elemento na fórmula."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho para conferir: [p=0.2] {a}em equação com íons, some as cargas de cada lado. [p=0.3] {b}Na equação do alumínio, à esquerda, três íons de carga dois mais: carga total mais seis. [p=0.2] {c}À direita, dois íons de carga três mais: mais seis também. [p=0.2] {d}Cargas iguais: está certa."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a carga vem dos elétrons, e eles não somem. [p=0.3] {b}Na equação errada do começo, era mais dois contra mais três. [p=0.3] {c}Não compensa quando ninguém tem carga, como no alto-forno: [p=0.1] aí, confira pelos átomos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] O ferro reage com o gás oxigênio e forma óxido de ferro, a parte principal da ferrugem. [p=0.2] {a}Ferro mais ó dois, dá fé dois ó três. [p=0.3] {b}Balanceie pela oxirredução."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O ferro vai de zero a mais três: perde três, com um átomo. [p=0.3] {b}O oxigênio vai de zero a menos dois: [p=0.1] ganha dois por átomo, {c}e o ó dois tem dois átomos: quatro elétrons."),
    dict(id="s19", block="resposta", text="{a}Cruze: quatro ferros, três ó dois. [p=0.3] {b}Quatro ferros saem como dois fé dois ó três. [p=0.3] {c}Confira o oxigênio: três vezes dois, seis; [p=0.1] dois vezes três, seis. [p=0.2] {d}Doze elétrons perdidos, doze ganhos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}conte os elétrons por fórmula, multiplicando pelo índice, [p=0.1] {b}cruze os números [p=0.1] {c}e feche o resto por tentativas."),
    dict(id="s21", block="fim", text="Na próxima aula, em vez de passar direto de um átomo para o outro, os elétrons vão por um fio: [p=0.2] {a}é a pilha de Daniell. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
