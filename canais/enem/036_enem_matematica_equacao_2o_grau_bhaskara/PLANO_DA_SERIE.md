# Equação do 2º Grau e Fórmula de Bhaskara — série de videoaulas

Material de apoio (cópia em `_material/21-equacao-2o-grau-bhaskara.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/21-equacao-2o-grau-bhaskara.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Quadrado da soma, fator comum, trinômio soma e produto | **Expressões Algébricas, vídeos 2 e 3** | Revisão relâmpago. Lá era fatorar; aqui é achar raízes (produto nulo). |
| Roteiro de resolução, montar equação a partir do texto, raiz não é a resposta | **Equações do 1º grau, vídeos 1 e 2** | Revisão relâmpago, com as mesmas analogias (etiqueta do x, releia a pergunta). |
| Raízes como cortes da parábola no eixo x; Δ e número de toques | **Função Quadrática** (série 25) | Só citar, com um único desenho ilustrativo. Gráfico, concavidade e vértice ficam para a série 25. |
| Vértice, máximo e mínimo, estudo do sinal, inequações do 2º grau | **Função Quadrática** (série 25) | Só citar. Na Q7 (lucro), a alternativa B (20, o vértice) é explicada como "lucro máximo, assunto da Função quadrática". O sinal do lucro é conferido **testando valores** (x = 5 dá prejuízo, x = 20 dá lucro), sem a regra do sinal. |
| h(t) = 20t − 5t² passando por 15 m em 1 s e 3 s | A série 25 usa a mesma função como exemplo (seção 08) | A Q4 fica aqui, só com os instantes (raízes). Altura máxima e simetria ficam para a série 25. |
| y = x² − 6x + k | Q2 daqui (Δ = 0, k = 9) × Q7 da série 25 (Δ < 0, k > 9) | Uso a Q2. "Parábola toda acima do eixo" fica para a série 25. |
| Soma e produto (relações de Girard) | A série 25 usa como atalho | **Ensinado aqui** (vídeo 3). A série 25 só revisa. |
| Pitágoras (Q9) | Série própria na Geometria | Dado pronto em uma frase. |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Forma geral, coeficientes com sinal e equações incompletas** | 02, 03 | Q5 | 8–10 min |
| **2. A fórmula de Bhaskara e o que o Δ revela** | 04, 05 | Q2 | 10–12 min |
| **3. Soma e produto: raízes de cabeça e equação a partir das raízes** | 06 | Q3, Q4 | 8–10 min |
| **4. Do texto à equação: modelar e descartar raízes** | 07 | Q1, Q6, Q9, Q7 | 10–12 min |
| **5. Equações que viram do 2º grau: biquadradas e x no denominador** | 08 | Q8 | 6–8 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Sinal do b:** em 2x² − 7x + 3 = 0, Δ = (−7)² − 24 = **25** e x = **(7 ± 5)/4** → 3 e 1/2. A IA de vídeo às vezes escreve −b = −7 e chega a −3 e −1/2. Confira a tela do vídeo 2.
- **Questão 7 (lucro):** a resposta é **10** (onde o prejuízo acaba). A IA tende a puxar o vértice (20) porque "lucro" lembra "máximo". Confira também o teste de valores: L(5) = −25 + 200 − 300 = −125 e L(20) = −400 + 800 − 300 = 100.
- **Descarte de raiz:** na Questão 1 a resposta é 2 m. Fique de olho em frases como "a raiz −10, em módulo, 10": isso é exatamente o distrator E.
- **Fronteira com a série 25:** se a IA começar a calcular x_V = −b/2a ou altura máxima nas Questões 2, 4 ou 7, corte. Esse conteúdo é da Função Quadrática, e o exemplo da seção 08 de lá usa a mesma bola (h = 20t − 5t²).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_forma_incompletas` · 1444 pal. ~9,6 min · voz: parte 2 da cena 16 · capa A · Q5 E · bloco c/erro 2 trocados (2x² − 10x) para não entregar a Q5
- **Vídeo 2:** pronto sem voz · `ep2_bhaskara_delta` · 1577 pal. ~10,5 min · voz: parte 2 da cena 17 · capa A · Q2 C · exemplos de Δ = 0 trocados (k = 16) para não entregar a Q2
- **Vídeo 3:** pronto sem voz · `ep3_soma_produto` · 1441 pal. ~9,6 min · voz: parte 2 da cena 20 · capa A · Q3 D, Q4 B · cartas soma 4/produto 3 só na resolução
- **Vídeo 5:** pronto sem voz · `ep5_biquadrada_denominador` · 1100 pal. ~7,3 min · voz: parte 2 da cena 14 · capa B · Q8 C · material escreve (5 ± 13/2); certo (5 ± 13)/2
- **Vídeo 4:** pronto sem voz · `ep4_texto_equacao` · 1691 pal. ~11,3 min · voz: parte 2 da cena 18 · capa A · Q1 A, Q6 C, Q9 D, Q7 A · erro 3 trocado (x² + (x+1)² = 25) para não entregar a Q9
- **Vídeo 6:** pronto sem voz · `ep6_revisao` · 1745 pal. ~11,6 min · voz: parte 2 da cena 20 · capa A · inéditas A, D, E, B, C
