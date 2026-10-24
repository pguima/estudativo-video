# Equações e Inequações do 1º Grau — série de videoaulas

Material de apoio (cópia em `_material/20-equacoes-inequacoes-1o-grau.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/20-equacoes-inequacoes-1o-grau.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Tradução de frases, distributiva, menos antes do parêntese | **Expressões Algébricas, vídeo 1** | Revisão relâmpago, reaproveitando o "espelho" do sinal de menos. |
| Somar frações pelo MMC; fração "do total" × "do restante" | **Frações** (série 03; a Q7 de lá é "do restante") | Revisão relâmpago. Na Q3 daqui as duas frações são **do salário**, e a alternativa D é justamente o caso "do restante": uso o contraste em vez de repetir a questão. |
| Gráfico das duas retas, plano de celular, ponto de equilíbrio com receita e custo | **Função afim** (série 24) | Só citar. Aqui o ponto de equilíbrio sai da equação e da inequação, sem gráfico. |
| M = C(1 + it), v = v₀ + at, F = 1,8C + 32 | **Juros Simples** (série 13) e Física | Só no vídeo de revisão, como "isolar a incógnita". |
| Planos com a mesma tarifa por unidade (Q6, 0x = −4) | **Sistemas Lineares, vídeo 3** retoma como retas paralelas | Aqui fica só a álgebra (0x = número). |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A equação como balança e o roteiro de resolução** | 02, 03, 04 | Q6 | 10–12 min |
| **2. Montar a equação a partir do texto** | 05 | Q5, Q3, Q9 | 10–12 min |
| **3. Inequações: a regra do sinal, intervalos e resposta inteira** | 06, 07 | Q4, Q8, Q7 | 10–12 min |
| **4. Comparar planos: o ponto de equilíbrio** | 08 | Q1, Q2 | 8–10 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Sinal na inequação:** −2x + 7 > 1 dá **x < 3**; na Questão 4, −8t ≤ −160 dá **t ≥ 20** ("no mínimo 20 minutos"). A IA de vídeo às vezes inverte o sinal na conta e esquece de inverter na frase final (ou o contrário). Confira a frase narrada.
- **Empate × "mais barato":** na Questão 2, o empate é 800 cartazes (R$ 400,00 nas duas), e a resposta é **801**. Confira se a IA não arredonda para 800.
- **Notação de intervalo:** o material usa a notação brasileira ]10, 20], com o colchete virado para fora. Se a IA trocar por (10, 20], o aluno vê duas notações no canal. Peça para manter a do material.
- **Questão 3:** o certo é 1/3 + 1/4 = **7/12** do salário (sobram 5/12 → R$ 3.000,00). Cuidado se a narração calcular a alimentação "sobre o que sobrou": esse é o distrator D (R$ 2.500,00).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_balanca_roteiro` · 1592 pal. ~10,6 min · voz: parte 2 da cena 15 · capa B · Q6 D
- **Vídeo 2:** pronto sem voz · `ep2_texto_equacao` · 1751 pal. ~11,7 min · voz: parte 2 da cena 16 · capa A · Q5 A, Q3 E, Q9 B
- **Vídeo 4:** pronto sem voz · `ep4_ponto_equilibrio` · 1414 pal. ~9,4 min · voz: parte 2 da cena 15 · capa A · Q1 D, Q2 E · erros com as locadoras (não entregar 801)
- **Vídeo 3:** pronto sem voz · `ep3_inequacoes_intervalos` · 1778 pal. ~11,9 min · voz: parte 2 da cena 20 · capa A · Q4 C, Q8 C, Q7 B
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1675 pal. ~11,2 min · voz: parte 2 da cena 20 · capa A · inéditas B, D, C, B, A
