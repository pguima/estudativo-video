# Estudativo · MAT-CNT-012 — Probabilidade com contagem (Matemática · Contagem e Probabilidade · Probabilidade: noções).
# Habilidade: achar a chance de soma 7 em dois dados (6/36 = 1/6) e a de um sorteio de comissão, contando favoráveis e possíveis.
# Pré-requisitos: MAT-CNT-011 (favoráveis sobre possíveis), MAT-CNT-008 (combinação), MAT-CNT-001 (casinhas). Próxima: MAT-CNT-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questões inéditas, criadas para esta aula. Evento complementar e "pelo menos" ficam para MAT-CNT-013.

TITULO = "Probabilidade com contagem"

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
    dict(id="s01", block="gancho", text="{a}Dois dados. [p=0.2] Qual a chance de a soma dar {b}sete? [p=0.3] Muita gente pensa: [p=0.2] as somas vão de dois a doze. [p=0.2] São onze somas. [p=0.2] Então, {c}um onze avos. [p=0.3] {d}Errado. [p=0.2] A chance é {e}um sexto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa a contagem para achar probabilidades [p=0.2] e leva um {b}atalho para sorteios."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a probabilidade: favoráveis sobre possíveis, [p=0.2] quando todos os resultados têm a mesma chance. [p=0.3] E as ferramentas de contagem: [p=0.2] {b}as casinhas [p=0.2] e {c}a combinação. [p=0.3] Se faltar alguma, procure no canal."),
    # possíveis
    dict(id="s04", block="dados", text="Pense nos dados com cores diferentes: [p=0.2] {a}um branco e um vermelho. [p=0.3] O branco tem {b}seis resultados. [p=0.2] O vermelho também tem {c}seis. [p=0.2] Cada dado é uma etapa, e o resultado precisa de cada um deles: [p=0.2] {d}seis vezes seis dá trinta e seis resultados possíveis."),
    dict(id="s05", block="dados", text="Veja na {a}tabela. [p=0.2] {b}Nas linhas, o dado branco. [p=0.2] {c}Nas colunas, o vermelho. [p=0.2] Cada quadradinho é {d}um resultado, como branco três e vermelho quatro. [p=0.3] Todos têm a mesma chance."),
    # favoráveis
    dict(id="s06", block="dados", text="Agora, os que somam sete. [p=0.2] {a}Branco um e vermelho seis. [p=0.2] {b}Branco dois e vermelho cinco. [p=0.2] {c}Três e quatro. [p=0.2] {d}Quatro e três. [p=0.2] {e}Cinco e dois. [p=0.2] {f}Seis e um. [p=0.3] Na tabela, é {g}uma diagonal inteira: seis quadradinhos."),
    dict(id="s07", block="dados", text="{a}Seis favoráveis em trinta e seis possíveis: [p=0.2] seis trinta e seis avos. [p=0.2] Divida em cima e embaixo por seis, [p=0.2] e dá {b}um sexto."),
    dict(id="s08", block="dados", text="E por que o um onze avos do começo errou? [p=0.2] Porque {a}as somas não têm a mesma chance. [p=0.3] Soma dois só sai com {b}um e um: [p=0.2] um quadradinho. [p=0.2] Soma sete sai de {c}seis jeitos. [p=0.3] Probabilidade se conta em {d}resultados de mesma chance, [p=0.2] não em somas."),
    # sorteio
    dict(id="s09", block="sorteio", text="A contagem também resolve sorteios. [p=0.2] Um grupo de {a}oito pessoas vai sortear {b}uma comissão de três. [p=0.3] Qual a chance de {c}Ana estar na comissão?"),
    dict(id="s10", block="sorteio", text="Possíveis: {a}comissões de três entre oito. [p=0.2] A ordem não importa: combinação. [p=0.2] {b}Oito vezes sete vezes seis, dividido por três fatorial, dá cinquenta e seis."),
    dict(id="s11", block="sorteio", text="Favoráveis: as comissões {a}com Ana dentro. [p=0.2] Ana já tem lugar. [p=0.2] Falta {b}escolher duas pessoas entre as sete que sobram: [p=0.2] {c}sete vezes seis dividido por dois dá vinte e um."),
    dict(id="s12", block="sorteio", text="{a}Vinte e um cinquenta e seis avos. [p=0.2] Divida em cima e embaixo por sete, [p=0.2] e dá {b}três oitavos. [p=0.3] Um oitavo é doze vírgula cinco por cento. [p=0.2] Três oitavos é o triplo: [p=0.2] doze vírgula cinco mais doze vírgula cinco dá vinte e cinco, [p=0.2] e mais doze vírgula cinco dá {c}trinta e sete vírgula cinco por cento."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}tratar os dados como se fossem iguais. [p=0.2] A pessoa lista {b}um e seis. [p=0.2] Dois e cinco. [p=0.2] Três e quatro. [p=0.2] E para aí. [p=0.3] Dá {c}três trinta e seis avos, [p=0.2] que simplifica para um doze avos. [p=0.3] Mas {d}branco um com vermelho seis [p=0.2] é diferente de {e}branco seis com vermelho um. [p=0.2] Na tabela, são quadradinhos diferentes."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para sorteios: {a}a chance de uma pessoa ser sorteada é vagas sobre pessoas. [p=0.3] {b}Três vagas para oito pessoas: três oitavos. [p=0.2] Sem combinação nenhuma."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o sorteio é justo: [p=0.2] ninguém tem mais chance que ninguém, [p=0.2] e as vagas se dividem igualmente entre todos. [p=0.3] {b}Não compensa quando a pergunta envolve mais de uma pessoa, [p=0.2] como Ana e Bia juntas: [p=0.2] aí, {c}conte favoráveis e possíveis."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Dois dados: qual a chance de a soma dar oito? [p=0.3] E {b}seis amigos sorteiam dois ingressos para um show. [p=0.2] {c}Qual a chance de Ana e Bia serem as sorteadas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Soma oito: {a}dois e seis. [p=0.2] Três e cinco. [p=0.2] Quatro e quatro. [p=0.2] Cinco e três. [p=0.2] Seis e dois. [p=0.3] {b}São cinco favoráveis em trinta e seis possíveis. [p=0.2] A chance é {c}cinco trinta e seis avos, [p=0.2] uma fração que não simplifica. [p=0.3] Quatro e quatro aparece uma vez só: [p=0.2] {d}trocar as cores não muda nada."),
    dict(id="s19", block="resposta", text="Nos ingressos, os possíveis são {a}duplas entre seis amigos. [p=0.2] {b}Seis vezes cinco dividido por dois dá quinze. [p=0.3] Favoráveis: {c}só uma dupla, Ana com Bia. [p=0.2] A chance é {d}um quinze avos. [p=0.3] Aqui o atalho não serve: [p=0.2] a pergunta envolve {e}duas pessoas ao mesmo tempo."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}conte os possíveis, [p=0.2] {b}conte os favoráveis [p=0.2] e {c}divida. [p=0.3] Sempre com resultados de mesma chance."),
    dict(id="s21", block="fim", text="Na próxima aula, a pergunta tem um {a}pelo menos: [p=0.2] a chance de sair {b}pelo menos uma cara em três moedas. [p=0.3] E o caminho mais curto é {c}olhar para o que não pode acontecer. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
