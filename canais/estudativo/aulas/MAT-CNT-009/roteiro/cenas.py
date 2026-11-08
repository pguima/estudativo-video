# Estudativo · MAT-CNT-009 — Combinações em problemas de escolha (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: formar uma comissão com 2 de 5 homens e 2 de 4 mulheres (60) e resolver "pelo menos um" pelo total menos o que não serve.
# Pré-requisitos: MAT-CNT-008 (combinação), MAT-CNT-002 (etapas multiplicam, casos somam). Próxima: MAT-CNT-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questão inédita, criada para esta aula.

TITULO = "Combinações em problemas de escolha"

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
    dict(id="s01", block="gancho", text="Uma comissão com {a}dois homens, escolhidos entre cinco, [p=0.2] e {b}duas mulheres, escolhidas entre quatro. [p=0.3] Quem soma as escolhas chega em {c}dezesseis. [p=0.2] A resposta certa é {d}sessenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta comissões com regras, [p=0.2] resolve {b}o pelo menos um [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a combinação: [p=0.2] o arranjo dividido pelo fatorial de quantos foram escolhidos. [p=0.3] E {b}duas ideias das casinhas: [p=0.2] {c}etapas que você faz todas se multiplicam, [p=0.2] e {d}casos que não acontecem juntos se somam. [p=0.3] Se faltar alguma, procure no canal."),
    # comissão em etapas
    dict(id="s04", block="etapas", text="Volte à comissão. [p=0.2] Ela é montada {a}em etapas: [p=0.2] {b}escolher os homens [p=0.2] e {c}escolher as mulheres. [p=0.3] Você faz todas as etapas, então {d}multiplique."),
    dict(id="s05", block="etapas", text="{a}Homens: dois entre cinco. [p=0.2] Ordem não importa, é combinação. [p=0.2] {b}Cinco vezes quatro dá vinte. [p=0.2] {c}Dividido por dois fatorial dá dez."),
    dict(id="s06", block="etapas", text="{a}Mulheres: duas entre quatro. [p=0.2] {b}Quatro vezes três dá doze. [p=0.2] {c}Dividido por dois fatorial dá seis."),
    dict(id="s07", block="etapas", text="Cada dupla de homens {a}combina com cada dupla de mulheres. [p=0.2] {b}Dez vezes seis dá sessenta comissões. [p=0.3] Somar daria dezesseis, [p=0.2] que é só {c}quantas duplas existem, sem formar comissão nenhuma."),
    # pelo menos uma
    dict(id="s08", block="pelomenos", text="Agora, o {a}pelo menos um. [p=0.2] O mesmo grupo: {b}cinco homens e quatro mulheres, nove pessoas. [p=0.3] Quantas comissões de {c}três pessoas têm pelo menos uma mulher? [p=0.3] No total, sem regra nenhuma, são {d}três entre nove: [p=0.2] nove vezes oito vezes sete dá quinhentos e quatro, [p=0.2] e dividido por três fatorial dá {e}oitenta e quatro."),
    dict(id="s09", block="pelomenos", text="Pelo menos uma quer dizer {a}uma, [p=0.2] {b}duas [p=0.2] ou {c}três mulheres. [p=0.3] Cada comissão cai em um caso só, [p=0.2] então {d}conte cada caso e some."),
    dict(id="s10", block="pelomenos", text="{a}Uma mulher: quatro opções, [p=0.2] e dois homens entre cinco, que dá dez. [p=0.2] {b}Quatro vezes dez dá quarenta. [p=0.3] {c}Duas mulheres: seis duplas, [p=0.2] vezes cinco opções de homem, [p=0.2] {d}dá trinta. [p=0.3] {e}Três mulheres: só quatro comissões, [p=0.2] porque escolher três entre quatro é deixar uma de fora."),
    dict(id="s11", block="pelomenos", text="{a}Quarenta mais trinta dá setenta. [p=0.2] {b}Mais quatro dá setenta e quatro comissões."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}garantir uma mulher e completar com qualquer pessoa. [p=0.2] {b}Quatro opções de mulher, [p=0.2] vezes duas pessoas entre as oito que sobram, que dá vinte e oito. [p=0.2] {c}Quatro vezes vinte e oito dá cento e doze. [p=0.3] Mais que {d}o total, que é oitenta e quatro! [p=0.3] A comissão {e}Ana, Bia e Caio foi contada duas vezes: [p=0.2] uma com Ana garantida, outra com Bia garantida."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}conte tudo e tire o que não serve. [p=0.3] O contrário de pelo menos uma mulher é {b}nenhuma mulher: [p=0.2] só homens. [p=0.2] {c}Três homens entre cinco é deixar dois de fora: [p=0.2] cinco vezes quatro dividido por dois dá dez. [p=0.3] {d}Oitenta e quatro menos dez dá setenta e quatro. [p=0.2] O mesmo resultado, em uma linha."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada comissão ou tem mulher, ou não tem. [p=0.3] Compensa sempre que aparece {b}pelo menos um: [p=0.2] o que não serve é um caso só, o nenhum. [p=0.3] {c}Não compensa quando a pergunta é exata, como exatamente uma mulher: [p=0.2] aí, {d}conte direto, que dá quarenta."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um grupo tem {a}quatro professores e seis alunos. [p=0.3] {b}Quantas comissões de dois professores e dois alunos existem? [p=0.2] E {c}quantas comissões de três pessoas têm pelo menos um professor?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Professores: {a}quatro vezes três dividido por dois dá seis. [p=0.2] Alunos: {b}seis vezes cinco dividido por dois dá quinze. [p=0.2] As etapas se multiplicam: {c}seis vezes quinze dá noventa comissões."),
    dict(id="s18", block="resposta", text="No pelo menos um, {a}conte tudo: três entre dez. [p=0.2] Dez vezes nove vezes oito dá setecentos e vinte, [p=0.2] {b}e dividido por seis dá cento e vinte. [p=0.3] O que não serve: {c}nenhum professor, só alunos. [p=0.2] Três entre seis: {d}seis vezes cinco vezes quatro dividido por seis dá vinte. [p=0.3] {e}Cento e vinte menos vinte dá cem. [p=0.3] Faz sentido: a parte que serve é menor que o total."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}grupos diferentes são etapas: multiplique as combinações. [p=0.2] {b}Pelo menos um? Conte tudo e tire o nenhum."),
    dict(id="s20", block="fim", text="Na próxima aula, é a sua vez de praticar: [p=0.2] você vai {a}decidir se multiplica, permuta, arranja ou combina, [p=0.2] em problemas {b}com regras no meio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
