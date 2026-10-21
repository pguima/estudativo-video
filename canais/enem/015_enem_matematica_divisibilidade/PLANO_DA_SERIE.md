# Série Divisibilidade, Primos, MMC e MDC (Matemática ENEM): 7 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html` (texto extraído em
`_material/material_divisibilidade.txt`; ATENÇÃO: na extração os expoentes viraram números colados — "23 · 32 · 5" = 2³ · 3² · 5)
· modelo de aula: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md) · prompts por episódio enviados pelo usuário em 21/10/2026.

| Ep. | Pasta | Tema | Seções do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_multiplos_divisores` | Múltiplos, divisores e os atalhos da divisibilidade | 02, 03 + Questão 3 | 10–12 min | Primos (só formam uma fila) | ✅ renderizado (10:44) |
| 2 | `ep2_primos` | Números primos: os tijolos de todos os números | 04 + Questão 7 | 6–8 min | Fatoração do 360 | ✅ renderizado (7:45) |
| 3 | `ep3_fatoracao_divisores` | Fatoração em primos e a fórmula de quantos divisores | 05, 06 + Questão 4 | 8–10 min | MMC | ✅ renderizado (8:12) |
| 4 | `ep4_mmc` | MMC: quando as coisas voltam a coincidir | 08 + Questões 1 e 5 | 10–12 min | MDC | ✅ renderizado (11:00) · reformulado em 22/10 (varal) |
| 5 | `ep5_mdc` | MDC: o maior pedaço que cabe certinho | 07 + Questões 2 e 6 | 10–12 min | MMC ou MDC? | ✅ renderizado (11:42) · reformulado em 22/10 (varal) |
| 6 | `ep6_mmc_ou_mdc` | MMC ou MDC? A decisão em 10 segundos | 09, 10 + Questões 9 e 8 | 10–12 min | Revisão | ✅ renderizado (12:07) · reformulado em 22/10 (varal + perímetro) |
| 7 | `ep7_revisao` | Revisão geral, pegadinhas e treino (5 questões inéditas) | 01, 11, 13 | 10–12 min | Próximo assunto: Frações, decimais e dízimas | ✅ renderizado (11:04) · reformulado em 22/10 (varal + perímetro) · SÉRIE COMPLETA |

**Analogias âncora (retomadas na revisão):** divisores = retângulos de quadradinhos (36 → 1×36, 2×18, 3×12, 4×9, 6×6) ·
critério = teste rápido · primos = TIJOLOS (compostos = construções; o 1 é categoria à parte) · fatoração = RECEITA do número ·
contagem de divisores = montar um LANCHE (escolhas 0…expoente) · MMC = o REENCONTRO (tabuadas que se encontram) ·
MDC = a MAIOR RÉGUA (mede todas as tábuas sem sobrar) · decisão = REPETE (MMC, resposta grande) ou REPARTE (MDC, resposta pequena).
Ícones dos episódios (índice da revisão): retângulo de quadradinhos · tijolo · receita · ônibus · régua · placa "repete × reparte".

**Números de referência do material (usar sempre os mesmos):** 72 = 2³ · 3² · 120 = 2³ · 3 · 5 · 360 = 2³ · 3² · 5 ·
MDC(72, 120) = 24 · MMC(72, 120) = 360 · 24 · 360 = 72 · 120 = 8 640 · MMC(12, 18, 30) = 180 · D(36) tem 9 divisores · 360 tem 24 divisores.

Cores com função: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
Selo/primeira cena: "MATEMÁTICA ENEM" · CTA: "...para acompanhar toda a Matemática do ENEM do zero" · playlist "Matemática ENEM do Zero".
Voz: Gemini TTS Studio local (voz Neno), `VOZ = dict(tags=["alegre", "curiosa", "amigavel"], prompt=...)` no `cenas.py`.

Arquivos finais: `epN_<tema>/final/enem_matematica_divisibilidade_epN_<tema>.mp4`.

**Reformulação de 22/10/2026 (pedido do usuário):** o atalho principal de MMC e MDC passou a ser a **decomposição simultânea**
(fatorar todos os números juntos num varal só: MMC = todos os primos; MDC = só os primos que dividiram todos, marcados com ✓;
"um varal, dois resultados"), com a fatoração separada como o "porquê". Nos eps 6 e 7 entrou a dica rápida do perímetro
(volta inteira; retângulo = 2 × (comprimento + largura)). Versões anteriores dos roteiros em `epN/roteiro/_v1/`.
No ep4 o varal de 12, 18, 30 usa 2, 2, 3, 3, 5 (o material divide por 3 com o 6 ainda par, o que contradiz o macete).
