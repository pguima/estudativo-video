# Roteiro — Matéria, Substâncias e Misturas, Episódio 2: Alotropia (aula para iniciantes)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seção 08 + Questão 5 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   GERAL: as MESMAS peças de LEGO montadas de jeitos diferentes; muda a montagem, muda tudo (retoma o ep. 1).
#   DIAMANTE = trepa-trepa de parquinho (cada peça presa a outras 4, em todas as direções).
#   GRAFITE = baralho de cartas (folhas empilhadas que escorregam) · GRAFENO = uma carta · NANOTUBO = a carta enrolada.
# Fecho de cada alótropo: "A estrutura decide a propriedade."
# Frases-chave (meio e fim, idênticas):
#   1. Alotropia: um elemento, várias substâncias simples.
#   2. Muda o arranjo ou o número de átomos, muda a substância.
#   3. A estrutura decide a propriedade.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
# Fórmulas escritas como se leem ("O dois", "O três"); na tela aparecem como O₂, O₃.

TITULO = "Grafite e diamante são a MESMA coisa? Alotropia do zero — Química ENEM, episódio 2"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O material mais duro da natureza, [p=0.2] o diamante, [p=0.3] {b}e um dos mais moles que existem, [p=0.2] o grafite do lápis, "
        "[p=0.4] {c}são feitos exatamente do mesmo elemento: [p=0.2] *carbono puro.* [p=0.5] {d}Um corta vidro. [p=0.2] O outro se desmancha no papel. "
        "[p=0.4] {e}Como isso é possível?"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai entender o que é *alotropia* [p=0.3] {b}e reconhecer os alótropos que caem no ENEM. "
        "[p=0.4]"),

    # ================= PRÉ-REQUISITOS (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, uma lembrança do episódio passado. [p=0.3] {a}Átomos são peças de LEGO, [p=0.2] e cada elemento é uma *cor.* [p=0.4] "
        "{b}Substância *simples* é a montagem feita com uma cor só: [p=0.2] um único elemento. [p=0.4] {c}E na fórmula, [p=0.2] "
        "o número pequeno conta as peças. [p=0.3] {d}O dois: [p=0.2] duas peças de oxigênio. [p=0.3] {e}O três: [p=0.2] três peças de oxigênio."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="04", block="def", text=
        "{t}E será que o *mesmo* elemento pode formar substâncias diferentes? [p=0.4] {a}Pense numa caixa de LEGO só com peças cinza. "
        "[p=0.3] {b}Com elas, você monta um prédio. [p=0.3] {c}Desmonta, [p=0.2] e com as mesmas peças monta um carrinho. [p=0.4] "
        "{d}Mesmas peças. [p=0.2] Montagem diferente. [p=0.2] *Muda a montagem, muda tudo.*"),
    dict(id="05", block="def", text=
        "{t}Na química, isso tem nome: [p=0.2] *alotropia.* [p=0.4] {a}Alotropia é quando um mesmo elemento [p=0.2] forma substâncias simples diferentes. "
        "[p=0.5] {b}E cada uma dessas substâncias [p=0.2] se chama *alótropo.* [p=0.4] {c}O prédio e o carrinho de peças cinza: [p=0.2] "
        "dois alótropos."),

    # ================= BLOCO B: OXIGÊNIO =================
    dict(id="06", block="oxigenio", text=
        "{t}Quer um exemplo que está no ar? [p=0.3] {a}O oxigênio que entra no seu pulmão agora [p=0.2] é *O dois:* [p=0.2] duas peças. "
        "[p=0.4] {b}Mas, lá no alto, [p=0.2] a uns vinte ou trinta quilômetros do chão, [p=0.2] existe outra montagem: [p=0.3] "
        "{c}*O três,* [p=0.2] três peças de oxigênio. [p=0.3] {d}Essa substância se chama *ozônio.*"),
    dict(id="07", block="atomicidade", text=
        "{t}O que mudou de um para o outro? [p=0.4] {a}Só o número de peças na montagem. [p=0.4] {b}Esse número tem nome: [p=0.2] "
        "*atomicidade,* [p=0.2] o número de átomos na molécula. [p=0.4] {c}O dois tem atomicidade dois. [p=0.3] O três, [p=0.2] três. "
        "[p=0.4] {d}Mudou a atomicidade, [p=0.2] *mudou a substância.*"),
    dict(id="08", block="ozonio", text=
        "{t}E muda muita coisa? [p=0.4] {a}Lá no alto, [p=0.2] o ozônio forma uma camada que protege a Terra [p=0.2] "
        "dos raios do sol que queimam a pele, [p=0.2] os ultravioleta. [p=0.4] {b}Mas aqui embaixo, [p=0.2] no nível do chão, "
        "[p=0.2] o ozônio é *tóxico:* [p=0.2] irrita os olhos e os pulmões. [p=0.4] {c}O dois você respira. [p=0.2] O três, não. "
        "[p=0.4] {d}*A estrutura decide a propriedade.*"),

    # ================= BLOCO C: CARBONO =================
    dict(id="09", block="carbono", text=
        "{t}Agora, o campeão do ENEM: [p=0.2] o carbono. [p=0.4] {a}Diamante e grafite são só carbono, [p=0.2] mais nada. "
        "[p=0.4] {b}Então a diferença tem que estar na montagem: [p=0.2] no jeito como os átomos se organizam, [p=0.2] o *arranjo.* "
        "[p=0.4] {c}Quando esse arranjo se repete organizado, [p=0.2] como os azulejos de uma parede, [p=0.2] ele se chama *retículo.*"),
    dict(id="10", block="diamante", text=
        "{t}E como é o diamante por dentro? [p=0.4] {a}Pense num *trepa-trepa* de parquinho. [p=0.3] {b}Cada peça presa a outras *quatro,* "
        "[p=0.2] em todas as direções: [p=0.2] para cima, para baixo, para os lados. [p=0.4] {c}Uma rede em três dimensões, [p=0.2] rígida. "
        "[p=0.4] {d}Para riscar um diamante, [p=0.2] você teria que quebrar essa rede. [p=0.3] Por isso ele é o material natural mais duro. "
        "[p=0.4] {e}*A estrutura decide a propriedade.*"),
    dict(id="11", block="grafite", text=
        "{t}E o grafite? [p=0.3] {a}Os mesmos carbonos se soltam do trepa-trepa [p=0.2] e se organizam em *folhas,* [p=0.2] "
        "com desenhos de seis lados, [p=0.2] como favos de mel. [p=0.4] {b}As folhas ficam empilhadas, [p=0.2] como um *baralho de cartas.* "
        "[p=0.4] {c}Dentro de cada folha, [p=0.2] as peças estão bem presas. [p=0.3] {d}Mas uma folha mal segura a outra."),
    dict(id="12", block="lapis", text=
        "{t}Então, o que acontece quando você escreve? [p=0.4] {a}O lápis passa no papel, [p=0.2] e as folhas *escorregam* umas sobre as outras, "
        "[p=0.2] como cartas deslizando do baralho. [p=0.4] {b}Algumas ficam no papel: [p=0.2] é o traço do lápis. [p=0.4] "
        "{c}Por isso o grafite é macio. [p=0.4] {d}*A estrutura decide a propriedade.*"),

    # ================= BLOCO D: NANOTECNOLOGIA =================
    dict(id="13", block="grafeno", text=
        "{t}E se você tirar *uma carta só* do baralho? [p=0.4] {a}Uma única folha de carbono, [p=0.2] com a espessura de um átomo. "
        "[p=0.4] {b}Isso é o *grafeno.* [p=0.4] {c}Ele é tão fino que é quase transparente, [p=0.2] e mesmo assim é muito resistente."),
    dict(id="14", block="nanotubo", text=
        "{t}E se você *enrolar* essa carta, [p=0.2] como um canudo? [p=0.4] {a}Vira um *nanotubo* de carbono: [p=0.2] "
        "uma folha de grafeno enrolada em forma de tubo. [p=0.5] {b}E existe ainda o *fulereno:* [p=0.2] carbonos montados no formato "
        "de uma bola de futebol."),
    dict(id="15", block="nanotec", text=
        "{t}E por que o ENEM gosta tanto disso? [p=0.4] {a}Por causa da *nanotecnologia:* [p=0.2] a tecnologia que trabalha com coisas "
        "do tamanho de átomos. [p=0.4] {b}Grafeno e nanotubos aparecem em questões de materiais novos, [p=0.2] leves e resistentes, "
        "[p=0.3] {c}e de *condutividade,* [p=0.2] que é a capacidade de deixar a eletricidade passar. [p=0.5] {d}Repare: [p=0.2] diamante, grafite, "
        "grafeno, nanotubo, fulereno. [p=0.3] Tudo carbono puro. [p=0.4] {e}*A estrutura decide a propriedade.*"),

    # ================= BLOCO E: FÓSFORO E ENXOFRE =================
    dict(id="16", block="outros", text=
        "{t}E outros elementos também fazem isso? [p=0.4] {b}O fósforo: [p=0.2] "
        "*fósforo branco* [p=0.2] e *fósforo vermelho.* [p=0.4] {c}E o enxofre: [p=0.2] *rômbico* [p=0.2] e *monoclínico,* "
        "[p=0.2] que são duas formas diferentes de cristal. [p=0.4] {d}Não precisa decorar detalhes. [p=0.2] Viu esses nomes, [p=0.2] *é alotropia.*"),

    # ================= BLOCO F: SUBSTÂNCIAS DIFERENTES =================
    dict(id="17", block="diferentes", text=
        "{t}Então, O dois e O três [p=0.2] são a mesma substância, [p=0.2] em versões diferentes? [p=0.5] {a}Não. [p=0.3] "
        "São substâncias *diferentes,* [p=0.2] cada uma com as suas propriedades. [p=0.4] {c}Mesmo elemento, [p=0.2] substâncias diferentes. [p=0.3] "
        "{d}E todas *simples:* [p=0.2] uma cor só."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] alotropia: [p=0.2] um elemento, várias substâncias simples. [p=0.5] "
        "{b}Dois: [p=0.2] muda o arranjo ou o número de átomos, [p=0.2] muda a substância. [p=0.5] {c}Três: [p=0.2] "
        "a estrutura decide a propriedade."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] O dois e O três são a mesma substância. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque os dois são oxigênio, [p=0.2] com a mesma letra O. [p=0.4] {c}Mas a atomicidade é diferente, "
        "[p=0.2] e as propriedades também. [p=0.3] São *substâncias diferentes.*"),
    dict(id="20", block="erro2", text=
        "{a}Segundo: [p=0.2] o diamante é duro porque é mais puro, [p=0.2] e o grafite tem *impurezas.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque, quando duas coisas parecidas se comportam diferente, [p=0.2] a gente pensa em sujeira. "
        "[p=0.4] {c}Mas os dois são carbono puro. [p=0.3] A diferença é o *arranjo:* [p=0.2] trepa-trepa contra baralho."),
    dict(id="21", block="erro3", text=
        "{a}Terceiro: [p=0.2] achar que algum alótropo é substância composta. [p=0.4] {b}Parece certo, [p=0.2] porque são substâncias "
        "diferentes, [p=0.2] e o O três tem três átomos. [p=0.4] {c}Mas use o ritual do episódio passado: [p=0.2] conte as letras. "
        "[p=0.3] O três: [p=0.2] uma letra. [p=0.2] Diamante: [p=0.2] só C. [p=0.3] {d}Todo alótropo é substância *simples.*"),

    # ================= QUESTÃO 5 =================
    dict(id="22", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {e1}O grafite e o diamante são formados *só* por átomos de carbono, "
        "[p=0.2] mas têm propriedades muito diferentes: [p=0.3] {e2}o diamante é o material natural mais duro conhecido, [p=0.2] "
        "e o grafite é macio, [p=0.2] usado no lápis. [p=0.4] {e3}Essa diferença é explicada:"),
    dict(id="23", block="questao", text=
        "{a}A: [p=0.2] pela presença de impurezas diferentes em cada um. [p=0.4] {b}B: [p=0.2] pelo arranjo diferente dos átomos de carbono "
        "no retículo. [p=0.4] {c}C: [p=0.2] pelo fato de o diamante ser substância composta. [p=0.4] {d}D: [p=0.2] pela diferença de "
        "massa atômica entre os carbonos. [p=0.4] {e}E: [p=0.2] por serem misturas de elementos diferentes. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="24", block="questao", text=
        "{t}Vamos eliminar. [p=0.3] {a}A, [p=0.2] impurezas: [p=0.2] o enunciado diz que os dois são *só* carbono. [p=0.2] Não há impureza. "
        "[p=0.4] {c}C: [p=0.2] o diamante só tem carbono. [p=0.2] Uma letra: [p=0.2] *simples,* [p=0.2] não composta. [p=0.4] "
        "{e}E, [p=0.2] misturas de elementos: [p=0.2] só existe um elemento aqui, [p=0.2] e ele é puro."),
    dict(id="25", block="questao", text=
        "{d}D: [p=0.2] massa atômica é o peso de cada átomo. [p=0.3] Mas os carbonos são idênticos nos dois: [p=0.2] *as mesmas peças.* "
        "[p=0.4] {b}Sobra a B: [p=0.2] o arranjo dos átomos no retículo. [p=0.3] Trepa-trepa no diamante, [p=0.2] baralho no grafite. "
        "[p=0.4] {ok}*Letra B.* [p=0.3] {x}A estrutura decide a propriedade."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] alotropia: [p=0.2] um elemento, várias substâncias simples. [p=0.5] "
        "{b}Dois: [p=0.2] muda o arranjo ou o número de átomos, [p=0.2] muda a substância. [p=0.5] {c}Três: [p=0.2] "
        "a estrutura decide a propriedade."),

    # ================= PONTE =================
    dict(id="27", block="ponte", text=
        "{t}Até agora, [p=0.2] só vimos substâncias puras. [p=0.4] {a}Mas quase nada ao seu redor é puro: [p=0.3] {b}nem o ar, "
        "[p=0.3] {c}nem a água mineral, [p=0.3] {d}nem um anel de ouro. [p=0.5] {e}No próximo episódio: [p=0.2] *misturas.*"),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que o diamante e o grafite eram a mesma coisa? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
