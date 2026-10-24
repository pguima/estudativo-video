# Função Modular e Funções Definidas por Partes — série de videoaulas

Material de apoio (cópia em `_material/29-funcao-modular-funcoes-por-partes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/29-funcao-modular-funcoes-por-partes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Função por partes e "hora ou fração" (estacionamento R$ 10,00 + R$ 4,00) | **Conceito de Função**: seção sobre funções por partes e **Questão 2** (mesmo estacionamento, 3 h 20 min) | A **Questão 5** deste material usa a mesma tarifa e o mesmo raciocínio (só muda o horário e o teto): **não uso**. No lugar, entra uma questão nova de frete "por kg ou fração" (texto completo no Vídeo 1). O exemplo de 2 h 05 min da seção 03 aparece só como lembrança, com o foco no gráfico em escada. |
| Parte fixa + parte por unidade, taxa de variação | **Função Afim** (tarifas, plano de celular, inclinação) | Revisão relâmpago: cada faixa é um pedaço de reta, e a "taxa" de cada faixa é a inclinação daquele pedaço. |
| Desconto por faixa (cada parte com a sua taxa) | **Descontos, acréscimos, lucro e prejuízo**, seção 07 e **Questão 8** (desconto progressivo numa compra de R$ 600,00) | Tratado como "você já viu isso disfarçado de desconto; agora é imposto". A Questão 7 daqui tem outros números e contexto e acrescenta a **parcela a deduzir**, que é nova. |
| √(x²) = \|x\| | **Potenciação e radiciação** (índice par devolve o módulo) | Só citado no Vídeo 3. |
| Parábola y = x² − 4 (raízes, vértice) | **Função Quadrática** | Revisão relâmpago antes de rebater o gráfico. |
| Função composta e inversa | Próxima série | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Funções por partes: ache a faixa antes de calcular** | 03 | Q8, nova (frete por kg ou fração) | 8–10 min |
| **2. Faixas progressivas: cada parte paga a taxa da sua faixa** | 08 | Q1, Q7 | 8–10 min |
| **3. Módulo é distância: o gráfico em V e o rebatimento** | 02, 04, 05 | Q3, Q6 | 10–12 min |
| **4. Equações e inequações modulares e tolerância** | 06, 07 | Q4, Q2, Q9 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

A Questão 5 do material fica de fora por duplicar a Questão 2 de Conceito de Função.

---

## Cuidados ao revisar os roteiros

- **Deslocamento do V:** em y = |x − 3| o vértice vai para **x = 3 (direita)**; em |x + 2|, para −2. A IA às vezes "lê o sinal" e manda para o lado errado, justamente o erro que a aula combate.
- **Progressivo:** a conta de 26 m³ é **40 + 10 · 6 + 6 · 9 = 154**, e o imposto de R$ 7.000,00 é **300 + 400 = 700**. Se aparecer 136, 184 ou 1 400 como resposta certa, a IA aplicou a taxa errada a uma faixa.
- **"Hora ou fração"** sempre arredonda **para cima**: no frete, 3,3 kg excedentes viram 4 kg (R$ 49,00). Qualquer cálculo proporcional (R$ 44,80) está errado.
- **Contagem de soluções de |x² − 4| = k:** k = 3 dá **quatro** soluções, k = 4 dá **três** (±√8 e 0). A IA costuma dizer "duas" para qualquer k positivo.

## Erros encontrados no material

- **Questão 8, explicação da alternativa E:** o material diz que f(x) = 50 + 8(x − 10) "daria fatura de R$ 10,00 para quem não consome nada". Está errado: com x = 0, f(0) = 50 − 80 = **−30** (fatura negativa). R$ 10,00 é o valor para quem consome 5 GB. A explicação certa está no prompt do Vídeo 1.
- **Questão 6, explicação da alternativa B ("uma"):** o material diz que B "conta apenas uma raiz por caso, esquecendo o ±". Contar uma raiz em cada um dos dois casos daria **duas** soluções, não uma. Correção usada no Vídeo 3: B é de quem fica com a raiz positiva de um único caso (x = √7), esquecendo o ± e o segundo caso.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 2:** pronto sem voz · `ep2_faixas_progressivas` · 1366 pal. ~9,1 min · voz: parte 2 da cena 16 · capa A · Q7 B, Q1 B
- **Vídeo 1:** pronto sem voz · `ep1_faixas_andares` · 1453 pal. ~9,7 min · voz: parte 2 da cena 17 · capa A · Q8 C, nova C
- **Vídeo 3:** pronto sem voz · `ep3_modulo_distancia` · 1691 pal. ~11,3 min · voz: parte 2 da cena 19 · capa B · Q3 A, Q6 E · Q6 B corrigida (fica só com √7)
- **Vídeo 4:** pronto sem voz · `ep4_equacoes_tolerancia` · 1678 pal. ~11,2 min · voz: parte 2 da cena 18 · capa A · Q4 C, Q2 D, Q9 E
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1657 pal. ~11,0 min · voz: parte 2 da cena 21 · capa A · inéditas C, E, D, A, B
