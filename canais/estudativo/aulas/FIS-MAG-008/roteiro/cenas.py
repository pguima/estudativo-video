# Estudativo · FIS-MAG-008 — Praticando: magnetismo e indução (Física · Magnetismo · Magnetismo e indução · prática).
# Habilidade: resolver questões de campo, força magnética, indução e transformadores.
# Pré-requisitos: FIS-MAG-001 a FIS-MAG-007. Próxima: FIS-MAG-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Mão do tapa (FIS-MAG-003): polegar = v ou i, dedos = B, palma = F.
# Campo saindo da folha: carga + para a direita → força para baixo (x̂ × ẑ = −ŷ).

TITULO = "Praticando: magnetismo e indução"

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
    dict(id="s01", block="gancho", text="No magnetismo, {a}as fórmulas são parecidas, [p=0.2] e {b}o difícil é saber qual usar. [p=0.3] {c}Até o fim desta aula, você vai resolver cinco questões de campo, força, indução e transformador, [p=0.2] e {d}reconhecer cada situação em segundos."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo: [p=0.2] {a}o campo da corrente, [p=0.1] {b}a força magnética, [p=0.1] {c}as leis de Faraday e de Lenz [p=0.1] {d}e o transformador. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método: [p=0.2] três perguntas. [p=0.2] {a}Uma corrente está criando campo? [p=0.1] É fio, espira ou bobina, com a mão que segura o fio. [p=0.3] {b}Alguém sente força? [p=0.1] Carga andando é quê vê bê, [p=0.1] fio com corrente é bê i éle, [p=0.1] com a mão do tapa."),
    dict(id="s04", block="metodo", text="{a}O fluxo está mudando? [p=0.1] É Faraday, com o sentido de Lenz. [p=0.3] {b}Duas bobinas num anel de ferro? [p=0.1] É transformador."),
    # questão 1
    dict(id="s05", block="q1", text="Questão um. [p=0.2] {a}A dez centímetros de um fio longo com cinco ampères, [p=0.1] o campo vale um vezes dez a menos cinco tesla. [p=0.3] {b}Quanto vale a vinte centímetros, com a corrente de vinte ampères? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s06", block="q1", text="Corrente criando campo: [p=0.1] {a}fio, bê proporcional a i dividido por dê. [p=0.3] {b}A corrente foi de cinco para vinte: [p=0.1] vezes quatro, em cima. [p=0.2] {c}A distância dobrou: [p=0.1] vezes dois, embaixo. [p=0.3] {d}Quatro dividido por dois, o campo dobra: [p=0.2] {e}dois vezes dez a menos cinco tesla."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Uma carga positiva de cinco vezes dez a menos seis coulomb anda para a direita, [p=0.1] a dois vezes dez ao cubo metros por segundo. [p=0.3] {b}O campo, de zero vírgula seis tesla, sai da folha. [p=0.3] {c}Qual é a força, e para que lado? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q2", text="Carga andando: [p=0.1] {a}efe igual a quê vê bê seno de teta. [p=0.2] {b}A velocidade está na folha e o campo fura a folha: [p=0.1] noventa graus, seno um. [p=0.3] {c}Cinco vezes dois dá dez, [p=0.1] e dez a menos seis vezes dez ao cubo dá dez a menos três: [p=0.1] dez vezes dez a menos três é dez a menos dois. [p=0.2] {d}Vezes zero vírgula seis: [p=0.1] seis vezes dez a menos três newton."),
    dict(id="s09", block="q2", text="O sentido: [p=0.2] {a}polegar para a direita, [p=0.1] {b}dedos saindo da folha, na sua direção. [p=0.3] {c}A palma fica virada para baixo. [p=0.2] Carga positiva: [p=0.1] {d}a força aponta para baixo."),
    # questão 3
    dict(id="s10", block="q3", text="Questão três. [p=0.2] {a}Num motor, um lado da espira tem cinquenta centímetros dentro de um campo de zero vírgula quatro tesla [p=0.1] e leva cinco ampères. [p=0.3] {b}O fio faz trinta graus com o campo. [p=0.3] {c}Qual é a força nesse lado? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q3", text="Fio com corrente: [p=0.1] {a}efe igual a bê i éle seno de teta. [p=0.3] {b}Cinquenta centímetros são zero vírgula cinco metro. [p=0.2] {c}Zero vírgula quatro vezes cinco dá dois, [p=0.1] vezes zero vírgula cinco dá um, [p=0.2] {d}vezes o seno de trinta, que é meio: [p=0.1] {e}zero vírgula cinco newton."),
    # questão 4
    dict(id="s12", block="q4", text="Questão quatro. [p=0.2] {a}O polo norte de um ímã se afasta de uma bobina de cinquenta espiras. [p=0.3] {b}O fluxo em cada espira cai de zero vírgula zero três para zero vírgula zero um weber, [p=0.1] em zero vírgula cinco segundo. [p=0.3] {c}Qual é a tensão induzida? [p=0.2] {d}E que face a bobina cria do lado do ímã? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s13", block="q4", text="O fluxo está mudando: Faraday. [p=0.2] {a}Delta fi é zero vírgula zero dois weber. [p=0.2] {b}Dividido por zero vírgula cinco, zero vírgula zero quatro. [p=0.2] {c}Vezes cinquenta espiras: [p=0.1] dois volts. [p=0.3] {d}E Lenz: saiu, atrai. [p=0.2] {e}Para atrair um norte, a face é sul, [p=0.1] com a corrente no sentido horário, olhando do lado do ímã."),
    # questão 5
    dict(id="s14", block="q5", text="Questão cinco. [p=0.2] {a}Um transformador ligado em duzentos e vinte volts tem quatrocentas espiras na primária. [p=0.3] {b}Ele precisa entregar onze volts. [p=0.3] {c}Quantas espiras tem a secundária? [p=0.2] {d}E se ela fornece dois ampères, qual é a corrente na primária? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s15", block="q5", text="{a}Duzentos e vinte dividido por onze dá vinte: [p=0.1] a tensão cai vinte vezes. [p=0.2] {b}As espiras também: [p=0.1] quatrocentas dividido por vinte, vinte espiras. [p=0.3] {c}E a corrente vai ao contrário: [p=0.1] na primária, ela é vinte vezes menor. [p=0.2] {d}Dois dividido por vinte: [p=0.1] {e}zero vírgula um ampère."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: {a}corrente cria campo, [p=0.1] {b}campo empurra carga e fio, [p=0.1] {c}e fluxo mudando cria corrente. [p=0.3] Na próxima aula, tudo isso numa usina de verdade: [p=0.2] {d}como a água, o vapor e o calor viram eletricidade. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
