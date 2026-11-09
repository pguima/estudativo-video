# Estudativo · FIS-ELE-010 — Segunda lei de Ohm (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: usar R = ρ·L/A por proporção e dizer o efeito de trocar comprimento, espessura ou material do fio.
# Pré-requisitos: FIS-ELE-009 (U = R·i, resistência em ohm), MAT-RAZ-011 (em cima direto, embaixo inverso). Próxima: FIS-ELE-011.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# A área do círculo (π·r²) não está em "Já ensinado": a aula só usa que a área do corte vai com o quadrado do diâmetro,
#   como a área do quadrado vai com o quadrado do lado (MAT-RAZ-010), e cita a fórmula como assunto de outra aula.
# MAT-RAZ-011 já usou "L dobra e A cai pela metade → 4×": aqui esse caso aparece só como o fio esticado (atalho).
# Contas: 4·3/2 = 6 Ω; esticar 2× → 2·2 = 4×, esticar 3× → 9×; questão 12·3/4 = 9 Ω (pegadinha 12·3/2 = 18 Ω).

TITULO = "Segunda lei de Ohm"

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
    dict(id="s01", block="gancho", text="{a}Você estica um fio de cobre até ele ficar com o dobro do comprimento. [p=0.3] {b}A resistência dele dobra? [p=0.3] {c}Não: fica quatro vezes maior."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender por quê, [p=0.2] e dizer o que acontece com a resistência quando mudam {b}o comprimento, [p=0.1] {c}a espessura [p=0.1] ou {d}o material do fio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a resistência, medida em ohm, que diz o quanto um fio dificulta a passagem da corrente; [p=0.2] e {c}ler uma fórmula: o que está em cima é direto, o que está embaixo é inverso. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Do que depende a resistência de um fio? [p=0.2] Pense num {a}corredor cheio de gente. [p=0.2] {b}Quanto mais comprido, mais difícil atravessar. [p=0.2] {c}Quanto mais largo, mais fácil. [p=0.3] E {d}o tipo de piso também conta: [p=0.1] no fio, é o material."),
    # a fórmula
    dict(id="s05", block="formula", text="Isso vira a segunda lei de Ohm: [p=0.2] {a}erre igual a rô vezes éle, dividido por á. [p=0.3] {b}Erre é a resistência, em ohm. [p=0.2] {c}Éle é o comprimento do fio, em metro. [p=0.2] {d}Á maiúsculo é a área do corte, a bolinha que aparece quando você corta o fio, em metro quadrado. [p=0.2] E {e}rô, essa letra grega, é a resistividade: [p=0.1] um número que depende do material."),
    dict(id="s06", block="formula", text="A unidade da resistividade é {a}ohm vezes metro. [p=0.2] Confira: [p=0.1] {b}ohm vezes metro, vezes metro, dividido por metro quadrado. [p=0.2] {c}Os metros cortam, e sobra ohm. [p=0.3] {d}O cobre tem resistividade bem baixa: [p=0.2] por isso, ele vai nos fios da sua casa."),
    # uma mudança de cada vez
    dict(id="s07", block="efeitos", text="Agora, uma mudança de cada vez. [p=0.2] {a}O comprimento está em cima: [p=0.1] direto. [p=0.2] {b}Dobre o comprimento, e a resistência dobra. [p=0.3] {c}A área está embaixo: [p=0.1] inverso. [p=0.2] {d}Dobre a área, e a resistência cai pela metade. [p=0.3] E {e}trocar o material muda o rô: [p=0.2] {f}resistividade três vezes maior, resistência três vezes maior."),
    dict(id="s08", block="efeitos", text="Um exemplo. [p=0.2] Um fio tem {a}quatro ohms. [p=0.2] Outro, do mesmo material, tem {b}o triplo do comprimento [p=0.1] e {c}o dobro da área. [p=0.3] {d}Vezes três, por causa do comprimento; [p=0.2] {e}dividido por dois, por causa da área. [p=0.2] {f}Quatro vezes três, doze; [p=0.1] dividido por dois, {g}seis ohms."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}confundir a espessura, que é o diâmetro do fio, com a área. [p=0.3] Se a questão diz que {b}o diâmetro dobrou, [p=0.2] a pessoa {c}divide a resistência por dois."),
    dict(id="s10", block="erro", text="Mas {a}a área vai com o quadrado do diâmetro, [p=0.2] como {b}num quadrado: lado dobrou, área vezes quatro. [p=0.3] {c}Diâmetro vezes dois, área vezes quatro. [p=0.2] {d}A resistência cai para um quarto, não para a metade. [p=0.3] {e}A fórmula da área do círculo é assunto de outra aula."),
    # atalho
    dict(id="s11", block="atalho", text="Agora, o atalho do fio esticado. [p=0.2] {a}Esticar não cria cobre novo. [p=0.2] Se o comprimento fica {b}duas vezes maior, [p=0.1] o fio afina, e {c}a área cai pela metade. [p=0.3] {d}Vezes dois pelo comprimento, [p=0.1] e vezes dois de novo pela área. [p=0.2] {e}Quatro vezes."),
    dict(id="s12", block="atalho", text="A regra: {a}esticou ene vezes, a resistência fica ene ao quadrado vezes maior. [p=0.2] {b}Esticou três vezes? Nove vezes. [p=0.3] Funciona porque {c}a quantidade de cobre é a mesma: [p=0.2] o comprimento multiplica, e a área divide pelo mesmo número. [p=0.3] {d}Não vale se o fio for trocado por outro: [p=0.2] aí, cada medida muda do seu jeito, e você usa a fórmula."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um fio de {a}doze ohms é trocado por outro do mesmo material, [p=0.2] com {b}o triplo do comprimento [p=0.1] e {c}o dobro do diâmetro. [p=0.3] {d}Qual é a resistência do fio novo?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Comprimento vezes três: [p=0.1] a resistência fica vezes três. [p=0.2] {b}Diâmetro vezes dois: [p=0.1] a área fica vezes quatro, [p=0.1] e a resistência, dividida por quatro. [p=0.3] {c}Doze vezes três, trinta e seis; [p=0.1] dividido por quatro, {d}nove ohms. [p=0.3] Quem dividiu só por dois achou {e}dezoito, a resposta da pegadinha."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: {a}erre igual a rô vezes éle, dividido por á. [p=0.2] {b}Fio mais comprido, mais resistência; [p=0.1] {c}fio mais grosso, menos resistência; [p=0.1] {d}e o material entra pelo rô. [p=0.2] Diâmetro dobrou? {e}Área vezes quatro."),
    dict(id="s17", block="fim", text="Na próxima aula, você vai {a}ligar resistores um atrás do outro, em série, [p=0.2] e descobrir por que {b}a resistência total é a soma. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
