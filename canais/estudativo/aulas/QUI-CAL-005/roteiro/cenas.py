# Estudativo · QUI-CAL-005 — Estequiometria de massa a massa (Química · Cálculos Químicos · Estequiometria).
# Habilidade: calcular que a queima de 46 g de etanol libera 88 g de CO₂ e fazer a conta direto, pelo atalho das massas
# na equação. Pré-requisitos: QUI-CAL-004, MAT-RAZ-006. Próxima: QUI-CAL-006 (reagente limitante e excesso).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Contas: C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O (balanceada); 46 g → 2·44 = 88 g; 23 g → 44 g; O₂ = 3·32 = 96 g; água = 3·18 = 54 g;
# 46 + 96 = 142 = 88 + 54. Erro (sem o coeficiente): 44 g, a metade. Questão: 230/46 = 5 → 5·88 = 440 g.
# Porcentagem e composição percentual NÃO estão em "Já ensinado" desta aula.

TITULO = "Estequiometria de massa a massa"

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
    dict(id="s01", block="gancho", text="{a}Queime quarenta e seis gramas de etanol, o álcool do posto. [p=0.3] {b}Saem oitenta e oito gramas de gás carbônico, [p=0.1] {c}quase o dobro do combustível que entrou. [p=0.3] {d}De onde vem essa massa a mais? [p=0.2] E como fazer essa conta {e}em uma linha?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}calcular a massa de um produto a partir da massa de um reagente, [p=0.2] e ainda leva {c}o atalho das massas na equação."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}ler uma equação em mols e passar mol para grama com a massa molar, [p=0.2] e {c}a regra de três. [p=0.3] Se faltar alguma, procure no canal."),
    # o método
    dict(id="s04", block="metodo", text="{a}Estequiometria é a conta das quantidades numa reação. [p=0.2] {b}O primeiro passo é sempre a equação balanceada. [p=0.3] {c}A queima do etanol: [p=0.1] cê dois agá seis ó mais três ó dois [p=0.1] forma dois cê ó dois mais três agá dois ó."),
    dict(id="s05", block="metodo", text="{a}Passo dois: leia em mols só as substâncias que a pergunta cita. [p=0.2] {b}Um mol de etanol [p=0.1] {c}forma dois mols de gás carbônico."),
    dict(id="s06", block="metodo", text="{a}Passo três: passe os mols para gramas. [p=0.2] {b}Um mol de etanol tem quarenta e seis gramas. [p=0.2] {c}Dois mols de cê ó dois: dois vezes quarenta e quatro dá oitenta e oito gramas."),
    dict(id="s07", block="metodo", text="{a}Passo quatro: a regra de três com o dado do problema. [p=0.2] {b}Quarenta e seis gramas de etanol dão oitenta e oito de gás carbônico. [p=0.2] {c}Com vinte e três gramas, a metade do etanol, [p=0.1] a regra de três dá a metade do gás: [p=0.1] {d}quarenta e quatro gramas."),
    dict(id="s08", block="metodo", text="{a}A conta também anda ao contrário. [p=0.2] {b}Quanto etanol é preciso para formar cento e setenta e seis gramas de gás carbônico? [p=0.3] {c}Cento e setenta e seis é o dobro de oitenta e oito, [p=0.1] {d}então o etanol também dobra: [p=0.1] {e}noventa e dois gramas."),
    # a massa a mais
    dict(id="s09", block="ar", text="E a massa a mais? [p=0.2] {a}Veio do ar. [p=0.2] {b}Os três mols de oxigênio têm noventa e seis gramas. [p=0.3] {c}Quarenta e seis mais noventa e seis dá cento e quarenta e dois, [p=0.2] {d}e é o que sai: oitenta e oito de gás carbônico mais cinquenta e quatro de água."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}esquecer o coeficiente na hora de passar para gramas. [p=0.3] {b}A pessoa usa quarenta e quatro gramas de gás carbônico, de um mol só, [p=0.2] e responde {c}a metade do certo. [p=0.3] {d}A massa de cada substância é o coeficiente vezes a massa molar."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho: [p=0.1] {a}escreva as massas direto embaixo da equação, [p=0.1] {b}coeficiente vezes massa molar. [p=0.3] {c}Embaixo do etanol, quarenta e seis gramas. [p=0.1] {d}Embaixo do gás carbônico, oitenta e oito. [p=0.3] {e}Em cima, o dado do problema e o xis. [p=0.2] {f}Uma regra de três, e pronto."),
    dict(id="s12", block="atalho", text="{a}Funciona porque a proporção das massas é fixa. [p=0.2] {b}Pule as substâncias que a pergunta não usa: [p=0.1] {c}aqui, o oxigênio e a água. [p=0.3] {d}Não compensa quando a pergunta pede mols ou moléculas: [p=0.1] aí, pare na linha dos mols."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Um fogareiro queima duzentos e trinta gramas de etanol. [p=0.2] {b}Quantos gramas de gás carbônico ele libera?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Embaixo da equação: quarenta e seis gramas de etanol para oitenta e oito de gás carbônico. [p=0.3] {b}Duzentos e trinta dividido por quarenta e seis dá cinco: [p=0.1] {c}cinco vezes mais etanol. [p=0.2] {d}Cinco vezes oitenta e oito dá quatrocentos e quarenta gramas."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}equação balanceada, [p=0.1] {b}mols da pergunta, [p=0.1] {c}mols em gramas [p=0.1] {d}e regra de três. [p=0.2] {e}Ou, pelo atalho, as massas direto embaixo da equação."),
    dict(id="s17", block="fim", text="Na próxima aula, {a}os reagentes chegam fora da proporção, [p=0.2] e você descobre {b}qual deles acaba primeiro e quanto sobra do outro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
