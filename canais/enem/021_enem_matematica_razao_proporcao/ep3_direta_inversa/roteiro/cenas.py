# Roteiro — Razão, Proporção e Regra de Três, Episódio 3 de 6: Direta ou inversa? A decisão que vale a questão (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html — seções 06 e 07 (+ Questões 4 e 5 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o TESTE DO DOBRO — dobre uma grandeza e pergunte o que acontece com a outra.
#   Dobrou também? Direta. Virou metade? Inversa. (retomado em todo problema)
# Cotidiano: o dobro de pão custa o dobro (direta) · o dobro de amigos na mesma pizza de 8 fatias ganha metade cada (inversa).
# Procedimento (5 passos, visível nas resoluções): 1 padronizar unidades (passo zero) · 2 duas colunas · 3 direta ou inversa
#   · 4 se inversa, inverter uma coluna · 5 multiplicar em cruz.
# Exemplos do procedimento: NOSSOS, para não entregar a Questão 5 ("você faz"). O material usa os números das próprias
#   Questões 4 e 5 (impressora 240/8/20; 15 operários em 24 dias). Aqui: tecido 6 m = R$ 48 → 15 m = R$ 120 (direta);
#   6 jardineiros em 10 dias → 4 jardineiros em 15 dias (inversa; atalho do produto 6·10 = 60 = 4·x).
#   Erro silencioso: 40 garrafas em 1 hora → 30 minutos: 1 200 (errado, sem converter) × 20 (certo, 1 h = 60 min).
# TREINO "dobrou ou virou metade?" (sem contas, 5 s de pausa cada; 3 diretas e 3 inversas, fora de ordem):
#   1 tinta e área pintada → DIRETA · 2 velocidade e tempo da mesma viagem → INVERSA · 3 torneiras iguais e tempo para
#   encher o mesmo tanque → INVERSA · 4 horas trabalhadas e salário total de quem ganha por hora → DIRETA · 5 pessoas dividindo um prêmio em
#   partes iguais e quanto cada uma recebe → INVERSA · 6 distância e litros de combustível, no mesmo ritmo → DIRETA.
# QUESTÃO 4 do material (eu faço; texto idêntico na tela): 240/8 = x/20 → 8x = 4 800 → x = 600 → C. Valor unitário: 30 pág/min.
#   Explicações NOSSAS (o material não explica as erradas): E (4 800) parou no 8x = 4 800 sem dividir por 8;
#   A (96 = 240·8/20) montou como inversa; B (480) e D (720) são o dobro e o triplo de 240, mas 20 min = 2,5 × 8 min.
# QUESTÃO 5 do material (você faz; texto idêntico na tela): 15 · 24 = 360 = 20 · x → x = 18 → B.
#   E (32): aplicou direta (explicação do material). Explicações NOSSAS: D (24) achou que nada muda; A (15) e C (20)
#   copiaram números de operários do enunciado.
# Frases-chave (meio e fim, idênticas, do usuário):
#   1. Dobrou também? Direta. Virou metade? Inversa.
#   2. Na direta, o quociente é constante; na inversa, o produto.
#   3. Unidades iguais antes de tudo.
# Atalhos (verde): o teste do dobro em voz alta, com a frase inteira · inversa pelo produto constante (6·10 = 4·x) ·
#   valor unitário (30 páginas por minuto) · conferência de bom senso (mais gente, menos dias).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Regra de três: direta ou inversa? O teste do dobro | Razão e Proporção Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. No treino, depois de cada "
            "pergunta, faça silêncio de verdade e responda com energia de jogo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quem erra regra de três [p=0.2] quase nunca erra a *multiplicação.* [p=0.5] {b}Erra a *decisão* de direta ou "
        "inversa, [p=0.3] {c}e resolve com perfeição [p=0.2] o *problema trocado.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai decidir *em segundos* [p=0.2] se a relação é direta ou inversa, [p=0.4] "
        "{b}e resolver *qualquer* regra de três simples. [p=0.4] {c}E o segredo cabe numa pergunta só: [p=0.2] *o que "
        "acontece no dobro?*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio anterior. [p=0.3] {a}Numa proporção, [p=0.2] como dois terços igual a "
        "quatro sextos, [p=0.3] {b}pontas vezes pontas [p=0.2] é igual a miolo vezes miolo. [p=0.4] {c}Dois vezes seis, "
        "[p=0.2] doze. [p=0.2] Três vezes quatro, [p=0.2] doze. [p=0.4] {d}Multiplicar assim, em xis, [p=0.2] se chama "
        "*produto cruzado.*"),

    # ================= O COTIDIANO =================
    dict(id="04", block="cotidiano", text=
        "{t}Duas cenas do dia a dia. [p=0.3] {a}Na padaria, [p=0.2] você compra *o dobro* de pão. [p=0.3] O que acontece com "
        "o preço? [p=0.4] {b}Dobra também. [p=0.5] {c}Agora, uma pizza de oito fatias. [p=0.2] Dois amigos dividindo: "
        "[p=0.2] quatro fatias para cada um. [p=0.4] {d}Chega *o dobro* de amigos: [p=0.2] quatro pessoas. [p=0.3] {e}Cada "
        "um ganha *metade:* [p=0.2] duas fatias."),
    dict(id="05", block="cotidiano", text=
        "{t}Pão, [p=0.1] preço, [p=0.1] amigos, [p=0.1] fatias. [p=0.3] {a}Cada uma é uma *grandeza:* [p=0.2] tudo o que "
        "dá para *medir* ou *contar.* [p=0.4] {b}E duas grandezas podem mudar juntas de dois jeitos. [p=0.3] {c}O jeito do "
        "pão, [p=0.3] {d}e o jeito da pizza."),

    # ================= BLOCO A: DIRETA =================
    dict(id="06", block="tipos", text=
        "{t}Primeiro, o tipo do pão. [p=0.3] {a}Um quilo de feijão custa oito reais. [p=0.3] {b}Dois quilos, [p=0.2] "
        "dezesseis. [p=0.3] {c}Três quilos, [p=0.2] vinte e quatro. [p=0.4] {d}Uma aumenta, [p=0.2] a outra aumenta *na "
        "mesma proporção.* [p=0.2] São grandezas *diretamente proporcionais.* [p=0.4] {e}E repare: [p=0.2] divida o preço "
        "pelos quilos. [p=0.2] Dezesseis dividido por dois, [p=0.2] oito. [p=0.2] Vinte e quatro dividido por três, [p=0.2] "
        "oito. [p=0.4] {f}O resultado da divisão, [p=0.2] o *quociente,* [p=0.2] é sempre o mesmo. [p=0.3] Ele é "
        "*constante:* [p=0.2] um valor que não muda."),

    # ================= BLOCO B: INVERSA =================
    dict(id="07", block="tipos", text=
        "{t}Agora, o tipo da pizza. [p=0.3] {a}Oito fatias. [p=0.2] Duas pessoas, [p=0.2] quatro fatias cada. [p=0.3] "
        "{b}Quatro pessoas, [p=0.2] duas cada. [p=0.3] {c}Oito pessoas, [p=0.2] uma cada. [p=0.4] {d}Uma aumenta, [p=0.2] "
        "a outra *diminui* na mesma proporção. [p=0.2] São grandezas *inversamente proporcionais.* [p=0.4] {e}E aqui o que "
        "não muda é a *multiplicação.* [p=0.2] Dois vezes quatro, [p=0.2] oito. [p=0.2] Quatro vezes dois, [p=0.2] oito. "
        "[p=0.2] Oito vezes um, [p=0.2] oito. [p=0.4] {f}O resultado da multiplicação, [p=0.2] o *produto,* [p=0.2] é "
        "constante: [p=0.2] a pizza inteira."),

    # ================= BLOCO C: O TESTE DO DOBRO =================
    dict(id="08", block="teste", text=
        "{t}Mas na prova, [p=0.2] como decidir rápido qual é qual? [p=0.4] {a}Com o *teste do dobro.* [p=0.3] {b}Dobre uma "
        "grandeza [p=0.2] e pergunte o que acontece com a outra. [p=0.4] {c}Dobrou também? [p=0.2] *Direta.* [p=0.3] "
        "{d}Virou metade? [p=0.2] *Inversa.*"),
    dict(id="09", block="teste", text=
        "{t}Vamos testar. [p=0.3] {a}Operários e dias de uma obra. [p=0.2] Dobre os operários. [p=0.3] {b}A obra fica pronta "
        "em *metade* dos dias. [p=0.3] {c}Virou metade: [p=0.2] *inversa.* [p=0.5] {d}Quilos comprados e preço. [p=0.2] "
        "Dobre os quilos. [p=0.3] {e}O preço *dobra.* [p=0.3] {f}Dobrou também: [p=0.2] *direta.* [p=0.4] {g}Atalho: "
        "[p=0.2] faça o teste *em voz alta,* [p=0.2] com a frase inteira: [p=0.2] se eu dobrar isso, [p=0.2] aquilo dobra "
        "ou vira metade?"),

    # ================= BLOCO D: CRESCER JUNTO NÃO BASTA =================
    dict(id="10", block="junto", text=
        "{t}Uma pegadinha: [p=0.2] crescer junto é ser proporcional? [p=0.4] {a}Pense numa criança. [p=0.2] Aos cinco "
        "anos, [p=0.2] ela mede mais ou menos um metro e dez. [p=0.4] {b}Aos dez anos, [p=0.2] o dobro da idade, [p=0.2] ela "
        "mede dois metros e vinte? [p=0.4] {c}Claro que não! [p=0.2] Mais ou menos um metro e quarenta. [p=0.4] {d}Idade e "
        "altura *crescem juntas,* [p=0.2] mas não são proporcionais. [p=0.3] {e}Proporcional exige que dobrar uma [p=0.2] "
        "dobre *exatamente* a outra."),

    # ================= BLOCO E: O PROCEDIMENTO =================
    dict(id="11", block="procedimento", text=
        "{t}Decidido o tipo, [p=0.2] vem a conta. [p=0.3] {a}A *regra de três* é o jeito de achar um valor desconhecido "
        "[p=0.2] quando você conhece outros *três.* [p=0.4] {b}O valor desconhecido se chama *incógnita,* [p=0.2] e a gente "
        "escreve como *xis.* [p=0.4] {c}O procedimento tem cinco passos. [p=0.3] {d}Um: [p=0.2] padronizar as unidades, "
        "[p=0.2] que é deixar tudo na mesma unidade: [p=0.2] horas com horas, [p=0.2] metros com metros. [p=0.2] É o *passo "
        "zero,* [p=0.2] antes de qualquer coisa. [p=0.3] {e}Dois: [p=0.2] montar duas colunas, [p=0.2] uma para cada "
        "grandeza. [p=0.3] {f}Três: [p=0.2] decidir se é direta ou inversa, [p=0.2] pelo teste do dobro. [p=0.3] {g}Quatro: "
        "[p=0.2] se for inversa, [p=0.2] inverter uma das colunas. [p=0.3] {h}Cinco: [p=0.2] multiplicar *em cruz.*"),
    dict(id="12", block="procedimento", text=
        "{t}Um exemplo direto. [p=0.3] {a}Seis metros de tecido custam quarenta e oito reais. [p=0.2] Quanto custam quinze "
        "metros? [p=0.4] {b}Passo um: [p=0.2] metros com metros, [p=0.2] reais com reais. [p=0.2] Tudo certo. [p=0.3] "
        "{c}Passo dois: [p=0.2] coluna dos metros, [p=0.2] seis e quinze. [p=0.2] Coluna dos reais, [p=0.2] quarenta e oito "
        "e xis. [p=0.4] {d}Passo três: [p=0.2] o dobro de tecido, [p=0.2] o dobro do preço. [p=0.2] *Direta.* [p=0.3] "
        "{e}Passo quatro: [p=0.2] direta não inverte nada. [p=0.3] {f}Passo cinco: [p=0.2] multiplicar em cruz [p=0.2] é "
        "usar as pontas e o miolo. [p=0.2] Seis vezes xis [p=0.2] igual a quarenta e oito vezes quinze, [p=0.2] setecentos "
        "e vinte. [p=0.4] {g}Xis é setecentos e vinte dividido por seis: [p=0.2] *cento e vinte reais.*"),
    dict(id="13", block="procedimento", text=
        "{t}Agora, um inverso. [p=0.3] {a}Seis jardineiros cuidam de um parque em dez dias. [p=0.2] Em quantos dias *quatro* "
        "jardineiros fazem o mesmo trabalho? [p=0.4] {b}Teste do dobro: [p=0.2] dobrando os jardineiros, [p=0.2] os dias "
        "viram metade. [p=0.2] *Inversa.* [p=0.4] {c}Passo quatro: [p=0.2] inverta uma coluna. [p=0.2] Seis sobre quatro "
        "[p=0.2] vira *quatro sobre seis.* [p=0.4] {d}Agora a cruz: [p=0.2] quatro vezes xis [p=0.2] igual a seis vezes dez, "
        "[p=0.2] sessenta. [p=0.3] {e}Xis é sessenta dividido por quatro: [p=0.2] *quinze dias.* [p=0.4] {f}Faz sentido? "
        "[p=0.2] Menos jardineiros, [p=0.2] mais dias. [p=0.2] *Faz.*"),
    dict(id="14", block="procedimento", text=
        "{t}Atalho da inversa: [p=0.2] lembra da pizza? [p=0.2] {a}O *produto* não muda. [p=0.4] {b}Seis jardineiros vezes dez "
        "dias: [p=0.2] sessenta. [p=0.3] {c}Quatro vezes xis [p=0.2] também dá sessenta. [p=0.4] {d}Xis igual a quinze. [p=0.2] Sem inverter coluna nenhuma."),

    # ================= BLOCO F: O ERRO SILENCIOSO =================
    dict(id="15", block="unidades", text=
        "{t}E por que padronizar é o passo zero? [p=0.3] {a}Uma máquina enche quarenta garrafas em *uma hora.* [p=0.2] "
        "Quantas em *trinta minutos?* [p=0.4] {b}Quem monta direto, [p=0.2] quarenta está para um, [p=0.2] assim como xis "
        "está para trinta, [p=0.3] {c}encontra *mil e duzentas* garrafas. [p=0.4] {d}A conta fecha certinho, [p=0.2] e "
        "nenhum alarme toca. [p=0.3] Esse é o *erro silencioso.* [p=0.4] {e}Agora, padronizando: [p=0.2] uma hora são "
        "sessenta minutos. [p=0.2] Quarenta está para sessenta, [p=0.2] assim como xis está para trinta. [p=0.3] {f}Xis "
        "igual a *vinte.* [p=0.2] Metade do tempo, [p=0.2] metade das garrafas."),

    # ================= TREINO: DOBROU OU VIROU METADE? =================
    dict(id="16", block="treino", text=
        "{t}Agora, um treino rápido: [p=0.2] *dobrou ou virou metade?* [p=0.4] {a}Seis situações, [p=0.2] sem conta: [p=0.2] "
        "só a decisão. [p=0.3] {b}Você tem cinco segundos para cada uma. [p=0.2] *Direta ou inversa?*"),
    dict(id="17", block="treino", text=
        "{q}Um: [p=0.2] litros de tinta e área pintada, [p=0.2] com a mesma tinta. [p=0.3] {p}Direta ou inversa? [p=5.0] "
        "{r}*Direta.* [p=0.2] {w}Com o dobro de tinta, [p=0.2] você pinta o dobro da parede."),
    dict(id="18", block="treino", text=
        "{q}Dois: [p=0.2] a velocidade do carro e o tempo da mesma viagem. [p=0.3] {p}Direta ou inversa? [p=5.0] "
        "{r}*Inversa.* [p=0.2] {w}No dobro da velocidade, [p=0.2] a viagem leva metade do tempo."),
    dict(id="19", block="treino", text=
        "{q}Três: [p=0.2] torneiras iguais abertas, [p=0.2] e o tempo para encher o mesmo tanque. [p=0.3] {p}Direta ou "
        "inversa? [p=5.0] {r}*Inversa.* [p=0.2] {w}O dobro de torneiras [p=0.2] enche na metade do tempo."),
    dict(id="20", block="treino", text=
        "{q}Quatro: [p=0.2] horas trabalhadas, [p=0.2] e o salário de quem ganha por hora. [p=0.3] {p}Direta ou inversa? "
        "[p=5.0] {r}*Direta.* [p=0.2] {w}O dobro de horas, [p=0.2] o dobro do salário."),
    dict(id="21", block="treino", text=
        "{q}Cinco: [p=0.2] pessoas dividindo um prêmio em partes iguais, [p=0.2] e quanto cada uma recebe. [p=0.3] "
        "{p}Direta ou inversa? [p=5.0] {r}*Inversa.* [p=0.2] {w}O dobro de pessoas, [p=0.2] metade para cada uma."),
    dict(id="22", block="treino", text=
        "{q}Seis: [p=0.2] a distância percorrida, [p=0.2] e os litros de combustível gastos, [p=0.2] no mesmo ritmo. "
        "[p=0.3] {p}Direta ou inversa? [p=5.0] {r}*Direta.* [p=0.2] {w}O dobro de quilômetros, [p=0.2] o dobro de litros. "
        "[p=0.4] {f}Quantas você acertou?"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="23", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] dobrou também? [p=0.2] Direta. [p=0.2] Virou metade? "
        "[p=0.2] Inversa. [p=0.5] {b}Dois: [p=0.2] na direta, [p=0.2] o quociente é constante; [p=0.2] na inversa, [p=0.2] "
        "o produto. [p=0.5] {c}Três: [p=0.2] unidades iguais antes de tudo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="24", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] aplicar direta onde é inversa. [p=0.2] Mais "
        "operários, [p=0.2] *mais* dias. [p=0.4] {b}Parece certo, [p=0.2] porque a gente se acostuma a montar tudo do mesmo "
        "jeito. [p=0.4] {c}Mas faça o teste do dobro: [p=0.2] o dobro de operários termina em *metade* dos dias."),
    dict(id="25", block="erros", text=
        "{a}Segundo: [p=0.2] achar que *crescer junto* é ser proporcional. [p=0.4] {b}Parece certo, [p=0.2] porque as duas "
        "grandezas sobem ao mesmo tempo. [p=0.4] {c}Mas proporcional é dobrar *exatamente.* [p=0.2] Idade e altura sobem "
        "juntas, [p=0.2] e ninguém dobra de altura ao dobrar de idade."),
    dict(id="26", block="erros", text=
        "{a}Terceiro: [p=0.2] montar a regra de três com *unidades misturadas,* [p=0.2] horas de um lado e minutos do "
        "outro. [p=0.4] {b}Parece certo, [p=0.2] porque a conta fecha sem nenhum erro. [p=0.4] {c}Mas o resultado sai "
        "errado, [p=0.2] em silêncio. [p=0.2] Converta primeiro, [p=0.2] monte depois."),

    # ================= QUESTÃO 4 DO MATERIAL (EU FAÇO) =================
    dict(id="27", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Essa, [p=0.2] eu faço com "
        "você. [p=0.4] {a}Uma impressora industrial produz duzentas e quarenta páginas em oito minutos, [p=0.2] mantendo "
        "ritmo constante. [p=0.3] Nessas condições, [p=0.2] em vinte minutos ela produzirá: [p=0.4] {qa}A: [p=0.2] noventa "
        "e seis páginas. [p=0.3] {qb}B: [p=0.2] quatrocentas e oitenta. [p=0.3] {qc}C: [p=0.2] seiscentas. [p=0.3] {qd}D: "
        "[p=0.2] setecentas e vinte. [p=0.3] {qe}E: [p=0.2] quatro mil e oitocentas."),
    dict(id="28", block="q4", text=
        "{t}Passo um: [p=0.2] minutos com minutos. [p=0.2] Tudo certo. [p=0.3] {a}Passo dois: [p=0.2] coluna das páginas, "
        "[p=0.2] duzentas e quarenta e xis. [p=0.2] Coluna dos minutos, [p=0.2] oito e vinte. [p=0.4] {b}Passo três: "
        "[p=0.2] o dobro de tempo [p=0.2] dá o dobro de páginas. [p=0.2] *Direta.* [p=0.3] {c}Passo quatro: [p=0.2] direta, "
        "[p=0.2] nada a inverter. [p=0.3] {d}Passo cinco, [p=0.2] a cruz: [p=0.2] oito vezes xis [p=0.2] igual a duzentos e "
        "quarenta vezes vinte, [p=0.2] quatro mil e oitocentos. [p=0.4] {e}Xis é quatro mil e oitocentos dividido por oito: "
        "[p=0.2] *seiscentas páginas.* [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q4", text=
        "{t}Atalho: [p=0.2] o *valor unitário,* [p=0.2] que é quanto sai em *uma* unidade. [p=0.4] {a}Duzentas e quarenta "
        "páginas em oito minutos: [p=0.2] trinta por minuto. [p=0.3] {b}Em vinte "
        "minutos, [p=0.2] trinta vezes vinte, [p=0.2] *seiscentas.* [p=0.4] {xe}E as outras? [p=0.2] A E é de quem parou no "
        "quatro mil e oitocentos [p=0.2] e esqueceu de dividir por oito. [p=0.4] {xa}A A montou ao contrário, [p=0.2] como se "
        "fosse inversa: [p=0.2] mais tempo, [p=0.2] *menos* páginas? [p=0.3] Não faz sentido. [p=0.4] {xb}E a B [p=0.2] {xd}e "
        "a D são *chutes* de dobro e de triplo. [p=0.3] {f}Mas vinte minutos são duas vezes e meia oito minutos: [p=0.2] nem "
        "o dobro, [p=0.2] nem o triplo."),

    # ================= QUESTÃO 5 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="30", block="q5", text=
        "{t}Agora é a sua vez. [p=0.3] {a}Uma obra seria concluída por quinze operários em vinte e quatro dias. [p=0.3] Se a "
        "construtora alocar vinte operários com o mesmo ritmo de trabalho, [p=0.2] a obra será concluída em: [p=0.4] "
        "{qa}A: [p=0.2] quinze dias. [p=0.3] {qb}B: [p=0.2] dezoito dias. [p=0.3] {qc}C: [p=0.2] vinte dias. [p=0.3] {qd}D: "
        "[p=0.2] vinte e quatro dias. [p=0.3] {qe}E: [p=0.2] trinta e dois dias. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="31", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}Teste do dobro: [p=0.2] o dobro de operários [p=0.2] termina em metade dos dias. "
        "[p=0.2] *Inversa.* [p=0.4] {b}Na inversa, [p=0.2] o produto é constante. [p=0.2] Quinze vezes vinte e quatro: "
        "[p=0.2] trezentos e sessenta. [p=0.4] {c}Vinte vezes xis [p=0.2] também dá trezentos e sessenta. [p=0.3] {d}Xis é "
        "trezentos e sessenta dividido por vinte: [p=0.2] *dezoito dias.* [p=0.3] {ok}*Letra B!* [p=0.4] {e}Confira: "
        "[p=0.2] mais operários, [p=0.2] menos dias. [p=0.2] Dezoito é menos que vinte e quatro. [p=0.2] *Faz sentido.*"),
    dict(id="32", block="q5", text=
        "{t}E as outras? [p=0.3] {xe}A E é a armadilha da aula: [p=0.2] trinta e dois dias [p=0.2] é de quem montou como "
        "*direta.* [p=0.3] Mais operários e *mais* dias? [p=0.2] O bom senso elimina. [p=0.4] {xd}A D acha que nada muda, "
        "[p=0.3] {xa}e a A [p=0.2] {xc}e a C [p=0.2] só copiaram números do enunciado: [p=0.2] quinze e vinte são os "
        "operários, [p=0.2] não os dias."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] dobrou também? [p=0.2] Direta. [p=0.2] Virou "
        "metade? [p=0.2] Inversa. [p=0.5] {b}Dois: [p=0.2] na direta, [p=0.2] o quociente é constante; [p=0.2] na inversa, "
        "[p=0.2] o produto. [p=0.5] {c}Três: [p=0.2] unidades iguais antes de tudo."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}E quando há *três* grandezas, [p=0.2] como operários, [p=0.2] horas por dia [p=0.2] e dias? [p=0.4] {b}Parece "
        "difícil, [p=0.2] mas é a simples *repetida,* [p=0.3] {c}e tem um atalho. [p=0.3] {d}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das seis situações do treino você acertou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
