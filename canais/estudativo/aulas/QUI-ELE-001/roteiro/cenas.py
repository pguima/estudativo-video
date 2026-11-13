# Estudativo · QUI-ELE-001 — Número de oxidação (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: calcular o Nox do enxofre em H₂SO₄ e do manganês em KMnO₄ somando as cargas até zero.
# Pré-requisitos: QUI-ATO-011, QUI-INO-003, MAT-EQU-008. Próxima: QUI-ELE-002 (oxirredução: quem perde e quem ganha elétrons).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula da trilha: guarda a linguagem visual dela (visual.py).
# Fórmulas lidas letra a letra: H₂SO₄ = "agá dois esse ó quatro", KMnO₄ = "cá eme ene ó quatro", HNO₃ = "agá ene ó três",
# NH₃ = "ene agá três", SO₄²⁻ = "esse ó quatro, dois menos". Questão inédita, criada para esta aula.
# Contas: H₂SO₄: 2(+1) + x + 4(−2) = 0 → x = +6 · KMnO₄: +1 + x − 8 = 0 → x = +7 · SO₄²⁻: x − 8 = −2 → x = +6
# erro (sem multiplicar pelo índice): +1 + x − 2 = 0 → x = +1 · HNO₃: 1 + x − 6 = 0 → +5 · NH₃: x + 3 = 0 → −3.
# Regra do O = −2 "quase sempre": a exceção (água oxigenada, −1) fica dita como existente, sem ser ensinada.

