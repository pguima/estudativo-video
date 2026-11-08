# Estudativo · MAT-CNT-011 — Probabilidade: favoráveis sobre possíveis (Matemática · Contagem e Probabilidade · Probabilidade: noções).
# Habilidade: montar o espaço amostral de um dado e dizer que a chance de sair número par é 3/6, ou 1/2, ou 50%.
# Pré-requisitos: MAT-CON-001 (conjuntos), MAT-FRA-003 (simplificar), MAT-POR-001 (porcentagem). Próxima: MAT-CNT-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. A ficha não inclui as aulas de contagem: nenhuma conta usa casinhas, fatorial ou combinação.

TITULO = "Probabilidade: favoráveis sobre possíveis"

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
    dict(id="s01", block="gancho", text="{a}Você joga um dado. [p=0.2] Qual a chance de sair {b}número par? [p=0.3] Dá para responder de três jeitos, [p=0.2] e todos estão certos: [p=0.2] {c}três sextos. [p=0.2] {d}Um meio. [p=0.2] Ou {e}cinquenta por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a chance de um resultado [p=0.2] e leva um {b}atalho para passar a chance para porcentagem."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}conjunto, escrito entre chaves, [p=0.2] {c}simplificar fração [p=0.2] e {d}porcentagem, que é uma fração com cem embaixo. [p=0.3] Se faltar alguma, procure no canal."),
    # espaço amostral e evento
    dict(id="s04", block="dado", text="Primeiro, liste {a}tudo o que pode acontecer. [p=0.2] No dado, são {b}um, [p=0.2] dois, [p=0.2] três, [p=0.2] quatro, [p=0.2] cinco e seis. [p=0.3] Esse conjunto tem nome: {c}espaço amostral. [p=0.2] Ele tem {d}seis elementos."),
    dict(id="s05", block="dado", text="Agora, {a}o que você quer que aconteça. [p=0.2] Número par: {b}dois, [p=0.2] quatro e seis. [p=0.3] Isso se chama {c}evento. [p=0.2] Repare: {d}o evento está contido no espaço amostral. [p=0.2] Ele é um pedaço dele."),
    # regra
    dict(id="s06", block="regra", text="A probabilidade é {a}uma fração. [p=0.2] {b}Em cima, quantos resultados servem: os favoráveis. [p=0.2] {c}Embaixo, quantos podem acontecer: os possíveis. [p=0.3] Número par no dado: {d}três favoráveis em seis possíveis. [p=0.2] Três sextos."),
    dict(id="s07", block="regra", text="{a}Três sextos simplifica: [p=0.2] divida em cima e embaixo por três, [p=0.2] e dá {b}um meio. [p=0.3] E um meio é {c}cinquenta em cada cem: [p=0.2] {d}cinquenta por cento. [p=0.3] Três respostas, a mesma chance: [p=0.2] metade dos resultados serve."),
    dict(id="s08", block="regra", text="Só tem um cuidado: [p=0.2] a regra vale quando {a}todos os resultados têm a mesma chance. [p=0.3] É o caso do {b}dado sem truque, [p=0.2] o que se chama de dado honesto. [p=0.2] Num {c}dado viciado, que cai mais no seis, [p=0.2] a conta não vale."),
    # limites
    dict(id="s09", block="limites", text="A chance vai de {a}zero a um. [p=0.3] Sair sete no dado: [p=0.2] nenhum resultado serve, [p=0.2] o evento é {b}o conjunto vazio, [p=0.2] e a chance é {c}zero sextos, que dá zero. [p=0.2] É um {d}evento impossível."),
    dict(id="s10", block="limites", text="Sair um número de um a seis: [p=0.2] todos servem. [p=0.2] {a}Seis sextos dá um. [p=0.2] Ou seja, {b}cem por cento. [p=0.2] É um {c}evento certo. [p=0.3] Se a sua conta passar de um, {d}tem erro nela."),
    # saco de bolas
    dict(id="s11", block="bolas", text="Outro exemplo. [p=0.2] Num saco, há {a}três bolas azuis, [p=0.2] {b}cinco vermelhas [p=0.2] e {c}duas verdes. [p=0.3] Você tira uma sem olhar. [p=0.2] Possíveis: {d}três mais cinco mais dois dá dez bolas."),
    dict(id="s12", block="bolas", text="Chance de azul: {a}três em dez. [p=0.2] Em fração, três décimos. [p=0.3] Chance de vermelha: {b}cinco décimos, [p=0.2] que simplifica para {c}um meio."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}trocar o de baixo. [p=0.2] A pessoa compara {b}as azuis com as que não são azuis: [p=0.2] três contra sete. [p=0.2] E escreve {c}três sétimos. [p=0.3] Mas embaixo vai {d}o total: todas as dez bolas. [p=0.2] As azuis também estão no saco e também podem sair. [p=0.2] O certo é {e}três décimos."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para virar porcentagem: {a}leve o de baixo até cem. [p=0.3] {b}Três décimos: vezes dez em cima e embaixo. [p=0.2] Dá {c}trinta centésimos, ou seja, trinta por cento. [p=0.3] {d}Sete vinte avos: vezes cinco em cima e embaixo. [p=0.2] Dá {e}trinta e cinco por cento."),
    dict(id="s15", block="atalho", text="Funciona porque {a}porcentagem é uma fração com cem embaixo, [p=0.2] e multiplicar em cima e embaixo pelo mesmo número não muda a fração. [p=0.3] {b}Não compensa quando o de baixo não chega em cem, como em um terço: [p=0.2] aí, {c}divida o de cima pelo de baixo, [p=0.2] ou deixe a resposta em fração."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Num dado honesto, qual a chance de sair um número primo? [p=0.3] E numa caixa com {b}cinco bombons de morango, [p=0.2] oito de coco e doze de chocolate, [p=0.2] {c}qual a chance de pegar um de coco, sem olhar? [p=0.2] Responda em fração e em porcentagem."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Número primo tem {a}exatamente dois divisores: [p=0.2] o um e ele mesmo. [p=0.2] No dado, são {b}dois, [p=0.2] três e cinco. [p=0.2] O um não é primo. [p=0.3] {c}Três favoráveis em seis possíveis. [p=0.2] Três sextos simplifica e dá {d}um meio. [p=0.2] Ou {e}cinquenta por cento."),
    dict(id="s19", block="resposta", text="Na caixa, os possíveis: {a}cinco mais oito mais doze dá vinte e cinco. [p=0.2] Favoráveis: {b}oito de coco. [p=0.3] {c}Oito vinte e cinco avos não simplifica. [p=0.2] Vezes quatro em cima e embaixo dá {d}trinta e dois centésimos, [p=0.2] ou seja, trinta e dois por cento."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}probabilidade é favoráveis sobre possíveis, [p=0.2] {b}quando todos os resultados têm a mesma chance."),
    dict(id="s21", block="fim", text="Na próxima aula, os possíveis ficam grandes demais para listar. [p=0.2] Você joga {a}dois dados e acha a chance de a soma dar sete, [p=0.2] e calcula a chance de {b}um sorteio de comissão, [p=0.2] usando a contagem para achar favoráveis e possíveis. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
