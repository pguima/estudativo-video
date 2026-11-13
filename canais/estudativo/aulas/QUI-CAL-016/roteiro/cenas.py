# Estudativo · QUI-CAL-016 — Difusão de gases: lei de Graham (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: dizer qual gás se espalha mais rápido comparando as massas molares.
# Pré-requisitos: QUI-CAL-012, MAT-POT-007. Próxima: QUI-CAL-015 (praticando: estudo dos gases).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# ATENÇÃO: QUI-CAL-013, QUI-CAL-014 e porcentagem NÃO estão em "Já ensinado" desta aula. Energia cinética também não:
# o motivo físico fica na comparação das bolas, sem fórmula.
# Fatos: tubo com NH₃ e HCl → anel branco de NH₄Cl mais perto do HCl (√(36,5/17) ≈ 1,47); v ∝ 1/√M.
# Contas: √(32/2) = √16 = 4; erro: 16 vezes; questão √(16/4) = √4 = 2 (hélio). Tempo é o inverso da velocidade.

TITULO = "Difusão de gases: lei de Graham"

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
    dict(id="s01", block="gancho", text="{a}Num tubo de vidro, ponha um algodão com amônia numa ponta [p=0.1] {b}e um algodão com ácido clorídrico na outra. [p=0.3] {c}Os vapores andam um em direção ao outro, [p=0.1] {d}e, onde se encontram, aparece um anel branco, [p=0.1] um pó que se forma quando os dois gases reagem. [p=0.3] {e}Ele nunca nasce no meio. [p=0.2] {f}Nasce mais perto do ácido. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}dizer qual gás se espalha mais rápido [p=0.2] e {c}quantas vezes mais rápido, pela lei de Graham, [p=0.2] com um {d}atalho de raiz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a massa molar de um gás, [p=0.2] e {c}a raiz quadrada exata, como a raiz de dezesseis, que dá quatro. [p=0.3] Se faltar alguma, procure no canal."),
    # difusão
    dict(id="s04", block="difusao", text="{a}Abra um perfume num canto da sala, e logo o cheiro chega ao outro canto. [p=0.3] {b}As partículas do perfume se espalham entre as do ar: [p=0.1] {c}isso é difusão. [p=0.3] {d}Quando o gás escapa por um furinho, como o ar de um balão, [p=0.1] {e}o nome é efusão. [p=0.2] As duas seguem a mesma regra."),
    # por que
    dict(id="s05", block="porque", text="{a}Na mesma temperatura, as partículas de qualquer gás têm, em média, a mesma agitação. [p=0.3] {b}Pense numa bola de pingue-pongue e numa de boliche, chutadas do mesmo jeito. [p=0.2] {c}A leve sai voando. [p=0.1] {d}A pesada anda devagar, [p=0.1] mas não na proporção das massas: entra uma raiz. [p=0.3] {e}Gás de massa molar menor anda mais rápido."),
    # a lei
    dict(id="s06", block="lei", text="{a}A lei de Graham diz quanto: [p=0.1] {b}a velocidade de um gás é inversamente proporcional à raiz quadrada da massa molar dele. [p=0.3] {c}Para comparar dois gases, aqui vê é a velocidade, não o volume: [p=0.1] {d}vê um sobre vê dois igual à raiz da fração eme dois sobre eme um. [p=0.3] {e}Repare: as massas aparecem trocadas. [p=0.2] {f}A massa do outro gás vai em cima."),
    dict(id="s07", block="lei", text="{a}Hidrogênio contra oxigênio. [p=0.2] {b}O agá dois tem massa molar dois; [p=0.1] {c}o ó dois tem trinta e dois. [p=0.3] {d}Raiz de trinta e dois sobre dois: [p=0.1] raiz de dezesseis, [p=0.1] {e}que dá quatro. [p=0.3] {f}O hidrogênio se espalha quatro vezes mais rápido que o oxigênio."),
    dict(id="s08", block="lei", text="{a}Volte ao tubo. [p=0.2] {b}A amônia, ene agá três, tem massa molar dezessete. [p=0.2] {c}O ácido, agá cê ele, tem trinta e seis e meio. [p=0.3] {d}A amônia é mais leve, anda mais rápido [p=0.1] e percorre mais tubo até o encontro. [p=0.2] {e}Por isso, o anel nasce mais perto do ácido."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}esquecer a raiz. [p=0.2] {b}Trinta e dois dividido por dois dá dezesseis, [p=0.1] e a pessoa responde {c}dezesseis vezes mais rápido. [p=0.3] {d}A massa dezesseis vezes menor deixa o gás só quatro vezes mais rápido: [p=0.1] {e}a raiz de dezesseis."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho: [p=0.1] {a}guarde a raiz das razões redondas. [p=0.3] {b}Massa quatro vezes maior: [p=0.1] metade da velocidade. [p=0.2] {c}Nove vezes maior: [p=0.1] um terço. [p=0.2] {d}Dezesseis vezes maior: [p=0.1] um quarto."),
    dict(id="s11", block="atalho", text="{a}E o tempo para percorrer o mesmo caminho é o contrário da velocidade: [p=0.1] {b}quem é duas vezes mais rápido leva metade do tempo. [p=0.3] {c}Funciona porque tudo é a raiz da razão das massas. [p=0.2] {d}Não compensa quando a raiz não é exata, [p=0.1] como trinta e seis e meio dividido por dezessete: [p=0.1] {e}aí, basta dizer quem é mais rápido, ou estimar a raiz."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}Dois balões iguais: um com hélio, de massa molar quatro, [p=0.1] {b}e outro com metano, de massa molar dezesseis. [p=0.3] {c}Qual murcha primeiro? [p=0.1] {d}E quantas vezes mais rápido o gás dele escapa?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}O hélio é mais leve: [p=0.1] {b}o balão de hélio murcha primeiro. [p=0.3] {c}Raiz de dezesseis sobre quatro: [p=0.1] raiz de quatro, [p=0.1] {d}que dá dois. [p=0.2] {e}O hélio escapa duas vezes mais rápido que o metano."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}gás mais leve se espalha mais rápido; [p=0.2] {b}a razão das velocidades é a raiz da razão das massas molares, [p=0.1] {c}com as massas trocadas."),
    dict(id="s16", block="fim", text="Na próxima aula, você pratica: [p=0.2] {a}balões, pneus e cilindros, [p=0.1] {b}com as equações dos gases em questões de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
