# Estudativo · MAT-TOP-006 — Praticando: binômio, binomial e contagem (Matemática · Tópicos Avançados · prática).
# Habilidade: expandir binômios, calcular chances de exatamente k sucessos e usar casa dos pombos e inclusão-exclusão.
# Pré-requisitos: MAT-TOP-001, MAT-TOP-002, MAT-TOP-003, MAT-TOP-004, MAT-TOP-005, MAT-TOP-019. Próxima: MAT-TOP-007.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Situação 5 (combinação com repetição, MAT-TOP-019): resolvida pelo método das bolinhas e barras (mesmo nome da MAT-TOP-019), que dá o binomial de
# (bolinhas + barras) sobre (bolinhas).

TITULO = "Praticando: binômio, binomial e contagem"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de contagem, [p=0.2] criadas para esta aula: [p=0.2] {b}binômio, chance, pombos, conjuntos e escolhas com repetição. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}cinco ferramentas: [p=0.2] {b}o termo geral do binômio; [p=0.2] {c}o binomial vezes a chance de uma ordem; [p=0.2] {d}o pior caso mais um; [p=0.2] {e}somar os conjuntos e tirar o repetido; [p=0.2] e {f}as bolinhas e barras. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: binômio
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Em {b}xis mais dois, elevado a cinco, [p=0.2] {c}qual é o coeficiente de xis?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] O expoente do xis é {a}cinco menos cá. [p=0.2] Para dar um, {b}cá vale quatro: [p=0.2] o dois foi escolhido quatro vezes. [p=0.3] {c}Binomial de cinco sobre quatro é cinco. [p=0.2] {d}Dois elevado a quatro é dezesseis. [p=0.2] {e}Cinco vezes dezesseis: oitenta. [p=0.3] Quem copiou só o cinco do triângulo {f}esqueceu o dois elevado."),
    # situação 2: distribuição binomial
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Um casal planeja {b}quatro filhos. [p=0.2] Supondo chance de um meio para menina em cada nascimento, [p=0.2] {c}qual a chance de nascerem exatamente duas meninas?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] A chance é um meio, então vale o atalho da moeda: [p=0.2] {a}a linha quatro do triângulo, um, quatro, seis, quatro, um, [p=0.2] dividida por {b}dois elevado a quatro, dezesseis. [p=0.3] Duas meninas é a posição dois: {c}seis dezesseis avos. [p=0.2] Simplificando por dois: {d}três oitavos, trinta e sete e meio por cento."),
    dict(id="s09", block="resposta2", text="Duas meninas e dois meninos é {a}o resultado mais provável: [p=0.2] seis é o maior número da linha. [p=0.3] Mas a chance dele {b}não chega à metade: [p=0.2] são três oitavos, porque {c}os outros resultados, juntos, somam mais."),
    # situação 3: casa dos pombos
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Existem {b}doze signos. [p=0.2] Quantas pessoas, no mínimo, garantem {c}quatro com o mesmo signo?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] As casinhas são {a}os doze signos. [p=0.2] Pior caso: {b}três pessoas em cada signo, sem passar de três. [p=0.2] {c}Doze vezes três, trinta e seis pessoas, e nenhum quarteto. [p=0.2] {d}A próxima fecha o quarteto: trinta e sete. [p=0.3] Quem fez doze vezes quatro e respondeu {e}quarenta e oito, garantiu, mas não achou o mínimo."),
    # situação 4: inclusão-exclusão
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] De um a cento e vinte, [p=0.2] quantos números {b}não são múltiplos de dois nem de três?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] Primeiro, quem é múltiplo de dois ou de três. [p=0.2] {a}Cento e vinte dividido por dois: sessenta. [p=0.2] {b}Por três: quarenta. [p=0.2] {c}Os dois ao mesmo tempo, pelo MMC seis: vinte. [p=0.3] {d}Sessenta mais quarenta, menos vinte: oitenta."),
    dict(id="s16", block="resposta4", text="A pergunta é quem {a}não está em nenhum dos dois. [p=0.2] {b}Cento e vinte menos oitenta: quarenta números. [p=0.3] Confira pelo atalho do bloco de seis: [p=0.2] em cada seis números, {c}só dois escapam, o um e o cinco. [p=0.2] {d}Cento e vinte tem vinte blocos de seis, e vinte vezes dois dá quarenta. [p=0.2] Bateu."),
    # situação 5: combinação com repetição
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] Uma sorveteria tem {b}cinco sabores. [p=0.2] Você monta {c}uma casquinha com duas bolas, podendo repetir o sabor, [p=0.2] e a ordem das bolas não importa. [p=0.3] {d}Quantas casquinhas diferentes existem?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] Pode repetir e a ordem não importa: {a}combinação com repetição. [p=0.3] Desenhe {b}duas bolinhas, uma para cada bola de sorvete, [p=0.2] e {c}quatro barras, que dividem os cinco sabores. [p=0.3] São {d}seis lugares, e você escolhe onde ficam as duas bolinhas: [p=0.2] {e}binomial de seis sobre dois, quinze casquinhas."),
    dict(id="s20", block="resposta5", text="Confira contando: [p=0.2] {a}com dois sabores diferentes, binomial de cinco sobre dois, dez. [p=0.2] {b}Com o mesmo sabor duas vezes, cinco. [p=0.2] {c}Dez mais cinco, quinze. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o binomial conta escolhas, abre binômios e calcula chances; [p=0.2] {b}o pior caso garante repetições; [p=0.2] e {c}tirar o repetido evita contar duas vezes."),
    dict(id="s22", block="fim", text="Na próxima aula, o assunto muda: [p=0.2] você calcula {a}a distância de um ponto até uma reta, [p=0.2] com uma fórmula de uma linha. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
