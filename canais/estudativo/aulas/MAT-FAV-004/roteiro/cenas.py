# Estudativo · MAT-FAV-004 — Função composta (Matemática · Funções Avançadas · Função composta e inversa).
# Habilidade: calcular f(g(3)) = 19 e g(f(3)) = 49 para f(x) = 2x + 1 e g(x) = x² e descobrir f(x) sabendo que f(2x + 1) = 4x + 3.
# Pré-requisitos: MAT-EQU-011 (isolar uma letra), MAT-FUN-004 (domínio e imagem), MAT-FUN-016 (função quadrática). Próxima: MAT-FAV-005.
# Questão inédita, criada para esta aula. Função afim e módulo (MAT-FUN-009, MAT-FAV-001 a 003) fora da ficha: não usados pelo nome.
# f(g(3)) = f(9) = 19 · g(f(3)) = g(7) = 49 · f(g(x)) = 2x² + 1 (em 3: 19) · g(f(x)) = (2x + 1)² = 4x² + 4x + 1 (em 3: 36 + 12 + 1 = 49).
# Volta: f(2x + 1) = 4x + 3 · u = 2x + 1 → x = (u − 1)/2 → f(u) = 4(u − 1)/2 + 3 = 2(u − 1) + 3 = 2u + 1 · conferência: 2(2x + 1) + 1 = 4x + 3.
# Erro: f · g em 3 = 7 · 9 = 63 (≠ 19).
# Atalho: f(5) → 2x + 1 = 5 → x = 2 → 4 · 2 + 3 = 11 (e 2 · 5 + 1 = 11).
# Questão: f(x) = x − 4, g(x) = 3x · f(g(2)) = f(6) = 2 · g(f(2)) = g(−2) = −6.
# Visual: duas máquinas (caixas com a lei) em fila, número que entra, passa e sai; f(g(3)) com chaves de dentro para fora;
#   troca do x pela caixinha; "u" numa caixa pontilhada; palco escuro no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "éfe de gê de xis".

