# Estudativo · MAT-ARE-010 — Razão entre áreas de figuras semelhantes (Matemática · Áreas e Perímetros).
# Habilidade: usar que a razão das áreas de figuras semelhantes é k² e descobrir que aumentar o lado em 20% aumenta a área em 44%.
# Pré-requisitos: MAT-ANG-012 (razão de semelhança), MAT-ARE-003 (área do triângulo). Usa MAT-RAZ-010 (dobra o lado, quadruplica a área),
#   MAT-POR-004 (fator 1,2) e MAT-POR-010 (atalho dos aumentos seguidos: a + b + a · b / 100). Próxima: MAT-ARE-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Raiz quadrada (MAT-POT-007) fora da cadeia: a aula não faz o caminho de volta (da área para o lado).
# Letra k narrada "cá".
# Contas: triângulo base 4, altura 3 → 6; ×3 → 12 e 9 → 54 = 9 · 6. Lado 10 → 100; 12 → 144; 1,2² = 1,44. Faixas 10 × 2 + 10 × 2 + 2 × 2 = 44 (erro 40).
#   Perímetro 40 → 48 (+20%). Redução −20%: −40 + 4 = −36 (0,8² = 0,64). Questão: 1,3² = 1,69; 200 · 1,69 = 338 mL; 30 + 30 + 9 = 69%.
# Visual:
#   s04-s06: E.triangulo base 4, altura 3 (tracejada) ao lado do ampliado 12 e 9; nove cópias do pequeno cobrindo o grande.
#   s07: fórmula A₂/A₁ = k² com legendas.
#   s08-s11: E.quadrado de lado 10 crescendo para 12: duas faixas 10 × 2 (verde) e o cantinho 2 × 2 (cor da matéria); no erro, o cantinho piscando.
#   s09: 1,2 × 1,2 = 1,44.
#   s14-s17: logotipo triangular e a ampliação com cada medida × 1,3; lata de 200 mL → 338 mL.

