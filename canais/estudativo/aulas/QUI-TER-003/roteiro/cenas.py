# Estudativo · QUI-TER-003 — Energia de ligação (Química · Termoquímica e Cinética · Entalpia, Hess e energia de ligação).
# Habilidade: calcular o ΔH de uma reação somando o que se gasta para quebrar ligações e o que se libera ao formar novas.
# Pré-requisitos: QUI-TER-001, QUI-LIG-002. Próxima: QUI-TER-004 (velocidade média de uma reação).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas letra a letra (Cl = "cê éle"); ligações pelo nome dos elementos ("carbono-hidrogênio"), para a voz não fundir letras.
# Mol não está em "Já ensinado": a tabela vem em kJ/mol, e o mol é citado como assunto de outra aula.
# Energias de ligação usadas (tabela usual de vestibular, kJ/mol): H–H 436, Cl–Cl 243, H–Cl 431, C–H 413, C–Cl 328,
# O=O 498, C=O 799, O–H 463. H₂ + Cl₂ → 2 HCl: 679 − 862 = −183 (tabela: −184,6). CH₄ + Cl₂ → CH₃Cl + HCl: 656 − 759 = −103.
# CH₄ + 2 O₂ → CO₂ + 2 H₂O (g): 2648 − 3450 = −802 (valor real com água gasosa: −802).

