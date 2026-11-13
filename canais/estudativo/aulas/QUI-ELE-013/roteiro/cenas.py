# Estudativo · QUI-ELE-013 — Fissão e fusão nuclear (Química · Eletroquímica e Radioatividade · Radioatividade).
# Habilidade: diferenciar fissão e fusão, explicar a usina nuclear e seu lixo radioativo e dizer como a fusão nas estrelas forma
# novos elementos.
# Pré-requisitos: QUI-ELE-011. Próxima: QUI-ELE-014 (praticando: eletrólise e radioatividade).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# "Já ensinado" não tem a meia-vida (QUI-ELE-012) nem E = m·c² (FIS-MOD-011, depois): o lixo é "radioativo por milhares de
# anos" e a energia vem de "um pouco de massa que some", sem conta.
# Fissão: ²³⁵₉₂U + ¹₀n → ¹⁴¹₅₆Ba + ⁹²₃₆Kr + 3 ¹₀n (A: 236 = 141 + 92 + 3; Z: 92 = 56 + 36). Reação em cadeia; barras de controle
# (boro ou cádmio) absorvem nêutrons. Usina: o calor ferve água, o vapor gira a turbina, que gira o gerador. Brasil: Angra 1 e
# Angra 2, em Angra dos Reis (RJ). Urânio natural tem cerca de 0,7% de U-235; a usina usa cerca de 3 a 5%. Não solta CO₂ ao gerar.
# Lixo: combustível usado fica em piscinas e depósitos blindados; radioativo por milhares de anos. Acidentes: Chernobyl (1986),
# Fukushima (2011). Goiânia (1987): uma cápsula de césio-137 de um aparelho de radioterapia abandonado.
# Fusão: ²₁H + ³₁H → ⁴₂He + ¹₀n (A: 5 = 5; Z: 2 = 2). Núcleo do Sol: cerca de 15 milhões de °C. Estrelas grandes: hélio → carbono,
# oxigênio... até o ferro; os mais pesados que o ferro, em explosões de estrelas e colisões de estrelas de nêutrons.
# Questão: ²³⁵₉₂U + n → ¹⁴⁰₅₄Xe + ⁹⁴₃₈Sr + x n: 236 = 140 + 94 + x → x = 2; Z: 92 = 54 + 38. Fissão.

