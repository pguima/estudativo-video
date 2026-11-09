# Estudativo · FIS-CIN-013 — Queda livre (Física · Cinemática · Queda livre e lançamentos).
# Habilidade: calcular tempo de queda e velocidade de chegada sem resistência do ar, com g = 10 m/s² e o atalho h = 5·t².
# Pré-requisitos: FIS-CIN-009 (Torricelli), com FIS-CIN-007 e FIS-CIN-008 já ensinadas. Próxima: FIS-CIN-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fato do gancho: na missão Apollo 15 (1971), o astronauta David Scott soltou um martelo e uma pena na Lua; caíram juntos.
# Contas: v = 10·t → 10, 20, 30; h = 5·t² → 5, 20, 45, 80; 80 = 5t² → t = 4 s, v = 40 m/s; Torricelli: v² = 2·10·80 = 1600 → 40.
# Erro: 80 = 10·t² → t² = 8 → t ≈ 2,8 s. Questão: 45 m → t = 3 s, v = 30 m/s = 108 km/h (RAZ-016 já ensinada).

TITULO = "Queda livre"

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
    dict(id="s01", block="gancho", text="Em mil novecentos e setenta e um, na Lua, [p=0.2] um astronauta soltou {a}um martelo [p=0.1] e {b}uma pena [p=0.1] ao mesmo tempo. [p=0.3] {c}Os dois chegaram juntos ao chão. [p=0.3] Na Lua não há ar, [p=0.2] e sem ar {d}tudo cai do mesmo jeito, pesado ou leve."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}quanto tempo um objeto leva para cair [p=0.2] e {c}com que velocidade ele chega ao chão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa das fórmulas do movimento com aceleração constante: [p=0.2] {a}a da velocidade, vê igual a vê zero mais a aceleração vezes tê, [p=0.2] e {b}a da posição, com o tê ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="conceito", text="Queda livre é {a}cair só pela gravidade, [p=0.2] {b}a partir do repouso [p=0.1] e {c}sem a resistência do ar. [p=0.3] Na Terra, o ar segura a pena. [p=0.2] Por isso, as questões dizem: {d}despreze a resistência do ar."),
    dict(id="s05", block="conceito", text="Perto do chão, a gravidade dá a todo corpo a mesma aceleração, [p=0.2] que se chama {a}gê. [p=0.2] Vale {b}cerca de nove vírgula oito metros por segundo ao quadrado, [p=0.2] e a prova quase sempre usa {c}dez."),
    # velocidade
    dict(id="s06", block="velocidade", text="Dez metros por segundo ao quadrado quer dizer: [p=0.2] {a}a cada segundo, a velocidade aumenta dez metros por segundo. [p=0.3] {b}Depois de um segundo, dez. [p=0.2] {c}Depois de dois, vinte. [p=0.2] {d}Depois de três, trinta."),
    dict(id="s07", block="velocidade", text="É a fórmula da velocidade com {a}vê zero igual a zero, [p=0.1] porque o objeto foi solto, [p=0.2] e {b}a aceleração igual a gê. [p=0.3] Sobra {c}vê igual a gê vezes tê: [p=0.2] {d}na prova, dez vezes o tempo."),
    # altura
    dict(id="s08", block="altura", text="E a altura? [p=0.2] Na fórmula da posição, {a}o objeto sai do repouso, [p=0.2] e o deslocamento é {b}a aceleração vezes tê ao quadrado, dividido por dois. [p=0.3] Com a aceleração igual a dez, {c}dez dividido por dois é cinco. [p=0.3] Fica o atalho da queda: {d}agá igual a cinco tê ao quadrado. [p=0.2] {e}Agá é a altura da queda, em metros, [p=0.1] e tê é o tempo, em segundos."),
    dict(id="s09", block="altura", text="Veja como a altura cresce rápido. [p=0.2] {a}Em um segundo, cinco metros. [p=0.2] {b}Em dois, vinte. [p=0.2] {c}Em três, quarenta e cinco. [p=0.2] {d}Em quatro, oitenta. [p=0.3] {e}Como a velocidade só aumenta, cada segundo de queda cobre mais metros que o anterior."),
    # exemplo
    dict(id="s10", block="exemplo", text="Um objeto cai de {a}oitenta metros. [p=0.2] {b}Oitenta igual a cinco tê ao quadrado. [p=0.2] {c}Divida por cinco: tê ao quadrado é dezesseis. [p=0.2] {d}Tê é quatro segundos, [p=0.1] a raiz de dezesseis."),
    dict(id="s11", block="exemplo", text="A velocidade de chegada: {a}dez vezes quatro, [p=0.1] {b}quarenta metros por segundo. [p=0.3] Sem o tempo, {c}Torricelli dá o mesmo: [p=0.2] vê ao quadrado igual a duas vezes dez vezes oitenta, mil e seiscentos. [p=0.2] {d}A raiz é quarenta."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o dividido por dois. [p=0.3] A pessoa escreve {b}oitenta igual a dez tê ao quadrado, [p=0.2] acha tê ao quadrado igual a oito, [p=0.2] e responde {c}quase três segundos. [p=0.3] {d}Errado: são quatro. [p=0.2] Para não errar, use direto {e}o cinco: [p=0.1] ele já é a metade de dez."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}decore a tabela da queda. [p=0.3] {b}Um segundo, cinco metros. [p=0.1] {c}Dois, vinte. [p=0.1] {d}Três, quarenta e cinco. [p=0.1] {e}Quatro, oitenta. [p=0.1] {f}Cinco, cento e vinte e cinco. [p=0.3] São os quadrados um, quatro, nove, dezesseis e vinte e cinco, [p=0.1] vezes cinco."),
    dict(id="s14", block="atalho", text="Ela mostra outra coisa: [p=0.2] {a}com o dobro do tempo, a altura fica quatro vezes maior. [p=0.3] {b}Não compensa quando a altura não está na tabela, como sessenta metros: [p=0.2] aí, {c}divida por cinco e tire a raiz de doze, [p=0.1] quase três vírgula cinco segundos."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um vaso cai do alto de um prédio de {b}quarenta e cinco metros. [p=0.2] Despreze a resistência do ar. [p=0.3] {c}Quanto tempo ele leva para chegar ao chão? [p=0.2] {d}E com que velocidade chega?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Quarenta e cinco igual a cinco tê ao quadrado. [p=0.2] {b}Tê ao quadrado é nove, [p=0.1] {c}e tê é três segundos. [p=0.2] Quem decorou a tabela, nem fez conta."),
    dict(id="s18", block="resposta", text="{a}Velocidade: dez vezes três, [p=0.1] {b}trinta metros por segundo. [p=0.3] Em quilômetros por hora, {c}cento e oito. [p=0.2] Por isso, nunca fique embaixo de onde algo pode cair."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: sem o ar, {a}tudo cai com a mesma aceleração, gê igual a dez. [p=0.2] {b}A velocidade é dez vezes o tempo, [p=0.2] e {c}a altura é cinco vezes o tempo ao quadrado."),
    dict(id="s20", block="fim", text="Na próxima aula, a bola {a}é jogada para cima: [p=0.2] você vai achar {b}a altura máxima [p=0.1] e {c}o tempo que ela fica no ar. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
