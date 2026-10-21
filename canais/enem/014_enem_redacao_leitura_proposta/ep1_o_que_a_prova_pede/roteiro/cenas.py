# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 1 de 6: O que a prova pede (aula para iniciantes)
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seções 01, 02 e 03 + Questão 1 da seção 12.
#   Competências só citadas (uma frase cada, tiradas das seções 13–17 do material; terão série própria).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE (retomar em todos os episódios): a frase temática é um ENDEREÇO DE ENTREGA COMPLETO.
#   assunto = a CIDADE (envelhecimento) · tema = o endereço exato, rua, número e bairro
#   (Perspectivas acerca do envelhecimento na sociedade brasileira) · tese = o que vai DENTRO DA CAIXA (a sua posição).
# Analogia de apoio (só neste episódio): ENCOMENDA DE BOLO — regras da casa = instruções, fotos de referência = textos
#   motivadores, pedido exato = comando.
# Sequência eu faço → nós fazemos → você faz: 2020 no rascunho (32–33) → 2022 (36–37) → Questão 1, 2017 (42–45).
# Tabela da seção 03: 2016, 2020 e 2025 aparecem na cena 28; as linhas de 2022 e 2017 ficam com "?" e são preenchidas
#   no exercício (2022) e na questão (2017), para não entregar as respostas antes.
# Frases-chave (meio e fim, idênticas):
#   1. Assunto é a cidade; tema é o endereço completo.
#   2. O tema a prova dá; a tese é sua.
#   3. "É um tema importante" não é tese.
# Cores: azul = definição/tema · verde = dica/método · amarelo = armadilha · vermelho = erro/penalidade ·
#   roxo = regra oficial (Cartilha/edital).
# Citações oficiais lidas EXATAMENTE como no material: comando (cena 15), definição de tema (27), Questão 1 (42–43).

