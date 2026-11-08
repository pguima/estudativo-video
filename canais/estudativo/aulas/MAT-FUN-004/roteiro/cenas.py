# Estudativo · MAT-FUN-004 — Domínio, contradomínio e imagem (Matemática · Funções · O que é função).
# Habilidade: dizer o domínio e a imagem de uma função dada por tabela ou diagrama, escrever t ≥ 0 como [0, +∞[ e explicar por que o número de pessoas só pode ser inteiro.
# Pré-requisitos: MAT-FUN-003 (f(x)), MAT-CON-004 (naturais e inteiros), MAT-CON-007 (intervalos). Próxima: MAT-FUN-005.
# Questão inédita, criada para esta aula. Valores do churrasco e do estacionamento inventados.
# Diagrama: f(x) = 2x, A = {1, 2, 3, 4}, B = {2, 4, 6, 8, 10} · D = A · CD = B · Im = {2, 4, 6, 8}; 10 fica de fora (2x = 10 pede x = 5 ∉ A).
# Tabela: horas 1, 2, 3, 4 → preço 5, 8, 8, 10 · D = {1, 2, 3, 4} · Im = {5, 8, 10}.
# Contexto: churrasco 20 por pessoa, 2,5 pessoas daria 50 mas não existe → D = ℕ · carro a 80 km/h, d(t) = 80t, t ≥ 0 → [0, +∞[.
# Questão: f(x) = x², A = {−1, 0, 1, 2}, B = {0, 1, 2, 3, 4} · (−1)² = 1, 0² = 0, 1² = 1, 2² = 4 · D = A · CD = B · Im = {0, 1, 4} · camisetas → ℕ.
# Visual: diagrama de flechas com ovais A e B, domínio, contradomínio e imagem realçados em cores; f: A → B; tabela de duas colunas;
#   reta numérica com o intervalo [0, +∞[ (bolinha fechada no zero); ℕ em destaque.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras: á, bê, tê.

