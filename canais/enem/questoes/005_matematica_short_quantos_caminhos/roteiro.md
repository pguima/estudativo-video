# Short 005 — Quantos caminhos? (desafio em 3 níveis, engajamento; não é aula)
Vertical 1080x1920, 71,5 s, SEM áudio (o usuário grava a narração). Linha do tempo fixa em render_short.py.
Página com o roteiro: https://claude.ai/artifact/JxsMRoH2aV3HKYqmLxEzX3
Regra: de A até B pelas ruas, só para a direita ou para baixo (os caminhos mais curtos).
Respostas: nível 1 (grade 2 × 2) B = 6, desenhados um por um · nível 2 (3 × 2) D = 10 · chefão (3 × 3) C = 20.
O segredo: cada esquina = a de cima + a da esquerda (borda = 1). A diagonal 1 3 3 1 do chefão é uma linha do triângulo de Pascal.
Pegadinhas do chefão: 9 = as casas da grade, 12, 27. Contagens conferidas por força bruta: conferir_contagens.py.

| Janela | Fala | Na tela |
|---|---|---|
| 0:00–0:03 | Quantos caminhos vão de A até B? | Grade 2 × 2 de ruas · A e B · “Quantos caminhos de A até B?” · selo PARECE FÁCIL |
| 0:03–0:06 | Só vale andar pra direita ou pra baixo. | Setinhas saindo do A (→ e ↓) · “só vale → ou ↓” |
| 0:06–0:09,5 | Quatro, seis, oito ou doze? Comenta antes de ver! | Opções A 4 · B 6 · C 8 · D 12 |
| 0:09,5–0:14,5 | Pausa e conta. Valendo! | PAUSE E CONTE · cronômetro 5 → 1 |
| 0:14,5–0:21,5 | Um por um: um, dois, três, quatro, cinco, seis! | UM POR UM: os 6 caminhos desenhados em âmbar, um a cada 0,9 s; os já contados ficam em verde · contador 1 → 6 |
| 0:21,5–0:24 | Seis caminhos. Letra B! | 6 caminhos · B certa |
| 0:24–0:28,5 | O segredo: cada esquina soma a de cima com a da esquerda. | O SEGREDO: “cada esquina = de cima + da esquerda” |
| 0:28,5–0:33 | Na borda, um. Depois dois, três, três... e três mais três: seis! | A borda ganha 1; as esquinas de dentro somam uma a uma, com a rua de cima (ciano) e a da esquerda (âmbar) piscando · 1 + 1 = 2 … 3 + 3 = 6 no B |
| 0:33–0:36 | Nível dois: e com três de largura? | NÍVEL 2 · grade 3 × 2 |
| 0:36–0:39,5 | Oito, doze, seis ou dez? | Opções A 8 · B 12 · C 6 · D 10 |
| 0:39,5–0:42,5 | Três segundos! | Cronômetro 3 → 1 |
| 0:42,5–0:47,5 | Soma esquina por esquina: dois, três, quatro... três, seis, dez! | Borda = 1 · esquinas 2, 3, 4 / 3, 6, 10 · conta de cada esquina no quadro |
| 0:47,5–0:50 | Dá dez! Letra D. | 4 + 6 = 10 · D certa |
| 0:50–0:52,5 | Nível chefão: grade três por três! | NÍVEL CHEFÃO · grade 3 × 3 · selo NÍVEL DIFÍCIL |
| 0:52,5–0:56 | Nove, doze, vinte ou vinte e sete? | Opções A 9 · B 12 · C 20 · D 27 |
| 0:56–0:59 | Valendo! | Cronômetro 3 → 1 |
| 0:59–1:04 | Mesma soma, esquina por esquina... e dez mais dez: vinte! | As 9 esquinas de dentro somam em sequência · 10 + 10 = 20 no B |
| 1:04–1:06,5 | Letra C! E olha: é o triângulo de Pascal! | C certa · a diagonal 1 3 3 1 acende em verde · “É O TRIÂNGULO DE PASCAL” |
| 1:06,5–1:11,5 | Quantos você acertou: zero, um, dois ou três? Comenta! No próximo: quantos apertos de mão? | Quantos você acertou? · 0 1 2 3 · “PRÓXIMO: QUANTOS APERTOS DE MÃO?” |
