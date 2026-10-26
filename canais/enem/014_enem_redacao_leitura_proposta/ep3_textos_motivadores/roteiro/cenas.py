# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 3 de 6: Textos motivadores — como usar sem copiar (aula para iniciantes)
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seções 06 e 07 + Questões 3 e 4 da seção 12.
#   Repertório sociocultural e "Situações que zeram" só são citados (terão séries próprias).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   GPS: os textos motivadores mostram onde fica o endereço, mas quem faz a entrega é você (liga com o endereço da série).
#   LINHA FANTASMA: linha copiada está no papel, mas não existe para o corretor.
# Trechos didáticos do material lidos EXATAMENTE como estão: Cartilha (cena 06), 2025 (07), passos (08–10),
#   C3 nível 120 (12), regra da cópia (15–17), centros culturais (18–20), insuficiente (21), como retomar (22), Q3 e Q4.
# A frase do exercício (cenas 26–27) é INÉDITA, marcada na tela "elaborada para fins didáticos".
# "Nível 120" e "nível 80": a única explicação dada é que cada competência tem níveis de nota (até 200, ep. 1).
# Frases-chave (meio e fim, idênticas):
#   1. O motivador é GPS: ajuda a chegar, não faz a entrega.
#   2. Linha copiada, mesmo em parte, é linha fantasma.
#   3. Parafraseie e acrescente algo seu.
# Cores: azul = definição · verde = dica/método · amarelo = armadilha · vermelho = erro/penalidade · roxo = regra oficial.

