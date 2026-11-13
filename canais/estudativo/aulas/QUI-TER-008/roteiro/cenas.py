# Estudativo · QUI-TER-008 — Praticando: energia e velocidade das reações (Química · Termoquímica e Cinética · prática).
# Habilidade: calcular ΔH e interpretar gráficos de energia e de velocidade em questões de prova.
# Pré-requisitos: QUI-TER-001 a QUI-TER-007. Próxima: nenhuma na trilha (a ponte vai para a trilha de equilíbrio, QUI-EQL-001).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Cinco questões inéditas, criadas para esta aula.
# Q1 diagrama: reagentes 40, produtos 100, topo 140 / 90 ⇒ Ea 100 / 50, ΔH +60 (endo, vizinhança esfria).
# Q2 Hess: C + O₂ → CO₂ −394; H₂ + ½O₂ → H₂O(l) −286; CH₄ + 2O₂ → CO₂ + 2H₂O(l) −890 ⇒ C + 2H₂ → CH₄: −394 − 572 + 890 = −76
# (tabela: −74,8). Q3 ligação: N≡N 945, H–H 436, N–H 391 ⇒ 2253 − 2346 = −93 (tabela: −92).
# Q4 velocidade: 2 N₂O₅ → 4 NO₂ + O₂; [N₂O₅] 1,2 → 0,8 em 5 min ⇒ 0,08; NO₂ 0,16; reação 0,04.
# Q5 ordem: 2 NO + Cl₂ → 2 NOCl, lei real v = k[NO]²[Cl₂]; NO dobra: v 3 → 12; Cl₂ dobra: v 12 → 24.

