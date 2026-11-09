# Estudativo · FIS-ENE-009 — Colisões e coeficiente de restituição (Física · Energia e Colisões · Impulso e colisões).
# Habilidade: classificar colisões em elástica, parcial ou inelástica e achar as velocidades finais com o coeficiente de restituição.
# Pré-requisitos: FIS-ENE-008 (Q antes = Q depois), FIS-ENE-003 (Ec), MAT-EQU-019 (sistema pela adição). Próxima: FIS-ENE-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Colisão frontal, numa reta. e = afastamento / aproximação (velocidades relativas). Velocidades com nome: vê á e vê bê.
# Contas: inelástica 1.000·20 = 2.000·v → v = 10; Ec 1.000·400/2 = 200.000 → 2.000·100/2 = 100.000 (metade);
#   erro Ec conservada: 2.000·v²/2 = 200.000 → v² = 200 → v ≈ 14,1 → Q ≈ 28.284 > 20.000; bilhar vA + vB = 4, vB − vA = 4 → vB = 4, vA = 0;
#   parcial 2·6 = 12 = 2vA + vB, vB − vA = 0,5·6 = 3 → vA = 3, vB = 6; Ec 36 → 9 + 18 = 27; questão 3·4 = 12 = 4v → v = 3;
#   Ec 3·16/2 = 24 → 4·9/2 = 18: perdeu 6 J.

