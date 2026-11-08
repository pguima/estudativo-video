# Estudativo · MAT-MTZ-009 — Praticando: sistemas lineares (Matemática · Matrizes e Sistemas · prática).
# Habilidade: resolver e discutir sistemas de até 3 equações e 3 incógnitas.
# Pré-requisitos: MAT-MTZ-006, MAT-MTZ-007, MAT-MTZ-008. Próxima: nenhuma (última da trilha).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Cinco questões inéditas, criadas para esta aula. Letras narradas "xis", "ípsilon", "zê" e "cá".

TITULO = "Praticando: sistemas lineares"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # abertura
    dict(id="s01", block="gancho", text="{a}Cinco questões de sistemas lineares, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}o escalonamento, uma letra por vez; [p=0.2] {b}a última linha da escada, que diz se há uma, infinitas ou nenhuma solução; [p=0.2] {c}a regra de Cramer, com cada letra igual ao seu determinante dividido por D; [p=0.2] e {d}a conferência no fim. [p=0.3] Se faltar alguma, procure no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Resolva: [p=0.2] {b}xis mais ípsilon mais zê igual a nove; [p=0.2] {c}xis menos ípsilon mais zê igual a três; [p=0.2] {d}dois xis mais ípsilon menos zê igual a três."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Repare: {a}a primeira e a segunda só são diferentes no ípsilon. [p=0.3] {b}Primeira menos segunda: o xis e o zê somem juntos, [p=0.2] e sobra {c}dois ípsilon igual a seis: [p=0.2] ípsilon igual a três."),
    dict(id="s06", block="resposta1", text="Ponha ípsilon igual a três nas outras. [p=0.2] {a}Na primeira: xis mais zê igual a seis. [p=0.2] {b}Na terceira: dois xis menos zê igual a zero. [p=0.3] {c}Somando as duas, o zê some: [p=0.2] três xis igual a seis, e xis igual a dois. [p=0.2] {d}Então, zê é quatro. [p=0.3] A solução é {e}dois, três, quatro."),
    # atalho
    dict(id="s07", block="atalho", text="Agora o atalho que apareceu aqui: [p=0.2] {a}procure duas equações quase iguais. [p=0.3] {b}Subtraindo uma da outra, várias letras somem de uma vez. [p=0.2] Na questão um, {c}uma subtração só já deu o ípsilon."),
    dict(id="s08", block="atalho", text="Funciona porque {a}o que é igual nas duas se cancela. [p=0.3] {b}Se nenhuma dupla for parecida, [p=0.2] volte ao caminho de sempre: tire o xis das outras."),
    # questão 2
    dict(id="s09", block="questao2", text="{a}Questão dois. [p=0.2] Numa lanchonete, {b}um suco, um sanduíche e um doce custam dezenove reais. [p=0.2] {c}Dois sucos e um sanduíche custam dezoito. [p=0.2] {d}Um sanduíche e três doces custam vinte e cinco. [p=0.3] {e}Quanto custa cada um?"),
    dict(id="s10", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta2", text="Vamos lá. [p=0.2] {a}Suco é xis, sanduíche é ípsilon, doce é zê. [p=0.3] {b}Xis mais ípsilon mais zê igual a dezenove; [p=0.2] {c}dois xis mais ípsilon igual a dezoito; [p=0.2] {d}ípsilon mais três zê igual a vinte e cinco."),
    dict(id="s12", block="resposta2", text="{a}Segunda menos duas vezes a primeira: [p=0.2] menos ípsilon menos dois zê igual a menos vinte. [p=0.2] Trocando todos os sinais, {b}ípsilon mais dois zê igual a vinte. [p=0.3] {c}A terceira menos essa: zê igual a cinco. [p=0.2] {d}Ípsilon mais dez igual a vinte: ípsilon igual a dez. [p=0.2] {e}Xis mais dez mais cinco igual a dezenove: xis igual a quatro."),
    dict(id="s13", block="resposta2", text="{a}Suco, quatro reais; sanduíche, dez; doce, cinco. [p=0.3] {b}Conferindo: dois sucos e um sanduíche, oito mais dez, dezoito. [p=0.2] Bateu."),
    # questão 3
    dict(id="s14", block="questao3", text="{a}Questão três. [p=0.2] {b}Para que valor de cá o sistema fica sem solução? [p=0.3] {c}Xis mais ípsilon mais zê igual a um; [p=0.2] {d}xis mais dois ípsilon mais zê igual a dois; [p=0.2] {e}dois xis mais três ípsilon mais cá zê igual a cinco."),
    dict(id="s15", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta3", text="{a}Segunda menos primeira: ípsilon igual a um. [p=0.3] {b}Terceira menos duas vezes a primeira: [p=0.2] ípsilon mais, abre parênteses, cá menos dois, fecha parênteses, vezes zê, igual a três."),
    dict(id="s17", block="resposta3", text="Como ípsilon é um, {a}cá menos dois, vezes zê, igual a dois. [p=0.3] {b}Com cá igual a dois, fica zero igual a dois: impossível. [p=0.3] Resposta: {c}cá igual a dois."),
    # questão 4
    dict(id="s18", block="questao4", text="{a}Questão quatro. [p=0.2] Pela regra de Cramer, {b}ache só o ípsilon: [p=0.2] {c}dois xis mais três ípsilon igual a treze; [p=0.2] {d}xis menos dois ípsilon igual a menos quatro."),
    dict(id="s19", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta4", text="Só uma letra: {a}dois determinantes. [p=0.3] {b}D: dois vezes menos dois, menos três vezes um: [p=0.2] menos quatro menos três, menos sete. [p=0.3] {c}D ípsilon, com a coluna do ípsilon trocada: [p=0.2] dois vezes menos quatro, menos treze vezes um: [p=0.2] menos oito menos treze, menos vinte e um. [p=0.3] {d}Ípsilon: menos vinte e um dividido por menos sete, três."),
    # questão 5
    dict(id="s21", block="questao5", text="{a}Última questão, rápida. [p=0.2] {b}Três planos passam todos pela mesma reta. [p=0.3] {c}O sistema com as equações desses planos tem quantas soluções?"),
    dict(id="s22", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta5", text="{a}Infinitas. [p=0.2] Cada ponto da reta está {b}nos três planos ao mesmo tempo, [p=0.2] e uma reta tem {c}infinitos pontos. [p=0.3] O sistema é {d}possível e indeterminado."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}escalone, uma letra por vez; [p=0.2] {b}procure equações quase iguais; [p=0.2] {c}leia a última linha da escada [p=0.2] e {d}confira sempre."),
    dict(id="s25", block="fim", text="Esta é a última aula da trilha de matrizes e sistemas. [p=0.2] {a}Volte às aulas das questões em que errou, [p=0.2] e {b}inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
