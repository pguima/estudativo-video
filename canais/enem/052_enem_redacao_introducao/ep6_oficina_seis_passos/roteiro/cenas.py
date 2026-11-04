# Roteiro — Redação ENEM, Introdução, Episódio 6 de 7: Oficina — montando uma introdução do zero, na ordem certa
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seções 09 (ordem de trabalho em 6 passos) e 10 (treino guiado,
#   tema de 2022) + Questão 9 da seção 12. Versão 3 da seção 07 só como UMA resposta possível no "você faz".
#   Desenvolvimento e Repertório só citados (séries próprias).
# Formato OFICINA: o professor faz tudo ao vivo no rascunho, pensando em voz alta; eu faço → nós fazemos → você faz.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora: "a introdução é a primeira a ser lida, mas não a primeira a ser pensada: primeiro você ARRUMA A CAIXA,
#   depois escreve a ETIQUETA" · etiqueta completa da série (mapa, rua de acesso, endereço + entrega, lista da caixa).
# Lidos EXATAMENTE como no material: os 6 passos da seção 09, a linha "Blocos" e o rascunho da seção 10 (tese provisória,
#   eixos A e B, referência constitucional), a introdução final da seção 10, a Questão 9 e a Versão 3 da seção 07.
# 1ª TENTATIVA IMPERFEITA (cena 10): "Desde os primórdios, os povos indígenas…" — do professor, marcada na tela
#   "tentativa elaborada para fins didáticos"; reprovada nos testes "serve para qualquer tema?" e da retirada, riscada e
#   trocada pela referência constitucional (art. 231 e art. 68 do ADCT, ambos do material).
# Frases-chave (meio e fim, idênticas):
#   1. Arrume a caixa antes de escrever a etiqueta.
#   2. Referência, ponte, tese com dois eixos.
#   3. Conferir é passar a tese pela frase temática, bloco a bloco.
# Cores: azul = tema/blocos · verde = método · amarelo = armadilha · vermelho = erro · roxo = regra oficial.

TITULO = "Escreva uma Introdução do ENEM Comigo, do Zero, em 6 Passos | Introdução da Redação Ep. 6"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Esta aula é uma oficina: quando escrever no rascunho, soe como "
            "quem está raciocinando de verdade, em voz alta; na primeira tentativa, mostre a dúvida e depois a "
            "descoberta do erro; comemore quando a introdução fica pronta. Faça as perguntas com curiosidade genuína e dê "
            "ênfase forte às palavras-chave. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Hoje você não vai só assistir. [p=0.5] {b}Pegue *papel e caneta:* [p=0.3] {c}vamos montar uma introdução do "
        "ENEM juntos, [p=0.2] do rascunho ao parágrafo pronto, [p=0.3] {d}em *seis passos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai ter uma *ordem de trabalho* [p=0.2] para escrever qualquer introdução [p=0.2] {b}em "
        "até *dez minutos* de rascunho."),
    dict(id="03", block="material", text=
        "{t}Então, [p=0.2] separe agora: [p=0.3] {a}uma folha, [p=0.2] {b}uma caneta [p=0.2] {c}e mais *duas cores.* "
        "[p=0.4] {d}Elas vão marcar as partes do parágrafo. [p=0.3] {e}Pegou? [p=0.3] Então vamos."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="04", block="prereq", text=
        "{t}Antes, [p=0.2] o que você já sabe, em quarenta e cinco segundos. [p=0.4] {a}Da série Leitura da proposta: "
        "[p=0.2] a frase temática se divide em *blocos,* [p=0.2] e cada bloco é uma exigência. [p=0.3] {b}E a *tese "
        "provisória* é a primeira resposta ao tema, [p=0.2] que ainda pode mudar."),
    dict(id="05", block="prereq", text=
        "{c}Desta série: [p=0.2] o *mapa* abre a introdução, [p=0.2] por uma de quatro portas: [p=0.2] lei, história, dado "
        "ou conceito. [p=0.4] {d}A *rua de acesso* é a ponte: [p=0.2] a frase que liga a referência ao recorte. [p=0.4] "
        "{e}E a tese entrega o endereço, [p=0.2] com a *lista da caixa:* [p=0.2] os dois eixos, [p=0.2] os dois caminhos "
        "que o desenvolvimento vai seguir."),

    # ================= A CAIXA ANTES DA ETIQUETA =================
    dict(id="06", block="caixa", text=
        "{t}Agora, [p=0.2] uma pergunta: [p=0.2] você colaria a lista do que vai dentro da caixa [p=0.2] antes de saber o "
        "que vai dentro? [p=0.5] {a}Claro que não. [p=0.3] {b}Primeiro você *arruma a caixa,* [p=0.3] {c}depois escreve a "
        "*etiqueta.* [p=0.5] {d}Com a introdução é igual: [p=0.2] ela é a primeira a ser *lida,* [p=0.3] {e}mas não a "
        "primeira a ser *pensada.*"),
    dict(id="07", block="passos", text=
        "{t}Por isso, [p=0.2] no rascunho, [p=0.2] uma ordem que costuma funcionar. [p=0.3] {a}Um: [p=0.2] *tese "
        "provisória,* [p=0.2] a resposta à pergunta-problema, feita na leitura da proposta. [p=0.4] {b}Dois: [p=0.2] "
        "*eixos,* [p=0.2] os dois argumentos que sustentam a tese, [p=0.2] cada um com seu repertório. [p=0.4] "
        "{c}Três: [p=0.2] *contextualização,* [p=0.2] a referência que melhor prepara essa tese."),
    dict(id="08", block="passos", text=
        "{d}Quatro: [p=0.2] *ponte,* [p=0.2] a frase que liga a referência ao recorte. [p=0.4] {e}Cinco: [p=0.2] *tese "
        "final com antecipação,* [p=0.2] a tese reescrita já com os dois eixos. [p=0.4] {f}Seis: [p=0.2] *conferência:* "
        "[p=0.2] a introdução cobre os blocos da frase temática? [p=0.2] A conclusão vai retomá-la? [p=0.5] {g}Repare: "
        "[p=0.2] a etiqueta só aparece no passo *três.* [p=0.3] {h}E isso é *método de estudo,* [p=0.2] não critério do "
        "Inep."),

    # ================= EU FAÇO: ENEM 2022 =================
    dict(id="09", block="tema", text=
        "{t}Eu faço primeiro, [p=0.2] você acompanha. [p=0.3] {a}Tema do ENEM dois mil e vinte e dois: [p=0.3] Desafios "
        "para a valorização de comunidades e povos tradicionais no Brasil. [p=0.5] {b}Blocos: [p=0.2] *desafios,* [p=0.3] "
        "{c}*valorização,* [p=0.3] {d}*comunidades e povos tradicionais,* [p=0.3] {e}e *Brasil.*"),
    dict(id="10", block="tema", text=
        "{a}Povos tradicionais são, por exemplo, [p=0.2] os indígenas, [p=0.2] {b}os *quilombolas,* [p=0.2] comunidades "
        "formadas a partir dos antigos quilombos, [p=0.3] {c}e os *ribeirinhos,* [p=0.2] que vivem à beira dos rios, [p=0.2] "
        "entre outros."),
    dict(id="11", block="p1", text=
        "{t}Passo um: [p=0.2] a tese provisória. [p=0.3] {a}Eu me pergunto: [p=0.2] o que impede essa valorização? "
        "[p=0.4] {b}E escrevo: [p=0.3] a valorização esbarra na insegurança sobre o território e no desconhecimento de "
        "seus modos de vida."),
    dict(id="12", block="p2", text=
        "{t}Passo dois: [p=0.2] os eixos. [p=0.3] {a}Eixo A, [p=0.2] *território:* [p=0.2] sem terra garantida, os modos de "
        "vida tradicionais não se sustentam. [p=0.5] {b}Eixo B, [p=0.2] *desconhecimento:* [p=0.2] a escola e a mídia "
        "pouco mostram esses povos fora de estereótipos. [p=0.5] {c}Pronto: [p=0.2] a caixa está arrumada. [p=0.3] Agora, "
        "sim, [p=0.2] a etiqueta."),

    # ================= PASSO 3: A PRIMEIRA TENTATIVA =================
    dict(id="13", block="p3", text=
        "{t}Passo três: [p=0.2] a contextualização. [p=0.3] {a}Deixa eu começar como muita gente começa. [p=0.4] {b}Desde "
        "os primórdios, os povos indígenas... [p=0.6] {c}Hum. [p=0.3] Parece bonito. [p=0.3] {d}Mas vamos testar."),
    dict(id="14", block="p3", text=
        "{a}Primeiro teste: [p=0.2] essa frase *serve para qualquer tema?* [p=0.4] {b}Desde os primórdios, a escrita. "
        "[p=0.2] Desde os primórdios, a música. [p=0.3] {c}Serve. [p=0.2] Então não diz nada sobre o *meu.* [p=0.5] "
        "{d}Segundo teste: [p=0.2] o *teste da retirada.* [p=0.3] {e}Se eu apago a frase, [p=0.2] o texto perde alguma "
        "coisa? [p=0.4] {f}Não perde. [p=0.3] {g}Então ela não estava trabalhando. [p=0.3] {h}Risco."),
    dict(id="15", block="p3", text=
        "{t}Eu troco por uma referência que se liga ao recorte. [p=0.3] {a}Olha o que diz a Constituição de mil novecentos e "
        "oitenta e oito: [p=0.3] {b}no artigo duzentos e trinta e um, [p=0.2] ela reconhece aos indígenas sua organização "
        "social, costumes, línguas, crenças e tradições, [p=0.2] e os direitos sobre as terras que tradicionalmente "
        "ocupam. [p=0.4] {c}E no artigo sessenta e oito do *A D C T,* [p=0.2] o Ato das Disposições Constitucionais "
        "Transitórias, [p=0.2] assegura aos remanescentes das comunidades dos quilombos [p=0.2] a propriedade das terras "
        "que ocupam."),
    dict(id="16", block="p3", text=
        "{t}Repare: [p=0.2] ela fala de *terra,* [p=0.2] que é o meu eixo A. [p=0.4] {a}Então escrevo: [p=0.3] A "
        "Constituição Federal de mil novecentos e oitenta e oito reconhece aos povos indígenas seus costumes, línguas e tradições, [p=0.2] bem como os "
        "direitos sobre as terras que tradicionalmente ocupam, [p=0.2] e assegura às comunidades quilombolas a propriedade "
        "de seus territórios."),

    # ================= PASSO 4: A PONTE =================
    dict(id="17", block="p4", text=
        "{t}Passo quatro: [p=0.2] a ponte. [p=0.3] {a}A lei promete. [p=0.2] E a realidade? [p=0.4] {b}Duas palavras "
        "fazem a virada: [p=0.2] *na prática, contudo.* [p=0.4] {c}Na prática, contudo, muitos desses grupos ainda lutam "
        "pela demarcação ou pela titulação de suas terras [p=0.2] e são retratados de forma estereotipada, [p=0.2] como se "
        "pertencessem apenas ao passado."),
    dict(id="18", block="p4", text=
        "{a}*Demarcação* [p=0.2] é o reconhecimento oficial dos limites de uma terra indígena. [p=0.4] {b}*Titulação* "
        "[p=0.2] é a entrega do título de propriedade a uma comunidade quilombola. [p=0.4] {c}E repare: [p=0.2] essa frase "
        "já toca nos *dois* eixos: [p=0.2] {d}terra [p=0.2] {e}e estereótipo."),

    # ================= PASSO 5: A TESE FINAL =================
    dict(id="19", block="p5", text=
        "{t}Passo cinco: [p=0.2] a tese final, [p=0.2] já com a lista da caixa. [p=0.4] {a}Assim, a valorização das "
        "comunidades e dos povos tradicionais no Brasil depende de superar dois obstáculos: [p=0.3] {b}a insegurança "
        "territorial, que ameaça seus modos de vida, [p=0.3] {c}e o desconhecimento da sociedade sobre suas culturas."),
    dict(id="20", block="pronta", text=
        "{t}Olha a introdução inteira. [p=0.3] {a}Referência constitucional *verificável:* [p=0.2] o contexto. [p=0.4] "
        "{b}Contraste com a realidade, [p=0.2] com na prática, contudo: [p=0.2] a ponte. [p=0.4] {c}E tese com dois eixos "
        "*nomeados:* [p=0.2] a antecipação."),

    # ================= PASSO 6: A CONFERÊNCIA =================
    dict(id="21", block="p6", text=
        "{t}Passo seis: [p=0.2] a conferência. [p=0.3] Frase temática em cima, [p=0.2] introdução embaixo. [p=0.4] "
        "{a}Desafios? [p=0.2] Tem: [p=0.2] dois obstáculos. [p=0.4] {b}Valorização? [p=0.2] Tem. [p=0.4] {c}Comunidades e "
        "povos tradicionais? [p=0.2] Tem. [p=0.4] {d}Brasil? [p=0.2] Tem."),
    dict(id="22", block="p6", text=
        "{a}E os dois eixos já têm *destino:* [p=0.3] {b}um parágrafo de desenvolvimento para o território, [p=0.3] {c}outro "
        "para o desconhecimento. [p=0.4] {d}E a conclusão vai retomar os dois. [p=0.4] {e}Introdução *pronta.*"),

    # ================= RECAPITULAÇÃO NO MEIO =================
    dict(id="23", block="recap", text=
        "{t}Guarde três frases. [p=0.3] {a}Arrume a caixa antes de escrever a etiqueta. [p=0.6] {b}Referência, ponte, tese "
        "com dois eixos. [p=0.6] {c}Conferir é passar a tese pela frase temática, bloco a bloco. [p=0.8]"),

    # ================= NÓS FAZEMOS: QUESTÃO 9 =================
    dict(id="24", block="q9", text=
        "{t}Agora, *nós fazemos.* [p=0.3] {a}Questão nove, [p=0.2] mesmo tema de dois mil e vinte e dois. [p=0.3] Uma das "
        "teses abaixo tende a levar o texto ao *tangenciamento.* [p=0.2] Qual? [p=0.4] {A}A: [p=0.2] A valorização dos povos "
        "tradicionais brasileiros esbarra na insegurança territorial e no desconhecimento da sociedade sobre seus modos de "
        "vida."),
    dict(id="25", block="q9", text=
        "{B}B: [p=0.2] No Brasil, comunidades quilombolas, indígenas e ribeirinhas ainda são pouco valorizadas [p=0.2] porque "
        "o Estado demora a garantir seus territórios e a escola pouco as apresenta. [p=0.4] {C}C: [p=0.2] A falta de "
        "demarcação de terras e o preconceito dificultam a valorização dos povos tradicionais no país."),
    dict(id="26", block="q9", text=
        "{D}D: [p=0.2] Os povos indígenas da América do Sul desenvolveram, ao longo dos séculos, técnicas agrícolas "
        "variadas. [p=0.4] {E}E: [p=0.2] Valorizar os povos tradicionais do Brasil exige enfrentar o estereótipo que os "
        "associa apenas ao passado e a pressão econômica sobre suas terras. [p=0.4] {p}Pause o vídeo e tente: [p=0.2] qual "
        "tangencia, [p=0.2] e que blocos ela perde? [p=2.0]"),
    dict(id="27", block="q9", text=
        "{ok}Letra *D.* [p=0.3] Vamos conferir bloco a bloco. [p=0.3] {d1}Desafios? [p=0.2] Não tem. [p=0.3] "
        "{d2}Valorização? [p=0.2] Não tem. [p=0.3] {d3}Brasil? [p=0.2] Não: [p=0.2] é a América do Sul. [p=0.4] {d4}Ela fala "
        "de povos indígenas, [p=0.2] parte do assunto amplo, [p=0.2] e fica só no assunto: [p=0.2] *tangenciamento.*"),
    dict(id="28", block="q9", text=
        "{xa}As outras cobrem os blocos. [p=0.3] A A, a C e a E nomeiam obstáculos à valorização no Brasil: [p=0.3] {xc}na "
        "C, [p=0.2] no país; [p=0.3] {xe}na E, [p=0.2] do Brasil. [p=0.4] {xb}E a B cita grupos, [p=0.2] lugar [p=0.2] e "
        "dois desafios."),

    # ================= VOCÊ FAZ: ENEM 2024 =================
    dict(id="29", block="vocefaz", text=
        "{t}Agora, *você faz.* [p=0.3] {a}Tema do ENEM dois mil e vinte e quatro: [p=0.3] Desafios para a valorização da "
        "herança africana no Brasil. [p=0.5] {b}Siga os seis passos [p=0.2] {c}e escreva a sua introdução. [p=0.3] {d}Use "
        "uma das quatro portas do episódio dois: [p=0.2] lei, história, dado ou conceito. [p=0.4] {p}Pause o vídeo e "
        "escreva. [p=2.5]"),
    dict(id="30", block="vocefaz", text=
        "{a}Pronto? [p=0.3] Aqui vai *uma* resposta possível, [p=0.2] a Versão três do episódio cinco. [p=0.4] {b}A Lei dez "
        "mil seiscentos e trinta e nove, de dois mil e três, abre o mapa. [p=0.4] {c}O porém faz a ponte. [p=0.4] {d}E a tese traz "
        "dois eixos: [p=0.2] a escola [p=0.2] e a mídia. [p=0.5] {e}Ela é *uma* resposta, [p=0.2] não a única. "
        "[p=0.3] Se a sua tem as quatro peças da etiqueta, [p=0.2] está no caminho."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="31", block="erros", text=
        "{t}Os erros clássicos. [p=0.3] {a}Primeiro: [p=0.2] escrever a antecipação *antes* de planejar os parágrafos. "
        "[p=0.4] {b}Parece certo porque a introdução vem primeiro na folha. [p=0.4] {c}Mas a lista da caixa se escreve "
        "*depois* de arrumar a caixa."),
    dict(id="32", block="erros", text=
        "{a}Segundo: [p=0.2] pular a conferência porque a introdução ficou bonita. [p=0.4] {b}Parece certo porque o "
        "parágrafo soa bem. [p=0.4] {c}Mas bonito não é completo: [p=0.2] passe bloco a bloco."),
    dict(id="33", block="erros", text=
        "{a}Terceiro: [p=0.2] deixar a introdução crescer com exemplos que são do desenvolvimento. [p=0.4] {b}Parece certo "
        "porque mostra que você sabe muito. [p=0.4] {c}Mas os exemplos são do desenvolvimento: [p=0.2] na introdução, só "
        "anuncie os eixos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="34", block="recap", text=
        "{t}As mesmas três frases, para fechar. [p=0.3] {a}Arrume a caixa antes de escrever a etiqueta. [p=0.6] "
        "{b}Referência, ponte, tese com dois eixos. [p=0.6] {c}Conferir é passar a tese pela frase temática, bloco a bloco. "
        "[p=0.8]"),

    # ================= PONTE E CTA =================
    dict(id="35", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] {b}juntamos tudo, [p=0.3] {c}caçamos as *pegadinhas* [p=0.3] {d}e "
        "você recebe um *desafio* com três temas reais."),
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] por qual porta você abriu a sua introdução sobre a herança africana? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do "
        "ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
