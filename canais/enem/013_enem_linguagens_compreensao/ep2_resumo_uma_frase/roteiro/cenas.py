# Roteiro — Compreensão Global e Tese, Episódio 2: O resumo em uma frase (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seção 07 + Questão 6 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o resumo é a MENSAGEM DE WHATSAPP que você mandaria para contar o texto a um amigo:
#   curta, com suas palavras, sem dar a sua opinião. Retoma a MESA do ep. 1 (exemplo = perna, não tampo).
# Fórmula (três peças que se encaixam): ASSUNTO + O QUE O TEXTO AFIRMA + O PRINCIPAL PORQUÊ (ou a proposta).
#   Cada pedaço do resumo ganha a cor da sua peça ({s1} {s2} {s3}).
# Sequência eu faço → nós fazemos → você faz: hortas (08–11) → Questão 6 lida juntos, com "pause e escreva" (21–27)
#   → desafio final: resumir a própria aula em uma frase nos comentários.
# Frases-chave (meio e fim, idênticas):
#   1. Assunto + o que o texto afirma + o porquê.
#   2. Com suas palavras, não copiando.
#   3. Resumo conta o texto, não a sua opinião.
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = fórmula/regra.
# Textos-base (parágrafo das hortas, os três resumos da seção 07, Questão 6) lidos EXATAMENTE como no material.

