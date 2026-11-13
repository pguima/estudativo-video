# Estudativo · QUI-CAL-014 — Misturas gasosas e pressão parcial (Química · Cálculos Químicos · Estudo dos gases).
# Habilidade: achar a pressão parcial do oxigênio no ar pela sua fração.
# Pré-requisitos: QUI-CAL-012, MAT-POR-002. Próxima: QUI-CAL-016 (difusão de gases: lei de Graham).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# ATENÇÃO: volume molar (QUI-CAL-013) NÃO está em "Já ensinado" desta aula: a ligação volume ↔ mols sai de PV = nRT.
# Fatos: ar seco = 78% N₂, 21% O₂, 0,9% Ar (fração constante até grande altitude); topo do Everest ≈ 0,33 atm.
# Contas: 2 mol O₂ + 8 mol N₂ a 10 atm → 0,2 · 10 = 2 atm; 0,21 · 1 = 0,21 atm; erro: 32 g O₂ + 28 g N₂ = 1 mol + 1 mol → metade;
# atalho 20% de 5 = 1 atm; questão 1 mol O₂ + 3 mol He a 8 atm → 2 atm e 6 atm.

TITULO = "Misturas gasosas e pressão parcial"

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
    dict(id="s01", block="gancho", text="{a}No alto do Everest, o ar tem os mesmos vinte e um por cento de oxigênio da praia. [p=0.3] {b}Mesmo assim, o alpinista sente falta de ar. [p=0.2] {c}O que falta lá em cima não é a porcentagem. [p=0.2] {d}É a pressão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}calcular a pressão parcial de um gás numa mistura, [p=0.2] {c}como a do oxigênio no ar, [p=0.2] com um {d}atalho de porcentagem."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a equação pê vê igual a ene erre tê, [p=0.2] e {c}calcular porcentagem multiplicando pelo decimal. [p=0.3] Se faltar alguma, procure no canal."),
    # mistura
    dict(id="s04", block="mistura", text="{a}O ar é uma mistura de gases. [p=0.2] {b}Cerca de setenta e oito por cento é nitrogênio, [p=0.1] {c}vinte e um por cento é oxigênio, [p=0.1] {d}e o resto é quase todo argônio."),
    dict(id="s05", block="mistura", text="{a}Numa mistura, cada gás bate nas paredes como se estivesse sozinho no recipiente. [p=0.3] {b}A pressão que ele faria sozinho se chama pressão parcial. [p=0.3] {c}A pressão total é a soma das parciais: [p=0.1] {d}é a lei de Dalton, o mesmo Dalton do modelo do átomo."),
    # fração
    dict(id="s06", block="fracao", text="{a}Quanto da pressão é de cada gás? [p=0.2] {b}Em pê vê igual a ene erre tê, [p=0.1] com o mesmo volume e a mesma temperatura, [p=0.1] {c}a pressão é proporcional aos mols. [p=0.3] {d}Então cada gás fica com a sua fração dos mols."),
    dict(id="s07", block="fracao", text="{a}A fração em mols é o número de mols do gás dividido pelo total de mols. [p=0.3] {b}A pressão parcial é essa fração vezes a pressão total."),
    # exemplo
    dict(id="s08", block="exemplo", text="{a}Um cilindro tem dois mols de oxigênio e oito mols de nitrogênio, [p=0.1] {b}a dez atmosferas. [p=0.3] {c}No total, dez mols. [p=0.2] {d}O oxigênio tem dois de dez: [p=0.1] {e}fração zero vírgula dois. [p=0.3] {f}Zero vírgula dois vezes dez dá duas atmosferas de oxigênio. [p=0.2] {g}O nitrogênio fica com as outras oito."),
    dict(id="s09", block="exemplo", text="{a}No ar, a porcentagem vem em volume. [p=0.2] {b}Pela mesma equação, na mesma pressão e temperatura, o volume de gás também é proporcional aos mols. [p=0.3] {c}Então a porcentagem em volume é a porcentagem em mols. [p=0.3] {d}Ao nível do mar, a pressão total é uma atmosfera: [p=0.1] {e}zero vírgula vinte e um vezes um dá zero vírgula vinte e uma atmosfera de oxigênio."),
    dict(id="s10", block="exemplo", text="{a}No alto do Everest, a pressão total cai para cerca de um terço de atmosfera. [p=0.3] {b}O oxigênio continua com vinte e um por cento, [p=0.1] {c}mas vinte e um por cento de um terço. [p=0.2] {d}A pressão do oxigênio cai a um terço da que há na praia. [p=0.3] {e}Cada respiração leva bem menos oxigênio para o pulmão."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar a fração das massas, em vez da fração dos mols. [p=0.3] {b}Trinta e dois gramas de oxigênio com quatro gramas de hélio, de massa molar quatro. [p=0.2] Pela massa, o oxigênio parece ter quase noventa por cento. [p=0.3] {c}Mas são um mol de cada: [p=0.1] {d}metade da pressão para cada gás. [p=0.3] {e}Antes da fração, passe as massas para mols."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}a pressão parcial é a porcentagem do gás aplicada à pressão total. [p=0.3] {b}Vinte por cento de oxigênio a cinco atmosferas: [p=0.1] {c}dez por cento de cinco dá meia atmosfera, [p=0.1] {d}e vinte por cento dá uma atmosfera."),
    dict(id="s13", block="atalho", text="{a}Funciona porque a pressão se divide na mesma proporção dos mols. [p=0.3] {b}E dá para conferir: [p=0.1] as parciais somadas têm que dar a pressão total. [p=0.3] {c}Não compensa quando a porcentagem vem em massa: [p=0.1] aí, passe para mols primeiro."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um cilindro de mergulho tem um mol de oxigênio e três mols de hélio, [p=0.1] {b}a oito atmosferas. [p=0.3] {c}Qual é a pressão parcial de cada gás?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}No total, quatro mols. [p=0.2] {b}O oxigênio tem um de quatro: [p=0.1] {c}um quarto de oito dá duas atmosferas. [p=0.3] {d}O hélio tem três quartos: [p=0.1] {e}três quartos de oito dá seis atmosferas. [p=0.2] {f}Confira: dois mais seis dá oito."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}cada gás da mistura faz a sua pressão parcial; [p=0.2] {b}ela é a fração em mols vezes a pressão total; [p=0.2] {c}e a soma das parciais dá a pressão total."),
    dict(id="s18", block="fim", text="Na próxima aula, os gases se espalham: [p=0.2] você descobre {a}qual gás anda mais rápido [p=0.1] {b}só comparando as massas molares. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
