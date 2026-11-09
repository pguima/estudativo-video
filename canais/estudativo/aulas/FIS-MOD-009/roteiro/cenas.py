# Estudativo · FIS-MOD-009 — Big Bang e expansão do Universo (Física · Física Moderna · Astronomia e cosmologia).
# Habilidade: usar o desvio para o vermelho e a radiação de fundo como provas do Big Bang e citar as partículas do modelo padrão.
# Pré-requisitos: FIS-MOD-008 (vida das estrelas), FIS-OND-008 (efeito Doppler). Próxima: FIS-MOD-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" desta aula não tem espectro eletromagnético (FIS-OND-010) nem espectros de linhas (FIS-MOD-003): a ordem das
# cores pelo comprimento de onda é dita na hora, e as linhas dos elementos são citadas como assunto de outra aula.
# Fatos: Hubble, 1929 (Lemaître propôs a expansão em 1927); H₀ ≈ 70 km/s por megaparsec ≈ 21 km/s por milhão de anos-luz
# → 100 milhões de anos-luz ≈ 2.100 km/s ("uns dois mil"). Idade do Universo: 13,8 bilhões de anos. Radiação de fundo:
# Penzias e Wilson, 1965; luz solta ~380 mil anos depois do início; hoje em micro-ondas, ~2,7 K = −270 °C.
# Modelo padrão: quarks (up +2/3, down −1/3), léptons (elétron, neutrino), bósons (fóton, glúon, W e Z, Higgs — achado em 2012).

