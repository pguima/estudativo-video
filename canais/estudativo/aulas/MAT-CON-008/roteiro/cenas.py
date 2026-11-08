# Estudativo · MAT-CON-008 — União e interseção de intervalos (Matemática · Conjuntos · Conjuntos numéricos).
# Habilidade: achar [1, 5] ∩ ]3, 7[ = ]3, 5] empilhando as duas retas.
# Pré-requisitos: MAT-CON-002 (união e interseção, e/ou), MAT-CON-007 (intervalos e colchetes). Próxima: MAT-CON-009.
# Questão inédita, criada para esta aula.
# Contas: [1, 5] ∩ ]3, 7[ = ]3, 5] (3 ∉ ]3, 7[; 5 ∈ ambos) · [1, 5] ∪ ]3, 7[ = [1, 7[ (1 ∈ [1, 5]; 7 em nenhum).
# Erro: [3, 5] (3 está pintado na primeira reta, mas tem bolinha aberta na segunda).
# Atalho: maior dos começos (3), menor dos fins (5); vazio se o maior começo passar do menor fim, como [1, 2] ∩ [4, 6] = ∅.
# Questão: A = [−2, 4[, B = [0, 6]: A ∩ B = [0, 4[ (0 ∈ ambos; 4 ∉ A) · A ∪ B = [−2, 6].
# Visual: duas (ou três) retas empilhadas com E.reta + E.intervalo, números alinhados; faixa vertical sobre a parte em comum; reta-resposta embaixo.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "União e interseção de intervalos"

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
    dict(id="s01", block="gancho", text="{a}O intervalo fechado de um a cinco, [p=0.2] interseção com {b}o intervalo aberto de três a sete. [p=0.3] Muita gente responde {c}de três a cinco, fechado no três. [p=0.3] Só que {d}o três não pode entrar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você cruza e junta intervalos sem errar as pontas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}interseção é o que está em um e no outro, ao mesmo tempo; [p=0.2] união é o que está em pelo menos um. [p=0.3] E {c}intervalo na reta, com colchete e bolinha aberta ou fechada. [p=0.3] Se faltar alguma, procure no canal."),
    # empilhar
    dict(id="s04", block="pilha", text="O método é {a}empilhar as retas, com os números alinhados, um embaixo do outro. [p=0.3] {b}Em cima, o fechado de um a cinco: [p=0.2] bolinhas fechadas no um e no cinco. [p=0.3] {c}Embaixo, o aberto de três a sete: [p=0.2] bolinhas abertas no três e no sete."),
    # interseção
    dict(id="s05", block="intersecao", text="Interseção é a palavra {a}e: [p=0.2] só vale onde {b}ambas as retas estão pintadas. [p=0.3] Passe uma régua de cima para baixo. [p=0.2] Isso acontece {c}do três até o cinco."),
    dict(id="s06", block="intersecao", text="Falta conferir as pontas, uma de cada vez. [p=0.2] {a}O três está na reta de cima, [p=0.2] mas na de baixo a bolinha é aberta. [p=0.3] Para a interseção, ele teria que estar em ambas: {b}fica de fora. [p=0.3] {c}O cinco está na de cima, com bolinha fechada, [p=0.2] e na de baixo, no meio do pintado: {d}entra."),
    dict(id="s07", block="intersecao", text="Resposta: {a}aberto no três, fechado no cinco. [p=0.3] São os reais {b}maiores que três e até cinco. [p=0.3] Toda vez que um problema pede {c}duas condições ao mesmo tempo, [p=0.2] como xis maior que três e xis até cinco, [p=0.2] a resposta é {d}uma interseção."),
    # união
    dict(id="s08", block="uniao", text="E a união? [p=0.2] É a palavra {a}ou: vale onde {b}pelo menos uma reta está pintada. [p=0.3] Isso vai {c}do um até o sete. [p=0.3] {d}O um está na reta de cima: entra. [p=0.2] {e}O sete não está em nenhuma: fica de fora. [p=0.3] Resposta: {f}fechado no um, aberto no sete."),
    # erro
    dict(id="s09", block="erro", text="O erro do começo é {a}fechar o três. [p=0.2] A pessoa olha a reta de cima, vê o três pintado, [p=0.2] e fecha. [p=0.3] Mas a reta de baixo {b}deixa o três de fora. [p=0.3] {c}Na interseção, basta uma reta deixar a ponta de fora para ela sair. [p=0.2] {d}Na união, basta uma reta pegar a ponta para ela entrar."),
    # atalho
    dict(id="s10", block="atalho", text="Agora o atalho da interseção: [p=0.2] {a}o maior dos começos e o menor dos fins. [p=0.3] Começos: um e três. {b}O maior é três. [p=0.2] Fins: cinco e sete. {c}O menor é cinco. [p=0.3] {d}Do três ao cinco, sem desenhar."),
    dict(id="s11", block="atalho", text="Funciona porque, para estar em ambos, o número precisa {a}ter passado de cada começo [p=0.2] e {b}ainda não ter chegado em nenhum fim. [p=0.3] Mas o atalho só acha onde fica o pedaço: {c}as pontas, confira na pilha."),
    dict(id="s12", block="atalho", text="E se {a}o maior começo passar do menor fim? [p=0.2] Como no fechado de um a dois com o fechado de quatro a seis: [p=0.2] {b}não sobra nada, e a interseção é o vazio. [p=0.3] O atalho não compensa na união: [p=0.2] ali, {c}empilhe sempre, [p=0.2] porque pedaços separados não viram um intervalo só."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}O intervalo á vai de menos dois a quatro, fechado no menos dois e aberto no quatro. [p=0.3] {b}O intervalo bê vai de zero a seis, fechado nas pontas. [p=0.3] Calcule {c}a interseção e {d}a união."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Começos: menos dois e zero. {a}O maior é zero. [p=0.2] Fins: quatro e seis. {b}O menor é quatro. [p=0.3] Pontas na pilha: {c}o zero está em á e em bê: fechado. [p=0.2] {d}O quatro não está em á: aberto. [p=0.3] Interseção: {e}de zero a quatro, fechado no zero e aberto no quatro."),
    dict(id="s16", block="resposta", text="Na união, o pintado vai {a}do menos dois ao seis, sem buraco. [p=0.3] {b}O menos dois está em á: fechado. [p=0.2] {c}O seis está em bê: fechado. [p=0.3] União: {d}o intervalo fechado de menos dois a seis."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}empilhe as retas. [p=0.2] {b}Interseção, onde ambas estão pintadas. [p=0.2] {c}União, onde pelo menos uma está. [p=0.2] E {d}confira cada ponta."),
    dict(id="s18", block="fim", text="Na próxima aula, é {a}hora de praticar: [p=0.2] diagrama de Venn, conjuntos de números, fração geratriz e intervalos, [p=0.2] {b}tudo em problemas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
