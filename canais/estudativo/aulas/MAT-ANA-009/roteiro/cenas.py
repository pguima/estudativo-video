# Estudativo · MAT-ANA-009 — Equação geral: completar quadrados (Matemática · Geometria Analítica).
# Habilidade: transformar x² + y² − 4x + 2y − 4 = 0 na forma reduzida (x − 2)² + (y + 1)² = 9 e achar o centro (2, −1) e o raio 3.
# Pré-requisitos: MAT-ANA-008 (equação reduzida), MAT-FAT-003 (trinômio quadrado perfeito). Próxima: MAT-ANA-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: equações em passos (agrupar, completar, somar dos dois lados); no fim, a circunferência de centro (2, −1) e raio 3 no plano.

TITULO = "Equação geral da circunferência: completar quadrados"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado mais ípsilon ao quadrado menos quatro xis mais dois ípsilon menos quatro igual a zero. [p=0.3] É uma circunferência. [p=0.2] Mas {b}onde está o centro? [p=0.3] Não dá para ver, porque os quadrados estão {c}desmontados."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta os quadrados de volta, [p=0.2] {b}acha o centro e o raio [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}a equação reduzida: xis menos á, ao quadrado, mais ípsilon menos bê, ao quadrado, igual a érre ao quadrado, [p=0.2] com o centro em á e bê, e érre como raio; [p=0.2] e {c}o quadrado da diferença: o primeiro ao quadrado, menos duas vezes o primeiro vezes o segundo, mais o segundo ao quadrado. [p=0.2] Na soma, o termo do meio vem com mais. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="De onde vem uma equação dessas? [p=0.2] Abra {a}xis menos dois, ao quadrado: [p=0.2] dá {b}xis ao quadrado menos quatro xis mais quatro. [p=0.3] Abra {c}ípsilon mais um, ao quadrado: [p=0.2] dá {d}ípsilon ao quadrado mais dois ípsilon mais um."),
    dict(id="s05", block="origem", text="Some tudo e iguale a {a}nove. [p=0.2] Tirando nove dos dois lados, os números soltos viram {b}quatro mais um menos nove, que dá menos quatro. [p=0.3] É {c}a equação do começo. [p=0.2] Ela é a circunferência da aula anterior, {d}com os parênteses abertos."),
    dict(id="s06", block="metodo", text="Então o caminho é {a}o contrário: montar os quadrados de volta. [p=0.2] Isso se chama {b}completar quadrados, [p=0.2] e tem {c}três passos."),
    # passo um
    dict(id="s07", block="metodo", text="{a}Passo um: junte o xis com o xis, o ípsilon com o ípsilon, [p=0.2] e {b}leve o número solto para a direita. [p=0.3] Somando quatro dos dois lados: [p=0.2] {c}xis ao quadrado menos quatro xis, mais ípsilon ao quadrado mais dois ípsilon, igual a quatro."),
    # passo dois
    dict(id="s08", block="metodo", text="{a}Passo dois: complete cada quadrado. [p=0.2] Em xis ao quadrado menos quatro xis, {b}falta um número para virar quadrado perfeito. [p=0.3] {c}Pegue o número que acompanha o xis: menos quatro. [p=0.2] {d}A metade dá menos dois. [p=0.2] {e}O quadrado de menos dois dá quatro. [p=0.2] Com mais quatro, fica {f}xis menos dois, ao quadrado."),
    dict(id="s09", block="metodo", text="Por que a metade? [p=0.2] No quadrado da diferença, o termo do meio é {a}duas vezes xis vezes o número de dentro. [p=0.2] No menos quatro xis, {b}o quatro é o dobro desse número. [p=0.2] A metade devolve {c}o número de dentro do parêntese: o dois."),
    dict(id="s10", block="metodo", text="No ípsilon é igual. [p=0.2] O número que acompanha o ípsilon é dois: {a}a metade dá um, [p=0.2] e {b}um ao quadrado dá um. [p=0.2] Com mais um, fica {c}ípsilon mais um, ao quadrado."),
    # passo três
    dict(id="s11", block="metodo", text="{a}Passo três: o que você somou na esquerda, some na direita também. [p=0.2] Foram {b}quatro e um. [p=0.2] {c}Quatro mais quatro mais um dá nove. [p=0.3] Ficou {d}xis menos dois, ao quadrado, mais ípsilon mais um, ao quadrado, igual a nove. [p=0.2] Centro {e}xis dois, ípsilon menos um, [p=0.2] e raio {f}três."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}completar só do lado esquerdo. [p=0.2] A pessoa soma quatro e um para montar os parênteses, [p=0.2] mas {b}deixa só o quatro na direita. [p=0.3] Acha {c}raio dois, a raiz de quatro. [p=0.2] Só que somar de um lado só {d}muda a equação. [p=0.2] É como uma balança: {e}o que entra de um lado entra do outro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}centro e raio direto da equação aberta. [p=0.3] {b}Cada coordenada do centro é a metade do número que acompanha a letra, com o sinal trocado. [p=0.2] Menos quatro xis dá {c}xis do centro igual a dois. [p=0.2] Mais dois ípsilon dá {d}ípsilon do centro igual a menos um."),
    dict(id="s14", block="atalho", text="E o raio: {a}eleve ao quadrado cada coordenada do centro, some, e tire o número solto. [p=0.2] {b}Dois ao quadrado dá quatro. [p=0.2] O quadrado de menos um dá um. [p=0.2] {c}Quatro mais um dá cinco. [p=0.3] O número solto é menos quatro, e tirar menos quatro é somar quatro: [p=0.2] {d}cinco mais quatro dá nove. [p=0.2] {e}Raio três."),
    dict(id="s15", block="atalho", text="Funciona porque {a}são os mesmos três passos, feitos de uma vez. [p=0.3] {b}Não compensa usar direto quando xis ao quadrado e ípsilon ao quadrado vêm com um número na frente, [p=0.2] como {c}dois xis ao quadrado mais dois ípsilon ao quadrado. [p=0.2] Aí, {d}divida a equação inteira por esse número antes."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Xis ao quadrado mais ípsilon ao quadrado mais oito xis menos seis ípsilon igual a zero. [p=0.3] {b}Qual é o centro, e qual é o raio?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Não tem número solto: {a}a direita começa em zero. [p=0.3] No xis: {b}a metade de oito dá quatro, e quatro ao quadrado dá dezesseis. [p=0.2] No ípsilon: {c}a metade de menos seis dá menos três, e o quadrado de menos três dá nove."),
    dict(id="s19", block="resposta", text="Somando dezesseis e nove dos dois lados: [p=0.2] {a}xis mais quatro, ao quadrado, mais ípsilon menos três, ao quadrado, igual a vinte e cinco. [p=0.3] Centro {b}xis menos quatro, ípsilon três. [p=0.2] Raio {c}cinco. [p=0.3] Pelo atalho: {d}dezesseis mais nove menos zero dá vinte e cinco. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a metade do número da letra, ao quadrado, completa o quadrado, [p=0.2] e {b}o que entra de um lado entra do outro."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre se {a}um ponto está dentro, fora ou em cima da circunferência, [p=0.2] e se {b}uma reta corta, só encosta ou passa longe, [p=0.2] com {c}a conta do delta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
