# Estudativo · QUI-CAL-004 — Lei de Proust e proporção em mols (Química · Cálculos Químicos · Estequiometria).
# Habilidade: ler 2 H₂ + O₂ → 2 H₂O em mols e dizer pela lei de Proust que, se 2 g de hidrogênio pedem 16 g de oxigênio,
# 4 g pedem 32 g. Pré-requisitos: QUI-CAL-002, QUI-INO-008, MAT-RAZ-002. Próxima: QUI-CAL-005 (massa a massa).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# Primeira aula do módulo Estequiometria: guarda a linguagem visual da trilha (veja o visual.py).
# Contas: 2·2 = 4 g H₂; 1·32 = 32 g O₂; 2·18 = 36 g H₂O; 4 + 32 = 36; 4 : 32 = 1 : 8; receita 1 : 8 : 9.
# Questão: N₂ + 3 H₂ → 2 NH₃ = 28 g : 6 g : 34 g; 56 g de N₂ = dobro → 12 g de H₂ e 68 g de NH₃.
# Porcentagem e composição percentual NÃO estão em "Já ensinado" desta aula: não usar.

TITULO = "Lei de Proust e proporção em mols"

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
    dict(id="s01", block="gancho", text="{a}Separe a água pura de um rio, da chuva ou do gelo de uma geleira. [p=0.3] {b}Em toda ela, para cada grama de hidrogênio, há oito de oxigênio. [p=0.3] Sempre. [p=0.2] {c}Essa receita fixa tem nome de lei, [p=0.1] e é a base de todas as contas de reação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}ler uma equação em mols, [p=0.2] {c}usar a lei de Proust para prever massas [p=0.2] e ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o mol e a massa molar; [p=0.2] {c}uma equação balanceada, com os coeficientes na frente; [p=0.2] e {d}achar o termo que falta numa proporção. [p=0.3] Se faltar alguma, procure no canal."),
    # ler em mols
    dict(id="s04", block="mols", text="Veja a formação da água: {a}dois agá dois mais ó dois forma dois agá dois ó. [p=0.3] {b}Os coeficientes contam moléculas: [p=0.1] {c}duas de hidrogênio para uma de oxigênio, [p=0.1] {d}formando duas de água."),
    dict(id="s05", block="mols", text="{a}Multiplique tudo por seis vezes dez elevado a vinte e três, [p=0.1] e a proporção não muda. [p=0.3] {b}Por isso, os coeficientes também contam mols: [p=0.2] {c}dois mols de agá dois [p=0.1] {d}reagem com um mol de ó dois [p=0.1] {e}e formam dois mols de água."),
    # em gramas
    dict(id="s06", block="massas", text="{a}De mol para grama, use a massa molar. [p=0.2] {b}Agá dois tem dois gramas por mol: dois mols dão quatro gramas. [p=0.2] {c}Ó dois tem trinta e dois: um mol dá trinta e dois gramas. [p=0.2] {d}Água, dezoito: dois mols dão trinta e seis gramas."),
    dict(id="s07", block="massas", text="{a}Quatro mais trinta e dois dá trinta e seis: [p=0.2] {b}a massa se conserva, como manda a lei de Lavoisier."),
    # Proust
    dict(id="s08", block="proust", text="Repare na proporção. [p=0.2] {a}Quatro gramas de hidrogênio para trinta e dois de oxigênio. [p=0.2] {b}Divida cada um por quatro: [p=0.1] {c}um para oito. [p=0.3] {d}Essa é a lei de Proust: [p=0.1] {e}numa substância, e numa reação, a proporção entre as massas é sempre a mesma."),
    dict(id="s09", block="proust", text="{a}Se dois gramas de hidrogênio pedem dezesseis de oxigênio, [p=0.2] {b}quatro gramas pedem quanto? [p=0.3] {c}O hidrogênio dobrou, então o oxigênio dobra: [p=0.1] {d}trinta e dois gramas. [p=0.3] {e}E a água também dobra: de dezoito para trinta e seis."),
    dict(id="s10", block="proust", text="{a}Numa tabela, cada linha é a mesma receita, maior ou menor. [p=0.3] {b}Um grama de hidrogênio com oito de oxigênio dá nove de água. [p=0.2] {c}Dois com dezesseis dá dezoito. [p=0.2] {d}Quatro com trinta e dois dá trinta e seis."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}ler os coeficientes como gramas. [p=0.3] {b}Dois agá dois mais ó dois não quer dizer dois gramas de hidrogênio com um grama de oxigênio. [p=0.3] {c}Isso daria dois para um, [p=0.1] e a receita certa é um para oito. [p=0.3] Coeficiente conta mols. [p=0.2] {d}Para ter gramas, multiplique pela massa molar."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho: [p=0.1] {a}simplifique a receita até o menor número inteiro, [p=0.1] {b}um para oito para nove. [p=0.2] {c}Divida a massa dada pelo número dela na receita, [p=0.1] e multiplique pelo número do que você quer. [p=0.3] {d}Quarenta gramas de oxigênio? [p=0.2] {e}Quarenta dividido por oito dá cinco: [p=0.1] cinco gramas de hidrogênio. [p=0.2] {f}Cinco vezes nove dá quarenta e cinco gramas de água."),
    dict(id="s13", block="atalho", text="{a}Funciona porque a lei de Proust garante que a proporção não muda. [p=0.3] {b}Não compensa quando os reagentes não estão na proporção certa [p=0.1] e um deles sobra: [p=0.1] {c}isso é assunto de outra aula, a do reagente em excesso."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Na fabricação da amônia, {a}ene dois mais três agá dois forma dois ene agá três. [p=0.3] {b}Leia essa equação em mols. [p=0.2] {c}Vinte e oito gramas de ene dois reagem com seis gramas de agá dois. [p=0.2] {d}Quanto hidrogênio reage com cinquenta e seis gramas de ene dois?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Em mols: um mol de ene dois reage com três mols de agá dois [p=0.1] {b}e forma dois mols de amônia. [p=0.3] {c}Cinquenta e seis gramas é o dobro de vinte e oito. [p=0.2] {d}Pela lei de Proust, o hidrogênio também dobra: [p=0.1] {e}doze gramas. [p=0.3] {f}E a amônia? [p=0.1] Vinte e oito mais seis dá trinta e quatro gramas; [p=0.1] o dobro dá sessenta e oito."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}os coeficientes contam mols; [p=0.2] {b}a massa de cada substância é o coeficiente vezes a massa molar; [p=0.2] {c}e a proporção das massas nunca muda."),
    dict(id="s18", block="fim", text="Na próxima aula, você junta tudo numa conta de massa para massa: [p=0.2] {a}quanto gás carbônico sai da queima do etanol. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
