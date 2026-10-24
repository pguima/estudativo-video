# Descontos, Acréscimos, Lucro e Prejuízo — série de videoaulas

Material de apoio (cópia em `_material/15-descontos-acrescimos-lucro-prejuizo.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/15-descontos-acrescimos-lucro-prejuizo.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator (1 + i), descontos sucessivos, voltar ao valor original, +20% e −20% não se anulam (seção 02 e parte da 06) | **Porcentagem** (série 09) | Revisão relâmpago de 30 s no início do vídeo 2. O foco é o novo: **base custo × base venda**, margem e markup, formação de preço, imposto sobre a venda, promoções, faixas e remarcações. |
| **Questão 3 do material** (30% de liquidação + 10% no Pix → 37%) | Igual à **Questão 6 de Porcentagem** (30% + 10% no caixa → 37%) | **Não uso.** No lugar dela entra uma questão nova (etiqueta de R$ 300,00, −20%, −5% no Pix, +10% de frete), com o texto completo no prompt do vídeo 2. |
| Questão 6 (R$ 102,00 depois de 15% de desconto) | Mesma ideia do exemplo "R$ 150,00 com 20% de desconto" de Porcentagem (seção 07), que lá não era questão | Mantida como "nós fazemos", apresentada como revisão aplicada. |
| Desconto por faixa | **Função modular e funções definidas por partes** (29) | Só citada ("isso tem série própria"). |
| Desconto à vista, "parcelado sem juros" | **Empréstimos** (17) e **Comparação de propostas** (18) | Só citado e prometido. |

## Plano: 4 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Lucro e prejuízo: porcentagem de quê? Margem e formação do preço** | 03, 04, 05 | Q1, Q2, Q7 | 10–12 min |
| **2. Descontos encadeados, preço original, promoções e faixas** | 02, 06, 07 | Nova (no lugar da Q3), Q6, Q5, Q8 | 10–12 min |
| **3. Remarcações, liquidações e o lucro que sobra** | 08 | Q9, Q4 | 6–8 min |
| **4. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Margem sobre a venda (vídeo 1):** a IA tende a multiplicar. Custo R$ 72,00 com 20% sobre a venda dá **72 ÷ 0,80 = R$ 90,00**, não 72 · 1,20 = 86,40; na Q2, **60 ÷ 0,75 = R$ 80,00**, não 75. Confira sempre o lucro em reais dividido pelo preço de venda.
- **Questão 7 (vídeo 1):** imposto e comissão são **15% dos R$ 600,00 = R$ 90,00**; o lucro líquido é 510 − 400 = R$ 110,00 = **27,5% do custo**. A IA costuma fazer 50% − 15% = 35% (é o distrator C).
- **Questão 5 (vídeo 2):** "segunda unidade com 50%" é **25%** de desconto efetivo. Ordem certa: **I (R$ 48,00), III (R$ 50,40), II (R$ 54,00)**. Se a IA tratar a loja II como 50%, a ordem sai invertida.
- **Questão 4 (vídeo 3):** prejuízo de **R$ 50,00** (custos 500 + 750 = 1.250 contra 1.200 de venda). R$ 48,00 é o distrator de quem faz 1.200 · 0,96.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_lucro_base` · 1762 pal. ~11,7 min · voz: parte 2 da cena 20 · capa A · Q1 B, Q2 C, Q7 B · bloco do imposto trocado (340 ÷ 0,85) para não entregar a Q7
- **Vídeo 3:** pronto sem voz · `ep3_remarcacoes` · 1148 pal. ~7,7 min · voz: parte 2 da cena 14 · capa B · Q9 A, Q4 E
- **Vídeo 2:** pronto sem voz · `ep2_promocoes` · 1726 pal. ~11,5 min · voz: parte 2 da cena 18 · capa A · nova C, Q6 D, Q5 A, Q8 D · erro 2 com números nossos (80 → 68) para não entregar a Q6
- **Vídeo 4:** pronto sem voz · `ep4_revisao` · 1642 pal. ~10,9 min · voz: parte 2 da cena 18 · capa A · inéditas B, E, C, A, D
