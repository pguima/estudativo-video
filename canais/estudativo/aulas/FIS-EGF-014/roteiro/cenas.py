# Estudativo · FIS-EGF-014 — Praticando: torque e gravitação (Física · Equilíbrio, Gravitação e Fluidos · prática).
# Habilidade: resolver questões de alavancas, planetas e satélites.
# Pré-requisitos: FIS-EGF-001, FIS-EGF-002, FIS-EGF-003, FIS-EGF-013. Próxima: FIS-EGF-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# g = 10 m/s². Contas: 800·0,4 = 1,6·F → 200 N; 80·1,5 = 30·2 + 20·d → d = 3 m; apoio = 1.300 N; Kepler 2 dias × 8 = 16 dias;
# astronauta 800 N a d = 2R → 200 N; v² · r constante: 36 · 1 = v² · 9 → v = 2 km/s.

TITULO = "Praticando: torque e gravitação"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula: [p=0.2] {b}do carrinho de mão [p=0.1] {c}até um satélite. [p=0.3] Em cada uma, {d}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}torque, força vezes braço, medido do eixo; [p=0.2] {b}tê ao quadrado sobre érre ao cubo constante, para quem gira em volta do mesmo astro; [p=0.2] {c}a gravitação, que cai com o quadrado da distância; [p=0.2] e {d}vê ao quadrado vezes érre constante, para satélites. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: carrinho de mão
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Num carrinho de mão, {b}a roda é o eixo. [p=0.2] {c}A carga pesa oitocentos newtons e fica a quarenta centímetros da roda. [p=0.2] {d}As suas mãos seguram os cabos a um metro e sessenta da roda. [p=0.3] {e}Que força você faz para cima?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O torque da carga: oitocentos vezes zero vírgula quatro, [p=0.1] {b}trezentos e vinte newtons vezes metro. [p=0.3] {c}O seu: efe vezes um vírgula seis, igual a trezentos e vinte. [p=0.2] {d}Efe igual a duzentos newtons. [p=0.3] {e}O seu braço é quatro vezes maior, [p=0.1] e a sua força, quatro vezes menor que o peso da carga."),
    # situação 2: gangorra com três pessoas
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Numa gangorra de seis metros, com o apoio no meio, [p=0.2] {b}um pai de oitenta quilos senta a um metro e meio do apoio. [p=0.3] Do outro lado, {c}um filho de trinta quilos senta a dois metros. [p=0.2] {d}A que distância do apoio senta a filha, de vinte quilos, do mesmo lado do irmão, para equilibrar?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Só pesos, então {a}use as massas direto: o dez corta. [p=0.3] {b}Lado do pai: oitenta vezes um vírgula cinco, cento e vinte. [p=0.2] {c}Lado dos filhos: trinta vezes dois, sessenta, [p=0.1] mais vinte vezes dê. [p=0.3] {d}Sessenta mais vinte dê igual a cento e vinte: [p=0.1] {e}vinte dê igual a sessenta, [p=0.1] {f}dê igual a três metros. [p=0.2] {g}Ela senta na ponta da gangorra."),
    dict(id="s09", block="resposta2", text="{a}E o apoio? [p=0.2] Para a força resultante ser zero, [p=0.1] {b}ele segura os três pesos: [p=0.1] {c}oitocentos, mais trezentos, mais duzentos, [p=0.1] {d}mil e trezentos newtons."),
    # situação 3: Kepler
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] {b}Duas luas giram em volta do mesmo planeta. [p=0.2] {c}A lua A dá uma volta em dois dias. [p=0.2] {d}A lua B tem o raio da órbita quatro vezes maior. [p=0.3] {e}Quanto tempo a lua B leva para dar uma volta?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Mesmo planeta, então tê ao quadrado sobre érre ao cubo é o mesmo para as luas. [p=0.3] {b}Raio quatro vezes maior: [p=0.1] {c}o período multiplica por quatro vezes a raiz de quatro, [p=0.1] {d}oito. [p=0.2] {e}Dois dias vezes oito: [p=0.1] {f}dezesseis dias."),
    # atalho
    dict(id="s13", block="atalho", text="Repare num atalho que serviu na primeira e na terceira: [p=0.2] {a}antes de fazer conta, procure o fator. [p=0.3] {b}Braço quatro vezes maior, força quatro vezes menor. [p=0.2] {c}Raio quatro vezes maior, período oito vezes maior. [p=0.3] {d}Com o fator, a conta vira uma multiplicação só. [p=0.2] {e}Ele não ajuda quando há mais de duas forças, como na gangorra de três: [p=0.1] aí, some os torques."),
    # situação 4: peso em órbita
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Um astronauta pesa oitocentos newtons na superfície da Terra. [p=0.3] {c}Quanto ele pesaria a uma altura igual ao raio da Terra? [p=0.2] {d}E por que, dentro da nave em órbita, ele flutua?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}A distância conta do centro da Terra: [p=0.1] {b}um raio até a superfície, mais um raio de altura, [p=0.1] {c}dois raios. [p=0.3] {d}Distância dobrada, força dividida por quatro: [p=0.1] {e}duzentos newtons."),
    dict(id="s17", block="resposta4", text="{a}E ele flutua porque a nave e ele caem juntos, [p=0.1] com a mesma aceleração. [p=0.2] {b}A gravidade está lá: [p=0.1] {c}é ela que segura a nave na órbita."),
    # situação 5: satélites
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] {b}Um satélite gira em volta da Terra a seis quilômetros por segundo. [p=0.3] {c}Outro satélite está numa órbita de raio nove vezes maior. [p=0.2] {d}Qual é a velocidade do segundo?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] {a}Vê ao quadrado vezes érre é constante. [p=0.3] {b}Primeiro satélite: seis ao quadrado vezes um, trinta e seis. [p=0.2] {c}Segundo: vê ao quadrado vezes nove, igual a trinta e seis. [p=0.2] {d}Vê ao quadrado igual a quatro, [p=0.1] {e}vê igual a dois quilômetros por segundo. [p=0.3] {f}Raio nove vezes maior, velocidade três vezes menor."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}torque sempre a partir do eixo; [p=0.2] {b}órbita maior, período maior e velocidade menor; [p=0.2] e {c}a distância da gravitação conta do centro do planeta."),
    dict(id="s22", block="fim", text="Na próxima aula, {a}a trilha vira para os fluidos: [p=0.2] {b}a pressão, e por que a faca afiada corta melhor. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
