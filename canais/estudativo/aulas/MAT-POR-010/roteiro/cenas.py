# Estudativo · MAT-POR-010 — Aumentos e descontos sucessivos (Matemática · Porcentagem).
# Habilidade: achar que 10% seguido de 20% dão 32% de aumento, e não 30%, e que subir 20% e cair 20% deixa o valor 4% menor.
# Pré-requisitos: MAT-POR-004 (fatores de aumento e de desconto), MAT-FRA-016 (multiplicar decimais). Próxima: MAT-POR-011.
# Questão inédita, criada para esta aula. Sem variação percentual (MAT-POR-005 fora desta cadeia): o resultado é lido no fator.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Aumentos e descontos sucessivos"

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
    dict(id="s01", block="gancho", text="Um produto {a}subiu dez por cento em um mês [p=0.2] e {b}vinte por cento no mês seguinte. [p=0.3] Subiu trinta por cento no total? [p=0.3] {c}Não. Subiu trinta e dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai juntar aumentos e descontos seguidos sem cair nessa, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] {b}Os fatores: somar quinze por cento é multiplicar por um vírgula quinze, [p=0.2] e tirar vinte por cento é multiplicar por zero vírgula oito. [p=0.3] E {c}multiplicar números com vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # com cem reais
    dict(id="s04", block="cem", text="Veja com um preço de {a}cem reais. [p=0.2] {b}Dez por cento de cem é dez: [p=0.1] o preço vai para {c}cento e dez."),
    dict(id="s05", block="cem", text="O segundo aumento é de vinte por cento, {a}só que sobre cento e dez, e não sobre cem. [p=0.2] {b}Vinte por cento de cento e dez: vinte e dois. [p=0.2] O preço vai para {c}cento e trinta e dois. [p=0.3] São {d}trinta e dois reais a mais em cada cem: trinta e dois por cento."),
    # fatores
    dict(id="s06", block="fatores", text="Com os fatores, a conta é direta. [p=0.2] {a}Dez por cento a mais, fator um vírgula um. [p=0.2] {b}Vinte por cento a mais, fator um vírgula dois. [p=0.3] Cada aumento multiplica o preço, então {c}multiplique os fatores: [p=0.2] {d}um vírgula um vezes um vírgula dois dá um vírgula trinta e dois."),
    dict(id="s07", block="fatores", text="E como se lê um vírgula trinta e dois? [p=0.2] {a}O um é o preço inteiro. [p=0.2] {b}O zero vírgula trinta e dois é o que veio a mais: [p=0.1] {c}trinta e dois por cento de aumento."),
    # sobe e desce
    dict(id="s08", block="sobedesce", text="O caso que mais engana é {a}subir vinte por cento e depois cair vinte por cento. [p=0.3] Parece que volta ao mesmo preço. [p=0.2] Multiplique os fatores: {b}um vírgula dois vezes zero vírgula oito dá [p=0.1] {c}zero vírgula noventa e seis."),
    dict(id="s09", block="sobedesce", text="Fator menor que um é desconto. [p=0.2] {a}Zero vírgula noventa e seis é ficar com noventa e seis por cento: [p=0.2] {b}o preço termina quatro por cento menor. [p=0.3] Com cem reais: {c}sobe para cento e vinte. [p=0.2] {d}Vinte por cento de cento e vinte são vinte e quatro, [p=0.2] e o preço cai para {e}noventa e seis."),
    dict(id="s10", block="sobedesce", text="E a ordem não importa: {a}cair vinte e depois subir vinte também termina em noventa e seis. [p=0.2] Na multiplicação, {b}a ordem não muda o resultado."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}somar as porcentagens. [p=0.2] Dez mais vinte dá {b}trinta. [p=0.2] Vinte menos vinte dá {c}zero. [p=0.3] Só que {d}cada porcentagem vale sobre o preço daquele momento, [p=0.2] e o preço já tinha mudado."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para duas variações. [p=0.2] {a}Some as porcentagens [p=0.2] e {b}some também uma vezes a outra, dividido por cem. [p=0.3] {c}Dez mais vinte dá trinta. [p=0.2] {d}Dez vezes vinte dá duzentos, dividido por cem dá dois. [p=0.2] Total: {e}trinta e dois por cento."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o segundo aumento também vale sobre o primeiro: [p=0.2] vinte por cento dos dez reais de aumento são {b}os dois reais extras. [p=0.3] Desconto entra {c}com sinal de menos. [p=0.2] Vinte menos vinte dá zero. [p=0.2] {d}Vinte vezes menos vinte, dividido por cem, menos quatro. [p=0.2] {e}Quatro por cento a menos."),
    dict(id="s14", block="atalho", text="Não compensa com {a}três variações ou mais: [p=0.2] aí, {b}multiplique os fatores."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma loja {a}aumentou um preço em vinte e cinco por cento. [p=0.2] Depois, anunciou {b}vinte por cento de desconto. [p=0.3] {c}O cliente paga mais, menos ou o mesmo que antes do aumento?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Os fatores são {a}um vírgula vinte e cinco e zero vírgula oito. [p=0.2] Sem as vírgulas, {b}cento e vinte e cinco vezes oito dá mil. [p=0.2] Com três casas, {c}um vírgula zero zero zero: [p=0.1] exatamente um. [p=0.3] Fator um não muda nada: {d}o cliente paga o mesmo preço de antes."),
    dict(id="s18", block="resposta", text="Pelo atalho: {a}vinte e cinco menos vinte dá cinco. [p=0.2] {b}Vinte e cinco vezes menos vinte, dividido por cem, menos cinco. [p=0.2] {c}Cinco menos cinco dá zero. [p=0.3] Quem somou achou {d}cinco por cento a mais, e errou."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}porcentagens seguidas não se somam. [p=0.2] {b}Multiplique os fatores e leia o resultado."),
    dict(id="s20", block="fim", text="Repare no teste: {a}subir vinte e cinco e cair vinte se desfazem. [p=0.2] Na próxima aula, você descobre {b}quanto um valor precisa subir para voltar ao que era, depois de uma queda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