TITULO = "Praticando: energia e velocidade das reações"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões, [p=0.1] {b}uma para cada ferramenta da trilha. [p=0.3] {c}Diagrama, Hess, ligações, velocidade e ordem. [p=0.3] {d}Em cada uma, pause, tente, e só depois veja a resolução."),
    # lembrete: a caixa de ferramentas
    dict(id="s02", block="lembrete", text="{a}A caixa de ferramentas: [p=0.2] {b}delta agá é chegada menos partida, [p=0.1] e a energia de ativação é topo menos reagentes. [p=0.2] {c}Na lei de Hess, inverteu, troca o sinal; multiplicou, multiplica. [p=0.2] {d}Nas ligações, delta agá é quebrar menos formar. [p=0.2] {e}Velocidade média é quanto a concentração mudou, dividido pelo tempo, [p=0.1] e a ordem sai da tabela, nunca dos coeficientes."),
    # questão 1: diagrama
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Num diagrama de entalpia, {b}os reagentes estão na marca de quarenta quilojoules [p=0.1] e {c}os produtos, na de cem. [p=0.2] {d}O topo do morro fica em cento e quarenta, [p=0.1] {e}e em noventa com catalisador. [p=0.3] {f}Ache a energia de ativação com e sem catalisador, o delta agá, [p=0.1] e diga se a vizinhança esquenta ou esfria."),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="{a}Sem catalisador: cento e quarenta menos quarenta {b}dá cem. [p=0.2] {c}Com catalisador: noventa menos quarenta {d}dá cinquenta. [p=0.3] {e}Delta agá: cem menos quarenta {f}dá mais sessenta, endotérmica. [p=0.2] {g}A reação puxa calor, e a vizinhança esfria. [p=0.2] {h}O catalisador só mudou o topo."),
    # questão 2: Hess
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] {b}Ache o delta agá de cê mais dois agá dois formando cê agá quatro, o metano. [p=0.3] Use três equações. [p=0.1] {c}Cê mais oxigênio dá cê ó dois: menos trezentos e noventa e quatro quilojoules. [p=0.2] {d}Agá dois mais meio oxigênio dá água líquida: menos duzentos e oitenta e seis. [p=0.2] {e}E a queima do metano, que forma cê ó dois e duas águas: menos oitocentos e noventa."),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="r2", text="{a}Comece pelo que aparece uma vez só. [p=0.2] {b}O cê está nos reagentes da primeira: ela fica. [p=0.2] {c}O alvo tem dois agá dois: multiplique a segunda por dois, [p=0.1] {d}e o delta agá vira menos quinhentos e setenta e dois. [p=0.3] {e}O metano está nos reagentes da terceira, mas o alvo o quer nos produtos: [p=0.1] {f}inverta, e vira mais oitocentos e noventa."),
    dict(id="s09", block="r2", text="{a}Na soma, o gás carbônico, a água e o oxigênio se cancelam. [p=0.3] {b}Menos trezentos e noventa e quatro, menos quinhentos e setenta e dois, mais oitocentos e noventa: [p=0.2] {c}dá menos setenta e seis quilojoules."),
    # questão 3: energia de ligação
    dict(id="s10", block="q3", text="{a}Questão três. [p=0.2] {b}Na síntese da amônia, ene dois mais três agá dois formam dois ene agá três. [p=0.3] {c}Tabela, em quilojoules por mol: a tripla entre os nitrogênios vale novecentos e quarenta e cinco. [p=0.1] {d}Hidrogênio-hidrogênio, quatrocentos e trinta e seis. [p=0.1] {e}Nitrogênio-hidrogênio, trezentos e noventa e um. [p=0.2] {f}Calcule o delta agá."),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="{a}Quebrar: uma tripla e três hidrogênio-hidrogênio. [p=0.2] {b}Novecentos e quarenta e cinco mais mil trezentos e oito {c}dá dois mil duzentos e cinquenta e três. [p=0.3] {d}Formar: cada amônia tem três ligações nitrogênio-hidrogênio, [p=0.1] {e}e são duas amônias: seis ligações. [p=0.2] {f}Seis vezes trezentos e noventa e um {g}dá dois mil trezentos e quarenta e seis."),
    dict(id="s13", block="r3", text="{a}Dois mil duzentos e cinquenta e três menos dois mil trezentos e quarenta e seis {b}dá menos noventa e três quilojoules. [p=0.3] {c}Quem contou três ligações em vez de seis achou mais mil e oitenta, [p=0.1] com o sinal errado."),
    # questão 4: velocidade média
    dict(id="s14", block="q4", text="{a}Questão quatro. [p=0.2] {b}Na reação em que duas moléculas de ene dois ó cinco formam quatro de ene ó dois e uma de oxigênio, [p=0.2] {c}o gráfico mostra a concentração de ene dois ó cinco caindo de um vírgula dois para zero vírgula oito mol por litro em cinco minutos. [p=0.3] {d}Ache a velocidade de consumo do ene dois ó cinco, [p=0.1] {e}a de formação do ene ó dois [p=0.1] {f}e a da reação."),
    dict(id="s15", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="r4", text="{a}Caiu zero vírgula quatro em cinco minutos: [p=0.1] {b}zero vírgula quatro dividido por cinco {c}dá zero vírgula zero oito mol por litro por minuto. [p=0.3] {d}O ene ó dois tem coeficiente quatro, contra o dois do ene dois ó cinco: [p=0.1] {e}vezes dois, dá zero vírgula dezesseis. [p=0.3] {f}A da reação divide pelo coeficiente: [p=0.1] {g}zero vírgula zero oito dividido por dois dá zero vírgula zero quatro."),
    # questão 5: ordem de reação
    dict(id="s17", block="q5", text="{a}Questão cinco. [p=0.2] {b}Na reação do ene ó com o cê éle dois, que forma ene ó cê éle, veja a tabela. [p=0.3] {c}Dobrando o ene ó, com o cloro igual, a velocidade vai de três para doze. [p=0.2] {d}Dobrando o cê éle dois, com o ene ó igual, vai de doze para vinte e quatro. [p=0.3] {e}Escreva a lei da velocidade [p=0.1] {f}e diga o que acontece com o cá se a temperatura subir."),
    dict(id="s18", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="r5", text="{a}Ene ó dobrou e a velocidade foi a quatro vezes: [p=0.1] {b}ordem dois. [p=0.2] {c}Cê éle dois dobrou e a velocidade dobrou: [p=0.1] {d}ordem um. [p=0.3] {e}Vê igual a cá, vezes ene ó ao quadrado, vezes cê éle dois. [p=0.3] {f}Esquentando, mais colisões têm a energia de ativação: [p=0.1] {g}o cá aumenta, e a reação acelera."),
    # fechamento
    dict(id="s20", block="fim", text="{a}Se você acertou três das cinco, a trilha está no lugar. [p=0.2] {b}Errou alguma? [p=0.1] Volte na aula daquela ferramenta e refaça a questão."),
    dict(id="s21", block="fim", text="Com isso, a energia e a velocidade das reações estão fechadas. [p=0.2] {a}A próxima trilha é o equilíbrio químico: [p=0.1] {b}reações que andam nos dois sentidos ao mesmo tempo, [p=0.1] e a constante que mede onde elas param. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