TITULO = "Resuma Qualquer Texto em 1 Frase: a Fórmula | Interpretação Ep. 2"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Se você não consegue dizer um texto em *uma frase,* [p=0.3] {b}você ainda não entendeu o texto. [p=0.5] "
        "{c}A boa notícia: [p=0.2] existe uma *fórmula* para isso."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resumir qualquer texto em uma frase, [p=0.3] {b}e usar isso para achar "
        "a alternativa certa [p=0.2] *antes mesmo de ler as opções.*"),

    # ================= PRÉ-REQUISITO (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, uma lembrança do episódio passado. [p=0.3] {a}*Assunto* é sobre o que o texto fala: [p=0.2] celular na escola. "
        "[p=0.4] {b}*Tese* é o que o texto diz sobre ele: [p=0.2] tem verbo, [p=0.2] e alguém poderia discordar. [p=0.3] "
        "{c}A escola deve ensinar a usar o celular."),

    # ================= O RESUMO (WHATSAPP) =================
    dict(id="04", block="whatsapp", text=
        "{t}Agora, pense na última série que você viu. [p=0.3] {a}Um amigo pergunta no WhatsApp: [p=0.2] e aí, é boa? [p=0.4] "
        "{b}Você não conta cena por cena. [p=0.3] {c}Você conta do que se trata, [p=0.2] e o que acontece."),
    dict(id="05", block="whatsapp", text=
        "{t}Sem perceber, [p=0.2] você fez um *resumo:* [p=0.2] o texto inteiro em poucas palavras, [p=0.2] *com as suas palavras.* "
        "[p=0.4] {b}Muitos livros chamam isso de *síntese.* [p=0.2] É a mesma coisa. [p=0.4] {c}Guarde a imagem: [p=0.2] "
        "o resumo é a mensagem de WhatsApp que você mandaria para contar o texto a um amigo: [p=0.3] {d}curta, [p=0.2] "
        "com suas palavras, [p=0.2] sem dar a sua opinião."),

    # ================= BLOCO A: A FÓRMULA =================
    dict(id="06", block="formula", text=
        "{t}Mas como montar essa mensagem [p=0.2] sem esquecer nada e sem inventar nada? [p=0.4] {a}Com três peças. "
        "[p=0.3] {b}Um: [p=0.2] o *assunto.* [p=0.4] {c}Dois: [p=0.2] *o que o texto afirma* sobre ele. [p=0.4] "
        "{d}Três: [p=0.2] o *principal porquê,* [p=0.2] o motivo mais forte que o texto dá. [p=0.3] {e}Ou a *proposta,* "
        "[p=0.2] se o texto sugere uma solução."),
    dict(id="07", block="formula", text=
        "{a}Na mensagem sobre a série, [p=0.2] fica assim: [p=0.3] {s1}a série da família Silva [p=0.2] "
        "{s2}vale muito a pena, [p=0.2] {s3}porque prende do primeiro ao último episódio. [p=0.4] {b}Três peças, [p=0.2] *uma frase.*"),

    # ================= BLOCO B: EU FAÇO (HORTAS) =================
    dict(id="08", block="hortas", text=
        "{t}Agora eu faço, [p=0.2] pensando em voz alta. [p=0.4] "
        "{f1}Hortas em terrenos baldios costumam ser lembradas pela alface que produzem, [p=0.2] mas o que elas cultivam de mais "
        "valioso é outra coisa. [p=0.4] {c1}Terreno baldio: [p=0.2] terreno vazio, [p=0.2] abandonado. [p=0.3] {c1b}E olha o *mas:* "
        "[p=0.2] a alface *não* é o principal."),
    dict(id="09", block="hortas", text=
        "{f2}O terreno que juntava entulho passa a ter dono coletivo; [p=0.2] vizinhos que não se cumprimentavam dividem ferramentas "
        "e turnos de rega; [p=0.2] crianças aprendem de onde vem a comida. [p=0.4] {c2}Três exemplos, [p=0.2] e todos falam de "
        "*pessoas* juntas. [p=0.4] {f3}A colheita é o pretexto [p=0.2] — o fruto é a vizinhança. [p=0.4] {c3}Pretexto é a desculpa "
        "para começar. [p=0.2] O que importa é a *vizinhança.*"),
    dict(id="10", block="hortas", text=
        "{t}Agora, peça por peça. [p=0.3] {s1}Assunto: [p=0.2] hortas comunitárias, [p=0.2] que os vizinhos cuidam juntos. "
        "[p=0.4] {s2}O que o texto afirma: [p=0.2] valem menos pela comida [p=0.2] do que pela convivência. [p=0.4] "
        "{s3}O porquê: [p=0.2] os exemplos mostram que as hortas *criam* laços."),
    dict(id="11", block="hortas", text=
        "{a}Encaixe as peças: [p=0.3] {r}Hortas comunitárias valem menos pelo alimento que produzem [p=0.2] do que pelos "
        "laços de convivência que criam. [p=0.5] {b}Esse é o resumo *fiel.* [p=0.3] Nem menos, [p=0.2] nem mais."),

    # ================= BLOCO C: OS DOIS RESUMOS ERRADOS =================
    dict(id="12", block="errados", text=
        "{t}E um resumo errado? [p=0.4] {a}Um amigo manda: [p=0.2] Hortas comunitárias produzem alface. [p=0.4] "
        "{b}Está no texto, [p=0.2] mas é só um pedaço, [p=0.2] justamente o que o texto diz *não* ser o principal. [p=0.4] "
        "{c}Esse erro se chama *redução:* [p=0.2] pegar uma parte como se fosse o todo."),
    dict(id="13", block="errados", text=
        "{a}Outro amigo manda: [p=0.2] Todo terreno baldio deveria virar horta por lei. [p=0.4] {b}O texto fala em lei? [p=0.2] "
        "Em *todo* terreno? [p=0.2] Não. [p=0.4] {c}Esse erro se chama *extrapolação:* [p=0.2] dizer mais do que o texto diz. "
        "[p=0.4] {d}No episódio três, [p=0.2] você vê os dois com calma."),
    dict(id="14", block="eixo", text=
        "{t}E o que o resumo fiel tem de diferente? [p=0.4] {a}Ele acertou o *eixo do texto:* [p=0.2] a ideia em volta da qual "
        "tudo gira, [p=0.2] como o eixo de uma roda. [p=0.4] {b}Aqui, o eixo é a vizinhança. [p=0.3] {c}A redução ficou longe dele. "
        "[p=0.3] {d}A extrapolação passou dele."),

    # ================= BLOCO D: RESUMO NÃO É CÓPIA =================
    dict(id="15", block="copia", text=
        "{t}E se você copiar a frase mais bonita do texto? [p=0.4] {a}A colheita é o pretexto [p=0.2] — o fruto é a vizinhança. "
        "[p=0.4] {b}Mande só isso para um amigo que não leu. [p=0.3] Pretexto de quê? [p=0.2] Que fruto? [p=0.4] "
        "{c}Copiar costuma dar *redução.* [p=0.3] {d}*Reescreva com as suas palavras.*"),

    # ================= BLOCO E: RESUMO NÃO OPINA =================
    dict(id="16", block="opiniao", text=
        "{t}E se você concorda com o texto? [p=0.4] {a}Hortas são ótimas, [p=0.2] e toda cidade devia ter uma. [p=0.4] "
        "{b}Isso é a *sua opinião.* [p=0.3] {c}O resumo diz o que o *texto* defende, [p=0.2] não o que *você* acha. [p=0.4] "
        "{d}No WhatsApp, [p=0.2] você conta o texto, [p=0.2] não dá palpite."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] assunto, [p=0.2] mais o que o texto afirma, [p=0.2] mais o porquê. "
        "[p=0.5] {b}Dois: [p=0.2] com suas palavras, [p=0.2] não copiando. [p=0.5] {c}Três: [p=0.2] resumo conta o texto, "
        "[p=0.2] não a sua opinião."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] copiar a *frase de efeito,* [p=0.2] aquela frase de impacto. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a frase está no texto. [p=0.4] {c}Mas ela é bonita, [p=0.2] não completa. "
        "[p=0.2] *Reescreva pela fórmula.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] resumir só um exemplo. [p=0.4] {b}Parece certo, [p=0.2] porque o exemplo é fácil de lembrar. [p=0.4] "
        "{c}Mas lembre da mesa: [p=0.2] o exemplo é *perna,* [p=0.2] não tampo."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] pôr no resumo a sua opinião, [p=0.2] ou uma proposta que o texto não faz. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque parece a continuação natural. [p=0.4] {c}Mas pergunte: [p=0.2] *em que linha isso está?*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="21", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] e vamos juntos. [p=0.4] {f1}Na adolescência, o relógio biológico "
        "costuma se atrasar: [p=0.2] o sono chega mais tarde e, com ele, a tendência de acordar mais tarde. [p=0.4] "
        "{c1}Relógio biológico: [p=0.2] o relógio de dentro do corpo. [p=0.3] {c1b}Aqui está o *assunto:* [p=0.2] o sono do adolescente."),
    dict(id="22", block="questao", text=
        "{f2}A escola, porém, continua começando cedo. [p=0.4] {c2}Olha o *porém:* [p=0.2] o corpo pede uma hora, [p=0.2] "
        "a escola cobra outra. [p=0.4] {f3}O resultado é uma privação de sono que muitos adultos interpretam como preguiça. [p=0.4] "
        "{c3}Privação de sono: [p=0.2] dormir menos do que o corpo precisa. [p=0.3] {c3b}E quem chama de preguiça [p=0.2] "
        "são os adultos, [p=0.2] não o texto."),
    dict(id="23", block="questao", text=
        "{f4}Por isso, algumas redes de ensino em outros países testaram adiar o início das aulas, [p=0.2] e pesquisadores "
        "acompanham os efeitos dessa mudança sobre a atenção e a frequência dos alunos. [p=0.4] {c4}A consequência: [p=0.2] "
        "*testes,* [p=0.2] ainda acompanhados. [p=0.2] Ninguém disse que funciona."),
    dict(id="24", block="questao", text=
        "{t}Agora, *pause o vídeo e escreva o seu resumo em uma frase,* [p=0.2] antes de ver as alternativas. [p=1.5] "
        "{b}Vamos montar. [p=0.3] {s1}Assunto: [p=0.2] o sono do adolescente e o horário da escola. [p=0.4] {s2}O que o texto afirma: "
        "[p=0.2] corpo e escola estão desencontrados, [p=0.2] e isso tira o sono do aluno. [p=0.4] {s3}A consequência: [p=0.2] "
        "testes para começar as aulas mais tarde."),
    dict(id="25", block="questao", text=
        "{t}Só agora, as alternativas. [p=0.3] A alternativa que melhor resume o texto é: [p=0.4] {a}A: [p=0.2] Adolescentes que "
        "dormem tarde precisam de mais disciplina para acordar cedo. [p=0.4] {b}B: [p=0.2] O horário das escolas brasileiras deve "
        "ser adiado imediatamente. [p=0.4] {c}C: [p=0.2] Em outros países, pesquisadores acompanham redes de ensino. [p=0.4] "
        "{d}D: [p=0.2] O descompasso entre o relógio biológico do adolescente e o horário escolar provoca privação de sono, "
        "[p=0.2] o que levou a testes de adiamento das aulas. [p=0.4] {e}E: [p=0.2] A atenção dos alunos depende exclusivamente "
        "do horário em que as aulas começam. [p=0.5] {p}*Pause e compare com o seu resumo.* [p=1.5]"),
    dict(id="26", block="questao", text=
        "{t}Vamos comparar. [p=0.3] {a}A: [p=0.2] disciplina. [p=0.2] Para o texto, o problema é o relógio do corpo. [p=0.2] "
        "A A repete a ideia dos adultos, [p=0.2] que o texto não aceita. [p=0.4] {c}C: [p=0.2] está no texto, [p=0.2] mas é só um "
        "pedaço da última frase. [p=0.2] *Redução.* [p=0.4] {b}B: [p=0.2] escolas brasileiras, [p=0.2] imediatamente? [p=0.2] "
        "O texto fala de testes em outros países. [p=0.2] *Foi além.*"),
    dict(id="27", block="questao", text=
        "{e}E: [p=0.2] exclusivamente? [p=0.2] O texto não diz isso. [p=0.2] Outra *extrapolação.* [p=0.4] {d}Sobra a D, "
        "[p=0.2] com as três peças do seu resumo: [p=0.2] {s1}assunto, [p=0.2] {s2}afirmação, [p=0.2] {s3}consequência. "
        "[p=0.3] {ok}*Letra D.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] assunto, [p=0.2] mais o que o texto afirma, [p=0.2] mais "
        "o porquê. [p=0.5] {b}Dois: [p=0.2] com suas palavras, [p=0.2] não copiando. [p=0.5] {c}Três: [p=0.2] resumo conta o texto, "
        "[p=0.2] não a sua opinião."),

    # ================= PONTE =================
    dict(id="29", block="ponte", text=
        "{t}Você já viu dois tipos de alternativa errada: [p=0.3] {a}a que pega só um pedaço, [p=0.2] {b}e a que vai além. [p=0.4] "
        "{c}No ENEM existem *cinco* tipos, [p=0.2] e eles se repetem sempre. [p=0.4] {d}Próximo episódio: [p=0.2] "
        "*as cinco alternativas-armadilha.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E um desafio nos *comentários:* [p=0.2] resuma esta aula em uma frase. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
