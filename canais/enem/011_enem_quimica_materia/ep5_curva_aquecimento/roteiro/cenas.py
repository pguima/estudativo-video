# Roteiro — Matéria, Substâncias e Misturas, Episódio 5: A curva de aquecimento (aula para iniciantes)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seção 02 (PF, PE e estado físico),
#       seções 06 e 07 + Questões 8, 2 e 6 da seção 12
# Fora do recorte: calor latente e mudanças de estado em detalhe (série Estados físicos); destilação (série Separação).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o patamar é a CABINE DO PEDÁGIO. A temperatura sobe pela estrada, para na cabine enquanto o material
#   "paga" a mudança de estado e só volta a subir depois. Pura para em DUAS cabines; mistura comum passa direto.
# Ritual de leitura de todo gráfico: conte os patamares → onde estão (fusão ou ebulição)? → classifique.
# Frases-chave (meio e fim, idênticas):
#   1. Dois patamares: puro. Nenhum: mistura comum.
#   2. Um patamar só: eutética se for na fusão, azeotrópica se for na ebulição.
#   3. O gráfico não diz se é simples ou composta.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica (patamar) · vermelho = erro.

TITULO = "Como saber se um material é puro só com um termômetro? Curva de aquecimento do zero — Química ENEM, episódio 5"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Sem laboratório, [p=0.2] sem análise química, [p=0.3] {b}só com um termômetro e um relógio, [p=0.3] "
        "{c}dá para descobrir se um material é *puro.* [p=0.5] {d}Esse gráfico [p=0.2] é o item mais cobrado deste assunto no ENEM."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai bater o olho numa curva de aquecimento [p=0.3] {b}e dizer: [p=0.2] "
        "substância *pura,* [p=0.2] mistura *comum,* [p=0.2] *eutética* [p=0.2] ou *azeotrópica.*"),

    # ================= PRÉ-REQUISITOS (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembranças rápidas. [p=0.3] {a}Gelo derretendo: [p=0.2] sólido virando líquido. [p=0.2] "
        "Isso é a *fusão.* [p=0.4] {b}Água fervendo: [p=0.2] líquido virando gás. [p=0.2] Isso é a *ebulição.*"),
    dict(id="04", block="prereq", text=
        "{t}No gráfico desta aula, [p=0.2] {a}o *tempo* fica no eixo deitado, [p=0.3] {b}e a *temperatura* no eixo em pé. "
        "[p=0.4] {c}Linha subindo: [p=0.2] esquentando. [p=0.3] Linha deitada: [p=0.2] temperatura parada."),
    dict(id="05", block="prereq", text=
        "{t}E cuidado com os negativos. [p=0.3] {a}Menos cento e catorze graus [p=0.2] é muito mais frio que vinte e cinco. "
        "[p=0.4] {b}No termômetro, [p=0.2] quanto mais negativo, [p=0.2] *mais embaixo.*"),

    # ================= BLOCO A: PF, PE E ESTADO FÍSICO =================
    dict(id="06", block="pfpe", text=
        "{t}Em que temperatura o gelo derrete? [p=0.4] {a}Zero grau. [p=0.3] Essa temperatura se chama *ponto de fusão,* "
        "[p=0.2] ou PF: [p=0.2] onde o sólido vira líquido. [p=0.5] {b}E a água ferve a cem graus, [p=0.2] ao nível do mar. "
        "[p=0.3] Esse é o *ponto de ebulição,* [p=0.2] ou PE: [p=0.2] onde o líquido vira gás."),
    dict(id="07", block="regua", text=
        "{t}E para que servem esses dois números? [p=0.4] {a}Para descobrir o estado do material em qualquer temperatura. "
        "[p=0.4] {b}Imagine uma régua de temperatura. [p=0.3] {c}Abaixo do PF: [p=0.2] *sólido.* [p=0.3] {d}Entre o PF e o PE: "
        "[p=0.2] *líquido.* [p=0.3] {e}Acima do PE: [p=0.2] *gasoso.*"),
    dict(id="08", block="mercurio", text=
        "{t}Teste com o mercúrio, [p=0.2] o líquido prateado dos termômetros antigos. [p=0.4] {a}PF: [p=0.2] menos trinta e nove graus. "
        "[p=0.3] {b}PE: [p=0.2] trezentos e cinquenta e sete. [p=0.4] {c}A temperatura ambiente, [p=0.2] uns vinte e cinco graus, "
        "[p=0.2] fica entre os dois: [p=0.2] *líquido.* [p=0.4] {d}Por isso, [p=0.2] ele é o único metal líquido na temperatura ambiente."),

    # ================= BLOCO B: A CURVA DA SUBSTÂNCIA PURA =================
    dict(id="09", block="curva", text=
        "{t}Agora, o grande truque. [p=0.3] {a}Coloque gelo num béquer, [p=0.2] no fogo, [p=0.2] com um termômetro dentro. "
        "[p=0.4] {b}A cada minuto, [p=0.2] anote a temperatura [p=0.2] e marque no gráfico. [p=0.4] {c}Esse desenho se chama "
        "*curva de aquecimento:* [p=0.2] o gráfico da temperatura enquanto o material esquenta."),
    dict(id="10", block="curva", text=
        "{t}E o que aparece? [p=0.4] {a}A temperatura sobe [p=0.3] até zero grau. [p=0.4] {b}E trava. [p=0.4] {c}O gelo está derretendo, "
        "[p=0.2] e o termômetro não sai do zero. [p=0.3] A linha fica deitada. [p=0.4] {d}Esse trecho deitado se chama *patamar:* "
        "[p=0.2] a temperatura parada enquanto o material muda de estado."),
    dict(id="11", block="curva", text=
        "{t}Pense numa estrada com *pedágio.* [p=0.4] {a}A temperatura vem subindo pela estrada [p=0.2] e para na cabine "
        "[p=0.2] enquanto o material *paga* a mudança de estado. [p=0.4] {b}Toda a energia do fogo vai para derreter o gelo. "
        "[p=0.4] {c}Quando o último pedaço derrete, [p=0.2] a cancela abre, [p=0.2] e a temperatura volta a subir."),
    dict(id="12", block="curva", text=
        "{t}E depois? [p=0.3] {a}Sobe até cem graus [p=0.3] {b}e para de novo: [p=0.2] a água fervendo. [p=0.2] Segunda cabine. "
        "[p=0.4] {c}Só quando toda a água vira vapor, [p=0.2] a temperatura volta a subir. [p=0.4] {d}Substância pura: "
        "[p=0.2] *dois patamares.* [p=0.3] O primeiro no PF, [p=0.2] o segundo no PE."),

    # ================= BLOCO C: A CURVA DA MISTURA COMUM =================
    dict(id="13", block="comum", text=
        "{t}E se for água com sal? [p=0.4] {a}Mesmo experimento. [p=0.3] A curva sobe, [p=0.3] {b}e não para. [p=0.3] "
        "Ela fica menos inclinada, [p=0.2] mas não deita. [p=0.4] {c}Numa mistura, [p=0.2] cada componente muda de estado "
        "numa temperatura diferente. [p=0.4] {d}Mistura comum: [p=0.2] *nenhum patamar.* [p=0.3] Passa direto pelo pedágio."),
    dict(id="14", block="ritual", text=
        "{t}Então, todo gráfico se lê com o mesmo ritual. [p=0.4] {a}Um: [p=0.2] conte os patamares. [p=0.4] {b}Dois: "
        "[p=0.2] veja onde eles estão: [p=0.2] na fusão ou na ebulição. [p=0.4] {c}Três: [p=0.2] classifique."),

    # ================= BLOCO D: O LIMITE DO GRÁFICO =================
    dict(id="15", block="limite", text=
        "{t}Mas o gráfico tem um limite. [p=0.4] {a}A água pura e o gás oxigênio: [p=0.2] os dois são puros, [p=0.2] "
        "os dois têm dois patamares. [p=0.4] {b}Só que a água é composta, [p=0.2] e o oxigênio é simples. [p=0.4] "
        "{c}O gráfico separa puro de mistura. [p=0.3] {d}Simples ou composta? [p=0.2] Só olhando a fórmula, [p=0.2] "
        "como no episódio um."),

    # ================= BLOCO E: AS MISTURAS QUE ENGANAM =================
    dict(id="16", block="solda", text=
        "{t}Agora, as misturas que enganam o gráfico. [p=0.4] {a}Pense na *solda* do eletricista: [p=0.2] o metal que ele derrete "
        "para grudar fios. [p=0.4] {b}A solda é uma *liga:* [p=0.2] uma mistura de metais. [p=0.3] Sessenta e três por cento de estanho "
        "[p=0.2] e trinta e sete de chumbo."),
    dict(id="17", block="eutetica", text=
        "{t}E como fica a curva dela? [p=0.4] {a}Ela derrete certinho, [p=0.2] a cento e oitenta e três graus: [p=0.2] "
        "*um patamar* na fusão. [p=0.4] {b}Mas ferve numa faixa de temperaturas, [p=0.2] sem parar. [p=0.4] {c}Mistura com "
        "patamar só na fusão [p=0.2] se chama *mistura eutética.*"),
    dict(id="18", block="azeotropica", text=
        "{t}E o álcool noventa e seis por cento do supermercado? [p=0.4] {a}É mistura de álcool e água. [p=0.3] Derrete numa faixa, "
        "[p=0.3] {b}mas ferve certinho, [p=0.2] a cerca de setenta e oito graus. [p=0.4] {c}Patamar só na ebulição: "
        "[p=0.2] *mistura azeotrópica.*"),
    dict(id="19", block="confundir", text=
        "{t}Como não trocar os nomes? [p=0.4] {a}A solda *funde* certinho: [p=0.2] *eutética.* [p=0.4] {b}O álcool *ferve* "
        "certinho: [p=0.2] *azeotrópica.* [p=0.4] {c}E o teste definitivo: [p=0.2] só a substância pura [p=0.2] para nas *duas* cabines."),
    dict(id="20", block="quatro", text=
        "{t}Veja as quatro curvas lado a lado. [p=0.4] {a}Pura: [p=0.2] dois patamares. [p=0.4] {b}Eutética: [p=0.2] patamar só embaixo, "
        "[p=0.2] na fusão. [p=0.4] {c}Azeotrópica: [p=0.2] patamar só em cima, [p=0.2] na ebulição. [p=0.4] {d}Comum: [p=0.2] nenhum."),
    dict(id="21", block="alcool", text=
        "{t}E isso tem uma consequência prática. [p=0.4] {a}O álcool comum [p=0.2] não passa de noventa e seis por cento [p=0.2] "
        "numa destilação simples, [p=0.2] que é ferver e recolher o vapor. [p=0.4] {b}Como ele ferve como se fosse puro, "
        "[p=0.2] o vapor sai com a mesma mistura do líquido. [p=0.4] {c}A destilação vai ganhar vídeo próprio."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dois patamares: puro. [p=0.2] Nenhum: mistura comum. [p=0.5] "
        "{b}Dois: [p=0.2] um patamar só: [p=0.2] eutética se for na fusão, [p=0.2] azeotrópica se for na ebulição. [p=0.5] "
        "{c}Três: [p=0.2] o gráfico não diz se é simples ou composta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erro1", text=
        "{t}Agora, os quatro erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] temperatura constante numa mudança "
        "prova que é puro. [p=0.4] {b}Parece certo, [p=0.2] porque o patamar é a marca da substância pura. [p=0.4] "
        "{c}Mas eutéticas e azeotrópicas também têm um patamar. [p=0.3] *Puro precisa de dois.*"),
    dict(id="24", block="erro2", text=
        "{a}Segundo: [p=0.2] a curva mostra se é simples ou composta. [p=0.4] {b}Parece certo, [p=0.2] porque ela já mostrou "
        "se é puro. [p=0.4] {c}Mas água e oxigênio têm curvas do mesmo tipo. [p=0.3] *Para isso, só a fórmula.*"),
    dict(id="25", block="erro3", text=
        "{a}Terceiro: [p=0.2] trocar eutética e azeotrópica. [p=0.4] {b}Parece fácil confundir, [p=0.2] porque os dois nomes "
        "são estranhos [p=0.2] e as duas têm um patamar só. [p=0.4] {c}Lembre: [p=0.2] a solda *funde* certinho, [p=0.2] "
        "o álcool *ferve* certinho."),
    dict(id="26", block="erro4", text=
        "{a}Quarto: [p=0.2] errar o estado por causa de um sinal de menos. [p=0.4] {b}Parece certo, [p=0.2] porque cento e oitenta "
        "e três parece maior que vinte e cinco. [p=0.4] {c}Mas menos cento e oitenta e três [p=0.2] é muito mais frio. [p=0.3] "
        "*Desenhe a régua.*"),

    # ================= QUESTÃO 8 =================
    dict(id="27", block="q8", text=
        "{t}Agora, três questões no estilo do ENEM. [p=0.4] {e1}Primeira. [p=0.2] A tabela mostra os pontos de fusão e de ebulição "
        "de quatro substâncias. [p=0.3] {e2}Etanol: [p=0.2] menos cento e catorze e setenta e oito. [p=0.3] Cloreto de sódio: "
        "[p=0.2] oitocentos e um e mil quatrocentos e treze. [p=0.3] Oxigênio: [p=0.2] menos duzentos e dezenove e menos cento e oitenta e três. "
        "[p=0.3] Mercúrio: [p=0.2] menos trinta e nove e trezentos e cinquenta e sete. [p=0.4] {e3}A vinte e cinco graus, "
        "[p=0.2] quantas estão no estado líquido? [p=0.4] {a}A: [p=0.2] zero. [p=0.2] {b}B: [p=0.2] uma. [p=0.2] {c}C: [p=0.2] duas. "
        "[p=0.2] {d}D: [p=0.2] três. [p=0.2] {e}E: [p=0.2] quatro. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="28", block="q8", text=
        "{t}A régua, uma por uma. [p=0.3] {s1}Etanol: [p=0.2] vinte e cinco fica entre menos cento e catorze e setenta e oito. "
        "[p=0.2] *Líquido.* [p=0.4] {s2}Cloreto de sódio: [p=0.2] vinte e cinco está abaixo do PF. [p=0.2] Sólido. [p=0.4] "
        "{s3}Oxigênio: [p=0.2] vinte e cinco está acima de menos cento e oitenta e três. [p=0.2] Gasoso. [p=0.4] {s4}Mercúrio: "
        "[p=0.2] entre menos trinta e nove e trezentos e cinquenta e sete. [p=0.2] *Líquido.* [p=0.4] {ok}Duas: [p=0.2] *letra C.*"),
    dict(id="29", block="q8", text=
        "{xd}Quem marcou D, três, [p=0.2] errou o sinal do oxigênio. [p=0.4] {xb}Quem marcou B, uma, [p=0.2] esqueceu o mercúrio, "
        "[p=0.2] achando que metal é sempre sólido. [p=0.4] {xa}E a A e a E [p=0.2] ignoram a régua: [p=0.2] zero ou todas."),

    # ================= QUESTÃO 2 =================
    dict(id="30", block="q2", text=
        "{t}Segunda. [p=0.3] {e1}Uma amostra foi aquecida sem parar. [p=0.3] {e2}A temperatura ficou constante em oitenta graus "
        "durante toda a fusão [p=0.3] e de novo constante em duzentos e dezoito graus durante toda a ebulição. [p=0.4] "
        "{e3}A amostra é: [p=0.3] {a}A: [p=0.2] uma substância pura. [p=0.2] {b}B: [p=0.2] uma mistura comum. [p=0.2] "
        "{c}C: [p=0.2] uma mistura eutética. [p=0.2] {d}D: [p=0.2] uma mistura azeotrópica. [p=0.2] {e}E: [p=0.2] uma substância simples. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="31", block="q2", text=
        "{t}O ritual. [p=0.3] {r1}Patamares: [p=0.2] dois. [p=0.3] {r2}Um na fusão, [p=0.2] outro na ebulição. [p=0.3] "
        "{r3}Duas cabines: [p=0.2] *substância pura.* [p=0.2] {ok}*Letra A.* [p=0.4] {xc}A C teria patamar só na fusão. [p=0.3] "
        "{xd}A D, só na ebulição. [p=0.3] {xb}A B, nenhum. [p=0.4] {xe}E a E é a armadilha: [p=0.2] o gráfico não diz se é simples. "
        "[p=0.3] Poderia ser O dois [p=0.2] ou H dois O."),

    # ================= QUESTÃO 6 =================
    dict(id="32", block="q6", text=
        "{t}Terceira. [p=0.3] {e1}Uma liga usada em soldagem [p=0.2] funde numa temperatura constante de cento e oitenta e três graus, "
        "[p=0.3] {e2}mas entra em ebulição ao longo de uma faixa de temperatura. [p=0.4] {e3}Ela é: [p=0.3] {a}A: [p=0.2] "
        "substância pura simples. [p=0.2] {b}B: [p=0.2] substância pura composta. [p=0.2] {c}C: [p=0.2] mistura eutética. [p=0.2] "
        "{d}D: [p=0.2] mistura azeotrópica. [p=0.2] {e}E: [p=0.2] mistura comum. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="33", block="q6", text=
        "{t}O ritual. [p=0.3] {r1}Patamares: [p=0.2] um só. [p=0.3] {r2}Onde? [p=0.2] Na fusão. [p=0.3] {r3}Funde certinho: "
        "[p=0.2] *eutética.* [p=0.2] {ok}*Letra C.* [p=0.4] {xa}A e B, [p=0.2] puras, [p=0.2] teriam dois patamares. [p=0.3] "
        "{xd}A D teria o patamar na ebulição. [p=0.3] {xe}E a E, [p=0.2] mistura comum, [p=0.2] não teria nenhum."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="34", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dois patamares: puro. [p=0.2] Nenhum: mistura comum. [p=0.5] "
        "{b}Dois: [p=0.2] um patamar só: [p=0.2] eutética se for na fusão, [p=0.2] azeotrópica se for na ebulição. [p=0.5] "
        "{c}Três: [p=0.2] o gráfico não diz se é simples ou composta."),

    # ================= PONTE =================
    dict(id="35", block="ponte", text=
        "{t}Você viu todas as peças deste assunto. [p=0.4] {a}No último episódio, [p=0.2] vamos juntar tudo num roteiro de três perguntas "
        "[p=0.2] que classifica qualquer material, [p=0.3] {b}caçar as pegadinhas [p=0.3] {c}e treinar com questões novas."),
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia a mistura eutética? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
