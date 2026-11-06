# Estudativo · MAT-NUM-006 — Tabuada com macetes: 3, 4, 6, 7 e 8 (Matemática · Números e Contas).
# Habilidade: achar 4 × 7 e 8 × 6 dobrando resultados que você já sabe e fechar a tabuada com 7 × 8.
# Pré-requisitos: MAT-NUM-005. Próxima: MAT-NUM-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 2 × 7 = 14 · 4 × 7 = 28 · 8 × 6 = 12 → 24 → 48 · 3 × 7 = 14 + 7 = 21 · 6 × 7 = 42 · 7 × 7 = 35 + 14 = 49 · 8 × 7 = 14 → 28 → 56.
# Sem 2, 5, 9 e 10 sobram 15 contas (pares entre 3, 4, 6, 7 e 8, contando cada par uma vez). Parar antes em 8 × 6 dá 24; 5 × 6 = 30.
# Questão: 8 × 8 = 16 → 32 → 64 · 6 × 4 = 4 × 6 = 24 · 64 + 24 = 88.

TITULO = "Tabuada com macetes: 3, 4, 6, 7 e 8"

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
    dict(id="s01", block="gancho", text="{a}Sete vezes oito. [p=0.3] Na hora do aperto, muita gente {b}chuta. [p=0.3] Hoje essa conta sai {c}dobrando um número que você já sabe."),
    dict(id="s02", block="gancho", text="E tem notícia boa: [p=0.2] tirando as tabuadas do um, do dois, do cinco, do nove e do dez, [p=0.2] {a}sobram só quinze contas. [p=0.3] {b}Até o fim desta aula, você fecha todas, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}o dobro, que é a tabuada do dois, [p=0.2] e {c}saber que a ordem não muda o resultado. [p=0.3] Se faltar alguma, procure no canal."),
    # por que dobrar funciona
    dict(id="s04", block="ideia", text="Imagine {a}duas fileiras com sete cadeiras: [p=0.2] {b}catorze cadeiras. [p=0.3] Coloque {c}uma sala igual ao lado. [p=0.2] Agora são {d}quatro fileiras [p=0.2] e {e}o dobro de cadeiras. [p=0.3] {f}Dobrou as fileiras, dobrou o resultado."),
    # quatro e oito
    dict(id="s05", block="quatro", text="Por isso, vezes quatro é {a}dobrar duas vezes. [p=0.3] {b}Quatro vezes sete: [p=0.2] o dobro de sete é {c}catorze. [p=0.2] O dobro de catorze é {d}vinte e oito."),
    dict(id="s06", block="oito", text="Vezes oito é {a}dobrar três vezes, [p=0.2] porque {b}oito é o dobro de quatro. [p=0.3] {c}Oito vezes seis: [p=0.2] dobre o seis três vezes. [p=0.2] {d}Doze. [p=0.2] {e}Vinte e quatro. [p=0.2] {f}Quarenta e oito. [p=0.3] Cada dobrada conta: [p=0.2] uma dobrada é vezes dois. [p=0.2] Duas dobradas, vezes quatro. [p=0.2] Três dobradas, vezes oito."),
    # três e seis
    dict(id="s07", block="tres", text="O três não vem de dobrar. [p=0.2] Mas {a}três fileiras são duas fileiras mais uma. [p=0.3] Vezes três é {b}o dobro mais uma vez. [p=0.3] {c}Três vezes sete: [p=0.2] o dobro de sete é {d}catorze. [p=0.2] Mais um sete dá {e}vinte e um. [p=0.3] {f}Três vezes oito: [p=0.2] o dobro de oito é dezesseis. [p=0.2] Mais um oito dá {g}vinte e quatro."),
    dict(id="s08", block="seis", text="E o seis é {a}o dobro de três. [p=0.2] Faça {b}vezes três e dobre. [p=0.3] {c}Seis vezes sete: [p=0.2] três vezes sete dá vinte e um. [p=0.2] O dobro de vinte e um é {d}quarenta e dois. [p=0.3] {e}Seis vezes seis: [p=0.2] três vezes seis dá dezoito. [p=0.2] O dobro de dezoito é {f}trinta e seis."),
    # sete
    dict(id="s09", block="sete", text="E a tabuada do sete? [p=0.2] {a}A maior parte você já fez, [p=0.2] porque a ordem não muda: [p=0.2] sete vezes quatro é {b}quatro vezes sete. [p=0.3] Só faltam {c}sete vezes sete [p=0.2] e {d}sete vezes oito."),
    dict(id="s10", block="sete", text="{a}Sete vezes sete. [p=0.2] Sete fileiras são {b}cinco fileiras mais duas. [p=0.3] {c}Cinco vezes sete dá trinta e cinco. [p=0.2] {d}Dois vezes sete dá catorze. [p=0.2] Juntando, {e}quarenta e nove."),
    dict(id="s11", block="sete", text="E {a}sete vezes oito, a conta que fecha a tabuada. [p=0.3] A ordem não muda: [p=0.2] é {b}oito vezes sete. [p=0.2] Dobre o sete três vezes: [p=0.2] {c}catorze. [p=0.2] {d}Vinte e oito. [p=0.2] {e}Cinquenta e seis. [p=0.3] Para guardar, repita em ordem: [p=0.2] {f}cinco, seis, sete, oito. [p=0.2] Cinquenta e seis é sete vezes oito. [p=0.2] É só coincidência, mas ajuda a lembrar."),
    # as quinze contas
    dict(id="s12", block="mapa", text="Olhe {a}as quinze contas juntas. [p=0.3] {b}Tem quatro ou oito? [p=0.2] Dobre. [p=0.2] {c}Tem três? [p=0.2] O dobro mais uma vez. [p=0.2] {d}Tem seis? [p=0.2] Vezes três e dobre. [p=0.3] {e}Só sete vezes sete pede a quebra em cinco mais dois."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}dobrar uma vez a menos. [p=0.2] Em oito vezes seis, a pessoa para em {b}vinte e quatro. [p=0.3] Mas vinte e quatro é {c}quatro vezes seis. [p=0.3] Dá para desconfiar: [p=0.2] {d}cinco vezes seis já dá trinta, [p=0.2] e oito vezes seis não pode dar menos que isso."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para o seis. [p=0.2] {a}Seis vezes oito. [p=0.3] {b}A metade do oito é quatro: [p=0.2] esse é o primeiro algarismo. [p=0.3] {c}O próprio oito é o segundo. [p=0.3] {d}Quarenta e oito. [p=0.3] Mais uma: {e}seis vezes quatro. [p=0.2] Metade de quatro é dois, [p=0.2] depois vem o quatro: {f}vinte e quatro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}seis vezes é cinco vezes mais uma vez. [p=0.3] Cinco vezes oito é a metade de oitenta: {b}quarenta. [p=0.2] Mais um oito, {c}quarenta e oito. [p=0.3] Só serve com dois, quatro, seis e oito. [p=0.3] {d}Não compensa em seis vezes sete: [p=0.2] o sete não se corta ao meio sem sobrar. [p=0.2] Aí, {e}faça vezes três e dobre."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um auditório tem {a}oito fileiras com oito cadeiras cada [p=0.2] e mais {b}seis fileiras com quatro cadeiras cada. [p=0.3] {c}Quantas cadeiras são ao todo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Oito vezes oito: [p=0.2] dobre o oito três vezes. [p=0.2] {b}Dezesseis. [p=0.2] {c}Trinta e dois. [p=0.2] {d}Sessenta e quatro."),
    dict(id="s19", block="resposta", text="{a}Seis vezes quatro: [p=0.2] a ordem não muda, então é quatro vezes seis. [p=0.2] Dobre o seis duas vezes: [p=0.2] {b}doze. [p=0.2] {c}Vinte e quatro. [p=0.3] Juntando: {d}sessenta e quatro mais vinte e quatro dá {e}oitenta e oito cadeiras."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}vezes quatro, dobre duas vezes. [p=0.2] {b}Vezes oito, dobre três vezes. [p=0.2] {c}Vezes seis, faça vezes três e dobre."),
    dict(id="s21", block="fim", text="Na próxima aula, a conta sai da tabela: [p=0.2] você {a}multiplica por dez e por cem de cabeça [p=0.2] e {b}multiplica um número maior por um algarismo, com a conta armada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