TITULO = "Fissão e fusão nuclear"

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
    dict(id="s01", block="gancho", text="{a}O carbono do seu corpo foi feito dentro de uma estrela, [p=0.1] bilhões de anos atrás. [p=0.3] {b}E a luz de parte das casas do Rio de Janeiro vem de átomos de urânio se partindo, em Angra dos Reis. [p=0.3] {c}Núcleos que se juntam, núcleos que se partem."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai separar {b}fissão de fusão, [p=0.2] explicar {c}a usina nuclear e o lixo dela, [p=0.1] e {d}como as estrelas fazem elementos novos. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de uma coisa: [p=0.2] {a}na equação nuclear, a soma das massas em cima {b}e a dos prótons embaixo [p=0.1] {c}são iguais dos dois lados. [p=0.2] Se faltar, procure no canal."),
    # fissão
    dict(id="s04", block="fissao", text="{a}Fissão quer dizer partir, como numa fissura. [p=0.2] {b}Um nêutron, sem carga, chega devagar e entra num núcleo de urânio duzentos e trinta e cinco. [p=0.3] {c}O núcleo fica instável {d}e se parte em dois núcleos médios, [p=0.1] {e}soltando dois ou três nêutrons novos e muita energia."),
    dict(id="s05", block="fissao", text="{a}Confira a equação. [p=0.2] {b}Urânio duzentos e trinta e cinco mais um nêutron: duzentos e trinta e seis em cima. [p=0.3] {c}Dá bário cento e quarenta e um, criptônio noventa e dois e três nêutrons. [p=0.2] {d}Cento e quarenta e um, mais noventa e dois, mais três: [p=0.1] {e}duzentos e trinta e seis. [p=0.2] Fechou."),
    dict(id="s06", block="fissao", text="{a}De onde vem a energia? [p=0.2] {b}Os números de cima só contam prótons e nêutrons, e essa conta fecha. [p=0.2] Mas, numa balança de precisão, os pedaços pesam um pouquinho menos que o começo. [p=0.3] {c}Essa massa que some vira energia. [p=0.2] {d}A conta disso é assunto de outra aula, na Física."),
    # cadeia
    dict(id="s07", block="cadeia", text="{a}Os nêutrons novos batem em outros núcleos de urânio, [p=0.1] {b}que se partem e soltam mais nêutrons. [p=0.3] {c}É a reação em cadeia. [p=0.3] {d}Solta, ela cresce em frações de segundo: [p=0.1] {e}é a bomba atômica."),
    # usina
    dict(id="s08", block="usina", text="{a}Na usina, a cadeia é controlada. [p=0.2] {b}Barras de controle, de boro ou de cádmio, engolem parte dos nêutrons, [p=0.1] {c}e cada fissão provoca, em média, só mais uma. [p=0.3] {d}O calor ferve água, [p=0.1] {e}o vapor gira uma turbina, [p=0.1] {f}e a turbina gira o gerador de eletricidade."),
    dict(id="s09", block="usina", text="{a}A vantagem: a usina não solta gás carbônico enquanto gera energia. [p=0.3] {b}O problema é o lixo. [p=0.2] {c}O combustível usado continua radioativo por milhares de anos. [p=0.2] {d}Ele fica guardado em piscinas e depósitos blindados, longe das pessoas."),
    dict(id="s10", block="usina", text="{a}E há o risco de acidente, como em Chernobyl, em mil novecentos e oitenta e seis, [p=0.1] e em Fukushima, em dois mil e onze. [p=0.3] {b}No Brasil, o maior acidente radioativo não foi numa usina: [p=0.1] {c}foi em Goiânia, em mil novecentos e oitenta e sete, [p=0.1] com uma cápsula de césio de um aparelho médico abandonado."),
    # fusão
    dict(id="s11", block="fusao", text="{a}Fusão é o contrário: juntar. [p=0.2] {b}Dois núcleos leves se chocam com tanta força que viram um só. [p=0.3] {c}Dois isótopos do hidrogênio, um com massa dois e outro com massa três, [p=0.1] {d}formam hélio quatro {e}e soltam um nêutron. [p=0.3] {f}Dois mais três dá cinco, e quatro mais um também."),
    dict(id="s12", block="fusao", text="{a}Mas os núcleos são positivos, e cargas iguais se empurram. [p=0.2] {b}Para vencer esse empurrão, precisam de milhões de graus. [p=0.3] {c}É o que acontece no centro do Sol, a uns quinze milhões de graus: [p=0.1] {d}hidrogênio vira hélio o tempo todo, e daí vem a luz."),
    # estrelas
    dict(id="s13", block="estrelas", text="{a}Nas estrelas maiores, a fusão continua. [p=0.2] {b}Hélio vira carbono: [p=0.1] foi assim que nasceu o carbono do seu corpo, dentro de estrelas antigas. [p=0.2] {c}carbono vira oxigênio, [p=0.1] e assim por diante, {d}até o ferro. [p=0.3] {e}Os elementos mais pesados que o ferro, como o ouro, [p=0.1] {f}nascem quando estrelas explodem ou se chocam."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que as usinas nucleares funcionam por fusão. [p=0.3] {b}Todas as usinas em funcionamento hoje usam fissão, quase sempre de urânio. [p=0.2] {c}A fusão controlada, para gerar energia, ainda está em teste."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}olhe os núcleos que entram. [p=0.2] {b}Um pesado, partindo em médios? [p=0.1] Fissão. [p=0.2] {c}Leves, virando um maior? [p=0.1] Fusão. [p=0.3] {d}E para achar quantos nêutrons saem, [p=0.1] {e}feche a soma das massas: [p=0.1] o que falta são os nêutrons, de massa um."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o nêutron tem massa um e número atômico zero: [p=0.1] {b}ele só aparece na soma de cima. [p=0.3] {c}Não compensa quando falta um núcleo com prótons: [p=0.1] {d}aí, feche também a soma de baixo."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Urânio duzentos e trinta e cinco, com número atômico noventa e dois, recebe um nêutron. [p=0.2] {b}Sai xenônio cento e quarenta, com número atômico cinquenta e quatro. [p=0.2] {c}Sai também estrôncio noventa e quatro, com número atômico trinta e oito. [p=0.2] {d}E saem alguns nêutrons. [p=0.3] {e}Quantos nêutrons? [p=0.2] E {f}é fissão ou fusão?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Em cima, duzentos e trinta e cinco mais um dá duzentos e trinta e seis. [p=0.2] {b}Do outro lado, cento e quarenta mais noventa e quatro dá duzentos e trinta e quatro. [p=0.3] {c}Faltam dois: dois nêutrons. [p=0.3] {d}Embaixo, cinquenta e quatro mais trinta e oito dá noventa e dois: confere. [p=0.3] {e}Um núcleo pesado se partiu: fissão."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}fissão parte um núcleo pesado e move as usinas; [p=0.1] {b}fusão junta núcleos leves e acende as estrelas; [p=0.1] {c}e as somas de cima e de baixo sempre fecham."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai resolver {a}questões de prova de eletrólise e de radioatividade, [p=0.2] {b}com Faraday, decaimento e meia-vida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
