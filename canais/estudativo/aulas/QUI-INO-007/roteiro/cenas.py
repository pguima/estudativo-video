# Estudativo · QUI-INO-007 — Ler uma equação: conservação das massas (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: reconhecer sinais de reação, ler reagentes, produtos e estados em uma equação e dizer pela lei de Lavoisier que
# 12 g de carbono com 32 g de oxigênio dão 44 g de gás carbônico.
# Pré-requisitos: QUI-MIS-001. Próxima: QUI-INO-001 (ácidos: o H⁺ na água, nomes e força).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula da trilha: linguagem visual da trilha no visual.py.
# Fatos: Antoine Lavoisier, químico francês do século XVIII (1743–1794), pesou reagentes e produtos em recipientes fechados.
# A cera da vela queima e vira gás carbônico e vapor de água. Palha de aço (ferro) queimada ao ar fica mais pesada: ganha o
# oxigênio do ar. C + O₂ → CO₂: 12 g + 32 g = 44 g. Questão inédita: Fe + S → FeS, 56 g + 32 g = 88 g (massas molares reais).
# Só se usa soma: a subtração do atalho é dita como "quanto falta para chegar".

TITULO = "Ler uma equação: conservação das massas"

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
    dict(id="s01", block="gancho", text="{a}Uma vela acesa vai encolhendo. [p=0.3] Parece que a matéria dela {b}some. [p=0.3] Mas, numa reação química, {c}nada some. [p=0.3] {d}A cera vira gás, e o gás vai para o ar."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer quando há reação, [p=0.2] {b}ler uma equação química [p=0.2] e {c}prever a massa que se forma, como na queima do carvão. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você só precisa lembrar das fórmulas. [p=0.2] {a}Cê é o símbolo do carbono. [p=0.2] {b}Ó dois é uma molécula com dois átomos de oxigênio. [p=0.2] E {c}cê ó dois, o gás carbônico, tem um carbono e dois oxigênios."),
    # o que é reação
    dict(id="s04", block="reacao", text="O que é uma reação química? [p=0.2] É quando {a}substâncias, como a água ou o gás oxigênio, viram {b}substâncias novas. [p=0.3] Os átomos {c}trocam de parceiros, [p=0.1] mas {d}continuam os mesmos átomos."),
    dict(id="s05", block="reacao", text="Como saber que houve reação? [p=0.2] Procure os sinais. [p=0.2] {a}Sai gás, com bolhas, [p=0.1] como no comprimido efervescente. [p=0.2] {b}Muda a cor, como no ferro que enferruja. [p=0.2] {c}Aparece um sólido no meio do líquido. [p=0.2] {d}Sai luz ou calor, como no fogo."),
    dict(id="s06", block="reacao", text="Cuidado: {a}gelo derretendo não é reação. [p=0.2] {b}A água continua sendo agá dois ó, só mudou de estado. [p=0.3] {c}Sal se dissolvendo na água também não: [p=0.1] {d}deixe a água evaporar, e o mesmo sal volta."),
    # equação
    dict(id="s07", block="equacao", text="A reação se escreve numa {a}equação química. [p=0.2] Veja a queima do carvão, que é carbono. [p=0.2] {b}Cê, mais ó dois, [p=0.1] {c}seta, [p=0.1] {d}cê ó dois."),
    dict(id="s08", block="equacao", text="{a}À esquerda da seta ficam os reagentes, o que existe antes. [p=0.2] {b}À direita, os produtos, o que se forma. [p=0.3] {c}A seta se lê produz, ou forma. [p=0.2] E {d}o sinal de mais separa as substâncias de um mesmo lado."),
    dict(id="s09", block="equacao", text="Muitas vezes a equação mostra {a}o estado de cada substância, entre parênteses. [p=0.2] {b}A letra ésse quer dizer sólido. [p=0.1] {c}Éle, líquido. [p=0.1] {d}Gê, gás. [p=0.2] E {e}á quê, de aquoso, quer dizer dissolvido em água."),
    dict(id="s10", block="equacao", text="Leia a equação completa: [p=0.2] {a}carbono sólido [p=0.1] {b}mais oxigênio gás [p=0.1] {c}produz gás carbônico. [p=0.3] {d}Um reagente sólido, um gasoso, e um produto gasoso."),
    # Lavoisier
    dict(id="s11", block="lavoisier", text="No século dezoito, o químico francês {a}Lavoisier pesou reagentes e produtos {b}em frascos fechados. [p=0.3] {c}A massa antes era igual à massa depois. [p=0.3] É a {d}lei da conservação das massas: [p=0.2] {e}num sistema fechado, a massa dos reagentes é igual à massa dos produtos."),
    dict(id="s12", block="lavoisier", text="Por que funciona? [p=0.2] {a}Conte os átomos. [p=0.2] Antes: {b}um carbono e dois oxigênios. [p=0.2] Depois: {c}um carbono e dois oxigênios, agora presos juntos. [p=0.3] {d}Nenhum átomo some, nenhum aparece. [p=0.2] Então {e}a massa também não muda."),
    dict(id="s13", block="lavoisier", text="Vamos à conta. [p=0.2] {a}Doze gramas de carbono queimam com {b}trinta e dois gramas de oxigênio, num frasco fechado. [p=0.3] {c}Quanto gás carbônico se forma? [p=0.3] {d}Some as massas dos reagentes: [p=0.1] doze mais trinta e dois {e}dá quarenta e quatro gramas."),
    # erro comum
    dict(id="s14", block="erro", text="O erro comum é {a}esquecer o gás. [p=0.2] Queime {b}palha de aço ao ar livre, e ela fica {c}mais pesada. [p=0.3] {d}Parece que a lei falhou."),
    dict(id="s15", block="erro", text="Não falhou. [p=0.2] {a}O ferro da palha se prendeu ao oxigênio do ar, [p=0.1] e esse oxigênio {b}entrou na balança. [p=0.3] Na vela, é o contrário: {c}o gás que se forma vai embora. [p=0.3] {d}A lei vale para o sistema fechado, [p=0.1] em que nada entra e nada sai."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho de prova: [p=0.2] {a}se faltar uma massa, [p=0.1] {b}ela é o pedaço que falta para fechar a conta. [p=0.3] {c}Quarenta e quatro gramas de gás carbônico vieram de doze gramas de carbono. [p=0.2] {d}De doze para quarenta e quatro faltam trinta e dois: [p=0.1] {e}trinta e dois gramas de oxigênio."),
    dict(id="s17", block="atalho", text="Funciona porque {a}os átomos dos dois lados são os mesmos. [p=0.3] {b}Só não compensa num sistema aberto: [p=0.1] aí, {c}procure o gás que entrou ou saiu."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Num frasco fechado, cinquenta e seis gramas de ferro reagem com {b}trinta e dois gramas de enxofre, e não sobra nada. [p=0.3] {c}Forma-se um sólido só, o sulfeto de ferro. [p=0.3] {d}Quais são os reagentes, e qual é o produto? [p=0.2] E {e}qual é a massa do produto?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Os reagentes, à esquerda, são o ferro e o enxofre. [p=0.2] {b}O produto, à direita, é o sulfeto de ferro. [p=0.3] {c}O frasco é fechado, então vale Lavoisier: [p=0.2] cinquenta e seis mais trinta e dois {d}dá oitenta e oito gramas. [p=0.3] {e}A massa do produto é a soma das massas dos reagentes."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}reagentes à esquerda, produtos à direita, [p=0.1] {b}o estado entre parênteses, [p=0.1] e {c}num sistema fechado a massa se conserva, porque os átomos são os mesmos."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai usar equações para conhecer os {a}ácidos: [p=0.2] {b}o que eles soltam na água, como se chamam e quando são fortes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
