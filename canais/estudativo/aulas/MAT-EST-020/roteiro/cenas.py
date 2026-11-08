# Estudativo · MAT-EST-020 — Números que enganam (Matemática · Estatística · Análise crítica de gráficos).
# Habilidade: questionar uma amostra ruim, desconfiar de porcentagem sobre base pequena e separar correlação de causa.
# Pré-requisitos: MAT-EST-001 (amostra; a colher da sopa mexida), MAT-EST-013 (valor extremo puxa a média), MAT-POR-012 (ponto percentual). Usa MAT-POR-005 (variação percentual). Próxima: MAT-EST-021.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Pesquisas, manchetes e dados criados para esta aula.

TITULO = "Números que enganam: amostra, base pequena e correlação"

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
    dict(id="s01", block="gancho", text="{a}Manchete: casos de uma doença rara sobem cem por cento na cidade. [p=0.3] Dá medo. [p=0.2] Agora o número que faltou: [p=0.2] {b}passou de um caso para dois. [p=0.3] {c}A conta está certa, [p=0.2] e mesmo assim a manchete engana."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desconfia de três tipos de número [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}amostra é a parte da população que a pesquisa ouve, [p=0.2] {c}um valor extremo puxa a média [p=0.2] e {d}diferença entre porcentagens se diz em pontos percentuais. [p=0.3] Se faltar alguma, procure no canal."),
    # amostra ruim
    dict(id="s04", block="amostra", text="{a}Primeiro número que engana: a amostra ruim. [p=0.3] Lembra da sopa? [p=0.2] {b}A colher só vale se a panela foi mexida. [p=0.3] Uma pesquisa feita {c}só pela internet conclui que {d}quase todo mundo usa internet todo dia. [p=0.2] Claro: [p=0.2] {e}quem não usa nem viu a pesquisa."),
    dict(id="s05", block="amostra", text="Outro caso: {a}a pesquisa em que só responde quem quer. [p=0.2] Numa enquete sobre o ônibus, {b}quem está irritado corre para votar. [p=0.2] {c}Quem está satisfeito nem abre. [p=0.3] Sempre pergunte: [p=0.2] {d}quem foi ouvido, [p=0.2] e {e}como essas pessoas foram escolhidas?"),
    dict(id="s06", block="amostra", text="E a média também pode enganar. [p=0.2] {a}A renda média de um bairro subiu muito? [p=0.2] Pode ser que {b}uma única pessoa muito rica tenha se mudado para lá. [p=0.3] O valor extremo {c}puxa a média, e a maioria continua igual."),
    # base pequena
    dict(id="s07", block="base", text="{a}Segundo número que engana: a porcentagem sobre base pequena. [p=0.3] De um caso para dois, {b}a alta é de um caso. [p=0.2] {c}Um dividido por um dá um: cem por cento. [p=0.3] Numa cidade grande, os casos vão de {d}mil para mil e cem. [p=0.2] {e}Cem dividido por mil dá zero vírgula um: dez por cento."),
    dict(id="s08", block="base", text="Qual mudou mais? [p=0.2] Em porcentagem, {a}a cidade pequena. [p=0.2] Em pessoas, {b}a grande: cem casos a mais, contra um. [p=0.3] Com base pequena, {c}um único caso vira uma porcentagem enorme. [p=0.2] Sempre pergunte: {d}por cento de quanto?"),
    dict(id="s09", block="base", text="O mesmo vale para taxas. [p=0.2] Uma taxa que vai de {a}um por cento para dois por cento [p=0.2] subiu {b}um ponto percentual, [p=0.2] ou {c}cem por cento. [p=0.3] Ambas as frases são verdadeiras. [p=0.2] {d}A manchete costuma escolher a que assusta mais."),
    # correlação e causa
    dict(id="s10", block="correlacao", text="{a}Terceiro número que engana: a correlação vendida como causa. [p=0.3] {b}Correlação é quando duas coisas sobem e descem juntas. [p=0.3] Os dados mostram: [p=0.2] {c}nos meses em que se vende mais sorvete, [p=0.2] {d}também há mais afogamentos."),
    dict(id="s11", block="correlacao", text="Então sorvete causa afogamento? [p=0.2] {a}Não. [p=0.2] Existe {b}um terceiro fator: o calor. [p=0.3] No calor, {c}mais gente toma sorvete [p=0.2] e {d}mais gente vai nadar. [p=0.3] As duas coisas andam juntas porque {e}dependem do mesmo motivo, e não uma da outra."),
    dict(id="s12", block="correlacao", text="Antes de aceitar uma causa, pergunte: [p=0.2] {a}existe um terceiro fator? [p=0.2] {b}A causa pode ser ao contrário? [p=0.2] {c}Pode ser coincidência? [p=0.3] Para provar causa, os cientistas usam {d}experimentos com grupos comparáveis, assunto que vai além desta aula."),
    # erro
    dict(id="s13", block="erro", text="Agora, um erro muito comum: [p=0.2] achar que {a}amostra grande conserta amostra mal escolhida. [p=0.3] Uma enquete com {b}cinquenta mil votos no site de um time [p=0.2] diz que esse time {c}é o preferido do país. [p=0.3] Só votou {d}quem visita o site do time. [p=0.2] {e}Uma colher maior, de um canto só da panela, continua de um canto só."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}três perguntas para qualquer número de manchete. [p=0.3] {b}Quem foi ouvido? [p=0.2] {c}Por cento de quanto? [p=0.2] {d}O que mais mudou junto? [p=0.3] Cada pergunta desarma um dos três truques."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a conta pode estar certa e a conclusão errada. [p=0.2] As perguntas olham {b}de onde o número veio, [p=0.2] não só a conta. [p=0.3] Não compensa quando {c}o enunciado já garante a amostra e dá os números. [p=0.2] Aí, {d}vá direto à conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Diga o problema de cada conclusão. [p=0.3] {a}Caso um: uma pesquisa na porta de uma academia conclui que setenta por cento dos moradores da cidade fazem exercício. [p=0.3] {b}Caso dois: furtos de bicicleta no bairro sobem duzentos por cento: [p=0.2] de dois para seis. [p=0.2] A conta está certa?"),
    dict(id="s17", block="questao", text="{a}Caso três: alunos que tomam café da manhã tiram notas maiores. [p=0.2] Logo, {b}o café da manhã faz a nota subir."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Caso um: amostra ruim. [p=0.2] Na porta da academia, {b}quase todo mundo faz exercício. [p=0.2] A colher veio de um canto só."),
    dict(id="s20", block="resposta", text="{a}Caso dois: a conta está certa. [p=0.2] {b}Seis menos dois dá quatro. [p=0.2] {c}Quatro dividido por dois dá dois: duzentos por cento. [p=0.3] Mas {d}a base é pequena: [p=0.2] são quatro furtos a mais. [p=0.2] Vale olhar o número de casos, não só a porcentagem."),
    dict(id="s21", block="resposta", text="{a}Caso três: correlação não prova causa. [p=0.2] Pode haver {b}um terceiro fator, [p=0.2] como uma rotina mais organizada, [p=0.2] que leva ao café da manhã {c}e também ao estudo. [p=0.3] Os dados mostram que as duas coisas andam juntas, [p=0.2] {d}não que uma causa a outra."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.2] {a}confira quem foi ouvido, [p=0.2] {b}pergunte por cento de quanto [p=0.2] e {c}procure o terceiro fator antes de aceitar uma causa."),
    dict(id="s23", block="fim", text="Na próxima aula, {a}você pratica tudo isso: [p=0.2] gráficos e pesquisas, [p=0.2] e uma pergunta só: {b}a conclusão se sustenta nos dados? [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
