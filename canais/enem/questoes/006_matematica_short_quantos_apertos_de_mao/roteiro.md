# Short 006 — Quantos apertos de mão? (desafio em 3 níveis, engajamento; não é aula)
Vertical 1080x1920, 71 s, SEM áudio (o usuário grava a narração). Linha do tempo fixa em render_short.py.
Página com o roteiro: https://claude.ai/artifact/MUFvBVPYj7YtGJ9TwQVf3k
Regra: cada amigo aperta a mão de todos os outros, uma vez (um aperto = uma linha entre duas pessoas).
Respostas: nível 1 (4 amigos) C = 3 + 2 + 1 = 6 · nível 2 (5) A = 5 × 4 ÷ 2 = 10 · chefão (10) D = 10 × 9 ÷ 2 = 45.
O segredo: n × (n − 1) conta cada aperto 2 vezes (2 mãos), por isso ÷ 2.
Pegadinhas do chefão: 90 (sem dividir), 100 (10 × 10), 55 (conta a si mesmo). Conferido por força bruta: conferir_contagens.py.

| Janela | Fala | Na tela |
|---|---|---|
| 0:00–0:04 | Quatro amigos. Todo mundo aperta a mão de todo mundo, uma vez. | Roda de 4 amigos · “Quantos apertos de mão?” · selo PARECE FÁCIL |
| 0:04–0:07,5 | Quantos apertos de mão? Oito, doze, seis ou quatro? | Opções A 8 · B 12 · C 6 · D 4 |
| 0:07,5–0:09,5 | Comenta antes de ver! | “comenta antes de ver ↓” |
| 0:09,5–0:14,5 | Pausa e conta. Valendo! | PAUSE E CONTE · cronômetro 5 → 1 |
| 0:14,5–0:17 | O primeiro aperta a mão de três. | O 1º acende e puxa 3 linhas em âmbar · o 1º → 3 |
| 0:17–0:19 | O segundo, de mais dois. | O 2º puxa 2 linhas novas em ciano · o 2º → 2 |
| 0:19–0:21 | O terceiro, de mais um. | O 3º puxa 1 linha nova em verde · o 3º → 1 |
| 0:21–0:23 | E o quarto já apertou todas! | O 4º acende: “já apertou todas” · o 4º → 0 |
| 0:23–0:26 | Três mais dois mais um: seis. Letra C! | 3 + 2 + 1 = 6 · C certa |
| 0:26–0:30,5 | Quem disse doze fez quatro vezes três. Mas cada aperto tem duas mãos! | O SEGREDO: cada um acende os seus 3 (4 × 3 = 12) · o aperto 1–2 ganha “+1” dos dois lados |
| 0:30,5–0:33,5 | Contou tudo duas vezes: doze dividido por dois, seis. | 12 ÷ 2 = 6 |
| 0:33,5–0:36 | Nível dois: e com cinco amigos? | NÍVEL 2 · roda de 5 |
| 0:36–0:39,5 | Dez, vinte, quinze ou vinte e cinco? | Opções A 10 · B 20 · C 15 · D 25 |
| 0:39,5–0:42,5 | Três segundos! | Cronômetro 3 → 1 |
| 0:42,5–0:46,5 | Cada um aperta quatro: cinco vezes quatro, vinte. | Cada amigo acende os seus 4 · 5 × 4 = 20 |
| 0:46,5–0:49,5 | Dividido por dois: dez! Letra A. | Os 10 apertos se desenham (a estrela) · 20 ÷ 2 = 10 · A certa |
| 0:49,5–0:52 | Nível chefão: dez amigos! | NÍVEL CHEFÃO · roda de 10 · selo NÍVEL DIFÍCIL |
| 0:52–0:56 | Noventa, cem, cinquenta e cinco ou quarenta e cinco? | Opções A 90 · B 100 · C 55 · D 45 |
| 0:56–0:59 | Valendo! | Cronômetro 3 → 1 |
| 0:59–1:03 | Dez vezes nove, noventa. Dividido por dois... | Cada um acende os seus 9, bem rápido · 10 × 9 = 90 |
| 1:03–1:06 | Quarenta e cinco! Letra D. O noventa conta tudo duas vezes! | Os 45 apertos se desenham · 90 ÷ 2 = 45 · D certa · “90 CONTA TUDO 2 VEZES” |
| 1:06–1:11 | Quantos você acertou: zero, um, dois ou três? Comenta! No próximo: quantas diagonais? | Quantos você acertou? · 0 1 2 3 · “PRÓXIMO: QUANTAS DIAGONAIS?” |
