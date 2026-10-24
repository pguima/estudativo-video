# Matrizes e Operações — série de videoaulas

Material de apoio (cópia em `_material/33-matrizes-operacoes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/33-matrizes-operacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver duas equações ao mesmo tempo (igualdade de matrizes: x + y = 7 e x − y = 1) | **Sistemas de equações lineares** (método da adição) | Revisão relâmpago no vídeo 2; não reensino o método. |
| O número ad − bc da inversa 2 × 2 e a forma A · X = B | **Determinantes e sistemas lineares** (próxima série) | Uso a fórmula da inversa e só prometo: "esse número ganha nome na próxima série". |
| Lei de formação a_ij = 2i − j | Volta na **Questão 8 de Determinantes** (versão 3 × 3) | Aqui fica só a montagem da 2 × 3; o determinante dela é assunto da próxima série. |
| Distância entre cidades, leitura de tabelas | Geografia (redes de transporte) e, mais adiante, leitura de tabelas | Só citado na revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Matriz é uma tabela com endereço** | 02, 03, 08 (tabelas e imagens) | Q1, Q5 | 10–12 min |
| **2. Operações casa a casa: igualdade, soma e número × matriz** | 04 | Q8 | 6–8 min |
| **3. Multiplicação de matrizes: linha por coluna** | 05, 08 (A² e rotas) | Q3, Q2, Q7 | 10–12 min |
| **4. O que muda em relação aos números e a matriz inversa** | 06, 07 | Q4, Q9, Q6 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

O material declara incidência Alta, mas na prática o ENEM cobra matriz quase só como leitura de tabela e produto em contexto. Por isso os vídeos 1 e 3 são os que mais importam; o vídeo 2 é curto.

---

## Cuidados ao revisar os roteiros

- **Multiplicação casa a casa:** a IA às vezes "multiplica" matrizes posição com posição (como na soma). Confira no vídeo 3 que (1 2 3 / 0 1 4) · (2 4 / 1 0 / 0 5) dá (4 19 / 1 20), e que no vídeo 2 só a soma e o número vezes matriz são feitos casa a casa.
- **Questão 7 (rotas):** a resposta é 2 (rotas 1 → 2 → 4 e 1 → 3 → 4). O valor 1 é o número de rotas com **duas** escalas, não "uma das escalas"; e 4 é a soma da linha 1 de A², não o elemento (A²)₁₄.
- **Questão 2:** a resposta é 235 (cada filial no seu fornecedor mais barato: 127 + 108). A IA tende a escolher 215 (o item mais barato de cada fornecedor), que o enunciado proíbe.
- **Inversa:** troca a **diagonal principal**, muda o sinal da **secundária**. Em (3 1 / 5 2) a inversa é (2 −1 / −5 3); se aparecer (−2 1 / 5 −3) ou (2 1 / 5 3), está errado.
- A seção 02 do material cita "no cabeçalho, a₂₃ = 9 e a₃₂ = 3", que vem de uma imagem que a IA de vídeo talvez não veja; por isso o vídeo 1 usa o exemplo próprio a_ij = i + 2j.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 2:** pronto sem voz · `ep2_casa_a_casa` · 1122 pal. ~7,5 min · voz: parte 2 da cena 14 · capa A · Q8 D
- **Vídeo 1:** pronto sem voz · `ep1_tabela_endereco` · 1740 pal. ~11,6 min · voz: parte 2 da cena 18 · capa B · Q1 A, Q5 C
- **Vídeo 4:** pronto sem voz · `ep4_ordem_inversa` · 1751 pal. ~11,7 min · voz: parte 2 da cena 18 · capa A · Q4 B, Q9 A, Q6 D
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1721 pal. ~11,5 min · voz: parte 2 da cena 21 · capa A · inéditas C, B, D, C, B
- **Vídeo 3:** pronto sem voz · `ep3_linha_por_coluna` · 1690 pal. ~11,3 min · voz: parte 2 da cena 18 · capa A · Q3 E, Q2 B, Q7 C
