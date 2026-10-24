# Polinômios e Equações Polinomiais — série de videoaulas

Material de apoio (cópia em `_material/35-polinomios-equacoes-polinomiais.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/35-polinomios-equacoes-polinomiais.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Termos semelhantes, distributiva, valor numérico com parênteses, fatoração | **Expressões algébricas e produtos notáveis** | Revisão relâmpago no vídeo 1; não reensino as operações. |
| Caixa recortada de uma folha (área do fundo com (a − 2x)(b − 2x)) | **Expressões algébricas**, Questão 6 (folha de 30 × 20, área do fundo) | **Mantive a Questão 1** deste material: a folha é outra (24 × 15) e a pergunta é o **volume** (grau 3), que é o conteúdo novo. No roteiro, o fundo é tratado como revisão e o foco é multiplicar pela altura x. |
| Bhaskara, soma −b/a e produto c/a, forma fatorada do 2º grau | **Equação do 2º grau e Bhaskara** | Revisão relâmpago. O novo é Girard no 3º grau (sinais −, +, −) e terminar a redução de grau no 2º grau. |
| Raízes como pontos onde o gráfico corta o eixo | **Função quadrática** (parábola) | Citado; aqui o novo é a multiplicidade (toca × atravessa). |
| Unidade imaginária i e raízes conjugadas (Questão 6) | **Números complexos** (próxima série) | Só i² = −1 em uma frase e a regra do par conjugado. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Polinômio, grau, valor numérico e modelagem** | 02, 03 | Q1, Q8 | 8–10 min |
| **2. Divisão, Briot-Ruffini e o teorema do resto** | 04, 05 | Q2, Q9 | 10–12 min |
| **3. Caçando raízes: forma fatorada, candidatas racionais e redução de grau** | 06, 07 | Q3, Q7 | 10–12 min |
| **4. Girard e gráficos: soma, produto, multiplicidade e raízes conjugadas** | 08, 09 | Q4, Q5, Q6 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

O próprio material avisa que a teoria completa de polinômios cai mais em vestibulares tradicionais do que no ENEM; por isso a revisão dá peso a modelagem e leitura de gráfico.

---

## Cuidados ao revisar os roteiros

- **Sinais de Girard no 3º grau:** soma −b/a, pares c/a, produto **−d/a**. Na Questão 4 o produto é −(−16)/2 = 8; se a IA usar d/a, aparece −8, que nem está nas alternativas, e ela tende a "ajustar" a conta.
- **Raiz do divisor:** para x + 3 usa-se −3; para x + 2, −2. Na Questão 2, P(−3) = 0 leva a k = −13 (distrator B); a resposta é k = −5, com P(3).
- **Coeficiente zero:** em x³ − 4x + 1 e x³ − 7x + 6 (exercícios dos vídeos 2 e 3) e na questão inédita 2 da revisão, o zero precisa aparecer na esteira. Confira a tela.
- **Questão 6 e a inédita 5:** usam i² = −1 antes da série de Números complexos. (1 − i)(1 + i) = 1 − i² = 2 e (2i)(−2i) = −4i² = 4; com i² = 1 a IA chega nos distratores C e B, respectivamente.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_grau_valor_modelagem` · 1410 pal. ~9,4 min · voz: parte 2 da cena 16 · capa A · Q1 D, Q8 A · CORRIGIDO: conferência da Q1 com x = 1 não basta (B e E também dão 286); vídeo confere com x = 2
- **Vídeo 2:** pronto sem voz · `ep2_briot_ruffini_resto` · 1634 pal. ~10,9 min · voz: parte 2 da cena 18 · capa B · Q2 C, Q9 B · erro 1 do prompt (÷ x − 1) não mostrava o erro; usado ÷ x − 2
- **Vídeo 3:** pronto sem voz · `ep3_cacando_raizes` · 1542 pal. ~10,3 min · voz: parte 2 da cena 17 · capa A · Q3 A, Q7 E
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1675 pal. ~11,2 min · voz: parte 2 da cena 21 · capa A · inéditas C, A, E, E, A
- **Vídeo 4:** pronto sem voz · `ep4_girard_graficos` · 1708 pal. ~11,4 min · voz: parte 2 da cena 18 · capa B · Q4 B, Q5 E, Q6 B · bloco e com o par 2 ± i (não entregar a Q6)
