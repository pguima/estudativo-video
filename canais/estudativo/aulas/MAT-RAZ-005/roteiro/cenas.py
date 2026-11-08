# Estudativo · MAT-RAZ-005 — Direta, inversa ou nenhuma: o teste do dobro (Matemática · Razão e Proporção).
# Habilidade: decidir o tipo de relação dobrando uma grandeza e explicar por que a corrida de táxi com bandeirada não é proporcional.
# Pré-requisitos: MAT-RAZ-004 (grandezas direta e inversamente proporcionais). Próxima: MAT-RAZ-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Valores do táxi e da academia são inventados, não preços reais.
# Divisão com resultado decimal (MAT-FRA-017) não está na cadeia: o táxi é decidido só pelo dobro.

TITULO = "Direta, inversa ou nenhuma: o teste do dobro"

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
    dict(id="s01", block="gancho", text="Numa cidade inventada, uma corrida de táxi de {a}dois quilômetros custa onze reais. [p=0.3] Então uma de quatro quilômetros custa {b}vinte e dois? [p=0.3] Não. [p=0.2] Custa {c}dezessete. [p=0.3] A distância dobrou, e o preço {d}não dobrou."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você decide em segundos se duas grandezas são proporcionais, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}na direta, a divisão não muda; [p=0.2] {c}na inversa, o produto não muda. [p=0.3] Se faltar essa aula, procure no canal."),
    # teste
    dict(id="s04", block="teste", text="Este é o teste do dobro: {a}dobre uma grandeza e olhe a outra. [p=0.3] A outra tem {b}três saídas possíveis."),
    dict(id="s05", block="teste", text="{a}Primeira: a outra também dobra. [p=0.2] É {b}direta. [p=0.2] Um quilo de feijão, oito reais. [p=0.2] Dois quilos, {c}dezesseis. [p=0.3] Se o preço do quilo não muda, {d}o dobro de quilos custa o dobro."),
    dict(id="s06", block="teste", text="{a}Segunda: a outra cai pela metade. [p=0.2] É {b}inversa. [p=0.2] Na viagem de cento e vinte quilômetros, a trinta por hora você leva quatro horas. [p=0.2] A sessenta, {c}duas horas. [p=0.3] Para o produto continuar cento e vinte, {d}se um dobra, o outro tem que cair pela metade."),
    dict(id="s07", block="teste", text="{a}Terceira: nem dobra, nem cai pela metade. [p=0.2] Aí {b}não é direta nem inversa. [p=0.3] E o dobro é só o mais fácil de imaginar: [p=0.2] {c}com o triplo, o teste funciona igual. [p=0.3] Um cuidado: {d}mude só uma grandeza e deixe o resto da situação igual. [p=0.2] Na viagem, a distância continua cento e vinte quilômetros."),
    # táxi
    dict(id="s08", block="taxi", text="Agora, o táxi. [p=0.2] Ele cobra {a}uma bandeirada de cinco reais: [p=0.2] um valor fixo, pago assim que você entra, mesmo sem andar nada. [p=0.2] Ela não depende da distância. [p=0.3] Depois, {b}três reais por quilômetro."),
    dict(id="s09", block="taxi", text="Dois quilômetros: {a}cinco mais seis dá onze reais. [p=0.2] Quatro quilômetros: {b}cinco mais doze dá dezessete reais. [p=0.3] A parte dos quilômetros dobrou, {c}de seis para doze. [p=0.2] Mas {d}a bandeirada continuou cinco."),
    dict(id="s10", block="taxi", text="É por isso que a corrida {a}não é proporcional à distância: [p=0.2] {b}tem um pedaço do preço que não acompanha os quilômetros. [p=0.3] Sempre que aparecer {c}taxa fixa, matrícula ou bandeirada, [p=0.2] desconfie."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é pensar: {a}um sobe, o outro desce, então é inversa. [p=0.3] Uma vela de {b}vinte centímetros queima dois centímetros por hora. [p=0.2] Depois de duas horas, {c}dezesseis centímetros. [p=0.2] Depois de quatro horas, {d}doze."),
    dict(id="s12", block="erro", text="O tempo dobrou. [p=0.2] Se fosse inversa, a vela teria {a}caído pela metade, para oito. [p=0.2] Ficou com doze. [p=0.3] {b}Não é inversa, nem direta. [p=0.2] O tempo sobe e a vela desce, {c}mas só descer não basta. [p=0.3] O produto também denuncia: {d}duas vezes dezesseis dá trinta e dois. [p=0.2] {e}Quatro vezes doze dá quarenta e oito. [p=0.2] Mudou."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido: {a}o teste do zero. [p=0.3] Na direta, {b}zero de um dá zero do outro: [p=0.2] zero quilo de feijão, zero real. [p=0.3] O táxi com {c}zero quilômetro custa cinco reais. [p=0.2] {d}Não é direta, sem fazer conta nenhuma. [p=0.3] A vela também cai nesse teste: [p=0.2] {e}com zero hora acesa, ela tem vinte centímetros."),
    dict(id="s14", block="atalho", text="Funciona porque na direta {a}uma grandeza é a outra vezes um número fixo, [p=0.2] e zero vezes qualquer número dá zero. [p=0.3] Não compensa para {b}descobrir se é inversa: [p=0.2] o zero só descarta a direta. [p=0.2] Para o resto, {c}dobre."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Diga se é direta, inversa ou nenhuma. [p=0.3] {a}Primeiro: o número de ingressos iguais comprados e o valor total pago. [p=0.2] {b}Segundo: o número de pessoas que dividem igualmente uma conta de cento e vinte reais, e quanto cada uma paga. [p=0.2] {c}Terceiro: uma academia com matrícula de cinquenta reais e mensalidade de oitenta, e o total pago em cada número de meses."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá, dobrando. [p=0.2] {a}No primeiro, o preço de cada ingresso não muda, [p=0.2] então o dobro de ingressos custa o dobro: direta. [p=0.3] {b}No segundo, duas pessoas pagam sessenta cada. [p=0.2] Quatro pessoas, trinta cada. [p=0.2] Caiu pela metade: {c}inversa."),
    dict(id="s18", block="resposta", text="{a}No terceiro, um mês sai cinquenta mais oitenta dá cento e trinta. [p=0.2] {b}Dois meses, cinquenta mais cento e sessenta dá duzentos e dez. [p=0.3] O dobro de cento e trinta seria duzentos e sessenta. [p=0.2] {c}Nenhuma: a matrícula faz o papel da bandeirada."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}dobrou junto, direta. [p=0.2] {b}Caiu pela metade, inversa. [p=0.2] {c}Nenhum dos casos, não é direta nem inversa."),
    dict(id="s20", block="fim", text="Na próxima aula, a {a}regra de três direta: [p=0.2] se {b}três quilos custam dezoito reais, quanto custam sete? [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
