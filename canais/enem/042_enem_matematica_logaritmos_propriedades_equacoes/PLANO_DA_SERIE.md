# Logaritmos: definição, propriedades e equações — série de videoaulas

Material de apoio (cópia em `_material/27-logaritmos-propriedades-equacoes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/27-logaritmos-propriedades-equacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Potências, expoente negativo, propriedades aᵐ · aⁿ = aᵐ⁺ⁿ | **Potenciação e radiciação** | Revisão relâmpago nos vídeos 1 e 2: as propriedades do log são "as de potência lidas de trás para frente". |
| Potências de 10, 10⁻ⁿ com n casas decimais, "cada ordem é ×10" | **Notação científica e ordem de grandeza** | Revisão relâmpago no vídeo 1 (log decimal "conta zeros" e conta algarismos). |
| Equações exponenciais de mesma base; 2ˣ = 10 "não fecha" | **Função exponencial, vídeo 5** | O vídeo 1 abre exatamente nessa pergunta deixada em aberto. |
| t = log(M/C) ÷ log(1 + i) e regra do 72 | **Juros Compostos** | Lá a fórmula veio pronta; no vídeo 3 mostro de onde ela vem. A regra do 72 entra só como conferência da Q1 (72 ÷ 8 = 9). Nenhuma questão de Juros Compostos é reutilizada (a Q1 daqui, a 8% para dobrar, é diferente das de lá). |
| Equação do 2º grau | **Equação do 2º grau (Bhaskara)** | Revisão de 30 s no vídeo 4. |
| pH, Richter, decibéis | **Função logarítmica e aplicações** (próxima série) | Só prometo. Nenhuma questão de escala aqui. |
| Meia-vida e tempo de dobrar com log | Função logarítmica não trata disso | Fica **aqui** (Q1 e Q8, vídeo 3). A série de Função exponencial resolve meia-vida só contando intervalos; aqui entra o caso que não fecha. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Logaritmo é um expoente: definição, condições e consequências** | 02, 03 | Q4 | 8–10 min |
| **2. As três propriedades e o kit log 2 e log 3** | 04, 06 | Q2, Q9, Q7 | 10–12 min |
| **3. Tirando a incógnita do expoente: equações com log e mudança de base** | 05, 07 | Q5, Q6, Q1, Q8 | 10–12 min |
| **4. Equações logarítmicas e a condição de existência** | 08 | Q3 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Sinal em decaimento (vídeo 3, Q8, e inédita 3):** log 0,9 = 0,954 − 1 = **−0,046** e log 0,8 = **−0,10**. A IA costuma escrever log 0,9 ≈ 0,954 (esquece o −1) ou apresentar o tempo como negativo. Os dois logs da divisão são negativos e o tempo sai positivo (cerca de 6,5 anos; 3 meses).
- **Mudança de base:** log_2 10 = log 10 ÷ log 2 = 1 ÷ 0,301 ≈ **3,32**, não 0,301. Confira em toda fração de logs se o logaritmando está no numerador (log_4 32 = 2,5, não 0,4).
- **Distrator B da Q8:** a explicação do material ("usa log 9 = 0,954 no lugar de log 0,9") só leva a 0,32 se o sinal do −0,301 for ignorado (0,301 ÷ 0,954 ≈ 0,32). Deixei isso explícito no roteiro; a IA não deve escrever "−0,32 ano" como alternativa.
- **Contar algarismos (vídeo 1 e inédita 5):** 2¹⁰⁰ tem **31** algarismos (log = 30,1) e 3⁵⁰ tem **24** (log = 23,85). A IA às vezes responde a parte inteira (30, 23).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_log_expoente` · 1420 pal. ~9,5 min · voz: parte 2 da cena 16 · capa A · Q4 B · bloco g e erro 2 trocados para não entregar a Q4
- **Vídeo 2:** pronto sem voz · `ep2_propriedades_kit` · 1680 pal. ~11,2 min · voz: parte 2 da cena 21 · capa A · Q2 E, Q9 A, Q7 B
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1756 pal. ~11,7 min · voz: parte 2 da cena 21 · capa A · inéditas D, C, D, A, B
- **Vídeo 4:** pronto sem voz · `ep4_equacoes_condicao` · 1150 pal. ~7,7 min · voz: parte 2 da cena 12 · capa A · Q3 B
- **Vídeo 3:** pronto sem voz · `ep3_equacoes_mudanca_base` · 1760 pal. ~11,7 min · voz: parte 2 da cena 19 · capa A · Q5 C, Q6 C, Q1 C, Q8 D · decaimento e erro 3 com exemplos nossos (não entregar a Q8)
