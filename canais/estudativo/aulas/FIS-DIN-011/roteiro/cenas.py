# Estudativo · FIS-DIN-011 — Carro na curva (Física · Dinâmica · Força centrípeta).
# Habilidade: achar a velocidade máxima numa curva plana com v = √(μ·g·R) e numa curva inclinada sem depender do atrito.
# Pré-requisitos: FIS-DIN-010 (centrípeta), FIS-DIN-007 (atrito), FIS-DIN-008 (plano inclinado). Próxima: FIS-DIN-012.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s². Coeficientes 0,8 (seco) e 0,2 (molhado) são ilustrativos. km/h ↔ m/s pelo fator 3,6 (MAT-RAZ-016).
# Curva inclinada: N·cos θ = m·g e N·sen θ = m·v²/R → tg θ = v²/(g·R) (decomposição: FIS-CIN-003; tangente: MAT-TRI-001).

TITULO = "Carro na curva"

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
    dict(id="s01", block="gancho", text="{a}A mesma curva que você faz a setenta e dois quilômetros por hora no seco [p=0.2] {b}pode jogar o carro para fora a quarenta, na chuva. [p=0.3] E {c}as pistas de corrida são inclinadas por um motivo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar {b}a velocidade máxima numa curva plana [p=0.2] e {c}a velocidade certa numa curva inclinada, sem depender do atrito."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a força centrípeta, eme vê ao quadrado sobre erre; [p=0.2] {c}o atrito estático máximo, mi vezes ene; [p=0.2] e {d}decompor uma força com seno e cosseno. [p=0.3] Se faltar alguma, procure no canal."),
    # curva plana
    dict(id="s04", block="plana", text="{a}Numa curva plana, quem segura o carro para o centro? [p=0.3] {b}O atrito entre o pneu e o chão. [p=0.2] E é {c}o estático: [p=0.1] o pneu gira, mas {d}não escorrega de lado."),
    dict(id="s05", block="plana", text="O carro aguenta a curva enquanto {a}o atrito máximo dá conta da centrípeta. [p=0.3] No limite, {b}mi vezes eme vezes gê é igual a eme vê ao quadrado sobre erre. [p=0.3] {c}A massa corta. [p=0.2] Sobra {d}vê ao quadrado igual a mi vezes gê vezes erre, [p=0.2] e {e}vê é a raiz quadrada de mi vezes gê vezes erre."),
    dict(id="s06", block="plana", text="{a}Chão seco, mi de zero vírgula oito, curva de cinquenta metros de raio. [p=0.3] {b}Zero vírgula oito vezes dez vezes cinquenta: quatrocentos. [p=0.2] {c}Raiz de quatrocentos: vinte metros por segundo. [p=0.2] {d}Vezes três vírgula seis: setenta e dois quilômetros por hora."),
    dict(id="s07", block="plana", text="{a}Na chuva, mi cai para zero vírgula dois. [p=0.2] {b}Zero vírgula dois vezes dez vezes cinquenta: cem. [p=0.2] {c}Raiz de cem: dez metros por segundo, [p=0.1] {d}trinta e seis quilômetros por hora. [p=0.3] {e}A curva segura só a metade da velocidade."),
    # curva inclinada
    dict(id="s08", block="inclinada", text="{a}E a pista inclinada? [p=0.2] {b}Nela, a normal não aponta reto para cima: [p=0.1] {c}ela tomba para o centro da curva, com o mesmo ângulo teta da pista. [p=0.3] Decomponha a normal: [p=0.2] {d}a parte vertical segura o peso, [p=0.2] e {e}a parte horizontal faz a centrípeta, sem precisar do atrito."),
    dict(id="s09", block="inclinada", text="{a}Vertical: ene vezes cosseno de teta igual a eme gê. [p=0.2] {b}Horizontal: ene vezes seno de teta igual a eme vê ao quadrado sobre erre. [p=0.3] {c}Divida a segunda pela primeira: [p=0.1] ene e eme cortam, [p=0.1] e seno sobre cosseno é a tangente, [p=0.2] e {d}tangente de teta é vê ao quadrado sobre gê vezes erre."),
    dict(id="s10", block="inclinada", text="{a}Uma pista de quarenta e cinco graus, com noventa metros de raio. [p=0.3] {b}Tangente de quarenta e cinco é um. [p=0.2] {c}Vê ao quadrado é dez vezes noventa: novecentos. [p=0.2] {d}Vê é trinta metros por segundo, cento e oito quilômetros por hora, [p=0.2] {e}mesmo com a pista lisa."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer a raiz. [p=0.3] {b}Zero vírgula oito vezes dez vezes cinquenta dá quatrocentos, [p=0.2] e a resposta {c}quatrocentos metros por segundo. [p=0.3] {d}É mais de mil e quatrocentos quilômetros por hora. [p=0.2] {e}Quatrocentos é vê ao quadrado; vê é vinte."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Curva plana: vê máximo é a raiz de mi vezes gê vezes erre. [p=0.2] {b}Curva inclinada, sem atrito: vê é a raiz de gê vezes erre vezes tangente de teta. [p=0.3] {c}Em nenhuma das duas entra a massa: [p=0.1] {d}o limite é o mesmo para a moto e para o caminhão."),
    dict(id="s13", block="atalho", text="Funciona porque {a}todas as forças da curva têm a massa como fator. [p=0.3] {b}Não compensa quando a curva é inclinada e com atrito ao mesmo tempo: [p=0.2] aí, {c}é preciso decompor o atrito também, numa conta maior."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Uma curva plana tem cento e vinte e cinco metros de raio. [p=0.2] {b}O mi estático entre pneu e asfalto é zero vírgula cinco. [p=0.3] {c}Qual é a velocidade máxima, em quilômetros por hora?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Vê ao quadrado é zero vírgula cinco vezes dez vezes cento e vinte e cinco. [p=0.3] {b}Zero vírgula cinco vezes dez é cinco, [p=0.1] {c}vezes cento e vinte e cinco: seiscentos e vinte e cinco. [p=0.2] {d}Raiz de seiscentos e vinte e cinco: vinte e cinco metros por segundo. [p=0.3] {e}Vezes três vírgula seis: noventa quilômetros por hora."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}na curva plana, o atrito estático faz a centrípeta, e vê máximo é a raiz de mi vezes gê vezes erre; [p=0.2] {b}na inclinada, a normal faz esse papel, [p=0.2] e {c}a massa nunca entra."),
    dict(id="s18", block="fim", text="Na próxima aula, a curva {a}fica de pé: [p=0.2] {b}lombadas, [p=0.1] {c}o globo da morte [p=0.1] e {d}o pêndulo. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
