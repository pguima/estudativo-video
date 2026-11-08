# Estudativo · MAT-TOP-008 — Alinhamento de três pontos pelo determinante (Matemática · Tópicos Avançados · Distância de ponto a reta e área por determinante).
# Habilidade: mostrar que (1, 1), (2, 3) e (3, 5) estão alinhados porque o determinante das coordenadas dá zero.
# Pré-requisitos: MAT-ANA-003 (coeficiente angular e alinhamento), MAT-MTZ-003 (determinante e regra de Sarrus). Próxima: MAT-TOP-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados "xis um, ípsilon um" (MAT-ANA-001). Letra k narrada "cá".
# Sarrus: "descendo para a direita" = diagonais principais; "no outro sentido" = as outras três, que se subtraem.

TITULO = "Alinhamento de três pontos pelo determinante"

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
    dict(id="s01", block="gancho", text="Três pontos: {a}xis um, ípsilon um; [p=0.2] {b}xis dois, ípsilon três; [p=0.2] e {c}xis três, ípsilon cinco. [p=0.3] Estão na mesma reta? [p=0.2] Ponha as coordenadas num quadro, [p=0.2] calcule {d}um determinante, [p=0.2] e, se der {e}zero, estão alinhados."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você testa o alinhamento de três pontos pelo determinante, [p=0.2] acha um número que falta [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}três pontos estão alinhados quando a inclinação, o eme, não muda de um ponto para o outro; [p=0.2] e {c}o determinante três por três, pela regra de Sarrus. [p=0.3] Se faltar alguma, procure no canal."),
    # montar
    dict(id="s04", block="montar", text="Monte a matriz assim: [p=0.2] {a}uma linha para cada ponto. [p=0.2] {b}Na primeira coluna, os xis. [p=0.2] {c}Na segunda, os ípsilons. [p=0.2] {d}Na terceira, só o número um, [p=0.2] para completar o três por três."),
    dict(id="s05", block="montar", text="Agora, Sarrus. [p=0.2] {a}Repita as duas primeiras colunas ao lado. [p=0.3] {b}Descendo para a direita: um vezes três vezes um dá três. [p=0.2] {c}Um vezes um vezes três dá três. [p=0.2] {d}Um vezes dois vezes cinco dá dez. [p=0.2] {e}Somando, dezesseis."),
    dict(id="s06", block="montar", text="{a}No outro sentido: um vezes três vezes três dá nove. [p=0.2] {b}Um vezes um vezes cinco dá cinco. [p=0.2] {c}Um vezes dois vezes um dá dois. [p=0.2] {d}Somando, dezesseis. [p=0.3] {e}Dezesseis menos dezesseis: zero. [p=0.2] {f}Os pontos estão alinhados."),
    # por que
    dict(id="s07", block="porque", text="Confira pelo eme: [p=0.2] {a}do primeiro ao segundo ponto, sobe dois e anda um: eme igual a dois. [p=0.2] {b}Do segundo ao terceiro, sobe dois e anda um: dois de novo. [p=0.2] {c}Mesma inclinação: alinhados. [p=0.3] O determinante faz {d}esse mesmo teste, numa conta só."),
    dict(id="s08", block="porque", text="Troque o terceiro ponto por {a}xis quatro, ípsilon seis. [p=0.2] {b}Descendo para a direita: três, mais quatro, mais doze, dezenove. [p=0.2] {c}No outro sentido: doze, mais seis, mais dois, vinte. [p=0.3] {d}Dezenove menos vinte dá menos um. [p=0.2] {e}Diferente de zero: os pontos formam um triângulo. [p=0.3] E a ordem das linhas? [p=0.2] {f}Trocar a ordem dos pontos pode trocar o sinal do resultado, [p=0.2] mas zero continua zero. [p=0.2] Monte na ordem que quiser."),
    # achar o número que falta
    dict(id="s09", block="falta", text="O determinante brilha quando {a}falta um número. [p=0.2] Para que valor de cá o ponto {b}xis cá, ípsilon sete, [p=0.2] fica alinhado com xis um, ípsilon um, e xis dois, ípsilon três? [p=0.3] {c}Faça Sarrus com o cá no lugar do xis. [p=0.2] {d}Descendo: três, mais cá, mais catorze. [p=0.2] {e}No outro sentido: três cá, mais sete, mais dois."),
    dict(id="s10", block="falta", text="{a}Primeira soma menos a segunda, igual a zero: [p=0.2] dezessete mais cá, menos três cá, menos nove. [p=0.2] {b}Oito menos dois cá igual a zero: [p=0.2] {c}cá vale quatro. [p=0.3] Confira pelo eme: de xis um, ípsilon um, até xis quatro, ípsilon sete, [p=0.2] {d}sobe seis e anda três: eme igual a dois. [p=0.2] Bateu."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}somar as duas partes em vez de subtrair. [p=0.2] Nos pontos do começo, a pessoa faz {b}dezesseis mais dezesseis, trinta e dois, [p=0.2] e conclui que {c}não estão alinhados. [p=0.3] {d}O determinante é a primeira soma menos a segunda: zero."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}leve o primeiro ponto para a origem. [p=0.2] {b}Subtraia o primeiro ponto dos outros dois. [p=0.3] Xis dois, ípsilon três, vira {c}xis um, ípsilon dois. [p=0.2] Xis três, ípsilon cinco, vira {d}xis dois, ípsilon quatro. [p=0.3] Sobra {e}um determinante dois por dois: [p=0.2] um vezes quatro, menos dois vezes dois: zero."),
    dict(id="s13", block="atalho", text="Funciona porque {a}deslizar os três pontos juntos não muda se eles estão alinhados. [p=0.2] E o dois por dois é {b}o mesmo multiplicar em cruz do teste do eme. [p=0.3] {c}E ele dá até o mesmo valor do três por três. [p=0.2] Só não esqueça de subtrair sempre o mesmo ponto dos outros dois."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Para que valor de cá os pontos {a}xis zero, ípsilon um; [p=0.2] {b}xis dois, ípsilon cinco; [p=0.2] e {c}xis cá, ípsilon nove [p=0.2] ficam alinhados?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Tire o primeiro ponto dos outros dois: [p=0.2] {b}xis dois, ípsilon quatro, [p=0.2] e {c}xis cá, ípsilon oito. [p=0.3] {d}Dois vezes oito, menos quatro vezes cá: dezesseis menos quatro cá. [p=0.2] {e}Igual a zero: cá vale quatro."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}uma linha por ponto, com um no fim, [p=0.2] e {b}determinante zero quer dizer alinhados."),
    dict(id="s18", block="fim", text="Na próxima aula, você compara {a}duas circunferências [p=0.2] e descobre, só pela distância entre os centros, se elas {b}se cortam, se encostam ou ficam separadas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