TITULO = "Big Bang e expansão do Universo"

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
    dict(id="s01", block="gancho", text="{a}Uma televisão antiga, fora de sintonia, [p=0.1] mostrava chuvisco na tela. [p=0.3] {b}Um pedacinho daquele chuvisco era luz do começo do Universo, [p=0.2] {c}viajando há quase catorze bilhões de anos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar o desvio para o vermelho [p=0.1] {b}e a radiação de fundo como provas do Big Bang, [p=0.2] e {c}citar as partículas do modelo padrão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}no efeito Doppler, a fonte que se afasta chega com frequência menor; [p=0.2] e {c}as estrelas fabricam elementos pela fusão. [p=0.3] Se faltar alguma, procure no canal."),
    # Doppler da luz
    dict(id="s04", block="doppler", text="{a}O efeito Doppler vale para a luz também. [p=0.2] Primeiro, as cores: [p=0.2] {b}a luz vermelha tem o maior comprimento de onda da luz visível, [p=0.2] {c}e a violeta, o menor. [p=0.3] {d}Uma galáxia que se afasta estica as ondas da luz dela: [p=0.2] {e}o comprimento de onda aumenta, e a luz escorrega para o vermelho."),
    dict(id="s05", block="doppler", text="Isso se chama {a}desvio para o vermelho. [p=0.3] {b}Se a galáxia se aproxima, as ondas se apertam: [p=0.1] {c}desvio para o azul. [p=0.3] Os astrônomos medem esse desvio pelas marcas que cada elemento deixa na luz, [p=0.2] {d}um assunto de outra aula."),
    # Hubble
    dict(id="s06", block="hubble", text="Em mil novecentos e vinte e nove, {a}o americano Edwin Hubble mediu muitas galáxias. [p=0.3] {b}Quase todas tinham desvio para o vermelho: [p=0.1] {c}estão se afastando de nós. [p=0.3] E mais: {d}quanto mais longe, mais depressa. [p=0.2] {e}O dobro da distância, o dobro da velocidade."),
    dict(id="s07", block="hubble", text="{a}Distâncias assim se medem em anos-luz: [p=0.1] {b}a distância que a luz anda num ano. [p=0.3] {c}Uma galáxia a cem milhões de anos-luz se afasta a uns dois mil quilômetros por segundo. [p=0.2] {d}Uma a duzentos milhões, a uns quatro mil."),
    # expansão
    dict(id="s08", block="expansao", text="Mas o que se expande {a}é o próprio espaço. [p=0.2] Pense num {b}balão com pontinhos pintados. [p=0.2] {c}Encha o balão: [p=0.1] {d}de qualquer pontinho, todos os outros se afastam, [p=0.1] {e}e os mais longe se afastam mais depressa. [p=0.3] {f}Nenhum pontinho é o centro."),
    dict(id="s09", block="expansao", text="{a}Agora, rode o filme para trás. [p=0.2] {b}Se tudo se afasta, antes tudo estava mais junto, [p=0.1] {c}mais denso e mais quente. [p=0.3] {d}Há uns treze vírgula oito bilhões de anos, [p=0.1] {e}o Universo inteiro estava num estado quentíssimo e apertado. [p=0.2] {f}É o Big Bang: o começo da expansão."),
    # radiação de fundo
    dict(id="s10", block="fundo", text="{a}Se o começo foi quente, ele deixou luz. [p=0.3] {b}Uns trezentos e oitenta mil anos depois do início, [p=0.1] o Universo esfriou o bastante para a luz andar livre. [p=0.3] {c}Essa luz viaja até hoje, [p=0.1] {d}esticada pela expansão até virar micro-ondas, [p=0.1] ondas bem mais compridas que a luz visível, como as do forno."),
    dict(id="s11", block="fundo", text="{a}Em mil novecentos e sessenta e cinco, dois cientistas, nos Estados Unidos, acharam um chiado que vinha de todas as direções do céu. [p=0.3] {b}Era essa luz: [p=0.1] a radiação cósmica de fundo. [p=0.2] {c}Ela corresponde a uns menos duzentos e setenta graus Celsius. [p=0.3] {d}Desvio para o vermelho e radiação de fundo: [p=0.1] {e}as duas grandes provas do Big Bang."),
    # modelo padrão
    dict(id="s12", block="particulas", text="{a}Logo no começo, se formaram as partículas mais básicas. [p=0.2] A teoria que as organiza se chama {b}modelo padrão. [p=0.3] {c}A matéria é feita de quarks e léptons. [p=0.2] {d}O elétron é um lépton. [p=0.2] {e}Prótons e nêutrons são feitos de três quarks cada."),
    dict(id="s13", block="particulas", text="{a}Dois tipos de quark formam os núcleos comuns: [p=0.1] {b}o up, com mais dois terços da carga do próton, [p=0.1] {c}e o down, com menos um terço. [p=0.3] {d}O próton é up, up, down: [p=0.1] {e}dois terços mais dois terços menos um terço, carga um. [p=0.3] {f}E as forças são levadas por outras partículas, os bósons, [p=0.1] como {g}o fóton, o pacote de luz, que leva a força elétrica e magnética."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}imaginar o Big Bang como uma bomba que explodiu num ponto do espaço. [p=0.3] {b}Não houve um centro, nem um lado de fora. [p=0.2] {c}Foi o espaço inteiro que começou a se esticar, [p=0.1] como a borracha do balão. [p=0.3] {d}Por isso, de qualquer galáxia, as outras parecem se afastar."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}vermelho é vai embora. [p=0.1] {b}Azul é aproxima: [p=0.1] {c}azul e aproxima começam com a mesma letra. [p=0.3] {d}Funciona porque é o Doppler: [p=0.1] {e}afastou, frequência menor, comprimento de onda maior, para o vermelho. [p=0.3] {f}Não serve para a radiação de fundo: [p=0.1] ela é esticada pela expansão inteira, e chega de todos os lados."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma galáxia se afasta de nós a dois mil quilômetros por segundo. [p=0.2] {b}Outra está no triplo da distância. [p=0.3] {c}A que velocidade ela se afasta? [p=0.2] {d}A luz dela chega desviada para o vermelho ou para o azul? [p=0.2] E {e}qual é a carga do nêutron, que é up, down, down?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Velocidade proporcional à distância: [p=0.1] {b}o triplo da distância, o triplo da velocidade. [p=0.2] {c}Seis mil quilômetros por segundo. [p=0.3] {d}Se afasta, então {e}desvio para o vermelho."),
    dict(id="s19", block="resposta", text="{a}E o nêutron: [p=0.1] {b}mais dois terços, menos um terço, menos um terço. [p=0.2] {c}Dois terços menos dois terços: [p=0.1] {d}carga zero. [p=0.2] Por isso ele se chama nêutron."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}as galáxias se afastam, e mais depressa quanto mais longe; [p=0.2] {b}desvio para o vermelho e radiação de fundo são as provas do Big Bang; [p=0.2] e {c}a matéria é feita de quarks e léptons."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}você pratica astronomia e cosmologia em questões: [p=0.2] {b}estrelas, buracos negros e o Universo em expansão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
