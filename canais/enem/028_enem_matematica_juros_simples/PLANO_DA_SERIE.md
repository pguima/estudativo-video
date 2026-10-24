# Juros Simples — série de videoaulas

Material de apoio (cópia em `_material/13-juros-simples.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/13-juros-simples.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator de multiplicação (1 + i), forma decimal da taxa, "aumento único de 12%" | **Porcentagem** (fator, variações sucessivas) | Revisão relâmpago no vídeo 1. O fator 1 + i·t aparece como "um aumento único", sem reensinar porcentagem. |
| Proporcionalidade entre juros e tempo; regra de três | **Razão, proporção e regra de três** e **Grandezas Proporcionais** | Só uma frase: "é por isso que a regra de três funciona aqui". |
| Taxas proporcionais (24% a.a. = 2% a.m.) | **Taxas equivalentes e inflação** (série própria) | Ensino a proporcional, que é deste assunto, e só aviso: "em juros compostos, dividir por 12 não vale; isso tem série própria". Não mostro 1,02¹² nem taxa equivalente. |
| Montante como reta (y = b + ax) | **Função afim** (série própria) | Uso só a leitura do gráfico (ponto em t = 0 e inclinação). Coeficientes e equação da reta ficam para a série de Função afim, só citada. |
| Montantes formando PA | **Progressão aritmética** (série própria) | Só reconhecer "soma constante = PA" e a razão C·i. Termo geral e soma da PA ficam para a série própria. |
| Contraste com juros compostos (PG, curva) | **Juros compostos e montante** (próxima série) | Só promessa, na ponte do vídeo 3 e na revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O vocabulário do dinheiro e a fórmula J = C · i · t** | 02, 03 | Q1 | 8–10 min |
| **2. Taxa e tempo na mesma unidade (meses, anos, dias e o boleto atrasado)** | 04, 08 | Q2, Q9, Q5 | 10–12 min |
| **3. O montante é uma reta (gráfico, tabela e PA)** | 05, 07 | Q7, Q6 | 8–10 min |
| **4. Descobrindo capital, taxa ou tempo** | 06 | Q3, Q8, Q4 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Vídeo 2, sentido da conversão:** mensal → anual **multiplica** (2% a.m. = 24% a.a.); anual → mensal **divide**. A IA costuma escrever "2% a.m. ÷ 12" ou "18% a.a. × 12". E o erro de converter os dois não é "sempre 12 vezes menor" (como diz o material): depende do sentido.
- **Vídeo 4, Questão 4:** 100 meses = **8 anos e 4 meses** (8 · 12 = 96; sobram 4). A IA tende a escrever 8,33 anos = "8 anos e 3 meses", que é justamente o distrator B.
- **Vídeo 4, Questão 8:** a taxa é 60 ÷ (600 · 2) = 5%, sobre o valor **financiado** (1.000 − 400), não sobre o preço de R$ 1.000,00 nem sobre a entrada. Confira também a explicação corrigida da alternativa B.
- **Vídeo 3:** a taxa é a inclinação dividida pelo **capital** (valor em t = 0), não pelo montante final; na Questão 6, 40 ÷ 1.600 = 2,5%, e 40 ÷ 2.000 = 2% é distrator.

## Erros encontrados no material

- **Questão 8, explicação da alternativa B:** o material diz que 6% "calcula os juros sobre o preço total de R$ 1.000,00, como se tudo fosse financiado". Com o preço total **e** a divisão pelos 2 meses, daria 60 ÷ 2.000 = 3%. Os 6% vêm de 60 ÷ 1.000, usando o preço total **e** esquecendo de dividir pelo tempo. O prompt do vídeo 4 usa essa explicação.
- **Seção 11, erro "converter a taxa e também o tempo":** o material diz que o resultado sai "12 vezes menor" nos dois casos. Depende do sentido: com R$ 1.000,00 a 2% a.m. por 2 anos (J correto = 480), usar 24% a.a. com 24 meses dá 5.760 (12 vezes **maior**), e usar 2% com 2 dá 40 (12 vezes **menor**). O prompt do vídeo 2 mostra os dois sentidos.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_vocabulario_formula` · 1553 pal. ~10,4 min · voz: parte 2 da cena 18 · capa A
- **Vídeo 4:** pronto sem voz · `ep4_capital_taxa_tempo` · 1753 pal. ~11,7 min · voz: parte 2 da cena 18 · capa A · Q8 B com a explicação corrigida
- **Vídeo 3:** pronto sem voz · `ep3_montante_reta` · 1457 pal. ~9,7 min · voz: parte 2 da cena 16 · capa A · Q7 E, Q6 B
- **Vídeo 2:** pronto sem voz · `ep2_taxa_tempo` · 1717 pal. ~11,4 min · voz: parte 2 da cena 20 · capa A · Q2 A, Q9 D, Q5 D
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1610 pal. ~10,7 min · voz: parte 2 da cena 18 · capa A · inéditas E, B, D, A, C
