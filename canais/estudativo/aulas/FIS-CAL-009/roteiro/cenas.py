# Estudativo · FIS-CAL-009 — Condução de calor (Física · Calor e Termodinâmica · Propagação de calor).
# Habilidade: usar a lei de Fourier como proporção e explicar por que o metal parece mais frio que a madeira à mesma temperatura.
# Pré-requisitos: FIS-CAL-003 (calor, caloria), MAT-RAZ-011 (ler uma fórmula como proporcionalidade). Próxima: FIS-CAL-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Potência e watt (FIS-ENE-002) não estão em "Já ensinado": o fluxo de calor sai em calorias por segundo, e o watt é só citado.
# Fourier: Φ = Q/Δt = k·A·ΔT/L (k condutividade térmica, A área, ΔT diferença de temperatura entre as faces, L espessura).
# Dilatação e mudança de estado (FIS-CAL-002, 004) não estão em "Já ensinado" e não aparecem.

TITULO = "Condução de calor"

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
    dict(id="s01", block="gancho", text="{a}De manhã cedo, encoste a mão numa maçaneta de metal [p=0.1] e depois {b}na porta de madeira. [p=0.3] {c}O metal parece bem mais frio. [p=0.3] Mas os dois passaram a noite no mesmo lugar: [p=0.2] {d}estão na mesma temperatura."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar esse engano [p=0.2] e usar {b}a lei de Fourier, a lei da condução de calor, como proporção."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}calor é a energia que passa do mais quente para o mais frio, medida em calorias; [p=0.2] e {c}ler uma fórmula como proporção: [p=0.1] o que está em cima aumenta o resultado, o que está embaixo diminui. [p=0.3] Se faltar alguma, procure no canal."),
    # condução
    dict(id="s04", block="conducao", text="O calor viaja de {a}três jeitos: [p=0.2] {b}condução, convecção e irradiação. [p=0.3] Esta aula é sobre a primeira. [p=0.3] {c}Ponha uma colher de metal numa panela quente. [p=0.2] Pouco depois, {d}o cabo também esquenta."),
    dict(id="s05", block="conducao", text="{a}As partículas da ponta quente se agitam mais [p=0.2] e {b}esbarram nas vizinhas, [p=0.1] que passam a se agitar também. [p=0.3] {c}A agitação passa de uma para outra, [p=0.2] e {d}nenhuma sai do lugar. [p=0.3] Isso é a {e}condução."),
    dict(id="s06", block="conducao", text="Uns materiais conduzem bem: [p=0.2] são os {a}condutores, como os metais. [p=0.3] Outros conduzem mal: [p=0.2] são os {b}isolantes, como a madeira, o isopor, a lã [p=0.1] e o ar parado."),
    # fluxo e Fourier
    dict(id="s07", block="fourier", text="Para medir a condução, a Física usa o {a}fluxo de calor, [p=0.1] escrito com a letra grega fi: [p=0.2] {b}quanto calor atravessa o material a cada segundo. [p=0.3] É {c}o calor dividido pelo tempo, [p=0.1] {d}em calorias por segundo."),
    dict(id="s08", block="fourier", text="Pense numa {a}parede, com um lado quente e o outro frio. [p=0.3] A lei de Fourier diz: [p=0.2] {b}o fluxo é igual a cá, vezes a área, vezes a diferença de temperatura, dividido pela espessura."),
    dict(id="s09", block="fourier", text="{a}A área da parede vai em metros quadrados. [p=0.2] {b}A espessura, em metros. [p=0.2] {c}A diferença de temperatura é entre os dois lados, em graus Celsius. [p=0.3] E {d}a letra cá é a condutividade térmica: [p=0.2] o número que diz {e}se o material é condutor ou isolante. [p=0.2] Metal tem cá grande; [p=0.1] isopor, cá pequeno."),
    dict(id="s10", block="fourier", text="Leia a fórmula como proporção. [p=0.2] {a}Dobre a área: o fluxo dobra. [p=0.2] {b}Dobre a diferença de temperatura: o fluxo dobra. [p=0.3] {c}Dobre a espessura: o fluxo cai pela metade. [p=0.3] É por isso que {d}parede grossa segura melhor o calor."),
    # metal frio
    dict(id="s11", block="metal", text="De volta à maçaneta. [p=0.2] {a}A pele da sua mão está a uns trinta e poucos graus; [p=0.2] {b}o metal e a madeira, a vinte. [p=0.3] Nos dois casos, {c}o calor sai da sua mão. [p=0.3] Mas o metal, com cá grande, {d}tira esse calor muito mais depressa."),
    dict(id="s12", block="metal", text="{a}Sua pele não mede a temperatura do objeto: [p=0.2] ela sente {b}a rapidez com que perde calor. [p=0.3] Perdeu rápido, {c}parece frio. [p=0.3] {d}Por isso o metal engana."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é dizer que {a}o cobertor esquenta. [p=0.3] Ele não produz calor nenhum. [p=0.2] {b}O calor vem do seu corpo, [p=0.2] e o cobertor, cheio de ar parado, {c}deixa esse calor sair devagar. [p=0.3] {d}Cobertor em cima de uma pedra de gelo não esquenta o gelo."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho: [p=0.2] {a}não calcule o fluxo, calcule o fator. [p=0.3] Multiplique pelo que muda em cima [p=0.1] e divida pelo que muda embaixo. [p=0.3] {b}A área triplica e a espessura dobra? [p=0.2] {c}Três dividido por dois: o fluxo fica uma vez e meia maior. [p=0.3] {d}Não compensa quando a questão dá todos os valores e pede o fluxo em números: [p=0.2] aí, faça a conta inteira."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa caixa de isopor, você {a}dobra a espessura das paredes. [p=0.3] E, num dia mais fresco, {b}a diferença de temperatura entre dentro e fora cai pela metade. [p=0.3] {c}O que acontece com o fluxo de calor?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A espessura está embaixo: dobrou, divide por dois. [p=0.3] {b}A diferença de temperatura está em cima: caiu pela metade, divide por dois de novo. [p=0.3] {c}Dois vezes dois dá quatro: [p=0.2] {d}o fluxo fica quatro vezes menor."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}na condução, a agitação passa de partícula em partícula; [p=0.2] {b}no fluxo de calor, a área e a diferença de temperatura multiplicam, e a espessura divide; [p=0.2] e {c}o metal parece frio porque tira o calor da mão mais depressa."),
    dict(id="s19", block="fim", text="Na próxima aula, os outros dois jeitos: [p=0.2] {a}a convecção, que faz as brisas do mar, [p=0.2] e {b}a irradiação, que traz o calor do Sol. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
