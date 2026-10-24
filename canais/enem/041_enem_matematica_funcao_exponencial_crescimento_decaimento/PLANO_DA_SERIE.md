# Função Exponencial: crescimento e decaimento — série de videoaulas

Material de apoio (cópia em `_material/26-funcao-exponencial-crescimento-decaimento.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/26-funcao-exponencial-crescimento-decaimento.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Expoente zero, expoente negativo (2⁻³ = 1/8), mesma base | **Potenciação e radiciação** | Revisão relâmpago nos vídeos 1 e 5 ("expoente negativo inverte, não troca o sinal"). Não reensino as propriedades. |
| Taxa vira fator (1 + i, 1 − i) | **Porcentagem** | Revisão de 30 s no vídeo 2. O novo é escrever a lei Q₀ · aᵗ. |
| M = C · (1 + i)ᵗ, tempo de duplicação constante | **Juros Compostos** | Vídeo 2 trata como "você já viu isso disfarçado": é a mesma exponencial com C no lugar de Q₀. Nenhuma questão de Juros Compostos é reutilizada. |
| Função afim, diferença constante | **Função afim** | Revisão relâmpago no vídeo 4 (teste da diferença × teste da razão). |
| Termo geral da PG, valores em PG | **Progressão geométrica** (série futura) | Só cito: "os valores de uma exponencial em tempos iguais formam uma PG; isso tem série própria". |
| **Q1 (500 bactérias, dobra a cada 20 min, 2 h)** e **Q2 (80 mg, 4 meias-vidas → 5 mg)** | **Q1 de PG é idêntica à Q1 daqui; a Q2 de PG (80 g, meia-vida de 5 anos, 20 anos → 5 g) é quase igual à Q2 daqui** | **Uso aqui**, porque esta série vem antes e é o lar do tema. A série de PG não deve repetir essas duas (pendência no relatório). A Q3 daqui (tabela, fator 0,8) tem o mesmo formato da Q9 de PG, mas números diferentes. |
| Equação que "não fecha" (2ˣ = 10) | **Logaritmos** (próxima série) | Só prometo: "a ferramenta é o logaritmo, próxima série". |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Multiplicar em vez de somar: a função exponencial e seu gráfico** | 02, 03 | Q9 | 8–10 min |
| **2. O modelo Q₀ · aᵗ: da frase do enunciado ao fator** | 04 | Q3, Q6 | 8–10 min |
| **3. Duplicação e meia-vida: conte os intervalos** | 05 | Q1, Q2, Q8 | 10–12 min |
| **4. Exponencial ou afim? O teste da razão** | 06 | Q5 | 6–8 min |
| **5. Equações e inequações exponenciais: mesma base** | 07, 08 | Q4, Q7 | 10–12 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Contagem de intervalos (vídeo 3):** em 2 h com duplicação a cada 20 min são **6** duplicações (500 · 2⁶ = 32 000). A IA às vezes conta o instante inicial e chega a 7 (64 000), que é justamente a alternativa E.
- **Expoente negativo e coeficiente (vídeos 1 e 2):** 2⁻² = 1/4 (positivo) e 3 · 2ˣ **não** é 6ˣ. Confira se a narração não "simplifica" 3 · 2³ como 6³ = 216 (o certo é 24, a resposta da Q6).
- **Inequação com base entre 0 e 1 (vídeo 5 e questão inédita 5 da revisão):** (1/3)ˣ > 9 dá x **<** −2; no forno, 0,5^(t/10) > 0,5³ dá t/10 **<** 3. A IA costuma manter o sentido. Na questão do forno, confira também se ela subtrai os 20 °C **antes** de dividir por 160.
- **Questão 5 (vídeo 4):** na semana 4, B (1 600) ainda perde para A (2 200). A resposta é **5** semanas (3 200 contra 2 500), não 4.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_multiplicar_grafico` · 1360 pal. ~9,1 min · voz: parte 2 da cena 16 · capa A · Q9 A · bloco g trocado (sopa a 22 °C) para não entregar a Q9
- **Vídeo 2:** pronto sem voz · `ep2_modelo_fator` · 1454 pal. ~9,7 min · voz: parte 2 da cena 16 · capa A · Q3 E, Q6 C · bloco e trocado (a = 3) para não entregar a Q6
- **Vídeo 3:** pronto sem voz · `ep3_duplicacao_meia_vida` · 1608 pal. ~10,7 min · voz: parte 2 da cena 16 · capa B · Q1 D, Q2 B, Q8 D
- **Vídeo 4:** pronto sem voz · `ep4_teste_razao` · 1141 pal. ~7,6 min · voz: parte 2 da cena 14 · capa A · Q5 C
- **Vídeo 5:** pronto sem voz · `ep5_mesma_base` · 1731 pal. ~11,5 min · voz: parte 2 da cena 19 · capa A · Q4 B, Q7 C · bloco g trocado (cloro da piscina) para não entregar a Q7
- **Vídeo 6:** pronto sem voz · `ep6_revisao` · 1747 pal. ~11,6 min · voz: parte 2 da cena 21 · capa A · inéditas C, B, E, C, D
