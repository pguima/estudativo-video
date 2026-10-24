# Progressão Aritmética (PA) — série de videoaulas

Material de apoio (cópia em `_material/31-progressao-aritmetica.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/31-progressao-aritmetica.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Montantes de juros simples formam PA de razão C · i (R$ 1.000,00 a 3%: 1.030, 1.060, 1.090…) | **Juros Simples**, seção 07 e **Questão 7** (identificar o tipo de sequência) | "Você já viu isso disfarçado": no Vídeo 4, revisão relâmpago com o exemplo de lá. A Questão 7 daqui é outra (achar o mês em que o montante chega a R$ 3.080,00), então uso, com foco no "termo zero". |
| PA = função afim nos naturais, razão = coeficiente angular | **Função Afim**, seções 03 e 10 | Revisão relâmpago no Vídeo 1; o gráfico de pontos alinhados é o elo. |
| Juros do SAC caem em PA; total de juros = soma de PA ((400 + 80) · 5 ÷ 2 = 1.200) | **Empréstimos, financiamentos e parcelamentos**, seção 06 | Citado no Vídeo 3 (soma) e no Vídeo 4 (PA disfarçada), com o exemplo de lá. Nenhuma questão de SAC é repetida. |
| PA × PG (diferença constante × quociente constante) | **Progressão Geométrica** (próxima série) e **Função Exponencial** | Só o aviso "(2, 4, 8, 16) não é PA; é assunto do próximo material". |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é PA, a razão e o "n − 1"** | 02, 03, 04 | Q2, Q1 | 10–12 min |
| **2. Contar termos e saltos: meios, postes, múltiplos e três termos** | 05 (média dos vizinhos, notação simétrica), 07 | Q4, Q5, Q6 | 10–12 min |
| **3. A soma de Gauss** | 06, 05 (termos equidistantes) | Q3, Q8, Q9 | 10–12 min |
| **4. A PA disfarçada: juros simples, calendário, SAC** | 08 | Q7 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **O "n − 1":** o 12º termo de (50, 65, 80, …) é 50 + **11** · 15 = 215. Confira cada termo geral do roteiro: a IA escorrega para 12 · 15 (230), que é justamente o distrator.
- **Questão 7 (juros simples):** a resposta é **18**, porque R$ 2.000,00 é o valor no instante zero (montante do mês n = 2 000 + 60n). Se a IA usar a₁ = 2 000 e a fórmula com n − 1, chega a 19 e "confirma" o distrator C.
- **Interpolação:** 5 meios entre 3 e 27 são **7 termos e 6 saltos** (r = 4). A IA às vezes divide por 5.
- **Soma:** toda soma usa ÷ 2 (S = 44 · 25 = 1 100 no teatro; 9,5 · 6 = 57 no treino). Desconfie de 2 200 ou 114.

## Erros encontrados no material

- **Questão 1, explicação da alternativa A (101):** o material diz que "A usa razão 2". Pelo termo geral, razão 2 daria 4 + 49 · 2 = **102**, não 101. O valor 101 vem da forma simplificada com 2 no lugar de 3: 2 · 50 + 1 (quem acha que cada quadrado novo acrescenta 2 palitos). Explicação corrigida no prompt do Vídeo 1.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 4:** pronto sem voz · `ep4_pa_disfarcada` · 1062 pal. ~7,1 min · voz: parte 2 da cena 12 · capa A · Q7 B
- **Vídeo 3:** pronto sem voz · `ep3_soma_gauss` · 1591 pal. ~10,6 min · voz: parte 2 da cena 16 · capa A · Q3 A, Q8 B, Q9 D · bloco f trocado para não entregar a Q9
- **Vídeo 2:** pronto sem voz · `ep2_contar_termos_saltos` · 1716 pal. ~11,4 min · voz: parte 2 da cena 21 · capa A · Q4 C, Q5 C, Q6 B · bloco f trocado (soma 45) para não entregar a Q6
- **Vídeo 1:** pronto sem voz · `ep1_razao_termo_geral` · 1649 pal. ~11,0 min · voz: parte 2 da cena 16 · capa A · Q2 C, Q1 D · Q1 A corrigida (101 = 2·50 + 1)
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1639 pal. ~10,9 min · voz: parte 2 da cena 21 · capa A · inéditas C, A, E, B, D
