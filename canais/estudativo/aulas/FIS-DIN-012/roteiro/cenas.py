# Estudativo · FIS-DIN-012 — Lombada, globo da morte e pêndulo (Física · Dinâmica · Força centrípeta).
# Habilidade: achar a normal em lombadas e depressões, a velocidade mínima no topo de um looping com v = √(g·R) e a tração
# no ponto mais baixo do pêndulo.
# Pré-requisitos: FIS-DIN-010 (centrípeta), FIS-DIN-004 (peso e normal). Próxima: FIS-DIN-013.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². Tração (FIS-DIN-005) NÃO está em "Já ensinado", mas a habilidade pede a tração do pêndulo: a aula explica na
# hora que tração é a força do fio, que só puxa. Só os pontos mais alto e mais baixo (forças na vertical).

TITULO = "Lombada, globo da morte e pêndulo"

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
    dict(id="s01", block="gancho", text="{a}No topo de uma lombada, o estômago sobe, [p=0.2] e {b}o carro parece ficar mais leve. [p=0.3] {c}No globo da morte, a moto passa de cabeça para baixo e não cai. [p=0.3] {d}É a mesma física nos dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar {b}a normal na lombada e na baixada, [p=0.2] {c}a velocidade mínima no topo do globo [p=0.2] e {d}a força do fio no pêndulo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a força centrípeta, eme vê ao quadrado sobre erre, que é a resultante para o centro; [p=0.2] e {c}o peso, eme gê, e a normal. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="O método é um só. [p=0.2] {a}Marque onde fica o centro da curva. [p=0.2] {b}Forças que apontam para o centro entram com mais; [p=0.2] {c}as que apontam para fora, com menos. [p=0.3] {d}O resultado é igual a eme vê ao quadrado sobre erre."),
    # lombada
    dict(id="s05", block="lombada", text="{a}No topo da lombada, o centro da curva fica embaixo. [p=0.2] {b}O peso aponta para o centro; [p=0.1] {c}a normal, para fora. [p=0.3] {d}Pê menos ene, a letra da normal, é igual a eme vê ao quadrado sobre erre."),
    dict(id="s06", block="lombada", text="{a}Um carro de mil quilogramas, a dez metros por segundo, numa lombada de vinte metros de raio. [p=0.3] {b}Vê ao quadrado sobre erre: cem dividido por vinte, cinco. [p=0.2] {c}Dez mil menos ene é igual a mil vezes cinco. [p=0.2] {d}Ene vale cinco mil newtons: metade do peso. [p=0.2] Por isso, o carro parece mais leve."),
    dict(id="s07", block="lombada", text="{a}Na baixada, o centro fica em cima. [p=0.2] {b}Agora a normal aponta para o centro, e o peso para fora: [p=0.2] {c}ene menos pê é igual a eme vê ao quadrado sobre erre. [p=0.3] {d}Com os mesmos números, ene vale quinze mil newtons. [p=0.2] {e}A normal fica maior que o peso, e a suspensão sente."),
    # looping
    dict(id="s08", block="looping", text="{a}No topo do globo da morte, a moto está de cabeça para baixo, [p=0.2] e o centro fica embaixo dela. [p=0.3] {b}O peso aponta para o centro, [p=0.1] e {c}a normal, que o globo faz na roda, também. [p=0.3] {d}Ene mais pê é igual a eme vê ao quadrado sobre erre."),
    dict(id="s09", block="looping", text="{a}Quanto mais devagar, menor a normal. [p=0.2] {b}A velocidade mínima é quando a normal chega a zero: [p=0.2] {c}só o peso faz a centrípeta. [p=0.3] {d}Eme gê igual a eme vê ao quadrado sobre erre, [p=0.1] a massa corta, [p=0.1] e {e}vê mínimo é a raiz de gê vezes erre."),
    dict(id="s10", block="looping", text="{a}Num globo de três vírgula seis metros de raio: [p=0.2] {b}dez vezes três vírgula seis, trinta e seis. [p=0.2] {c}Raiz de trinta e seis: seis metros por segundo. [p=0.3] {d}Mais devagar que isso, a moto descola do globo no topo."),
    # pêndulo
    dict(id="s11", block="pendulo", text="{a}Agora, o pêndulo. [p=0.2] {b}A força do fio se chama tração, letra tê: o fio só puxa, sempre ao longo dele. [p=0.3] {c}No ponto mais baixo, o centro fica em cima: [p=0.2] {d}a tração aponta para o centro, e o peso para fora. [p=0.3] {e}Tê menos pê é igual a eme vê ao quadrado sobre erre."),
    dict(id="s12", block="pendulo", text="{a}Uma bola de dois quilogramas, num fio de um metro, passa embaixo a três metros por segundo. [p=0.3] {b}Tê menos vinte é igual a dois vezes nove dividido por um. [p=0.2] {c}Tê vale trinta e oito newtons, [p=0.2] {d}quase o dobro do peso. [p=0.2] É embaixo que o fio arrebenta."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a normal igual ao peso numa curva. [p=0.3] {b}Isso só vale no chão plano, parado ou com velocidade constante. [p=0.2] {c}Na lombada, ene igual a pê daria dez mil newtons, [p=0.2] {d}e o certo é cinco mil."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Corpo por cima da pista, no topo, como na lombada: a normal diminui, [p=0.1] {b}eme vezes, abre parênteses, gê menos vê ao quadrado sobre erre. [p=0.3] {c}Corpo embaixo, com o centro em cima, como na baixada e no pêndulo: a força aumenta, [p=0.1] {d}eme vezes, abre parênteses, gê mais vê ao quadrado sobre erre."),
    dict(id="s15", block="atalho", text="E no topo do looping, por dentro da pista, {a}decore: vê mínimo é a raiz de gê vezes erre. [p=0.3] Funciona porque {b}nesses pontos todas as forças estão na vertical. [p=0.2] {c}Não compensa no meio da curva, [p=0.1] onde as forças ficam inclinadas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma montanha-russa tem um looping de dez metros de raio. [p=0.3] {b}Qual é a velocidade mínima no topo? [p=0.2] E, {c}se o carrinho passa a vinte metros por segundo, [p=0.1] {d}qual é a normal numa pessoa de sessenta quilogramas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Vê mínimo é a raiz de dez vezes dez: [p=0.1] {b}dez metros por segundo, trinta e seis quilômetros por hora. [p=0.3] {c}A vinte metros por segundo: vê ao quadrado sobre erre é quatrocentos dividido por dez, quarenta. [p=0.3] {d}Ene mais seiscentos é igual a sessenta vezes quarenta, dois mil e quatrocentos. [p=0.2] {e}Ene vale mil e oitocentos newtons."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}marque o centro; [p=0.2] {b}força para o centro entra com mais, para fora com menos; [p=0.2] e {c}no topo do looping, vê mínimo é a raiz de gê vezes erre."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar tudo isso: [p=0.2] {b}atrito, rampas, blocos ligados e curvas, [p=0.2] em questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
