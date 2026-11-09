# Estudativo · FIS-MAG-002 — Campo criado por corrente (Física · Magnetismo · Magnetismo e indução).
# Habilidade: achar direção e sentido do campo de um fio com a regra da mão direita e calcular fio, espira e solenoide por proporção.
# Pré-requisitos: FIS-MAG-001, FIS-ELE-008, MAT-RAZ-011. Próxima: FIS-MAG-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fato do gancho: Hans Christian Oersted, 1820, agulha desviada por um fio com corrente.
# μ₀ = 4π × 10⁻⁷ T·m/A, narrado "mi zero"; atalho μ₀/2π = 2 × 10⁻⁷. Sem trigonometria (MAT-TRI não está em "Já ensinado").

TITULO = "Campo criado por corrente"

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
    dict(id="s01", block="gancho", text="{a}Em mil oitocentos e vinte, o professor Oersted ligou um fio numa bateria, [p=0.2] perto de uma bússola. [p=0.3] {b}E a agulha girou. [p=0.3] Sem nenhum ímã por perto. [p=0.3] {c}A corrente elétrica cria campo magnético."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar o sentido desse campo {b}com a mão direita, [p=0.2] e {c}calcular o campo de um fio, de uma espira e de uma bobina por proporção."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Corrente é carga passando por segundo, em ampère. [p=0.3] E {c}o norte da bússola aponta no sentido do campo bê, que se mede em tesla. [p=0.3] Se faltar alguma, procure no canal."),
    # fio
    dict(id="s04", block="fio", text="Comece pelo fio reto e comprido. [p=0.2] {a}Espalhe bússolas em volta dele. [p=0.3] {b}Com a corrente ligada, as agulhas formam um círculo. [p=0.3] {c}As linhas de campo de um fio são círculos em volta dele."),
    dict(id="s05", block="fio", text="E o sentido sai da {a}regra da mão direita. [p=0.2] {b}Segure o fio com a mão direita, com o polegar no sentido da corrente. [p=0.3] {c}Os outros dedos dobram em volta do fio, [p=0.2] e {d}apontam o sentido do campo."),
    # símbolos
    dict(id="s06", block="simbolos", text="Na prova, o campo muitas vezes {a}fura a folha. [p=0.2] Por isso, existem dois símbolos. [p=0.3] {b}Um ponto num círculo é o campo saindo da folha, [p=0.2] como a ponta de uma flecha vindo na sua direção. [p=0.3] {c}Um xis num círculo é o campo entrando, [p=0.2] como a cauda da flecha indo embora."),
    dict(id="s07", block="simbolos", text="{a}Fio deitado na folha, corrente para cima. [p=0.2] {b}Do lado direito do fio, o campo entra na folha. [p=0.2] {c}Do lado esquerdo, ele sai. [p=0.3] Confira com a mão: [p=0.1] {d}polegar para cima, [p=0.1] e os dedos entram à direita e voltam pela esquerda."),
    # intensidade
    dict(id="s08", block="valor", text="Quanto vale esse campo? [p=0.2] {a}Bê igual a mi zero vezes i, [p=0.1] dividido por dois pi vezes dê. [p=0.3] {b}I é a corrente, em ampère. [p=0.2] {c}Dê é a distância até o fio, em metro. [p=0.2] {d}E mi zero é uma constante do vácuo: [p=0.1] quatro pi vezes dez elevado a menos sete."),
    dict(id="s09", block="valor", text="Leia como proporção. [p=0.2] {a}A corrente está em cima: [p=0.1] dobrou a corrente, dobrou o campo. [p=0.3] {b}A distância está embaixo: [p=0.1] dobrou a distância, o campo cai pela metade."),
    dict(id="s10", block="valor", text="Um exemplo. [p=0.2] {a}Corrente de dez ampères, ponto a vinte centímetros, [p=0.1] que são zero vírgula dois metro. [p=0.3] {b}O pi de cima corta com o de baixo, [p=0.2] e {c}quatro dividido por dois dá dois. [p=0.3] Fica {d}dois vezes dez a menos sete, vezes dez, dividido por zero vírgula dois. [p=0.2] {e}Dez elevado a menos cinco tesla."),
    # espira e solenoide
    dict(id="s11", block="espira", text="Agora, {a}dobre o fio num círculo: [p=0.2] é uma espira. [p=0.3] No centro dela, {b}bê igual a mi zero vezes i, dividido por dois erre, [p=0.2] e {c}erre é o raio, a distância do centro até o fio. [p=0.3] Mesma leitura: [p=0.1] {d}mais corrente, mais campo; [p=0.1] raio maior, campo menor."),
    dict(id="s12", block="espira", text="{a}Enrole muitas espiras em fila: [p=0.2] é o solenoide, uma bobina. [p=0.3] {b}Dentro dele, bê igual a mi zero vezes ene vezes i, dividido por éle. [p=0.2] {c}Ene é o número de espiras, [p=0.1] e éle é o comprimento da bobina. [p=0.3] {d}Dentro, o campo fica reto e igual em todo ponto."),
    dict(id="s13", block="espira", text="E a bobina {a}vira um ímã em barra. [p=0.2] Para achar o norte, {b}dobre os dedos da mão direita no sentido da corrente nas espiras. [p=0.3] {c}O polegar aponta o lado do norte, [p=0.2] por onde as linhas saem."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que, dobrando a distância, o campo do fio cai para um quarto. [p=0.3] {b}Isso é da força entre cargas, que tem a distância ao quadrado. [p=0.3] {c}No fio, a distância não tem quadrado: [p=0.2] {d}dobrou a distância, o campo cai pela metade."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Mi zero dividido por dois pi dá sempre dois vezes dez a menos sete. [p=0.3] Então, para o fio, {b}bê igual a dois vezes dez a menos sete, vezes i, dividido por dê. [p=0.3] {c}Sem pi na conta."),
    dict(id="s16", block="atalho", text="E muita questão {a}nem pede o número: [p=0.2] pede quantas vezes o campo muda. [p=0.3] {b}Multiplique pelo que mudou em cima [p=0.1] e divida pelo que mudou embaixo. [p=0.3] {c}Só não esqueça: a fórmula é do fio longo. [p=0.2] Ela vale para pontos perto do fio, comparado com o comprimento dele."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um fio longo, deitado na folha, leva seis ampères para cima. [p=0.3] {b}A três centímetros dele, o campo vale quatro vezes dez a menos cinco tesla. [p=0.3] {c}Quanto vale o campo a seis centímetros, se a corrente subir para dezoito ampères? [p=0.3] E mais: {d}à direita do fio, o campo entra ou sai da folha?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}A corrente foi de seis para dezoito: [p=0.1] {b}vezes três, em cima. [p=0.2] {c}A distância foi de três para seis: [p=0.1] {d}vezes dois, embaixo. [p=0.3] {e}Três dividido por dois, um vírgula cinco."),
    dict(id="s20", block="resposta", text="{a}Quatro vezes dez a menos cinco, vezes um vírgula cinco: [p=0.2] {b}seis vezes dez a menos cinco tesla. [p=0.3] E o sentido: {c}polegar para cima, [p=0.1] {d}os dedos entram na folha do lado direito. [p=0.2] {e}O campo entra."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}corrente cria campo, [p=0.2] {b}o sentido sai da mão direita, [p=0.2] e {c}o campo cresce com a corrente e cai com a distância. [p=0.3] Na próxima aula, o caminho inverso: [p=0.2] {d}a força que o campo faz numa carga em movimento."),
    dict(id="s22", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
