# Estudativo · MAT-CNT-013 — Evento complementar: o que não pode acontecer (Matemática · Contagem e Probabilidade · Probabilidade: noções).
# Habilidade: calcular a chance de sair pelo menos uma cara em 3 moedas como 1 − 1/8 = 7/8.
# Pré-requisitos: MAT-CNT-012 (probabilidade com contagem), MAT-CON-002 (complementar). Próxima: MAT-CNT-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, pê).
# Questão inédita, criada para esta aula. Mesmos termos de MAT-CNT-001 e 011: casinhas, árvore de possibilidades, espaço amostral, favoráveis sobre possíveis.
# 3 moedas: 2 × 2 × 2 = 8 (E.arvore 3 níveis, cara/coroa; só a ponta coroa-coroa-coroa fora) · 8 − 1 = 7 → 7/8 = 87,5%.
# Na tela: P(A) = 1 − P(Ā) (complementar com traço, como em MAT-CON-002); 1 = 8/8; 8/8 − 1/8 = 7/8.
# Chute em 2 questões de 5 alternativas: 5 × 5 = 25 · errar ambas 4 × 4 = 16 · 25 − 16 = 9 → 9/25 = 36%.
# Erro: "exatamente uma" = 3/8 (Ca-Co-Co, Co-Ca-Co, Co-Co-Ca). Atalho: "pelo menos um" → 1 − P(nenhum); não compensa em "três caras" = 1/8.
# Questão: 2 dados, pelo menos um seis: 36 · nenhum 5 × 5 = 25 · 36 − 25 = 11 → 11/36 (< 1/3). Erro "nenhum = 1 caso": 35/36.

