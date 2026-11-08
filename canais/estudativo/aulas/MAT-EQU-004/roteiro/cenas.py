# Estudativo · MAT-EQU-004 — Distributiva e sinal de menos antes do parêntese (Matemática · Equações do 1º Grau).
# Habilidade: abrir −2(x − 5) e simplificar 5 − (x − 3) sem errar o sinal.
# Pré-requisitos: MAT-EQU-003 (juntar termos semelhantes), MAT-NUM-017 (regra de sinais). Próxima: MAT-EQU-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Preço do suco inventado para a conta. Sem potência: fora da ficha.
# 3(x + 4) = 3x + 12 (x = 10: 42) · −2(x − 5) = −2x + 10 (x = 10: −10; erro −2x − 5 = −25).
# 5 − (x − 3) = 8 − x (x = 10: −2; erro 5 − x − 3 = 2 − x = −8).
# Questão: 3(x + 2) − (x − 4) = 2x + 10 (x = 10: 30); sem trocar o 4: 2x + 2.

TITULO = "Distributiva e sinal de menos antes do parêntese"

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
    dict(id="s01", block="gancho", text="{a}Cinco menos, abre parênteses, xis menos três, fecha parênteses. [p=0.3] Se você apagou os parênteses e escreveu {b}cinco menos xis menos três, [p=0.2] errou um sinal. [p=0.3] O certo é {c}oito menos xis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você abre parênteses sem errar o sinal, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}Regra de sinais: multiplicando, sinais iguais dão mais, e sinais diferentes dão menos. [p=0.3] E {c}juntar termos semelhantes: xis com xis, número com número. [p=0.3] Se faltar alguma, procure no canal."),
    # distributiva
    dict(id="s04", block="combo", text="{a}Três amigos pedem o mesmo combo: [p=0.2] {b}um lanche de xis reais [p=0.2] e {c}um suco de quatro reais. [p=0.3] A conta é {d}três, abre parênteses, xis mais quatro, fecha parênteses. [p=0.2] Entre o três e o parêntese, {e}o vezes está escondido."),
    dict(id="s05", block="combo", text="Três combos são {a}três lanches e três sucos: [p=0.2] {b}três xis mais doze. [p=0.3] Cada amigo leva o lanche e o suco, [p=0.2] então nada fica de fora da conta. [p=0.3] O número de fora {c}multiplica cada termo de dentro. [p=0.2] Isso se chama {d}propriedade distributiva."),
    dict(id="s06", block="combo", text="Teste com {a}um lanche de dez reais. [p=0.2] Pelo parêntese: {b}dez mais quatro dá catorze, [p=0.2] e {c}catorze vezes três dá quarenta e dois. [p=0.2] Aberto: {d}trinta mais doze, também quarenta e dois. [p=0.2] {e}Bateu."),
    # com sinal de menos
    dict(id="s07", block="negativo", text="Com sinal de menos, a ideia é a mesma, [p=0.2] com a regra de sinais em cada termo. [p=0.2] {a}Menos dois, abre parênteses, xis menos cinco, fecha parênteses. [p=0.3] {b}Menos dois vezes xis: menos dois xis. [p=0.2] {c}Menos dois vezes menos cinco: sinais iguais, mais dez. [p=0.3] Resultado: {d}menos dois xis mais dez."),
    dict(id="s08", block="negativo", text="Confira com xis igual a dez. [p=0.2] {a}Dez menos cinco dá cinco [p=0.2] e menos dois vezes cinco dá {b}menos dez. [p=0.2] Aberto: {c}menos vinte mais dez, também menos dez. [p=0.3] O menos dois de fora {d}alcança o xis e também o cinco."),
    # menos sozinho
    dict(id="s09", block="menos", text="E quando o menos está sozinho na frente do parêntese? [p=0.2] Volte ao começo: {a}cinco menos, abre parênteses, xis menos três, fecha parênteses. [p=0.3] Só com números, você faria primeiro a conta de dentro. [p=0.2] Aqui não dá: o xis é desconhecido. [p=0.3] Então use o que esse menos faz: tira {b}o parêntese inteiro. [p=0.2] Tira o xis [p=0.2] e {c}tira também o menos três."),
    dict(id="s10", block="menos", text="Tirar o xis é {a}menos xis. [p=0.2] Tirar menos três é tirar uma dívida, [p=0.2] e tirar uma dívida é como ganhar: {b}mais três. [p=0.3] Fica {c}cinco menos xis mais três. [p=0.2] Juntando os números soltos: {d}oito menos xis."),
    dict(id="s11", block="menos", text="Aquele cinco menos xis menos três do começo {a}deixou o três de fora: [p=0.2] o menos tirou só o xis. [p=0.3] Com xis igual a dez, o certo dá {b}menos dois, [p=0.2] e a versão errada dá {c}menos oito."),
    # erro
    dict(id="s12", block="erro", text="Outro erro comum: [p=0.2] {a}multiplicar só o primeiro termo. [p=0.2] Em menos dois, abre parênteses, xis menos cinco, fecha parênteses, [p=0.2] a pessoa escreve {b}menos dois xis menos cinco. [p=0.3] O cinco ficou {c}sem ser multiplicado. [p=0.2] Com dez no lugar do xis, isso dá {d}menos vinte e cinco, [p=0.2] e o certo é {e}menos dez."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}menos sozinho na frente do parêntese troca todos os sinais de dentro. [p=0.3] {b}Xis vira menos xis. [p=0.2] {c}Menos três vira mais três. [p=0.2] E {d}o parêntese some."),
    dict(id="s14", block="atalho", text="Funciona porque {a}esse menos é o mesmo que menos um vezes o parêntese. [p=0.2] Multiplicar por menos um {b}só troca o sinal. [p=0.3] {c}Com número na frente, como menos dois, não basta trocar: [p=0.2] tem que multiplicar também. [p=0.2] E {d}com mais na frente, nada muda: [p=0.2] é só apagar o parêntese. [p=0.3] No começo da aula, {e}xis menos três com o menos na frente [p=0.2] vira {f}menos xis mais três, direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Simplifique: {a}três, abre parênteses, xis mais dois, fecha parênteses, [p=0.2] {b}menos, abre parênteses, xis menos quatro, fecha parênteses."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Primeiro parêntese: {a}três xis mais seis. [p=0.2] Segundo, com o atalho: {b}menos xis mais quatro. [p=0.3] Junte: {c}três xis menos xis dá dois xis. [p=0.2] {d}Seis mais quatro dá dez. [p=0.3] Resposta: {e}dois xis mais dez."),
    dict(id="s18", block="resposta", text="Confira com dez: [p=0.2] {a}trinta e seis menos seis dá trinta. [p=0.2] {b}Dois vezes dez mais dez também. [p=0.3] Quem esqueceu de trocar o sinal do quatro chegou em {c}dois xis mais dois."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o número de fora multiplica cada termo de dentro, [p=0.2] e {b}menos sozinho troca todos os sinais."),
    dict(id="s20", block="fim", text="Na próxima aula, você multiplica {a}letra por letra, [p=0.2] como {b}três xis vezes dois xis, [p=0.2] e abre {c}dois parênteses multiplicados. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
