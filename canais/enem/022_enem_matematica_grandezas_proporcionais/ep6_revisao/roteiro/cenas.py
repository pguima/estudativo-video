# Roteiro — Grandezas Proporcionais, Episódio 6 de 6: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seções 01, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 ETIQUETA R$/kg: o k é o número que não muda (direta: o quociente; inversa: o produto, o "bolo" de 240 km) ·
#   ep2 LUPA: o detetive tem dois testes (divide e multiplica) e testa TODAS as linhas · ep3 TAXÍMETRO: a PERGUNTA DA
#   ORIGEM; a reta do táxi nasce "devendo" a bandeirada · ep4 FRAÇÃO-GUIA: direto em cima, inverso embaixo; efeitos se
#   multiplicam · ep5 LANTERNA: azulejos ×4, cubinhos ×8, dobrou a distância → 1/4 da luz.
# Treino-relâmpago (direta, inversa ou nenhuma?): tabela (2; 9), (4; 18), (6; 27) → ÷ = 4,5 sempre → DIRETA ·
#   tabela (1; 24), (3; 8), (6; 4) → × = 24 sempre → INVERSA · gráfico: reta que corta o eixo vertical em 5 → NENHUMA ·
#   gráfico: hipérbole → INVERSA.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (a reta y = 2x + 10 é proporção direta; não nasce na origem) · 2 V (táxi R$ 6 + R$ 2,50/km: 8 km = 26, 16 km = 46) ·
#   3 F (lado dobra → área dobra; quadruplica) · 4 F (dobro da distância → metade da luz; 1/4) ·
#   5 V (idade e altura crescem juntas e NÃO são proporcionais) · 6 F (a 1ª linha da tabela basta para achar o k) ·
#   7 V (2,4 h = 2 h 24 min) · 8 F (y = k·a/b, a ×2 e b ×3 → y ×6; é ×2/3) · 9 F (a hipérbole acaba tocando os eixos).
# QUESTÕES INÉDITAS (todas conferidas em Python: uma única correta; cada errada = um erro clássico):
#   Q1 (tabela) gráfica: (10; 120), (20; 240), (30; 300), (40; 360) → ÷ 12, 12, 10, 9 · × 1 200, 4 800, 9 000, 14 400 →
#      nenhuma → E. A (direta, k = 12) testou só as duas primeiras linhas, que ENGANAM · B (inversa, k = 1 200) multiplicou só a
#      1ª linha · C (inversa, k = 12) achou o 12 e chamou de inversa · D (direta, k = 9) testou só a última linha.
#   Q2 (parcela fixa) água: R$ 30 fixos + R$ 5/m³; 10 m³ = R$ 80; 20 m³ = 30 + 100 = R$ 130 → C.
#      A 100 (esqueceu a taxa) · B 110 (dobrou a parte fixa e não o consumo: 60 + 50) · D 160 (dobrou tudo, inclusive a taxa) ·
#      E 190 (dobrou tudo e ainda somou outra taxa).
#   Q3 (inversa + horas decimais) 3 máquinas em 6 h → 5 máquinas: 3·6 = 18 = 5·t → t = 3,6 h = 3 h 36 min → B.
#      A 3 h 6 min (leu 0,6 h como 6 min) · C 4 h (leu 0,6 h como 60 min) · D 6 h (achou que nada muda) · E 10 h (direta).
#   Q4 (fórmula, duas mudanças) pressão = k · força/área; 600 Pa; força ×3 e área ×2 → 600·3/2 = 900 Pa → C.
#      A 300 (ignorou a força) · B 400 (inverteu: força embaixo, área em cima) · D 1 800 (ignorou a área) ·
#      E 3 000 (SOMOU os efeitos: ×5).
#   Q5 (inverso do quadrado, som) 50 a 4 m → 2 m (distância ÷ 2 → intensidade ×4) = 200 → D.
#      A 12,5 (aplicou o ¼ no sentido errado) · B 25 (tratou como direta) · C 100 (inversa simples, sem o quadrado) ·
#      E 400 (usou o cubo, ×8).
# Checklist (seção 13, 13 itens) → episódio: quociente/produto, achar o k, o que o k significa e décimos de hora: ep1 ·
#   tabela e todas as linhas: ep2 · gráfico, reta fora da origem e parcela fixa: ep3 · direto em cima e ler fórmulas: ep4 ·
#   quadrática, cúbica e inverso do quadrado: ep5 · conferir se faz sentido: todos.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), priorizando tabela e parcela fixa.
# Ponte (do usuário): Divisão proporcional (os pacotinhos de k da série de Razão).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de grandezas proporcionais: treino, 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 6"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Na regra de três você aprendeu a *resolver.* [p=0.3] {b}Aqui aprendeu a *reconhecer,* [p=0.3] e o ENEM "
        "pergunta das *duas* formas. [p=0.4] {c}Hoje você confere se está *pronto.* [p=0.4] {d}Com um treino, [p=0.2] "
        "nove frases [p=0.2] e cinco questões novas."),

    # ================= OS TRÊS FORMATOS (seção 01) =================
    dict(id="02", block="formatos", text=
        "{t}E o ENEM pergunta de *três* jeitos. [p=0.3] {a}Com uma *tabela:* [p=0.2] que relação é essa, [p=0.2] ou qual "
        "valor falta? [p=0.3] {b}Com um *gráfico:* [p=0.2] que situação esse desenho representa? [p=0.3] {c}E com uma "
        "*fórmula* de Física ou de Química: [p=0.2] o que acontece com uma grandeza [p=0.2] quando outra dobra?"),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] o *k* é o número que não muda. "
        "[p=0.2] Na direta, [p=0.2] o quociente, [p=0.2] como o preço por quilo da etiqueta. [p=0.2] Na inversa, [p=0.2] "
        "o produto, [p=0.2] como o bolo de duzentos e quarenta quilômetros. [p=0.4] {b}Dois: [p=0.2] o *detetive* da "
        "tabela divide [p=0.2] e multiplica, [p=0.2] em *todas* as linhas. [p=0.4] {c}Três: [p=0.2] a *pergunta da "
        "origem.* [p=0.2] Zero de um dá zero do outro? [p=0.2] A reta do táxi nasce devendo a bandeirada."),
    dict(id="04", block="indice", text=
        "{a}Quatro: [p=0.2] a *fração-guia.* [p=0.2] O que é direto vai em cima, [p=0.2] o que é inverso vai embaixo, "
        "[p=0.2] e os efeitos se *multiplicam.* [p=0.4] {b}E cinco: [p=0.2] quando dobrar não dobra. [p=0.2] Azulejos, "
        "[p=0.2] vezes quatro. [p=0.2] Cubinhos, [p=0.2] vezes oito. [p=0.2] E a *lanterna:* [p=0.2] o dobro da "
        "distância, [p=0.2] um quarto da luz."),

    # ================= O QUE MAIS RENDE + TREINO-RELÂMPAGO =================
    dict(id="05", block="rendem", text=
        "{t}E se você só tiver tempo para duas coisas? [p=0.4] {a}Primeiro: [p=0.2] o *teste da tabela,* [p=0.2] "
        "dividir e multiplicar. [p=0.4] {b}Segundo: [p=0.2] a *reta que não passa pela origem,* [p=0.2] a armadilha "
        "mais cobrada do assunto."),
    dict(id="06", block="treino", text=
        "{t}Treino-relâmpago. [p=0.3] {a}Direta, [p=0.2] inversa, [p=0.2] ou *nenhuma?* [p=0.4] {b}Um: [p=0.2] a "
        "tabela dois e nove, [p=0.2] quatro e dezoito, [p=0.2] seis e vinte e sete. [p=0.3] {c}Dois: [p=0.2] a tabela "
        "um e vinte e quatro, [p=0.2] três e oito, [p=0.2] seis e quatro. [p=0.3] {d}Três: [p=0.2] uma reta que corta o "
        "eixo vertical no cinco. [p=0.3] {e}Quatro: [p=0.2] uma curva que desce e vai chegando perto dos dois eixos. "
        "[p=0.4] {p}*Pause e decida.* [p=2.0]"),
    dict(id="07", block="treino", text=
        "{t}Conferindo! [p=0.3] {a}Na primeira, [p=0.2] o quociente dá sempre quatro e meio. [p=0.2] *Direta.* [p=0.3] "
        "{b}Na segunda, [p=0.2] o produto dá sempre vinte e quatro. [p=0.2] *Inversa.* [p=0.3] {c}A reta começa no "
        "cinco: [p=0.2] zero de um não dá zero do outro. [p=0.2] *Nenhuma.* [p=0.3] {d}E a curva que nunca toca os "
        "eixos é a hipérbole. [p=0.2] *Inversa.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] o gráfico de y igual a dois xis mais dez é uma reta, [p=0.2] então é proporção *direta.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é uma reta, [p=0.2] e a direta também é. "
        "[p=0.3] {g}Mas faça a pergunta da origem: [p=0.2] com xis igual a zero, [p=0.2] y vale *dez,* [p=0.2] não "
        "zero. [p=0.2] Tem parcela fixa."),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] um táxi cobra seis reais de bandeirada [p=0.2] mais dois e cinquenta por quilômetro. [p=0.2] "
        "Oito quilômetros custam vinte e seis reais, [p=0.2] e dezesseis quilômetros custam *quarenta e seis.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de dobrar: [p=0.2] cinquenta e "
        "dois. [p=0.3] {g}Mas a bandeirada é cobrada *uma vez só.* [p=0.2] Seis mais quarenta: [p=0.2] quarenta e seis."),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] se o lado de um quadrado dobra, [p=0.2] a área também *dobra.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o lado e a área crescem juntos. [p=0.3] {g}Lembre dos azulejos: [p=0.2] "
        "dois de largura vezes dois de comprimento. [p=0.2] A área fica *quatro* vezes maior."),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] se você fica ao dobro da distância de uma lâmpada, [p=0.2] a luz cai pela *metade.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece uma inversa simples. [p=0.3] {g}Mas é "
        "o inverso do *quadrado:* [p=0.2] a mesma luz se espalha por uma área quatro vezes maior. [p=0.2] Cada pedaço "
        "recebe *um quarto.*"),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] a idade e a altura de uma criança crescem juntas, [p=0.2] mas *não* são proporcionais. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque crescer junto parece proporção. "
        "[p=0.3] {g}Mas ninguém tem o dobro da altura ao dobrar de idade. [p=0.2] Proporção exige a razão "
        "*constante.*"),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] numa tabela, [p=0.2] basta dividir a *primeira linha* para achar o k. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque uma linha sozinha sempre dá algum número. [p=0.3] {g}Mas é a "
        "*constância* que prova a relação. [p=0.2] O detetive testa *todas* as linhas."),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] dois vírgula quatro horas [p=0.2] são duas horas e *vinte e quatro* minutos. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente lê duas horas e quarenta. [p=0.3] "
        "{g}Mas décimo de hora não é minuto: [p=0.2] zero vírgula quatro vezes sessenta, [p=0.2] *vinte e quatro.*"),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] em y igual a k vezes a sobre b, [p=0.2] se o a dobra e o b triplica, [p=0.2] y fica *seis* "
        "vezes maior. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o dois e o três parecem se "
        "juntar. [p=0.3] {g}Mas o b está *embaixo:* [p=0.2] ele divide. [p=0.2] Vezes dois, [p=0.2] dividido por "
        "três: [p=0.2] y fica multiplicado por *dois terços.*"),
    dict(id="17", block="vf", text=
        "{t}E nove: [p=0.2] a hipérbole de uma relação inversa acaba *tocando* os eixos. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a curva chega muito perto. [p=0.3] {g}Mas nunca encosta: [p=0.2] por "
        "mais rápido que você dirija, [p=0.2] o tempo de viagem nunca chega a *zero.*"),
    dict(id="18", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM."),

    # ================= QUESTÃO 1: TABELA COM LINHAS QUE ENGANAM =================
    dict(id="19", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma gráfica registrou o preço total cobrado por lotes de camisetas: [p=0.2] dez "
        "camisetas, [p=0.2] cento e vinte reais. [p=0.2] Vinte, [p=0.2] duzentos e quarenta. [p=0.2] Trinta, [p=0.2] "
        "trezentos. [p=0.2] Quarenta, [p=0.2] trezentos e sessenta. [p=0.3] {b}Sobre o número de camisetas e o preço "
        "total, [p=0.2] é correto afirmar que as duas grandezas são: [p=0.4] {la}A, [p=0.2] diretamente proporcionais, com k igual a "
        "doze. [p=0.2] {lb}B, [p=0.2] inversamente proporcionais, com k igual a mil e duzentos. [p=0.2] {lc}C, [p=0.2] "
        "inversamente proporcionais, com k igual a doze. [p=0.2] {ld}D, [p=0.2] diretamente proporcionais, com k igual "
        "a nove. [p=0.2] {le}E, [p=0.2] nem diretamente, nem inversamente proporcionais. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q1", text=
        "{d}O detetive entra em ação. [p=0.2] {a}Primeiro teste, [p=0.2] dividir: [p=0.2] doze, [p=0.2] doze… "
        "[p=0.2] {b}e depois *dez* [p=0.2] e *nove.* [p=0.2] Não é constante. [p=0.3] {c}Segundo teste, [p=0.2] "
        "multiplicar: [p=0.2] mil e duzentos, [p=0.2] quatro mil e oitocentos… [p=0.2] também muda. [p=0.3] Nenhum "
        "dos dois: [p=0.2] *não são proporcionais.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Faz sentido: [p=0.2] lote maior "
        "costuma ter desconto. [p=0.4] {xa}A A caiu nas duas primeiras linhas, [p=0.2] as que *enganam.* [p=0.2] "
        "{xd}A D olhou só a última. [p=0.2] {xb}A B multiplicou uma linha só. [p=0.2] {xc}E a C achou o doze [p=0.2] "
        "e chamou de inversa."),

    # ================= QUESTÃO 2: PARCELA FIXA =================
    dict(id="21", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma companhia de água cobra uma taxa fixa de *trinta reais* por mês [p=0.2] mais "
        "*cinco reais* por metro cúbico consumido. [p=0.3] {b}Uma família consumiu dez metros cúbicos e pagou oitenta "
        "reais. [p=0.2] No mês seguinte, [p=0.2] consumiu o *dobro.* [p=0.2] Quanto pagou? [p=0.4] {la}A, [p=0.2] cem "
        "reais. [p=0.2] {lb}B, [p=0.2] cento e dez. [p=0.2] {lc}C, [p=0.2] cento e trinta. [p=0.2] {ld}D, [p=0.2] "
        "cento e sessenta. [p=0.2] {le}E, [p=0.2] cento e noventa. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{g}Pergunta da origem: [p=0.2] com consumo zero, [p=0.2] a conta é zero? [p=0.2] *Não:* [p=0.2] trinta "
        "reais. [p=0.2] Tem parcela fixa. [p=0.3] {a}Separe o fixo do que varia. [p=0.2] Vinte metros cúbicos vezes "
        "cinco: [p=0.2] cem reais. [p=0.3] {b}Mais a taxa, [p=0.2] *uma vez só:* [p=0.2] *cento e trinta.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {xd}A D dobrou tudo, [p=0.2] até a taxa. [p=0.2] {xe}A E dobrou tudo [p=0.2] e ainda "
        "somou outra taxa. [p=0.2] {xa}A A esqueceu a taxa. [p=0.2] {xb}E a B dobrou a parte errada: [p=0.2] a fixa."),

    # ================= QUESTÃO 3: INVERSA COM HORAS DECIMAIS =================
    dict(id="23", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Três máquinas iguais embalam um lote de produtos em *seis horas.* [p=0.3] {b}Com "
        "*cinco* máquinas iguais a essas, [p=0.2] no mesmo ritmo, [p=0.2] o mesmo lote será embalado em: [p=0.4] "
        "{la}A, [p=0.2] três horas e seis minutos. [p=0.2] {lb}B, [p=0.2] três horas e trinta e seis minutos. [p=0.2] "
        "{lc}C, [p=0.2] quatro horas. [p=0.2] {ld}D, [p=0.2] seis horas. [p=0.2] {le}E, [p=0.2] dez horas. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q3", text=
        "{d}Mais máquinas, [p=0.2] menos tempo: [p=0.2] *inversa.* [p=0.2] O produto não muda. [p=0.3] {a}Três vezes "
        "seis, [p=0.2] dezoito, [p=0.2] igual a cinco vezes o tempo. [p=0.3] {b}O tempo é dezoito dividido por cinco: "
        "[p=0.2] três vírgula seis horas. [p=0.3] {c}E agora, [p=0.2] o relógio: [p=0.2] zero vírgula seis vezes "
        "sessenta, [p=0.2] *trinta e seis* minutos. [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A leu o seis como seis "
        "minutos. [p=0.2] {xc}A C leu como sessenta minutos. [p=0.2] {xd}A D achou que nada muda. [p=0.2] {xe}E a E "
        "usou direta: [p=0.2] mais máquinas, [p=0.2] mais tempo? [p=0.2] Não faz sentido."),

    # ================= QUESTÃO 4: FÓRMULA COM DUAS MUDANÇAS =================
    dict(id="25", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}A pressão que um objeto faz sobre o chão é diretamente proporcional à *força* "
        "[p=0.2] e inversamente proporcional à *área* de apoio. [p=0.3] {b}Um objeto faz pressão de *seiscentos* "
        "pascals, [p=0.2] a unidade de pressão. [p=0.3] {c}Se a força *triplicar* [p=0.2] e a área de apoio "
        "*dobrar,* [p=0.2] a pressão passará a ser de: [p=0.4] {la}A, [p=0.2] trezentos pascals. [p=0.2] {lb}B, "
        "[p=0.2] quatrocentos. [p=0.2] {lc}C, [p=0.2] novecentos. [p=0.2] {ld}D, [p=0.2] mil e oitocentos. [p=0.2] "
        "{le}E, [p=0.2] três mil. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{d}Fração-guia: [p=0.2] a força, [p=0.2] direta, [p=0.2] vai em cima. [p=0.2] A área, [p=0.2] inversa, "
        "[p=0.2] vai embaixo. [p=0.3] {a}Os efeitos se multiplicam: [p=0.2] vezes três, [p=0.2] dividido por dois. "
        "[p=0.3] {b}Seiscentos vezes três, [p=0.2] mil e oitocentos. [p=0.2] Dividido por dois, [p=0.2] *novecentos.* "
        "[p=0.2] {ok}*Letra C!* [p=0.4] {xe}A E *somou* os efeitos: [p=0.2] vezes cinco. [p=0.2] {xd}A D ignorou a "
        "área. [p=0.2] {xa}A A ignorou a força. [p=0.2] {xb}E a B trocou os andares: [p=0.2] força embaixo, [p=0.2] "
        "área em cima."),

    # ================= QUESTÃO 5: INVERSO DO QUADRADO =================
    dict(id="27", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}A intensidade do som de uma caixa de som é inversamente proporcional ao "
        "*quadrado* da distância até ela. [p=0.3] {b}A *quatro metros,* [p=0.2] um medidor marca *cinquenta* unidades. "
        "[p=0.3] {c}A *dois metros* da caixa, [p=0.2] o medidor vai marcar: [p=0.4] {la}A, [p=0.2] doze vírgula cinco. "
        "[p=0.2] {lb}B, [p=0.2] vinte e cinco. [p=0.2] {lc}C, [p=0.2] cem. [p=0.2] {ld}D, [p=0.2] duzentos. [p=0.2] "
        "{le}E, [p=0.2] quatrocentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{d}Lembre da lanterna. [p=0.2] Aqui a distância *caiu* pela metade. [p=0.3] {a}Metade da distância, [p=0.2] "
        "o som se concentra numa área quatro vezes *menor.* [p=0.3] {b}Então a intensidade fica *quatro* vezes maior: "
        "[p=0.2] cinquenta vezes quatro, [p=0.2] *duzentos.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Faz sentido: [p=0.2] "
        "mais perto, [p=0.2] mais alto. [p=0.4] {xc}A C esqueceu o quadrado: [p=0.2] só dobrou. [p=0.2] {xb}A B "
        "tratou como direta. [p=0.2] {xa}A A aplicou o um quarto ao contrário. [p=0.2] {xe}E a E usou o cubo."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="29", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta,* "
        "[p=0.2] sem consultar nada. [p=0.4] {b}Quociente e produto, [p=0.2] achar o k, [p=0.2] o que ele significa "
        "[p=0.2] e décimo de hora: [p=0.2] episódio um. [p=0.3] {c}Tabela, [p=0.2] testando todas as linhas: [p=0.2] "
        "episódio dois. [p=0.3] {d}Gráfico, [p=0.2] reta fora da origem [p=0.2] e parcela fixa: [p=0.2] episódio três."),
    dict(id="30", block="checklist", text=
        "{a}Direto em cima, [p=0.2] inverso embaixo, [p=0.2] e ler fórmulas de Física: [p=0.2] episódio quatro. "
        "[p=0.3] {b}Quadrado, [p=0.2] cubo [p=0.2] e inverso do quadrado: [p=0.2] episódio cinco. [p=0.3] {c}E "
        "conferir se o resultado faz sentido: [p=0.2] *todos* eles. [p=0.4] {d}O que você *não* marcou, [p=0.2] reveja "
        "o episódio correspondente."),

    # ================= META =================
    dict(id="31", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta* questões [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}Priorize as de *tabela* [p=0.2] e as de *parcela fixa:* [p=0.2] juntas, [p=0.2] elas são "
        "a maior parte das questões deste assunto."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}O próximo assunto é *Divisão proporcional,* [p=0.3] {b}e o truque dos *pacotinhos de k* [p=0.2] que você viu "
        "na série de Razão [p=0.2] vai virar a ferramenta principal."),
    dict(id="33", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual questão te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de grandezas proporcionais está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