TITULO = "Evento complementar: o que não pode acontecer"

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
    dict(id="s01", block="gancho", text="Você lança {a}três moedas. [p=0.3] Qual a chance de sair {b}pelo menos uma cara? [p=0.3] Listar todos os jeitos cansa. [p=0.2] Mas só existe {c}um resultado sem cara nenhuma. [p=0.3] E ele resolve a questão em uma linha: [p=0.2] a chance dá {d}sete oitavos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula chances pelo lado contrário, [p=0.2] sabe {b}quando isso economiza tempo [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}probabilidade é favoráveis sobre possíveis, [p=0.2] e {c}o complementar de um conjunto: o que está no universo e fica fora dele. [p=0.3] Se faltar alguma, procure no canal."),
    # espaço amostral
    dict(id="s04", block="moedas", text="Primeiro, o espaço amostral: {a}todos os resultados possíveis. [p=0.2] Cada moeda tem {b}duas faces, cara ou coroa. [p=0.2] São {c}três casinhas com duas opções cada: [p=0.2] {d}dois vezes dois vezes dois dá oito resultados."),
    dict(id="s05", block="moedas", text="Na árvore de possibilidades, são {a}oito pontas. [p=0.2] Pelo menos uma cara quer dizer {b}uma, [p=0.2] duas [p=0.2] ou três caras. [p=0.3] Só {c}uma ponta fica de fora: [p=0.2] {d}coroa, coroa, coroa."),
    dict(id="s06", block="moedas", text="Então os favoráveis são {a}oito menos um, que dá sete. [p=0.2] A chance é {b}sete oitavos. [p=0.3] Repare: você {c}não contou o que pode acontecer. [p=0.2] {d}Contou o que não pode, e tirou do total."),
    # regra
    dict(id="s07", block="regra", text="Esse lado contrário tem nome: {a}evento complementar. [p=0.3] É o mesmo complementar dos conjuntos, [p=0.2] e o universo é {b}o espaço amostral. [p=0.3] O evento é {c}pelo menos uma cara. [p=0.2] O complementar é {d}tudo que fica fora dele: nenhuma cara."),
    dict(id="s08", block="regra", text="Um evento e o seu complementar {a}dividem o espaço amostral inteiro: [p=0.2] ou acontece um, ou acontece o outro. [p=0.3] Juntas, as chances somam {b}oito oitavos, que é um inteiro: [p=0.2] {c}cem por cento, a certeza."),
    dict(id="s09", block="regra", text="Daí sai a regra: [p=0.2] {a}a chance do evento é um menos a chance do complementar. [p=0.3] Na tela, {b}pê de á é a chance do evento á. [p=0.2] {c}Com um traço em cima do á, é a chance do complementar."),
    dict(id="s10", block="regra", text="Nas três moedas: {a}um menos um oitavo. [p=0.2] Um inteiro tem {b}oito oitavos: oito pedaços iguais. [p=0.2] Tirando um pedaço, {c}sobram sete oitavos. [p=0.3] Em por cento, dá {d}oitenta e sete e meio por cento: [p=0.2] quase certeza."),
    # chute
    dict(id="s11", block="chute", text="Agora um caso em que o nenhum tem {a}muitos resultados. [p=0.2] Você chuta {b}duas questões, cada uma com cinco alternativas e só uma certa. [p=0.3] Qual a chance de acertar {c}pelo menos uma?"),
    dict(id="s12", block="chute", text="Possíveis: {a}cinco vezes cinco dá vinte e cinco. [p=0.3] O complementar é {b}errar ambas. [p=0.2] Cada questão tem {c}quatro alternativas erradas: [p=0.2] {d}quatro vezes quatro dá dezesseis jeitos de errar tudo."),
    dict(id="s13", block="chute", text="A chance de errar tudo é {a}dezesseis vinte e cinco avos. [p=0.2] Tire do inteiro: [p=0.2] {b}vinte e cinco menos dezesseis dá nove. [p=0.3] A chance de acertar pelo menos uma é {c}nove vinte e cinco avos, [p=0.2] que dá {d}trinta e seis por cento."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é ler pelo menos uma como {a}exatamente uma. [p=0.2] Nas três moedas, a pessoa conta só {b}cara, coroa, coroa; [p=0.2] coroa, cara, coroa; [p=0.2] e coroa, coroa, cara. [p=0.2] Responde {c}três oitavos. [p=0.3] Mas pelo menos uma {d}também aceita duas [p=0.2] ou três caras. [p=0.2] Por isso, {e}sete oitavos."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho. [p=0.2] Viu {a}pelo menos um, [p=0.2] {b}no mínimo um [p=0.2] ou {c}algum? [p=0.3] {d}Calcule a chance do nenhum e tire de um."),
    dict(id="s16", block="atalho", text="Funciona porque o nenhum costuma ser {a}um grupo pequeno e fácil de contar, [p=0.2] enquanto o pelo menos um se espalha em vários casos. [p=0.3] {b}Não compensa quando o próprio evento já é pequeno, [p=0.2] como {c}sair três caras: [p=0.2] é uma ponta só, [p=0.2] {d}um oitavo, direto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Você lança {a}dois dados comuns, de seis faces. [p=0.3] {b}Qual a chance de sair pelo menos um seis?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Possíveis: {a}seis vezes seis dá trinta e seis. [p=0.3] O complementar é {b}nenhum seis. [p=0.2] Cada dado tem {c}cinco faces que não são seis: [p=0.2] {d}cinco vezes cinco dá vinte e cinco."),
    dict(id="s20", block="resposta", text="Os favoráveis: {a}trinta e seis menos vinte e cinco dá onze. [p=0.2] A chance é {b}onze trinta e seis avos, [p=0.2] um pouco menos que um terço. [p=0.3] Quem achou que nenhum seis era um caso só [p=0.2] respondeu {c}trinta e cinco trinta e seis avos, [p=0.2] e errou feio."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o complementar é tudo que fica fora do evento. [p=0.3] {b}Pelo menos um? Calcule o nenhum e tire de um."),
    dict(id="s22", block="fim", text="Na próxima aula, a palavra ou entra na probabilidade: [p=0.2] a chance de tirar do baralho {a}um rei ou uma carta de copas, [p=0.2] sem contar {b}o rei de copas duas vezes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
