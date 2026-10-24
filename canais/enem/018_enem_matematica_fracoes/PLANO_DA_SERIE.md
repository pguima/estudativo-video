# Série Frações, Decimais e Dízimas (Matemática ENEM): 8 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html` (texto extraído em
`_material/material_fracoes.txt`: frações aparecem como "(3/4)", número misto como "2(3/4)" e expoentes como "^3")
· modelo de aula: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md) · prompts por episódio enviados pelo usuário em 23/10/2026
(pedido: "prepare tudo sem gerar os áudios" → roteiro, roteiro_para_gravar.txt, animações com tempos SINTÉTICOS, prévias e capas;
voz, render e publicacao.md depois).

| Ep. | Pasta | Tema | Recorte do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_o_que_e_fracao` | O que é uma fração: os 4 significados, equivalentes e simplificação | 02, 03 + questão INÉDITA | 8–10 min | Números mistos e comparação | pronto sem voz (1334 pal. ~8,9 min · voz: parte 2 da cena 20) |
| 2 | `ep2_mistos_comparar` | Números mistos e como saber qual fração é maior | 04, 05 + Questões 6 e 2 + questão extra das tintas | 10–12 min | As 4 operações | pronto sem voz (1551 pal. ~10,3 min · voz: parte 2 da cena 18) |
| 3 | `ep3_operacoes` | As quatro operações com frações (sem o "do restante"; potência só com expoente positivo) | 06 (exceto o quadro do restante) + Questão 9 | 10–12 min | "Do restante" | pronto sem voz (1547 pal. ~10,5 min · voz: parte 2 da cena 16) |
| 4 | `ep4_do_restante` | A armadilha do "do restante" | quadro do restante (06) + duas etapas (01) + Questões 7 e 1 | 6–8 min | Decimais | pronto sem voz (1043 pal. ~7 min · voz: parte 2 da cena 14) |
| 5 | `ep5_decimais` | Operações com decimais sem calculadora | 07 + Questão 5 | 8–10 min | Exato ou dízima? | pronto sem voz (1209 pal. ~8,1 min · voz: parte 2 da cena 16) |
| 6 | `ep6_dizimas_geratriz` | Decimal exato ou dízima? E a fração geratriz | 08, 09 + Questões 3 e 4 + questão extra do sensor | 10–12 min (se passar, 6a/6b) | A tabela que vale ouro | pronto sem voz (1741 pal. ~11,6 min (sem divisão) · voz: parte 2 da cena 20) |
| 7 | `ep7_tabela_ouro` | A tabela que vale ouro: fração, decimal e porcentagem (só conversão) | 10 + Questão 8 | 6–8 min | Revisão | pronto sem voz (1214 pal. ~8,1 min · voz: parte 2 da cena 16) |
| 8 | `ep8_revisao` | Revisão geral, pegadinhas (V/F dos 9 erros) e 5 questões INÉDITAS | 01, 11, 13 (sem as Questões 1–9) | 10–12 min | Próximo assunto: Potenciação e radiciação | pronto sem voz (1509 pal. ~10,5 min · voz: parte 2 da cena 20) |

**Analogias âncora (a revisão retoma todas, com os mesmos ícones):**
ep1 fração = PIZZA (denominador = em quantas fatias; numerador = quantas você pegou) · equivalentes = a mesma pizza cortada de
jeitos diferentes · "DE" = um "vezes" disfarçado · ep2 misto = pizzas inteiras e mais um pedaço · mesmo numerador: pizza para
menos gente dá fatia maior · a metade como régua de referência · ep3 soma = recortar tudo no MESMO tamanho de fatia (MMC) ·
multiplicar = tirar uma fração DE outra (barra de chocolate) · dividir = quantas vezes uma cabe na outra · ep4 "do restante" =
a PIZZA QUE ENCOLHE · ep5 decimal = DINHEIRO (a vírgula separa reais de centavos; moedas de 12 centavos em R$ 4,80) ·
ep6 o 10 só aceita 2 e 5 (10 = 2 × 5) · geratriz = a "mãe" da dízima · as duas FITAS com a mesma cauda infinita ·
ep7 fração, decimal e porcentagem = três IDIOMAS do mesmo número.
Ícones da revisão: pizza · pizzas inteiras + pedaço · sinais + − × ÷ · pizza que encolhe · moedas · fita infinita · três cartas.
Séries anteriores citadas: MMC = "o reencontro" e MDC = "a maior régua que mede tudo certinho" (série 015); racional = vira fração (010).

**Números de referência do material (usar sempre os mesmos):** 3/4 de 200 = 150 · 2/5 de 300 = 120 · 1/2 = 2/4 = 3/6 = 50/100 = 0,5 ·
6/9 e 10/15 (6·15 = 90 = 9·10) · 84/120 → MDC 12 → 7/10 · 2 3/4 = 11/4 · 11 ÷ 4 = 2 resto 3 · 3/5 vs 5/8 → 24 vs 25 · 7/16 < 1/2 < 9/16 ·
1/6 + 1/4 + 1/3 = 9/12 = 3/4 · 4/9 · 3/8 = 1/6 · 3/4 ÷ 2/5 = 15/8 · (2/3)³ = 8/27 · salário R$ 1 200 → 400 → 800 → 200 ·
0,3 · 0,04 = 0,012 · 4,8 ÷ 0,12 = 40 · 3,47 · 100 = 347 · 0,777… = 7/9 · 0,8333… = 5/6 · 1,2454545… = 1233/990 = 137/110 · 0,999… = 1 ·
37,5% = 3/8 · 0,24 = 6/25.

**Peças comuns:** `comum.py` (nesta pasta) — pizza, barra de chocolate, reta 0–1, frações empilhadas e expressões (`expr("1/2 + 1/3")`),
cronômetro de pausa, cartões de erro e lista de alternativas. Cada `visual.py` importa como `K` e chama `K.usar_tempos(...)`.
Regra (pedido de 22/10): em exatas, sempre uma cena de ATALHO/macete (verde) por procedimento, e toda fórmula de outro assunto
ganha uma frase de explicação na hora.

Cores com função: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
Selo/primeira cena: "MATEMÁTICA ENEM" · CTA: "...inscreva-se no Estudativo ... para acompanhar toda a Matemática do ENEM do zero" ·
playlist "Matemática ENEM do Zero".
Voz: Gemini TTS Studio local (voz Neno), `VOZ = dict(tags=["alegre", "curiosa", "amigavel"], prompt=...)` no `cenas.py`.

Arquivos finais: `epN_<tema>/final/enem_matematica_fracoes_epN_<tema>.mp4`.

**Status 23/10/2026:** os 8 episódios têm roteiro, roteiro_para_gravar.txt, visual com tempos SINTÉTICOS, prévias e 3 capas (A recomendada).
Faltam: voz (Neno), transcrição, render e publicacao.md. Erro do material: na Questão 9, a alternativa E (1/13) NÃO é a de "quem somou termo a termo"
(isso dá 3/13 arrecadado); o vídeo do ep3 diz só que o 13 vem de 6 + 4 + 3. Gabaritos das 5 questões inéditas do ep8: B, C, E, D, D.
