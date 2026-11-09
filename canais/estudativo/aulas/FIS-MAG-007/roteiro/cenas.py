# Estudativo · FIS-MAG-007 — Transformadores e transmissão (Física · Magnetismo · Magnetismo e indução).
# Habilidade: usar U1/U2 = N1/N2 e explicar por que a tensão alta reduz a corrente e a perda r·i² nas linhas.
# Pré-requisitos: FIS-MAG-006, FIS-ELE-017. Próxima: FIS-MAG-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Transformador ideal (sem perdas): U1·i1 = U2·i2. Exemplo de linha: 100 kW,
# r = 5 Ω; a 1.000 V, i = 100 A e perde 50 kW; a 10.000 V, i = 10 A e perde 500 W.

TITULO = "Transformadores e transmissão"

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
    dict(id="s01", block="gancho", text="{a}A energia elétrica sai da usina e viaja centenas de quilômetros [p=0.2] {b}com centenas de milhares de volts. [p=0.3] {c}Na sua tomada, chegam cento e vinte e sete ou duzentos e vinte. [p=0.3] {d}Por que subir tanto a tensão, para depois baixar?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a tensão de um transformador [p=0.2] e {b}entender por que a tensão alta quase acaba com a perda nos fios."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Fluxo mudando numa bobina cria tensão, pela lei de Faraday. [p=0.3] E {c}a potência elétrica é tensão vezes corrente, [p=0.1] e a perda num fio é erre vezes i ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # transformador
    dict(id="s04", block="transf", text="O transformador é simples: [p=0.2] {a}um anel de ferro [p=0.1] com {b}duas bobinas enroladas nele. [p=0.3] {c}A primeira, chamada primária, recebe a tensão da rede. [p=0.2] {d}A segunda, a secundária, entrega a tensão nova."),
    dict(id="s05", block="transf", text="{a}A rede é de corrente alternada: [p=0.1] ela vai e volta o tempo todo. [p=0.3] {b}Então, o campo da primária muda o tempo todo. [p=0.2] {c}O ferro leva esse fluxo até a secundária, [p=0.2] e {d}o fluxo mudando cria tensão nela, pela lei de Faraday. [p=0.3] {e}Nenhum fio liga uma bobina na outra."),
    dict(id="s06", block="transf", text="Cada espira recebe {a}a mesma mudança de fluxo, [p=0.2] e ganha a mesma tensão. [p=0.3] Então, {b}mais espiras, mais tensão. [p=0.3] {c}U um dividido por U dois é igual a ene um dividido por ene dois. [p=0.2] {d}U é a tensão, em volt, [p=0.1] e {e}ene é o número de espiras de cada bobina."),
    dict(id="s07", block="transf", text="Um exemplo. [p=0.2] {a}Duzentos e vinte volts na primária, que tem mil e cem espiras. [p=0.2] {b}A secundária tem sessenta espiras. [p=0.3] {c}Mil e cem dividido por sessenta [p=0.1] é o mesmo que duzentos e vinte dividido por U dois. [p=0.3] {d}Duzentos e vinte vezes sessenta, dividido por mil e cem: [p=0.1] {e}doze volts. [p=0.2] É o que fazia o carregador antigo, aquele pesado."),
    dict(id="s08", block="transf", text="{a}E com uma pilha, ele não funciona. [p=0.2] {b}A corrente da pilha é contínua: [p=0.1] o fluxo fica parado, [p=0.2] e {c}fluxo parado não cria tensão."),
    # potência
    dict(id="s09", block="potencia", text="Agora, o ponto que a prova mais cobra. [p=0.2] {a}O transformador não cria energia. [p=0.3] Num transformador ideal, {b}a potência que entra é a potência que sai: [p=0.2] {c}U um vezes i um é igual a U dois vezes i dois. [p=0.3] {d}Se a tensão sobe, a corrente desce na mesma proporção."),
    # transmissão
    dict(id="s10", block="linha", text="E é aí que entra a transmissão. [p=0.2] {a}Uma usina manda cem quilowatts por uma linha com resistência de cinco ohms. [p=0.3] {b}Com mil volts, a corrente é cem mil dividido por mil: [p=0.1] cem ampères. [p=0.3] {c}A perda é cinco vezes cem ao quadrado: [p=0.2] {d}cinquenta mil watts. [p=0.2] {e}Metade da energia vira calor no caminho."),
    dict(id="s11", block="linha", text="Agora, {a}com dez mil volts. [p=0.2] {b}A corrente cai para dez ampères. [p=0.3] {c}A perda é cinco vezes dez ao quadrado: [p=0.1] {d}quinhentos watts. [p=0.3] {e}A tensão subiu dez vezes, [p=0.1] e a perda caiu cem vezes."),
    dict(id="s12", block="linha", text="Por isso, {a}perto da usina, um transformador sobe a tensão. [p=0.2] {b}A energia viaja com corrente pequena. [p=0.2] {c}E perto da sua casa, outros transformadores, como o do poste, baixam a tensão de novo."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o transformador que sobe a tensão aumenta a potência. [p=0.3] {b}A tensão sobe dez vezes, [p=0.1] e a corrente cai dez vezes. [p=0.3] {c}O produto, que é a potência, fica igual. [p=0.2] {d}Na vida real, até perde um pouco no ferro e nos fios."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}A tensão segue as espiras: [p=0.1] {b}dez vezes mais espiras, dez vezes mais tensão. [p=0.3] {c}A corrente vai ao contrário: [p=0.1] {d}dez vezes menos corrente."),
    dict(id="s15", block="atalho", text="E a perda vai com o quadrado da corrente. [p=0.2] Então, {a}multiplique a tensão por um número, [p=0.2] e {b}a perda fica dividida por esse número ao quadrado. [p=0.3] {c}Tensão vezes dez, perda dividida por cem. [p=0.3] {d}Isso vale para a mesma potência e a mesma linha: [p=0.2] se a questão mudar a potência, faça a conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Na saída de uma usina, um transformador tem duzentas espiras na primária [p=0.1] e quatro mil na secundária. [p=0.3] {b}A primária recebe onze mil volts. [p=0.3] {c}Qual é a tensão na linha? [p=0.3] E mais: {d}comparando com mandar a energia direto com onze mil volts, quantas vezes a perda cai?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Quatro mil dividido por duzentos: [p=0.1] {b}a secundária tem vinte vezes mais espiras. [p=0.3] {c}Onze mil vezes vinte: [p=0.1] {d}duzentos e vinte mil volts."),
    dict(id="s19", block="resposta", text="{a}Tensão vinte vezes maior, [p=0.1] {b}corrente vinte vezes menor. [p=0.3] {c}A perda cai vinte ao quadrado: [p=0.2] {d}quatrocentas vezes."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a tensão segue as espiras, [p=0.2] {b}a potência que entra é a que sai, [p=0.2] e {c}tensão alta deixa a corrente pequena e a perda menor. [p=0.3] Na próxima aula, {d}você pratica tudo do magnetismo e da indução em questões."),
    dict(id="s21", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
