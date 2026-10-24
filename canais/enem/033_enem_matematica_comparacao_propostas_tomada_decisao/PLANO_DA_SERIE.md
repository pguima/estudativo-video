# Comparação de Propostas e Tomada de Decisão — série de videoaulas

Material de apoio (cópia em `_material/18-comparacao-propostas-tomada-decisao.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/18-comparacao-propostas-tomada-decisao.html` · Incidência: Média

## Sobreposições com outras séries

Este assunto é integrador: quase tudo é revisão aplicada das séries 13 a 17. Cada prompt cita o episódio de origem e nenhuma questão dessas séries é repetida.

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Mover valores no tempo (× e ÷ pelo fator), sequência de parcelas | **Juros Compostos** (seção 07) e **Empréstimos, vídeo 1** | Revisão relâmpago com a mesma analogia do câmbio entre datas. O novo é a **data focal** e a **taxa de oportunidade**. |
| Questão 8 (R$ 10.000,00 hoje, R$ 11.000,00 em 1 ano, R$ 12.100,00 em 2 anos) | Usa os mesmos números da **Questão 3 de Juros Compostos** (12.100 ÷ 1,21 = 10.000) | Mantida: a pergunta é outra (decidir entre três prêmios). O prompt cita a origem. |
| Questão 2 (2 × R$ 500,00 ou 5% à vista, aplicação a 1%) | Mesmo formato da **Questão 1 de Empréstimos** (2 × R$ 500,00 ou R$ 900,00 à vista) | Mantida: números e pergunta diferentes (decisão). O prompt cita Empréstimos, vídeo 2. |
| Questão 4 (1% a.m. × 12,5% a.a. × 6% a.s.) | 1,01¹² da **Questão 1 de Taxas Equivalentes** | Mantida como decisão entre três bancos. O prompt cita Taxas Equivalentes, vídeo 1. |
| Custo efetivo com tarifa no ato | Mesma lógica da taxa embutida (**Empréstimos, vídeo 2**) | Citado como "a mesma conta, com a tarifa no lugar da entrada". |
| Planos com parte fixa e variável | **Função afim** (24) e **Otimização e tomada de decisão** (93, com questão própria de planos, outros números) | Só citados. A ponte final é para **Expressões algébricas** (19). |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A regra de ouro: comparar na mesma data (à vista ou a prazo)** | 02, 03 | Q8, Q2 | 10–12 min |
| **2. Planos com parte fixa e variável: o ponto de equilíbrio** | 04, 08 | Q1, Q6, Q9 | 10–12 min |
| **3. Investimentos líquidos e custos escondidos** | 05, 06 | Q7, Q4, Q3 | 10–12 min |
| **4. Ponto de equilíbrio de um negócio e meta de lucro** | 07 | Q5 | 6–8 min |
| **5. Revisão e fechamento do bloco de Matemática Financeira** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **"A partir de" (vídeo 2):** na Q9 a resposta é **13 dias**; com 12 dias as duas opções custam R$ 300,00. Na Q1, "superior a **100** minutos". A IA costuma responder o próprio empate.
- **Questão 2 (vídeo 1):** o preço à vista é **R$ 950,00** e a taxa embutida é 50 ÷ **450** ≈ **11,1%** ao mês. A IA tende a dizer "5% ao mês", que é o distrator D (decisão certa, taxa errada).
- **Questão 4 (vídeo 3):** R = 1,06² = **1,1236 → 12,36%**, abaixo de Q (12,5%) e de P (≈ 12,7%). Se a IA usar 2 · 6% = 12%, a ordem continua certa por acaso, mas a explicação fica errada.
- **Inédita 2 da revisão (vídeo 5):** no empate (600 h) as duas lâmpadas custam R$ 36,00; o mínimo de horas inteiras para a LED ficar mais barata é **601**, não 600. Confira se o enunciado criado pela IA e o gabarito batem.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_mesma_data` · 1649 pal. ~11,0 min · voz: parte 2 da cena 20 · capa A · Q8 E, Q2 A
- **Vídeo 3:** pronto sem voz · `ep3_liquido_custos` · 1671 pal. ~11,1 min · voz: parte 2 da cena 19 · capa A · Q7 E, Q4 D, Q3 B
- **Vídeo 2:** pronto sem voz · `ep2_ponto_equilibrio` · 1727 pal. ~11,5 min · voz: parte 2 da cena 20 · capa A · Q1 B, Q6 C, Q9 C
- **Vídeo 4:** pronto sem voz · `ep4_equilibrio_negocio` · 1064 pal. ~7,1 min · voz: parte 2 da cena 14 · capa A · Q5 D
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1729 pal. ~11,5 min · voz: parte 2 da cena 20 · capa A · inéditas A, C, E, D, C
