# Visual de uma aula

O `visual.py` do piloto é o modelo. Cada bloco do roteiro vira uma função `b_<bloco>(c, t, C, b)`, e `C["s01.a"]` é o instante do cue.

## Início do arquivo

```python
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, passo, corrida, palco
import motor as M
import skia

E.usar("<Matéria>", "<Trilha>")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_<id>_<slug>.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("<blocos que abrem com cortina>"))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)
```

`CAPTION` vazio é o que tira a legenda. `COR = E.COR_TEXTO` é o que mantém o texto legível nas matérias de cor clara. Em matemática, ele é igual a `E.COR`. Formas usam a cor da matéria sozinhas.

Texto sobre esfera ou faixa da matéria usa `E.SOBRE`, nunca branco fixo: Redação, Inglês e Espanhol pedem texto preto.

## Peças

| Peça | Uso |
|---|---|
| `E.frase(c, t, t0, [(texto, estilo, tamanho[, cor]), ...], x, y, align)` | Linha palavra a palavra. Estilos: `g` pesada, `b` bold, `m` média, `i` itálica, `s` serifada |
| `E.foco(c, t, t0, d, fn)` | Entrada desfocada de qualquer desenho; `fn(a)` desenha |
| `E.saida(c, t, t1, fn)` | Desenha até `t1` e some desfocando |
| `E.escreve(c, s, x, y, size, estilo, cor, a)` | Texto parado, y é a linha de base |
| `fr`, `sinal`, `E.resultado` | Fração, sinal e fração na esfera |
| `E.fracao`, `E.barra_fatias` | Fração sem animação, barra dividida |
| `corrida` | Conta a/b ∓ c/d até o resultado, numa linha |
| `passo` | Linha de método com número |
| `E.centro(c, s, cx, y, size, estilo, cor, a)` | Texto centrado em `cx`, sem animação; y é a linha de base |
| `E.linha(c, t, [(texto, estilo, tamanho, cor, t0), ...], x, y, align)` | Como `E.frase`, com um instante para cada parte; devolve o x de cada uma |
| `E.chocolate(c, x, y, w, h, n, pedacos, a, cortes, escuro)` | Barra de pedaços que se contam, somam e saem. `pedacos = [(i, cor, p[, dy])]`, `escuro=True` no palco |
| `E.tablete(c, x, y, w, h, cor, a, k)` | Um pedaço de chocolate solto, fora da barra |
| `E.barra(c, x, y, w, h, pintado, cortes, a, cor, enche, largura)` | Barra de área contínua: a parte pintada fica fixa e os cortes `[(posição, p)]` descem e voltam. Boa para frações equivalentes |
| `E.chave(c, x0, x1, y, cor, p, h, largura, abre)` | Colchete que marca um trecho de barra; `h < 0` fica acima; `abre=False` só surge, sem abrir do meio |
| `E.ponte(c, t, t0, x0, x1, y, rotulo, cor, size)` | Seta com a operação numa pílula |
| `E.pontes(c, t, x0, x1, cy, s, rot, tc, tb, cor, size)` | A mesma operação no de cima e no de baixo de uma fração de tamanho `s` |
| `E.frac_q(c, t, t0, n, d, tn, td, cx, cy, s, cor)` | Fração que chega com `?` e ganha os números na fala |
| `E.montar(nums, primos)` | Faz a fatoração de verdade e devolve os dados da tabela (`assert` se os primos não fecharem em 1) |
| `E.tabela(c, t, T, tn, tp, tb, g, cor_fim, cor_primo)` | Tabela de fatoração simultânea; `g` = `E.TAB_GRANDE` ou `E.TAB_PEQUENA` |
| `E.seta_primo(c, t, ini, fim, i, g)` | Caixa pontilhada na casa do primo da vez |
| `E.passos(c, t, T, ti, tp, tn, tf)` | Painel à direita com a conta de cada número |
| `E.produto(c, t, T, ts, x0, y, g, s, passo_x)` | Os primos voam da coluna até formar a multiplicação |
| `E.bola`, `E.simbolo`, `E.arco` | Formas |
| `E.caixa_pontilhada`, `E.cursor`, `E.pilula`, `E.risco` | Destaques |
| `E.relogio(c, t, t0, cx, cy, r, escuro)` | Relógio de pausa com "pause o vídeo", na cena da questão |
| `E.selo(c, cx, cy, r, ok, a)` | Certo ou errado numa esfera |
| `E.corta(c, t, t0, cx, cy, size, novo, tn=...)` | Risca um número e escreve o novo em cima: corte em cruz, empréstimo |
| `E.grade(c, x, y, w, h, cols, lins, pc, pl, a, ec, el)` | Multiplicar frações por área: colunas pintadas, linhas por cima, cruzamento forte |
| `E.numero(c, s, xv, y, size, estilo, cor, a, cores)` | Decimal alinhado pela vírgula: `xv` é a posição dela. `cores = {índice: cor}` acende uma casa |
| `E.anda(c, t, dig, pos, saltos, x, y, size, tv=..., some=...)` | A vírgula salta e os algarismos ficam parados; os zeros entram sozinhos. `"37", 1, [(t0, 2), (t1, 3)]` é 3,7 → 37 → 370 |
| `E.armada(c, t, nums, op, res, tn, tr, xv, y0, size, tz=..., marcas=...)` | Conta armada com vírgula sobre vírgula. Refaz a conta e para com `assert` se o resultado não bater. `tr` vai da direita para a esquerda; `tz` é o instante dos zeros que completam; `marcas = [(linha, índice, novo, t0)]` faz o empréstimo |
| `E.conta_mult(c, t, a, b, tn, tl, xv, y0, size, tz=..., tr=..., tsoma=..., vai=...)` | Conta armada de multiplicar, refeita pela peça. `tl` = uma lista por linha, da direita para a esquerda; `tz` = o zero de cada linha depois da primeira; `vai = [(coluna da direita, texto, t0[, t_some])]`. `E.armada` aceita o mesmo `vai` |
| `E.expressao(c, t, estados, tp, cx, y, size, empilha=..., t0=...)` | Expressão que se resolve no lugar: `estados = [(texto, trecho da vez), ...]`, com `assert` de que todos valem o mesmo. `empilha=dy` deixa cada etapa numa linha |
| `E.divida(c, cx, cy, w, h, valor, a, cancela)` | Cartão de dívida; `cancela` 0..1 risca |
| `E.formula(c, s, x, y, size, estilo, cor, a, align)` | Fórmula com expoente, raiz e fração: `2^5 · 2^4`, `10^{−3}`, `r{72}`, `6r{2}`, `r3{27}`, `(f{2}{3})^3`, `9^{1/2}`, `r{f{9}{16}}`. `E.formula_em(c, t, t0, ...)` entra com foco |
| `E.cientifica(c, t, t0, n, e, x, y, size, te=..., cor_e=...)` | Notação científica; `te` faz o expoente entrar depois. Para em `assert` se 1 ≤ n < 10 não valer: a forma errada se mostra com `E.formula` |
| `E.balanca(c, cx, cy, esq, dir_, inclina, a, size)` | Balança de dois pratos: cada prato recebe uma fórmula (`"2x + 3"`) ou uma função que desenha. `inclina` baixa um lado; 0 é a equação |
| `E.intervalo(c, t, t0, vx, y, ini, fim, fecha_ini, fecha_fim)` | Solução de inequação sobre `E.reta`: bolinha cheia entra, aberta não; `None` segue até a ponta com seta |
| `E.sistema(c, t, t0, linhas, x, y, size, tl=...)` | Chave do sistema com uma fórmula por linha |
| `E.dividir(dividendo, divisor, casas_max)` | Faz a divisão de verdade e devolve os passos, para `E.conta_div` (`"7,5"` ou `"7"`; divisor inteiro). Com resto de verdade, use `casas_max=0`: `E.dividir("17", 5, 0)` |
| `E.conta_div(c, t, D, tq, tr, t0, x, y, size, tv=..., ts=...)` | Conta de dividir na chave: `tq` = cada algarismo do quociente, `tr` = cada linha de baixo com o resto e o algarismo que desceu, mais a última com o resto final. `ts` mostra o resto sozinho antes de o algarismo descer |
| `E.quadro_casas(c, t, nomes, tc, linhas, x, y, w_col, size, grossa=1)` | Quadro inteiro, décimo, centésimo, milésimo; com `grossa=None`, centena, dezena, unidade. Célula `(algarismo, t0[, cor])` |
| `E.reta(c, t, t0, x0, x1, y, vmin, vmax, marcas, fmt, tm=...)` | Reta numérica; devolve a função valor → x. `tm` = instante de cada marca |
| `E.salto(c, t, t0, x0, x1, y, alto, rotulo=...)` | Arco com seta sobre a reta: dívida e pagamento |
| `E.moeda(c, cx, cy, r, s, a)` | Moeda na cor da matéria (`"25¢"`) |
| `P = E.plano(c, t, t0, x, y, w, h, xmin, xmax, ymin, ymax, passo=1, grade=True, marcas_x=..., marcas_y=...)` | Plano cartesiano na caixa (x, y, w, h), eixos com seta, marcas e grade. Devolve `P`: `P.x(v)`, `P.y(v)`, `P(x, y)` levam valor a pixel |
| `E.ponto(c, t, t0, P, x, y, rotulo, guias=False, valores=False, lado=(1, -1))` | Ponto no plano, que entra com um salto. `guias` traça o tracejado até os eixos, `valores` escreve x e y na ponta delas. `lado` = de que lado fica o rótulo |
| `E.curva(c, t, t0, P, f, a, b, d=1.2, rotulo=..., em=(x, y), tracejada=False)` | Gráfico de `f` desenhado da esquerda para a direita. Corta sozinho em assíntota e furo (`1/x`, `math.tan`, `math.log`) |
| `E.reta_pontos(c, t, t0, P, A, B, rotulos=("A", "B"), rotulo=...)` | Reta por dois pontos, de borda a borda do plano, com os pontos marcados |
| `E.area(c, t, t0, P, f, a, b, g=None, alfa=0.24)` | Região entre `f` e `g` (ou o eixo x) de a até b, pintada da esquerda para a direita |
| `E.colunas(c, t, t0, dados, x, y, w, h, destaque=(), deitado=False, eixo_y=False, fmt=...)` | Colunas, ou barras com `deitado=True`. `dados = [(rótulo, valor[, cor])]`. Com `destaque`, só esses índices ficam na cor da matéria e os outros em cinza |
| `E.serie(c, t, t0, dados, x, y, w, h, vmin=0, vmax=..., marcas=..., eixos=True)` | Gráfico de linha. A linha cresce e cada ponto acende quando ela chega. Para uma segunda série, chame de novo com `eixos=False` |
| `E.pizza(c, t, t0, dados, cx, cy, r, rosca=0, destaque=(), casas=0)` | Setores girando a partir do alto, com rótulo e porcentagem por fora. `rosca` abre o miolo. Os índices de `destaque` saem um pouco do centro |
| `E.histograma(c, t, t0, limites, freqs, x, y, w, h, poligono=False)` | Classes coladas com rótulo nos limites (`limites` tem um item a mais que `freqs`). `poligono` traça o polígono de frequências |
| `E.segmento(c, t, t0, A, B, medida, rotulos=("A", "B"), lado=1, cota=False, tracejado=False)` | Segmento que cresce, com a medida ao lado. `cota` faz a linha de cota afastada, como no desenho técnico |
| `E.angulo(c, t, t0, V, A, B, rotulo, r=64, reto=None, dentro=False)` | Ângulo AVB com arco e rótulo na bissetriz. O ângulo de 90° vira quadradinho sozinho |
| `E.poligono(c, t, t0, pts, vertices, lados=..., angulos=..., iguais=..., retos=(), tv/tl/ta=...)` | Polígono que se desenha em volta, com nomes, medidas dos lados (`lados[i]` vai de `pts[i]` a `pts[i+1]`), ângulos, tracinhos de lados iguais e ângulos retos. É a base das peças abaixo |
| `E.triangulo(c, t, t0, A, B, C, vertices=("A", "B", "C"), lados=(AB, BC, CA), angulos=..., iguais=..., retos=...)` | Triângulo por três pontos, com os mesmos parâmetros de `E.poligono` |
| `E.marcas_iguais(c, A, B, n, cor, a)` | n tracinhos no meio de um lado: lados com o mesmo número de tracinhos são iguais |
| `E.regular(c, t, t0, n, cx, cy, r, vertices, lado=..., raio=..., apotema=...)` | Polígono regular de n lados com um lado deitado embaixo. `raio` e `apotema` traçam esses segmentos a partir do centro |
| `E.retangulo(c, t, t0, x, y, w, h, base, altura)` e `E.quadrado(c, t, t0, x, y, l, lado)` | Retângulo com a base embaixo e a altura à esquerda. O quadrado já vem com os tracinhos de lados iguais e o ângulo reto |
| `E.paralelogramo(c, t, t0, x, y, w, h, desloca, base, altura, lado)` e `E.trapezio(c, t, t0, x, y, B, b, h, desloca=None, base_maior=..., base_menor=..., altura=...)` | A altura entra tracejada, com o quadradinho no pé. O trapézio sem `desloca` é isósceles |
| `E.circulo(c, t, t0, cx, cy, r, o="O", raio=(ang, rót), diametro=(ang, rót), corda=(a1, a2, rót), setor=(a1, a2, rót), arco=(a1, a2, rót), te={...})` | Circunferência que se fecha, com centro, raio, diâmetro, corda, setor pintado e arco em destaque. Ângulos em graus, no sentido anti-horário a partir da direita |
| `E.paralelas(c, t, t0, cx, cy, w, gap, inclina=60, angulos={k: rót}, cores={k: cor}, ta={k: t})` | Retas paralelas r e s cortadas pela transversal t. Os ângulos vão de 1 a 4 no cruzamento de cima e de 5 a 8 no de baixo, na ordem acima à direita, acima à esquerda, abaixo à esquerda, abaixo à direita |
| `E.cubo(c, t, t0, x, y, a, medida, todas=False)` e `E.paralelepipedo(c, t, t0, x, y, a, b, h, (larg, prof, alt), vertices=...)` | Perspectiva cavaleira. (x, y) é o canto de baixo à esquerda da frente. As arestas escondidas saem tracejadas |
| `E.prisma(c, t, t0, cx, cy, n, r, h, altura, aresta)` e `E.piramide(c, t, t0, cx, cy, n, r, h, altura, aresta)` | Base regular de n lados vista de cima e de lado. (cx, cy) é o centro da base. A pirâmide traça a altura tracejada até o centro |
| `E.cilindro(c, t, t0, cx, cy, r, h, raio, altura)`, `E.cone(c, t, t0, cx, cy, r, h, raio, altura, geratriz)` e `E.esfera(c, t, t0, cx, cy, r, raio)` | Corpos redondos com volume suave. A parte de trás da base (e do equador) sai tracejada. (cx, cy) é o centro da base, ou da esfera |
| `E.venn(c, t, t0, cx, cy, r, nomes, numeros={reg: n}, pinta=[reg ou (reg, t)], tn={reg: t})` | Venn de 2 ou 3 conjuntos no retângulo do universo. As regiões são nomeadas pela posição do conjunto: `"A"`, `"AB"`, `"ABC"`, `"BC"`…; `""` = fora de todos. O número fica no ponto mais folgado da região |
| `E.arvore(c, t, t0, niveis, x, y, w, h, ramos=..., folha=fn, tn=[...], destaque=(caminho,))` | Árvore de possibilidades da esquerda para a direita. `niveis[i]` é uma lista igual para todos os nós ou uma função caminho → rótulos (sem reposição). `ramos` faz o mesmo para o texto do ramo (`"f{1}{2}"`). Os caminhos em `destaque` ficam na cor da matéria |
| `E.trigono(c, t, t0, cx, cy, r, ang, rotulo="θ", seno=True, cosseno=True, tangente=False, notaveis=(30, 45, 60), ts={...})` | Círculo trigonométrico com o ângulo, o ponto P, o cosseno projetado no eixo x e o seno no eixo y. `ang` pode variar com `t` para girar |
| `palco(c, t)` | Fundo escuro: chame no início do bloco |
| `E.cortina` | Transição, já chamada no `OVERLAY` |

## Como compor

- Uma ideia por tela, com muito espaço vazio.
- Tipografia grande: mínimo de 40 no texto de apoio, 60 ou mais no principal, porque muita gente assiste no celular.
- Misture itálico fino com uma palavra pesada na cor da matéria. É a assinatura do canal.
- O que está sendo dito aparece na hora. Use um cue por elemento.
- Reserve o palco escuro para atalho e macete.
- Cortina nos blocos grandes, não em todos: uso demais cansa.
- Animação serve para ensinar. Se ela ajuda a entender, faça sob medida, como a barra de chocolate (`E.chocolate`).
- Para parar de mostrar algo no meio do bloco, use `E.saida`, não apague de repente.

## Peça que falta

Matérias de texto ainda não têm trecho marcado nem mapa. Se a aula precisar, crie a peça em `editorial.py`, para servir às próximas, e não no `visual.py`. Faça o mesmo com a forma-símbolo da matéria: na primeira aula dela, desenhe a forma em `simbolo()` e `capa_modelo()`. Peça que mude uma cena já aprovada precisa continuar igual no piloto: confira um quadro antes e depois.
