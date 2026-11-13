# Estudativo · QUI-INO-011 — Dupla troca: precipitado, gás ou água (Química · Funções e Reações Inorgânicas · Reações e balanceamento).
# Habilidade: dizer se uma dupla troca acontece vendo se forma precipitado, gás ou água, como em AgNO₃ + NaCl.
# Pré-requisitos: QUI-INO-003, QUI-INO-008. Próxima: QUI-INO-012 (praticando reações e balanceamento).
# "Já ensinado" NÃO tem a simples troca (QUI-INO-010) nem síntese/análise (QUI-INO-009): não se compara com elas.
# Sais e ácidos são ditos pelo NOME; a fórmula fica na tela (a leitura letra a letra de AgNO₃ + NaCl seria longa demais).
# Fatos: AgNO₃ + NaCl → AgCl↓ (branco) + NaNO₃. Na₂CO₃ + 2 HCl → 2 NaCl + H₂CO₃; H₂CO₃ → H₂O + CO₂ (efervescência).
# HCl + NaOH → NaCl + H₂O (neutralização = dupla troca). Regras de solubilidade: sais de Na⁺, K⁺ e todo nitrato são solúveis;
# cloretos são solúveis, exceto os de prata e de chumbo (e de mercúrio I, fora da aula). NaCl + KNO₃: não reage.
# Questão inédita: BaCl₂ + Na₂SO₄ → BaSO₄↓ + 2 NaCl. BaSO₄ é o contraste que se bebe para o raio X do estômago (insolúvel).

TITULO = "Dupla troca: precipitado, gás ou água"

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
    dict(id="s01", block="gancho", text="{a}Misture duas soluções transparentes: [p=0.1] nitrato de prata e cloreto de sódio. [p=0.3] {b}Na hora, aparece um pó branco. [p=0.3] {c}Agora, cloreto de sódio com nitrato de potássio: [p=0.1] {d}nada. [p=0.3] Por quê?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer uma dupla troca [p=0.2] e {b}prever se ela acontece, [p=0.1] procurando {c}um sólido, um gás ou água."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}o sal que se dissolve na água solta os seus íons. [p=0.3] {b}O nitrato de prata solta á gê mais e o nitrato, ene ó três menos. [p=0.2] {c}O cloreto de sódio solta ene á mais e cê éle menos."),
    # dupla troca
    dict(id="s04", block="troca", text="{a}Na dupla troca, dois compostos trocam de parceiros. [p=0.3] {b}Á bê, mais cê dê, produz á dê, mais cê bê. [p=0.3] {c}O íon positivo de um fica com o negativo do outro."),
    dict(id="s05", block="troca", text="{a}Nitrato de prata mais cloreto de sódio [p=0.1] {b}produz cloreto de prata mais nitrato de sódio. [p=0.3] {c}A prata ficou com o cloreto, [p=0.1] {d}e o sódio ficou com o nitrato."),
    dict(id="s06", block="troca", text="{a}Mas a troca só acontece de verdade se algum produto sair da solução. [p=0.3] {b}Se todos os íons continuam soltos na água, [p=0.1] {c}nada mudou: [p=0.1] é só uma mistura de íons."),
    # três jeitos
    dict(id="s07", block="jeitos", text="{a}Primeiro jeito: um precipitado. [p=0.2] {b}É um sólido que não se dissolve e cai no fundo. [p=0.3] {c}O cloreto de prata é assim: é o pó branco. [p=0.2] {d}Na equação, ele ganha uma setinha para baixo."),
    dict(id="s08", block="jeitos", text="{a}Ou, com os estados entre parênteses: [p=0.1] {b}os reagentes e o nitrato de sódio são á quê, dissolvidos em água. [p=0.2] {c}O cloreto de prata fica com a letra ésse, de sólido. [p=0.3] {d}Um sólido no meio de tudo dissolvido é a pista do precipitado."),
    dict(id="s09", block="jeitos", text="{a}Segundo jeito: um gás, que escapa em bolhas. [p=0.3] {b}Carbonato de sódio mais ácido clorídrico forma ácido carbônico, [p=0.1] {c}que se desfaz em gás carbônico e água. [p=0.2] {d}O gás ganha uma setinha para cima."),
    dict(id="s10", block="jeitos", text="{a}Terceiro jeito: água, que quase não forma íons. [p=0.3] {b}Ácido clorídrico mais hidróxido de sódio dá cloreto de sódio e água. [p=0.3] {c}Sim: a neutralização é uma dupla troca."),
    # solubilidade
    dict(id="s11", block="regras", text="Como saber se um sal precipita? [p=0.2] Guarde duas regras. [p=0.2] {a}Sal de sódio, sal de potássio e todo nitrato se dissolvem. [p=0.3] {b}Cloreto se dissolve, menos o de prata e o de chumbo. [p=0.3] {c}Para os outros, a prova costuma dar uma tabela."),
    dict(id="s12", block="regras", text="Volte à mistura que não deu nada. [p=0.2] {a}Cloreto de sódio com nitrato de potássio [p=0.1] {b}daria nitrato de sódio e cloreto de potássio. [p=0.3] {c}Os dois se dissolvem. [p=0.2] {d}Sem precipitado, sem gás e sem água: [p=0.1] {e}não há reação."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}parar no ácido carbônico. [p=0.2] A pessoa escreve {b}agá dois cê ó três como produto final [p=0.1] e {c}conclui que nada sai da solução. [p=0.3] {d}Mas ele se desfaz em gás carbônico e água: [p=0.1] {e}tem gás, e a reação acontece."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.1] {a}olhe só os dois produtos novos. [p=0.3] {b}Se um deles é de sódio, de potássio ou nitrato, ele com certeza fica dissolvido. [p=0.2] {c}Procure o precipitado no outro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}os sais de sódio, de potássio e os nitratos nunca precipitam. [p=0.3] {b}Só não compensa se os dois produtos forem de outros tipos: [p=0.1] {c}aí, consulte a tabela de solubilidade."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Cloreto de bário mais sulfato de sódio. [p=0.3] {b}O enunciado avisa: o sulfato de bário não se dissolve. [p=0.3] {c}Quais são os produtos? [p=0.2] E {d}a reação acontece? Por quê?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O bário fica com o sulfato: [p=0.1] {b}sulfato de bário. [p=0.2] {c}O sódio fica com o cloreto: [p=0.1] {d}cloreto de sódio, com coeficiente dois, para fechar a conta."),
    dict(id="s19", block="resposta", text="{a}O cloreto de sódio se dissolve. [p=0.2] {b}Mas o sulfato de bário não: [p=0.1] {c}ele precipita. [p=0.3] {d}Há reação, porque se forma um precipitado. [p=0.2] {e}É o sulfato de bário que se bebe antes do raio X do estômago."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}na dupla troca, os íons trocam de parceiros; [p=0.2] {b}ela só acontece se sair um precipitado, um gás ou água; [p=0.2] e {c}sal de sódio, de potássio e nitrato sempre se dissolvem."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}praticar tudo do módulo: [p=0.2] {b}balancear e prever o produto de cada tipo de reação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
