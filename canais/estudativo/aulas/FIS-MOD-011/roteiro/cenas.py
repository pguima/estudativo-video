# Estudativo · FIS-MOD-011 — E = m·c² (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: usar E = m·c² e ligar a massa perdida à energia da fissão e da fusão.
# Pré-requisitos: FIS-MOD-005 (relatividade restrita), QUI-ELE-013 (fissão e fusão nuclear). Próxima: FIS-MOD-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" desta aula não tem trabalho e energia (FIS-ENE) nem porcentagem (MAT-POR): o joule é apresentado na hora
# (≈ erguer 100 g a 1 m: 0,1 · 9,8 · 1 ≈ 1 J) e a massa perdida vai em gramas por quilo, sem por cento.
# Fatos: Einstein, 1905. c² = 9 × 10¹⁶ m²/s². Fusão do hidrogênio em hélio: some cerca de 7 g por kg (0,7 %).
# Fissão do urânio-235: cerca de 0,9 g por kg (0,09 %). O Sol converte cerca de 4 milhões de toneladas de massa por segundo
# (4,3 × 10⁹ kg/s). Hiroshima (~15 kt, 6 × 10¹³ J): menos de um grama de massa virou energia (~0,7 g).

TITULO = "E = m·c²"

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
    dict(id="s01", block="gancho", text="{a}A cada segundo, o Sol fica {b}quatro milhões de toneladas mais leve. [p=0.3] {c}Essa massa não escapa para o espaço como poeira. [p=0.2] {d}Ela vira luz e calor. [p=0.3] Quem explica é {e}a fórmula mais famosa da Física."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar a fórmula energia igual a massa vezes cê ao quadrado [p=0.2] e {b}achar a energia que sai da massa perdida na fissão e na fusão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a velocidade da luz, cê, é a mesma para todos e é o limite de tudo que tem massa; [p=0.2] e {c}a fissão quebra núcleos grandes, a fusão junta núcleos pequenos. [p=0.3] Se faltar alguma, procure no canal."),
    # o joule
    dict(id="s04", block="joule", text="Antes, a unidade. [p=0.2] {a}A energia, no Sistema Internacional, se mede em joule. [p=0.3] {b}Um joule é mais ou menos a energia para erguer uma maçã pequena, de cem gramas, [p=0.1] {c}até um metro de altura. [p=0.3] {d}É pouca coisa."),
    # a fórmula
    dict(id="s05", block="formula", text="Em mil novecentos e cinco, {a}Einstein mostrou que massa e energia são duas formas da mesma coisa. [p=0.3] {b}A energia é a massa vezes a velocidade da luz ao quadrado: [p=0.2] {c}energia igual a massa vezes cê ao quadrado. [p=0.3] {d}A massa vai em quilograma, [p=0.1] {e}cê em metro por segundo, [p=0.1] {f}e a energia sai em joule."),
    dict(id="s06", block="formula", text="O segredo está no {a}cê ao quadrado. [p=0.2] {b}Três vezes dez elevado a oito, ao quadrado: [p=0.2] {c}três ao quadrado, nove, [p=0.1] {d}e oito vezes dois, dez elevado a dezesseis. [p=0.3] {e}Nove vezes dez elevado a dezesseis. [p=0.2] {f}Um número gigante multiplicando a massa."),
    dict(id="s07", block="formula", text="{a}Um quilograma inteiro virando energia daria nove vezes dez elevado a dezesseis joules. [p=0.2] {b}São noventa milhões de bilhões de maçãs erguidas. [p=0.3] {c}Na bomba de Hiroshima, menos de um grama de massa virou energia."),
    # massa perdida
    dict(id="s08", block="massa", text="Mas de onde sai a massa? [p=0.2] {a}Numa fusão, junte os núcleos que entram e pese. [p=0.2] {b}Depois, pese o que sai. [p=0.3] {c}O que sai pesa um pouquinho menos. [p=0.2] {d}Essa diferença se chama defeito de massa. [p=0.3] {e}Ela some da balança e vira a energia liberada."),
    dict(id="s09", block="massa", text="{a}Na fusão do hidrogênio em hélio, a que acontece no Sol, [p=0.2] {b}somem uns sete gramas a cada quilograma. [p=0.3] {c}Sete gramas são sete vezes dez elevado a menos três quilogramas. [p=0.2] {d}Vezes nove vezes dez elevado a dezesseis: [p=0.2] {e}sessenta e três vezes dez elevado a treze, [p=0.1] {f}ou seis vírgula três vezes dez elevado a catorze joules."),
    dict(id="s10", block="massa", text="{a}Vale para a fissão também, a da usina nuclear. [p=0.2] {b}E vale até para uma fogueira: [p=0.1] {c}a massa perdida é tão pequena que nenhuma balança percebe. [p=0.3] {d}A diferença é o tamanho: [p=0.1] {e}a reação nuclear transforma muito mais massa por quilo que a queima."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}esquecer o quadrado. [p=0.3] {b}Sete vezes dez elevado a menos três, vezes três vezes dez elevado a oito, [p=0.2] dá {c}dois vírgula um vezes dez elevado a seis joules. [p=0.3] {d}Trezentos milhões de vezes menos que a resposta certa. [p=0.2] {e}Confira pela unidade: [p=0.1] {f}massa vezes velocidade dá quilograma vezes metro por segundo, [p=0.2] e o joule é quilograma vezes metro ao quadrado por segundo ao quadrado."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}decore cê ao quadrado, nove vezes dez elevado a dezesseis. [p=0.3] {b}Com a massa em quilograma, a conta vira: [p=0.1] {c}multiplique o número por nove [p=0.1] {d}e some dezesseis ao expoente. [p=0.3] {e}Para dez elevado a menos três quilograma, um grama: [p=0.1] {f}nove vezes dez elevado a treze joules."),
    dict(id="s13", block="atalho", text="{a}E a energia é proporcional à massa: [p=0.2] {b}o dobro de massa perdida, o dobro de energia. [p=0.3] {c}Cuidado só com a massa em grama ou em tonelada: [p=0.2] {d}antes, passe para quilograma."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Na fissão de um quilograma de urânio duzentos e trinta e cinco, [p=0.1] {b}somem zero vírgula nove grama de massa. [p=0.3] {c}Quanta energia sai? [p=0.2] E {d}quantas vezes a fusão do hidrogênio, com os seus sete gramas por quilo, libera mais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Zero vírgula nove grama é nove vezes dez elevado a menos quatro quilograma. [p=0.3] {b}Multiplique por nove: oitenta e um. [p=0.2] {c}Some dezesseis ao expoente: menos quatro mais dezesseis, doze. [p=0.3] {d}Oitenta e um vezes dez elevado a doze, [p=0.1] {e}ou oito vírgula um vezes dez elevado a treze joules."),
    dict(id="s17", block="resposta", text="{a}E a comparação, pela proporção: [p=0.2] {b}sete gramas contra zero vírgula nove. [p=0.2] {c}Sete dividido por zero vírgula nove dá quase oito. [p=0.3] {d}Por quilo, a fusão libera quase oito vezes mais energia que a fissão."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}massa é energia, e energia é igual a massa vezes cê ao quadrado; [p=0.2] {b}cê ao quadrado vale nove vezes dez elevado a dezesseis; [p=0.2] e {c}a energia da fissão e da fusão vem da massa que some."),
    dict(id="s19", block="fim", text="Na próxima aula, {a}a Física Moderna entra no seu bolso: [p=0.2] {b}o silício, o diodo e o transistor, que fazem o celular funcionar. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
