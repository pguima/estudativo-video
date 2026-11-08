# Estudativo · MAT-PRO-003 — Padrões que se repetem: o resto manda (Matemática · Progressões).
# Habilidade: achar a letra da posição 2.026 em A, B, C, D, A, B…, o dia da semana daqui a 100 dias só pelo resto da divisão e o dia em que dois ciclos de 12 e 18 dias voltam a coincidir.
# Pré-requisitos: MAT-DIV-007 (MMC: encontros que se repetem), MAT-NUM-010 (dividir por dois algarismos), MAT-PRO-001 (posição e termo). Próxima: MAT-PRO-004.
# Questão inédita, criada para esta aula. Divisão com resto narrada como na MAT-NUM-009 ("dá três, com resto dois"); divisibilidade por 4 pelos dois últimos algarismos, como na MAT-DIV-002.
# Letras: ciclo de 4 · 2.026 ÷ 4 = 506, resto 2 (4 × 506 = 2.024 → D) → B · 2.028 ÷ 4 = 507, resto 0 → D (erro: responder A).
# Dias: terça + 100 dias · 100 ÷ 7 = 14, resto 2 → quinta · daqui a 7 dias, mesmo dia (resto 0 = hoje).
# Ciclos: MMC(12, 18) = 36 · segunda + 36 dias · 36 ÷ 7 = 5, resto 1 → terça.
# Atalho: resto por 4 = resto dos dois últimos algarismos (100 é múltiplo de 4): 26 ÷ 4 = 6, resto 2 · não vale para 7 (100 ÷ 7 deixa resto 2).
# Questão: vermelho, azul, verde… posição 100 · 100 ÷ 3 = 33, resto 1 → vermelho · sábado + 45 dias · 45 ÷ 7 = 6, resto 3 → domingo, segunda, terça → terça.
# Visual: fila de letras A B C D em blocos de quatro com as posições embaixo; blocos completos apagando ("voltas"); conta armada 2.026 ÷ 4 com o resto aceso;
#   roda dos sete dias da semana com ponteiro andando o resto; linhas do tempo de 12 e 18 dias encontrando-se no 36; fila de cores no exercício.
# Ciclos: MMC pela história (ciclos que voltam a coincidir), não pela palavra, como na MAT-DIV-007. Resposta: daqui a 36 dias, numa terça.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas "á", "bê", "cê", "dê".