TITULO = "Razão entre áreas de figuras semelhantes"

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
    dict(id="s01", block="gancho", text="Um terreno quadrado teve {a}cada lado aumentado em vinte por cento. [p=0.3] A área aumentou quanto? [p=0.2] Vinte por cento? [p=0.2] Quarenta? [p=0.3] {b}Quarenta e quatro por cento."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você compara a área de figuras ampliadas ou reduzidas sem medir tudo de novo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}em figuras semelhantes, todos os lados são multiplicados pelo mesmo número, a razão de semelhança; [p=0.2] {c}aumentar vinte por cento é multiplicar por um vírgula dois; [p=0.2] e {d}dobrar o lado de um quadrado quadruplica a área. [p=0.3] Se faltar alguma, procure no canal."),
    # triângulo
    dict(id="s04", block="triangulo", text="O que vale para o quadrado vale para {a}qualquer figura semelhante. [p=0.2] Veja um triângulo com {b}base quatro e altura três. [p=0.2] Área: {c}quatro vezes três, dividido por dois, dá seis."),
    dict(id="s05", block="triangulo", text="Amplie esse triângulo com {a}razão de semelhança três. [p=0.2] Todos os comprimentos ficam três vezes maiores, {b}inclusive a altura. [p=0.2] Base {c}doze, altura {d}nove. [p=0.3] {e}Doze vezes nove, dividido por dois, dá cinquenta e quatro."),
    dict(id="s06", block="triangulo", text="{a}Cinquenta e quatro é nove vezes seis. [p=0.2] A razão dos lados é três, [p=0.2] e {b}a razão das áreas é três ao quadrado, que dá nove. [p=0.3] Por quê? [p=0.2] A área multiplica {c}duas medidas, base e altura, [p=0.2] e {d}cada uma ganhou o fator três."),
    # regra
    dict(id="s07", block="regra", text="Na fórmula: se a razão de semelhança é {a}cá, [p=0.2] {b}a razão entre as áreas é cá ao quadrado. [p=0.2] {c}Cá é o número que multiplica cada lado. [p=0.3] Vale para triângulo, retângulo, círculo, mapa ou foto, [p=0.2] {d}desde que a figura inteira mude na mesma proporção."),
    # porcentagem
    dict(id="s08", block="porcento", text="Voltando ao terreno do começo. [p=0.2] Imagine {a}lado dez e área cem. [p=0.2] Com vinte por cento a mais, {b}o lado vai para doze. [p=0.2] {c}Doze vezes doze dá cento e quarenta e quatro. [p=0.3] {d}Cento e quarenta e quatro menos cem dá quarenta e quatro a mais em cada cem: [p=0.2] quarenta e quatro por cento."),
    dict(id="s09", block="porcento", text="Com fatores, nem precisa do lado. [p=0.2] O lado foi multiplicado por {a}um vírgula dois. [p=0.2] A área, por {b}um vírgula dois ao quadrado. [p=0.2] {c}Um vírgula dois vezes um vírgula dois dá um vírgula quarenta e quatro. [p=0.3] {d}O zero vírgula quarenta e quatro é o aumento: quarenta e quatro por cento."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}somar vinte com vinte e dizer quarenta por cento. [p=0.3] Olhe o desenho. [p=0.2] O quadrado de lado dez ganhou {b}uma faixa de dez por dois na direita [p=0.2] e {c}outra de dez por dois em cima. [p=0.2] Vinte mais vinte dá quarenta. [p=0.3] Mas falta {d}o cantinho de dois por dois, que dá mais quatro. [p=0.2] {e}Quarenta mais quatro dá quarenta e quatro."),
    dict(id="s11", block="erro", text="Quem cresce na mesma porcentagem do lado é {a}o perímetro: [p=0.2] quarenta vezes um vírgula dois dá quarenta e oito, [p=0.2] os mesmos vinte por cento. [p=0.3] {b}Contorno acompanha o lado. [p=0.2] {c}Área acompanha o lado ao quadrado."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, que você já usou nos aumentos seguidos. [p=0.2] Aumentar o lado é {a}aumentar a largura e depois a altura. [p=0.3] {b}Some as porcentagens: vinte mais vinte dá quarenta. [p=0.2] {c}Some também vinte vezes vinte, dividido por cem, que dá quatro. [p=0.2] {d}Quarenta mais quatro dá quarenta e quatro por cento."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a área ganha o mesmo aumento duas vezes, um em cada medida. [p=0.3] Na redução, {b}a porcentagem entra com sinal de menos. [p=0.2] Lados vinte por cento menores: [p=0.2] {c}menos vinte menos vinte dá menos quarenta, [p=0.2] e {d}menos vinte vezes menos vinte, dividido por cem, dá mais quatro. [p=0.2] {e}A área cai trinta e seis por cento. [p=0.3] {f}Não compensa quando só um lado muda: [p=0.2] a figura deixa de ser semelhante, e a área muda na porcentagem desse lado."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um logotipo pintado numa parede gastou {a}duzentos mililitros de tinta. [p=0.3] Vão pintar uma versão ampliada, com {b}cada medida trinta por cento maior. [p=0.2] A tinta gasta {c}acompanha a área. [p=0.3] {d}Quantos mililitros a versão nova vai gastar?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Fator do lado: {a}um vírgula três. [p=0.2] Fator da área: {b}um vírgula três ao quadrado. [p=0.2] Sem as vírgulas, {c}treze vezes treze dá cento e sessenta e nove. [p=0.2] Com duas casas, {d}um vírgula sessenta e nove."),
    dict(id="s17", block="resposta", text="{a}Duzentos vezes um vírgula sessenta e nove dá trezentos e trinta e oito mililitros. [p=0.3] Pelo atalho: {b}trinta mais trinta dá sessenta, [p=0.2] e {c}trinta vezes trinta, dividido por cem, dá nove. [p=0.2] {d}Sessenta e nove por cento a mais. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}lados vezes cá, [p=0.2] {b}área vezes cá ao quadrado. [p=0.2] E {c}a porcentagem do lado não passa igual para a área."),
    dict(id="s19", block="fim", text="Na próxima aula, os triângulos não são semelhantes, [p=0.2] mas têm {a}a mesma altura. [p=0.2] Aí, {b}a razão das áreas é a razão das bases, [p=0.2] e você vai ver por que {c}a mediana corta a área ao meio. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
