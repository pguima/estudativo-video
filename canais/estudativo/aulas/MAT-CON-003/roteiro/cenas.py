# Estudativo · MAT-CON-003 — Problemas com diagrama de Venn (Matemática · Conjuntos).
# Habilidade: descobrir quantos alunos não praticam nenhum de dois ou de três esportes, preenchendo o diagrama de dentro para fora, e usar n(A ∪ B) = n(A) + n(B) − n(A ∩ B).
# Pré-requisitos: MAT-CON-002 (união e interseção), MAT-EQU-008 (equação, mesmo nos dois lados). Próxima: MAT-CON-004.
# Questões e turmas inéditas, criadas para esta aula.
# Dois conjuntos: turma de 40; futebol 22, vôlei 17, ambos 7 → só futebol 15, só vôlei 10, união 32, nenhum 8. Erro: 40 − 22 − 17 = 1.
# Três conjuntos: turma de 50; F 19, V 20, B 16; F∩V 6, F∩B 5, V∩B 7, os três 2 →
#   só F e V 4, só F e B 3, só V e B 5; só F 10, só V 9, só B 6; total 39; nenhum 11.
# Questão: 60 pessoas, mapas 35, música 30, nenhum 10 → união 50; 35 + 30 − x = 50 → x = 15; só mapas 20.
# Visual: Venn de 2 conjuntos (E.venn) preenchido do meio para fora; Venn de 3 conjuntos com os 7 números + o 11 fora; fórmula n(A ∪ B).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Problemas com diagrama de Venn"

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
    dict(id="s01", block="gancho", text="Numa turma de {a}quarenta alunos, [p=0.2] {b}vinte e dois jogam futebol, [p=0.2] {c}dezessete jogam vôlei [p=0.2] e {d}sete jogam ambos. [p=0.3] Quantos não jogam nenhum? [p=0.3] Muita gente tira tudo do quarenta e acha {e}um. [p=0.2] A resposta é {f}oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve esse tipo de problema com dois e com três esportes, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}interseção e união no diagrama de Venn, [p=0.2] e {c}resolver equação fazendo o mesmo nos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # dois conjuntos
    dict(id="s04", block="dois", text="O segredo é {a}preencher o diagrama de dentro para fora. [p=0.3] Comece pela {b}interseção: [p=0.2] {c}sete alunos jogam ambos. [p=0.2] Esse sete vai {d}no meio."),
    dict(id="s05", block="dois", text="Dos vinte e dois do futebol, sete já estão no meio. [p=0.2] {a}Só futebol: vinte e dois menos sete dá quinze. [p=0.3] Dos dezessete do vôlei, sete também já estão lá. [p=0.2] {b}Só vôlei: dezessete menos sete dá dez."),
    dict(id="s06", block="dois", text="Some os pedaços: {a}quinze mais sete mais dez dá trinta e dois. [p=0.2] São os que jogam pelo menos um esporte. [p=0.3] O resto fica {b}fora dos círculos: [p=0.2] {c}quarenta menos trinta e dois dá oito alunos."),
    # fórmula
    dict(id="s07", block="formula", text="Na prova, o número de elementos de um conjunto á se escreve {a}ene de á. [p=0.3] E existe uma fórmula para a união: [p=0.2] {b}ene da união é ene de á, mais ene de bê, menos ene da interseção."),
    dict(id="s08", block="formula", text="Por que esse menos? [p=0.2] Quem joga ambos foi contado {a}duas vezes: [p=0.2] {b}uma no futebol e outra no vôlei. [p=0.3] Então tira uma vez. [p=0.2] {c}Vinte e dois mais dezessete dá trinta e nove, [p=0.2] {d}menos sete dá trinta e dois. [p=0.2] Igual ao diagrama."),
    # três conjuntos
    dict(id="s09", block="tres", text="Com três esportes, o método é o mesmo. [p=0.2] Turma de {a}cinquenta alunos. [p=0.2] {b}Dezenove jogam futebol, [p=0.2] {c}vinte jogam vôlei, [p=0.2] {d}dezesseis jogam basquete."),
    dict(id="s10", block="tres", text="{a}Seis jogam futebol e vôlei. [p=0.2] {b}Cinco jogam futebol e basquete. [p=0.2] {c}Sete jogam vôlei e basquete. [p=0.3] E {d}só dois jogam os três esportes. [p=0.3] Atenção: os seis de futebol e vôlei {e}já incluem quem joga tudo."),
    dict(id="s11", block="tres", text="De dentro para fora. [p=0.2] {a}No centro, o dois. [p=0.3] Em cada dupla de esportes, desconte o centro. [p=0.2] {b}Futebol e vôlei: seis menos dois dá quatro. [p=0.2] {c}Futebol e basquete: cinco menos dois dá três. [p=0.2] {d}Vôlei e basquete: sete menos dois dá cinco."),
    dict(id="s12", block="tres", text="Falta quem joga um esporte só. [p=0.2] {a}Futebol: dezenove menos quatro, menos três, menos dois. [p=0.2] Sobram {b}dez. [p=0.3] {c}Vôlei: vinte menos quatro, menos cinco, menos dois: [p=0.2] {d}nove. [p=0.3] {e}Basquete: dezesseis menos três, menos cinco, menos dois: [p=0.2] {f}seis."),
    dict(id="s13", block="tres", text="Some as sete partes: {a}trinta e nove alunos jogam alguma coisa. [p=0.3] {b}Cinquenta menos trinta e nove: [p=0.2] {c}onze não jogam nenhum dos esportes."),
    # erro
    dict(id="s14", block="erro", text="Volte ao erro do começo. [p=0.2] {a}Quarenta menos vinte e dois menos dezessete dá um. [p=0.3] Só que os sete que jogam ambos {b}saíram duas vezes, [p=0.2] uma em cada esporte. [p=0.3] {c}Devolva os sete: um mais sete dá oito. [p=0.2] {d}É a resposta certa."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}a fórmula também roda ao contrário. [p=0.3] Se a questão dá {b}quem não joga nenhum e esconde quem joga ambos, [p=0.2] {c}chame a interseção de xis [p=0.2] e resolva a equação."),
    dict(id="s16", block="atalho", text="Funciona porque a fórmula é {a}uma igualdade: [p=0.2] sabendo três números, a equação dá o quarto. [p=0.3] {b}Não compensa com três conjuntos: [p=0.2] a fórmula fica comprida demais. [p=0.2] Ali, {c}preencha o diagrama de dentro para fora."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Numa pesquisa com {a}sessenta pessoas, [p=0.2] {b}trinta e cinco usam um aplicativo de mapas, [p=0.2] {c}trinta usam um aplicativo de música [p=0.2] e {d}dez não usam nenhum. [p=0.3] {e}Quantas usam ambos? [p=0.2] {f}E quantas usam só o de mapas?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Se dez não usam nenhum, {a}a união tem sessenta menos dez dá cinquenta. [p=0.3] Chame de xis quem usa ambos. [p=0.2] Pela fórmula: {b}trinta e cinco mais trinta, menos xis, igual a cinquenta. [p=0.2] {c}Sessenta e cinco menos xis igual a cinquenta."),
    dict(id="s20", block="resposta", text="{a}Some xis nos dois lados: sessenta e cinco igual a cinquenta mais xis. [p=0.2] {b}Tire cinquenta: xis igual a quinze. [p=0.3] {c}Quinze pessoas usam ambos. [p=0.3] E só o de mapas: {d}trinta e cinco menos quinze dá vinte pessoas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}preencha de dentro para fora [p=0.2] e {b}tire uma vez a interseção, que foi contada duas vezes."),
    dict(id="s22", block="fim", text="Na próxima aula, os conjuntos mais famosos da matemática: [p=0.2] os {a}naturais, os inteiros e os racionais, [p=0.2] e por que {b}uma dízima também é fração. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
