# Conceito de Função, Domínio e Imagem — série de videoaulas

Material de apoio (cópia em `_material/23-conceito-funcao-dominio-imagem.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/23-conceito-funcao-dominio-imagem.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver equação e inequação do 1º grau, intervalos (]2, 5], colchete aberto no infinito), inverter o sinal ao dividir por negativo | **Equações e inequações do 1º grau** (série 20) | Revisão relâmpago: no "caminho de volta" (f(x) = k) e no domínio por fórmula (√(10 − 2x) exige inverter o sinal). Não reensino. |
| Plano cartesiano (eixos, par ordenado) | Série própria depois: **Plano cartesiano e distância entre pontos** (Geometria Analítica) | O material não cita o 56. No vídeo 4, apresento só o mínimo (eixo x horizontal, eixo y vertical, par (x, y)) em 30 s e prometo a série própria. |
| Funções definidas por partes ("hora ou fração") | Série própria depois: **Função modular e funções por partes** (29) | Aqui, só a ideia de "localizar a faixa" (vídeo 3). A Questão 5 do material 29 usa **a mesma tarifa** (R$ 10,00 + R$ 4,00 por hora ou fração) com outro tempo (4 h 20 min). Mantive a Q2 daqui porque esta série vem antes. A série 29 deve usar outra questão. |
| Táxi P(d) = 5 + 2,5d, gráfico que sobe e desce, h(t) = 20t − 5t² | Séries **Função afim** (24) e **Função quadrática** (25) | Uso esses exemplos só como "máquinas" e como leitura de gráfico. Coeficientes, vértice e raízes ficam para as séries próprias. |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A ideia de função: quando é e quando não é** | 02, 03 | Q6, Q1 | 8–10 min |
| **2. Domínio, contradomínio, imagem e a notação f(x)** | 04, 05 (até "f(a + b)") | Q4, Q7 | 10–12 min |
| **3. O caminho de volta e as funções por partes** | 05 ("O caminho de volta" e "Funções definidas por partes") | Q9, Q2 | 8–10 min |
| **4. O gráfico: teste da reta vertical e leitura de domínio e imagem** | 06, 07 | Q8 | 10–12 min |
| **5. Domínio pela fórmula e pelo contexto** | 08 | Q3, Q5 | 8–10 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Números negativos (vídeo 2):** f(−2) com f(x) = x² − 1 é (−2)² − 1 = **3**. A IA às vezes escreve −2² − 1 = −5. A mesma confusão estraga a Q4: g(−2) = (−2)² = 4, não −4.
- **Estacionamento (vídeo 3):** o exemplo da seção 05 (2 h 15 min) dá **R$ 18,00** e a Q2 (3 h 20 min) dá **R$ 22,00**. Com os dois números tão parecidos, a IA pode trocar um pelo outro ou contar só 2 horas adicionais na Q2.
- **Imagem × domínio no gráfico (vídeo 4):** no gráfico da seção 07 a imagem é [1, 4]. Na Q8 é **[0, 4]**: o ponto mais baixo é (5, 0), na ponta, e não (−2, 1). A IA tende a repetir o [1, 4] da seção.
- **Extremo que entra (vídeo 5):** na Q3, x = 2 **pertence** ao domínio (√0 = 0 não dá erro). A resposta é x ≥ 2 e x ≠ 5. Se a IA "arredondar" para x > 2, ela valida o distrator C.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_ideia_funcao` · 1435 pal. ~9,6 min · voz: parte 2 da cena 16 · capa B · Q6 A, Q1 C
- **Vídeo 3:** pronto sem voz · `ep3_volta_partes` · 1424 pal. ~9,5 min · voz: parte 2 da cena 14 · capa A · Q9 B, Q2 D · erros 2–4 com 1 h 30 min (não entregar a Q2)
- **Vídeo 2:** pronto sem voz · `ep2_dominio_imagem_notacao` · 1714 pal. ~11,4 min · voz: parte 2 da cena 17 · capa B · Q4 B, Q7 C · f(2x) trocado por f(3x) nos blocos (não entregar a Q7)
- **Vídeo 4:** pronto sem voz · `ep4_grafico_sombras` · 1556 pal. ~10,4 min · voz: parte 2 da cena 17 · capa C · Q8 E
- **Vídeo 5:** pronto sem voz · `ep5_dominio_formula_contexto` · 1452 pal. ~9,7 min · voz: parte 2 da cena 17 · capa A · Q3 D, Q5 B · bloco f trocado (folha 36×16) para não entregar a Q5
- **Vídeo 6:** pronto sem voz · `ep6_revisao` · 1736 pal. ~11,6 min · voz: parte 2 da cena 21 · capa A · inéditas B, E, C, D, A
