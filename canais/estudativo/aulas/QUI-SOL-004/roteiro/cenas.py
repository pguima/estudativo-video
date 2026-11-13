# Estudativo · QUI-SOL-004 — Concentração em mol/L (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: calcular que 40 g de NaOH em 2 L dão 0,5 mol/L e converter g/L em mol/L.
# Pré-requisitos: QUI-SOL-003, QUI-CAL-002. Próxima: QUI-SOL-005 (diluição e mistura de soluções).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Massas: H = 1, C = 12, O = 16, Na = 23, Cl = 35,5. NaOH = 40 g/mol; NaCl = 58,5 g/mol; C₆H₁₂O₆ = 180 g/mol.
# Contas: 40 ÷ 40 = 1 mol, 1 ÷ 2 = 0,5 mol/L; 40 g/L de NaOH e 58,5 g/L de NaCl = 1 mol/L cada; 20 g/L ÷ 40 = 0,5;
# preparar 0,5 L de glicose 0,2 mol/L: 0,2 × 0,5 = 0,1 mol, 0,1 × 180 = 18 g; erro: 40 ÷ 2 = 20 (é g/L);
# questão: 9 g de glicose em 250 mL: 9 ÷ 180 = 0,05 mol, 0,05 ÷ 0,25 = 0,2 mol/L; pelo atalho 9 ÷ 0,25 = 36 g/L, 36 ÷ 180 = 0,2.
# Na tela, a concentração em mol/L aparece como M (M = n/V), sem falar "eme" na voz, para não confundir com a massa m.

TITULO = "Concentração em mol/L"

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
    dict(id="s01", block="gancho", text="{a}Dois frascos de um litro. [p=0.2] {b}Um tem quarenta gramas de soda cáustica. [p=0.2] {c}O outro, cinquenta e oito vírgula cinco gramas de sal de cozinha. [p=0.3] {d}Qual tem mais soluto? [p=0.3] Em gramas, o sal. [p=0.2] {e}Mas, contados em mol, empatam: cada frasco tem exatamente um mol."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a concentração {b}em mol por litro [p=0.2] e {c}passar de gramas por litro para mol por litro com uma divisão só."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}um mol é um pacote com sempre o mesmo número de partículas. [p=0.3] {b}A massa molar é quantos gramas pesa um mol. [p=0.2] {c}Para achar os mols, divida a massa pela massa molar. [p=0.3] E {d}a concentração comum é a massa do soluto dividida pelo volume da solução em litros."),
    # por que mol
    dict(id="s04", block="porque", text="Por que contar em mol? [p=0.2] {a}Porque as reações acontecem partícula com partícula, [p=0.2] e {b}o grama engana. [p=0.3] {c}Cada unidade de sal, um sódio e um cloro, pesa mais que cada unidade de soda. [p=0.2] {d}Por isso o mesmo número de unidades pesa diferente: [p=0.1] {e}quarenta gramas de uma, cinquenta e oito vírgula cinco da outra."),
    # a fórmula
    dict(id="s05", block="formula", text="A concentração em mol por litro diz {a}quantos mols de soluto há em cada litro de solução. [p=0.3] {b}É o número de mols dividido pelo volume da solução, em litros. [p=0.3] {c}Na tela, ela ganha uma letra própria, maiúscula, para não confundir com a massa. [p=0.2] Alguns livros a chamam de {d}concentração molar, ou molaridade."),
    # exemplo NaOH
    dict(id="s06", block="exemplo", text="{a}Quarenta gramas de soda cáustica, o hidróxido de sódio, em dois litros de solução. [p=0.3] Primeiro, a massa molar: [p=0.1] {b}sódio vinte e três, oxigênio dezesseis, hidrogênio um: [p=0.1] {c}quarenta gramas por mol."),
    dict(id="s07", block="exemplo", text="{a}Passo um, gramas em mols: [p=0.1] {b}quarenta dividido por quarenta dá um mol. [p=0.3] {c}Passo dois, mols por litro: [p=0.1] {d}um mol dividido por dois litros dá zero vírgula cinco mol por litro."),
    # conversão
    dict(id="s08", block="ponte", text="{a}E se você já tem a concentração em gramas por litro? [p=0.2] A mesma solução tem {b}quarenta gramas em dois litros: vinte gramas por litro. [p=0.3] {c}Divida pela massa molar: [p=0.1] {d}vinte dividido por quarenta dá zero vírgula cinco mol por litro. [p=0.3] {e}O mesmo resultado, numa conta só."),
    dict(id="s09", block="ponte", text="{a}O caminho de volta é multiplicar. [p=0.2] Quer preparar meio litro de soro de glicose a zero vírgula dois mol por litro? [p=0.3] {b}Zero vírgula dois vezes zero vírgula cinco dá zero vírgula um mol. [p=0.2] {c}A glicose tem cento e oitenta gramas por mol, [p=0.1] {d}então são dezoito gramas."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum: [p=0.2] {a}dividir a massa pelo volume e chamar de mol por litro. [p=0.3] {b}Quarenta gramas em dois litros, quarenta dividido por dois: [p=0.1] {c}a pessoa marca vinte mol por litro. [p=0.3] {d}Mas vinte é em gramas por litro. [p=0.2] {e}Faltou passar pela massa molar."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho de prova: [p=0.2] {a}gramas por litro, dividido pela massa molar, dá mol por litro. [p=0.3] {b}E, de volta, mol por litro vezes a massa molar dá gramas por litro. [p=0.3] {c}Confira pelas unidades: gramas divididos por gramas por mol viram mols."),
    dict(id="s12", block="atalho", text="Funciona porque {a}dividir pela massa molar troca gramas por mols, [p=0.2] e o litro continua embaixo. [p=0.3] {b}Não compensa quando a questão pede só o número de mols: [p=0.2] {c}aí basta dividir a massa pela massa molar."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Um soro tem nove gramas de glicose em duzentos e cinquenta mililitros de solução. [p=0.3] {b}A massa molar da glicose é cento e oitenta gramas por mol. [p=0.3] {c}Qual é a concentração em mol por litro?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}Primeiro, o volume em litros: [p=0.1] divida por mil, e duzentos e cinquenta mililitros viram zero vírgula vinte e cinco litro. [p=0.3] {b}Em gramas por litro, nove dividido por zero vírgula vinte e cinco dá trinta e seis. [p=0.3] {c}Agora, o atalho: trinta e seis dividido por cento e oitenta [p=0.1] {d}dá zero vírgula dois mol por litro."),
    dict(id="s16", block="resposta", text="{a}Pelo outro caminho, nove dividido por cento e oitenta dá zero vírgula zero cinco mol, [p=0.2] e {b}zero vírgula zero cinco dividido por zero vírgula vinte e cinco [p=0.1] {c}também dá zero vírgula dois."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}mol por litro é o número de mols dividido pelo volume em litros, [p=0.2] e {b}para sair de gramas por litro, divida pela massa molar."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai {a}juntar água a uma solução [p=0.2] e {b}misturar duas soluções, [p=0.1] descobrindo a nova concentração com uma fórmula de uma linha só. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