TITULO = "Energia de ligação"

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
    dict(id="s01", block="gancho", text="{a}Para separar os dois átomos de uma molécula de hidrogênio, [p=0.1] {b}é preciso gastar energia. [p=0.3] {c}Mesmo assim, quando o hidrogênio queima, sobra energia para empurrar um foguete. [p=0.3] {d}Se quebrar gasta, de onde vem essa energia?"),
    dict(id="s02", block="gancho", text="{a}A resposta está nas ligações. [p=0.2] Até o fim da aula, você vai {b}calcular o delta agá de uma reação [p=0.1] {c}só com uma tabela de energias de ligação."),
    # lembrete
    dict(id="s03", block="lembrete", text="{a}Você já sabe que delta agá negativo libera calor e positivo absorve. [p=0.2] E sabe desenhar as ligações: [p=0.1] {b}um traço é ligação simples, [p=0.1] {c}dois traços, dupla, [p=0.1] {d}três, tripla. [p=0.2] Se faltar alguma, procure no canal."),
    # quebrar e formar
    dict(id="s04", block="quebra", text="{a}Uma ligação é como dois ímãs grudados. [p=0.2] {b}Para separar, você gasta energia. [p=0.2] {c}Quebrar ligação sempre absorve energia. [p=0.3] {d}Quando os ímãs se juntam de novo, a energia volta: [p=0.1] {e}formar ligação sempre libera energia."),
    dict(id="s05", block="quebra", text="{a}A energia de ligação é quanto custa quebrar uma ligação. [p=0.2] {b}A energia da ligação hidrogênio-hidrogênio é quatrocentos e trinta e seis quilojoules por mol. [p=0.2] {c}O mol é um pacote de partículas, assunto de outra aula: [p=0.1] aqui, basta o número da tabela, que vem pronta na questão. [p=0.3] {d}Formar a mesma ligação libera o mesmo valor."),
    dict(id="s06", block="quebra", text="{a}Toda reação quebra as ligações dos reagentes [p=0.1] {b}e forma as dos produtos. [p=0.2] Então: [p=0.1] {c}delta agá é o que se gasta quebrando, menos o que se libera formando. [p=0.3] {d}Se formar libera mais do que quebrar custou, sobra energia: [p=0.1] exotérmica."),
    # exemplo resolvido
    dict(id="s07", block="exemplo", text="Veja a formação do cloreto de hidrogênio: [p=0.1] {a}agá dois mais cê éle dois formam dois agá cê éle. [p=0.3] Tabela: {b}hidrogênio-hidrogênio, quatrocentos e trinta e seis. [p=0.1] {c}Cloro-cloro, duzentos e quarenta e três. [p=0.1] {d}Hidrogênio-cloro, quatrocentos e trinta e um."),
    dict(id="s08", block="exemplo", text="{a}Quebrar: uma hidrogênio-hidrogênio e uma cloro-cloro. [p=0.1] {b}Quatrocentos e trinta e seis mais duzentos e quarenta e três {c}dá seiscentos e setenta e nove. [p=0.3] {d}Formar: o coeficiente dois diz que são duas ligações hidrogênio-cloro. [p=0.1] {e}Duas vezes quatrocentos e trinta e um {f}dá oitocentos e sessenta e dois."),
    dict(id="s09", block="exemplo", text="{a}Seiscentos e setenta e nove menos oitocentos e sessenta e dois {b}dá menos cento e oitenta e três quilojoules. [p=0.3] {c}Negativo: formar as ligações novas liberou mais do que quebrar as velhas custou. [p=0.3] {d}E está aí a resposta do começo: [p=0.1] a energia do foguete vem das ligações novas da água, [p=0.1] que liberam mais do que custou quebrar as velhas."),
    # erro comum
    dict(id="s10", block="erro", text="{a}O erro mais comum é esquecer o coeficiente. [p=0.2] {b}Quem conta uma ligação hidrogênio-cloro só faz seiscentos e setenta e nove menos quatrocentos e trinta e um [p=0.1] {c}e acha mais duzentos e quarenta e oito: [p=0.1] {d}endotérmica, com o sinal trocado. [p=0.3] {e}Conte todas as ligações, molécula por molécula."),
    dict(id="s11", block="erro", text="{a}Outro cuidado: a ligação dupla tem valor próprio na tabela. [p=0.2] {b}Ó dois tem uma dupla entre os oxigênios. [p=0.1] {c}Cê ó dois tem duas duplas, carbono com oxigênio. [p=0.2] {d}Desenhe a estrutura antes de contar."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.2] {a}conte só as ligações que mudam. [p=0.2] {b}Ligação que existe igualzinha dos dois lados se cancela. [p=0.3] {c}Cê agá quatro mais cê éle dois forma cê agá três cê éle mais agá cê éle. [p=0.2] {d}Três ligações carbono-hidrogênio não mudam. [p=0.2] {e}Só quebra uma carbono-hidrogênio e uma cloro-cloro, [p=0.1] {f}e só forma uma carbono-cloro e uma hidrogênio-cloro."),
    dict(id="s13", block="atalho", text="{a}Quatrocentos e treze mais duzentos e quarenta e três {b}dá seiscentos e cinquenta e seis. [p=0.2] {c}Trezentos e vinte e oito mais quatrocentos e trinta e um {d}dá setecentos e cinquenta e nove. [p=0.2] {e}A diferença dá menos cento e três. [p=0.3] {f}Funciona porque quebrar e formar a mesma ligação se anulam. [p=0.2] {g}Atenção: se uma simples vira dupla, ela não é igual, [p=0.1] e entra na conta."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Na queima do metano, cê agá quatro mais dois ó dois formam cê ó dois mais dois agá dois ó, [p=0.1] {b}tudo gás. [p=0.3] {c}Use a tabela da tela, com as quatro ligações. [p=0.2] {d}Quanto vale o delta agá?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Quebrar: quatro carbono-hidrogênio [p=0.1] e uma dupla em cada ó dois, duas no total. [p=0.2] {b}Mil seiscentos e cinquenta e dois mais novecentos e noventa e seis {c}dá dois mil seiscentos e quarenta e oito. [p=0.3] {d}Formar: duas duplas carbono-oxigênio e quatro oxigênio-hidrogênio, duas em cada água. [p=0.2] {e}Mil quinhentos e noventa e oito mais mil oitocentos e cinquenta e dois {f}dá três mil quatrocentos e cinquenta."),
    dict(id="s17", block="resposta", text="{a}Dois mil seiscentos e quarenta e oito menos três mil quatrocentos e cinquenta {b}dá menos oitocentos e dois quilojoules. [p=0.3] {c}Exotérmica, como toda queima."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}quebrar ligação gasta, formar libera, [p=0.2] {b}e o delta agá é o que se gasta menos o que se libera. [p=0.2] {c}Conte cada ligação, com os coeficientes."),
    dict(id="s19", block="fim", text="Na próxima aula, a pergunta muda: [p=0.1] {a}não quanto, mas com que rapidez. [p=0.2] {b}Você vai calcular a velocidade média de uma reação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
