# Estudativo · QUI-TER-001 — Exotérmica, endotérmica e ΔH (Química · Termoquímica e Cinética · Entalpia, Hess e energia de ligação).
# Habilidade: dizer pelo sinal de ΔH se a reação libera ou absorve energia, ler um diagrama de entalpia e explicar por que a
# bolsa instantânea gelada é endotérmica.
# Pré-requisitos: QUI-MIS-003, QUI-INO-008, MAT-NUM-016, FIS-CAL-001. Próxima: QUI-TER-002 (lei de Hess).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas narradas letra a letra: H₂ = "agá dois", NH₄NO₃ = "ene agá quatro ene ó três"; ΔH = "delta agá".
# Mol ainda não foi ensinado (não está em "Já ensinado"): o ΔH vale "para as quantidades escritas na equação".
# Fatos: 2 H₂(g) + O₂(g) → 2 H₂O(l), ΔH = −572 kJ (2 × −286 kJ, entalpia de formação da água líquida);
# compressa fria = dissolução do nitrato de amônio, endotérmica; o kJ aparece no rótulo nutricional ao lado da kcal.

TITULO = "Exotérmica, endotérmica e ΔH"

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
    dict(id="s01", block="gancho", text="{a}Você aperta uma bolsa de plástico [p=0.1] e, em segundos, ela fica {b}gelada, sem geladeira nenhuma. [p=0.3] É a compressa instantânea, a das lesões no esporte. [p=0.3] {c}Ela libera ou absorve energia? [p=0.3] {d}A resposta que parece óbvia está errada."),
    dict(id="s02", block="gancho", text="{a}Até o fim da aula, você vai ler {b}o sinal do delta agá, [p=0.2] {c}um diagrama de entalpia [p=0.2] e {d}desvendar essa bolsa."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar três ideias. [p=0.2] {a}Calor é energia que passa do mais quente para o mais frio. [p=0.2] {b}Derreter e ferver absorvem calor. [p=0.2] E {c}um número negativo fica abaixo do zero, como uma dívida. [p=0.2] Se faltar alguma, procure no canal."),
    # sistema e vizinhança
    dict(id="s04", block="sistema", text="Comece separando o mundo em dois. [p=0.2] {a}O sistema é a reação: as substâncias que se transformam. [p=0.2] {b}A vizinhança é tudo em volta: [p=0.1] o ar, o plástico, a sua mão. [p=0.3] {c}A energia passa de um para o outro."),
    dict(id="s05", block="sistema", text="Pense na chama do fogão. [p=0.2] {a}O gás queima e {b}a panela esquenta. [p=0.3] A reação {c}soltou calor para a vizinhança. [p=0.2] Ela é {d}exotérmica: [p=0.1] {e}exo quer dizer para fora."),
    dict(id="s06", block="sistema", text="O contrário também existe. [p=0.2] {a}No processo endotérmico, o sistema puxa calor da vizinhança, [p=0.2] e {b}o que está em volta esfria. [p=0.2] {c}Endo quer dizer para dentro. [p=0.3] {d}Derreter o gelo é endotérmico: [p=0.1] ele tira calor do copo e da sua mão."),
    # entalpia e ΔH
    dict(id="s07", block="dh", text="Para medir essa troca, a Química usa a {a}entalpia, escrita com um agá maiúsculo, [p=0.1] que aqui não é o hidrogênio. [p=0.2] Ela é a energia guardada nas substâncias. [p=0.3] {b}Ninguém mede a entalpia sozinha, [p=0.1] só {c}a variação dela: o delta agá. [p=0.2] Delta é a letra grega que indica variação."),
    dict(id="s08", block="dh", text="{a}Delta agá é a entalpia dos produtos menos a dos reagentes. [p=0.2] {b}Chegada menos partida. [p=0.3] {c}Na exotérmica, a energia saiu, [p=0.1] e os produtos ficaram com menos: [p=0.1] {d}delta agá negativo. [p=0.3] {e}Na endotérmica, a energia entrou: [p=0.1] {f}delta agá positivo."),
    dict(id="s09", block="dh", text="{a}É como o saldo de uma conta. [p=0.2] {b}Pagou, o saldo desce. [p=0.1] {c}Recebeu, o saldo sobe. [p=0.2] O saldo é o da reação: [p=0.1] o que ela perde, a vizinhança ganha."),
    # exemplo
    dict(id="s10", block="exemplo", text="Veja a queima do hidrogênio, um combustível de foguete. [p=0.2] {a}Dois agá dois mais ó dois formam duas moléculas de água. [p=0.3] {b}Delta agá igual a menos quinhentos e setenta e dois quilojoules. [p=0.3] {c}Quilojoule é unidade de energia, [p=0.1] a mesma que aparece no rótulo dos alimentos, ao lado das quilocalorias."),
    dict(id="s11", block="exemplo", text="{a}O sinal é negativo, então a reação libera energia: [p=0.1] {b}é exotérmica. [p=0.3] E o número vale {c}para as quantidades escritas na equação."),
    # diagrama
    dict(id="s12", block="diagrama", text="Isso cabe num desenho, o {a}diagrama de entalpia. [p=0.2] {b}O eixo de pé é a entalpia: [p=0.1] quanto mais alto, mais energia guardada, [p=0.1] e o zero é só uma referência combinada. [p=0.2] {c}Os reagentes ficam num degrau, [p=0.1] {d}os produtos em outro, [p=0.2] e {e}a seta vai da partida até a chegada."),
    dict(id="s13", block="diagrama", text="Na queima do hidrogênio, {a}os produtos ficam abaixo dos reagentes. [p=0.2] {b}A seta desce: [p=0.1] delta agá negativo, exotérmica. [p=0.3] {c}Se os produtos ficassem acima, a seta subiria: [p=0.1] {d}delta agá positivo, endotérmica. [p=0.3] {e}O caminho entre os degraus, com um morro no meio, é assunto de outra aula."),
    # a bolsa (erro comum)
    dict(id="s14", block="bolsa", text="{a}De volta à bolsa gelada. [p=0.2] Dentro dela há água e um pó, {b}o nitrato de amônio, ene agá quatro ene ó três. [p=0.2] Ao apertar, {c}o sal se dissolve na água."),
    dict(id="s15", block="bolsa", text="{a}O erro comum é pensar assim: [p=0.1] ficou fria, então soltou frio, então é exotérmica. [p=0.3] {b}Mas frio não é uma coisa que sai. [p=0.2] {c}A bolsa esfria porque perde calor."),
    dict(id="s16", block="bolsa", text="{a}Perde para onde? [p=0.1] Para o nitrato se dissolver, {b}a mistura puxa calor do plástico e da sua pele. [p=0.3] {c}A vizinhança perde calor e esfria. [p=0.2] O sistema ganhou energia: [p=0.1] {d}endotérmica, delta agá positivo."),
    # atalho
    dict(id="s17", block="atalho", text="O atalho de prova: [p=0.2] {a}o sinal do delta agá é o contrário do que o termômetro de fora mostra. [p=0.3] {b}Esquentou em volta? [p=0.1] A reação soltou calor: delta agá negativo. [p=0.2] {c}Esfriou em volta? [p=0.1] Ela puxou calor: delta agá positivo."),
    dict(id="s18", block="atalho", text="Funciona porque {a}o delta agá é contado do lado da reação, não do seu. [p=0.3] {b}Nem precisa do termômetro quando a questão dá o diagrama ou os números: [p=0.2] aí, {c}faça chegada menos partida."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Num diagrama de entalpia, {a}os reagentes estão na marca de cento e vinte quilojoules [p=0.1] e {b}os produtos, na de quarenta. [p=0.3] {c}Quanto vale o delta agá? [p=0.2] {d}A reação é exotérmica ou endotérmica? [p=0.2] E {e}a vizinhança esquenta ou esfria?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="{a}Chegada menos partida: [p=0.1] {b}quarenta menos cento e vinte {c}dá menos oitenta quilojoules. [p=0.3] {d}Negativo: exotérmica. [p=0.2] {e}A seta desce, e a vizinhança esquenta."),
    dict(id="s22", block="resposta", text="{a}Quem fez cento e vinte menos quarenta achou mais oitenta [p=0.1] e chamou de endotérmica. [p=0.2] {b}A ordem importa: [p=0.1] sempre produtos menos reagentes."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: [p=0.1] {a}delta agá negativo, a reação libera calor e a vizinhança esquenta. [p=0.2] {b}Delta agá positivo, ela absorve calor e a vizinhança esfria, [p=0.1] como na bolsa gelada."),
    dict(id="s24", block="fim", text="Na próxima aula, a {a}lei de Hess: [p=0.2] {b}achar o delta agá de uma reação somando outras equações, como peças de um quebra-cabeça. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