TITULO = "Linha Copiada Vira Linha Fantasma: Textos Motivadores | Proposta de Redação Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Quando pensar em voz alta no rascunho, soe como quem está raciocinando de verdade. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Copiar uma frase do texto de apoio parece *inofensivo.* [p=0.5] {b}Mas essa linha simplesmente *some da "
        "contagem,* [p=0.4] {c}e uma redação curta pode até virar *texto insuficiente,* [p=0.2] com *nota zero.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai ler os textos motivadores *como um corretor* [p=0.4] {b}e usar as ideias "
        "deles *sem copiar uma linha.*"),
    dict(id="03", block="prereq", text=
        "{t}Lembrando, em trinta segundos. [p=0.3] {a}O *tema* é o endereço completo, [p=0.2] o recorte que a prova dá. "
        "[p=0.4] {b}E ele vem na *frase temática,* [p=0.2] que a gente desmonta em blocos: [p=0.2] cada bloco, uma exigência."),

    # ================= BLOCO A: PARA QUE SERVEM =================
    dict(id="04", block="gps", text=
        "{t}Agora, uma pergunta: [p=0.2] o que o *GPS* faz por você? [p=0.4] {a}Ele mostra o caminho [p=0.2] {b}e avisa onde virar. [p=0.4] "
        "{c}Mas *não dirige* por você. [p=0.4] {d}Quem chega lá [p=0.2] e faz a entrega "
        "[p=0.2] é *você.*"),
    dict(id="05", block="gps", text=
        "{t}Na redação, [p=0.2] o GPS tem nome: [p=0.2] *textos motivadores.* [p=0.4] {a}São os textos que a prova traz "
        "*junto com o tema.* [p=0.4] {b}Mostram onde fica o endereço. [p=0.3] {c}A entrega é sua."),
    dict(id="06", block="cartilha", text=
        "{t}E o que a Cartilha diz deles? [p=0.4] {a}Que são textos, [p=0.2] em geral *verbais e não verbais,* [p=0.3] "
        "{b}ou seja, [p=0.2] feitos de palavras, [p=0.2] ou de imagens e números, [p=0.4] {c}que remetem ao tema [p=0.2] "
        "*a fim de orientar sua reflexão.*"),
    dict(id="07", block="cartilha", text=
        "{t}Veja a variedade. [p=0.3] {a}Na proposta de dois mil e vinte e cinco havia: [p=0.3] {b}dados do Censo dois mil "
        "e vinte e dois, [p=0.2] divulgados pelo IBGE; [p=0.3] {c}pictogramas, [p=0.2] aqueles desenhos simples, [p=0.2] "
        "usados para representar pessoas idosas; [p=0.3] {d}um artigo de opinião; [p=0.3] {e}um *infográfico,* [p=0.2] "
        "que é uma imagem que junta dados e desenhos; [p=0.3] {f}um trecho de conto; [p=0.3] {g}e a resenha de um documentário. "
        "[p=0.4] {h}Gêneros diferentes [p=0.2] iluminando *o mesmo tema.* [p=0.3] Esse conjunto se chama *coletânea.*"),

    # ================= BLOCO B: OS TRÊS PASSOS =================
    dict(id="08", block="passos", text=
        "{t}E como ler esses textos *como um corretor?* [p=0.4] A Cartilha dá três passos. [p=0.4] {a}Primeiro: [p=0.2] "
        "observar as palavras que mostram a posição dos autores [p=0.2] e a *situação-problema* central, [p=0.3] o problema "
        "real em discussão. [p=0.4] {b}Na prática: [p=0.2] *sublinhe,* em cada texto, [p=0.2] a frase que resume o problema."),
    dict(id="09", block="passos", text=
        "{a}Segundo: [p=0.2] identificar o ponto de vista [p=0.2] e os argumentos de cada autor, [p=0.2] se houver. [p=0.4] "
        "{b}Na prática: [p=0.2] *anote na margem,* em poucas palavras, [p=0.2] o que cada texto defende ou mostra."),
    dict(id="10", block="passos", text=
        "{a}Terceiro: [p=0.2] refletir, [p=0.2] definir com clareza a *sua* posição, [p=0.2] e juntar outras informações "
        "do seu conhecimento de mundo. [p=0.4] {b}Na prática: [p=0.2] *liste o que você sabe que os textos não dizem:* "
        "[p=0.3] {c}leis, [p=0.2] fatos, [p=0.2] obras, [p=0.2] conceitos."),

    # ================= BLOCO C: PONTO DE PARTIDA =================
    dict(id="11", block="partida", text=
        "{t}Então posso usar as ideias dos motivadores? [p=0.4] {a}Pode! [p=0.3] A Cartilha permite que você *se aproprie* "
        "delas. [p=0.4] {b}Mas pede que você *não fique preso* a elas: [p=0.3] {c}a redação precisa trazer informações "
        "*de fora da prova.* [p=0.4] {d}Isso é o *repertório:* [p=0.2] o que você sabe e leva para o texto. [p=0.2] "
        "Ele vai ganhar uma série própria."),
    dict(id="12", block="partida", text=
        "{t}E se a redação só repete a coletânea? [p=0.4] {a}Cada competência dá uma nota em *níveis,* [p=0.2] até duzentos. "
        "[p=0.4] {b}Na competência três, [p=0.2] o nível cento e vinte fala em informações [p=0.2] *limitadas aos "
        "argumentos dos textos motivadores.* [p=0.4] {c}Quem só repete a coletânea, [p=0.2] ainda que com outras palavras, "
        "[p=0.3] tende a ficar nos *níveis médios.*"),

    # ================= BLOCO D: NÃO VERBAL =================
    dict(id="13", block="naoverbal", text=
        "{t}E o gráfico, [p=0.2] a charge, [p=0.2] a imagem? [p=0.3] Também são texto? [p=0.4] {a}São! [p=0.3] Eles trazem "
        "o problema *condensado.* [p=0.4] {b}Pergunte: [p=0.2] o que o dado mostra? [p=0.3] Qual é a comparação? [p=0.3] "
        "Que crítica a imagem faz? [p=0.4] {c}E um dado de gráfico [p=0.2] *não* deve ser simplesmente transcrito. [p=0.3] "
        "{d}*Interprete.*"),

    # ================= BLOCO E: A REGRA DA CÓPIA =================
    dict(id="14", block="copia", text=
        "{t}Agora, lembra daquele trabalho da escola [p=0.2] *copiado da internet?* [p=0.4] {a}O professor percebia na hora. "
        "[p=0.4] {b}Na redação do ENEM, [p=0.2] *cópia* é escrever trechos iguais aos da prova [p=0.2] como se fossem seus. "
        ""),
    dict(id="15", block="copia", text=
        "{t}O que diz o *edital,* [p=0.2] o documento oficial com as regras do ENEM? [p=0.4] {a}Os trechos copiados da prova "
        "[p=0.2] são *desconsiderados* na contagem das linhas. [p=0.4] {b}Contam só as linhas produzidas pelo participante."),
    dict(id="16", block="copia", text=
        "{t}E repare neste detalhe. [p=0.3] {a}Linha com cópia é a linha composta, [p=0.2] *integral ou parcialmente,* "
        "[p=0.2] por trechos copiados. [p=0.4] {b}Copiou meia linha? [p=0.3] A linha inteira some. [p=0.4] {c}Ela vira uma "
        "*linha fantasma:* [p=0.3] está no papel, [p=0.2] mas *não existe* para o corretor."),
    dict(id="17", block="copia", text=
        "{t}E não para por aí. [p=0.3] {a}A cópia repetida é avaliada *negativamente:* [p=0.3] pode baixar a nota, [p=0.2] "
        "ou até anular o texto como cópia. [p=0.4] {b}Na competência dois, [p=0.2] o nível *oitenta* fala em desenvolver "
        "o tema [p=0.2] *recorrendo à cópia de trechos dos textos motivadores.*"),

    # ================= BLOCO F: CÓPIA × USO AUTÔNOMO =================
    dict(id="18", block="lado", text=
        "{t}Então como usar uma informação sem copiar? [p=0.4] {a}Imagine um texto motivador que diga: [p=0.3] "
        "{b}Em muitas cidades brasileiras, [p=0.2] centros culturais fecharam as portas [p=0.2] por falta de público e de verba."),
    dict(id="19", block="lado", text=
        "{t}Primeiro, [p=0.2] a *cópia:* [p=0.3] {a}Em muitas cidades brasileiras, [p=0.2] centros culturais fecharam as "
        "portas [p=0.2] por falta de público e de verba. [p=0.2] Isso é um problema muito grave para o país. [p=0.5] "
        "{b}A linha copiada *não conta.* [p=0.3] {c}E nada é acrescentado."),
    dict(id="20", block="lado", text=
        "{t}Agora, o *uso autônomo:* [p=0.3] {a}O fechamento de espaços culturais por escassez de recursos, [p=0.2] apontado "
        "na própria discussão sobre o tema, [p=0.3] {b}não é causa isolada: [p=0.2] ele resulta de políticas que concentram "
        "investimentos nas capitais [p=0.2] e deixam o interior sem programação regular. [p=0.5] {c}A ideia foi retomada por "
        "*paráfrase:* [p=0.2] dizer a mesma ideia com outras palavras. [p=0.4] {d}E virou ponto de partida [p=0.2] para uma "
        "*causa* que o texto vai defender."),

    # ================= BLOCO G: TEXTO INSUFICIENTE =================
    dict(id="21", block="insuficiente", text=
        "{t}E agora, a consequência mais grave. [p=0.4] {a}Como as linhas copiadas não contam, [p=0.2] um texto curto e "
        "apoiado em cópia [p=0.3] {b}pode ficar com *sete linhas próprias ou menos.* [p=0.4] {c}E texto com até sete linhas "
        "[p=0.2] é classificado como *insuficiente,* [p=0.2] com *nota zero.* [p=0.4] {d}O assunto "
        "*Situações que zeram* aprofunda isso."),

    # ================= BLOCO H: COMO RETOMAR (EU FAÇO) =================
    dict(id="22", block="retomar", text=
        "{t}E como retomar sem copiar? [p=0.3] Vou fazer no rascunho, [p=0.2] com a frase dos centros culturais. [p=0.4] "
        "{a}Passo um: [p=0.2] *troque a estrutura* da frase, [p=0.2] e não só uma ou outra palavra. [p=0.3] {a2}Em vez de "
        "começar pelas cidades, [p=0.2] eu começo pelo fechamento: [p=0.2] o fechamento de espaços culturais [p=0.2] por "
        "escassez de recursos."),
    dict(id="23", block="retomar", text=
        "{b}Passo dois: [p=0.2] *resuma* em vez de reproduzir. [p=0.3] {b2}Uma frase curta basta: [p=0.2] apontado na própria "
        "discussão sobre o tema. [p=0.5] {c}Passo três, [p=0.2] o mais importante: [p=0.2] logo depois, *acrescente algo seu.* "
        "[p=0.3] Uma causa, [p=0.2] um exemplo, [p=0.2] uma comparação. [p=0.3] {c2}Aqui, [p=0.2] uma causa: [p=0.2] políticas "
        "que concentram investimentos nas capitais. [p=0.4] {d}E se precisar de um dado, [p=0.2] cite de forma breve [p=0.2] "
        "e *interprete.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="24", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Imagine que um texto motivador diga: [p=0.3] {b}Muitos trabalhadores das grandes cidades "
        "brasileiras [p=0.2] passam horas no transporte público todos os dias. [p=0.5] {c}Pause o vídeo [p=0.2] e reescreva "
        "com as suas palavras, [p=0.3] {d}acrescentando *uma causa.* [p=2.0]"),
    dict(id="25", block="exercicio", text=
        "{t}Uma versão possível: [p=0.3] {a}O longo tempo gasto no deslocamento diário, [p=0.2] comum nas metrópoles do país, "
        "[p=0.3] {b}não acontece por acaso: [p=0.2] ele resulta de bairros afastados dos locais de trabalho. [p=0.5] "
        "{c}Estrutura nova, [p=0.2] ideia curta, [p=0.3] {d}e uma causa *sua.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="26", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o motivador é GPS: [p=0.2] ajuda a chegar, [p=0.2] não faz a "
        "entrega. [p=0.5] {b}Dois: [p=0.2] linha copiada, [p=0.2] mesmo em parte, [p=0.2] é linha fantasma. [p=0.5] "
        "{c}Três: [p=0.2] parafraseie e acrescente algo seu."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="27", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] copiar *só um pedacinho,* [p=0.2] achando que a "
        "linha conta. [p=0.4] {b}Parece certo, [p=0.2] porque o resto da linha é seu. [p=0.4] {c}Mas a linha inteira "
        "vira *fantasma.*"),
    dict(id="28", block="erros", text=
        "{a}Segundo: [p=0.2] construir a redação toda com as ideias da coletânea. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "são fontes oficiais da prova. [p=0.4] {c}Mas sem nada de fora, [p=0.2] fica nos *níveis médios.*"),
    dict(id="29", block="erros", text=
        "{a}Terceiro: [p=0.2] transcrever o dado do gráfico [p=0.2] sem interpretá-lo. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "número passa credibilidade. [p=0.4] {c}Mas o corretor quer saber *o que o dado mostra.*"),
    dict(id="30", block="erros", text=
        "{a}Quarto: [p=0.2] *não ler* os motivadores. [p=0.4] {b}Parece certo, [p=0.2] porque a frase temática já diz o "
        "tema. [p=0.4] {c}Mas são eles que mostram a situação-problema."),

    # ================= QUESTÃO 3 =================
    dict(id="31", block="q3", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}Entre as estratégias abaixo, [p=0.2] a que corresponde às "
        "recomendações da Cartilha do Participante [p=0.2] para o uso dos textos motivadores é: [p=0.4] {b}A: [p=0.2] "
        "apropriar-se das ideias dos textos motivadores para entender o problema, [p=0.2] retomá-las por paráfrase quando "
        "necessário [p=0.2] e acrescentar informações de fora da prova. [p=0.5] {c}B: [p=0.2] reproduzir o primeiro parágrafo "
        "de um dos textos motivadores na introdução, [p=0.2] já que ele apresenta o tema com precisão."),
    dict(id="32", block="q3", text=
        "{d}C: [p=0.2] construir toda a argumentação com os dados dos textos motivadores, [p=0.2] pois são fontes legítimas "
        "e dispensam outro repertório. [p=0.5] {e}D: [p=0.2] deixar de ler os textos motivadores, [p=0.2] pois a frase "
        "temática já contém todas as informações necessárias. [p=0.5] {f}E: [p=0.2] copiar trechos dos textos motivadores, "
        "[p=0.2] desde que ocupem, ao todo, menos de sete linhas. [p=0.5] {p}*Pause e tente!* [p=2.0]"),
    dict(id="33", block="q3", text=
        "{t}Vamos conferir. [p=0.3] {xb}A B é cópia: [p=0.2] essas linhas viram fantasmas. [p=0.4] {xc}A C fica presa à "
        "coletânea: [p=0.2] é o nível cento e vinte. [p=0.4] {xd}A D contraria a recomendação de ler com atenção. [p=0.4] "
        "{xe}E a E inventa um limite que *não existe:* [p=0.2] toda linha com cópia deixa de contar. [p=0.5] {ok}*Letra A!*"),

    # ================= QUESTÃO 4 =================
    dict(id="34", block="q4", text=
        "{t}Próxima. [p=0.3] {a}Uma redação tem *vinte* linhas escritas. [p=0.3] {b}Quatro delas contêm, cada uma, [p=0.2] "
        "um trecho copiado de um dos textos motivadores; [p=0.3] {c}o restante de cada uma dessas quatro linhas [p=0.2] foi "
        "escrito pelo participante. [p=0.4] {d}De acordo com o edital e a Cartilha do ENEM de dois mil e vinte e seis:"),
    dict(id="35", block="q4", text=
        "{a}A: [p=0.2] como as quatro linhas são apenas parcialmente copiadas, [p=0.2] todas as vinte linhas entram na contagem "
        "[p=0.2] e a cópia não interfere na avaliação. [p=0.5] {b}B: [p=0.2] a redação recebe nota zero por fuga ao tema, "
        "[p=0.2] já que reproduziu a coletânea. [p=0.5] {c}C: [p=0.2] as quatro linhas contam pela metade, [p=0.2] totalizando "
        "dezoito linhas válidas. [p=0.5] {d}D: [p=0.2] a redação é classificada como texto insuficiente, [p=0.2] pois apresenta "
        "cópia. [p=0.5] {e}E: [p=0.2] as quatro linhas são desconsideradas na contagem, [p=0.2] restando dezesseis linhas "
        "próprias; [p=0.2] o texto não é insuficiente, [p=0.2] mas a cópia é avaliada negativamente. [p=0.5] "
        "{p}*Pause e tente!* [p=2.0]"),
    dict(id="36", block="q4", text=
        "{t}Vamos fazer a conta. [p=0.3] {a}Cópia parcial também vira linha fantasma. [p=0.3] {b}Então: [p=0.2] vinte menos "
        "quatro, [p=0.2] *dezesseis* linhas próprias. [p=0.4] {c}Dezesseis é maior que sete: [p=0.2] *não* é insuficiente. "
        "[p=0.4] {d}Mas a cópia ainda pesa: [p=0.2] é avaliada negativamente."),
    dict(id="37", block="q4", text=
        "{xa}A A esquece que a cópia parcial também tira a linha. [p=0.4] {xb}A B confunde cópia com fuga: [p=0.2] o trecho "
        "copiado é sobre o tema. [p=0.4] {xc}A C inventa a regra da *meia linha.* [p=0.4] {xd}A D aplica o insuficiente sem "
        "fazer a conta. [p=0.5] {ok}*Letra E!*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="38", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o motivador é GPS: [p=0.2] ajuda a chegar, [p=0.2] "
        "não faz a entrega. [p=0.5] {b}Dois: [p=0.2] linha copiada, [p=0.2] mesmo em parte, [p=0.2] é linha fantasma. "
        "[p=0.5] {c}Três: [p=0.2] parafraseie e acrescente algo seu."),

    # ================= PONTE E CTA =================
    dict(id="39", block="ponte", text=
        "{a}E o que acontece quando você *erra o endereço?* [p=0.4] {b}Bairro errado é uma coisa; [p=0.3] {c}cidade errada "
        "[p=0.2] é outra. [p=0.5] {d}Próximo episódio: [p=0.2] *abordagem completa, [p=0.2] tangenciamento e fuga ao tema.*"),
    dict(id="40", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] como ficou a sua versão da frase do transporte? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
