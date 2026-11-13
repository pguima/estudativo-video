# Estudativo · QUI-MIS-009 — Praticando: escolher o método de separação (Química · Matéria e Misturas · Separação de misturas).
# Habilidade: montar a sequência de métodos para separar uma mistura de três componentes.
# Pré-requisitos: QUI-MIS-006, QUI-MIS-007, QUI-MIS-008. Próxima: fim da trilha; a próxima aula de Química do Zero é
# QUI-ATO-001 (modelos de Dalton e Thomson).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: quatro questões inéditas, criadas para esta aula.
# Q1 areia + sal + limalha de ferro: ímã → água → filtração → evaporação (ou destilação simples, se quiser a água).
# Q2 água + óleo + areia: filtração (a areia fica) → funil de decantação (sai a água primeiro).
# Q3 serragem + areia + sal: água → a serragem boia (flotação, retira por cima) → filtrar a areia → evaporar a água.
# Q4 água + álcool + sal: uma destilação fracionada: álcool a cerca de 78 °C (sai a 96%), depois água a 100 °C, sal no balão.

TITULO = "Praticando: escolher o método de separação"

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
    dict(id="s01", block="gancho", text="{a}Areia, sal e ferro em pó, tudo misturado. [p=0.3] {b}Você conhece todos os métodos para separar, [p=0.1] mas a ordem errada estraga tudo. [p=0.3] {c}Hoje são quatro misturas de três componentes, e a gente monta a sequência de cada uma."),
    dict(id="s02", block="gancho", text="Você vai precisar dos {a}métodos para sólidos, [p=0.1] {b}de decantar e filtrar [p=0.1] {c}e da destilação. [p=0.3] Se faltar alguma dessas aulas, procure no canal."),
    # estratégia
    dict(id="s03", block="estrategia", text="Antes, uma estratégia que serve para todas. [p=0.2] {a}Primeiro, o que funciona com a mistura seca, como o ímã e a peneira. [p=0.3] {b}Depois, a água, se precisar dissolver alguma coisa. [p=0.3] {c}Em seguida, separe o sólido do líquido. [p=0.2] {d}E, por último, o que usa fogo."),
    dict(id="s04", block="estrategia", text="Funciona porque {a}a água estraga os métodos a seco: [p=0.1] areia molhada não passa na peneira e gruda no ferro, e o ímã puxa os dois juntos. [p=0.3] {b}E o fogo vem no fim porque gasta energia e só é preciso para separar o que está dissolvido."),
    # Q1
    dict(id="s05", block="q1", text="{a}Questão um. [p=0.2] {b}Areia, sal e limalha de ferro, aquele ferro em pó. [p=0.3] {c}Que métodos, e em que ordem?"),
    dict(id="s06", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s07", block="q1", text="{a}Primeiro, com a mistura seca, o ímã tira o ferro: [p=0.1] {b}separação magnética. [p=0.3] {c}Sobram areia e sal. [p=0.2] {d}Ponha água e mexa: o sal dissolve, a areia não. [p=0.2] Dissolução fracionada."),
    dict(id="s08", block="q1", text="{a}Passe no filtro: a areia fica presa, a água salgada passa. [p=0.3] {b}Por fim, evapore a água, e o sal fica. [p=0.3] {c}Se quiser guardar a água também, troque a evaporação pela destilação simples. [p=0.3] {d}Quem pôs água primeiro ficou com ferro molhado e grudado na areia."),
    # Q2
    dict(id="s09", block="q2", text="{a}Questão dois. [p=0.2] {b}Água, óleo e areia. [p=0.3] {c}Monte a sequência."),
    dict(id="s10", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="q2", text="{a}A areia é o único sólido, então comece por ela: [p=0.1] {b}filtração. [p=0.3] {c}A areia fica no filtro; a água e o óleo passam juntos. [p=0.3] {d}Os dois líquidos não se misturam: [p=0.1] {e}funil de decantação. [p=0.2] {f}Abre a torneira, sai a água, que é mais densa, e o óleo fica."),
    # Q3
    dict(id="s12", block="q3", text="{a}Questão três. [p=0.2] {b}Serragem, areia e sal. [p=0.3] {c}E agora?"),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="q3", text="{a}A seco, até daria para soprar a serragem, a ventilação. [p=0.2] Mas aqui a água resolve duas coisas de uma vez. [p=0.2] {b}Ponha a mistura na água: [p=0.1] {c}a serragem boia, [p=0.1] {d}a areia afunda [p=0.1] {e}e o sal dissolve."),
    dict(id="s15", block="q3", text="{a}Retire a serragem de cima: flotação. [p=0.3] {b}Filtre, e a areia fica no filtro. [p=0.3] {c}Evapore a água, e sobra o sal. [p=0.3] {d}Três componentes, três passos depois da água."),
    # Q4
    dict(id="s16", block="q4", text="{a}Questão quatro. [p=0.2] {b}Água, álcool e sal dissolvido, tudo numa mistura homogênea. [p=0.3] {c}Qual é a sequência?"),
    dict(id="s17", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="q4", text="{a}Filtro não adianta: é tudo homogêneo. [p=0.3] {b}Uma destilação fracionada separa quase tudo. [p=0.3] {c}Sai primeiro o álcool, perto de setenta e oito graus. [p=0.2] {d}Depois, a água, a cem. [p=0.2] {e}E o sal, que não ferve, fica no balão."),
    dict(id="s19", block="q4", text="{a}Um detalhe que a prova adora: [p=0.1] o álcool sai com noventa e seis por cento, [p=0.1] {b}porque álcool e água formam uma mistura azeotrópica. [p=0.3] {c}Uma sequência de um passo só, com esse limite."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}primeiro o que é a seco, [p=0.1] {b}depois a água, [p=0.1] {c}depois separa sólido de líquido [p=0.1] {d}e, por último, o fogo."),
    dict(id="s21", block="fim", text="Com isso, você fecha a trilha de substâncias e misturas. [p=0.3] {a}A próxima trilha entra no átomo: [p=0.1] {b}como os cientistas descobriram o que tem lá dentro, começando por Dalton e Thomson. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
