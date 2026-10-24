# Sistemas de Equações Lineares — série de videoaulas

Material de apoio (cópia em `_material/22-sistemas-equacoes-lineares.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/22-sistemas-equacoes-lineares.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver equação do 1º grau, montar a partir do texto, "releia a pergunta" | **Equações do 1º grau, vídeos 1 e 2** | Revisão relâmpago, com as mesmas analogias (balança, etiqueta do x). |
| Fretes com a mesma tarifa por km que nunca empatam (Q6 de Equações, 0x = −4) | **Equações do 1º grau, vídeo 1** | Retomada no vídeo 3 como "retas paralelas", sem repetir a questão. |
| Classificação SPD / SPI / SI e retas concorrentes, paralelas e coincidentes | Também na **série 34 (Determinantes e sistemas lineares)** | **Fica aqui:** classificação pela conta (0 = 2, 0 = 0), pelas razões entre coeficientes e pelo desenho das retas. Na série 34 entram o determinante (D ≠ 0), Cramer, discussão com dois parâmetros, sistema homogêneo e escalonamento 3 × 3 com classificação: aqui, **só citar**. |
| Ingressos de R$ 40 e R$ 20 | Q1 daqui (400 ingressos, R$ 11.200) × Q1 da série 34 (250 ingressos, R$ 7.400, por Cramer) | Mesmo contexto, números diferentes. Uso a Q1 daqui, resolvida por substituição. |
| Paralelas: Q6 daqui (x + 2y = 4 e 2x + 4y = 10) × Q5 da série 34 (3x − 6y = 9 e −x + 2y = 4) | Série 34 | Mesmo tipo, números diferentes. Uso a Q6 daqui, sem determinante. |
| Retas como funções, ponto de equilíbrio com gráfico | **Conceito de Função** (23) e **Função afim** (24) | Só a ponte no vídeo de revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é um sistema, do texto ao sistema e o método da substituição** | 02, 03, 04 | Q1, Q5, Q9 | 10–12 min |
| **2. O método da adição e quando a pergunta já é a soma** | 05 | Q4, Q7 | 8–10 min |
| **3. As três posições de duas retas e classificar sem resolver** | 06, 07 | Q6, Q3 | 10–12 min |
| **4. Três incógnitas: escalonar ou somar tudo** | 08 | Q2, Q8 | 8–10 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Tradução invertida:** "Pedro tem o dobro de Júlia" é **P = 2J**. A IA de vídeo às vezes escreve 2P = J na tela enquanto a narração diz o certo. Confira a tela do gancho do vídeo 1 e a Questão 5.
- **Substituição com parênteses:** 4c + 2(30 − c) = 100 → **4c + 60 − 2c** = 100 → c = 20. Se aparecer 60 − c, o resultado vira c = 13,3 e a aula se contradiz.
- **Questão 6 (paralelas):** 2 · (x + 2y = 4) dá 2x + 4y = 8. Comparando com 2x + 4y = 10, sai 0 = 2 (ou 0 = −2, conforme a ordem da subtração). As duas formas indicam SI. A IA às vezes conclui "coincidentes" porque os coeficientes da esquerda são proporcionais.
- **Fronteira com a série 34:** se a IA calcular D = a₁b₂ − a₂b₁ ou usar Cramer nos vídeos 3 e 4, corte. Na Questão 2, a soma das pesagens (410) se divide por **2** (total 205), e não por 3.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_texto_substituicao` · 1741 pal. ~11,6 min · voz: parte 2 da cena 18 · capa A · Q1 D, Q5 D, Q9 B
- **Vídeo 4:** pronto sem voz · `ep4_tres_incognitas` · 1369 pal. ~9,1 min · voz: parte 2 da cena 16 · capa A · Q2 C, Q8 B
- **Vídeo 2:** pronto sem voz · `ep2_metodo_adicao` · 1406 pal. ~9,4 min · voz: parte 2 da cena 18 · capa A · Q4 B, Q7 C
- **Vídeo 3:** pronto sem voz · `ep3_tres_posicoes` · 1633 pal. ~10,9 min · voz: parte 2 da cena 16 · capa A · Q6 E, Q3 A · bloco e trocado (k = 4) para não entregar a Q3
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1707 pal. ~11,4 min · voz: parte 2 da cena 21 · capa A · inéditas B, D, C, E, A
