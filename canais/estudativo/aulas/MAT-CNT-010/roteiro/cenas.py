# Estudativo · MAT-CNT-010 — Praticando: contagem (Matemática · Contagem e Probabilidade · prática).
# Habilidade: decidir se multiplica, permuta, arranja ou combina e resolver problemas com restrição.
# Pré-requisitos: MAT-CNT-001 a MAT-CNT-009. Próxima: MAT-CNT-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial"; letras narradas como se falam (pê, erre, á, tê, ó).
# Questões inéditas, criadas para esta aula.

TITULO = "Praticando: contagem"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula. [p=0.2] Em cada uma, a decisão vem antes da conta: [p=0.2] {b}multiplico, permuto, arranjo ou combino? [p=0.3] {c}Pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes de cada conta, {a}faça o teste. [p=0.2] Etapas de coisas diferentes, como camisa e calça? [p=0.2] {b}Casinhas, e multiplique. [p=0.2] Todos entram em fila? [p=0.2] {c}Permutação. [p=0.2] Só alguns, e trocar a ordem muda? [p=0.2] {d}Arranjo. [p=0.2] Só alguns, e a ordem não muda nada? [p=0.2] {e}Combinação. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: casinhas com restrição
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Quantos números de quatro algarismos diferentes são ímpares?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] São casinhas com regra. [p=0.2] {a}Comece pela mais difícil: a unidade. [p=0.2] Número ímpar termina em {b}um, [p=0.2] três, [p=0.2] cinco, [p=0.2] sete ou nove: [p=0.2] {c}cinco opções."),
    dict(id="s06", block="resposta1", text="Depois, {a}a casinha da frente. [p=0.2] Ela não aceita o zero nem o algarismo da unidade: [p=0.2] {b}oito opções. [p=0.2] As outras aceitam o zero, mas não os já usados: [p=0.2] {c}oito [p=0.2] e {d}sete. [p=0.3] {e}Cinco vezes oito dá quarenta. [p=0.2] {f}Vezes oito dá trezentos e vinte. [p=0.2] {g}Vezes sete dá dois mil duzentos e quarenta números. [p=0.3] Se você começasse pela casinha da frente, {h}a unidade travaria: [p=0.2] as opções dela dependeriam de a frente ter usado um ímpar ou um par."),
    # situação 2: permutação com restrição
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] {b}Quantos anagramas da palavra prato começam com vogal?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Todas as letras entram, e são diferentes: {a}permutação. [p=0.3] Prato tem {b}pê, erre, á, tê, ó. [p=0.2] A primeira casinha tem regra: [p=0.2] só aceita {c}á ou ó. [p=0.2] Duas opções. [p=0.3] As outras quatro letras se arrumam no resto: [p=0.2] {d}quatro fatorial dá vinte e quatro. [p=0.2] {e}Duas vezes vinte e quatro dá quarenta e oito anagramas. [p=0.3] Sem a regra, seriam {f}cinco fatorial, que dá cento e vinte. [p=0.2] Com regra, a resposta tem que ser menor: bateu."),
    # situação 3: arranjo
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um campeonato tem {b}doze times. [p=0.3] {c}Quantas possibilidades existem para campeão e vice?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] O teste da troca: {a}time Azul campeão e time Verde vice [p=0.2] é diferente do contrário. [p=0.2] {b}A ordem importa: arranjo. [p=0.3] Dois lugares, dois números descendo do doze: [p=0.2] {c}doze vezes onze dá cento e trinta e dois."),
    dict(id="s13", block="resposta3", text="Quem trata como combinação divide por dois [p=0.2] e responde {a}sessenta e seis. [p=0.2] Isso conta só {b}quais times chegam à final, [p=0.2] sem dizer quem ganhou. [p=0.3] Campeão e vice são {c}lugares diferentes, como ouro e prata no pódio."),
    # situação 4: combinação com atalho
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Uma salada leva {b}quatro frutas diferentes, [p=0.2] escolhidas entre {c}sete frutas. [p=0.3] {d}Quantas saladas diferentes dá para fazer?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] Banana com maçã é a mesma salada que maçã com banana: {a}combinação. [p=0.3] Use o atalho: {b}escolher quatro que entram é escolher três que ficam de fora. [p=0.2] {c}Sete vezes seis vezes cinco dá duzentos e dez. [p=0.2] {d}Dividido por três fatorial dá trinta e cinco saladas. [p=0.3] Pela conta direta, {e}sete vezes seis vezes cinco vezes quatro dá oitocentos e quarenta, [p=0.2] e dividido por quatro fatorial {f}dá trinta e cinco também. [p=0.2] Mesma resposta, com uma conta maior."),
    # situação 5: combinação com obrigatórias
    dict(id="s17", block="questao5", text="{a}Última situação, e ela tem uma regra no meio. [p=0.2] Uma prova tem {b}dez questões, [p=0.2] e o aluno deve escolher {c}sete para responder. [p=0.3] {d}A primeira e a segunda questão são obrigatórias. [p=0.2] {e}De quantos jeitos ele pode escolher as sete?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] A ordem de escolha não importa: {a}combinação. [p=0.3] E as obrigatórias {b}já estão dentro. [p=0.2] Sobram {c}cinco escolhas entre as oito questões restantes. [p=0.3] Cinco entre oito é deixar três de fora: [p=0.2] {d}oito vezes sete vezes seis dá trezentos e trinta e seis. [p=0.2] {e}Dividido por três fatorial dá cinquenta e seis."),
    dict(id="s20", block="resposta5", text="Quem esquece a regra faz {a}sete entre dez [p=0.2] e responde {b}cento e vinte. [p=0.3] Essa conta inclui {c}escolhas que deixam de fora uma questão obrigatória. [p=0.2] Regra de que algo tem que entrar? [p=0.2] {d}Coloque dentro primeiro e escolha só o resto."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}antes da conta, decida: [p=0.2] etapas, fila, ordem que importa ou ordem que não importa. [p=0.3] {b}Tem regra? Comece por ela."),
    dict(id="s22", block="fim", text="Na próxima aula, começa um assunto novo: {a}probabilidade. [p=0.2] Você vai dizer {b}qual a chance de sair número par num dado, [p=0.2] em fração e em porcentagem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