TITULO = "Padrões que se repetem: o resto manda"

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
    dict(id="s01", block="gancho", text="{a}Á, bê, cê, dê, [p=0.1] á, bê, cê, dê, [p=0.1] e assim por diante. [p=0.3] Qual letra está na {b}posição dois mil e vinte e seis? [p=0.3] Ninguém precisa escrever duas mil letras. [p=0.2] Basta {c}uma divisão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha qualquer posição de um padrão que se repete, [p=0.2] o dia da semana daqui a muitos dias [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}dividir com resto, [p=0.2] {b}o MMC dos encontros que se repetem [p=0.2] e {c}a diferença entre posição e termo. [p=0.3] Se faltar alguma, procure no canal."),
    # ciclo
    dict(id="s04", block="ciclo", text="Repare que a lista anda {a}em blocos de quatro letras. [p=0.2] Cada bloco é {b}uma volta completa, que termina em dê. [p=0.3] O dê está {c}na posição quatro, na oito e na doze: [p=0.2] os múltiplos de quatro."),
    dict(id="s05", block="ciclo", text="Então divida a posição pelo tamanho do bloco. [p=0.2] {a}Dois mil e vinte e seis dividido por quatro dá quinhentos e seis, com resto dois. [p=0.3] São {b}quinhentas e seis voltas completas, [p=0.2] e a última termina em dê, na posição {c}dois mil e vinte e quatro."),
    dict(id="s06", block="ciclo", text="O resto diz {a}quantas casas você anda depois da última volta. [p=0.2] Resto dois: {b}á, bê. [p=0.3] A letra da posição dois mil e vinte e seis é {c}bê. [p=0.3] As voltas não importam. [p=0.2] {d}Quem manda é o resto."),
    dict(id="s07", block="ciclo", text="Guarde a tabela: [p=0.2] {a}resto um dá a letra á, [p=0.2] {b}resto dois dá bê, [p=0.2] {c}resto três dá cê, [p=0.2] e {d}resto zero dá dê, a última do bloco."),
    # dias
    dict(id="s08", block="dias", text="A semana é o padrão que mais se repete: [p=0.2] {a}um bloco de sete dias. [p=0.2] Hoje é {b}terça. [p=0.2] Que dia será {c}daqui a cem dias?"),
    dict(id="s09", block="dias", text="{a}Cem dividido por sete dá catorze, com resto dois. [p=0.2] Catorze semanas completas {b}voltam para a terça. [p=0.2] Ande mais {c}dois dias: quarta, quinta. [p=0.3] Daqui a cem dias, {d}é quinta-feira."),
    dict(id="s10", block="dias", text="Repare: na semana, cada volta de sete dias {a}fecha de novo no dia de hoje. [p=0.2] Então resto zero quer dizer {b}o mesmo dia de hoje: [p=0.2] daqui a sete dias, terça de novo. [p=0.3] É a mesma ideia das letras: com resto zero, você para onde a última volta fechou."),
    # dois ciclos
    dict(id="s11", block="ciclos", text="E quando são {a}dois ciclos? [p=0.2] Uma máquina passa por manutenção {b}a cada doze dias. [p=0.2] Outra, {c}a cada dezoito. [p=0.2] Hoje, {d}uma segunda-feira, as máquinas pararam juntas. [p=0.3] Em que dia da semana voltam a parar juntas?"),
    dict(id="s12", block="ciclos", text="Ciclos que voltam a coincidir {a}pedem o MMC, como nos ônibus da aula de MMC. [p=0.2] O MMC de doze e dezoito {b}dá trinta e seis. [p=0.3] Agora o resto: {c}trinta e seis dividido por sete dá cinco, com resto um. [p=0.2] Segunda mais um dia dá terça. [p=0.2] {d}Param juntas daqui a trinta e seis dias, numa terça-feira."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}o resto zero. [p=0.2] Na posição {b}dois mil e vinte e oito, a divisão por quatro dá quinhentos e sete, com resto zero. [p=0.2] A pessoa pensa que não sobrou nada, volta para o começo [p=0.2] e responde {c}a letra á."),
    dict(id="s14", block="erro", text="Mas resto zero quer dizer que {a}a última volta acabou de fechar. [p=0.2] As voltas fecham em dê, como nas posições quatro e oito. [p=0.2] A resposta é {b}dê."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}no bloco de quatro, olhe só os dois últimos algarismos. [p=0.3] Em dois mil e vinte e seis, olhe o {b}vinte e seis. [p=0.2] {c}Vinte e seis dividido por quatro dá seis, com resto dois. [p=0.2] {d}O mesmo resto, com uma conta de cabeça."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cem é múltiplo de quatro. [p=0.2] As centenas e os milhares fecham voltas inteiras e não mudam o resto. [p=0.3] Não compensa com {b}o bloco de sete da semana. [p=0.2] Cem dividido por sete {c}deixa resto, [p=0.2] então ali você {d}faz a divisão inteira."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma fila de luzes pisca {a}vermelho, azul, verde, vermelho, azul, verde, e assim por diante. [p=0.3] {b}Qual é a cor da luz da posição cem? [p=0.3] E, se hoje é {c}sábado, [p=0.2] {d}que dia da semana será daqui a quarenta e cinco dias?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O bloco tem {a}três cores. [p=0.2] {b}Cem dividido por três dá trinta e três, com resto um. [p=0.2] Resto um é {c}a primeira cor do bloco: vermelho."),
    dict(id="s20", block="resposta", text="Nos dias, o bloco tem sete. [p=0.2] {a}Quarenta e cinco dividido por sete dá seis, com resto três. [p=0.2] Seis semanas voltam ao sábado. [p=0.2] Ande três dias: {b}domingo, segunda, terça. [p=0.3] {c}Daqui a quarenta e cinco dias, é terça-feira."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}divida pelo tamanho do bloco. [p=0.2] {b}As voltas somem, e o resto diz onde você para. [p=0.2] E {c}resto zero é o fim de uma volta."),
    dict(id="s22", block="fim", text="Na próxima aula, a sequência {a}sobe sempre do mesmo tanto, como cinco, nove, treze: [p=0.2] {b}a progressão aritmética. [p=0.3] Você vai achar a razão, {c}calcular o vigésimo termo com uma fórmula [p=0.2] e ver que ela é {d}parente da função afim. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
