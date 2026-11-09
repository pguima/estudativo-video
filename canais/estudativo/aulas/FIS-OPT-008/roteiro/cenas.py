# Estudativo · FIS-OPT-008 — Olho humano e defeitos da visão (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: dizer onde a imagem se forma na miopia, na hipermetropia, na presbiopia e no astigmatismo e qual lente corrige cada um.
# Pré-requisitos: FIS-OPT-007 (equação das lentes, V = 1/f com f em metros). Próxima: FIS-OPT-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Grau do míope = −1/PR (PR = ponto remoto, em metros): a lente divergente faz a imagem
# de um objeto muito distante no seu foco, no ponto remoto. Ponto próximo normal ≈ 25 cm. Cones e bastonetes são de Biologia.

TITULO = "Olho humano: miopia, hipermetropia e as lentes que corrigem"

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
    dict(id="s01", block="gancho", text="{a}Na receita de quem tem miopia, o grau vem com sinal de menos. [p=0.3] {b}Na de quem tem hipermetropia, com sinal de mais. [p=0.3] {c}O sinal diz qual lente o olho precisa, [p=0.2] e hoje você vai entender por quê."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer {b}onde a imagem se forma em cada defeito da visão [p=0.2] e {c}qual lente corrige cada um."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}lente convergente junta os raios, e a divergente espalha; [p=0.2] e {c}o grau é um dividido pelo foco em metros, positivo na convergente. [p=0.3] Se faltar alguma, procure no canal."),
    # o olho
    dict(id="s04", block="olho", text="{a}A luz entra no olho pela córnea, a janela transparente da frente, [p=0.2] {b}passa pela pupila, o furinho escuro no meio, [p=0.2] e {c}atravessa o cristalino, uma lente natural dentro do olho. [p=0.3] {d}Córnea e cristalino funcionam juntos como uma lente convergente."),
    dict(id="s05", block="olho", text="{a}A imagem se forma na retina, o fundo do olho, que funciona como uma tela. [p=0.3] Ela é {b}real, [p=0.1] {c}invertida [p=0.1] e {d}menor. [p=0.2] {e}É o cérebro que deixa a imagem de pé."),
    dict(id="s06", block="olho", text="Para ver de perto, {a}músculos em volta do cristalino deixam ele mais curvo, [p=0.2] e {b}o foco fica menor. [p=0.2] Isso é {c}a acomodação. [p=0.3] {d}O ponto mais longe que o olho vê nítido é o ponto remoto: [p=0.2] no olho normal, ele está no infinito. [p=0.3] {e}O mais perto é o ponto próximo: [p=0.2] no olho normal, uns vinte e cinco centímetros."),
    # miopia
    dict(id="s07", block="miopia", text="{a}Na miopia, o olho é comprido demais, ou converge demais. [p=0.3] {b}A imagem de algo distante se forma antes da retina, [p=0.2] e {c}chega à retina borrada. [p=0.3] {d}O míope vê mal de longe."),
    dict(id="s08", block="miopia", text="{a}A correção é uma lente divergente. [p=0.2] {b}Ela espalha um pouco os raios [p=0.2] e {c}empurra a imagem para trás, até a retina. [p=0.3] {d}Por isso o grau do míope é negativo."),
    dict(id="s09", block="miopia", text="E dá para calcular. [p=0.2] {a}Um míope com ponto remoto a cinquenta centímetros. [p=0.3] {b}A lente pega o objeto muito distante [p=0.2] e {c}faz a imagem dele no foco, a cinquenta centímetros, onde o olho enxerga bem. [p=0.3] {d}Então efe é menos zero vírgula cinco metro, [p=0.2] e {e}o grau é menos dois."),
    # hipermetropia e presbiopia
    dict(id="s10", block="hiper", text="{a}Na hipermetropia, é o contrário: o olho é curto, ou converge de menos. [p=0.3] {b}A imagem de algo perto se forma depois da retina. [p=0.3] {c}A pessoa vê mal de perto. [p=0.2] {d}A correção é uma lente convergente, de grau positivo."),
    dict(id="s11", block="hiper", text="{a}A presbiopia, a vista cansada, vem com a idade. [p=0.2] {b}O cristalino endurece e acomoda menos, [p=0.2] e {c}o ponto próximo se afasta: [p=0.2] de perto, a imagem cai depois da retina. [p=0.3] {d}A pessoa estica o braço para ler. [p=0.2] {e}A correção também é convergente, para perto: [p=0.2] os óculos de leitura."),
    # astigmatismo
    dict(id="s12", block="astig", text="{a}No astigmatismo, a córnea não é curva por igual: [p=0.2] {b}é mais curva numa direção que na outra, [p=0.2] como uma bola de futebol americano. [p=0.3] {c}Cada direção forma a imagem num ponto diferente: [p=0.2] linhas numa direção ficam nítidas, e na outra, borradas. [p=0.3] {d}A correção é uma lente cilíndrica, curva numa direção só."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}dar lente convergente ao míope, [p=0.2] porque ele precisa enxergar melhor. [p=0.3] {b}Mas o olho dele já converge demais. [p=0.2] {c}Uma convergente juntaria os raios ainda mais cedo, [p=0.2] e {d}a imagem ficaria mais longe da retina."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Míope, menos: as duas palavras começam com M. [p=0.3] {b}Miopia: divergente, grau negativo. [p=0.2] {c}Hipermetropia e presbiopia: convergente, grau positivo. [p=0.2] {d}Astigmatismo: cilíndrica."),
    dict(id="s15", block="atalho", text="E a conta do míope: {a}o grau é menos um dividido pelo ponto remoto, em metros. [p=0.3] {b}Ponto remoto de vinte e cinco centímetros: menos quatro graus. [p=0.3] Funciona porque {c}a lente certa tem o foco bem no ponto remoto. [p=0.3] {d}Na hipermetropia, essa conta não serve, [p=0.2] porque o problema está no ponto próximo."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma pessoa {a}enxerga nítido só até quarenta centímetros. [p=0.3] {b}Qual é o defeito, [p=0.2] {c}que lente corrige [p=0.2] e {d}qual é o grau?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Ela não vê nítido de longe: é miopia. [p=0.3] {b}A correção é uma lente divergente. [p=0.3] {c}Quarenta centímetros são zero vírgula quatro metro. [p=0.2] {d}Menos um dividido por zero vírgula quatro: [p=0.2] {e}menos dois vírgula cinco graus."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o olho forma na retina uma imagem real, invertida e menor; [p=0.2] {b}na miopia, a imagem cai antes da retina, e a lente é divergente; [p=0.2] {c}na hipermetropia e na presbiopia, a lente é convergente; [p=0.2] e {d}no astigmatismo, cilíndrica."),
    dict(id="s20", block="fim", text="Na próxima aula, as lentes {a}viram instrumentos: [p=0.2] {b}a lupa e a câmera, e o microscópio e a luneta, com duas lentes juntas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
