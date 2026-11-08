# Estudativo · MAT-ESP-014 — Esfera: área e volume (Matemática · Geometria Espacial · Esfera).
# Habilidade: usar A = 4πr² e V = 4πr³/3 e calcular o volume de um reservatório esférico de raio 3 m (36π m³).
# Pré-requisitos: MAT-ESP-008 (cilindro, πr²·h, "lata"). Usa MAT-ARE-008 (A = πr²), MAT-POT-001/003 (cubo, r²·r = r³), MAT-MED-005 (1.000 cm³ = 1 L; 1 m³ = 1.000 L). Próxima: MAT-ESP-015.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Letras: "érre", "vê".
# Pirâmide e cone não entram (fora do "já ensinado" desta ficha): o atalho do pi igual a três é apresentado do zero.
# Questão inédita, criada para esta aula.
# Contas: bola r = 5: 4·25 = 100 → 100π cm². Lata em volta: πr²·2r = 2πr³; 2/3 de 2πr³ = 4πr³/3.
#   r = 3: 3³ = 27; 4·27 = 108; 108/3 = 36 → 36π m³ (27/3 = 9; 9·4 = 36). Erro: r = 6 (diâmetro): 6³ = 216; 4·216/3 = 288 → 288π = 8·36π.
#   Atalho π = 3: V = 4r³ = 108 m³ = 108.000 L (= 36·3); A = 12r². Questão: r = 10 cm: A = 12·100 = 1.200 cm²; V = 4·1.000 = 4.000 cm³ = 4 L (4·3·1.000 = 12.000; ÷3 = 4.000). Lata: 2πr·2r = 4πr².
# Visual:
#   s01: E.esfera (laranja) cortada ao meio; quatro círculos iguais desenhados ao lado, sendo cobertos pela casca.
#   s04: E.esfera com centro, raio e o círculo do meio marcados.
#   s07-s09: E.esfera dentro de um E.cilindro de mesmo raio e altura 2r; 2/3 da lata pintados; lateral da lata (2πr × 2r) = casca.
#   s11: dois reservatórios lado a lado, raio 3 e raio 6 (vermelho), com 36π e 288π. s12-s13: palco escuro do atalho.

