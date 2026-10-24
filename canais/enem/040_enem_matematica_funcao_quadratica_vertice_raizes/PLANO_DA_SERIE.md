# Função Quadrática: Vértice, Raízes, Máximo e Mínimo — série de videoaulas

Material de apoio (cópia em `_material/25-funcao-quadratica-vertice-raizes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/25-funcao-quadratica-vertice-raizes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Forma geral, coeficientes com sinal, Bhaskara, Δ, soma e produto, forma fatorada, "nunca divida por x" | **Equação do 2º grau e fórmula de Bhaskara** (série 21) | Tudo vira revisão relâmpago (vídeo 1). Achar as raízes é pré-requisito. O foco aqui é o **gráfico**: concavidade, vértice, máximo/mínimo e sinal. |
| **Questão 7 deste material** (x² − 6x + k acima do eixo, k > 9) | Quase igual à **Questão 2 do material 21** (mesma função x² − 6x + k, Δ = 0, k = 9), também usada como exemplo na seção 05 de 21 | **Não uso.** No lugar dela entra uma questão nova, com o texto completo no prompt do vídeo 1: −x² + 10x − k abaixo do eixo, k > 25. Ela treina a mesma habilidade e ainda cobra o sinal de a. |
| h(t) = 20t − 5t² passando por 15 m em 1 s e 3 s | **Questão 4 do material 21** | No vídeo 2, a seção 08 é usada só para o **vértice** (2 s, 20 m) e a simetria. Os instantes de 15 m são citados como "você já resolveu na série de Equação do 2º grau". |
| Lucro positivo entre as raízes (a < 0) | Q7 do material 21 pede a **menor** quantidade sem prejuízo | Mantive a Q5 daqui (pede o **intervalo**, com distrator de sinal invertido). A habilidade nova é o estudo do sinal. |
| Taxa de variação constante, ponto de equilíbrio | **Função afim** (série 24) | Gancho do vídeo 1: na afim os degraus são iguais; na parábola não são. |
| Leitura de máximo, mínimo, crescimento e imagem no gráfico | **Conceito de função** (série 23, vídeo do gráfico) | Pré-requisito de 30 s ("sombra na parede"). |
| Produtos notáveis para passar da forma canônica para a geral | **Expressões algébricas e produtos notáveis** (série 19) | Citado no vídeo 4. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A parábola: concavidade, corte no eixo y e raízes (o que o Δ desenha)** | 02, 03 | questão nova (substitui a Q7) | 8–10 min |
| **2. O vértice: eixo de simetria, máximo ou mínimo e trajetórias** | 04, 08 | Q1, Q8, Q9 | 10–12 min |
| **3. Otimização: área máxima e receita máxima** | 05 | Q3, Q2 | 10–12 min |
| **4. Três formas da mesma função e estudo do sinal** | 06, 07 | Q4, Q6, Q5 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

A Questão 7 do material ficou de fora por causa da duplicação com a série 21 (ver tabela acima).

---

## Cuidados ao revisar os roteiros

- **Questão nova do vídeo 1:** com a = −1, b = 10 e c = −k, o produto 4ac vale 4 · (−1) · (−k) = **+4k**, e então Δ = 100 − 4k. A IA costuma escrever Δ = 100 + 4k e chegar em k < −25, que é o distrator E. A resposta é **k > 25**.
- **y do vértice (vídeo 2):** na Q8, C(30) = 2 · 900 − 3 600 + 5 000 = **3 200**. A IA às vezes faz 2 · 30² como 3 600 (dobra antes de elevar ao quadrado) e chega em 5 000, que é o distrator E.
- **Preço × desconto (vídeo 3, Q2):** a resposta é o **preço de R$ 45,00**. O desconto de R$ 15,00 é o distrator A. Confira também a receita: 45 · 450 = 20 250.
- **Arco da ponte (vídeo 4, Q6):** a altura a 5 m do pé é **4,375 m**. O valor 5,625 m (distrator C) é o quanto o arco desceu em relação ao topo. A IA confunde os dois com facilidade, porque 4,375 + 5,625 = 10.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 3:** pronto sem voz · `ep3_otimizacao` · 1665 pal. ~11,1 min · voz: parte 2 da cena 14 · capa A · Q3 C, Q2 C
- **Vídeo 1:** pronto sem voz · `ep1_parabola_delta` · 1440 pal. ~9,6 min · voz: parte 2 da cena 17 · capa A · nova C (k > 25)
- **Vídeo 2:** pronto sem voz · `ep2_vertice` · 1694 pal. ~11,3 min · voz: parte 2 da cena 20 · capa A · Q1 B, Q8 A, Q9 C
- **Vídeo 4:** pronto sem voz · `ep4_formas_sinal` · 1727 pal. ~11,5 min · voz: parte 2 da cena 18 · capa A · Q4 B, Q6 B, Q5 D
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1713 pal. ~11,4 min · voz: parte 2 da cena 21 · capa A · inéditas C, D, E, A, B
