# Função Composta e Função Inversa — série de videoaulas

Material de apoio (cópia em `_material/30-funcao-composta-inversa.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/30-funcao-composta-inversa.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| "Caminho de volta" f(x) = k (táxi P = 5 + 2,5d, pagou R$ 30,00) | **Conceito de Função**, seção "o caminho de volta" e **Questão 9** | A Questão 3 daqui (táxi 4,5 + 2,5x) pede a **fórmula** da volta, não um número: uso, apresentada como "lá você voltou com um número; agora você monta a volta inteira". |
| Substituir uma expressão em f (f(2x) com f(x) = x² − 1) | **Conceito de Função**, Questão 7 | Revisão relâmpago antes de montar f(g(x)). |
| Lei afim, F = 1,8C + 32, táxi, taxa de variação | **Função Afim** | Revisão relâmpago; a inversa da afim é "desfazer na ordem contrária". |
| Descontos encadeados ("a ordem não importa") | **Descontos, acréscimos, lucro e prejuízo**, seção 02 | A Questão 6 (cupom × 10%) é o contraponto: dois percentuais comutam, mas cupom em reais + percentual **não**. Digo explicitamente que as duas aulas não se contradizem. |
| Exponencial e logaritmo como par inverso, espelho em y = x | **Função Logarítmica**, seção 02 | Só revisão: o par aparece como exemplo do espelho, sem reensinar logaritmo. |
| Progressão aritmética | Próxima série | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Composição: máquinas em fila e a ordem que importa** | 02, 03 | Q2, Q6 | 10–12 min |
| **2. Composição em contexto e a função escondida** | 04, 05 | Q1, Q4 | 8–10 min |
| **3. Função inversa: desfazer o caminho** | 06 (definição e f⁻¹ ≠ 1/f), 07 (receita), 08 (conversões) | Q3, Q8 | 10–12 min |
| **4. Quem tem inversa e o espelho na reta y = x** | 06 (bijetora, restringir domínio), 07 (gráfico), 08 (exp–log), 09 (tabelas) | Q7, Q5, Q9 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Ordem da composição:** em f(g(2)) com f(x) = x² − 1 e g(x) = 2x + 3, o certo é g(2) = 7 e f(7) = **48**. Se a IA chegar a 9, inverteu a ordem; se chegar a 24, desenvolveu (2x + 3)² sem o termo do meio.
- **Questão 6 (cupom × 10%):** a diferença entre as ordens é **R$ 2,00** (117 − 115). A IA tende a dizer que "a ordem não importa", porque a série de Descontos ensina isso para dois percentuais; confira se o roteiro faz a distinção (percentual com percentual comuta; reais com percentual, não).
- **Inversa da afim:** desfazer 2x + 1 é **subtrair 1 e depois dividir por 2**, (x − 1)/2. Atenção a "x/2 − 1" (ordem errada) e "(x + 1)/2" (sinal errado).
- **Gráfico da inversa:** reflexão na reta **y = x**; (3, 7) vira (7, 3). A IA às vezes descreve "espelho no eixo y".

## Erros encontrados no material

- **Seção 06, quadro "f⁻¹ não é 1/f":** o material diz que, para f(x) = 2x, a inversa x/2 e 1/(2x) "por coincidência, nesse caso parecem próximas". Não parecem: com x = 4, x/2 = 2 e 1/(2x) = 0,125; uma é reta, a outra é hipérbole. Imprecisão pequena, mas que reforça justamente a confusão que o quadro quer evitar. No Vídeo 3 o roteiro mostra que são funções diferentes, sem a frase.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_maquinas_em_fila` · 1708 pal. ~11,4 min · voz: parte 2 da cena 17 · capa A · Q2 E, Q6 D
- **Vídeo 3:** pronto sem voz · `ep3_inversa_desfazer` · 1718 pal. ~11,5 min · voz: parte 2 da cena 19 · capa A · Q3 A, Q8 A · bloco f trocado para não entregar a Q8
- **Vídeo 2:** pronto sem voz · `ep2_ponte_escondida` · 1449 pal. ~9,7 min · voz: parte 2 da cena 17 · capa A · Q1 C, Q4 E · caso 1 trocado (2x + 5) para não entregar a Q4
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1758 pal. ~11,7 min · voz: parte 2 da cena 21 · capa A · inéditas E, B, D, C, A
- **Vídeo 4:** pronto sem voz · `ep4_bijetora_espelho` · 1716 pal. ~11,4 min · voz: parte 2 da cena 19 · capa B · Q7 D, Q5 B, Q9 B
