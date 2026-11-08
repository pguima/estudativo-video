# Estudativo · MAT-POR-012 — Ponto percentual e porcentagem de porcentagem (Matemática · Porcentagem).
# Habilidade: dizer que passar de 8% para 10% é subir 2 pontos percentuais, ou 25%, e calcular 30% de 40% de um grupo.
# Pré-requisitos: MAT-POR-002 (calcular porcentagem), MAT-POR-005 (variação percentual). Próxima: MAT-POR-013.
# Questão inédita, criada para esta aula. Sem fatores e sem somar decimais: esta cadeia não tem MAT-POR-004 nem MAT-FRA-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ponto percentual e porcentagem de porcentagem"

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
    dict(id="s01", block="gancho", text="Em uma cidade, a parte dos trabalhadores que vão de bicicleta passou de {a}oito por cento para {b}dez por cento. [p=0.3] Um jornal diz: {c}subiu dois por cento. [p=0.2] Outro diz: {d}subiu vinte e cinco por cento. [p=0.3] Um deles errou. [p=0.2] Qual?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber a resposta, [p=0.2] calcular porcentagem de porcentagem [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] {b}Calcular a porcentagem de um número. [p=0.2] E {c}a variação percentual: a diferença dividida pelo valor de antes. [p=0.3] Se faltar alguma, procure no canal."),
    # duas medidas
    dict(id="s04", block="pontos", text="Quando uma porcentagem muda, existem {a}duas formas de medir a mudança. [p=0.3] A primeira é a {b}diferença simples: [p=0.2] {c}dez menos oito dá dois. [p=0.2] A diferença entre duas porcentagens se chama {d}ponto percentual. [p=0.2] Subiu {e}dois pontos percentuais."),
    dict(id="s05", block="pontos", text="A segunda é a {a}variação percentual: [p=0.2] a diferença dividida pelo valor de antes. [p=0.2] {b}Dois dividido por oito dá zero vírgula vinte e cinco. [p=0.2] {c}Subiu vinte e cinco por cento."),
    dict(id="s06", block="pontos", text="Para ver que as duas medidas estão certas, imagine {a}mil trabalhadores. [p=0.2] {b}Oito por cento são oitenta pessoas de bicicleta. [p=0.2] {c}Dez por cento são cem pessoas. [p=0.3] De oitenta para cem, {d}o aumento é de vinte e cinco por cento. [p=0.2] As duas medidas descrevem {e}a mesma mudança."),
    dict(id="s07", block="pontos", text="A diferença entre elas pode ser enorme. [p=0.2] Uma taxa que passa de {a}um por cento para dois por cento [p=0.2] subiu só {b}um ponto percentual. [p=0.2] Mas {c}dobrou: [p=0.1] {d}subiu cem por cento."),
    # porcentagem de porcentagem
    dict(id="s08", block="dede", text="{a}Porcentagem de porcentagem. [p=0.2] Numa empresa, {b}quarenta por cento dos funcionários vão de ônibus. [p=0.2] Desses, {c}trinta por cento pegam mais de um ônibus. [p=0.3] {d}Que porcentagem de todos os funcionários pega mais de um ônibus?"),
    dict(id="s09", block="dede", text="Os trinta por cento não são de todos: [p=0.2] são {a}dos quarenta por cento que vão de ônibus. [p=0.3] Imagine {b}cem funcionários. [p=0.2] {c}Quarenta vão de ônibus. [p=0.2] {d}Trinta por cento de quarenta dá doze. [p=0.2] Doze em cem: {e}doze por cento de todos."),
    dict(id="s10", block="dede", text="Sem imaginar ninguém, é uma multiplicação: [p=0.2] {a}trinta por cento de quarenta por cento [p=0.2] é {b}zero vírgula três vezes zero vírgula quatro: [p=0.1] {c}zero vírgula doze, doze por cento."),
    # erro
    dict(id="s11", block="erro", text="Voltando aos jornais: errou {a}o que disse subiu dois por cento. [p=0.3] Dois por cento de oitenta ciclistas é {b}menos de duas pessoas. [p=0.2] Mas os ciclistas aumentaram {c}vinte pessoas. [p=0.3] Diferença entre duas porcentagens se diz em {d}pontos percentuais. [p=0.2] O certo seria: {e}subiu dois pontos percentuais, ou vinte e cinco por cento."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho da porcentagem de porcentagem: [p=0.2] {a}multiplique os números e divida por cem. [p=0.2] {b}Trinta vezes quarenta dá mil e duzentos. [p=0.2] {c}Dividido por cem dá doze por cento."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada porcentagem é uma fração com cem embaixo. [p=0.2] Trinta centésimos vezes quarenta centésimos dá {b}mil e duzentos dividido por dez mil, [p=0.2] que é {c}doze centésimos. [p=0.3] Não compensa quando o problema dá {d}o número de pessoas e pede pessoas: [p=0.2] aí, vá em etapas. [p=0.2] {e}Quarenta por cento de quinhentos dá duzentos. [p=0.2] {f}Trinta por cento de duzentos dá sessenta."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Em uma escola, {a}sessenta por cento dos alunos estudam de manhã. [p=0.2] Desses, {b}vinte e cinco por cento vão de bicicleta. [p=0.3] {c}Que porcentagem de todos os alunos estuda de manhã e vai de bicicleta?"),
    dict(id="s15", block="questao", text="No ano seguinte, essa porcentagem passa para {a}dezoito por cento. [p=0.2] {b}Subiu quantos pontos percentuais? [p=0.2] {c}E quantos por cento?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Vinte e cinco por cento de sessenta por cento: {a}vinte e cinco vezes sessenta dá mil e quinhentos. [p=0.2] {b}Dividido por cem dá quinze por cento de todos os alunos. [p=0.3] Confira com {c}cem alunos: [p=0.2] sessenta de manhã, [p=0.2] e {d}vinte e cinco por cento de sessenta dá quinze. [p=0.3] Quem somou achou {e}oitenta e cinco por cento: [p=0.2] mais do que todos os alunos da manhã. [p=0.2] Impossível."),
    dict(id="s18", block="resposta", text="De quinze para dezoito: {a}dezoito menos quinze dá três pontos percentuais. [p=0.3] E a variação percentual: {b}três dividido por quinze dá zero vírgula dois. [p=0.2] {c}Subiu vinte por cento."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a diferença entre porcentagens é ponto percentual. [p=0.2] {b}Dividida pelo valor de antes, é variação percentual. [p=0.2] E {c}porcentagem de porcentagem se multiplica."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica as variações sucessivas: [p=0.2] {b}aumentos e descontos seguidos, a volta ao valor original [p=0.2] e {c}notícias cheias de porcentagem. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