TITULO = "O que a prova de redação pede: assunto, tema e tese — Redação ENEM, episódio 1"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas ('Parece certo... mas não é!'); comemore os acertos "
            "com entusiasmo ('Letra B!'); dê ênfase forte às palavras-chave. Quando pensar em voz alta no rascunho, "
            "soe como quem está raciocinando de verdade. Ritmo didático e tranquilo, sem pressa, respeitando as pausas "
            "entre as frases. Leia apenas o texto, sem acrescentar nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}A redação começa *antes da primeira linha.* [p=0.5] {b}Um erro na leitura da proposta [p=0.2] pode prender seu texto "
        "em *quarenta pontos* em três competências, [p=0.4] {c}ou até *zerar* a redação, [p=0.3] {d}mesmo que você escreva "
        "*muito bem.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber *exatamente o que a prova pede* [p=0.3] {b}e separar *assunto,* [p=0.2] "
        "*tema* [p=0.2] e *tese* [p=0.2] de qualquer proposta. [p=0.4] {c}E calma: [p=0.2] cada palavra nova vai ser explicada, "
        "[p=0.2] uma de cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Você não precisa saber nada antes. [p=0.3] {a}Nunca escreveu uma redação? [p=0.2] A gente começa do zero. [p=0.4] "
        "{b}E se você viu a nossa série de Linguagens, [p=0.2] sobre compreensão global, [p=0.2] {c}já tem *meio caminho andado.*"),

    # ================= BLOCO A: O QUE O ENEM PEDE =================
    dict(id="04", block="pede", text=
        "{t}Primeira pergunta: [p=0.2] o que a prova de redação pede? [p=0.4] {a}Muita gente responde: [p=0.2] "
        "*um texto sobre um assunto.* [p=0.3] {b}Tipo: [p=0.2] escreva sobre a velhice. [p=0.4] {c}Parece certo. [p=0.3] "
        "{d}Mas *não é isso.*"),
    dict(id="05", block="pede", text=
        "{t}O ENEM pede, primeiro, [p=0.2] um *tipo* certo de texto: [p=0.3] {a}o *texto dissertativo-argumentativo.* [p=0.4] "
        "{b}Traduzindo: [p=0.2] você *defende um ponto de vista com argumentos,* [p=0.3] {c}em prosa, [p=0.2] ou seja, "
        "[p=0.2] em parágrafos, [p=0.2] e não em versos."),
    dict(id="06", block="pede", text=
        "{t}E sobre o quê? [p=0.3] {a}Sobre um *recorte* exato, [p=0.2] que vem escrito numa frase: [p=0.2] a *frase temática,* "
        "[p=0.2] a frase que diz exatamente sobre o que escrever. [p=0.4] {b}Em dois mil e vinte e cinco, [p=0.2] foi esta: "
        "[p=0.3] {c}*Perspectivas acerca do envelhecimento na sociedade brasileira.* [p=0.4] {d}Não é escrever sobre velhice. "
        "[p=0.2] É escrever sobre *esse recorte.*"),

    # ================= BLOCO B: AS TRÊS PARTES DA PROPOSTA =================
    dict(id="07", block="proposta", text=
        "{t}E onde fica essa frase? [p=0.3] {a}Na *proposta de redação:* [p=0.3] a parte da prova que traz tudo o que você "
        "precisa para escrever."),
    dict(id="08", block="proposta", text=
        "{t}Quem explica a proposta [p=0.2] é a *Cartilha do Participante:* [p=0.3] {a}o guia oficial da redação do ENEM."),
    dict(id="09", block="proposta", text=
        "{a}Ela é publicada pelo *Inep,* [p=0.2] o órgão do governo que organiza a prova. [p=0.4] {b}E segundo a Cartilha, "
        "[p=0.2] a proposta tem *três partes.*"),
    dict(id="10", block="bolo", text=
        "{t}Pense numa encomenda de bolo. [p=0.3] {a}A confeitaria tem as *regras da casa:* [p=0.2] prazo, [p=0.2] tamanho "
        "máximo. [p=0.4] {b}O cliente manda *fotos de referência.* [p=0.4] {c}E faz o *pedido exato:* [p=0.2] chocolate, "
        "[p=0.2] dois andares, [p=0.2] para sábado. [p=0.4] {d}Se o confeiteiro olha só as fotos, [p=0.2] *erra o bolo.*"),
    dict(id="11", block="proposta", text=
        "{t}Na proposta é igual. [p=0.3] {a}As *instruções* são as regras da casa: [p=0.2] as regras práticas da prova. [p=0.3] "
        "{b}Limite de linhas, [p=0.2] uso do rascunho, [p=0.2] {c}e o que pode *anular* a redação."),
    dict(id="12", block="proposta", text=
        "{a}Os *textos motivadores* são as fotos de referência: [p=0.3] {b}notícias, [p=0.2] dados, [p=0.2] gráficos, [p=0.2] "
        "imagens, [p=0.3] {c}que mostram a *situação-problema,* [p=0.2] o problema real em discussão. [p=0.4] {d}Servem para "
        "você *entender.* [p=0.2] *Não* para copiar."),
    dict(id="13", block="proposta", text=
        "{a}E o *comando* é o pedido exato: [p=0.2] o trecho que diz *o que você tem que fazer.*"),
    dict(id="14", block="proposta", text=
        "{t}Agora repare no perigo. [p=0.3] {a}Quem lê só a frase temática [p=0.2] *perde as regras.* [p=0.4] {b}Quem lê só os "
        "textos motivadores [p=0.2] corre o risco de *copiar.*"),

    # ================= BLOCO C: O COMANDO, TRECHO POR TRECHO =================
    dict(id="15", block="comando", text=
        "{t}Então vamos abrir o comando, [p=0.2] porque *cada pedaço dele é uma exigência.* [p=0.4] {b}A Cartilha reproduz o "
        "começo: [p=0.3] {q}A partir da leitura dos textos motivadores [p=0.2] e com base nos conhecimentos construídos ao "
        "longo de sua formação, [p=0.2] redija texto dissertativo-argumentativo [p=0.2] em modalidade escrita formal da língua "
        "portuguesa [p=0.2] sobre o tema."),
    dict(id="16", block="comando", text=
        "{t}Cada exigência se liga a uma *competência:* [p=0.3] {a}um dos *cinco critérios* da correção, [p=0.2] {b}cada um "
        "valendo até *duzentos pontos.* [p=0.3] {c}Do C1 ao C5. [p=0.4] {d}Hoje, [p=0.2] só uma frase de cada."),
    dict(id="17", block="comando", text=
        "{t}Vou sublinhar no rascunho. [p=0.3] {a}A partir da leitura dos textos motivadores: [p=0.3] {b}entender a "
        "situação-problema. [p=0.3] {c}Isso conta na *C2,* [p=0.2] que avalia se você compreendeu a proposta."),
    dict(id="18", block="comando", text=
        "{a}Com base nos conhecimentos construídos ao longo de sua formação: [p=0.3] {b}trazer informações *de fora da prova.* "
        "[p=0.3] {c}Isso se chama *repertório sociocultural:* [p=0.2] o que você sabe e leva para o texto. [p=0.4] {d}Conta "
        "na C2 [p=0.2] e na *C3,* [p=0.2] que avalia como você seleciona e organiza os argumentos."),
    dict(id="19", block="comando", text=
        "{a}Texto dissertativo-argumentativo: [p=0.3] {b}defender um ponto de vista. [p=0.3] {c}C2 de novo."),
    dict(id="20", block="comando", text=
        "{a}Modalidade escrita formal: [p=0.3] {b}usar a *norma-padrão,* [p=0.2] o português que segue as regras da gramática, "
        "[p=0.3] {c}sem marcas de fala, [p=0.2] tipo, [p=0.2] né. [p=0.4] {d}Isso é a *C1:* [p=0.2] o domínio da escrita formal."),
    dict(id="21", block="comando", text=
        "{a}Sobre o tema: [p=0.3] {b}discutir o recorte *por inteiro.* [p=0.3] {c}C2, [p=0.2] com reflexo na C3 [p=0.2] e na C5."),
    dict(id="22", block="comando", text=
        "{t}E o comando pede mais uma coisa: [p=0.3] {a}uma *proposta de intervenção,* [p=0.2] uma ação concreta para o "
        "problema discutido, [p=0.3] {b}que respeite os *direitos humanos.* [p=0.4] {c}Essa é a *C5.*"),
    dict(id="23", block="comando", text=
        "{a}E a C4? [p=0.3] {b}Ela avalia a *coesão:* [p=0.2] as palavras que costuram uma ideia na outra."),

    # ================= BLOCO D: ASSUNTO × TEMA (O ENDEREÇO) =================
    dict(id="24", block="endereco", text=
        "{t}Agora, a dúvida que mais confunde: [p=0.3] assunto e tema não são a mesma coisa? [p=0.4] {a}Pense numa encomenda. "
        "[p=0.3] {b}Na etiqueta está escrito só: [p=0.2] *São Paulo.* [p=0.4] {c}Chega? [p=0.3] {d}*Não chega.* [p=0.2] "
        "Falta a rua, [p=0.2] o número, [p=0.2] o bairro."),
    dict(id="25", block="endereco", text=
        "{t}Guarde esta imagem, [p=0.2] ela vai voltar na série inteira: [p=0.3] {a}a frase temática é um *endereço de entrega "
        "completo.* [p=0.4] {b}O *assunto* é a *cidade,* [p=0.2] a área ampla: [p=0.3] {c}*envelhecimento.*"),
    dict(id="26", block="endereco", text=
        "{a}O *tema* é o *endereço exato,* [p=0.2] com rua, [p=0.2] número [p=0.2] e bairro: [p=0.3] {b}*Perspectivas acerca "
        "do envelhecimento na sociedade brasileira.* [p=0.4] {c}Escrever só sobre envelhecimento [p=0.2] é deixar a encomenda "
        "*parada na cidade.*"),
    dict(id="27", block="endereco", text=
        "{t}E a Cartilha confirma. [p=0.3] {a}Para ela, [p=0.2] o tema se caracteriza por ser *uma delimitação de um assunto "
        "mais abrangente.* [p=0.4] {b}Delimitação quer dizer *recorte.*"),
    dict(id="28", block="tabela", text=
        "{t}Veja em provas de verdade. [p=0.3] {a}Dois mil e dezesseis. [p=0.2] Assunto: [p=0.2] intolerância religiosa. "
        "[p=0.2] Tema: [p=0.2] Caminhos para combater a intolerância religiosa no Brasil. [p=0.5] {b}Dois mil e vinte. [p=0.2] "
        "Assunto: [p=0.2] saúde mental. [p=0.2] Tema: [p=0.2] O estigma associado às doenças mentais na sociedade brasileira. "
        "[p=0.2] {b2}Estigma é um rótulo de preconceito. [p=0.5] {c}E dois mil e vinte e cinco, [p=0.2] que você já conhece. "
        "[p=0.4] {d}Repare: [p=0.2] o assunto cabe em *duas ou três palavras.* [p=0.2] O tema é a *frase inteira.* [p=0.4] "
        "{e}E as linhas vazias? [p=0.2] Quem vai preencher é *você.*"),

    # ================= BLOCO E: AVISO DE NOMENCLATURA =================
    dict(id="29", block="nomes", text=
        "{t}Um aviso sobre nomes. [p=0.3] {a}Na série de Linguagens, [p=0.2] chamamos o campo amplo de "
        "*tema.* [p=0.4] {b}Na Redação, [p=0.2] seguimos a Cartilha do Inep: [p=0.2] o amplo é o *assunto,* [p=0.2] e o "
        "recorte é o *tema.* [p=0.4] {c}O que importa é a mesma coisa: [p=0.2] não confundir *sobre o que se fala* [p=0.2] "
        "com o *recorte exato.*"),

    # ================= BLOCO F: TEMA × TESE (EU FAÇO) =================
    dict(id="30", block="tese", text=
        "{t}E se o endereço a prova te dá, [p=0.2] o que é *seu* na redação? [p=0.4] {a}O que vai *dentro da caixa.* [p=0.4] "
        "{b}Todo mundo recebe *o mesmo endereço.* [p=0.3] {c}Mas cada um decide *o que entregar.* [p=0.4] {d}Isso é a *tese:* "
        "[p=0.2] a *sua posição* sobre o tema."),
    dict(id="31", block="tese", text=
        "{t}O tema é dado pela prova [p=0.2] e é *igual para todos.* [p=0.3] {a}A tese é *sua.* [p=0.4] {b}E o teste é simples: "
        "[p=0.2] a tese é uma frase completa [p=0.2] que *alguém poderia contestar,* [p=0.2] ou seja, [p=0.2] discordar."),
    dict(id="32", block="eufaco", text=
        "{t}Vou fazer na sua frente, [p=0.2] no rascunho, [p=0.2] com o tema de dois mil e vinte. [p=0.3] São três perguntas. "
        "[p=0.4] {a}Primeira: [p=0.2] *de que área a prova fala?* [p=0.4] {a2}Saúde mental. [p=0.2] Esse é o assunto: [p=0.2] "
        "a cidade. [p=0.5] {b}Segunda: [p=0.2] *que recorte dessa área ela pede?* [p=0.4] {b2}O estigma associado às doenças "
        "mentais [p=0.2] na sociedade brasileira. [p=0.2] Esse é o tema: [p=0.2] o endereço completo."),
    dict(id="33", block="eufaco", text=
        "{c}Terceira: [p=0.2] *o que eu defendo sobre esse recorte?* [p=0.4] {c1}Deixa eu pensar. [p=0.5] {c2}Que o estigma "
        "*afasta as pessoas do tratamento* [p=0.3] {c3}e precisa ser combatido *na escola e na mídia.* [p=0.4] {d}Alguém "
        "poderia discordar? [p=0.2] Poderia. [p=0.3] {e}Então é tese: [p=0.2] *o que vai dentro da caixa.*"),

    # ================= BLOCO G: REPETIR O TEMA NÃO É TESE =================
    dict(id="34", block="repetir", text=
        "{t}Agora, uma armadilha que pega muita gente. [p=0.3] {a}Olha esta frase: [p=0.3] {b}*O estigma associado às doenças "
        "mentais é um tema muito importante.* [p=0.4] {c}Parece tese, [p=0.2] não parece? [p=0.3] Tem todas as palavras do "
        "tema, [p=0.2] e soa séria."),
    dict(id="35", block="repetir", text=
        "{t}Mas faça o teste. [p=0.3] {a}Alguém discorda? [p=0.3] Ninguém. [p=0.4] {b}Ela só *reescreve a frase temática.* "
        "[p=0.2] Não toma posição. [p=0.4] {c}É uma caixa *vazia,* [p=0.2] com o endereço colado na tampa. [p=0.4] "
        "{d}Compare com a tese: [p=0.2] o estigma afasta as pessoas do tratamento. [p=0.3] Essa *toma partido.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="36", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Tema de dois mil e vinte e dois: [p=0.3] {b}*Desafios para a valorização de comunidades e "
        "povos tradicionais no Brasil.* [p=0.4] {c}Pause o vídeo [p=0.2] e escreva: [p=0.2] qual é o *assunto,* [p=0.2] "
        "a cidade? [p=0.3] {d}E qual é o *tema,* [p=0.2] o endereço completo? [p=2.0]"),
    dict(id="37", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Assunto: [p=0.2] *povos e comunidades tradicionais.* [p=0.2] A cidade. [p=0.4] "
        "{b}Tema: [p=0.2] a frase inteira. [p=0.3] {c}Repare: [p=0.2] *desafios,* [p=0.2] *valorização* [p=0.2] e "
        "*no Brasil* [p=0.2] fazem parte do endereço."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="38", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] assunto é a cidade; [p=0.2] tema é o endereço completo. "
        "[p=0.5] {b}Dois: [p=0.2] o tema a prova dá; [p=0.2] a tese é sua. [p=0.5] {c}Três: [p=0.2] *é um tema importante* "
        "[p=0.2] não é tese."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="39", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que a redação é *sobre um assunto* qualquer. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque na escola era assim: [p=0.2] escreva sobre as suas férias. [p=0.4] {c}Mas o "
        "ENEM pede um *recorte exato:* [p=0.2] o endereço completo."),
    dict(id="40", block="erros", text=
        "{a}Segundo: [p=0.2] *inverter* assunto e tema. [p=0.4] {b}Parece certo, [p=0.2] porque no dia a dia as duas palavras "
        "viram sinônimos. [p=0.4] {c}Mas o assunto é a cidade, [p=0.2] curtinho. [p=0.2] O tema é o endereço: [p=0.2] "
        "a frase inteira."),
    dict(id="41", block="erros", text=
        "{a}Terceiro: [p=0.2] *repetir a frase temática* achando que é tese. [p=0.4] {b}Parece certo, [p=0.2] porque tem "
        "todas as palavras da prova. [p=0.4] {c}Mas pergunte: [p=0.2] alguém poderia discordar? [p=0.2] Se não, [p=0.2] "
        "a caixa está vazia."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="42", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}O tema da redação do ENEM de dois mil e dezessete foi: [p=0.3] "
        "{b}Desafios para a formação educacional de surdos no Brasil. [p=0.4] {c}A alternativa que identifica corretamente "
        "o assunto amplo e o tema dessa proposta, [p=0.2] nessa ordem, [p=0.2] é:"),
    dict(id="43", block="questao", text=
        "{a}A: [p=0.2] assunto: [p=0.2] desafios para a formação educacional de surdos no Brasil; [p=0.2] tema: [p=0.2] "
        "educação. [p=0.5] {b}B: [p=0.2] assunto: [p=0.2] educação de pessoas surdas; [p=0.2] tema: [p=0.2] os desafios para "
        "a formação educacional de surdos no Brasil. [p=0.5] {c}C: [p=0.2] assunto e tema coincidem: [p=0.2] ambos "
        "correspondem à palavra surdos. [p=0.5] {d}D: [p=0.2] assunto: [p=0.2] a Língua Brasileira de Sinais; [p=0.2] tema: "
        "[p=0.2] a surdez como condição biológica. [p=0.5] {e}E: [p=0.2] assunto: [p=0.2] educação de pessoas surdas; "
        "[p=0.2] tema: [p=0.2] a educação de surdos nos diferentes países do mundo. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="44", block="questao", text=
        "{t}Vamos usar o endereço. [p=0.3] {a}A cidade, [p=0.2] o assunto: [p=0.2] *educação de "
        "pessoas surdas.* [p=0.4] {b}O endereço completo, [p=0.2] o tema: [p=0.2] a frase inteira, [p=0.2] com desafios, "
        "[p=0.2] formação educacional [p=0.2] e no Brasil."),
    dict(id="45", block="questao", text=
        "{ea}A A *inverte:* [p=0.2] chama o endereço de cidade, [p=0.2] e a cidade de endereço. [p=0.4] {ec}A C *apaga a "
        "diferença:* [p=0.2] reduz tudo a uma palavra só. [p=0.4] {ed}A D *troca o endereço:* [p=0.2] a surdez como condição "
        "biológica não é o tema. [p=0.4] {ee}A E quase engana, [p=0.2] mas *tira o bairro:* [p=0.2] fala dos países do mundo, "
        "[p=0.2] e o tema diz *no Brasil.* [p=0.4] {ok}Sobra a *letra B!*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="46", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] assunto é a cidade; [p=0.2] tema é o endereço completo. "
        "[p=0.5] {b}Dois: [p=0.2] o tema a prova dá; [p=0.2] a tese é sua. [p=0.5] {c}Três: [p=0.2] *é um tema importante* "
        "[p=0.2] não é tese."),

    # ================= PONTE E CTA =================
    dict(id="47", block="ponte", text=
        "{a}Uma última ideia: [p=0.2] um endereço tem várias partes, [p=0.3] {b}e se faltar uma, [p=0.2] *a entrega dá "
        "errado.* [p=0.5] {c}Próximo episódio: [p=0.2] *como desmontar a frase temática, [p=0.2] bloco a bloco.*"),
    dict(id="48", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] no tema de dois mil e vinte e dois, [p=0.2] você "
        "acertou? [p=0.5] {bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
