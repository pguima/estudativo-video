# Estudativo · QUI-EQL-009 — Calcular Kc (Química · Equilíbrio Químico · Equilíbrio e Le Chatelier).
# Habilidade: calcular Kc e o grau de equilíbrio pelo quadro início, reage, equilíbrio.
# Pré-requisitos: QUI-EQL-001, MAT-FRA-018, MAT-POR-002. Próxima: QUI-EQL-002 (princípio de Le Chatelier).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; resultado de conta sempre com "dá". Questão inédita.
# Leitura para a voz: HI = "agá i", I₂ = "i dois" ou "iodo", N₂O₄ = "ene dois ó quatro", α = "grau de equilíbrio".
# Contas: H₂ + I₂ ⇌ 2 HI; equilíbrio 0,1 / 0,1 / 0,8 ⇒ Kc = 0,64 / 0,01 = 64. Quadro: início 1 / 1 / 0; reage −0,8 / −0,8 / +1,6;
# equilíbrio 0,2 / 0,2 / 1,6 ⇒ Kc = 2,56 / 0,04 = 64; α = 0,8 / 1 = 80%. Erro: 1,6² / (1 · 1) = 2,56.
# Questão: 2 mol N₂O₄ em 2 L (1 mol/L); 0,8 mol NO₂ no equilíbrio (0,4 mol/L) ⇒ reage 0,2; sobra 0,8 ⇒ Kc = 0,16 / 0,8 = 0,2; α = 20%.
# Os valores de Kc são ilustrativos ("numa certa temperatura"); para HI a 450 °C a tabela dá perto de 50.

