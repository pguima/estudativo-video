# Determinantes e Sistemas Lineares — série de videoaulas

Material de apoio (cópia em `_material/34-determinantes-sistemas-lineares.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/34-determinantes-sistemas-lineares.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Montar e resolver sistemas (substituição, adição), SPD/SPI/SI como retas concorrentes, paralelas e coincidentes, 0 = 0 e 0 = 2, razões entre coeficientes | **Sistemas de equações lineares** (série 22) | Revisão relâmpago de 30 s no vídeo 4. O que é novo é decidir pelo **determinante** (D ≠ 0, D = 0 e D_x ≠ 0), discutir com parâmetro e o sistema homogêneo. |
| **Questão 1** (teatro, inteiras a R$ 40 e meias a R$ 20) | Quase igual à **Questão 1 de Sistemas** (mesmo contexto e mesmos preços, só mudam os totais) | **Não uso como questão.** Os números dela (250 ingressos, R$ 7 400) aparecem só como exemplo de Cramer, que é o da seção 07. No lugar, uma questão nova (camisetas e bonés), com o texto completo no prompt do vídeo 3. |
| **Questão 5** (posição de duas retas, mesmo enunciado e alternativas) | Quase igual à **Questão 6 de Sistemas** (x + 2y = 4 e 2x + 4y = 10, que a série 22 usa como "eu faço") | **Não uso.** A leitura geométrica fica como revisão no vídeo 4, com o foco no critério D = 0 (D_x ≠ 0 → SI), e uma das questões inéditas da revisão cobra o caso de infinitas soluções pelo D. |
| Combinado com o roteiro já escrito da série 22 | `22-sistemas-equacoes-lineares.md` usa a Q1 e a Q6 do material 22 sem determinante | Aqui o novo é só determinante, Cramer, discussão com parâmetro, sistema homogêneo e escalonamento 3 × 3 no caso D = 0; razões entre coeficientes e retas são revisão relâmpago. |
| Inversa 2 × 2 com ad − bc; a_ij = 2i − j | **Matrizes e operações**, vídeos 4 e 1 | Ponte: "o número da inversa ganha nome". A Questão 8 retoma a lei de formação. |
| Bhaskara (x² + x − 6 = 0) e k² = 4 com duas raízes | **Equação do 2º grau e Bhaskara** | Revisão relâmpago. |
| A seção 09 usa como exemplo o mesmo sistema da Questão 4; a seção 02 usa a mesma equação da Questão 2 | (dentro do material) | Nos blocos uso exemplos novos, para que as questões não fiquem "já resolvidas". |
| Área de triângulo por determinante | Geometria Analítica (série própria mais adiante) | Só citada. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é o determinante: 2 × 2, Sarrus, Laplace e o teste da inversa** | 02, 03, 05 | Q2 | 10–12 min |
| **2. Propriedades que poupam conta** | 04 | Q8, Q3 | 6–8 min |
| **3. O sistema como A · X = B e a regra de Cramer** | 06, 07 | Questão nova (camisetas e bonés), Q6 | 8–10 min |
| **4. Uma, infinitas ou nenhuma: classificar e discutir pelo determinante** | 08, 09 | Q4, Q7, Q9 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

Q1 e Q5 foram descartadas por duplicação com a série de Sistemas (ver tabela acima).

---

## Cuidados ao revisar os roteiros

- **Sinal do segundo produto:** em |3 −2; 4 5| a conta é 15 − (−8) = 23. A IA de vídeo costuma escrever "15 − 8 = 7" na tela mesmo narrando certo; confira cada determinante 2 × 2 escrito.
- **Sarrus:** o menos vale para a soma inteira das três diagonais vermelhas (13 − 64 = −51). Se aparecer 13 − 60 + 4 + 0, está errado.
- **Cramer:** D fica sempre no denominador, e as divisões de negativo por negativo dão positivo (−2 400 ÷ −20 = 120). Confira também que o roteiro do vídeo 3 não transforma a Questão 1 do material em questão (ela repete a série de Sistemas).
- **D = 0:** a IA tende a dizer "D = 0, logo impossível". No vídeo 4 e na questão inédita 4 da revisão, D = 0 leva a SPI.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_determinante_inversa` · 1548 pal. ~10,3 min · voz: parte 2 da cena 17 · capa A · Q2 D · pré-requisito trocado (x² − 5x + 6) para não entregar a Q2
- **Vídeo 2:** pronto sem voz · `ep2_propriedades` · 1029 pal. ~6,9 min · voz: parte 2 da cena 15 · capa A · Q8 C, Q3 D · blocos com det 7 (não entregar a Q3; o gancho do prompt já cita 5 → 40)
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1595 pal. ~10,6 min · voz: parte 2 da cena 21 · capa A · inéditas C, C, B, B, A
- **Vídeo 4:** pronto sem voz · `ep4_uma_infinitas_nenhuma` · 1752 pal. ~11,7 min · voz: parte 2 da cena 21 · capa A · Q4 A, Q7 E, Q9 B
- **Vídeo 3:** pronto sem voz · `ep3_cramer` · 1467 pal. ~9,8 min · voz: parte 2 da cena 17 · capa A · nova C, Q6 C