TITULO = "Função composta"

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
    dict(id="s01", block="gancho", text="{a}Éfe de xis é dois xis mais um. [p=0.2] {b}Gê de xis é xis ao quadrado. [p=0.3] Use uma depois da outra, começando no três. [p=0.2] Numa ordem, dá {c}dezenove. [p=0.2] Na outra, {d}quarenta e nove. [p=0.3] A ordem muda tudo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a função composta, [p=0.2] {b}monta a lei dela [p=0.2] e {c}descobre uma função escondida, [p=0.2] com um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}calcular éfe de um número, trocando o xis por ele; [p=0.2] {b}o quadrado de uma soma; [p=0.2] e {c}isolar uma letra numa igualdade. [p=0.3] Se faltar alguma, procure no canal."),
    # máquinas
    dict(id="s04", block="maquinas", text="Pense em cada função como {a}uma máquina: [p=0.2] entra um número, sai outro. [p=0.2] A máquina éfe {b}dobra e soma um. [p=0.2] A máquina gê {c}eleva ao quadrado."),
    dict(id="s05", block="maquinas", text="Função composta é {a}ligar as máquinas em fila: [p=0.2] a saída da primeira {b}vira a entrada da segunda. [p=0.3] Ela se escreve {c}éfe de gê de xis. [p=0.2] E se lê de dentro para fora: {d}primeiro o gê, depois o éfe."),
    dict(id="s06", block="maquinas", text="{a}Éfe de gê de três. [p=0.2] Primeiro, {b}gê de três: três ao quadrado, nove. [p=0.2] O nove entra no éfe: {c}dois vezes nove, mais um, dezenove."),
    dict(id="s07", block="maquinas", text="Agora, {a}gê de éfe de três. [p=0.2] Primeiro, {b}éfe de três: dois vezes três, mais um, sete. [p=0.2] O sete entra no gê: {c}sete ao quadrado, quarenta e nove. [p=0.3] {d}Dezenove e quarenta e nove: trocar a ordem trocou o resultado."),
    dict(id="s08", block="maquinas", text="Nas provas, aparece também {a}éfe bola gê de xis. [p=0.2] É o mesmo que éfe de gê de xis. [p=0.2] {b}A bolinha só quer dizer: faça o gê primeiro."),
    # a lei
    dict(id="s09", block="lei", text="Para {a}a lei da composta, troque o xis do éfe pelo gê de xis inteiro. [p=0.2] {b}Éfe de xis é dois xis mais um. [p=0.2] No lugar do xis, entra {c}xis ao quadrado. [p=0.2] Então, {d}éfe de gê de xis é dois xis ao quadrado mais um. [p=0.3] Com o três: {e}dois vezes nove, mais um, dezenove."),
    dict(id="s10", block="lei", text="Na outra ordem, o gê eleva ao quadrado o éfe inteiro: [p=0.2] {a}dois xis mais um, tudo ao quadrado. [p=0.2] Pelo quadrado da soma, {b}quatro xis ao quadrado, mais quatro xis, mais um. [p=0.3] Com o três: {c}trinta e seis, mais doze, mais um, quarenta e nove."),
    # caminho de volta
    dict(id="s11", block="volta", text="Agora o caminho de volta. [p=0.2] A prova diz: {a}éfe de dois xis mais um é igual a quatro xis mais três. [p=0.2] {b}Quem é éfe de xis?"),
    dict(id="s12", block="volta", text="Dê um nome para o que está dentro: [p=0.2] {a}chame dois xis mais um de u. [p=0.2] {b}Isole o xis: [p=0.2] xis é u menos um, dividido por dois. [p=0.3] {c}Troque no lado direito: [p=0.2] quatro vezes isso, mais três. [p=0.2] {d}Quatro dividido por dois dá dois: [p=0.2] dois vezes u menos um, mais três. [p=0.2] {e}Dois u, menos dois, mais três: dois u mais um."),
    dict(id="s13", block="volta", text="Então, {a}éfe de u é dois u mais um, [p=0.2] e trocar o nome da letra não muda a função: [p=0.2] {b}éfe de xis é dois xis mais um. [p=0.3] Confira: {c}dois vezes dois xis mais um, mais um, dá quatro xis mais três."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}multiplicar as funções. [p=0.2] A pessoa lê éfe de gê como {b}éfe vezes gê. [p=0.2] No três, isso dá {c}sete vezes nove, sessenta e três."),
    dict(id="s15", block="erro", text="Mas a composta {a}não multiplica nada: ela encadeia. [p=0.2] {b}O resultado de uma entra na outra. [p=0.2] O certo é {c}dezenove."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho. [p=0.2] Muitas vezes a prova não quer a lei: [p=0.2] quer só {a}um valor, como éfe de cinco. [p=0.3] Então, {b}faça o de dentro valer cinco: [p=0.2] {c}dois xis mais um igual a cinco dá xis igual a dois. [p=0.2] {d}Coloque o dois no lado direito: quatro vezes dois, mais três, onze."),
    dict(id="s17", block="atalho", text="Funciona porque, {a}com xis igual a dois, o de dentro vira cinco, [p=0.2] e a igualdade vira {b}éfe de cinco igual a onze. [p=0.3] {c}Se a prova pedir a lei inteira, ou muitos valores, [p=0.2] o caminho com o u compensa mais."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Éfe de xis é xis menos quatro. [p=0.2] {b}Gê de xis é três xis. [p=0.3] Calcule {c}éfe de gê de dois [p=0.2] e {d}gê de éfe de dois."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Em éfe de gê de dois, primeiro o gê: {a}três vezes dois, seis. [p=0.2] O seis entra no éfe: {b}seis menos quatro, dois."),
    dict(id="s21", block="resposta", text="Em gê de éfe de dois, primeiro o éfe: {a}dois menos quatro, menos dois. [p=0.2] O menos dois entra no gê: {b}três vezes menos dois, menos seis. [p=0.3] {c}Dois e menos seis: de novo, a ordem mudou o resultado."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}de dentro para fora, [p=0.2] {b}a saída de uma é a entrada da outra, [p=0.2] e {c}a ordem importa."),
    dict(id="s23", block="fim", text="Na próxima aula, a pergunta é: {a}dá para desfazer uma função? [p=0.2] Você vai ver {b}quando existe a função inversa, [p=0.2] e por que xis ao quadrado não tem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
