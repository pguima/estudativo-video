# Função Logarítmica e aplicações (pH, Richter, decibéis) — série de videoaulas

Material de apoio (cópia em `_material/28-funcao-logaritmica-aplicacoes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/28-funcao-logaritmica-aplicacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Definição de log, propriedades, log 2 e log 3 | **Logaritmos** | Revisão relâmpago. O log do produto é usado no pH (vídeo 2) e o log do quociente na magnitude (vídeo 3). Não reensino. |
| Gráfico da exponencial, assíntota, inequação com base entre 0 e 1 | **Função exponencial, vídeos 1 e 5** | O vídeo 1 desenha o log como espelho da exponencial e reaproveita a regra "base menor que 1 inverte". |
| "Quantas vezes maior" é divisão; diferença de ordens de grandeza é fator 10 | **Notação científica e ordem de grandeza** | Revisão de 30 s no vídeo 2. É a base da regra "diferença de leitura = expoente da razão". |
| Domínio de uma fórmula | **Conceito de função** | Revisão de 30 s no vídeo 1. |
| Função inversa, simetria na reta y = x | **Função composta e inversa** (série futura) | Só cito: "inversa tem série própria". |
| Meia-vida, tempo para dobrar | **Função exponencial** (contando intervalos) e **Logaritmos** (com log, Q1 e Q8) | **Este material não trata disso**, então não entra aqui. Não há questão repetida entre as três séries. |
| pH, decibéis, Richter em Química, Física e Geografia | Sem série própria no canal até agora | Uso **só as fórmulas e os números do material**: pH = −log[H⁺], log E = 4,8 + 1,5M, M_w = (2/3) · log M₀ − 10,7, β = 10 · log(I/I₀), I₀ = 10⁻¹² W/m². |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A função logarítmica: o espelho da exponencial (gráfico, domínio e sinal)** | 02, 03, 04 | Q7 | 10–12 min |
| **2. Escalas logarítmicas e o pH** | 05, 06 | Q1, Q2, Q6 | 10–12 min |
| **3. Terremotos: amplitude, energia e magnitude de momento** | 07 | Q3, Q8 | 8–10 min |
| **4. Decibéis: por que 80 + 80 não dá 160** | 08 | Q5, Q4, Q9 | 8–10 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Decibéis (vídeo 4 e inédita 5):** a diferença em dB é **dividida por 10** antes de virar expoente (40 dB a mais → 10⁴, não 10⁴⁰). Duas fontes iguais somam cerca de **3 dB** (80 → 83), não 80 nem 10. Na Q9, a resposta é **10** máquinas no total, não 11.
- **Amplitude × energia (vídeo 3 e inédita 4):** por grau, amplitude ×10 e energia ×10^1,5 ≈ 32. De 5 para 7: amplitude ×100, energia ×1 000. A IA costuma usar ×10 por grau também para a energia.
- **Sentido do pH (vídeo 2, Q6 e inédita 3):** menor pH é **mais** H⁺. Na piscina, a maior concentração é 10 elevado a **−7,2**. Em 4 · 10⁻⁶, o pH é 6 − 0,60 = **5,4** (entre 5 e 6), não 6,6.
- **Ordem das operações em M_w (vídeo 3, Q8):** (2/3) · 27 = 18 e **depois** − 10,7 = 7,3. A IA às vezes subtrai primeiro (10,9). E não deve inventar fórmulas de Química, Física ou sismologia além das do material (por exemplo, cálculos com pOH ou com energia em decibéis).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_espelho_grafico` · 1656 pal. ~11,0 min · voz: parte 2 da cena 16 · capa A · Q7 C
- **Vídeo 3:** pronto sem voz · `ep3_terremotos` · 1371 pal. ~9,1 min · voz: parte 2 da cena 15 · capa A · Q3 C, Q8 A · CORRIGIDO: frase-chave 2 do prompt e hábito 1 do material ('divida pelo coeficiente') erram na energia: é 10^(1,5·ΔM)
- **Vídeo 2:** pronto sem voz · `ep2_escalas_ph` · 1693 pal. ~11,3 min · voz: parte 2 da cena 19 · capa A · Q1 D, Q2 B, Q6 B
- **Vídeo 4:** pronto sem voz · `ep4_decibeis` · 1343 pal. ~9,0 min · voz: parte 2 da cena 18 · capa A · Q5 C, Q4 D, Q9 D
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1725 pal. ~11,5 min · voz: parte 2 da cena 21 · capa A · inéditas E, D, A, D, C · hábito 1 corrigido (energia multiplica por 1,5)
