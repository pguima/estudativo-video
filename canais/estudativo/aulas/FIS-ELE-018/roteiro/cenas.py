# Estudativo · FIS-ELE-018 — Consumo em kWh e conta de luz (Física · Eletricidade · Potência elétrica e conta de luz).
# Habilidade: calcular E = P·Δt em kWh, converter em reais e somar o consumo mensal de vários aparelhos.
# Pré-requisitos: FIS-ELE-017 (potência elétrica). Próxima: FIS-ELE-019.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# MAT-LEI-005 (conta por faixas) NÃO está em "Já ensinado": tarifa única, de exemplo (R$ 0,80/kWh), sem bandeiras nem impostos.
# Hora decimal (MAT-MED-006) está em "Já ensinado". Geladeira: consumo mensal lido na etiqueta (25 kWh/mês, valor de exemplo).
# Contas: 4.000 W = 4 kW; 4·0,5 = 2 kWh/dia; 2·30 = 60 kWh; 60·0,8 = R$ 48; TV 0,1·5·30 = 15 kWh; 0,1·5 = 0,5 kWh/dia (2/0,5 = 4×);
#   60 + 15 + 25 = 100 kWh; 100·0,8 = R$ 80; 1 kWh = 1.000·3.600 = 3.600.000 J = 3,6·10⁶ J.
#   Erro: 4.000·0,5·30 = 60.000 (Wh); 60.000·0,8 = 48.000. Atalho: 4 kW·0,5 h = 2 kWh = 0,1 kW·20 h; 4.000/100 = 40; 20/0,5 = 40.
#   Medidor: 4.620 − 4.520 = 100 kWh. Questão: 1,5·2 = 3 kWh/dia; 3·30 = 90 kWh; 90·0,8 = R$ 72.

TITULO = "Consumo em kWh e conta de luz"

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
    dict(id="s01", block="gancho", text="{a}Um chuveiro de quatro mil watts, ligado meia hora por dia, [p=0.2] ou {b}uma TV de cem watts, ligada cinco horas por dia: [p=0.2] qual pesa mais na conta de luz? [p=0.3] {c}O chuveiro, [p=0.1] e gasta {d}quatro vezes mais."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o consumo em quilowatt-hora, [p=0.2] {b}transformar em reais [p=0.1] e {c}somar a conta do mês."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}potência é energia dividida pelo tempo, em watt, e um quilowatt é mil watts; [p=0.2] e {c}hora decimal: trinta minutos são zero vírgula cinco hora. [p=0.3] Se faltar alguma, procure no canal."),
    # energia
    dict(id="s04", block="energia", text="Se potência é energia dividida pelo tempo, [p=0.2] então {a}energia é potência vezes tempo. [p=0.3] {b}No Sistema Internacional, watt vezes segundo dá joule. [p=0.2] {c}Mas um chuveiro ligado meia hora gasta milhões de joules: [p=0.2] número grande demais para uma conta de luz."),
    dict(id="s05", block="energia", text="Por isso, a conta usa outra unidade: [p=0.2] {a}o quilowatt-hora. [p=0.3] {b}Potência em quilowatt, [p=0.1] {c}tempo em hora, [p=0.2] e {d}a energia sai direto em quilowatt-hora. [p=0.3] {e}Um quilowatt-hora é um aparelho de mil watts ligado durante uma hora."),
    dict(id="s06", block="energia", text="Em joules, {a}um quilowatt-hora é mil watts vezes três mil e seiscentos segundos: [p=0.2] {b}três milhões e seiscentos mil joules. [p=0.2] {c}Três vírgula seis vezes dez elevado a seis."),
    # o chuveiro
    dict(id="s07", block="conta", text="Vamos ao chuveiro. [p=0.2] {a}Quatro mil watts são quatro quilowatts. [p=0.2] {b}Meia hora por dia é zero vírgula cinco hora. [p=0.3] {c}Quatro vezes zero vírgula cinco: dois quilowatts-hora por dia. [p=0.2] {d}Em trinta dias: sessenta quilowatts-hora."),
    dict(id="s08", block="conta", text="{a}A conta multiplica o consumo pela tarifa, o preço de cada quilowatt-hora. [p=0.2] Com uma tarifa de exemplo de {b}oitenta centavos, ou zero vírgula oito real: [p=0.2] {c}sessenta vezes zero vírgula oito, [p=0.1] {d}quarenta e oito reais por mês, só no banho."),
    # a casa
    dict(id="s09", block="casa", text="Para a casa toda, {a}calcule cada aparelho e some. [p=0.2] {b}A TV de cem watts, cinco horas por dia: [p=0.1] zero vírgula um vezes cinco vezes trinta, {c}quinze quilowatts-hora. [p=0.3] {d}A geladeira liga e desliga sozinha: [p=0.1] o consumo dela vem na etiqueta, por exemplo {e}vinte e cinco quilowatts-hora por mês."),
    dict(id="s10", block="casa", text="{a}Sessenta mais quinze mais vinte e cinco: cem quilowatts-hora. [p=0.2] {b}Vezes oitenta centavos: oitenta reais."),
    dict(id="s11", block="casa", text="{a}Na conta de verdade, o consumo vem do medidor, o relógio de luz, que conta quilowatts-hora. [p=0.2] {b}A leitura de um mês menos a do mês anterior é o consumo. [p=0.3] {c}Quatro mil seiscentos e vinte menos quatro mil quinhentos e vinte: [p=0.1] {d}cem quilowatts-hora."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer de passar o watt para quilowatt. [p=0.3] {b}Quatro mil vezes zero vírgula cinco vezes trinta dá sessenta mil. [p=0.2] Se isso fosse quilowatt-hora, {c}o banho custaria quarenta e oito mil reais por mês. [p=0.3] {d}Sessenta mil é watt-hora: [p=0.1] divida por mil, {e}sessenta quilowatts-hora."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho para comparar aparelhos: [p=0.2] {a}o que pesa na conta é potência vezes tempo, [p=0.1] não a potência sozinha. [p=0.3] {b}Quatro mil watts por meia hora, [p=0.1] ou {c}a mesma TV de cem watts, por vinte horas: [p=0.2] {d}os dois dão dois quilowatts-hora. [p=0.3] {e}Potência quarenta vezes maior, tempo quarenta vezes menor: [p=0.1] o mesmo gasto."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a energia é proporcional à potência e ao tempo. [p=0.2] {b}Por isso, o chuveiro, muito potente, e a geladeira, ligada o mês inteiro, costumam pesar na conta. [p=0.3] E não confunda: {c}quilowatt é potência; [p=0.1] {d}quilowatt-hora é energia."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um aquecedor de {a}mil e quinhentos watts fica ligado {b}duas horas por dia, [p=0.1] durante {c}trinta dias. [p=0.3] Com a tarifa de {d}oitenta centavos por quilowatt-hora, [p=0.1] {e}quanto ele custa no mês?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Mil e quinhentos watts: um vírgula cinco quilowatt. [p=0.2] {b}Vezes duas horas: três quilowatts-hora por dia. [p=0.2] {c}Vezes trinta dias: noventa quilowatts-hora. [p=0.3] {d}Noventa vezes zero vírgula oito: [p=0.1] {e}setenta e dois reais."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}energia é potência vezes tempo; [p=0.2] {b}com quilowatt e hora, ela sai em quilowatt-hora; [p=0.2] e {c}a conta é o consumo vezes a tarifa, somando cada aparelho."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai descobrir {a}por que o chuveiro na posição inverno tem resistência menor, [p=0.2] e {b}qual lâmpada brilha mais, em série e em paralelo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
