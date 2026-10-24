# Taxas Equivalentes e Inflação — série de videoaulas

Material de apoio (cópia em `_material/16-taxas-equivalentes-inflacao.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/16-taxas-equivalentes-inflacao.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Taxa proporcional (2% a.m. = 24% a.a.) | **Juros Simples** (série 13, seção 04) | Revisão relâmpago: "certa em juros simples, errada em compostos". |
| M = C(1 + i)ᵗ, potências 1,1² = 1,21 e 1,1³ = 1,331, taxas diferentes em sequência | **Juros Compostos** (série 14) e **Porcentagem** (09) | Revisão rápida; a seção 05 (taxas acumuladas) vira um bloco curto do vídeo 2. |
| **Questão 4 do material** (inflação de 10% e 20% → 32%) | Mesma conta e quase as mesmas alternativas da **Questão 3 de Porcentagem** (reajustes de 10% e 20% → 32%) | **Não uso.** Entra uma questão nova (inflação de 25% e 20% → 50%), com o texto completo no prompt do vídeo 3. |
| Poder de compra (1 ÷ 1,25 = 0,80) | Mesma conta de "voltar ao valor original" da série de Porcentagem | Apresentada como a mesma ideia com outro nome, como o próprio material faz; a Q5 fica (a pergunta é outra). |
| Taxa de cada período para parcelas e rotativo | **Empréstimos** (17) e **Comparação de propostas** (18) | Só prometido na ponte. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Proporcional × equivalente: trocar o período de uma taxa** | 02, 03 | Q1, Q2, Q9 | 10–12 min |
| **2. Taxa nominal × efetiva e taxas acumuladas** | 04, 05 | Q3 + 1 questão nova ("você faz") | 8–10 min |
| **3. Inflação, inflação acumulada e poder de compra** | 06, 07 | Nova (no lugar da Q4), Q5 | 8–10 min |
| **4. Taxa real e a armadilha da subtração** | 07 (deflacionar), 08, 09 | Q6, Q8, Q7 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Perda de poder de compra × inflação (vídeo 3):** inflação de 25% tira **20%** (1 ÷ 1,25 = 0,80); inflação de 100% tira **50%**. A IA costuma dizer "perde 25%" e contradiz o próprio exemplo.
- **Taxa real (vídeo 4):** 1,26 ÷ 1,20 = **1,05 → 5%**, não 6%; 1,06 ÷ 1,10 ≈ **0,964 → perda de ≈ 3,6%**, não 4%. Se a IA usar a subtração "para simplificar", ela cai exatamente no distrator.
- **Taxa nominal (vídeo 2):** dividir 24% por 12 só dá a taxa **do período de capitalização** (2% ao mês); a efetiva anual é 1,02¹² − 1 ≈ **26,8%**. A IA às vezes chama os 2% de "taxa mensal equivalente a 24% ao ano", o que inverte a lição do vídeo 1.
- **Gancho do vídeo 1:** 1,1¹² ≈ 3,14 significa cerca de **214% ao ano** (tirando o 1), não 314%.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 2:** pronto sem voz · `ep2_nominal_efetiva` · 1430 pal. ~9,5 min · voz: parte 2 da cena 18 · capa B · Q3 C, nova D
- **Vídeo 3:** pronto sem voz · `ep3_inflacao_poder_compra` · 1396 pal. ~9,3 min · voz: parte 2 da cena 16 · capa A · nova D, Q5 B
- **Vídeo 1:** pronto sem voz · `ep1_proporcional_equivalente` · 1711 pal. ~11,4 min · voz: parte 2 da cena 18 · capa A · Q1 D, Q2 C, Q9 E · bloco d/erro 2 trocados para 69% a.a. (não entregar a Q9)
- **Vídeo 4:** pronto sem voz · `ep4_taxa_real` · 1688 pal. ~11,3 min · voz: parte 2 da cena 19 · capa A · Q6 B, Q8 A, Q7 E · plausibilidade corrigida: a real fica mais perto do zero que a subtração
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1618 pal. ~10,8 min · voz: parte 2 da cena 18 · capa A · inéditas C, A, D, B, E · hábito 3 do material (taxa real 'abaixo da diferença') só vale com ganho
