# Estudativo · FIS-DIN-006 — Praticando: leis de Newton (Física · Dinâmica · Leis de Newton · prática).
# Habilidade: desenhar o diagrama de forças e aplicar as três leis em questões do trânsito e do cotidiano.
# Pré-requisitos: FIS-DIN-001, FIS-DIN-002, FIS-DIN-003, FIS-DIN-004, FIS-DIN-005. Próxima: FIS-DIN-007.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# g = 10 m/s². Situação 2 usa Torricelli (FIS-CIN-009, em "Já ensinado"). Atrito não entra: é a aula seguinte.

TITULO = "Praticando: leis de Newton"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações do trânsito e do dia a dia, [p=0.2] criadas para esta aula, [p=0.2] com {b}as três leis de Newton. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes de qualquer conta, {a}desenhe o corpo e as forças nele: [p=0.2] {b}o peso, [p=0.1] e uma força para cada contato. [p=0.3] Depois, escolha a lei: [p=0.2] {c}resultante zero, primeira lei; [p=0.2] {d}resultante e aceleração, segunda; [p=0.2] {e}força entre dois corpos, terceira."),
    # situação 1: inércia
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Um carro freia de repente, [p=0.2] e {c}uma garrafa solta no banco rola para a frente. [p=0.3] {d}Que força empurrou a garrafa?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Nenhuma. [p=0.2] {b}O freio age no carro, não na garrafa. [p=0.3] {c}A garrafa continua com a velocidade que tinha, por inércia, [p=0.2] e {d}o carro para embaixo dela. [p=0.3] É a primeira lei. [p=0.2] {e}Com você, só o cinto evita o mesmo destino: [p=0.2] ele faz em você a força para trás que o freio faz no carro."),
    # situação 2: frenagem
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}Um carro de mil quilogramas, a vinte metros por segundo, [p=0.2] {c}freia até parar em quarenta metros. [p=0.3] {d}Qual é a força resultante que o freia?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Sem o tempo, use {a}Torricelli: [p=0.1] {b}vê ao quadrado igual a vê zero ao quadrado mais dois á delta esse. [p=0.3] {c}Zero é igual a quatrocentos mais oitenta á. [p=0.2] {d}Á vale menos cinco metros por segundo ao quadrado: [p=0.1] o sinal de menos diz que freia."),
    dict(id="s09", block="resposta2", text="Agora, a segunda lei, com o módulo: [p=0.2] {a}mil vezes cinco, [p=0.1] {b}cinco mil newtons, [p=0.2] {c}para trás. [p=0.3] Quem esquece de elevar ao quadrado acha {d}zero igual a vinte mais oitenta á, [p=0.2] e uma força de {e}duzentos e cinquenta newtons. [p=0.2] Pequena demais para parar um carro."),
    # situação 3: ação e reação
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] {b}Uma pessoa rema um barco para a frente. [p=0.3] {c}Quem faz a força que empurra o barco para a frente?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}O remo empurra a água para trás. [p=0.2] Troque os nomes: [p=0.1] {b}a água empurra o remo para a frente. [p=0.3] {c}É a água que empurra, pelo remo, o barco e quem rema. [p=0.3] É a terceira lei, [p=0.1] como no pé que empurra o chão para andar. [p=0.3] {d}E as duas forças não se anulam: [p=0.2] uma está na água, a outra no remo."),
    # situação 4: elevador
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Uma pessoa de setenta quilogramas está numa balança, num elevador [p=0.2] que {c}sobe acelerando a um metro por segundo ao quadrado. [p=0.3] {d}Qual é a força normal na pessoa?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}Desenhe: o peso, setecentos newtons, para baixo; [p=0.1] a normal da balança, para cima. [p=0.3] Aceleração para cima: a normal vence o peso. [p=0.2] {b}Normal igual a eme vezes, abre parênteses, gê mais á: [p=0.2] {c}setenta vezes onze, [p=0.1] {d}setecentos e setenta newtons. [p=0.3] {e}A balança mostra setenta e sete quilos, [p=0.1] sem a pessoa ter engordado nada."),
    # atalho
    dict(id="s16", block="atalho", text="Uma pausa para o atalho que mais salva tempo: [p=0.2] {a}antes de calcular, diga em uma frase para onde aponta a aceleração. [p=0.3] {b}Ela aponta para onde a velocidade está aumentando, [p=0.2] {c}ou contra o movimento, se está freando. [p=0.3] {d}A resultante aponta para o mesmo lado. [p=0.2] Isso já diz qual força é maior."),
    # situação 5: dinamômetro
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] {b}Uma mala pendurada num dinamômetro, parada, [p=0.2] estica a mola {c}cinco centímetros. [p=0.3] A constante da mola é {d}oitocentos newtons por metro. [p=0.3] {e}Qual é a massa da mala?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] {a}Cinco centímetros são zero vírgula zero cinco metro. [p=0.2] {b}Efe é oitocentos vezes zero vírgula zero cinco: [p=0.1] {c}quarenta newtons. [p=0.3] Parada, {d}a força da mola é igual ao peso. [p=0.2] {e}Quarenta é eme vezes dez: [p=0.1] {f}quatro quilogramas. [p=0.3] Quem usa cinco, sem passar para metro, acha quatro mil newtons: uma mala de quatrocentos quilos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}desenhe as forças, [p=0.2] {b}descubra para onde aponta a aceleração [p=0.2] e {c}só então escolha a lei e faça a conta."),
    dict(id="s21", block="fim", text="Na próxima aula, chega a força que faltava: [p=0.2] {a}o atrito, [p=0.2] e o porquê de {b}o freio ABS parar o carro em menos metros. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
