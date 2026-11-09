# Estudativo · FIS-MOD-010 — Praticando: astronomia e cosmologia (Física · Física Moderna · Astronomia e cosmologia · prática).
# Habilidade: resolver questões de estrelas, Big Bang e expansão do Universo.
# Pré-requisitos: FIS-MOD-008 (estrelas e buracos negros), FIS-MOD-009 (Big Bang). Próxima: nenhuma (fim da trilha).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Q1: 1 massa solar → anã branca; 30 → supernova e buraco negro.
# Q2: buraco negro com a massa do Sol → mesma força na Terra (F = G·M·m/d²). Q3: Andrômeda tem desvio para o azul (se aproxima,
# fato real). Q4: Hubble por proporção, 50 milhões de anos-luz → 1.000 km/s; 400 milhões → 8.000 km/s (≈ 20 km/s por milhão de
# anos-luz, perto do valor real de ~21). Q5: radiação de fundo esticada pela expansão até micro-ondas.
# Última aula da trilha: a ponte final convida a seguir o curso em outras trilhas, sem citar uma aula.

TITULO = "Praticando: astronomia e cosmologia"

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
    dict(id="s01", block="gancho", text="{a}Questão de astronomia quase não tem conta. [p=0.2] {b}Ela cobra a ideia certa no lugar certo. [p=0.3] {c}Até o fim desta aula, você vai resolver cinco questões [p=0.2] de estrelas, buracos negros, Big Bang e expansão do Universo."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as duas últimas aulas: [p=0.2] {a}a vida das estrelas e os buracos negros, [p=0.2] {b}e o Big Bang, com as provas dele. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método: [p=0.2] {a}ache a palavra-chave e lembre a regra dela. [p=0.3] {b}Fim de uma estrela: [p=0.1] olhe a massa. [p=0.2] {c}Força da gravidade: [p=0.1] só massas e distância. [p=0.2] {d}Cor da luz de uma galáxia: [p=0.1] vermelho vai embora, azul aproxima. [p=0.2] {e}Velocidade de afastamento: [p=0.1] proporcional à distância."),
    dict(id="s04", block="metodo", text="E {a}duas pegadinhas que a prova adora. [p=0.2] {b}Primeira: o Sol não vai virar buraco negro, [p=0.1] porque tem pouca massa. [p=0.3] {c}Segunda: o Big Bang não explodiu num ponto, [p=0.1] {d}o espaço inteiro se estica, [p=0.1] {e}e por isso o Universo não tem centro."),
    # questão 1
    dict(id="s05", block="q1", text="Questão um. [p=0.2] {a}Como termina a vida de uma estrela com a massa do Sol? [p=0.2] {b}E a de uma estrela com trinta massas solares? [p=0.2] {c}Qual das duas vive mais? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q1", text="{a}A massa do Sol é pouca: [p=0.1] {b}gigante vermelha, as camadas de fora se soltam, [p=0.1] {c}e sobra uma anã branca. [p=0.3] {d}Trinta massas solares é massa enorme: [p=0.1] {e}a fusão vai até o ferro, o centro desaba, supernova, [p=0.1] {f}e o que sobra vira buraco negro. [p=0.3] {g}E quem vive mais é a pequena: [p=0.1] a estrela grande tem mais combustível, [p=0.1] {h}mas queima muito mais depressa."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Imagine que o Sol virasse, de repente, um buraco negro com a mesma massa. [p=0.3] {b}A força que puxa a Terra aumentaria, diminuiria ou ficaria igual? [p=0.2] {c}E se a Terra chegasse a um décimo da distância? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q2", text="{a}A força é a constante gê vezes as duas massas, dividido pela distância ao quadrado. [p=0.3] {b}Mesma massa do Sol, mesma massa da Terra, mesma distância: [p=0.1] {c}a força fica igual. [p=0.3] {d}A Terra seguiria na mesma órbita, [p=0.1] {e}só que sem luz e sem calor. [p=0.2] O buraco negro não é um aspirador. [p=0.3] {f}Já um décimo da distância muda tudo: [p=0.1] {g}a distância está ao quadrado, embaixo, [p=0.1] {h}dez ao quadrado, cem vezes mais força. [p=0.2] {i}Seria assim com o Sol também."),
    # questão 3
    dict(id="s09", block="q3", text="Questão três. [p=0.2] {a}A luz da galáxia de Andrômeda chega com desvio para o azul. [p=0.3] {b}Ela se afasta ou se aproxima de nós? [p=0.2] {c}Isso contradiz a expansão do Universo? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s10", block="q3", text="{a}Azul é aproxima: [p=0.1] {b}Andrômeda vem na nossa direção. [p=0.3] {c}E não contradiz: [p=0.1] Andrômeda é nossa vizinha, [p=0.1] {d}e a gravidade entre galáxias próximas vence a expansão. [p=0.2] {e}As galáxias distantes, sim, quase todas se afastam."),
    # questão 4
    dict(id="s11", block="q4", text="Questão quatro. [p=0.2] {a}Uma galáxia a cinquenta milhões de anos-luz se afasta a mil quilômetros por segundo. [p=0.3] {b}A que velocidade se afasta uma galáxia a quatrocentos milhões de anos-luz? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s12", block="q4", text="{a}A velocidade é proporcional à distância. [p=0.2] {b}Quatrocentos dividido por cinquenta: oito. [p=0.2] {c}Oito vezes a distância, [p=0.1] {d}oito vezes a velocidade: [p=0.1] {e}oito mil quilômetros por segundo."),
    # questão 5
    dict(id="s13", block="q5", text="Questão cinco. [p=0.2] {a}A radiação cósmica de fundo saiu como luz quente, há quase catorze bilhões de anos. [p=0.3] {b}Por que hoje ela chega como micro-ondas? [p=0.2] {c}E por que é prova do Big Bang? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s14", block="q5", text="{a}Enquanto a luz viajava, o espaço se esticou, [p=0.1] {b}e esticou junto as ondas. [p=0.3] {c}Comprimento de onda muito maior: micro-ondas. [p=0.3] {d}E é prova porque um começo quente e apertado tinha que deixar essa luz, [p=0.1] {e}vinda igual de todas as direções. [p=0.2] Ela foi achada em mil novecentos e sessenta e cinco."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}a massa decide o fim da estrela, [p=0.2] {b}a gravidade só depende de massa e distância, [p=0.2] {c}e o vermelho e a radiação de fundo contam a história do Big Bang. [p=0.3] {d}Com esta aula, você fechou a Física Moderna. [p=0.2] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
