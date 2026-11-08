# Estudativo · MAT-CNT-001 — Princípio multiplicativo e árvore de possibilidades (Matemática · Contagem e Probabilidade).
# Habilidade: contar 3 camisas e 4 calças como 12 combinações de roupa, desenhar a árvore e calcular que há 10⁴ senhas de 4 dígitos.
# Pré-requisitos: MAT-POT-001 (o que é potência). Próxima: MAT-CNT-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem restrição nem soma de casos: isso é MAT-CNT-002.
# Árvore (E.arvore): raiz → 3 camisas (branca, azul, preta) → 4 calças cada (jeans, cinza, bege, verde) = 12 pontas; 12 × 2 tênis = 24.
# Casinhas: 3 × 4 × 2 = 24 · senha 10 × 10 × 10 × 10 = 10⁴ = 10.000 · 10⁶ = 1.000.000. Erro: 3 + 4 = 7.
# Questão: 3 pães × 5 recheios × 2 bebidas = 30 (somando dá 10) · cadeado 10³ = 1.000 (000 a 999).

TITULO = "Princípio multiplicativo e árvore de possibilidades"

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
    dict(id="s01", block="gancho", text="{a}Três camisas {b}e quatro calças. [p=0.3] Quantas roupas diferentes dá para montar? [p=0.3] Se você respondeu {c}sete, [p=0.2] você somou. [p=0.2] A resposta é {d}doze."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta possibilidades sem listar uma por uma, [p=0.2] desenha a {b}árvore de possibilidades [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}tabuada [p=0.2] e de {b}potência: [p=0.2] o expoente diz quantas vezes a base aparece na multiplicação. [p=0.3] Se faltar alguma, procure no canal."),
    # árvore
    dict(id="s04", block="arvore", text="Vamos montar as roupas. [p=0.2] As camisas são {a}branca, azul e preta. [p=0.2] As calças são {b}jeans, cinza, bege e verde."),
    dict(id="s05", block="arvore", text="Comece pela {a}camisa branca. [p=0.2] Com ela, dá para usar {b}qualquer uma das calças. [p=0.3] Só com a branca, já são {c}quatro roupas."),
    dict(id="s06", block="arvore", text="Desenhe isso como {a}uma árvore. [p=0.2] Do ponto de partida saem {b}três galhos, um para cada camisa. [p=0.2] De cada camisa saem {c}quatro galhos, um para cada calça. [p=0.3] Cada ponta da árvore é {d}uma roupa completa."),
    dict(id="s07", block="arvore", text="Conte as pontas: [p=0.2] {a}quatro com a branca, [p=0.2] {b}quatro com a azul, [p=0.2] {c}quatro com a preta. [p=0.3] São três grupos de quatro: [p=0.2] {d}três vezes quatro dá doze."),
    dict(id="s08", block="arvore", text="A ordem das etapas não muda o total. [p=0.2] {a}Comece pela calça: [p=0.2] quatro galhos, cada um com três camisas. [p=0.3] {b}Quatro vezes três dá doze do mesmo jeito. [p=0.2] Muda o desenho, não a conta."),
    # regra
    dict(id="s09", block="regra", text="Esse é o {a}princípio multiplicativo, [p=0.2] também chamado de princípio fundamental da contagem. [p=0.3] Quando uma escolha é feita {b}em etapas, [p=0.2] e você faz {c}todas as etapas, [p=0.2] {d}multiplique as opções de cada etapa."),
    dict(id="s10", block="regra", text="Por que multiplicar, e não somar? [p=0.2] Porque {a}cada opção da primeira etapa combina com todas as opções da segunda. [p=0.3] Junte {b}um par de tênis, entre dois que você tem: [p=0.2] a árvore ganha {c}mais um andar, [p=0.2] e cada roupa vira duas. [p=0.2] {d}Doze vezes dois dá vinte e quatro."),
    # casinhas
    dict(id="s11", block="casinhas", text="Desenhar a árvore inteira cansa. [p=0.2] Na prova, faça {a}uma casinha para cada etapa [p=0.2] e escreva dentro {b}quantas opções ela tem. [p=0.3] {c}Camisa: três opções. [p=0.2] {d}Calça: quatro. [p=0.2] {e}Tênis: duas. [p=0.3] {f}Três vezes quatro vezes dois dá vinte e quatro."),
    # senha
    dict(id="s12", block="senha", text="Veja uma senha de banco com {a}quatro dígitos. [p=0.2] Dígito é o mesmo que algarismo, os símbolos que formam os números: [p=0.2] {b}de zero a nove, são dez. [p=0.3] E na senha {c}pode repetir algarismo."),
    dict(id="s13", block="senha", text="Faça {a}quatro casinhas. [p=0.2] Cada uma aceita {b}dez algarismos. [p=0.2] Como pode repetir, a casinha não perde opção com o que veio antes. [p=0.3] A conta é {c}dez vezes dez vezes dez vezes dez, [p=0.2] que dá {d}dez mil senhas."),
    # erro
    dict(id="s14", block="erro", text="O erro do começo é {a}somar. [p=0.2] Três camisas mais quatro calças dá sete, [p=0.3] mas sete é só {b}o número de peças no armário. [p=0.3] Uma roupa usa {c}uma camisa e uma calça ao mesmo tempo, [p=0.2] e cada camisa vai com quatro calças. [p=0.2] Por isso, {d}doze. [p=0.2] Confira na árvore: são doze pontas, não sete."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}casinhas iguais viram potência. [p=0.3] Na senha, o dez aparece quatro vezes: [p=0.2] {b}dez elevado a quatro. [p=0.3] A base é {c}quantas opções cabem em cada casinha. [p=0.2] O expoente é {d}quantas casinhas existem."),
    dict(id="s16", block="atalho", text="Funciona porque {a}potência é multiplicação repetida. [p=0.3] Uma senha de seis dígitos? [p=0.2] {b}Dez elevado a seis dá um milhão. [p=0.3] {c}Não compensa quando as casinhas têm números diferentes, [p=0.2] como camisa e calça: [p=0.2] aí, {d}multiplique um por um."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Numa lanchonete, o cliente monta o combo escolhendo {a}um pão entre três tipos, [p=0.2] {b}um recheio entre cinco [p=0.2] e {c}uma bebida entre duas. [p=0.3] {d}Quantos combos diferentes existem? [p=0.3] E um cadeado tem {e}três rodinhas, cada uma de zero a nove. [p=0.2] {f}Quantos códigos diferentes ele aceita?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] São três etapas, e o cliente faz todas. [p=0.2] {a}Três vezes cinco dá quinze. [p=0.2] {b}Quinze vezes dois dá trinta combos. [p=0.3] Quem somou chegou em {c}dez, e errou: [p=0.2] isso é só o número de itens do cardápio."),
    dict(id="s20", block="resposta", text="No cadeado, são {a}três casinhas iguais, com dez opções cada. [p=0.2] {b}Dez elevado a três dá mil códigos, [p=0.2] {c}do zero zero zero até o nove nove nove."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}escolha em etapas, e você faz todas? Multiplique. [p=0.3] {b}Casinhas iguais viram potência."),
    dict(id="s22", block="fim", text="Na próxima aula, as casinhas ganham {a}regras: [p=0.2] algarismo que não pode repetir, [p=0.2] zero que não pode vir na frente. [p=0.3] E você descobre {b}por qual casinha começar. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
