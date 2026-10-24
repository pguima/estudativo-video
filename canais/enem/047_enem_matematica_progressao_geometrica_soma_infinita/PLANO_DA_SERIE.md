# Progressão Geométrica (PG) e Soma dos Infinitos Termos — série de videoaulas

Material de apoio (cópia em `_material/32-progressao-geometrica-soma-infinita.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/32-progressao-geometrica-soma-infinita.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| **Questão 1** (500 bactérias que dobram a cada 20 min, 2 h → 32 000) | Idêntica à **Questão 1 de Função Exponencial** | **Não uso.** O exemplo da seção 03 (os mesmos números) entra só como "você já viu isso na série de Função Exponencial", para mostrar a contagem a partir do instante zero. No lugar, uma questão nova de termo geral por dois termos (Vídeo 1). |
| **Questão 2** (80 g, meia-vida de 5 anos, 20 anos → 5 g) | Quase igual à **Questão 2 de Função Exponencial** (80 mg, meia-vida de 8 dias, 32 dias → 5 mg: mesmas 4 meias-vidas, mesmo resultado) | **Não uso.** Meia-vida vira revisão relâmpago no Vídeo 4, e entra uma questão nova de depreciação percentual. |
| Questão 9 (tabela 1 000, 1 200, 1 440, 1 728 → 1 000 · 1,2ⁿ) | Mesma estrutura da Questão 3 de Função Exponencial (tabela de valores com fator 0,8) | Uso (números, sentido e contexto diferentes), apresentada como "agora com o olhar de PG". |
| Montantes de juros compostos formam PG de razão 1 + i; dobra a cada 7 anos → ×2³ | **Juros Compostos**, seções 04 e 08 | "Você já viu isso disfarçado": revisão relâmpago no Vídeo 4. |
| Porcentagem vira fator (1 + i, 1 − i) | **Porcentagem** e **Função Exponencial** | Revisão relâmpago no Vídeo 1. |
| Dízima periódica e fração geratriz (regra prática dos noves) | **Frações, decimais e dízimas** (seção 09) | Só a justificativa nova: a dízima é uma soma infinita de PG. A regra prática não é reensinada. |
| PA (termo geral, n − 1, termos equidistantes) | **Progressão Aritmética** | Revisão relâmpago e comparação lado a lado. |
| Matrizes e operações | Próxima série | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é PG, a razão como fator e o termo geral** | 02, 03, 04 | Q7, nova (algas), Q9 | 10–12 min |
| **2. Propriedades e soma finita** | 05, 06 | Q4, Q5 | 10–12 min |
| **3. Soma infinita: infinitas parcelas, um número finito** | 07, 08 (a bola) | Q8, Q6, Q3 | 10–12 min |
| **4. A PG disfarçada: juros compostos, meia-vida, depreciação** | 08 (tabela), 09 (estratégia 1) | nova (depreciação) | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

As Questões 1 e 2 do material ficam de fora por duplicarem questões de Função Exponencial.

---

## Cuidados ao revisar os roteiros

- **n − 1 × instante zero:** "500 bactérias que dobram a cada 20 min, em 2 h" são **6** duplicações (500 · 2⁶), porque se conta a partir do instante zero. A IA às vezes aplica o "n − 1" da PA e usa 2⁵. A regra: o expoente é o número de vezes que o fator age.
- **Soma infinita só com |q| < 1:** confira que a IA não aplica a₁/(1 − q) a uma PG de razão maior que 1, e que o denominador é (1 − q), não q (12 ÷ 1/4 = 48 é o distrator da Questão 8).
- **Bola:** total = 8 + 2 · 24 = **56 m**. Erros típicos da IA: 64 (dobrar também a primeira queda) ou 32 (só descidas).
- **Questão 5:** com a notação x/q, x, x·q, a equação é 6q² − 13q + 6 = 0 (raízes 3/2 e 2/3). A IA às vezes escreve 6q + 6 + 6q = 19, que perde o termo 6/q.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 2:** pronto sem voz · `ep2_propriedades_soma` · 1726 pal. ~11,5 min · voz: parte 2 da cena 15 · capa A · Q4 C, Q5 C · bloco b trocado (produto 64) para não entregar a Q5
- **Vídeo 1:** pronto sem voz · `ep1_maquina_multiplicar` · 1737 pal. ~11,6 min · voz: parte 2 da cena 16 · capa A · Q7 D, algas D, Q9 E · bloco f e teste da tabela trocados
- **Vídeo 3:** pronto sem voz · `ep3_soma_infinita` · 1706 pal. ~11,4 min · voz: parte 2 da cena 17 · capa A · Q8 C, Q6 B, Q3 D · bola do bloco f trocada (9 m, 2/3) para não entregar a Q3
- **Vídeo 4:** pronto sem voz · `ep4_pg_disfarcada` · 1083 pal. ~7,2 min · voz: parte 2 da cena 14 · capa A · nova C (R$ 40.960)
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1721 pal. ~11,5 min · voz: parte 2 da cena 21 · capa A · inéditas B, D, A, E, C · Q3 com bola de 10 m (a de 9 m já estava no ep3)
