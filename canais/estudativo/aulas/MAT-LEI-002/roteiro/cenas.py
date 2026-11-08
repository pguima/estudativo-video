# Estudativo · MAT-LEI-002 — Palavras que mudam a conta (Matemática · Leitura de Problemas).
# Habilidade: traduzir 'a mais que', 'do restante' e 'no mínimo' para a conta certa, como 3 a mais que x e 1/4 do restante.
# Pré-requisitos: MAT-EQU-001 (letra no lugar de um número), MAT-FRA-010 (fração do restante), MAT-LEI-001 (pergunta e dados úteis), MAT-POR-002 (porcentagem). Próxima: MAT-LEI-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.

TITULO = "Palavras que mudam a conta"

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
    dict(id="s01", block="gancho", text="Maria tem {a}xis reais. [p=0.2] João tem {b}três reais a mais que Maria. [p=0.3] Se você escreveu {c}três xis para o João, [p=0.2] trocou uma soma por uma multiplicação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você traduz três expressões que mudam a conta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de três coisas: [p=0.2] {a}a letra guarda o lugar de um número, [p=0.2] {b}antes de cada fração, pergunte fração de quê, [p=0.2] e {c}leia a pergunta primeiro. [p=0.3] Se faltar alguma, procure no canal."),
    # a mais que
    dict(id="s04", block="amais", text="Primeira expressão: {a}a mais que. [p=0.3] Ela compara duas quantidades. [p=0.2] A base é quem vem logo depois da expressão: [p=0.2] {b}aqui, a Maria. [p=0.2] O João tem o da Maria {c}e mais três."),
    dict(id="s05", block="amais", text="Então o João tem {a}xis mais três. [p=0.3] Se a Maria tem dez reais, ele tem {b}treze. [p=0.3] Com a menos que, o sentido vira: [p=0.2] três reais a menos que a Maria é {c}xis menos três."),
    dict(id="s06", block="amais", text="E três vezes o que a Maria tem? [p=0.2] Aí sim: {a}três xis. [p=0.3] {b}A mais soma. [p=0.2] {c}Vezes multiplica."),
    # do restante
    dict(id="s07", block="restante", text="Segunda expressão: {a}do restante, [p=0.2] ou do que sobrou. [p=0.3] Ela muda {b}o total da fração. [p=0.3] Uma pessoa tem {c}sessenta balas. [p=0.2] Dá {d}um terço para a Ana [p=0.2] e {e}um quarto do restante para a Bia."),
    dict(id="s08", block="restante", text="Um terço de sessenta: {a}vinte, para a Ana. [p=0.2] O restante é {b}quarenta. [p=0.3] E o um quarto é de quê? [p=0.2] Do restante. [p=0.2] {c}Um quarto de quarenta: dez balas para a Bia. [p=0.3] Sobram {d}trinta."),
    dict(id="s09", block="restante", text="Sem a palavra restante, a frase seria {a}um quarto das balas: [p=0.2] um quarto de sessenta, {b}quinze. [p=0.3] Uma palavra, e a Bia recebe {c}quinze balas em vez de dez. [p=0.3] Por isso, antes de cada fração, a pergunta de sempre: fração de quê?"),
    # no mínimo
    dict(id="s10", block="minimo", text="Terceira expressão: {a}no mínimo. [p=0.3] Um elevador leva {b}oito pessoas por viagem. [p=0.2] {c}Trinta pessoas precisam subir. [p=0.2] {d}No mínimo, quantas viagens ele faz?"),
    dict(id="s11", block="minimo", text="{a}Trinta dividido por oito dá três vírgula setenta e cinco. [p=0.3] Três viagens levam {b}vinte e quatro pessoas, e seis ficam esperando. [p=0.2] Então são {c}quatro viagens. [p=0.3] No mínimo pede {d}o menor número que ainda resolve tudo. [p=0.2] Com sobra, ele sobe, como nos ônibus da aula passada. [p=0.3] Se fossem {e}trinta e duas pessoas, seriam quatro viagens exatas, sem arredondar nada. [p=0.3] E {f}pelo menos funciona igual a no mínimo."),
    dict(id="s12", block="minimo", text="O par dele é {a}no máximo. [p=0.2] Com cem reais, quantos ingressos de doze reais, no máximo? [p=0.3] {b}Oito ingressos custam noventa e seis. [p=0.2] {c}Nove custariam cento e oito: não dá. [p=0.3] No máximo pede {d}o maior número que ainda cabe: [p=0.2] {e}oito."),
    # erro comum
    dict(id="s13", block="erro", text="O erro comum é o do começo: [p=0.2] {a}ler a mais que como vezes. [p=0.3] Três reais a mais não é o triplo. [p=0.2] Se a Maria tem dez, três xis daria {b}trinta para o João, [p=0.2] quando ele tem só {c}treze."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}na dúvida, troque a letra por dez e leia a frase de novo. [p=0.3] Se a Maria tem dez, três reais a mais que ela {b}são treze. [p=0.3] Teste as contas: {c}xis mais três dá treze, [p=0.2] e três xis dá trinta. [p=0.2] Só a primeira serve."),
    dict(id="s15", block="atalho", text="Funciona porque, com um número na mão, a frase vira uma situação do dia a dia, [p=0.2] e a conta errada {a}dá um valor que não bate. [p=0.3] Só não teste com o dois: o dobro dele e ele mais dois dão o mesmo quatro. [p=0.3] Não compensa quando a frase já vem na ordem da conta, como {b}um número mais três: [p=0.2] aí, escreva direto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma pessoa tem {a}noventa reais. [p=0.2] Gasta {b}um terço no mercado [p=0.1] e {c}um quarto do restante na farmácia. [p=0.3] Com o que sobrou, quer comprar camisetas de {d}vinte reais. [p=0.2] {e}No máximo, quantas ela compra?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Um terço de noventa, trinta reais. [p=0.2] Restante: {b}sessenta. [p=0.3] {c}Um quarto de sessenta, quinze reais. [p=0.2] Sobram {d}quarenta e cinco reais."),
    dict(id="s19", block="resposta", text="{a}Duas camisetas custam quarenta. [p=0.2] {b}Três custariam sessenta: não dá. [p=0.3] No máximo, {c}duas camisetas. [p=0.3] Quem tirou um quarto dos noventa ficou com {d}trinta e sete reais e cinquenta centavos, [p=0.2] e respondeu uma camiseta só."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a mais que soma à base, [p=0.2] {b}do restante muda o total, [p=0.2] {c}no mínimo pede o menor que resolve [p=0.2] e {d}no máximo, o maior que cabe. [p=0.3] São pistas: a história sempre confere."),
    dict(id="s21", block="fim", text="Na próxima aula, você resolve problemas {a}desenhando: [p=0.2] {b}barras para as frações [p=0.2] e {c}tabelas para testar opções, sem montar equação. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
