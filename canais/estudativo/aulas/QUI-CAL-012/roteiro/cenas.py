# Estudativo · QUI-CAL-012 — Equação de Clapeyron: PV = nRT (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: calcular a massa de gás em um cilindro com PV = nRT, sabendo o que cada letra significa e quando usar R = 0,082.
# Pré-requisitos: QUI-CAL-002, QUI-CAL-011. Próxima: QUI-CAL-013 (volume molar e estequiometria com gases).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# R = 0,082 atm·L/(mol·K) (= 62,3 mmHg·L/(mol·K) = 8,31 J/(mol·K)). Contas: 6 · 41 = 246; 0,082 · 300 = 24,6; 246/24,6 = 10 mol;
# 10 · 32 = 320 g de O₂. Erro (V em mL): 41.000 → n = 10.000 mol, mil vezes mais. Questão: 10 · 12,3 = 123; 123/24,6 = 5 mol;
# 5 · 44 = 220 g de CO₂. Porcentagem NÃO está em "Já ensinado".

TITULO = "Equação de Clapeyron: PV = nRT"

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
    dict(id="s01", block="gancho", text="{a}Um tanque de quarenta e um litros guarda oxigênio [p=0.1] {b}a seis atmosferas e vinte e sete graus Celsius. [p=0.3] {c}Quantos gramas de oxigênio estão lá dentro? [p=0.2] Ninguém abre o tanque para pesar. [p=0.2] {d}Uma equação curta responde."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}saber o que cada letra de pê vê igual a ene erre tê significa, [p=0.2] {c}calcular os mols e a massa de um gás [p=0.2] e {d}quando usar erre igual a zero vírgula zero oito dois."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a equação geral dos gases, com a temperatura em kelvin; [p=0.2] {c}o mol; [p=0.1] e {d}a massa molar. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="{a}Na equação geral, pê vê sobre tê não muda enquanto o gás fica preso. [p=0.3] {b}Mas esse valor depende de quanto gás há: [p=0.1] {c}com o dobro de mols, o valor dobra. [p=0.3] {d}Então pê vê sobre tê é igual ao número de mols vezes uma constante."),
    dict(id="s05", block="origem", text="{a}Passando o tê para o outro lado, sai a equação de Clapeyron: [p=0.1] {b}pê vê igual a ene erre tê."),
    # as letras
    dict(id="s06", block="letras", text="{a}Pê é a pressão, em atmosferas. [p=0.2] {b}Vê é o volume, em litros. [p=0.2] {c}Ene é o número de mols. [p=0.2] {d}Tê é a temperatura, sempre em kelvin. [p=0.3] {e}E erre é a constante dos gases, a mesma para qualquer gás."),
    dict(id="s07", block="letras", text="{a}Com pressão em atmosfera e volume em litro, [p=0.1] {b}erre vale zero vírgula zero oito dois [p=0.1] atmosfera vezes litro, por mol vezes kelvin. [p=0.3] {c}Se a prova der a pressão em milímetros de mercúrio, ou em pascal, o erre muda, [p=0.1] {d}e a prova costuma dar o valor. [p=0.3] {e}Confira sempre se as unidades do erre batem com as do problema."),
    # exemplo
    dict(id="s08", block="exemplo", text="Volte ao tanque. [p=0.2] {a}Pê igual a seis atmosferas. [p=0.1] {b}Vê igual a quarenta e um litros. [p=0.1] {c}Tê: vinte e sete mais duzentos e setenta e três dá trezentos kelvin. [p=0.3] {d}Ene é o que falta."),
    dict(id="s09", block="exemplo", text="{a}Isole o ene: pê vê dividido por erre tê. [p=0.3] {b}Em cima, seis vezes quarenta e um dá duzentos e quarenta e seis. [p=0.2] {c}Embaixo, zero vírgula zero oito dois vezes trezentos dá vinte e quatro vírgula seis. [p=0.3] {d}Duzentos e quarenta e seis dividido por vinte e quatro vírgula seis dá dez mols."),
    dict(id="s10", block="exemplo", text="{a}Para ter a massa, use a massa molar. [p=0.2] {b}O ó dois tem trinta e dois gramas por mol. [p=0.2] {c}Dez vezes trinta e dois dá trezentos e vinte gramas de oxigênio."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}misturar as unidades. [p=0.2] {b}Com o volume em mililitros, [p=0.1] {c}os quarenta e um litros viram quarenta e um mil, [p=0.1] {d}e a conta dá mil vezes mais gás: dez mil mols. [p=0.3] {e}Com erre igual a zero vírgula zero oito dois, o volume vai em litros e a pressão em atmosferas."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}a vinte e sete graus Celsius, ou trezentos kelvin, erre vezes tê dá vinte e quatro vírgula seis. [p=0.3] {b}Esse número aparece em muitas provas. [p=0.2] {c}Então ene é pê vê dividido por vinte e quatro vírgula seis. [p=0.3] {d}Seis vezes quarenta e um dá duzentos e quarenta e seis: [p=0.1] {e}dez vezes vinte e quatro vírgula seis. [p=0.2] Dez mols, de cabeça."),
    dict(id="s13", block="atalho", text="{a}E na hora de escolher a equação: [p=0.2] {b}se a quantidade de gás não muda e a pergunta compara antes e depois, [p=0.1] {c}use a equação geral. [p=0.2] {d}Se a pergunta pede mols ou massa, [p=0.1] {e}use pê vê igual a ene erre tê. [p=0.3] {f}O vinte e quatro vírgula seis não compensa em outras temperaturas: [p=0.1] aí, multiplique erre por tê."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um cilindro de doze vírgula três litros tem gás carbônico [p=0.1] {b}a dez atmosferas e vinte e sete graus Celsius. [p=0.2] {c}A massa molar do cê ó dois é quarenta e quatro gramas por mol. [p=0.3] {d}Quantos gramas de gás há no cilindro?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Vinte e sete graus são trezentos kelvin, [p=0.1] e erre vezes tê dá vinte e quatro vírgula seis. [p=0.3] {b}Pê vezes vê: dez vezes doze vírgula três dá cento e vinte e três. [p=0.2] {c}Cento e vinte e três dividido por vinte e quatro vírgula seis dá cinco mols. [p=0.3] {d}Cinco vezes quarenta e quatro dá duzentos e vinte gramas."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}pê vê igual a ene erre tê liga pressão, volume e temperatura à quantidade de gás; [p=0.2] {b}com atmosfera e litro, erre é zero vírgula zero oito dois; [p=0.2] {c}e a temperatura vai sempre em kelvin."),
    dict(id="s18", block="fim", text="Na próxima aula, você descobre que {a}um mol de qualquer gás ocupa o mesmo volume nas mesmas condições, [p=0.2] {b}vinte e dois vírgula quatro litros a zero grau e uma atmosfera, [p=0.1] e usa isso nas reações. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
