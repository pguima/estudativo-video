# Estudativo · MAT-FAV-006 — Calcular a inversa e ver seu gráfico (Matemática · Funções Avançadas · Função composta e inversa).
# Habilidade: achar a inversa de f(x) = 2x + 3, que é (x − 3)/2, e reconhecer o gráfico como o espelho na reta y = x, como 2ˣ e log₂ x.
# Pré-requisitos: MAT-EQU-011 (isolar uma letra), MAT-EXP-013 (log como espelho de 2ˣ), MAT-FAV-005 (bijetora). Próxima: MAT-FAV-007.
# Questão inédita, criada para esta aula. Composta (MAT-FAV-004) fora da ficha: a conferência é por valores, não por f(f⁻¹(x)).
# f(5) = 13 · f⁻¹(13) = (13 − 3)/2 = 5 · passos: y = 2x + 3 → x = 2y + 3 → x − 3 = 2y → y = (x − 3)/2.
# Gráfico: f passa por (0, 3) e (1, 5); f⁻¹ por (3, 0) e (5, 1); f⁻¹(1) = −1 ↔ f(−1) = 1. Espelho na reta y = x.
# Erro: 1/(2x + 3) em 13 = 1/29 (≠ 5).
# Atalho: ×2 e +3 → desfaz −3 e ÷2.
# Questão: f(x) = 4x − 1 → f⁻¹(x) = (x + 1)/4 · f⁻¹(7) = 8/4 = 2 · f(2) = 7.
# Visual: setas de ida (5 → 13) e volta; três passos com passo(); troca de letras com as letras voando; plano −2..8 com f, f⁻¹ e a
#   diagonal tracejada, dobra levando (a, b) em (b, a); miniatura de 2ˣ e log₂ x; palco escuro no atalho (meia e sapato).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; f⁻¹ narrado "éfe à menos um".

TITULO = "Calcular a inversa e ver seu gráfico"

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
    dict(id="s01", block="gancho", text="{a}Éfe de xis é dois xis mais três. [p=0.2] {b}Éfe de cinco dá treze. [p=0.3] Agora, o contrário: {c}saiu treze, qual foi a entrada? [p=0.2] A máquina que responde isso para qualquer número é {d}a função inversa."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a inversa em três passos, [p=0.2] {b}reconhece o gráfico dela [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}só a função bijetora tem inversa; [p=0.2] {b}isolar uma letra numa igualdade; [p=0.2] e {c}o gráfico do logaritmo como espelho do gráfico de dois elevado a xis. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="A inversa de éfe se escreve {a}éfe com um menos um no alto. [p=0.2] {b}Não é expoente: é só o nome da inversa. [p=0.3] Para achar a lei, {c}três passos."),
    dict(id="s05", block="metodo", text="{a}Passo um: troque éfe de xis por ípsilon. [p=0.2] {b}Ípsilon igual a dois xis mais três."),
    dict(id="s06", block="metodo", text="{a}Passo dois: troque as letras. [p=0.2] Onde era xis, ípsilon; onde era ípsilon, xis. [p=0.2] {b}Xis igual a dois ípsilon mais três. [p=0.3] É aqui que a entrada vira saída."),
    dict(id="s07", block="metodo", text="{a}Passo três: isole o ípsilon. [p=0.2] {b}Tire três dos dois lados: xis menos três igual a dois ípsilon. [p=0.2] {c}Divida por dois: ípsilon igual a xis menos três, dividido por dois. [p=0.3] Essa é a inversa: {d}éfe à menos um de xis é xis menos três, sobre dois."),
    dict(id="s08", block="metodo", text="Confira: {a}éfe de cinco dava treze. [p=0.2] {b}Na inversa, treze menos três dá dez, [p=0.2] e dez dividido por dois dá cinco. [p=0.2] {c}Voltou para o cinco."),
    # gráfico
    dict(id="s09", block="grafico", text="E o gráfico? [p=0.2] {a}Éfe passa por xis zero, ípsilon três, [p=0.2] e por {b}xis um, ípsilon cinco. [p=0.3] Na inversa, cada par troca de ordem: [p=0.2] {c}xis três, ípsilon zero, [p=0.2] e {d}xis cinco, ípsilon um."),
    dict(id="s10", block="grafico", text="Trocar xis com ípsilon é {a}refletir na diagonal, a reta ípsilon igual a xis. [p=0.2] {b}Dobre o papel nela, e um gráfico cai em cima do outro. [p=0.3] É o mesmo espelho de {c}dois elevado a xis e do logaritmo na base dois: [p=0.2] {d}o logaritmo é a inversa da exponencial."),
    dict(id="s11", block="grafico", text="E, como xis e ípsilon trocam de papel, {a}o domínio de uma é a imagem da outra."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}ler o menos um como expoente. [p=0.2] A pessoa escreve {b}um sobre dois xis mais três. [p=0.3] Teste com o treze: [p=0.2] {c}dá um sobre vinte e nove, e não cinco. [p=0.2] {d}A inversa desfaz a função: ela não é um dividido pela função."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}desfaça de trás para frente. [p=0.3] Éfe {b}multiplica por dois e depois soma três. [p=0.2] A inversa desfaz na ordem contrária: [p=0.2] {c}primeiro tira três, [p=0.2] {d}depois divide por dois. [p=0.2] {e}Xis menos três, sobre dois, sem passo nenhum."),
    dict(id="s14", block="atalho", text="É como se vestir: {a}você põe a meia e depois o sapato, [p=0.2] mas {b}tira primeiro o sapato. [p=0.3] {c}O atalho só compensa quando o xis aparece uma vez só. [p=0.2] {d}Com o xis em dois lugares, use os três passos."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Éfe de xis é quatro xis menos um. [p=0.3] {b}Ache a inversa [p=0.2] e {c}calcule éfe à menos um de sete."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Ípsilon igual a quatro xis menos um. [p=0.2] {b}Troque: xis igual a quatro ípsilon menos um. [p=0.2] {c}Some um: xis mais um igual a quatro ípsilon. [p=0.2] {d}Divida por quatro: ípsilon igual a xis mais um, sobre quatro."),
    dict(id="s18", block="resposta", text="Pelo atalho, dá o mesmo: [p=0.2] éfe multiplica por quatro e tira um, [p=0.2] então a inversa {a}soma um e divide por quatro. [p=0.3] {b}Éfe à menos um de sete: sete mais um, oito; oito dividido por quatro, dois. [p=0.2] Confira: {c}quatro vezes dois, menos um, dá sete."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}troque as letras e isole o ípsilon; [p=0.2] {b}a inversa desfaz de trás para frente; [p=0.2] e {c}o gráfico é o espelho na diagonal."),
    dict(id="s20", block="fim", text="Na próxima aula, outro tipo de espelho: [p=0.2] {a}a função par e a função ímpar, [p=0.2] que você reconhece {b}pela simetria do gráfico. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
