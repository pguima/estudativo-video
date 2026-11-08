# Estudativo · MAT-EXP-006 — Equação exponencial com troca de variável (Matemática · Exponencial e Logaritmo).
# Habilidade: resolver 4ˣ − 6 · 2ˣ + 8 = 0 chamando 2ˣ de y.
# Pré-requisitos: MAT-EXP-004 (igualar as bases), MAT-FAT-011 (soma e produto). Próxima: MAT-EXP-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equação exponencial com troca de variável"

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
    dict(id="s01", block="gancho", text="{a}Quatro elevado a xis, [p=0.2] menos seis vezes dois elevado a xis, [p=0.2] mais oito, igual a zero. [p=0.3] São três termos, e {b}igualar as bases não resolve. [p=0.3] Mas com {c}um apelido, ela vira uma equação do segundo grau que você resolve de cabeça."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve esse tipo de equação sem pular nenhum passo, [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}igualar as bases, [p=0.2] {b}achar raízes por soma e produto, [p=0.2] e {c}saber que a exponencial de base positiva nunca dá zero nem negativo. [p=0.3] Se faltar alguma, procure no canal."),
    # o quadrado escondido
    dict(id="s04", block="quadrado", text="O segredo está no quatro. [p=0.2] {a}Quatro é dois ao quadrado. [p=0.2] Então quatro elevado a xis é {b}dois ao quadrado, tudo elevado a xis. [p=0.2] Potência de potência multiplica os expoentes, e fica {c}dois elevado a dois xis."),
    dict(id="s05", block="quadrado", text="E dois xis é o mesmo que xis vezes dois. [p=0.2] Pela mesma regra, de trás para a frente, [p=0.2] fica {a}dois elevado a xis, tudo ao quadrado. [p=0.3] Ou seja: quatro elevado a xis é {b}o quadrado de dois elevado a xis."),
    dict(id="s06", block="quadrado", text="Confira com xis igual a três. [p=0.2] {a}Quatro ao cubo dá sessenta e quatro. [p=0.2] {b}Dois ao cubo dá oito, [p=0.2] e {c}oito ao quadrado dá sessenta e quatro."),
    # apelido
    dict(id="s07", block="apelido", text="Agora o apelido: {a}chame dois elevado a xis de ípsilon. [p=0.2] Quatro elevado a xis vira {b}ípsilon ao quadrado. [p=0.3] A equação fica {c}ípsilon ao quadrado menos seis ípsilon mais oito igual a zero."),
    dict(id="s08", block="apelido", text="Soma e produto: [p=0.2] {a}soma seis, produto oito. [p=0.2] Os pares com produto oito são um e oito. [p=0.1] Ou dois e quatro. [p=0.2] {b}Dois e quatro somam seis. [p=0.3] Então {c}ípsilon igual a dois, ou ípsilon igual a quatro."),
    # volta
    dict(id="s09", block="volta", text="Mas a pergunta é o xis, e não o ípsilon. [p=0.2] Volte ao apelido. [p=0.2] {a}Dois elevado a xis igual a dois dá xis igual a um. [p=0.2] {b}Dois elevado a xis igual a quatro dá xis igual a dois."),
    dict(id="s10", block="volta", text="Com xis igual a um, a conta fica {a}quatro menos doze mais oito, e dá zero. [p=0.2] Com xis igual a dois, fica {b}dezesseis menos vinte e quatro mais oito, e também dá zero. [p=0.2] Xis igual a um e xis igual a dois servem."),
    dict(id="s11", block="metodo", text="O método tem {a}quatro passos. [p=0.2] {b}Ache a potência que se repete. [p=0.2] {c}Dê o apelido. [p=0.2] {d}Resolva em ípsilon. [p=0.2] {e}Volte para o xis."),
    # descarte
    dict(id="s12", block="descarte", text="Às vezes, uma raiz {a}não volta. [p=0.2] Veja {b}nove elevado a xis, [p=0.2] menos dois vezes três elevado a xis, [p=0.2] menos três, igual a zero. [p=0.3] Nove é três ao quadrado. [p=0.2] Com ípsilon igual a três elevado a xis: {c}ípsilon ao quadrado menos dois ípsilon menos três igual a zero."),
    dict(id="s13", block="descarte", text="Produto menos três, soma dois: {a}as raízes são três e menos um. [p=0.2] {b}Três elevado a xis igual a três dá xis igual a um. [p=0.3] Mas {c}três elevado a xis igual a menos um não tem solução: [p=0.2] a exponencial de base positiva nunca dá negativo. [p=0.2] Essa raiz {d}se descarta. [p=0.2] Resposta: só xis igual a um."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}parar no ípsilon. [p=0.2] Na primeira equação, a pessoa responde {b}xis igual a dois ou xis igual a quatro. [p=0.3] Teste o quatro. [p=0.2] {c}Quatro elevado a quatro dá duzentos e cinquenta e seis. [p=0.2] {d}Seis vezes dois elevado a quatro dá noventa e seis."),
    dict(id="s15", block="erro", text="{a}Duzentos e cinquenta e seis menos noventa e seis mais oito dá cento e sessenta e oito. [p=0.2] Não deu zero. [p=0.3] O xis igual a dois só aparece ali por coincidência, [p=0.2] e o xis igual a um ficou de fora. [p=0.3] O ípsilon é o apelido, {b}e não a resposta."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}separe a soma do expoente. [p=0.2] Repete a base e soma os expoentes, só que de trás para a frente: [p=0.2] {b}dois elevado a xis mais um, com o xis mais um todo no expoente, é dois vezes dois elevado a xis."),
    dict(id="s17", block="atalho", text="Veja a equação na tela: {a}dois elevado a xis mais um, com o xis mais um todo no expoente, somado a dois elevado a xis, igual a vinte e quatro. [p=0.3] Com o apelido, fica {b}dois ípsilon mais ípsilon igual a vinte e quatro. [p=0.2] {c}Três ípsilon igual a vinte e quatro, e ípsilon igual a oito. [p=0.2] Dois elevado a xis igual a oito dá {d}xis igual a três."),
    dict(id="s18", block="atalho", text="Funciona porque {a}multiplicar potências de mesma base soma os expoentes, e o caminho de volta separa. [p=0.3] Não compensa quando só há {b}uma potência, como dois elevado a xis mais um, com o xis mais um todo no expoente, igual a trinta e dois. [p=0.2] Aí, {c}iguale as bases direto."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Resolva {a}quatro elevado a xis, [p=0.2] menos três vezes dois elevado a xis, [p=0.2] menos quatro, igual a zero."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Com {a}ípsilon igual a dois elevado a xis: [p=0.2] {b}ípsilon ao quadrado menos três ípsilon menos quatro igual a zero. [p=0.2] Produto menos quatro, soma três: {c}as raízes são quatro e menos um."),
    dict(id="s22", block="resposta", text="{a}Dois elevado a xis igual a quatro dá xis igual a dois. [p=0.2] {b}Dois elevado a xis igual a menos um: descarte. [p=0.3] Resposta: {c}xis igual a dois. [p=0.2] Conferindo: {d}dezesseis menos doze menos quatro dá zero."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}apelide a potência que se repete, [p=0.2] {b}resolva em ípsilon [p=0.2] e {c}volte para o xis, descartando o que for zero ou negativo."),
    dict(id="s24", block="fim", text="Na próxima aula, você pratica tudo da função exponencial: [p=0.2] {a}monta modelos de crescimento e de meia-vida [p=0.2] e {b}resolve equações exponenciais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
