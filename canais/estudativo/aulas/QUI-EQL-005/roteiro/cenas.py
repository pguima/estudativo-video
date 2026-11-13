# Estudativo · QUI-EQL-005 — Hidrólise salina (Química · Equilíbrio Químico · pH, hidrólise, tampão e Kps).
# Habilidade: prever se NaCl, NH₄Cl e NaHCO₃ deixam a água neutra, ácida ou básica pela regra do forte vence.
# Pré-requisitos: QUI-EQL-004, QUI-INO-003. Próxima: QUI-EQL-006 (solução tampão).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Le Chatelier (EQL-002) não está em "Já ensinado": a hidrólise é explicada pelo Brønsted (INO-013), sem deslocamento.
# Fatos: NaCl pH 7; NaHCO₃ 0,1 mol/L pH ≈ 8,3 (antiácido); NH₄Cl 0,1 mol/L pH ≈ 5,1. Hidrólise: NH₄⁺ + H₂O ⇌ NH₃ + H₃O⁺;
# HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻. Questão: KNO₃ neutro; Na₂CO₃ básico; NH₄NO₃ ácido. Ambos fracos (acetato de amônio): depende de Ka e Kb.

TITULO = "Hidrólise salina"

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
    dict(id="s01", block="gancho", text="{a}Sal de cozinha na água: pê agá sete. [p=0.2] {b}Bicarbonato de sódio na água: pê agá acima de sete, básico. [p=0.2] {c}Cloreto de amônio: abaixo de sete, ácido. [p=0.3] {d}Três sais, três resultados. [p=0.2] Como prever sem medir?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai prever se um sal deixa a água {a}neutra, ácida ou básica, [p=0.2] {b}pela regra do forte vence."),
    # lembrete
    dict(id="s03", block="lembrete", text="{a}Todo sal nasce de um ácido com uma base, na neutralização. [p=0.2] {b}Ácidos fortes, como o clorídrico, o nítrico e o sulfúrico, se ionizam quase por completo. [p=0.2] {c}Bases fortes são, por exemplo, os hidróxidos de sódio, potássio e cálcio. [p=0.2] {d}E, pelo jeito de Brønsted, ácido doa agá mais, e base recebe. [p=0.2] Se faltar alguma, procure no canal."),
    # os pais do sal
    dict(id="s04", block="pais", text="{a}Primeiro passo: descubra os pais do sal. [p=0.2] {b}Separe o sal em duas partes. [p=0.2] {c}A parte metálica, ou o amônio, ganha ó agá e vira a base. [p=0.2] {d}A outra parte ganha quantos agá precisar e vira o ácido."),
    dict(id="s05", block="pais", text="{a}Cloreto de sódio, ene á cê éle. [p=0.1] {b}A base é o hidróxido de sódio, forte, [p=0.1] {c}e o ácido é o clorídrico, forte. [p=0.3] {d}Cloreto de amônio, ene agá quatro cê éle. [p=0.1] {e}A base é o hidróxido de amônio, fraca, [p=0.1] {f}e o ácido, de novo o clorídrico, forte."),
    dict(id="s06", block="pais", text="{a}Bicarbonato de sódio, ene á agá cê ó três. [p=0.1] {b}A base é o hidróxido de sódio, forte; [p=0.1] {c}o ácido é o carbônico, agá dois cê ó três, fraco."),
    # a regra
    dict(id="s07", block="regra", text="{a}Agora, a regra do forte vence. [p=0.2] {b}Ácido forte com base fraca: a solução fica ácida. [p=0.2] {c}Base forte com ácido fraco: básica. [p=0.2] {d}Ambos fortes: empate, neutra."),
    dict(id="s08", block="regra", text="{a}Sal de cozinha: pais fortes, neutro. [p=0.2] {b}Cloreto de amônio: o forte é o ácido, então fica ácido. [p=0.2] {c}Bicarbonato: a forte é a base, então fica básico. [p=0.3] {d}É por isso que o bicarbonato alivia a azia: [p=0.1] ele neutraliza parte do ácido do estômago."),
    # por que funciona
    dict(id="s09", block="hidrolise", text="{a}Por que funciona? [p=0.2] {b}A parte que veio do pai fraco reage com a água. [p=0.1] {c}Essa reação se chama hidrólise. [p=0.3] {d}O amônio doa um agá mais para a água: [p=0.1] {e}forma amônia e o hidrônio, agá três ó mais, que é o agá mais preso a uma água. [p=0.2] {f}Sobra agá mais na solução: ácida."),
    dict(id="s10", block="hidrolise", text="{a}O bicarbonato faz o contrário: recebe um agá mais da água. [p=0.2] {b}Forma ácido carbônico e deixa um ó agá menos. [p=0.2] {c}Sobra ó agá menos: básica. [p=0.3] {d}A parte que veio do pai forte, como o sódio e o cloreto, não reage com a água."),
    # erro comum
    dict(id="s11", block="erro", text="{a}O erro comum: o bicarbonato tem agá na fórmula, então seria ácido. [p=0.3] {b}Não é a fórmula que decide, são os pais. [p=0.2] {c}Ácido carbônico, fraco; base, forte: [p=0.1] {d}básico."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.2] {a}o lado forte dá o resultado. [p=0.2] {b}O pai forte é o ácido? Solução ácida. [p=0.1] {c}É a base? Solução básica. [p=0.1] {d}Ambos fortes? Neutra. [p=0.3] {e}Não vale quando ambos são fracos, como no acetato de amônio: [p=0.1] {f}aí quem decide é comparar a força do ácido com a da base, e a questão precisa dar esses valores."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Diga se cada sal deixa a água neutra, ácida ou básica. [p=0.2] {a}Nitrato de potássio, cá ene ó três. [p=0.2] {b}Carbonato de sódio, ene á dois cê ó três. [p=0.2] {c}Nitrato de amônio, ene agá quatro ene ó três."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}Nitrato de potássio: hidróxido de potássio, forte, e ácido nítrico, forte. [p=0.1] {b}Neutro. [p=0.3] {c}Carbonato de sódio: base forte com ácido carbônico, fraco. [p=0.1] {d}Básico. [p=0.3] {e}Nitrato de amônio: hidróxido de amônio, fraco, com ácido nítrico, forte. [p=0.1] {f}Ácido."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}ache os pais do sal [p=0.1] {b}e deixe o forte vencer: [p=0.1] {c}ácido forte deixa ácida, base forte deixa básica, e ambos fortes, neutra."),
    dict(id="s17", block="fim", text="Na próxima aula, você vai juntar um ácido fraco com o seu sal [p=0.1] e criar {a}uma solução que segura o pê agá: [p=0.1] {b}a solução tampão, como a do seu sangue. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
