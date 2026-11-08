# Estudativo · MAT-ANA-011 — Praticando: circunferência no plano (Matemática · Geometria Analítica · prática).
# Habilidade: achar centro e raio de uma equação e dizer a posição de pontos e retas.
# Pré-requisitos: MAT-ANA-008, MAT-ANA-009, MAT-ANA-010. Próxima: nenhuma (fecha a trilha e a Matemática do núcleo).
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Visual: plano com cada circunferência (centro (4, −3) raio 7 com a origem; centro (2, 1) passando por (5, 5); centro (1, 3) raio 2 com a reta y = 1; x² + y² = 5 com a reta y = x + 4).

TITULO = "Praticando: circunferência no plano"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações com a circunferência no plano, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}quatro ferramentas: [p=0.2] {b}o centro é o que zera os parênteses, e o raio é a raiz do número da direita; [p=0.2] {c}completar quadrados; [p=0.2] {d}comparar o ponto com érre ao quadrado; [p=0.2] e {e}substituir a reta e olhar o delta. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: ler e posição de ponto
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] A circunferência é {b}xis menos quatro, ao quadrado, mais ípsilon mais três, ao quadrado, igual a quarenta e nove. [p=0.3] {c}Qual é o centro, e qual é o raio? [p=0.2] E {d}a origem está dentro, fora ou em cima dela?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Xis menos quatro zera com quatro. [p=0.2] {b}Ípsilon mais três zera com menos três. [p=0.2] Centro: {c}xis quatro, ípsilon menos três. [p=0.2] Raio: {d}a raiz de quarenta e nove dá sete."),
    dict(id="s06", block="resposta1", text="A origem é {a}xis zero, ípsilon zero. [p=0.2] {b}Zero menos quatro dá menos quatro, e o quadrado dá dezesseis. [p=0.2] {c}Zero mais três dá três, e o quadrado dá nove. [p=0.2] {d}Dezesseis mais nove dá vinte e cinco. [p=0.3] {e}Vinte e cinco é menos que quarenta e nove: a origem está dentro."),
    # situação 2: escrever a partir de centro e ponto
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma circunferência tem centro em {b}xis dois, ípsilon um, [p=0.2] e passa pelo ponto {c}xis cinco, ípsilon cinco. [p=0.3] {d}Qual é a equação reduzida dela?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Falta o raio, e ele é {a}a distância do centro até o ponto. [p=0.3] {b}Nos xis: cinco menos dois dá três. [p=0.2] {c}Nos ípsilons: cinco menos um dá quatro. [p=0.2] {d}Três ao quadrado mais quatro ao quadrado dá vinte e cinco: [p=0.2] esse é {e}o raio ao quadrado."),
    dict(id="s10", block="resposta2", text="A equação: {a}xis menos dois, ao quadrado, mais ípsilon menos um, ao quadrado, igual a vinte e cinco. [p=0.3] {b}O raio é cinco, mas nem precisava tirar a raiz: [p=0.2] a equação pede {c}o raio ao quadrado, e ele já estava pronto."),
    # atalho
    dict(id="s11", block="atalho", text="Esse é um atalho de prova: [p=0.2] {a}quando você acha o raio por uma distância, pare antes da raiz. [p=0.3] Funciona porque {b}Pitágoras entrega a distância ao quadrado, [p=0.2] e é ela que vai do lado direito da equação. [p=0.3] {c}Não compensa quando a questão pergunta o raio, ou o comprimento da volta: [p=0.2] aí, {d}tire a raiz."),
    # situação 3: completar quadrados e reta tangente
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] A circunferência é {b}xis ao quadrado mais ípsilon ao quadrado menos dois xis menos seis ípsilon mais seis igual a zero. [p=0.3] {c}Ache o centro e o raio. [p=0.2] E {d}a reta ípsilon igual a um é secante, tangente ou externa?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] O número solto vai para a direita: {a}menos seis. [p=0.3] No xis: {b}a metade de menos dois dá menos um, e o quadrado de menos um dá um. [p=0.2] No ípsilon: {c}a metade de menos seis dá menos três, e o quadrado de menos três dá nove. [p=0.2] Somando um e nove dos dois lados: {d}menos seis mais um mais nove dá quatro."),
    dict(id="s15", block="resposta3", text="Ficou {a}xis menos um, ao quadrado, mais ípsilon menos três, ao quadrado, igual a quatro. [p=0.2] Centro {b}xis um, ípsilon três, [p=0.2] e raio {c}dois. [p=0.3] Quem esqueceu de somar na direita ficou com {d}menos seis. [p=0.2] Raio ao quadrado negativo é impossível: {e}sinal de que a conta escorregou."),
    dict(id="s16", block="resposta3", text="A reta ípsilon igual a um é {a}deitada. [p=0.2] Do centro até ela, {b}três menos um dá dois passos. [p=0.2] {c}Dois é o raio: tangente. [p=0.3] Pela substituição dá o mesmo: [p=0.2] troque o ípsilon por um, e {d}um menos três, ao quadrado, dá quatro. [p=0.2] Tirando quatro dos dois lados, sobra {e}xis menos um, ao quadrado, igual a zero. [p=0.2] {f}Só o um zera o parêntese: uma raiz só, tangente, no ponto xis um, ípsilon um."),
    # situação 4: reta inclinada
    dict(id="s17", block="questao4", text="{a}Última situação. [p=0.2] A circunferência é {b}xis ao quadrado mais ípsilon ao quadrado igual a cinco, [p=0.2] e a reta é {c}ípsilon igual a xis mais quatro. [p=0.3] {d}A reta é secante, tangente ou externa?"),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] Reta inclinada: {a}substituição e delta. [p=0.2] {b}Xis ao quadrado mais xis mais quatro, ao quadrado, igual a cinco. [p=0.3] Xis mais quatro, ao quadrado, dá {c}xis ao quadrado mais oito xis mais dezesseis. [p=0.2] Juntando e tirando cinco dos dois lados: {d}dois xis ao quadrado mais oito xis mais onze igual a zero."),
    dict(id="s20", block="resposta4", text="{a}Bê ao quadrado: oito ao quadrado dá sessenta e quatro. [p=0.2] {b}Quatro vezes dois vezes onze dá oitenta e oito. [p=0.2] {c}Sessenta e quatro menos oitenta e oito dá menos vinte e quatro. [p=0.3] {d}Delta negativo: nenhum ponto de encontro. [p=0.2] A reta é {e}externa: passa longe."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}monte a equação reduzida, [p=0.2] {b}leia o centro e o raio, [p=0.2] e {c}compare: o ponto com érre ao quadrado, a reta pelo delta."),
    dict(id="s22", block="fim", text="Com esta aula, {a}você fecha a geometria analítica e a sequência principal de Matemática do curso: [p=0.2] {b}dos algarismos até a circunferência no plano. [p=0.3] {c}Se algum passo travou, procure a aula no canal e refaça. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