TITULO = "Calcular Kc"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}Você põe hidrogênio e iodo num frasco e espera. [p=0.2] {b}No fim, mede uma coisa só: quanto se formou de agá i. [p=0.3] {c}Com esse único número, dá para descobrir tudo o que sobrou [p=0.1] e o cá cê da reação. [p=0.2] {d}O truque é um quadro de três linhas."),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}calcular o cá cê [p=0.1] e {b}o grau de equilíbrio [p=0.1] com {c}o quadro início, reage, equilíbrio."),
    # lembrete
    dict(id="s03", block="lembrete", text="{a}Da aula anterior: cá cê é produtos sobre reagentes, com os coeficientes no expoente. [p=0.2] Você também vai {b}dividir por números decimais [p=0.1] e {c}calcular porcentagem. [p=0.2] Se faltar alguma, procure no canal."),
    # cálculo direto
    dict(id="s04", block="direto", text="{a}O caso mais simples: a questão já dá as concentrações no equilíbrio. [p=0.2] {b}Agá dois mais iodo formam dois agá i, numa certa temperatura. [p=0.3] {c}O agá dois tem zero vírgula um mol por litro. [p=0.1] {d}O iodo também. [p=0.1] {e}E o agá i, zero vírgula oito."),
    dict(id="s05", block="direto", text="{a}Cá cê é agá i ao quadrado, dividido por agá dois vezes iodo. [p=0.3] {b}Zero vírgula oito ao quadrado dá zero vírgula sessenta e quatro. [p=0.2] {c}Zero vírgula um vezes zero vírgula um dá zero vírgula zero um. [p=0.2] {d}Zero vírgula sessenta e quatro dividido por zero vírgula zero um {e}dá sessenta e quatro."),
    # o quadro
    dict(id="s06", block="quadro", text="{a}Quase sempre, porém, a questão dá o começo, e não o fim. [p=0.2] Aí entra o quadro. [p=0.2] {b}Na primeira linha, o início. [p=0.1] {c}Na segunda, o que reage. [p=0.1] {d}Na terceira, o equilíbrio, [p=0.1] {e}que é o início mais a linha do reage, com o sinal dela."),
    dict(id="s07", block="quadro", text="Veja. [p=0.1] {a}No início, um mol por litro de agá dois, um de iodo e nada de agá i. [p=0.3] {b}A questão diz que, no equilíbrio, há um vírgula seis mol por litro de agá i. [p=0.3] {c}Então se formou um vírgula seis de agá i: [p=0.1] {d}é o número que abre a linha do reage."),
    dict(id="s08", block="quadro", text="{a}A linha do reage segue os coeficientes. [p=0.2] {b}Para formar dois agá i, gasta-se um agá dois e um iodo. [p=0.2] {c}Formou um vírgula seis? [p=0.1] {d}Gastou a metade disso de cada um: zero vírgula oito. [p=0.3] {e}Reagente perde, então leva sinal de menos; [p=0.1] produto ganha, sinal de mais."),
    dict(id="s09", block="quadro", text="{a}No equilíbrio, um menos zero vírgula oito dá zero vírgula dois de agá dois, [p=0.1] {b}e o mesmo de iodo. [p=0.2] {c}De agá i, zero mais um vírgula seis dá um vírgula seis."),
    dict(id="s10", block="quadro", text="{a}Cá cê: um vírgula seis ao quadrado dá dois vírgula cinquenta e seis. [p=0.2] {b}Zero vírgula dois vezes zero vírgula dois dá zero vírgula zero quatro. [p=0.2] {c}Dividindo, dá sessenta e quatro de novo. [p=0.3] {d}Mesma reação, mesma temperatura: mesmo cá cê."),
    # grau de equilíbrio
    dict(id="s11", block="grau", text="{a}O grau de equilíbrio diz quanto do reagente reagiu, em porcentagem. [p=0.2] {b}É o que reagiu dividido pelo que havia no início. [p=0.3] {c}Zero vírgula oito dividido por um {d}dá zero vírgula oito: [p=0.1] {e}oitenta por cento do agá dois reagiu."),
    # erro comum
    dict(id="s12", block="erro", text="{a}O erro comum é pôr no cá cê os reagentes do início, junto com o produto do equilíbrio. [p=0.3] {b}Um vírgula seis ao quadrado, dividido por um vezes um, [p=0.1] {c}dá dois vírgula cinquenta e seis, e não sessenta e quatro. [p=0.3] {d}O cá cê só aceita a linha do equilíbrio."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho: [p=0.2] {a}ache um número da linha do reage, [p=0.1] e os outros saem pela proporção dos coeficientes. [p=0.2] {b}Aqui, o agá i formado dividido por dois dá o agá dois e o iodo gastos. [p=0.3] {c}E, se a questão der quantidades em mol e o volume, [p=0.1] {d}divida pelo volume antes de montar o quadro: [p=0.1] o cá cê usa mol por litro."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Num frasco de dois litros, numa certa temperatura, você coloca dois mols de ene dois ó quatro. [p=0.2] {b}Ele se transforma em ene ó dois, com coeficiente dois, até o equilíbrio. [p=0.3] {c}No equilíbrio, há zero vírgula oito mol de ene ó dois. [p=0.3] {d}Calcule o cá cê e o grau de equilíbrio."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Primeiro, divida pelo volume. [p=0.1] {b}Dois mols em dois litros dão um mol por litro de ene dois ó quatro no início. [p=0.2] {c}Zero vírgula oito mol em dois litros dão zero vírgula quatro mol por litro de ene ó dois no equilíbrio."),
    dict(id="s17", block="resposta", text="{a}Formou zero vírgula quatro de ene ó dois. [p=0.1] {b}Pelo coeficiente, gastou a metade: zero vírgula dois de ene dois ó quatro. [p=0.2] {c}No equilíbrio, sobra zero vírgula oito."),
    dict(id="s18", block="resposta", text="{a}Cá cê: zero vírgula quatro ao quadrado dá zero vírgula dezesseis. [p=0.2] {b}Dividido por zero vírgula oito, {c}dá zero vírgula dois. [p=0.3] {d}Grau de equilíbrio: zero vírgula dois dividido por um {e}dá zero vírgula dois, ou seja, vinte por cento."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}monte início, reage e equilíbrio, [p=0.1] {b}use os coeficientes na linha do reage [p=0.1] {c}e só ponha no cá cê a linha do equilíbrio."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}mexer no equilíbrio: [p=0.2] {b}mudar concentração, pressão e temperatura [p=0.1] {c}e prever para que lado ele se desloca. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