TITULO = "Esfera: área e volume"

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
    dict(id="s01", block="gancho", text="{a}Corte uma laranja ao meio [p=0.2] e risque {b}o contorno do corte num papel, quatro vezes. [p=0.3] Agora descasque a laranja [p=0.2] e use a casca para cobrir esses círculos. [p=0.3] Ela cobre {c}os quatro, certinho."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área e o volume de qualquer esfera, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área do círculo é pi érre ao quadrado; [p=0.2] {c}o volume do cilindro é a área da base vezes a altura; [p=0.2] e {d}érre ao cubo é érre vezes érre vezes érre. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="esfera", text="{a}A esfera é a bola. [p=0.2] Todos os pontos da superfície ficam {b}à mesma distância do centro, [p=0.2] e essa distância é {c}o raio. [p=0.3] Cortando bem no meio, aparece {d}o maior círculo da esfera, [p=0.2] com o mesmo raio dela."),
    # área
    dict(id="s05", block="area", text="Foi esse círculo do meio que você riscou no papel. [p=0.2] {a}A casca vale quatro deles. [p=0.3] Na fórmula: {b}á igual a quatro pi érre ao quadrado. [p=0.2] É quatro vezes {c}a área do círculo, pi érre ao quadrado."),
    dict(id="s06", block="area", text="Uma bola de {a}raio cinco centímetros: [p=0.2] {b}cinco ao quadrado dá vinte e cinco, [p=0.2] e {c}quatro vezes vinte e cinco dá cem. [p=0.3] {d}Cem pi centímetros quadrados de couro."),
    # volume
    dict(id="s07", block="volume", text="E o volume? [p=0.2] Pense na {a}lata em que a bola cabe certinho: [p=0.2] {b}o mesmo raio, e a altura igual a dois raios. [p=0.3] Há mais de dois mil anos, Arquimedes descobriu: [p=0.2] {c}a esfera ocupa dois terços dessa lata."),
    dict(id="s08", block="volume", text="A lata tem {a}pi érre ao quadrado de base [p=0.2] e {b}dois érre de altura: [p=0.2] o volume dela dá {c}dois pi érre ao cubo. [p=0.3] Dois terços disso: [p=0.2] {d}vê igual a quatro pi érre ao cubo, dividido por três. [p=0.3] Aparece o cubo porque {e}volume tem três medidas: [p=0.2] comprimento, largura e altura."),
    dict(id="s09", block="volume", text="A mesma lata confirma a área. [p=0.2] {a}A lateral dela tem dois pi érre de largura [p=0.2] e {b}dois érre de altura: [p=0.2] {c}dá quatro pi érre ao quadrado. [p=0.3] {d}A mesma área da casca da esfera."),
    dict(id="s10", block="volume", text="Um reservatório esférico de {a}raio três metros. [p=0.2] {b}Três vezes três vezes três dá vinte e sete. [p=0.2] {c}Vinte e sete dividido por três dá nove, [p=0.2] e {d}nove vezes quatro dá trinta e seis. [p=0.3] O reservatório guarda {e}trinta e seis pi metros cúbicos."),
    # erro comum
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar o diâmetro no lugar do raio. [p=0.2] A prova diz: reservatório de {b}seis metros de diâmetro. [p=0.2] Quem põe seis no érre faz {c}seis ao cubo, que dá duzentos e dezesseis, [p=0.2] e acha {d}duzentos e oitenta e oito pi. [p=0.3] É {e}oito vezes o certo, [p=0.2] porque o raio entra ao cubo. [p=0.2] {f}Primeiro, divida o diâmetro por dois: raio três."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, quando a prova manda usar {a}pi igual a três. [p=0.2] No volume, {b}o três do pi cancela o dividido por três: [p=0.2] sobra {c}quatro érre ao cubo. [p=0.3] No reservatório: {d}quatro vezes vinte e sete dá cento e oito metros cúbicos, [p=0.2] ou {e}cento e oito mil litros."),
    dict(id="s13", block="atalho", text="Na área não tem divisão: [p=0.2] {a}quatro vezes três dá doze, [p=0.2] e sobra {b}doze érre ao quadrado. [p=0.3] No volume, funciona porque {c}multiplicar por três e dividir por três se desfazem. [p=0.3] {d}Não compensa quando a prova quer a resposta com o pi escrito: [p=0.2] aí, {e}use a fórmula inteira."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma luminária tem forma de {a}esfera, com dez centímetros de raio. [p=0.2] {b}Use pi igual a três. [p=0.3] {c}Quanto plástico forma a superfície? [p=0.2] {d}E quantos litros de ar cabem dentro?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] Área: {a}dez ao quadrado dá cem, [p=0.2] e {b}doze vezes cem dá mil e duzentos centímetros quadrados de plástico."),
    dict(id="s17", block="resposta", text="Volume: {a}dez ao cubo dá mil, [p=0.2] e {b}quatro vezes mil dá quatro mil centímetros cúbicos. [p=0.3] {c}Mil centímetros cúbicos são um litro: [p=0.2] cabem {d}quatro litros de ar."),
    dict(id="s18", block="resposta", text="Pela fórmula inteira, confira: [p=0.2] {a}quatro vezes três vezes mil dá doze mil, [p=0.2] e {b}dividido por três dá quatro mil. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}área, quatro pi érre ao quadrado, a casca de quatro círculos. [p=0.2] {b}Volume, quatro pi érre ao cubo dividido por três, que dá dois terços da lata."),
    dict(id="s20", block="fim", text="Na próxima aula, você corta a esfera em pedaços: [p=0.2] {a}a meia esfera, o hemisfério; [p=0.2] {b}o gomo, chamado fuso; [p=0.2] e {c}o círculo que aparece num corte fora do centro, achado com Pitágoras. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