TITULO = "Colisões e coeficiente de restituição"

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
    dict(id="s01", block="gancho", text="{a}Na sinuca, a bola branca bate de frente numa bola parada, igual a ela. [p=0.2] {b}A branca para, [p=0.1] e {c}a outra sai com a velocidade que a branca tinha. [p=0.3] {d}Num engavetamento, os carros saem grudados. [p=0.3] O que muda de uma batida para a outra?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai classificar as colisões em {b}elástica, parcial ou inelástica, [p=0.2] e achar {c}as velocidades depois da batida."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}quantidade de movimento antes igual à de depois, com sinal; [p=0.2] {c}energia cinética, eme vezes vê ao quadrado, dividido por dois; [p=0.2] e {d}sistemas de duas equações. [p=0.3] Se faltar alguma, procure no canal."),
    # o que se conserva
    dict(id="s04", block="ideia", text="Numa colisão, os corpos se empurram com forças enormes, por um tempo muito curto. [p=0.2] {a}Essas forças são de um corpo no outro, internas ao sistema, [p=0.2] então {b}a quantidade de movimento total se conserva em toda colisão. [p=0.3] {c}A energia cinética, nem sempre: [p=0.2] parte pode virar {d}calor, som e deformação."),
    dict(id="s05", block="ideia", text="Para medir quanto os corpos se afastam depois, existe o {a}coeficiente de restituição, a letra é. [p=0.2] Ele é {b}a velocidade de afastamento dividida pela velocidade de aproximação."),
    dict(id="s06", block="ideia", text="{a}Aproximação é a rapidez com que um corpo chega perto do outro, antes da batida. [p=0.2] {b}Afastamento é a rapidez com que eles se separam, depois. [p=0.3] Na mesma reta: {c}se andam em sentidos opostos, some as velocidades; [p=0.2] {d}se andam no mesmo sentido, subtraia."),
    # tipos
    dict(id="s07", block="tipos", text="O coeficiente vai de zero a um e dá nome à colisão. [p=0.2] {a}Coeficiente igual a um: colisão elástica. [p=0.2] Eles se afastam tão rápido quanto chegaram, e {b}a energia cinética se conserva. [p=0.3] {c}Coeficiente entre zero e um: parcialmente elástica, [p=0.2] e {d}parte da energia se perde."),
    dict(id="s08", block="tipos", text="{a}Coeficiente igual a zero: colisão inelástica. [p=0.2] {b}Eles não se afastam: saem grudados. [p=0.2] {c}É a que mais perde energia."),
    # inelástica
    dict(id="s09", block="inelastica", text="Comece pela inelástica. [p=0.2] {a}Um carro de mil quilogramas, a vinte metros por segundo, bate num carro igual, parado, [p=0.2] e {b}eles saem grudados. [p=0.3] {c}Antes: mil vezes vinte, vinte mil. [p=0.2] {d}Depois: dois mil vezes vê. [p=0.2] {e}Vê igual a dez metros por segundo."),
    dict(id="s10", block="inelastica", text="E a energia? [p=0.2] {a}Antes: mil vezes quatrocentos, dividido por dois, duzentos mil joules. [p=0.2] {b}Depois: dois mil vezes cem, dividido por dois, cem mil joules. [p=0.3] {c}Metade da energia virou deformação e calor."),
    # elástica
    dict(id="s11", block="elastica", text="Na sinuca, {a}a colisão é elástica, com bolas de mesma massa. [p=0.2] A branca, a bola á, chega a {b}quatro metros por segundo. [p=0.3] {c}Quantidade de movimento, com a massa cortada: quatro igual a vê á mais vê bê. [p=0.2] {d}Coeficiente igual a um: vê bê menos vê á, depois, dá os mesmos quatro."),
    dict(id="s12", block="elastica", text="{a}Some as duas equações: [p=0.2] {b}duas vezes vê bê igual a oito, [p=0.1] {c}vê bê igual a quatro. [p=0.2] {d}E vê á fica zero: a branca para. [p=0.3] {e}Massas iguais, colisão elástica: elas trocam de velocidade."),
    # parcial
    dict(id="s13", block="parcial", text="Falta a parcial. [p=0.2] {a}Um carrinho á, de dois quilogramas, a seis metros por segundo, bate num carrinho bê, de um quilograma, parado. [p=0.2] {b}O coeficiente vale zero vírgula cinco. [p=0.3] {c}Quantidade de movimento: doze igual a dois vê á mais vê bê. [p=0.2] {d}Restituição: vê bê menos vê á igual a meio vezes seis, três."),
    dict(id="s14", block="parcial", text="{a}Da segunda equação, vê bê é vê á mais três. [p=0.2] {b}Na primeira: doze igual a dois vê á, mais vê á, mais três. [p=0.2] {c}Três vê á igual a nove: vê á igual a três. [p=0.2] {d}E vê bê igual a seis metros por segundo. [p=0.3] {e}A energia caiu de trinta e seis para vinte e sete joules."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}conservar a energia em toda colisão. [p=0.2] No exemplo dos carros de mil quilogramas, quem iguala as energias {b}acha cerca de catorze metros por segundo para o conjunto."),
    dict(id="s16", block="erro", text="Mas aí {a}a quantidade de movimento daria cerca de vinte e oito mil, [p=0.2] {b}mais do que os vinte mil de antes. [p=0.3] {c}A quantidade de movimento se conserva sempre; [p=0.2] {d}a energia cinética, só na elástica."),
    # atalho
    dict(id="s17", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}massas iguais, colisão elástica, uma parada: elas trocam de velocidade, [p=0.2] sem conta nenhuma. [p=0.3] {b}E na inelástica, com um corpo parado: [p=0.2] {c}a velocidade final é a quantidade de movimento de antes dividida pela massa total."),
    dict(id="s18", block="atalho", text="Funciona porque, {a}na troca, é a única saída que conserva a quantidade de movimento e afasta as bolas na mesma rapidez. [p=0.2] {b}Na inelástica, só existe uma velocidade, a do conjunto. [p=0.3] {c}Não compensa na elástica com massas diferentes: [p=0.2] aí, monte o sistema."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}Um carrinho de três quilogramas, a quatro metros por segundo, bate num carrinho de um quilograma, parado, [p=0.2] e {b}eles seguem grudados. [p=0.3] {c}Qual é a velocidade final? [p=0.2] {d}Que tipo de colisão é essa, [p=0.1] {e}e quanta energia cinética se perdeu?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Antes: três vezes quatro, doze. [p=0.2] {b}Depois: quatro quilogramas juntos, quatro vezes vê. [p=0.2] {c}Vê igual a três metros por segundo. [p=0.3] {d}Saíram grudados: inelástica, com coeficiente zero."),
    dict(id="s22", block="resposta", text="{a}Energia antes: três vezes dezesseis, dividido por dois, vinte e quatro joules. [p=0.2] {b}Depois: quatro vezes nove, dividido por dois, dezoito joules. [p=0.2] {c}Perdeu seis joules."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}em toda colisão, a quantidade de movimento se conserva; [p=0.2] {b}o coeficiente é o afastamento dividido pela aproximação; [p=0.2] e {c}só na elástica, com coeficiente um, a energia cinética também se conserva."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai {a}praticar impulso, recuo e colisões, [p=0.2] juntando quantidade de movimento e energia em questões de prova. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
