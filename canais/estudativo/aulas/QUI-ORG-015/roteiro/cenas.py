# Estudativo · QUI-ORG-015 — Isomeria geométrica: cis e trans (Química · Química Orgânica · Propriedades físicas e isomeria).
# Habilidade: dizer quando existe isomeria cis-trans e reconhecer o isômero cis e o trans do but-2-eno.
# Pré-requisitos: QUI-ORG-014. Próxima: QUI-ORG-016 (isomeria óptica: carbono quiral, 2 elevado a n, talidomida).
# Marcas: {cue} animação · [p=0.2] pausa. Números e fórmulas por extenso; nomes IUPAC falados: but-2-eno = "but dois eno".
# Fatos: cis-but-2-eno ferve a 3,7 °C e trans-but-2-eno a 0,9 °C (CRC); os dois são C4H8. A ligação simples gira; a dupla não.
# Gordura trans = gordura com dupla em trans na cadeia (a natural costuma ser cis). Anel também dá cis-trans: fica fora da aula.
# Questão inédita, criada para esta aula: pent-2-eno (tem cis-trans) × 2-metilbut-2-eno (não tem: C2 com dois CH3).

TITULO = "Isomeria geométrica: cis e trans"

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
    dict(id="s01", block="gancho", text="{a}Gordura trans. [p=0.3] Você já viu esse nome no rótulo. [p=0.3] {b}O trans diz como os átomos ficam arrumados em volta de uma ligação dupla. [p=0.3] {c}Mesma fórmula, mesmas ligações, [p=0.2] e mesmo assim {d}duas substâncias diferentes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer {b}quando existe isomeria cis e trans [p=0.2] e reconhecer {c}o cis e o trans do but dois eno. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre da aula de isomeria plana: [p=0.2] {a}isômeros têm a mesma fórmula molecular, mas estruturas diferentes. [p=0.3] E do nome dos hidrocarbonetos: [p=0.2] {b}o but dois eno tem quatro carbonos, com a dupla começando no carbono dois."),
    # giro
    dict(id="s04", block="giro", text="Primeiro, uma pergunta. [p=0.2] {a}Uma ligação simples deixa os átomos girarem? [p=0.3] Deixa. [p=0.2] Pense em {b}duas tábuas presas por um prego só: [p=0.2] {c}uma gira em volta da outra."),
    dict(id="s05", block="giro", text="{a}Com dois pregos, nada gira. [p=0.3] A ligação dupla é assim. [p=0.2] {b}Os dois carbonos da dupla ficam travados, [p=0.2] e o que está preso a cada um {c}fica de um lado ou do outro."),
    # cis e trans
    dict(id="s06", block="cistrans", text="Veja o but dois eno: [p=0.1] {a}cê agá três, cê agá, dupla, cê agá, cê agá três. [p=0.3] Cada carbono da dupla tem {b}dois ligantes, quer dizer, duas coisas presas a ele: [p=0.2] {c}um hidrogênio e um grupo cê agá três."),
    dict(id="s07", block="cistrans", text="{a}Os dois grupos cê agá três podem ficar do mesmo lado da dupla. [p=0.2] Esse é o {b}cis, palavra do latim que quer dizer deste lado. [p=0.3] {c}Ou podem ficar em lados opostos: [p=0.2] é o {d}trans, que quer dizer do outro lado."),
    dict(id="s08", block="cistrans", text="Para passar de um para o outro, {a}seria preciso girar a dupla, [p=0.2] e ela não gira sem se quebrar. [p=0.3] Por isso, são {b}duas substâncias diferentes, com a mesma fórmula, {c}cê quatro agá oito. [p=0.3] Até a temperatura em que fervem muda: [p=0.2] {d}o cis ferve perto de quatro graus, [p=0.2] {e}o trans, perto de um grau."),
    # regra
    dict(id="s09", block="regra", text="Então, quando existe isomeria cis e trans? [p=0.2] São duas condições. [p=0.2] {a}Primeira: uma ligação dupla entre carbonos, que não gira. [p=0.3] {b}Segunda: cada carbono da dupla precisa ter dois ligantes diferentes entre si."),
    dict(id="s10", block="regra", text="No but dois eno, {a}o carbono dois tem hidrogênio e cê agá três: diferentes. [p=0.2] {b}O carbono três também. [p=0.3] {c}As duas condições valem, então existe cis e trans."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}achar que toda ligação dupla tem cis e trans. [p=0.3] Veja o but um eno: [p=0.1] {b}cê agá dois, dupla, cê agá, cê agá dois, cê agá três."),
    dict(id="s12", block="erro", text="{a}O carbono um tem dois hidrogênios. [p=0.2] {b}Troque um pelo outro de lugar: [p=0.2] {c}a molécula continua igual. [p=0.3] Não dá para formar um cis e um trans diferentes. [p=0.2] {d}Basta um carbono da dupla com dois ligantes iguais, e a isomeria cis e trans some."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}olhe um carbono da dupla de cada vez. [p=0.2] {b}Achou dois ligantes iguais no mesmo carbono? [p=0.2] Pare: {c}não tem isomeria cis e trans. [p=0.3] Funciona porque {d}trocar dois iguais de lugar não muda nada."),
    dict(id="s14", block="atalho", text="{a}Só tome cuidado ao comparar: [p=0.2] olhe o grupo inteiro, não só o primeiro átomo. [p=0.2] {b}Cê agá três e cê agá dois cê agá três começam com carbono, [p=0.2] mas {c}são grupos diferentes."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Qual destes tem isomeria cis e trans: [p=0.2] {b}o pent dois eno, [p=0.2] ou {c}o dois metil but dois eno? [p=0.3] {d}E, no que tiver, como fica o isômero cis?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Comece pelo dois metil but dois eno. [p=0.2] {a}O carbono dois tem dois grupos cê agá três: [p=0.2] {b}iguais. [p=0.2] Pelo atalho, {c}pare: não tem cis e trans."),
    dict(id="s18", block="resposta", text="{a}No pent dois eno, o carbono dois tem hidrogênio e cê agá três, [p=0.2] {b}e o carbono três tem hidrogênio e cê agá dois cê agá três. [p=0.2] Os carbonos dois e três têm, cada um, ligantes diferentes: {c}existe cis e trans. [p=0.3] {d}No cis, os dois grupos de carbono ficam do mesmo lado da dupla."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}a dupla não gira, [p=0.2] e, se {b}cada carbono dela tem dois ligantes diferentes, [p=0.1] existem {c}o cis, com os grupos do mesmo lado, [p=0.1] e {d}o trans, em lados opostos. [p=0.3] {e}O trans da gordura trans vem daí."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver a isomeria óptica, [p=0.2] a do {a}carbono quiral, [p=0.2] com moléculas que são {b}a imagem uma da outra no espelho, como as suas mãos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
