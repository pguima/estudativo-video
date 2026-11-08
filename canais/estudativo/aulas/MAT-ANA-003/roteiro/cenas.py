# Estudativo · MAT-ANA-003 — Coeficiente angular e alinhamento (Matemática · Geometria Analítica · Equação da reta).
# Habilidade: calcular m = Δy/Δx, dizer que m = tg θ e testar se três pontos estão alinhados.
# Pré-requisitos: MAT-FUN-010 (a = Δy/Δx), MAT-TRI-003 (tg 45° = 1, tg 60° = √3). Usa também MAT-TRI-001 (tangente) e MAT-RAZ-002 (produto cruzado, no atalho). Próxima: MAT-ANA-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas: "eme" (m), "teta" (θ), "á", "bê", "cê"; Δ = "delta", como na MAT-FUN-010.
# Tangente de ângulo maior que 90° não está na ficha: reta que desce fica como assunto de outra aula, sem ângulo.

TITULO = "Coeficiente angular e alinhamento de três pontos"

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
    dict(id="s01", block="gancho", text="Três postes, num mapa quadriculado: [p=0.2] {a}xis um, ípsilon um; [p=0.2] {b}xis três, ípsilon cinco; [p=0.2] e {c}xis cinco, ípsilon dez. [p=0.3] {d}Eles estão na mesma reta? [p=0.3] No desenho, parece que sim. [p=0.2] {e}Não estão, e uma conta curta prova isso."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede a inclinação de uma reta, [p=0.2] liga essa medida a {b}um ângulo [p=0.2] e testa {c}se três pontos estão alinhados."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a taxa de variação da função afim, delta ípsilon dividido por delta xis; [p=0.2] e {c}a tangente, cateto oposto dividido pelo adjacente, que dá um em quarenta e cinco graus. [p=0.3] Se faltar alguma, procure no canal."),
    # coeficiente angular
    dict(id="s04", block="eme", text="Na geometria analítica, aquela taxa ganha {a}um nome e uma letra: [p=0.2] {b}coeficiente angular, a letra eme. [p=0.3] É o mesmo á da função afim: [p=0.2] {c}quanto a reta sobe a cada passo para a direita."),
    dict(id="s05", block="eme", text="Pegue os pontos {a}xis um, ípsilon dois, [p=0.2] e {b}xis quatro, ípsilon oito. [p=0.3] {c}Delta ípsilon: oito menos dois dá seis. [p=0.2] {d}Delta xis: quatro menos um dá três. [p=0.2] {e}Eme igual a seis dividido por três, que dá dois. [p=0.3] A cada passo para a direita, {f}a reta sobe dois."),
    # ângulo
    dict(id="s06", block="angulo", text="E de onde vem o nome angular? [p=0.2] Desenhe {a}o triângulo da subida: [p=0.2] {b}o delta xis deitado [p=0.2] e {c}o delta ípsilon em pé. [p=0.3] {d}O ângulo entre a reta e a horizontal se chama teta. [p=0.2] É o ângulo que a reta faz com o eixo xis."),
    dict(id="s07", block="angulo", text="Para o ângulo teta, {a}o delta ípsilon é o cateto oposto [p=0.2] e {b}o delta xis é o adjacente. [p=0.3] Oposto dividido por adjacente é {c}a tangente. [p=0.2] Então, {d}eme é a tangente de teta. [p=0.3] Quanto maior o ângulo, {e}mais em pé fica a reta, e maior o eme."),
    dict(id="s08", block="angulo", text="Teste com um ângulo conhecido. [p=0.2] Reta por {a}xis um, ípsilon um, [p=0.2] e {b}xis quatro, ípsilon quatro. [p=0.2] {c}Sobe três, anda três: três dividido por três dá um. [p=0.3] {d}Tangente igual a um: quarenta e cinco graus. [p=0.2] E uma reta de sessenta graus tem {e}eme igual a raiz de três. [p=0.3] Quando a reta desce, {f}o eme é negativo, e esse ângulo é assunto de outra aula."),
    # alinhamento
    dict(id="s09", block="alinhamento", text="Agora, o teste de alinhamento. [p=0.2] Três pontos estão {a}na mesma reta quando a inclinação não muda. [p=0.3] {b}Calcule o eme do primeiro ao segundo ponto [p=0.2] e {c}o eme do segundo ao terceiro. [p=0.2] {d}Deu igual: alinhados. [p=0.2] {e}Deu diferente: a linha entorta no meio, e eles não estão alinhados."),
    dict(id="s10", block="alinhamento", text="Nos postes do começo: [p=0.2] {a}do primeiro ao segundo, sobe quatro e anda dois: [p=0.2] quatro dividido por dois dá dois. [p=0.3] {b}Do segundo ao terceiro, sobe cinco e anda dois: [p=0.2] cinco dividido por dois dá dois vírgula cinco. [p=0.3] {c}A inclinação mudou: não estão alinhados."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}dividir ao contrário, o delta xis pelo delta ípsilon. [p=0.3] Com os pontos de antes, a pessoa faz {b}três dividido por seis, que dá zero vírgula cinco. [p=0.3] Mas a reta sobe seis enquanto anda três: [p=0.2] {c}ela está mais em pé que a de quarenta e cinco graus, [p=0.2] e o eme tem de passar de um. [p=0.3] {d}O que sobe vai em cima. O que anda vai embaixo."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho do alinhamento: [p=0.2] {a}multiplique em cruz, sem fazer a divisão. [p=0.3] Nos postes, as inclinações são {b}quatro dividido por dois [p=0.2] e {c}cinco dividido por dois. [p=0.2] {d}Quatro vezes dois dá oito. [p=0.2] {e}Dois vezes cinco dá dez. [p=0.2] {f}Oito não é igual a dez: não estão alinhados."),
    dict(id="s13", block="atalho", text="Funciona porque {a}duas frações são iguais quando os produtos em cruz são iguais: [p=0.2] é a proporção. [p=0.3] Serve para fugir de {b}divisão que não dá exata. [p=0.3] {c}Não compensa quando as divisões são fáceis, [p=0.2] como seis dividido por três: [p=0.2] aí, calcule o eme direto."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Os pontos são {a}á, em xis menos um, ípsilon quatro; [p=0.2] {b}bê, em xis um, ípsilon um; [p=0.2] e {c}cê, em xis cinco, ípsilon menos cinco. [p=0.3] {d}Qual é o coeficiente angular de á até bê? [p=0.2] E {e}os três pontos estão alinhados?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] De á até bê: {a}delta ípsilon, um menos quatro, dá menos três. [p=0.2] {b}Delta xis, um menos, abre parênteses, menos um, dá dois. [p=0.3] {c}Eme igual a menos três dividido por dois, que dá menos um vírgula cinco. [p=0.2] Negativo: {d}a reta desce."),
    dict(id="s17", block="resposta", text="De bê até cê: {a}delta ípsilon, menos cinco menos um, dá menos seis. [p=0.2] {b}Delta xis, cinco menos um, dá quatro. [p=0.3] Em cruz: {c}menos três vezes quatro dá menos doze. [p=0.2] {d}Dois vezes menos seis dá menos doze. [p=0.3] {e}Deu igual: os três pontos estão alinhados."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}eme é delta ípsilon dividido por delta xis, [p=0.2] {b}eme é a tangente do ângulo com o eixo xis, [p=0.2] e {c}pontos alinhados mantêm o mesmo eme."),
    dict(id="s19", block="fim", text="Na próxima aula, você escreve {a}a equação de uma reta [p=0.2] de três jeitos: {b}reduzida, geral e segmentária. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
