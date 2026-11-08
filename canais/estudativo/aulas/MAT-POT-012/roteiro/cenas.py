# Estudativo · MAT-POT-012 — Escrever em notação científica (Matemática · Potências e Raízes).
# Habilidade: escrever 45.000.000 como 4,5 × 10⁷ e 0,00032 como 3,2 × 10⁻⁴ e dizer por que 45 × 10³ não está na forma correta.
# Pré-requisitos: MAT-NUM-002 (números grandes), MAT-POT-005 (expoente negativo e potências de 10). Próxima: MAT-POT-013.
# Questão inédita, criada para esta aula. A fábrica de parafusos é invenção; os números reais da questão estão abaixo.
# Fatos: população do Brasil cerca de 214 milhões (IBGE, estimativa para 1/7/2026: 214.211.951, divulgada em 28/8/2026).
# Fatos: glóbulo vermelho cerca de 8 micrômetros, ou 0,000008 m (NIST/DOE, The Scale of Things: "red blood cells ~7-8 μm").
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Escrever em notação científica"

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
    dict(id="s01", block="gancho", text="{a}Quarenta e cinco vezes dez elevado a três. [p=0.3] A conta está certa: {b}vale quarenta e cinco mil. [p=0.3] Mas esse número {c}não está na forma correta, [p=0.2] e uma prova pode cobrar exatamente isso."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escrever números enormes e números minúsculos em uma linha curta, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}ler números grandes [p=0.2] e {c}conhecer as potências de dez, inclusive com expoente negativo. [p=0.3] Se faltar alguma, procure no canal."),
    # por que existe
    dict(id="s04", block="porque", text="Uma fábrica produziu {a}quarenta e cinco milhões de parafusos. [p=0.3] Escrito por inteiro, são {b}seis zeros, [p=0.2] e basta perder um para errar feio. [p=0.3] A saída é trocar os zeros por uma potência de dez. [p=0.2] Isso se chama {c}notação científica."),
    # a forma
    dict(id="s05", block="forma", text="A forma tem {a}duas partes: [p=0.2] um {b}número na frente, [p=0.2] {c}vezes uma potência de dez. [p=0.3] Esse número da frente, que vamos chamar só de frente, tem uma regra: [p=0.2] ele vai {d}de um até menos de dez."),
    dict(id="s06", block="forma", text="{a}O um vale. [p=0.2] {b}Nove vírgula nove também vale. [p=0.3] Mas {c}o dez já não vale, [p=0.2] e {d}zero vírgula cinco também não. [p=0.3] Na prática: {e}um único algarismo antes da vírgula, e ele não pode ser zero."),
    # número grande
    dict(id="s07", block="grande", text="Vamos escrever {a}quarenta e cinco milhões. [p=0.3] Todo número inteiro tem uma {b}vírgula escondida no fim. [p=0.3] Ande com ela para a esquerda, até sobrar um algarismo antes dela. [p=0.2] São {c}sete casas, [p=0.2] e fica {d}quatro vírgula cinco."),
    dict(id="s08", block="grande", text="Mas quatro vírgula cinco não é quarenta e cinco milhões. [p=0.3] Andar sete casas para a esquerda {a}dividiu o número por dez elevado a sete. [p=0.3] Para o valor não mudar, {b}multiplique por dez elevado a sete. [p=0.3] Resultado: {c}quatro vírgula cinco vezes dez elevado a sete."),
    # número pequeno
    dict(id="s09", block="pequeno", text="Com número pequeno, é o caminho de volta. [p=0.2] Pegue {a}zero vírgula zero zero zero trinta e dois. [p=0.3] Aqui a vírgula anda para a direita, até passar do primeiro algarismo que não é zero. [p=0.2] São {b}quatro casas, [p=0.2] e fica {c}três vírgula dois."),
    dict(id="s10", block="pequeno", text="Andar para a direita {a}multiplicou o número por dez mil. [p=0.3] Para desfazer, é preciso {b}dividir por dez mil, [p=0.2] e isso é o mesmo que multiplicar por {c}dez elevado a menos quatro. [p=0.3] Resultado: {d}três vírgula dois vezes dez elevado a menos quatro."),
    # regra
    dict(id="s11", block="regra", text="A regra cabe em três linhas. [p=0.2] {a}A vírgula andou para a esquerda: expoente positivo. [p=0.2] {b}Andou para a direita: expoente negativo. [p=0.2] {c}Quantas casas andou, esse é o tamanho do expoente."),
    # corrigir a forma
    dict(id="s12", block="corrigir", text="Voltemos ao começo: {a}quarenta e cinco vezes dez elevado a três. [p=0.3] Por que não está na forma? [p=0.2] Porque {b}quarenta e cinco passa de dez. [p=0.3] Para consertar, ande a vírgula uma casa para a esquerda: {c}quatro vírgula cinco."),
    dict(id="s13", block="corrigir", text="A frente ficou {a}dez vezes menor. [p=0.2] Então a potência precisa ficar {b}dez vezes maior: [p=0.2] {c}o expoente sobe de três para quatro. [p=0.3] Fica {d}quatro vírgula cinco vezes dez elevado a quatro. [p=0.3] Mesmo valor, {e}quarenta e cinco mil, agora na forma correta."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: {a}contar os zeros. [p=0.3] Quarenta e cinco milhões tem {b}seis zeros, [p=0.2] e a pessoa escreve {c}quatro vírgula cinco vezes dez elevado a seis."),
    dict(id="s15", block="erro", text="Mas isso é {a}quatro milhões e quinhentos mil: [p=0.2] dez vezes menos! [p=0.3] {b}Quem manda é a vírgula, não o zero. [p=0.2] Ela também passa pelo cinco, e essa casa entra na conta."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho, para número grande: [p=0.2] {a}conte quantos algarismos vêm depois do primeiro. [p=0.3] Quarenta e cinco milhões tem {b}oito algarismos. [p=0.2] Tirando o primeiro, {c}sobram sete: [p=0.2] dez elevado a sete, sem andar casa por casa."),
    dict(id="s17", block="atalho", text="Funciona porque {a}a vírgula passa por cada algarismo depois do primeiro. [p=0.3] {b}Não compensa quando o número já vem com vírgula ou com potência: [p=0.2] aí, ande a vírgula e compense."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] O Brasil tem {a}cerca de duzentos e catorze milhões de habitantes. [p=0.3] Um glóbulo vermelho do sangue mede {b}cerca de zero vírgula zero zero zero zero zero oito metro. [p=0.3] {c}Escreva cada valor em notação científica."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Duzentos e catorze milhões tem nove algarismos. [p=0.2] Tirando o primeiro, {b}sobram oito. [p=0.2] Fica {c}dois vírgula catorze vezes dez elevado a oito."),
    dict(id="s21", block="resposta", text="No glóbulo, a vírgula anda para a direita até passar do oito: {a}seis casas. [p=0.2] Direita, expoente negativo: [p=0.2] {b}oito vezes dez elevado a menos seis metro."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}um número de um até menos de dez, [p=0.2] {b}vezes uma potência de dez, [p=0.2] e {c}o expoente conta as casas que a vírgula andou."),
    dict(id="s23", block="fim", text="Na próxima aula, você vai {a}fazer contas em notação científica [p=0.2] e descobrir {b}quantas vezes a massa da Terra é maior que a da Lua. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
