# Estudativo · FIS-MOD-003 — Espectros e níveis de energia (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: ligar o salto do elétron à cor emitida e diferenciar espectro de emissão de absorção.
# Pré-requisitos: FIS-MOD-001 (E = h·f, elétron-volt), QUI-ATO-003 (modelo de Bohr: níveis e saltos). Próxima: FIS-MOD-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Níveis do hidrogênio: Eₙ = −13,6/n² eV → −13,6; −3,4; −1,51; −0,85. Saltos: 3→2 = 1,89 eV (vermelho, 656 nm);
# 4→2 = 2,55 eV (azul-esverdeado, 486 nm); 2→1 = 10,2 eV (ultravioleta). Hélio: achado no espectro do Sol em 1868,
# na Terra só em 1895: linha amarela de EMISSÃO na borda do Sol num eclipse (não uma linha escura). Atalho: de um nível n, o número de linhas possíveis é n·(n − 1)/2 (pares de níveis).

TITULO = "Espectros e níveis de energia"

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
    dict(id="s01", block="gancho", text="{a}Ninguém nunca foi ao Sol. [p=0.2] Mesmo assim, a gente sabe do que ele é feito. [p=0.3] {b}O gás hélio foi descoberto no Sol em mil oitocentos e sessenta e oito, [p=0.2] {c}quase trinta anos antes de ser achado na Terra. [p=0.3] {d}A pista estava nas cores da luz."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai ligar cada salto do elétron a uma cor [p=0.2] e {b}diferenciar o espectro de emissão do espectro de absorção."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a energia do fóton é agá vezes efe, e frequência maior é fóton mais forte; [p=0.2] e {c}no modelo de Bohr, o elétron só fica em certos níveis de energia. [p=0.3] Se faltar alguma, procure no canal."),
    # os níveis
    dict(id="s04", block="niveis", text="Os níveis são como {a}os degraus de uma escada. [p=0.2] No hidrogênio, {b}o primeiro nível vale menos treze vírgula seis elétron-volts, [p=0.1] {c}o segundo, menos três vírgula quatro, [p=0.1] {d}o terceiro, menos um vírgula cinquenta e um."),
    dict(id="s05", block="niveis", text="Por que negativos? [p=0.2] {a}O zero é o elétron solto, fora do átomo. [p=0.2] {b}Preso, ele tem menos que isso: [p=0.2] é preciso dar energia para soltá-lo. [p=0.3] {c}Quanto mais embaixo na escada, mais preso o elétron está."),
    # emissão
    dict(id="s06", block="salto", text="{a}Quando o elétron desce um degrau, [p=0.2] {b}ele solta um fóton. [p=0.3] {c}A energia do fóton é a diferença entre os níveis: [p=0.2] {d}energia do nível de cima menos a do nível de baixo, [p=0.1] {e}igual a agá vezes efe."),
    dict(id="s07", block="salto", text="Do terceiro para o segundo nível: [p=0.2] {a}menos um vírgula cinquenta e um, tirando menos três vírgula quatro. [p=0.2] {b}Tirar um negativo é somar: [p=0.1] um vírgula oitenta e nove elétron-volt. [p=0.3] {c}Esse fóton é vermelho. [p=0.2] {d}Do segundo para o primeiro, o salto é de dez vírgula dois elétron-volts: [p=0.2] {e}um fóton ultravioleta, que o olho não vê."),
    dict(id="s08", block="salto", text="{a}Salto grande, fóton forte, cor puxada para o violeta. [p=0.2] {b}Salto pequeno, fóton fraco, cor puxada para o vermelho. [p=0.3] E como os degraus são fixos, [p=0.2] {c}cada elemento só emite algumas cores certas."),
    # emissão e absorção
    dict(id="s09", block="espectro", text="Passe essa luz por um prisma, que separa as cores. [p=0.2] {a}O gás quente brilha em poucas linhas coloridas, sobre um fundo escuro. [p=0.2] Isso é o {b}espectro de emissão. [p=0.3] {c}Cada elemento tem as suas linhas, como uma impressão digital."),
    dict(id="s10", block="espectro", text="Agora, o contrário. [p=0.2] {a}Passe luz branca, que tem todas as cores, por um gás frio. [p=0.3] {b}O elétron sobe de degrau absorvendo só o fóton que paga exatamente o salto. [p=0.3] {c}Sai um arco-íris com linhas escuras. [p=0.2] É o {d}espectro de absorção, [p=0.2] e {e}as linhas escuras ficam nas mesmas posições das linhas coloridas da emissão."),
    dict(id="s11", block="espectro", text="{a}A luz do Sol tem linhas escuras, [p=0.2] porque os gases mais frios da camada de fora do Sol absorvem algumas cores. [p=0.3] E o hélio? [p=0.2] {b}Num eclipse, a borda do Sol mostrou uma linha amarela brilhante [p=0.2] {c}que não batia com nenhum elemento conhecido. [p=0.2] {d}Era o hélio."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}usar o valor do nível no lugar da diferença. [p=0.3] {b}A pessoa diz que o fóton do terceiro nível tem um vírgula cinquenta e um elétron-volt. [p=0.3] {c}Errado: o fóton leva o tamanho do salto. [p=0.2] {d}Do terceiro para o segundo, um vírgula oitenta e nove. [p=0.2] {e}Do terceiro para o primeiro, doze vírgula zero nove. [p=0.2] Mesmo ponto de partida, fótons diferentes."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}quantas linhas diferentes um gás pode mostrar? [p=0.3] {b}Cada par de níveis dá um salto. [p=0.2] Com elétrons no terceiro nível, {c}os saltos são três para dois, três para um e dois para um: [p=0.1] {d}três linhas."),
    dict(id="s14", block="atalho", text="A conta rápida é {a}ene vezes ene menos um, dividido por dois, [p=0.2] onde ene é o nível de partida. [p=0.3] {b}Funciona porque é o número de pares que dá para formar com ene degraus. [p=0.3] {c}Não serve para dizer a cor: [p=0.1] para isso, faça a diferença de energia."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}No hidrogênio, o quarto nível vale menos zero vírgula oitenta e cinco elétron-volt. [p=0.3] {b}Qual é a energia do fóton do salto do quarto para o segundo nível? [p=0.2] {c}Ele fica mais perto do violeta ou do vermelho que o salto do terceiro para o segundo? [p=0.2] E {d}quantas linhas diferentes um gás com elétrons no quarto nível pode mostrar?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Menos zero vírgula oitenta e cinco, tirando menos três vírgula quatro: [p=0.2] {b}dois vírgula cinquenta e cinco elétron-volts. [p=0.3] {c}É maior que um vírgula oitenta e nove, [p=0.2] então {d}fica mais perto do violeta. [p=0.2] De fato, é uma linha azul-esverdeada."),
    dict(id="s18", block="resposta", text="E as linhas: [p=0.2] {a}quatro vezes três, doze, [p=0.1] {b}dividido por dois, [p=0.1] {c}seis linhas. [p=0.3] {d}Quatro para três, para dois e para um, [p=0.1] três para dois e para um, [p=0.1] e dois para um."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o fóton leva a diferença entre os níveis; [p=0.2] {b}salto maior, cor mais perto do violeta; [p=0.2] e {c}emissão são linhas coloridas, absorção são linhas escuras, nas mesmas posições."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a luz se comporta ora como onda, ora como partícula, [p=0.2] e {b}o elétron também. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
