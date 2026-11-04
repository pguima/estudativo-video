# Roteiro — Redação ENEM, Desenvolvimento, Episódio 6 de 7: Oficina — planejar o parágrafo em cinco linhas e escrever o
#   segundo desenvolvimento
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seção 10 (rascunho em cinco linhas, eixo 2: mídia, e
#   equilíbrio entre os parágrafos) + Questão 9 da seção 12. Tese de 2021 da Questão 3 para o "você faz".
#   Repertório sociocultural (banco de referências) só citado: série própria.
# Formato OFICINA: o professor faz tudo ao vivo no rascunho, pensando em voz alta; nós fazemos (Q9, abre o parágrafo) →
#   eu faço (as cinco linhas) → você faz (tese de 2021).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora: o rascunho de cinco linhas é a LISTA DE COMPRAS do parágrafo (linha vazia = parágrafo ainda não está
#   pronto) + as cinco etapas da entrega da série (etiqueta, por quê, nota fiscal, produto funcionando, recibo).
# Frases-chave (meio e fim, idênticas):
#   1. Cinco linhas antes do parágrafo.  2. Linha vazia: parágrafo não está pronto.
#   3. Repertório só o que você conhece de fato.
# 1ª TENTATIVA IMPERFEITA (cenas 16–18): o professor pula a linha "Análise" e escreve logo o fecho; o "e daí?" revela o
#   buraco; a linha pisca vazia em vermelho com ✗ e depois recebe a análise da tabela, com ✓.
# FIDELIDADE: as cinco linhas da seção 10, a Questão 9 (enunciado e alternativas) e a tese de 2021 lidas EXATAMENTE como
#   no material. A linha "Repertório" fica EM ABERTO: na tela, "[aqui entra um exemplo que VOCÊ conhece de fato]" em
#   âmbar; nenhum filme, série, notícia, dado, pesquisa ou lei inventado — nem no parágrafo do eixo 2 (frases elaboradas
#   para fins didáticos, com o espaço do repertório vazio) nem no rascunho de 2021 (só causa e consequência, marcado
#   "elaborado para fins didáticos"). Tópico do rascunho de 2021 = alternativa A da Questão 3 do material (1º eixo da
#   tese). Nenhum nível ou nota da C3. Números e anos falados por extenso.
# Cores: azul = tema/eixos · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial.

TITULO = "Planeje em 5 Linhas e Escreva Comigo o 2º Parágrafo | Desenvolvimento da Redação Ep. 6"
# Estilo da voz (gerar_voz_local.py): o mesmo da série Introdução
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas ('Parece certo... mas não é!'); comemore os acertos com "
            "entusiasmo ('Letra E!'); dê ênfase forte às palavras-chave. Quando ler o parágrafo no rascunho, leia como "
            "quem lê um texto bonito, e quando pensar em voz alta, soe como quem está raciocinando de verdade. Ritmo "
            "didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente "
            "como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Hoje você não vai só assistir. [p=0.5] {b}Pegue *papel e caneta:* [p=0.3] {c}vamos escrever juntos o *segundo "
        "parágrafo* da redação sobre o estigma das doenças mentais, [p=0.3] {d}começando por *cinco linhas* de rascunho."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai ter um jeito de *planejar* qualquer parágrafo de desenvolvimento em poucos minutos "
        "[p=0.3] {b}e de saber se ele está *pronto* antes de escrever."),
    dict(id="03", block="material", text=
        "{t}Então, [p=0.2] separe agora: [p=0.2] {a}uma folha [p=0.2] {b}e uma caneta. [p=0.4] {c}Essa folha vai ser o seu "
        "*rascunho:* [p=0.2] o espaço de teste, [p=0.2] onde você planeja antes de passar o texto a limpo. [p=0.4] "
        "{d}Pegou? [p=0.3] Então vamos."),

    # ================= CONCRETO ANTES DO ABSTRATO: A LISTA DE COMPRAS =================
    dict(id="04", block="lista", text=
        "{t}Comece por uma cena do dia a dia. [p=0.3] {a}Você vai ao mercado comprar o que falta para um *bolo.* [p=0.3] "
        "{b}Antes de sair, [p=0.2] faz uma *lista de compras:* [p=0.2] {c}farinha, [p=0.2] ovos, [p=0.2] açúcar, [p=0.2] "
        "leite... [p=0.3] {d}e uma linha ficou *em branco.* [p=0.4] {e}Resultado: [p=0.2] você volta para casa *sem o "
        "ingrediente,* [p=0.2] e só descobre na hora de bater a massa."),
    dict(id="05", block="lista", text=
        "{t}Com o parágrafo é igual. [p=0.3] {a}O *planejamento em cinco linhas* é isto: [p=0.2] no rascunho, [p=0.2] "
        "antes de redigir o parágrafo inteiro, [p=0.2] você escreve *uma linha curta para cada parte.* [p=0.4] {b}O "
        "rascunho de cinco linhas é a *lista de compras* do parágrafo: [p=0.3] {c}se uma linha ficar vazia, [p=0.2] o "
        "parágrafo *ainda não está pronto.*"),

    # ================= PRÉ-REQUISITOS RELÂMPAGO =================
    dict(id="06", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago dos episódios um a cinco. [p=0.3] {a}Cada parágrafo de desenvolvimento "
        "*entrega um item* da tese, [p=0.2] em cinco etapas: [p=0.2] {b}a *etiqueta,* [p=0.2] que é o tópico frasal; "
        "[p=0.2] {c}*por que* está na caixa, [p=0.2] o argumento; [p=0.2] {d}a *nota fiscal,* [p=0.2] o repertório; "
        "[p=0.2] {e}o *produto funcionando,* [p=0.2] a análise; [p=0.2] {f}e o *recibo,* [p=0.2] o fechamento. [p=0.4] "
        "{g}E a pergunta do cliente é sempre: [p=0.2] *e daí?*"),
    dict(id="07", block="prereq", text=
        "{t}A nossa redação é a do tema de dois mil e vinte. [p=0.3] {a}A tese anunciou *dois eixos,* [p=0.2] dois "
        "caminhos de prova: [p=0.2] {b}a desinformação [p=0.2] {c}e a mídia. [p=0.4] {d}No episódio cinco, [p=0.2] você viu "
        "o parágrafo do *eixo um,* [p=0.2] com O Alienista. [p=0.4] {e}Hoje falta o *eixo dois:* [p=0.2] o segundo "
        "caminho, [p=0.2] a mídia."),
    dict(id="08", block="midia", text=
        "{t}Uma expressão antes de começar. [p=0.3] {a}*Representação midiática* [p=0.2] é o jeito como a mídia mostra "
        "alguma coisa: [p=0.2] {b}no *noticiário,* [p=0.2] que é o jornal, [p=0.2] {c}e na *ficção,* [p=0.2] as histórias "
        "inventadas dos filmes, das séries e das novelas. [p=0.4] {d}O eixo dois diz que essas representações associam o "
        "adoecimento psíquico à *violência.*"),

    # ================= NÓS FAZEMOS: QUESTÃO 9 (ABRE O PARÁGRAFO) =================
    dict(id="09", block="q9", text=
        "{t}E o parágrafo começa com *nós dois.* [p=0.3] {a}Questão nove do material. [p=0.2] A introdução de uma redação "
        "sobre o tema do ENEM dois mil e vinte anunciou dois eixos: [p=0.2] a desinformação sobre os transtornos [p=0.2] e "
        "as representações midiáticas que os associam à violência. [p=0.3] O primeiro parágrafo de desenvolvimento tratou "
        "da desinformação. [p=0.3] A frase mais adequada para abrir o segundo é: [p=0.4] {A}A: [p=0.2] Em primeiro lugar, "
        "a desinformação sobre os transtornos mentais sustenta o estigma. [p=0.4] {B}B: [p=0.2] Portanto, cabe ao "
        "Ministério da Saúde criar campanhas sobre saúde mental."),
    dict(id="10", block="q9", text=
        "{C}C: [p=0.2] Além disso, ao associar o adoecimento psíquico à violência, [p=0.2] parte da mídia reforça a imagem "
        "de perigo que alimenta o estigma. [p=0.4] {D}D: [p=0.2] A televisão foi inventada no início do século vinte. "
        "[p=0.4] {E}E: [p=0.2] Por outro lado, a desinformação também é um problema. [p=0.4] Escolha a frase que abre o "
        "segundo parágrafo. [p=0.3] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="11", block="q9", text=
        "{ok}Letra *C!* [p=0.3] Ela cumpre o segundo eixo anunciado, [p=0.2] com um conectivo de adição, [p=0.2] *além "
        "disso,* [p=0.2] e uma afirmação a provar: [p=0.2] a mídia reforça o estigma. [p=0.4] {xa}A A *repete* o primeiro "
        "eixo. [p=0.3] {xb}A B salta para a proposta, [p=0.2] que é papel da conclusão. [p=0.3] {xd}A D traz informação sem "
        "relação com o recorte. [p=0.3] {xe}E a E usa *por outro lado* sem contraste [p=0.2] e volta ao primeiro eixo."),

    # ================= EU FAÇO: AS CINCO LINHAS DO EIXO 2 =================
    dict(id="12", block="eufaco", text=
        "{t}Agora *eu faço,* [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] {a}À esquerda, [p=0.2] a nossa lista de "
        "compras: [p=0.2] cinco linhas, [p=0.2] uma para cada parte. [p=0.4] {b}Linha um, [p=0.2] *Tópico.* [p=0.2] A letra "
        "C vira a minha anotação curta: [p=0.3] {c}além disso, a mídia associa transtorno a violência."),
    dict(id="13", block="eufaco", text=
        "{a}Linha dois, [p=0.2] *Por quê.* [p=0.2] Eu me pergunto: [p=0.2] por que essa afirmação procede? [p=0.4] "
        "{b}noticiário e ficção destacam casos extremos, [p=0.2] e isso gera *imagem de perigo.* [p=0.4] {c}Repare na "
        "seta: [p=0.2] ela marca *causa e consequência.* [p=0.2] No rascunho, [p=0.2] a seta economiza palavras."),
    dict(id="14", block="eufaco", text=
        "{a}Linha três, [p=0.2] *Repertório.* [p=0.3] {b}O material pede um exemplo que eu conheça *de fato:* [p=0.2] "
        "série, [p=0.2] filme [p=0.2] ou cobertura jornalística, [p=0.2] que é o jeito como os jornais trataram um caso. "
        "[p=0.4] {c}Então eu *não* invento nada. [p=0.3] {d}Escrevo um lembrete: [p=0.2] aqui entra um exemplo que você "
        "conhece de fato."),
    dict(id="15", block="eufaco", text=
        "{t}E por que não inventar? [p=0.3] {a}O repertório é a *nota fiscal* do parágrafo. [p=0.3] {b}Um exemplo inventado "
        "é uma *nota fiscal falsa:* [p=0.2] se o corretor conhece a obra ou o caso, [p=0.2] percebe o erro, [p=0.2] e o "
        "seu argumento perde a confiança. [p=0.4] {c}Se nenhum exemplo verdadeiro vier à cabeça, [p=0.2] use *outro tipo* "
        "de fundamentação, [p=0.2] o apoio do argumento: [p=0.2] {d}uma relação de *causa e consequência* bem explicada, "
        "[p=0.2] {e}ou uma *comparação* entre situações. [p=0.4] {f}Um apoio simples, [p=0.2] mas *verdadeiro,* [p=0.2] "
        "vale mais que um inventado."),

    # ================= A PRIMEIRA TENTATIVA IMPERFEITA =================
    dict(id="16", block="eufaco", text=
        "{t}Agora, [p=0.2] a linha quatro. [p=0.3] {a}Aqui eu vou fazer como *muita gente* faz. [p=0.3] {b}O exemplo já "
        "está lá, [p=0.2] então eu pulo direto para o fim. [p=0.3] {c}Linha cinco, [p=0.2] *Fecho:* [p=0.3] {d}assim, a "
        "mídia reforça o estigma que afasta do tratamento. [p=0.4] {e}Pronto. [p=0.2] Lista feita... [p=0.3] será?"),
    dict(id="17", block="eufaco", text=
        "{t}Vamos testar com a pergunta do cliente. [p=0.3] {a}A mídia destaca casos extremos. [p=0.2] *E daí?* [p=0.4] "
        "{b}O que isso causa nas pessoas? [p=0.3] Na minha lista, [p=0.2] nada responde. [p=0.4] {c}Opa. [p=0.3] {d}Eu "
        "pulei do exemplo *direto para o fecho.* [p=0.3] {e}A linha da análise ficou *vazia.* [p=0.3] {f}E linha vazia "
        "[p=0.2] quer dizer: [p=0.2] parágrafo *não está pronto.*"),
    dict(id="18", block="eufaco", text=
        "{t}Então eu volto [p=0.2] e respondo ao *e daí?* [p=0.3] {a}Quem é afetado, [p=0.2] e de que forma? [p=0.4] "
        "{b}o público passa a temer quem tem diagnóstico, [p=0.2] e isso leva ao *isolamento* e ao *silêncio.* [p=0.4] "
        "{c}*Diagnóstico* é quando um profissional de saúde identifica o transtorno. [p=0.4] {d}Agora sim: [p=0.2] o "
        "produto funcionando. [p=0.3] {e}Cinco linhas preenchidas. [p=0.2] Lista pronta."),
    dict(id="19", block="lado", text=
        "{t}Olha as duas listas lado a lado. [p=0.3] {a}Na primeira tentativa, [p=0.2] o exemplo cai direto no fecho: "
        "[p=0.2] o leitor fica sem saber *o que* aquilo prova. [p=0.4] {b}Na versão corrigida, [p=0.2] entre o exemplo e "
        "o fecho [p=0.2] aparece a *consequência concreta:* [p=0.2] medo, [p=0.2] isolamento, [p=0.2] silêncio. [p=0.4] "
        "{c}E o fecho agora *tem de onde sair.*"),

    # ================= DAS CINCO LINHAS AO PARÁGRAFO =================
    dict(id="20", block="frases", text=
        "{t}Agora eu transformo cada linha em frase, [p=0.2] em voz alta. [p=0.3] Cada linha vira uma ou duas frases. "
        "[p=0.4] {s1}Além disso, ao associar o adoecimento psíquico à violência, [p=0.2] parte da mídia reforça a imagem "
        "de perigo que alimenta o estigma. [p=0.4] {s2}Isso acontece porque o noticiário e a ficção costumam destacar casos "
        "extremos, [p=0.2] o que fixa a imagem de que quem tem um transtorno mental é perigoso. [p=0.4] {s3}Na linha do "
        "repertório, [p=0.2] eu *não* escrevo nada inventado: [p=0.2] ali entra o *seu* exemplo, [p=0.2] com o nome certo "
        "e o que ele mostra."),
    dict(id="21", block="frases", text=
        "{s4}Com isso, [p=0.2] o público passa a temer quem tem diagnóstico, [p=0.2] e quem sofre psiquicamente acaba "
        "empurrado para o isolamento e para o silêncio, [p=0.2] em vez de buscar ajuda. [p=0.4] {s5}Assim, [p=0.2] a mídia "
        "reforça o estigma que afasta os brasileiros do tratamento. [p=0.5] {d}Parágrafo elaborado para fins didáticos, "
        "[p=0.2] com o espaço do repertório *em aberto,* [p=0.2] esperando o *seu* exemplo."),

    # ================= DICA: EQUILÍBRIO ENTRE OS PARÁGRAFOS =================
    dict(id="22", block="equilibrio", text=
        "{t}Uma dica antes de você fazer sozinho: [p=0.2] o *equilíbrio entre os parágrafos.* [p=0.3] {a}Quer dizer: "
        "[p=0.2] os dois parágrafos de desenvolvimento costumam ter *tamanho parecido* [p=0.2] e ser os mais longos da "
        "redação. [p=0.4] {b}Se um deles ficou com *metade* do outro, [p=0.3] {c}provavelmente lhe falta *análise.* "
        "[p=0.4] {d}Foi exatamente o buraco da nossa primeira tentativa."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="23", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Cinco linhas antes do parágrafo. [p=0.6] {b}Linha vazia: [p=0.2] "
        "parágrafo não está pronto. [p=0.6] {c}Repertório só o que você conhece de fato. [p=0.5]"),

    # ================= VOCÊ FAZ: ENEM 2021 =================
    dict(id="24", block="vocefaz", text=
        "{t}Agora, *você faz.* [p=0.3] {a}Tema do ENEM dois mil e vinte e um. [p=0.2] *Registro civil* [p=0.2] é o "
        "registro oficial de uma pessoa, [p=0.2] feito no *cartório.* [p=0.4] {b}A tese é esta: [p=0.3] A falta de "
        "registro civil torna parte dos brasileiros invisível para o Estado, [p=0.2] situação mantida pela distância dos "
        "cartórios [p=0.2] e pela desinformação sobre a gratuidade do registro."),
    dict(id="25", block="vocefaz", text=
        "{a}Fique com o eixo da *distância dos cartórios.* [p=0.3] {b}Faça as cinco linhas de rascunho: [p=0.2] tópico, "
        "[p=0.2] por quê, [p=0.2] repertório, [p=0.2] análise [p=0.2] e fecho. [p=0.3] {c}Confira se nenhuma linha ficou "
        "vazia [p=0.2] {d}e escreva o parágrafo. [p=0.3] {p}Pause o vídeo e escreva. [p=2.5]"),
    dict(id="26", block="vocefaz", text=
        "{t}Pronto? [p=0.2] Aqui vai *um* rascunho possível, [p=0.2] elaborado para fins didáticos. [p=0.4] {a}Tópico: "
        "[p=0.2] em primeiro lugar, a distância dos cartórios dificulta o registro em regiões isoladas. [p=0.4] {b}Por "
        "quê: [p=0.2] cartório longe, [p=0.2] viagem cara e demorada, [p=0.2] e a família adia o registro. [p=0.4] "
        "{c}Repertório: [p=0.2] de novo, [p=0.2] o *seu* exemplo, [p=0.2] ou outra fundamentação verdadeira."),
    dict(id="27", block="vocefaz", text=
        "{d}Análise: [p=0.2] sem registro, [p=0.2] a pessoa fica *invisível* para o Estado [p=0.2] e longe da cidadania. "
        "[p=0.4] {e}Fecho: [p=0.2] assim, a distância dos cartórios mantém parte dos brasileiros invisível para o Estado. "
        "[p=0.4] {f}Nenhuma linha vazia. [p=0.3] {g}Se a sua lista tem as cinco linhas, [p=0.2] você está no caminho."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="28", block="erros", text=
        "{a}Erro um: [p=0.2] começar a escrever *sem rascunho.* [p=0.4] {b}Parece certo, [p=0.2] porque economiza tempo. "
        "[p=0.4] {c}Mas aí você descobre o buraco na *folha definitiva,* [p=0.2] a que vai para a correção, [p=0.2] quando "
        "já não dá para consertar."),
    dict(id="29", block="erros", text=
        "{a}Erro dois: [p=0.2] *inventar* um exemplo para preencher a linha. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "linha do repertório fica cheia. [p=0.4] {c}Mas nota fiscal falsa derruba a confiança: [p=0.2] use o que você "
        "conhece de fato, [p=0.2] ou outra fundamentação verdadeira."),
    dict(id="30", block="erros", text=
        "{a}Erro três: [p=0.2] deixar o segundo parágrafo *muito mais curto* que o primeiro. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o tempo da prova está acabando. [p=0.4] {c}Mas parágrafo com metade do tamanho [p=0.2] "
        "provavelmente está *sem análise:* [p=0.2] confira a linha quatro."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Cinco linhas antes do parágrafo. [p=0.6] {b}Linha "
        "vazia: [p=0.2] parágrafo não está pronto. [p=0.6] {c}Repertório só o que você conhece de fato. [p=0.5]"),
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.3] {c}caçamos as *pegadinhas* [p=0.3] {d}e "
        "você recebe o *desafio* de escrever os dois desenvolvimentos de uma redação sua."),

    # ================= CTA =================
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual linha da sua lista de compras costuma ficar vazia? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
