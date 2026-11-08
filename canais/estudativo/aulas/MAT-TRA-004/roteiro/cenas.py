# Estudativo · MAT-TRA-004 — Secante, cossecante e identidades (Matemática · Trigonometria Avançada · Identidades, adição de arcos e equações).
# Habilidade: usar 1 + tg² x = sec² x e simplificar (1 − cos² x)/sen x até chegar a sen x.
# Pré-requisitos: MAT-TRI-010 (sen²x + cos²x = 1, tg = sen/cos, "que número ao quadrado dá..."), MAT-FAT-004 (cortar só fatores,
#   nunca parcelas). Usa MAT-FRA-004 (número misto: 1 e 9/16 = 25/16), MAT-FRA-009 (multiplicar frações), MAT-EQU-007 (o mesmo dos
#   dois lados), MAT-TRI-008 (sinal no 1º quadrante), MAT-TRI-003 (sen 45° = cos 45°). Próxima: MAT-TRA-005.
# FORA da ficha desta aula: MAT-FRA-007/008 (somar frações), MAT-FRA-011 (dividir frações), MAT-POT-016 (raiz de fração) e MAT-TRI-009.
#   Por isso: inverso explicado pela multiplicação (4/5 · 5/4 = 1); 1 + 9/16 pelo número misto; raiz de 25/16 como "que número ao
#   quadrado dá", igual à MAT-TRI-010; "dividir uma soma é dividir cada parcela" mostrado com (6 + 4) ÷ 2 = 3 + 2.
# Questão inédita, criada para esta aula. sen²x narrado "seno ao quadrado de xis", como na MAT-TRI-010.
# Contas: cos = 4/5 → sec = 5/4 · tg = 3/4 → tg² = 9/16 → sec² = 1 + 9/16 = 25/16 → sec = 5/4 (1º quadrante) → cos = 4/5.
#   (1 − cos²)/sen = sen²/sen = sen (sen ≠ 0). Erro: (sen + cos)/sen "= cos"; em 45°: (√2/2 + √2/2) ÷ (√2/2) = 2 ≠ √2/2.
#   Atalho: tg · cossec = (sen/cos) · (1/sen) = 1/cos = sec.
#   Questão: tg = 5/12 → 25/144 → 1 + 25/144 = 169/144 → sec = 13/12 → cos = 12/13.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Secante, cossecante e identidades"

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
    dict(id="s01", block="gancho", text="{a}Um menos cosseno ao quadrado de xis, dividido por seno de xis. [p=0.3] Parece conta de três linhas. [p=0.2] {b}É só seno de xis. [p=0.3] {c}Quem conhece as identidades vê isso de longe."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conhece secante, cossecante e cotangente, [p=0.2] {b}simplifica expressões assim [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a relação fundamental, seno ao quadrado mais cosseno ao quadrado igual a um, com a tangente igual a seno dividido por cosseno; [p=0.2] e {c}simplificar fração com letra, cortando só fator, nunca parcela. [p=0.3] Se faltar alguma, procure no canal."),
    # as novas razões
    dict(id="s04", block="novas", text="Três nomes novos. [p=0.2] {a}Secante é um dividido pelo cosseno. [p=0.2] {b}Cossecante é um dividido pelo seno. [p=0.2] {c}Cotangente é um dividido pela tangente, [p=0.2] ou seja, cosseno dividido por seno. [p=0.3] Para não trocar: {d}o có aparece uma vez só em cada dupla. [p=0.2] Secante anda com cosseno; [p=0.2] cossecante anda com seno."),
    dict(id="s05", block="novas", text="Cada uma é {a}o inverso de outra: [p=0.2] o número que, multiplicado por ela, dá um. [p=0.3] Se {b}o cosseno de xis é quatro quintos, [p=0.2] {c}a secante é cinco quartos, a fração de ponta-cabeça. [p=0.2] Confira: {d}quatro quintos vezes cinco quartos dá vinte vinte avos, um. [p=0.3] E o de baixo nunca pode ser zero: {e}em noventa graus, o cosseno é zero, e a secante não existe."),
    # a identidade
    dict(id="s06", block="identidade", text="Da relação fundamental sai uma identidade nova. [p=0.2] {a}Seno ao quadrado mais cosseno ao quadrado igual a um. [p=0.2] {b}Divida os dois lados por cosseno ao quadrado. [p=0.3] Dividir uma soma é dividir cada parcela, [p=0.2] como {c}seis mais quatro, dividido por dois, que dá três mais dois."),
    dict(id="s07", block="identidade", text="{a}Seno ao quadrado dividido por cosseno ao quadrado é tangente ao quadrado. [p=0.2] {b}Cosseno ao quadrado dividido por ele mesmo dá um. [p=0.2] {c}Um dividido por cosseno ao quadrado é secante ao quadrado. [p=0.3] Fica {d}tangente ao quadrado mais um, igual a secante ao quadrado. [p=0.3] Dividindo por seno ao quadrado, sai a irmã: {e}um mais cotangente ao quadrado, igual a cossecante ao quadrado."),
    # usando a identidade
    dict(id="s08", block="usar", text="Para que serve? [p=0.2] A tangente de xis é {a}três quartos, com xis no primeiro quadrante. [p=0.2] {b}Quanto vale o cosseno? [p=0.3] {c}Tangente ao quadrado: nove dezesseis avos. [p=0.2] {d}Um mais nove dezesseis avos é um inteiro e nove dezesseis avos, [p=0.2] ou {e}vinte e cinco dezesseis avos. [p=0.2] Essa é a secante ao quadrado."),
    dict(id="s09", block="usar", text="Que número, ao quadrado, dá vinte e cinco dezesseis avos? [p=0.2] {a}Cinco quartos, [p=0.2] positivo no primeiro quadrante. [p=0.2] {b}A secante é cinco quartos, [p=0.2] e o cosseno é o inverso: {c}quatro quintos."),
    # simplificar
    dict(id="s10", block="simplificar", text="Agora, a expressão do começo. [p=0.2] {a}Um menos cosseno ao quadrado, dividido por seno. [p=0.3] Da relação fundamental, {b}tirando cosseno ao quadrado dos dois lados: [p=0.2] {c}um menos cosseno ao quadrado é seno ao quadrado."),
    dict(id="s11", block="simplificar", text="Fica {a}seno ao quadrado dividido por seno, [p=0.2] ou seja, {b}seno vezes seno, dividido por seno. [p=0.2] Agora sim, {c}é fator: corta um seno em cima e um embaixo. [p=0.2] Sobra {d}seno de xis, [p=0.2] onde o seno não é zero."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}cortar parcela. [p=0.2] Em {b}seno mais cosseno, dividido por seno, [p=0.2] a pessoa corta os senos e responde {c}cosseno. [p=0.3] Teste com quarenta e cinco graus, em que seno e cosseno valem o mesmo. [p=0.2] {d}Em cima fica o dobro do de baixo: a conta dá dois. [p=0.2] {e}O cosseno de quarenta e cinco não é dois. [p=0.3] {f}O seno ali é parcela: não corta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}travou, escreva tudo em seno e cosseno. [p=0.3] Veja {b}tangente vezes cossecante. [p=0.2] {c}Tangente vira seno sobre cosseno. [p=0.2] {d}Cossecante vira um sobre seno. [p=0.2] Multiplicando, {e}o seno corta, porque é fator, [p=0.2] e sobra {f}um sobre cosseno: secante."),
    dict(id="s14", block="atalho", text="Funciona porque {a}as seis razões são feitas só de seno e cosseno. [p=0.3] {b}Não compensa quando a expressão já é uma identidade pronta: [p=0.2] um mais tangente ao quadrado, por exemplo, {c}troque direto por secante ao quadrado."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] A tangente de xis vale {a}cinco doze avos, [p=0.2] com xis {b}no primeiro quadrante. [p=0.3] {c}Calcule a secante e o cosseno de xis."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Tangente ao quadrado: vinte e cinco cento e quarenta e quatro avos. [p=0.2] {b}Mais um: um inteiro e vinte e cinco cento e quarenta e quatro avos, [p=0.2] {c}cento e sessenta e nove cento e quarenta e quatro avos."),
    dict(id="s18", block="resposta", text="Que número, ao quadrado, dá isso? [p=0.2] {a}Treze doze avos, [p=0.2] porque treze vezes treze dá cento e sessenta e nove, e doze vezes doze dá cento e quarenta e quatro. [p=0.3] {b}A secante é treze doze avos, positiva no primeiro quadrante, [p=0.2] e {c}o cosseno é doze treze avos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}secante, cossecante e cotangente são inversos. [p=0.2] {b}Um mais tangente ao quadrado dá secante ao quadrado. [p=0.2] E, {c}na dúvida, tudo em seno e cosseno, cortando só fator."),
    dict(id="s20", block="fim", text="Na próxima aula, você calcula {a}o seno de setenta e cinco graus, [p=0.2] que não está na tabela, [p=0.2] {b}somando quarenta e cinco com trinta, [p=0.2] e aprende o {c}seno do arco duplo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
