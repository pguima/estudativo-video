# Expressões Algébricas e Produtos Notáveis — série de videoaulas

Material de apoio (cópia em `_material/19-expressoes-algebricas-produtos-notaveis.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/19-expressoes-algebricas-produtos-notaveis.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Regras de sinais, −2² × (−2)², ordem das operações | **Operações e conjuntos numéricos** (série 01) | Revisão relâmpago no vídeo 1, com o mesmo exemplo de lá: −3² = −9, (−3)² = 9. |
| Expoente distribui no produto e não na soma; x² · x³ = x⁵ | **Potenciação e radiciação** (série 04) | Revisão relâmpago nos vídeos 1 e 2. O novo é o desenho do quadrado (a + b)². |
| Somar frações pelo MMC, cortar só fatores | **Frações, decimais e dízimas** (série 03) | Revisão relâmpago no vídeo 3, antes das frações algébricas. |
| **Questão 8** (+30% e depois −30%) | Quase igual à **Questão 4 de Porcentagem** (+20% e −20% dão −4%), que já está no canal | **Não uso como questão.** No vídeo 4 vira uma conexão de 1 minuto: o porquê da regra de Porcentagem, (1 + p)(1 − p) = 1 − p², com os números da Q8 narrados, sem alternativas. |
| (1 + i)² nos juros compostos; Bhaskara nasce do quadrado da soma | **Juros Compostos** (série 14) e **Equação do 2º grau** (série 21) | Só citar. |
| Trinômio soma e produto (x² + 5x + 6) | **Equação do 2º grau** (série 21) usa para achar raízes | Aqui só como fatoração; resolver equação fica para a série 21. |
| Pitágoras na Q5 (diagonal² = a² + b²) | Teorema de Pitágoras tem série própria (Geometria) | Dado pronto em uma frase; o foco é a² + b² = (a + b)² − 2ab. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Linguagem algébrica, valor numérico e operações com polinômios** | 02, 03 | Q1, Q6 | 10–12 min |
| **2. Produtos notáveis e o sonho do calouro** | 04, 05 | Q2, Q7, Q9 | 10–12 min |
| **3. Fatoração, frações algébricas e o produto notável ao contrário** | 06, 07 | Q4, Q5 | 10–12 min |
| **4. Contas de cabeça com produtos notáveis** | 08 | Q3 (+ conexão com Porcentagem) | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Termo do meio com coeficiente:** em (2x − 3)², o termo do meio é 2 · 2x · 3 = **12x**. A IA de vídeo às vezes escreve 6x (esquece o 2 de 2ab) e às vezes deixa o 9 negativo. Esse é exatamente o distrator C da Questão 7 (−12x em vez de −24x).
- **Valor numérico com negativo:** 3x² − 2x + 1 em x = −2 dá **17**. Se a IA escrever "3 · −2²", chega a −12 + 4 + 1 = −7. Exija os parênteses na tela: 3 · (−2)².
- **Frações algébricas na tela:** confira se (x − 4)/(x + 4) não foi escrita como x − 4/x + 4 (sem parênteses, outra expressão). Na alternativa A da Questão 4, o "corte" do x² deixa −16/(8x + 16), que é −2/(x + 2).
- **Conexão com Porcentagem (vídeo 4):** 0,91 significa 9% **abaixo**. Fique de olho em "0,09%" ou "9% acima" na narração.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_linguagem_polinomios` · 1750 pal. ~11,7 min · voz: parte 2 da cena 21 · capa A · Q1 C, Q6 E
- **Vídeo 2:** pronto sem voz · `ep2_produtos_notaveis` · 1722 pal. ~11,5 min · voz: parte 2 da cena 17 · capa A · Q2 D, Q7 B, Q9 D
- **Vídeo 3:** pronto sem voz · `ep3_fatoracao_fracoes` · 1716 pal. ~11,4 min · voz: parte 2 da cena 17 · capa A · Q4 B, Q5 A · bloco h trocado (soma 5, produto 6) para não entregar a Q5
- **Vídeo 4:** pronto sem voz · `ep4_contas_de_cabeca` · 1161 pal. ~7,7 min · voz: parte 2 da cena 14 · capa A · Q3 A · reta 997/1000/1003 só na resolução; erros com 503 · 497
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1727 pal. ~11,5 min · voz: parte 2 da cena 22 · capa A · inéditas D, B, E, A, C
