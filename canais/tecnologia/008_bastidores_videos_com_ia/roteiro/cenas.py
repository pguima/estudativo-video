# Roteiro — Tecnologia 008: Bastidores — como eu faço estes vídeos com IA
# Base: original/fonte_bastidores.md (o próprio pipeline do projeto, números contados por script em 19/10/2026)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Como eu faço estes vídeos com IA: os bastidores do pipeline"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um criador de conteúdo de tecnologia apaixonado, mostrando os bastidores do próprio trabalho para "
            "um amigo: voz calorosa, envolvente e MUITO expressiva, com bastante variação de entonação e emoção verdadeira. "
            "Sorria na voz. Mostre entusiasmo genuíno nas descobertas, um tom de confidência e humor leve quando contar o que "
            "deu errado, e orgulho no resultado. Dê ênfase forte às palavras-chave e aos números. Ritmo natural e tranquilo, "
            "sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, sem acrescentar nem repetir nada."),
)

PRONUNCIA = {}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "{a}Este vídeo não teve *câmera.* [p=0.3] {b}Nem *microfone.* [p=0.3] {c}Nem *editor de vídeo.* [p=0.5] "
        "{d}A voz, [p=0.2] as animações, [p=0.2] as legendas: [p=0.2] tudo saiu de *código* [p=0.2] e de *IA.* [p=0.5] "
        "{e}E ele não está sozinho: [p=0.2] já são *cinquenta e três vídeos,* [p=0.2] quase *sete horas,* [p=0.2] "
        "em quatro canais. [p=0.5] {f}Hoje eu abro os *bastidores.*"),
    dict(id="02", block="mapa", text=
        "{t}O caminho tem cinco etapas. [p=0.3] {a}O *roteiro.* [p=0.2] {b}A *voz.* [p=0.2] {c}A *transcrição.* [p=0.2] "
        "{d}A *animação.* [p=0.2] {e}E a *renderização.* [p=0.4] {f}E no fim, [p=0.2] eu conto o que *deu errado* pelo caminho. "
        "[p=0.3] Porque deu!"),

    # ================= ROTEIRO =================
    dict(id="03", block="roteiro", text=
        "{t}Tudo começa no *material de estudo:* [p=0.2] apostilas que eu já tinha, [p=0.2] em HTML e markdown. [p=0.4] "
        "{a}Eu peço ao *Claude Code,* [p=0.2] e ele lê o material [p=0.2] {b}e escreve o roteiro [p=0.2] num arquivo "
        "*Python,* [p=0.2] o *cenas ponto py.* [p=0.4] {c}Cada cena é um item de uma lista, [p=0.2] com o texto que vai ser falado."),
    dict(id="04", block="marcas", text=
        "{t}Mas o texto tem umas marcações espertas. [p=0.4] {a}Uma letra entre *chaves* [p=0.2] é um gatilho: [p=0.2] "
        "nessa palavra, [p=0.2] uma animação começa. [p=0.4] {b}O *asterisco* destaca a palavra na legenda. [p=0.4] "
        "{c}E o *p igual a zero vírgula quatro* [p=0.2] é uma pausa. [p=0.5] {d}O roteiro já nasce sabendo [p=0.2] "
        "*onde* cada coisa acontece."),
    dict(id="05", block="fidelidade", text=
        "{t}E tem uma regra de ouro: [p=0.2] a IA *não* inventa conteúdo. [p=0.4] {a}Toda citação, [p=0.2] toda lei, "
        "[p=0.2] todo número, [p=0.2] tem que estar no material. [p=0.4] {b}E um script *confere,* [p=0.2] palavra por palavra, "
        "[p=0.2] se as citações do roteiro batem com o original."),

    # ================= VOZ =================
    dict(id="06", block="voz", text=
        "{t}Agora, a *voz.* [p=0.3] {a}Ela vem do *Gemini TTS,* [p=0.2] o modelo de voz do Google, [p=0.3] {b}por um app "
        "que roda aqui no meu computador. [p=0.4] {c}Um script manda o roteiro em *duas partes,* [p=0.2] {d}com a voz "
        "*Neno,* [p=0.2] {e}umas etiquetas de emoção, [p=0.2] alegre, [p=0.2] curiosa, [p=0.3] {f}e uma instrução de estilo: "
        "[p=0.2] *fale como um professor apaixonado.* [p=0.5] {g}É exatamente a voz que você está ouvindo agora."),
    dict(id="07", block="voz_erros", text=
        "{t}Só que a voz de IA *apronta.* [p=0.4] {a}Às vezes ela lê um trecho *duas vezes.* [p=0.4] {b}Às vezes "
        "*inventa* uma frase que não estava no roteiro. [p=0.4] {c}E às vezes o servidor troca para um modelo reserva, "
        "[p=0.2] com *outra voz.* [p=0.5] {d}Nesse caso, [p=0.2] o script percebe [p=0.2] e pede de novo, [p=0.2] sozinho."),

    # ================= TRANSCRIÇÃO =================
    dict(id="08", block="whisper", text=
        "{t}E como eu descubro esses erros? [p=0.4] {a}Transcrevendo a voz de volta. [p=0.3] {b}Com o *faster-whisper,* "
        "[p=0.2] modelo *small,* [p=0.2] rodando no processador. [p=0.4] {c}Ele devolve cada palavra [p=0.2] *com o "
        "segundo exato* em que ela foi dita."),
    dict(id="09", block="diff", text=
        "{t}Aí um script compara: [p=0.2] {a}o *roteiro* [p=0.2] {b}contra a *transcrição.* [p=0.4] {c}Palavra sobrando? "
        "[p=0.2] Foi repetição ou invenção. [p=0.3] Eu corto. [p=0.5] {d}E o contrário também acontece: [p=0.2] numa aula, "
        "[p=0.2] o Whisper *pulou sete segundos* de fala. [p=0.4] {e}A voz estava certa! [p=0.3] Retranscrevi só aquele pedaço."),
    dict(id="10", block="alinha", text=
        "{t}Com a transcrição limpa, [p=0.2] vem o pulo do gato. [p=0.4] {a}Outro script casa cada palavra do roteiro "
        "[p=0.2] com o tempo em que ela foi falada. [p=0.4] {b}E aí cada gatilho entre chaves [p=0.2] vira um *instante "
        "exato* do áudio. [p=0.5] {c}É por isso que a animação acontece [p=0.2] *bem na palavra.*"),

    # ================= ANIMAÇÃO =================
    dict(id="11", block="skia", text=
        "{t}Agora, a parte que eu mais gosto: [p=0.2] a *animação.* [p=0.4] {a}Não existe linha do tempo, [p=0.2] "
        "nem arrastar caixinha. [p=0.4] {b}Existe uma *função:* [p=0.2] ela recebe o *tempo,* [p=0.2] em segundos, [p=0.3] "
        "{c}e desenha o quadro daquele instante [p=0.2] com a *Skia,* [p=0.2] a biblioteca de desenho 2D do Chrome. [p=0.5] "
        "{d}Mudou o tempo, [p=0.2] muda o desenho. [p=0.3] Isso é a animação."),
    dict(id="12", block="temas", text=
        "{t}E cada canal tem o seu *estilo.* [p=0.4] {a}As aulas do ENEM, [p=0.2] claras, [p=0.2] com folha de rascunho "
        "e letra de mão. [p=0.4] {b}As aulas de Seguridade Social, [p=0.2] em verde-petróleo. [p=0.4] {c}E este canal, "
        "[p=0.2] escuro e futurista. [p=0.5] {d}As peças repetidas, [p=0.2] como cartões, [p=0.2] legendas e a tela de "
        "inscrição, [p=0.2] ficam em *bibliotecas compartilhadas.*"),
    dict(id="13", block="legenda", text=
        "{t}E a legenda? [p=0.3] {a}Ela também vem dos tempos: [p=0.2] cada palavra aparece *na hora* em que é dita, "
        "[p=0.3] {b}e as palavras com asterisco [p=0.2] *brilham.* [p=0.4] {c}Como estas."),

    # ================= RENDER =================
    dict(id="14", block="render", text=
        "{t}Falta transformar tudo em vídeo. [p=0.3] {a}São *trinta quadros* por segundo. [p=0.4] {b}Um vídeo de dez minutos "
        "[p=0.2] tem *dezoito mil quadros.* [p=0.5] {c}Então o vídeo é cortado em pedaços de *vinte segundos,* [p=0.3] "
        "{d}vários processos desenham ao mesmo tempo, [p=0.3] {e}e o *ffmpeg* transforma os quadros em vídeo [p=0.2] "
        "e junta com a narração."),
    dict(id="15", block="ram", text=
        "{t}E aqui entra a vida real. [p=0.3] {a}Meu computador tem *oito gigas* de memória. [p=0.4] {b}Uma vez eu "
        "coloquei *sete* processos em paralelo, [p=0.3] {c}e o render *estourou a memória.* [p=0.5] {d}Hoje são *três* "
        "de cada vez. [p=0.3] {e}E se algum falhar, [p=0.2] o script refaz *só os pedaços* que faltaram."),
    dict(id="16", block="previa", text=
        "{t}Antes de renderizar tudo, [p=0.2] uma revisão. [p=0.4] {a}O script tira *um quadro de cada cena* [p=0.3] "
        "{b}e monta tudo numa folha só. [p=0.4] {c}Assim dá para ver, [p=0.2] de uma vez, [p=0.2] um texto que saiu do "
        "cartão, [p=0.2] uma seta no lugar errado, [p=0.3] {d}e corrigir *antes* de gastar o render inteiro."),

    # ================= FECHAMENTO =================
    dict(id="17", block="capas", text=
        "{t}E o vídeo sai *pronto para publicar.* [p=0.4] {a}Um script desenha *três capas* para eu testar. [p=0.4] "
        "{b}E outro arquivo traz títulos, [p=0.2] descrição, [p=0.2] tags [p=0.3] {c}e os *capítulos,* [p=0.2] "
        "calculados direto dos tempos da narração."),
    dict(id="18", block="humano", text=
        "{t}Então a IA faz *tudo?* [p=0.4] {a}Não! [p=0.3] {b}Eu escolho o tema, [p=0.2] defino o estilo de cada canal, "
        "[p=0.2] e aprovo cada etapa. [p=0.4] {c}A IA faz o trabalho *pesado.* [p=0.3] {d}O critério continua sendo *meu.*"),
    dict(id="19", block="cuidados", text=
        "{t}E três cuidados, [p=0.2] se você quiser fazer algo parecido. [p=0.4] {a}Use uma *fonte confiável,* [p=0.2] "
        "e não deixe a IA inventar. [p=0.4] {b}*Confira* a voz, [p=0.2] sempre. [p=0.4] {c}E seja transparente: "
        "[p=0.2] no YouTube, [p=0.2] eu declaro que a narração é *sintética.*"),
    dict(id="20", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o Claude Code escreve o *roteiro.* [p=0.3] {b}O Gemini dá a *voz.* [p=0.3] "
        "{c}O Whisper *confere* e marca o tempo de cada palavra. [p=0.3] {d}A Skia *desenha.* [p=0.3] {e}E o ffmpeg "
        "*monta.* [p=0.4] {f}Cinco ferramentas, [p=0.2] e uma pasta por vídeo."),
    dict(id="21", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual etapa você quer ver *em detalhe* num próximo vídeo? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
