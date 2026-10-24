# Números Complexos — série de videoaulas

Material de apoio (cópia em `_material/36-numeros-complexos.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/36-numeros-complexos.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Δ < 0 = "nenhuma raiz real" (x² + 2x + 5 = 0, Δ = −16), soma −b/a e produto c/a | **Equação do 2º grau e Bhaskara** | O gancho do vídeo 1 retoma a frase "nenhuma raiz **real**" e resolve x² + 2x + 5 = 0 nos complexos. Soma e produto servem de conferência. |
| Propriedades de potência, sinal de base negativa, "√−4 não existe nos reais" | **Potenciação e radiciação** | Revisão relâmpago. O ciclo de quatro potências de i é **novo** (o material de Potenciação não traz ciclos). |
| Distributiva, (a + b)² | **Expressões algébricas e produtos notáveis** | Revisão. Atenção: lá, (1 + i)² aparece com i = taxa de juros; aqui i é a unidade imaginária (ver Cuidados). |
| Raízes conjugadas, x² − 2x + 2, Q6 de Polinômios | **Polinômios**, vídeo 4 | Revisão de 1 frase: "a regra do par de meias agora tem explicação". |
| Sistema 2 × 2 em a e b (equações com z e z̄) | **Sistemas de equações lineares** | Revisão relâmpago. |
| Pitágoras, distância entre pontos, seno e cosseno de 30°, 45° e 60°, ciclo trigonométrico | Séries próprias no bloco de Geometria e de Trigonometria (ainda não publicadas) | Dou só o que é preciso em uma frase ou uma tabela na tela e prometo: "isso tem série própria". |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A unidade imaginária: i² = −1, Δ negativo e as potências de i** | 02, 03 | Q8, Q1 | 10–12 min |
| **2. As operações: produto, conjugado, divisão e igualdade** | 04, 05 | Q2, Q3, Q9 | 10–12 min |
| **3. O plano de Argand-Gauss: módulo, distância e o giro de 90°** | 06, 08 ("giros prontos") | Q4, Q5 | 6–8 min |
| **4. Forma trigonométrica e De Moivre: multiplicar é girar** | 07, 08, 09 | Q6, Q7 | 8–10 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

O próprio material admite que complexos "quase não aparecem de forma direta no ENEM"; por isso os vídeos 3 e 4 são curtos e a revisão dá peso ao que se reaproveita (Δ < 0, potências de i, geometria no plano).

Vários exemplos das seções do material são as mesmas contas das questões (x² − 4x + 13, (2 + 3i)(1 − i), (3 + i)/(1 − i), 1 + 2i → 4 + 6i, i(3 + 2i), 1 + √3 i, (1 + i)⁸). Nos blocos uso exemplos novos, para que as questões não cheguem "já resolvidas".

---

## Cuidados ao revisar os roteiros

- **i² = −1 em toda conta:** é o erro que gera quase todos os distratores. Confira na tela do vídeo 2 que (2 + 3i)(1 − i) = 5 + i (o −3i² vira +3) e, no vídeo 5, que (1 − i)⁴ = −4.
- **Colisão de notação com a série de Expressões algébricas:** lá, (1 + i)² = 1 + 2i + i² aparece com i = taxa de juros. Se a IA de vídeo "lembrar" esse exemplo aqui, ela precisa dizer que agora i é a unidade imaginária e que i² = −1 (lá, i² era só um número positivo pequeno).
- **Quadrante do argumento:** −1 + i tem argumento 135°, 1 − i tem 315° e 1 + √3 i tem 60°. A IA costuma devolver o ângulo de referência (45°) sem olhar os sinais.
- **Questão 4:** a resposta é 5 metros (módulo da diferença 3 + 4i). As alternativas A e D são √5 e √52; no texto extraído do material o símbolo de raiz pode sumir e virar "5" e "52". Confira que a IA não leia a alternativa A como "5".

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_unidade_imaginaria` · 1532 pal. ~10,2 min · voz: parte 2 da cena 16 · capa A · Q8 A, Q1 C · bloco e com i²⁰²⁵ (não entregar a Q1)
- **Vídeo 2:** pronto sem voz · `ep2_operacoes` · 1717 pal. ~11,4 min · voz: parte 2 da cena 20 · capa A · Q2 A, Q3 E, Q9 E
- **Vídeo 3:** pronto sem voz · `ep3_plano_argand` · 1136 pal. ~7,6 min · voz: parte 2 da cena 15 · capa A · Q4 B, Q5 D
- **Vídeo 4:** pronto sem voz · `ep4_de_moivre` · 1418 pal. ~9,5 min · voz: parte 2 da cena 16 · capa A · Q6 B, Q7 C
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1679 pal. ~11,2 min · voz: parte 2 da cena 21 · capa A · inéditas B, C, A, D, B · Q2 B do prompt corrigida (dividiu só pelo 1)
