# Estudativo · MAT-POT-009 — Simplificar e somar radicais (Matemática · Potências e Raízes · Radiciação).
# Habilidade: calcular √2 · √8 = 4, escrever √72 como 6√2 e somar √8 + √18, sabendo que √2 + √3 não vira √5.
# Pré-requisitos: MAT-POT-004, MAT-POT-007. Próxima: MAT-POT-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# √4 · √9 = 2 · 3 = 6 = √36 · √2 · √8 = √16 = 4 · 72 = 2·2·2·3·3 → 2·3 = 6, sobra 2 → 6√2; 36 · 2 = 72.
# √8 = 2√2; √18 = 3√2; soma 5√2 · Erro: √36 + √64 = 14; √100 = 10 · √2 ≈ 1,4; √3 ≈ 1,7; soma ≈ 3,1; √5 ≈ 2,2.
# Atalho: 72 ÷ 36 = 2 → 6√2 · 1.008 = 2·2·2·2·3·3·7 → 12√7 (não dito). Só raiz quadrada: raiz cúbica e expoente fracionário não estão na ficha.
# Questão: √12 + √75 = 2√3 + 5√3 = 7√3 ≈ 12,1; erro √87 ≈ 9,3. Inédita.

TITULO = "Simplificar e somar radicais"

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
    dict(id="s01", block="gancho", text="{a}Raiz de dois não é exata. [p=0.2] {b}Raiz de oito também não. [p=0.3] Mas multiplique uma pela outra, e sai {c}quatro, certinho. [p=0.3] Na soma, a história muda."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você precisa de {a}raiz quadrada exata [p=0.2] e de {b}fatoração em primos. [p=0.3] Se faltar alguma, procure no canal. [p=0.3] E um nome: {c}radical é a raiz escrita com o símbolo, como {d}raiz de dois."),
    # multiplicar
    dict(id="s03", block="multiplicar", text="Comece com números fáceis: {a}raiz de quatro vezes raiz de nove. [p=0.2] A primeira dá dois e a segunda dá três. [p=0.2] Dois vezes três: {b}seis. [p=0.3] Junte tudo em uma raiz só: {c}raiz de trinta e seis. [p=0.2] Também {d}seis."),
    dict(id="s04", block="multiplicar", text="Essa é a regra: {a}raiz vezes raiz é a raiz da multiplicação. [p=0.3] Então {b}raiz de dois vezes raiz de oito é {c}raiz de dezesseis, [p=0.2] que dá {d}quatro. [p=0.3] Por quê? [p=0.2] Eleve raiz de dois vezes raiz de oito ao quadrado. [p=0.2] O expoente de fora vai para cada número da multiplicação, [p=0.2] e cada raiz, ao quadrado, devolve o número de dentro. [p=0.2] Sobra {e}dois vezes oito, que dá dezesseis. [p=0.2] Então essa multiplicação é o número positivo que, ao quadrado, dá dezesseis: quatro."),
    # simplificar
    dict(id="s05", block="simplificar", text="A regra também anda {a}ao contrário, e é assim que se simplifica. [p=0.2] Veja a {b}raiz quadrada de setenta e dois. [p=0.2] Fatorando: {c}dois vezes dois vezes dois vezes três vezes três."),
    dict(id="s06", block="simplificar", text="Procure as {a}duplas. [p=0.2] Uma {b}dupla de dois [p=0.2] e uma {c}dupla de três. [p=0.2] Cada dupla tem raiz exata, então {d}sai da raiz como um número só. [p=0.3] Sobrou {e}um número dois sem dupla: [p=0.2] ele {f}fica dentro."),
    dict(id="s07", block="simplificar", text="Fora da raiz: {a}dois vezes três dá seis. [p=0.2] Dentro: {b}dois. [p=0.3] Resultado: {c}seis raiz de dois. [p=0.2] Isso significa {d}seis vezes a raiz de dois, com o vezes escondido. [p=0.3] Se mais de um primo ficar sem dupla, todos continuam dentro, multiplicados. [p=0.2] E, sem nenhuma dupla, como em raiz de quinze, a raiz já está na forma mais simples."),
    dict(id="s08", block="simplificar", text="Conferindo: {a}seis ao quadrado dá trinta e seis. [p=0.2] {b}Raiz de dois ao quadrado dá dois. [p=0.2] {c}Trinta e seis vezes dois dá setenta e dois. [p=0.2] Bateu."),
    # somar
    dict(id="s09", block="somar", text="E somar? [p=0.2] Raiz exata vira número comum. [p=0.2] Raiz não exata só se junta com outra de {a}mesmo número dentro. [p=0.3] Pense em caixas: {b}duas caixas mais três caixas dá {c}cinco caixas. [p=0.2] Do mesmo jeito, {d}dois raiz de dois mais três raiz de dois dá {e}cinco raiz de dois."),
    dict(id="s10", block="somar", text="Só que {a}raiz de oito mais raiz de dezoito parece não ter nada igual. [p=0.2] Simplifique primeiro. [p=0.2] {b}Oito é dois vezes dois vezes dois: [p=0.2] vira {c}dois raiz de dois."),
    dict(id="s11", block="somar", text="{a}Dezoito é dois vezes três vezes três: [p=0.2] vira {b}três raiz de dois. [p=0.3] O número de dentro ficou igual, e a soma dá {c}cinco raiz de dois."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}somar o que está dentro. [p=0.2] Escrever {b}raiz de dois mais raiz de três igual a raiz de cinco. [p=0.3] Teste com raízes exatas: {c}raiz de trinta e seis mais raiz de sessenta e quatro é seis mais oito, que dá {d}catorze. [p=0.2] Somando dentro, daria {e}raiz de cem, que é dez. [p=0.2] Não bate."),
    dict(id="s13", block="erro", text="Nos valores aproximados, {a}raiz de dois é perto de um vírgula quatro [p=0.2] e {b}raiz de três é perto de um vírgula sete. [p=0.2] A soma dá {c}três vírgula um. [p=0.2] Só que {d}raiz de cinco é perto de dois vírgula dois. [p=0.3] Essa soma {e}fica como está. [p=0.3] E {f}raiz de oito mais raiz de dezoito também não vira raiz de vinte e seis: [p=0.2] esta dá perto de cinco, e a soma certa dá perto de sete."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}procure o maior quadrado que divide o número. [p=0.2] Quadrado aqui é o resultado de elevar ao quadrado, como nove ou trinta e seis. [p=0.3] {b}Setenta e dois dividido por trinta e seis dá dois. [p=0.2] Então é {c}raiz de trinta e seis vezes raiz de dois: [p=0.2] {d}seis raiz de dois, sem fatorar."),
    dict(id="s15", block="atalho", text="Funciona porque é a {a}regra do vezes, ao contrário. [p=0.3] Não compensa em número grande, como {b}raiz de mil e oito: [p=0.2] lá, o quadrado não salta aos olhos, e a {c}fatoração é mais segura."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Quanto dá raiz de doze mais raiz de setenta e cinco? [p=0.2] Deixe na forma mais simples."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Doze é quatro vezes três: {b}dois raiz de três. [p=0.2] {c}Setenta e cinco é vinte e cinco vezes três: {d}cinco raiz de três."),
    dict(id="s19", block="resposta", text="O número de dentro é igual, então some os de fora: {a}dois mais cinco dá sete. [p=0.2] Resposta: {b}sete raiz de três. [p=0.3] Quem soma direto escreve {c}raiz de oitenta e sete, que dá perto de nove. [p=0.2] O certo dá {d}perto de doze."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no vezes, tudo entra na mesma raiz. [p=0.2] {b}Simplificar é tirar as duplas. [p=0.2] E {c}raiz não exata só se soma com o mesmo número dentro."),
    dict(id="s21", block="fim", text="A próxima aula é {a}prática: [p=0.2] você vai calcular, estimar e simplificar raízes em {b}problemas de medida. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