TITULO = "Domínio, contradomínio e imagem"

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
    dict(id="s01", block="gancho", text="Um churrasco custa {a}vinte reais por pessoa. [p=0.2] Quanto pagam {b}duas pessoas e meia? [p=0.3] A conta dá cinquenta, [p=0.2] mas {c}meia pessoa não existe. [p=0.3] Saber {d}o que pode entrar numa função também é matemática, [p=0.2] e tem nome: {e}domínio."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você diz o domínio e a imagem de uma função, [p=0.2] escreve o domínio como intervalo [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}efe de xis, a saída quando entra xis; [p=0.2] {c}os conjuntos dos naturais e dos inteiros; [p=0.2] e {d}intervalo, um pedaço da reta entre colchetes. [p=0.3] Se faltar alguma, procure no canal."),
    # diagrama
    dict(id="s04", block="diagrama", text="Veja esta função em diagrama de flechas: [p=0.2] {a}efe de xis igual a dois xis. [p=0.3] {b}O conjunto á tem um, dois, três e quatro. [p=0.2] {c}O conjunto bê tem dois, quatro, seis, oito e dez. [p=0.3] {d}Cada número de á manda uma flecha para o seu dobro."),
    dict(id="s05", block="diagrama", text="As flechas {a}saem de á e chegam em bê. [p=0.2] Por isso se escreve {b}efe de á em bê, com uma flecha entre as letras. [p=0.3] E cada parte desse desenho tem um nome."),
    dict(id="s06", block="nomes", text="O conjunto de partida, á, é o {a}domínio: [p=0.2] {b}todas as entradas que a função aceita. [p=0.3] O conjunto de chegada, bê, é o {c}contradomínio: [p=0.2] {d}onde as saídas podem cair."),
    dict(id="s07", block="nomes", text="E a {a}imagem? [p=0.2] É {b}só o que sai de verdade: [p=0.2] os elementos de bê onde chega flecha. [p=0.3] Aqui, {c}dois, quatro, seis e oito. [p=0.2] {d}O dez está no contradomínio, mas não na imagem: [p=0.2] nenhum número de á tem dobro dez. [p=0.3] Por isso, {e}a imagem está contida no contradomínio."),
    # tabela
    dict(id="s08", block="tabela", text="Numa {a}tabela, é mais fácil ainda. [p=0.2] Um estacionamento cobra pelas horas. [p=0.2] {b}Uma hora custa cinco reais. [p=0.2] Duas horas custam oito. [p=0.2] Três horas, também oito. [p=0.2] E quatro horas custam dez. [p=0.3] {c}O domínio é a coluna das entradas: um, dois, três e quatro. [p=0.2] {d}A imagem é a coluna das saídas: cinco, oito e dez. [p=0.2] {e}O oito aparece duas vezes, mas no conjunto entra uma vez só."),
    # contexto
    dict(id="s09", block="contexto", text="Às vezes {a}o domínio vem da vida real. [p=0.2] No churrasco, a entrada é {b}o número de pessoas. [p=0.2] Pessoa não se divide: {c}só entram zero, um, dois, três, e assim por diante. [p=0.3] O domínio são {d}os naturais. [p=0.2] Duas pessoas e meia {e}fica de fora, mesmo que a conta funcione."),
    dict(id="s10", block="contexto", text="Outro caso: um carro a {a}oitenta quilômetros por hora. [p=0.2] A distância depende do {b}tempo de viagem, tê, em horas. [p=0.3] Tempo pode ser quebrado: {c}duas horas e meia existem. [p=0.2] Mas {d}tempo negativo não, porque a contagem começa no zero. [p=0.3] O domínio é {e}tê maior ou igual a zero."),
    dict(id="s11", block="contexto", text="Como intervalo: {a}de zero até mais infinito. [p=0.2] {b}Fechado no zero, porque ele entra. [p=0.2] {c}Aberto no infinito, como sempre."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}trocar contradomínio por imagem. [p=0.2] A pessoa olha o diagrama e diz que a imagem é {b}tudo o que está em bê, até o dez. [p=0.3] Mas o dez {c}não recebe flecha nenhuma. [p=0.2] {d}Contradomínio é onde pode chegar. [p=0.2] {e}Imagem é onde chega de fato."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}domínio é de onde sai flecha. [p=0.2] {b}Imagem é onde chega flecha. [p=0.3] Na tabela, {c}domínio é a coluna de entrada, [p=0.2] e {d}imagem é a coluna de saída, sem repetir."),
    dict(id="s14", block="atalho", text="Funciona porque cada flecha é {a}uma entrada ligada à sua saída. [p=0.3] {b}Não compensa quando a função vem de uma história, sem desenho nem tabela, [p=0.2] como no churrasco. [p=0.2] Aí, pergunte {c}o que a situação deixa entrar."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Efe de xis igual a xis ao quadrado, de á em bê. [p=0.2] {b}O conjunto á tem menos um, zero, um e dois. [p=0.2] {c}O conjunto bê tem zero, um, dois, três e quatro. [p=0.3] {d}Diga o domínio, o contradomínio e a imagem. [p=0.3] E mais: numa loja, {e}a entrada é o número de camisetas compradas. [p=0.2] {f}Que números podem entrar?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá, flecha por flecha. [p=0.2] {a}Menos um ao quadrado dá um. [p=0.2] {b}Zero ao quadrado dá zero. [p=0.2] {c}Um ao quadrado dá um. [p=0.2] {d}Dois ao quadrado dá quatro. [p=0.3] Domínio: {e}o conjunto á. [p=0.2] Contradomínio: {f}o conjunto bê."),
    dict(id="s18", block="resposta", text="Imagem: onde chega flecha. [p=0.2] {a}Zero, um e quatro. [p=0.2] O um recebe duas flechas e entra uma vez só. [p=0.2] {b}O dois e o três ficam de fora. [p=0.3] E as camisetas: [p=0.2] ninguém compra meia camiseta, nem menos uma. [p=0.2] {c}Só entram os naturais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}domínio é o que entra, [p=0.2] {b}contradomínio é onde pode chegar [p=0.2] e {c}imagem é o que sai de verdade."),
    dict(id="s20", block="fim", text="Na próxima aula, a função vem {a}só pela fórmula, sem história nenhuma. [p=0.2] Você descobre o domínio olhando {b}a divisão e a raiz quadrada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
