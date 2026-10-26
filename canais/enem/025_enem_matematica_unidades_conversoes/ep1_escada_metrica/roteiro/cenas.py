# Roteiro — Unidades de Medida e Conversões, Episódio 1 de 5: A escada do sistema métrico, comprimento e massa
# Base: Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html — seções 02, 03 e 06 (sem "1 L de água pesa 1 kg",
#   que fica para o ep. 2) + Questão 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A ESCADA de 7 degraus: km, hm, dam, m, dm, cm, mm. Descer um degrau multiplica por 10; subir divide por 10.
#   Frase para decorar (K-H-D-M-D-C-M): "Kátia Hoje Dançou Muito, Dançou Com Marcos".
#   A conferência de sentido: unidade MENOR, número MAIOR (cabem mais centímetros do que metros na mesma distância).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos: nenhum bloco usa 3,5 t → kg (é a Questão 7). Exemplos do material: 2,5 km = 2 500 m; 1,8 m = 180 cm;
#   7,2 cm = 72 mm; 350 cm = 3,5 m. Exemplos NOSSOS: altura 1,75 m = 175 cm; comprimido de 500 mg = 0,5 g; 2 t = 2 000 kg;
#   boi de 20 arrobas = 300 kg; 2 m + 30 cm = 230 cm (erro 3).
# Nós fazemos (prompt): 3,2 km = 3 200 m · 45 cm = 0,45 m · 2,5 kg = 2 500 g · 750 mg = 0,75 g.
# QUESTÃO 7 do material (texto idêntico na tela): 3,5 t · 1 000 = 3 500 kg → C.
#   Material: B (350 kg) = peso de uma moto grande; D (35 000 kg) = 35 t, acima do limite legal de muitos veículos.
#   Explicações NOSSAS: B = usou 100 em vez de 1 000 (dois degraus); D = andou a vírgula quatro casas;
#   A (35 kg) = andou uma casa só (× 10); E (350 000 kg) = andou cinco casas (× 100 000).
# Atalhos (verde): "Kátia Hoje Dançou Muito, Dançou Com Marcos" · "conte os degraus: cada um é uma casa da vírgula" ·
#   "conferência de dois segundos: unidade menor, número maior" · "padronize antes de somar".
# Frases-chave (meio e fim, idênticas): 1. Cada degrau da escada vale 10. 2. Unidade menor, número maior.
#   3. Tonelada é mil quilos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Unidades de medida do zero: a escada do sistema métrico | Unidades de Medida Ep. 1"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Um erro de unidade *não avisa.* [p=0.4] {b}A conta fecha, [p=0.2] o número sai bonito [p=0.2] e está *errado.* "
        "[p=0.5] {c}E a alternativa errada está lá, [p=0.2] *esperando por você.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai converter qualquer *comprimento* ou *massa* contando degraus [p=0.3] "
        "{b}e conferir o resultado em *dois segundos.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Multiplicar por dez, cem ou mil [p=0.2] é andar a vírgula para a "
        "*direita:* [p=0.2] uma, duas ou três casas. [p=0.2] Dividir é andar para a *esquerda.* [p=0.4] {b}E, da série de "
        "Notação científica: [p=0.2] *quilo* quer dizer *mil,* [p=0.2] dez elevado a três. [p=0.2] Quilômetro é mil metros. "
        "[p=0.2] Quilograma, mil gramas."),

    # ================= CONCRETO =================
    dict(id="04", block="cotidiano", text=
        "{t}Repare quantas unidades você usa sem perceber. [p=0.3] {a}A sua altura: [p=0.2] *um vírgula setenta e cinco* "
        "metro, [p=0.2] ou *cento e setenta e cinco* centímetros. [p=0.4] {b}O caminho até o trabalho, [p=0.2] em "
        "*quilômetros.* [p=0.4] {c}O remédio, [p=0.2] em *miligramas.* [p=0.4] {d}A carga de um caminhão, [p=0.2] em "
        "*toneladas.* [p=0.4] {e}Mesma medida, [p=0.2] números diferentes. [p=0.2] E é na troca de um para o outro [p=0.2] "
        "que mora o erro."),

    # ================= BLOCO A: UNIDADES-BASE =================
    dict(id="05", block="base", text=
        "{t}Por onde começa? [p=0.3] {a}Pelas *unidades-base:* [p=0.2] as unidades de referência, [p=0.2] de onde as outras "
        "saem. [p=0.4] {b}O *metro,* [p=0.2] para comprimento. [p=0.2] O *grama,* [p=0.2] para massa, [p=0.2] que é o que a "
        "balança mede. [p=0.2] E o *litro,* [p=0.2] para capacidade. [p=0.4] {c}As três usam os mesmos *prefixos:* [p=0.2] o "
        "pedacinho que vem antes do nome [p=0.2] e diz quantas vezes maior ou menor. [p=0.3] {d}Quilômetro, quilograma: "
        "[p=0.2] o *quilo* é sempre mil. [p=0.3] Milímetro, miligrama, mililitro: [p=0.2] o *mili* é sempre a milésima parte."),

    # ================= BLOCO B: A ESCADA =================
    dict(id="06", block="escada", text=
        "{t}Agora, a ferramenta da aula: [p=0.2] uma *escada* de sete degraus. [p=0.4] {a}No meio, o *metro.* [p=0.4] "
        "{b}Subindo, [p=0.2] os *múltiplos,* [p=0.2] as unidades maiores: [p=0.2] decâmetro, [p=0.2] dez metros; [p=0.2] "
        "hectômetro, [p=0.2] cem metros; [p=0.2] quilômetro, [p=0.2] mil metros. [p=0.4] {c}Descendo, [p=0.2] os "
        "*submúltiplos,* [p=0.2] as unidades menores: [p=0.2] decímetro, [p=0.2] a décima parte do metro; [p=0.2] "
        "centímetro, [p=0.2] a centésima; [p=0.2] milímetro, [p=0.2] a milésima. [p=0.4] {d}E a regra: [p=0.2] *descer um "
        "degrau multiplica por dez.* [p=0.3] *Subir divide por dez.*"),
    dict(id="07", block="escada", text=
        "{t}E como lembrar a ordem? [p=0.3] {a}Atalho: [p=0.2] uma frase boba, [p=0.2] que gruda. [p=0.3] {b}*Kátia Hoje "
        "Dançou Muito, [p=0.2] Dançou Com Marcos.* [p=0.4] {c}K de quilômetro, [p=0.2] H de hectômetro, [p=0.2] D de "
        "decâmetro, [p=0.2] M de metro, [p=0.2] D de decímetro, [p=0.2] C de centímetro, [p=0.2] M de milímetro. [p=0.4] "
        "{d}Sete palavras, [p=0.2] sete degraus, [p=0.2] do maior para o menor."),

    # ================= CONTANDO DEGRAUS =================
    dict(id="08", block="contar", text=
        "{t}Vamos usar. [p=0.3] Quantos metros há em *dois vírgula cinco* quilômetros? [p=0.4] {a}Ache os dois degraus: "
        "[p=0.2] quilômetro lá em cima, [p=0.2] metro no meio. [p=0.4] {b}Conte, descendo: [p=0.2] um, [p=0.2] dois, "
        "[p=0.2] *três degraus.* [p=0.3] Cada um vale vezes dez: [p=0.2] vezes mil. [p=0.4] {c}A vírgula anda três casas "
        "para a direita: [p=0.2] *dois mil e quinhentos metros.*"),
    dict(id="09", block="contar", text=
        "{t}E o caminho de volta? [p=0.3] Trezentos e cinquenta centímetros [p=0.2] são quantos metros? [p=0.4] {a}Do "
        "centímetro ao metro, [p=0.2] você *sobe:* [p=0.2] um, [p=0.2] *dois degraus.* [p=0.3] Subir divide: [p=0.2] por "
        "cem. [p=0.4] {b}A vírgula anda duas casas para a esquerda: [p=0.2] *três vírgula cinco metros.* [p=0.4] {c}Atalho: "
        "[p=0.2] *cada degrau é uma casa da vírgula.*"),

    # ================= BLOCO C: A CONFERÊNCIA DE SENTIDO =================
    dict(id="10", block="sentido", text=
        "{t}E como saber se você andou para o lado certo? [p=0.4] {a}Pense numa mesma distância. [p=0.2] Cabem *mais* "
        "centímetros do que metros nela, [p=0.2] porque o centímetro é pequenininho. [p=0.4] {b}Então: [p=0.2] *unidade "
        "menor, número maior.* [p=0.3] Unidade maior, número menor. [p=0.4] {c}Atalho: [p=0.2] essa é a *conferência de dois "
        "segundos.* [p=0.2] Foi para o metro, [p=0.2] que é menor que o quilômetro? [p=0.2] O número *tem* que crescer. "
        "[p=0.2] Dois e meio virou dois mil e quinhentos: [p=0.2] cresceu. [p=0.2] Fecha."),

    # ================= BLOCO D: PREFIXOS ALÉM DA ESCADA =================
    dict(id="11", block="prefixos", text=
        "{t}E existem degraus fora da escada? [p=0.3] Existem. [p=0.3] {a}Para cima, [p=0.2] *mega,* [p=0.2] um milhão, "
        "[p=0.2] e *giga,* [p=0.2] um bilhão: [p=0.2] o megawatt da usina, [p=0.2] o gigabyte do celular. [p=0.4] {b}Para "
        "baixo, [p=0.2] *micro,* [p=0.2] a milionésima parte, [p=0.2] e *nano,* [p=0.2] a bilionésima: [p=0.2] o tamanho de "
        "um vírus. [p=0.4] {c}Esses você já viu na série de Notação científica. [p=0.2] Hoje, a gente fica nos sete degraus."),

    # ================= BLOCO E: COMPRIMENTO =================
    dict(id="12", block="comprimento", text=
        "{t}Agora, as conversões de comprimento que mais aparecem. [p=0.4] {a}Quilômetro para metro: [p=0.2] três degraus, "
        "[p=0.2] *vezes mil.* [p=0.4] {b}Metro para centímetro: [p=0.2] dois degraus, [p=0.2] *vezes cem.* [p=0.2] Um vírgula "
        "oito metro [p=0.2] são cento e oitenta centímetros. [p=0.4] {c}Metro para milímetro: [p=0.2] três degraus, [p=0.2] "
        "*vezes mil.* [p=0.4] {d}Centímetro para milímetro: [p=0.2] um degrau, [p=0.2] *vezes dez.* [p=0.2] Sete vírgula dois "
        "centímetros [p=0.2] são setenta e dois milímetros. [p=0.4] {e}E centímetro para metro? [p=0.2] Sobe dois: [p=0.2] "
        "*dividido por cem.*"),
    dict(id="13", block="comprimento", text=
        "{t}Quer ver isso com os olhos? [p=0.3] {a}Esta é uma régua de *um metro.* [p=0.4] {b}Ela tem *cem* risquinhos de "
        "centímetro. [p=0.4] {c}E, dentro de cada centímetro, [p=0.2] *dez* de milímetro. [p=0.2] Dez vezes cem: [p=0.2] "
        "*mil milímetros.* [p=0.4] {d}Por isso, [p=0.2] metro para milímetro é vezes mil."),

    # ================= BLOCO F: MASSA =================
    dict(id="14", block="massa", text=
        "{t}E a massa? [p=0.3] A boa notícia: [p=0.2] a escada é a *mesma.* [p=0.4] {a}No meio, o *grama.* [p=0.2] Subindo, "
        "[p=0.2] decagrama, hectograma, [p=0.2] *quilograma.* [p=0.2] Descendo, [p=0.2] decigrama, centigrama, [p=0.2] "
        "*miligrama.* [p=0.4] {b}Quilograma é *mil gramas:* [p=0.2] três degraus. [p=0.4] {c}E o miligrama, [p=0.2] a "
        "milésima parte do grama, [p=0.2] é a unidade do remédio. [p=0.2] Um comprimido de quinhentos miligramas [p=0.2] "
        "tem *meio grama.*"),
    dict(id="15", block="massa", text=
        "{t}E as massas grandes? [p=0.3] {a}A *tonelada* vale *mil quilos.* [p=0.2] Um jeito de lembrar: [p=0.2] é um *quilo "
        "de quilos.* [p=0.3] Duas toneladas [p=0.2] são dois mil quilogramas. [p=0.4] {b}E no campo [p=0.2] aparece a "
        "*arroba:* [p=0.2] uma unidade antiga, [p=0.2] usada até hoje na cotação do gado. [p=0.2] Uma arroba vale *quinze "
        "quilos.* [p=0.4] {c}Um boi de vinte arrobas: [p=0.2] vinte vezes quinze, [p=0.2] *trezentos quilos.*"),

    # ================= NÓS FAZEMOS (JOGO) =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez, [p=0.2] em ritmo de jogo. [p=0.3] Quatro conversões. [p=0.3] {a}Três vírgula dois quilômetros em metros. "
        "[p=0.3] {b}Quarenta e cinco centímetros em metros. [p=0.3] {c}Dois vírgula cinco quilos em gramas. [p=0.3] "
        "{d}Setecentos e cinquenta miligramas em gramas. [p=0.4] {e}*Pause o vídeo e converta.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir, [p=0.2] contando degraus. [p=0.3] {a}Quilômetro para metro: [p=0.2] desce três, [p=0.2] vezes "
        "mil: [p=0.2] *três mil e duzentos metros.* [p=0.4] {b}Centímetro para metro: [p=0.2] sobe dois, [p=0.2] dividido "
        "por cem: [p=0.2] *zero vírgula quarenta e cinco metro.* [p=0.4] {c}Quilo para grama: [p=0.2] desce três: [p=0.2] "
        "*dois mil e quinhentos gramas.* [p=0.4] {d}Miligrama para grama: [p=0.2] sobe três, [p=0.2] dividido por mil: "
        "[p=0.2] *zero vírgula setenta e cinco grama.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] cada degrau da escada vale dez. [p=0.5] {b}Dois: [p=0.2] "
        "unidade menor, número maior. [p=0.5] {c}Três: [p=0.2] tonelada é mil quilos."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] andar a vírgula para o *lado errado.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque você contou os degraus direitinho: [p=0.2] só errou a direção. [p=0.4] {c}A "
        "conferência de dois segundos pega: [p=0.2] foi para uma unidade menor? [p=0.2] O número tem que *crescer.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] achar que uma tonelada [p=0.2] é *cem* quilos. [p=0.4] {b}Parece certo, [p=0.2] porque cem é "
        "um número redondo, [p=0.2] que soa como uma medida grande. [p=0.4] {c}Mas tonelada é *mil* quilos: [p=0.2] um "
        "quilo de quilos."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *somar* medidas em unidades diferentes [p=0.2] sem padronizar. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a conta fecha: [p=0.2] dois metros mais trinta centímetros, [p=0.2] trinta e dois. [p=0.4] {c}Mas "
        "trinta e dois *o quê?* [p=0.2] Passe tudo para a mesma unidade antes: [p=0.2] dois metros são duzentos "
        "centímetros, [p=0.2] mais trinta, [p=0.2] *duzentos e trinta centímetros.*"),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="22", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um caminhão transporta "
        "uma carga de *três vírgula cinco toneladas* de grãos. [p=0.4] {b}Essa carga, [p=0.2] expressa em quilogramas, "
        "[p=0.2] corresponde a: [p=0.4] {qa}A: [p=0.2] trinta e cinco quilos. [p=0.3] {qb}B: [p=0.2] trezentos e cinquenta. "
        "[p=0.3] {qc}C: [p=0.2] três mil e quinhentos. [p=0.3] {qd}D: [p=0.2] trinta e cinco mil. [p=0.3] {qe}E: [p=0.2] "
        "trezentos e cinquenta mil. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q7", text=
        "{t}Vamos resolver. [p=0.3] {a}Tonelada para quilograma: [p=0.2] uma tonelada é mil quilos. [p=0.3] {b}Então, "
        "[p=0.2] três vírgula cinco vezes mil: [p=0.2] a vírgula anda três casas, [p=0.2] *três mil e quinhentos quilos.* "
        "[p=0.4] {c}Confira o sentido: [p=0.2] o quilo é menor que a tonelada, [p=0.2] e o número cresceu. [p=0.3] {d}E a "
        "plausibilidade: [p=0.2] um caminhão médio leva alguns milhares de quilos. [p=0.2] Faz sentido. [p=0.3] "
        "{ok}*Letra C!*"),
    dict(id="24", block="q7", text=
        "{t}E as outras? [p=0.3] {xb}A B, [p=0.2] trezentos e cinquenta quilos, [p=0.2] usou cem em vez de mil: [p=0.2] é o "
        "peso de uma moto grande, [p=0.2] não a carga de um caminhão. [p=0.4] {xd}A D, [p=0.2] trinta e cinco mil quilos, "
        "[p=0.2] andou a vírgula casas demais: [p=0.2] seriam trinta e cinco toneladas, [p=0.2] acima do limite de muitos "
        "veículos. [p=0.4] {xa}A A [p=0.2] {xe}e a E [p=0.2] erram ainda mais: [p=0.2] uma casa só, [p=0.2] ou cinco casas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] cada degrau da escada vale dez. [p=0.5] {b}Dois: "
        "[p=0.2] unidade menor, número maior. [p=0.5] {c}Três: [p=0.2] tonelada é mil quilos."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}E em *área* e *volume?* [p=0.3] {b}A escada continua a mesma, [p=0.2] mas cada degrau passa a valer *cem* "
        "[p=0.2] e *mil.* [p=0.4] {c}Esse é o erro mais caro deste assunto. [p=0.4] {d}Próximo episódio."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia a frase da Kátia? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
