# Empréstimos, Financiamentos e Parcelamentos — série de videoaulas

Material de apoio (cópia em `_material/17-emprestimos-financiamentos-parcelamentos.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/17-emprestimos-financiamentos-parcelamentos.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Levar ao futuro × (1 + i)ⁿ e trazer ao presente ÷ (1 + i)ⁿ | **Juros Compostos** (série 14, seção 07 e Q3) | Revisão relâmpago. O novo é a **sequência de parcelas**, cada uma pelo seu prazo, e o rotativo como "levar a dívida ao futuro". |
| **Questão 8 do material** (2.420 ÷ 1,21 = 2.000, quitação antecipada) | Mesma conta e mesmos distratores (÷ 1,1; × 0,9; × 1,21) da **Questão 3 de Juros Compostos** (12.100 ÷ 1,21) | **Não uso.** Entra uma questão nova de quitação de **três** parcelas de R$ 1.331,00, com o texto completo no prompt do vídeo 1. |
| Taxa embutida com entrada | **Juros Simples** (série 13, Q8, pagamento em 2 meses) | Citada no vídeo 2; aqui o formato mais cobrado, uma parcela em 30 dias (com um único período, simples e compostos dão o mesmo). |
| Soma dos juros do SAC como PA | **Progressão aritmética** (31) tem série própria | Uso só a fórmula dada no material, com a promessa da série própria. |
| Taxa mensal de dois dígitos vira anual de três (rotativo) | **Taxas Equivalentes**, vídeo 1 | Só citado. |
| Pagar à vista ou parcelar | **Comparação de propostas** (18) | Só prometido. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Dinheiro em datas diferentes: parcelas, quitação e rotativo** | 03, 09 | Q7, Q6, Nova (no lugar da Q8) | 10–12 min |
| **2. Entrada mais uma parcela e o falso "sem juros"** | 02 (valor financiado, entrada), 04, 05 | Q1 | 6–8 min |
| **3. Sistema de Amortização Constante (SAC)** | 02 (saldo, juros, amortização, parcela), 06 | Q2, Q3 | 8–10 min |
| **4. Sistema Price e SAC × Price** | 07, 08 | Q4, Q9, Q5 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Questão 1 (vídeo 2):** o denominador é o **valor financiado, R$ 400,00** (900 − 500), e a taxa é **25% ao mês**. A IA tende a dividir por 900 (11,1%), que é justamente o distrator C, e a confundir com o exemplo da geladeira, que dá 11,1%.
- **Rotativo (vídeo 1):** 1,12³ = 1,404928, então 1.500 · 1,12³ = **R$ 2.107,39**; o material arredonda o fator para 1,405 e escreve ≈ R$ 2.107,50. As duas versões servem, desde que a IA não misture "1,405" com "2.107,39" na mesma cena.
- **SAC (vídeo 3):** na Q3, a PA dos juros vai de **600 até 60** (10 termos), e o total é **R$ 3.300,00**. Se a IA terminar a PA em zero, sai R$ 3.000,00, o distrator A.
- **Price (vídeo 4):** a amortização **cresce** e os juros **caem**. A IA às vezes descreve a Price como "amortização constante", que é o SAC (é o distrator B da Q5).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_datas_diferentes` · 1763 pal. ~11,8 min · voz: parte 2 da cena 18 · capa A · Q7 C, Q6 C, nova B
- **Vídeo 2:** pronto sem voz · `ep2_entrada_sem_juros` · 1040 pal. ~6,9 min · voz: parte 2 da cena 14 · capa A · Q1 E
- **Vídeo 4:** pronto sem voz · `ep4_price_sac` · 1739 pal. ~11,6 min · voz: parte 2 da cena 19 · capa C · Q4 C, Q9 D, Q5 A
- **Vídeo 3:** pronto sem voz · `ep3_sac` · 1477 pal. ~9,8 min · voz: parte 2 da cena 20 · capa B · Q2 D, Q3 B
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1663 pal. ~11,1 min · voz: parte 2 da cena 20 · capa A · inéditas E, D, B, C, A
