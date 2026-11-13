# Estudativo · QUI-AMB-007 — Praticando: química e ambiente (Química · Química e Ambiente · Tratamento de água e química verde).
# Habilidade: analisar textos sobre energia, poluição e água com o que aprendeu em toda a Química.
# Pré-requisitos: QUI-AMB-001 a QUI-AMB-006. Próxima: nenhuma; é a última aula de Química do Zero.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: quatro questões inéditas, criadas para esta aula.
# Q1 anúncio "etanol emissão zero e protege o ozônio" (AMB-001, AMB-003): C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O.
# Q2 diesel com menos enxofre (AMB-002): SO₂ → SO₃ → H₂SO₄, chuva ácida, mármore.
# Q3 usina devolve água limpa e 8 °C mais quente, "DBO não mudou" (AMB-005): poluição térmica, OD cai.
# Q4 duas rotas para o etanol (AMB-006): C₂H₄ + H₂O → C₂H₆O (28 + 18 = 46 → 100%);
#    C₆H₁₂O₆ → 2 C₂H₆O + 2 CO₂ (92 ÷ 180 ≈ 0,511 → cerca de 51%), mas a glicose vem da cana (renovável) e o eteno do
#    petróleo. Fórmulas faladas: C₂H₄ "cê dois agá quatro", C₆H₁₂O₆ "cê seis agá doze ó seis".

TITULO = "Praticando: química e ambiente"

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
    dict(id="s01", block="gancho", text="{a}Anúncio, notícia, laudo de rio: [p=0.1] {b}a prova traz um texto e pergunta o que está certo. [p=0.3] {c}Hoje são quatro textos, cada um com uma afirmação que parece boa e não é."),
    dict(id="s02", block="gancho", text="Você vai usar {a}combustíveis, [p=0.1] {b}chuva ácida, [p=0.1] {c}efeito estufa, [p=0.1] {d}oxigênio dissolvido [p=0.1] {e}e economia atômica. [p=0.3] Se faltar alguma dessas aulas, procure no canal."),
    # Q1
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Um anúncio diz: [p=0.1] {b}carro a etanol, emissão zero de gás carbônico, [p=0.1] {c}e ainda protege a camada de ozônio. [p=0.3] {d}O que está errado nas duas promessas?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}A primeira: o etanol tem carbono, então solta cê ó dois ao queimar. [p=0.2] {b}Cada molécula de etanol dá duas de cê ó dois. [p=0.3] {c}O certo é dizer que a cana retirou esse carbono do ar ao crescer: [p=0.1] {d}o ciclo fecha em parte, [p=0.1] {e}porque plantar e transportar também emitem."),
    dict(id="s06", block="q1", text="{a}A segunda mistura os assuntos. [p=0.2] {b}Cê ó dois é gás estufa: segura calor. [p=0.2] {c}Quem ataca o ozônio é o cloro do cê éfe cê. [p=0.3] {d}Trocar gasolina por etanol não protege a camada de ozônio."),
    # Q2
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] {b}Uma cidade troca o óleo diesel dos ônibus por um com muito menos enxofre. [p=0.3] {c}Qual poluente cai? [p=0.2] {d}E que estrago ele causava nas estátuas de mármore da praça?"),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="q2", text="{a}Menos enxofre no diesel, menos ésse ó dois saindo do escapamento. [p=0.3] {b}No ar, o ésse ó dois vira ésse ó três, [p=0.1] {c}e o ésse ó três com a água da chuva forma ácido sulfúrico. [p=0.3] {d}É a chuva ácida, que corrói o carbonato de cálcio do mármore."),
    dict(id="s10", block="q2", text="{a}A pegadinha seria dizer que cai o cê ó dois. [p=0.2] {b}O gás carbônico vem do carbono do diesel, e isso não mudou."),
    # Q3
    dict(id="s11", block="q3", text="{a}Questão três. [p=0.2] {b}Uma usina usa água do rio para resfriar máquinas [p=0.1] e a devolve limpa, oito graus mais quente. [p=0.3] {c}Um fiscal diz: a dê bê ó não mudou, então não há poluição. [p=0.3] {d}Ele está certo?"),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="q3", text="{a}Não está. [p=0.2] {b}Água mais quente dissolve menos oxigênio, como o refrigerante quente que perde gás. [p=0.3] {c}O oxigênio dissolvido cai, mesmo sem esgoto nenhum. [p=0.3] {d}E, no calor, o peixe precisa de mais oxigênio. [p=0.2] {e}É poluição térmica: a dê bê ó não mede isso."),
    # Q4
    dict(id="s14", block="q4", text="{a}Questão quatro. [p=0.2] Há dois caminhos para fazer etanol. [p=0.3] {b}Rota A: [p=0.1] cê dois agá quatro, o eteno, que sai do petróleo, mais água, dá etanol. [p=0.3] {c}Rota B: [p=0.1] a glicose da cana, cê seis agá doze ó seis, dá duas moléculas de etanol e duas de cê ó dois. [p=0.3] {d}Qual tem a maior economia atômica? [p=0.2] {e}E que princípio da química verde a rota B cumpre melhor?"),
    dict(id="s15", block="q4", text="{a}As massas molares: eteno vinte e oito, água dezoito, etanol quarenta e seis, glicose cento e oitenta. [p=0.2] {b}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="q4", text="{a}Rota A tem um produto só: [p=0.1] {b}cem por cento, sem conta. [p=0.3] {c}Rota B: duas vezes quarenta e seis dá noventa e dois, [p=0.1] {d}e noventa e dois dividido por cento e oitenta dá cerca de cinquenta e um por cento."),
    dict(id="s17", block="q4", text="{a}A rota A vence na economia atômica. [p=0.3] {b}Mas ela usa petróleo, e a B usa cana: [p=0.1] a rota B cumpre melhor o princípio da matéria-prima renovável. [p=0.3] {c}Química verde tem doze princípios, e um número só não decide. [p=0.2] {d}A resposta completa cita os dois lados."),
    # fechamento
    dict(id="s18", block="fim", text="As quatro lições, em uma frase cada: [p=0.2] {a}renovável não é emissão zero; [p=0.2] {b}enxofre vira chuva ácida; [p=0.2] {c}água quente também asfixia; [p=0.2] e {d}economia atômica é um princípio, não o único."),
    dict(id="s19", block="fim", text="Esta é a última aula de Química do Zero. [p=0.3] {a}Você foi do átomo até o planeta. [p=0.3] {b}Para revisar qualquer assunto, a playlist completa está no canal. [p=0.3] {c}Inscreva-se para continuar estudando com a gente. [p=0.2] {d}Bons estudos!"),
]