TITULO = "Número de oxidação"

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
    dict(id="s01", block="gancho", text="{a}Agá dois esse ó quatro, o ácido sulfúrico. [p=0.3] Na fórmula, aparecem {b}o número dois e o número quatro. [p=0.3] Mas a prova diz que o enxofre ali vale {c}mais seis. [p=0.3] {d}De onde sai esse seis?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o número de oxidação, o Nox, [p=0.1] de um átomo dentro de uma fórmula, [p=0.2] como o {c}manganês no cá eme ene ó quatro. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Na ligação, o átomo mais eletronegativo puxa os elétrons para perto de si. [p=0.3] E {b}um íon tem carga: [p=0.1] o sódio que perdeu um elétron fica com {c}carga mais um. [p=0.2] Se faltar alguma, procure no canal."),
    # o que é Nox
    dict(id="s04", block="ideia", text="Comece pelo sal de cozinha, o cloreto de sódio. [p=0.2] {a}O sódio entregou um elétron ao cloro. [p=0.2] {b}O sódio ficou com carga mais um, [p=0.1] {c}o cloro, com menos um. [p=0.3] Essas cargas são o número de oxidação de cada um."),
    dict(id="s05", block="ideia", text="E quando ninguém entrega elétron de vez? [p=0.2] No cloreto de hidrogênio, agá cê ele, {a}o hidrogênio e o cloro dividem um par de elétrons. [p=0.3] Mas o cloro é mais eletronegativo: [p=0.1] {b}ele puxa o par para o lado dele."),
    dict(id="s06", block="ideia", text="O Nox finge que o mais eletronegativo {a}levou o par inteiro. [p=0.2] Assim, {b}o hidrogênio fica com mais um, [p=0.1] {c}e o cloro, com menos um. [p=0.3] {d}O Nox é a carga que o átomo teria se cada ligação virasse uma entrega."),
    # regras
    dict(id="s07", block="regras", text="Para calcular, a prova usa quatro regras. [p=0.2] {a}Primeira: numa substância simples, feita de um elemento só, como o gás oxigênio ou o ferro, [p=0.1] o Nox é {b}zero. [p=0.2] Átomos iguais não puxam elétron um do outro."),
    dict(id="s08", block="regras", text="{a}Segunda: num íon de um átomo só, o Nox é a própria carga. [p=0.2] {b}No cobre dois mais, é mais dois."),
    dict(id="s09", block="regras", text="{a}Terceira: alguns valores são fixos. [p=0.2] {b}Sódio e potássio, a família um: mais um. [p=0.2] {c}Hidrogênio ligado a ametal: mais um. [p=0.2] {d}Oxigênio: quase sempre menos dois. [p=0.2] {e}Cloro no fim da fórmula, como no sal: menos um. [p=0.3] {f}A exceção mais famosa, a água oxigenada, é assunto de outra aula."),
    dict(id="s10", block="regras", text="{a}E a quarta, a mais importante: [p=0.1] {b}numa substância, a soma de todos os Nox dá zero, [p=0.2] porque ela não tem carga. [p=0.3] {c}Num íon, a soma dá a carga do íon."),
    # H2SO4
    dict(id="s11", block="sulfurico", text="Volte ao ácido sulfúrico. [p=0.2] {a}O Nox do enxofre é o que você não sabe: {b}xis. [p=0.3] {c}Cada hidrogênio vale mais um, e são dois: [p=0.1] {d}mais dois. [p=0.3] {e}Cada oxigênio vale menos dois, e são quatro: [p=0.1] {f}menos oito."),
    dict(id="s12", block="sulfurico", text="{a}A soma tem que dar zero: [p=0.1] mais dois, mais xis, menos oito, igual a zero. [p=0.3] {b}Juntando os números, xis menos seis igual a zero. [p=0.2] {c}Xis dá mais seis. [p=0.3] {d}Esse é o seis do começo."),
    # KMnO4
    dict(id="s13", block="permanganato", text="Agora o cá eme ene ó quatro, o permanganato de potássio, [p=0.1] {a}um pó roxo usado para desinfetar. [p=0.3] {b}O potássio vale mais um. [p=0.2] {c}Quatro oxigênios: menos oito. [p=0.2] {d}O manganês é o xis."),
    dict(id="s14", block="permanganato", text="{a}Mais um, mais xis, menos oito, igual a zero. [p=0.2] {b}Xis menos sete igual a zero, [p=0.1] {c}e o manganês dá mais sete."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar o Nox de um átomo só e esquecer o índice, o numerinho embaixo da letra. [p=0.3] No ácido sulfúrico, a pessoa faz {b}mais um, mais xis, menos dois, igual a zero, [p=0.2] e acha {c}mais um para o enxofre."),
    dict(id="s16", block="erro", text="{a}Mas são dois hidrogênios e quatro oxigênios. [p=0.2] {b}Cada átomo entra na soma. [p=0.2] Por isso, {c}multiplique o Nox pelo índice antes de somar."),
    # atalho
    dict(id="s17", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}faça de cabeça, sem montar a equação. [p=0.2] Some só os valores que você conhece: [p=0.1] {b}o Nox que falta é o número que leva essa soma até zero. [p=0.3] {c}No ácido sulfúrico, mais dois e menos oito dão {d}menos seis. [p=0.2] Para chegar a zero, {e}o enxofre é mais seis."),
    dict(id="s18", block="atalho", text="{a}Num íon, a soma vai até a carga. [p=0.2] {b}No íon sulfato, esse ó quatro, com carga dois menos, [p=0.1] os oxigênios dão menos oito, [p=0.1] e a soma precisa chegar a {c}menos dois. [p=0.2] {d}Faltam mais seis: [p=0.1] o enxofre de novo."),
    dict(id="s19", block="atalho", text="Funciona porque {a}a soma de todos os Nox é a carga da substância ou do íon. [p=0.3] {b}Não compensa quando a fórmula tem dois elementos sem valor fixo. [p=0.2] Aí, a questão precisa dar mais uma informação."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] {a}Qual é o Nox do nitrogênio no ácido nítrico, {b}agá ene ó três? [p=0.3] E {c}qual é o Nox dele na amônia, {d}ene agá três?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}No ácido nítrico, o hidrogênio dá mais um, [p=0.1] {b}e três oxigênios dão menos seis. [p=0.2] {c}Mais um e menos seis dão menos cinco, [p=0.1] {d}então o nitrogênio é mais cinco."),
    dict(id="s23", block="resposta", text="{a}Na amônia, três hidrogênios dão mais três. [p=0.2] {b}Para zerar, o nitrogênio é menos três. [p=0.3] {c}O mesmo elemento pode ter Nox diferente em cada substância: [p=0.1] {d}é a fórmula que decide."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: [p=0.1] {a}use os valores fixos, [p=0.1] {b}multiplique cada um pelo índice [p=0.1] {c}e complete a soma até zero, [p=0.1] ou até a carga do íon."),
    dict(id="s25", block="fim", text="Na próxima aula, você vai ver o Nox mudar no meio de uma reação: [p=0.2] {a}quem perde elétrons se oxida, {b}quem ganha se reduz. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
