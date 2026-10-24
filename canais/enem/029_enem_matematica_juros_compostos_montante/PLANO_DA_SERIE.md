# Juros Compostos e Montante — série de videoaulas

Material de apoio (cópia em `_material/14-juros-compostos-montante.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/14-juros-compostos-montante.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator (1 + i), variações sucessivas (multiplicar fatores), "três aumentos de 10% = 1,1³ = 1,331", voltar ao valor original dividindo pelo fator | **Porcentagem** | Revisão relâmpago. A **Questão 5** (+10%, +20%, −25%) começa igual à Q3 de Porcentagem (1,10 · 1,20 = 1,32): uso, mas digo "o 1,32 você já conhece" e o foco fica no ×0,75 e no resultado negativo. |
| Capital, taxa, montante, J = M − C; juros simples como reta e PA | **Juros simples** (série anterior) | Revisão relâmpago. A comparação reta × curva é o conteúdo novo do vídeo 2. |
| Potências (1,1² = 1,21; propriedades da potência) | **Potenciação e radiciação** | Só revisão das propriedades (aᵐ⁺ⁿ = aᵐ · aⁿ; a²ⁿ = (aⁿ)²), aplicadas a fatores. |
| Converter taxa anual em mensal em compostos; 1,02¹² ≈ 26,8% | **Taxas equivalentes e inflação** (série própria) | Só o aviso "dividir por 12 não funciona aqui; isso tem série própria". Não calculo taxa equivalente nem mostro 1,02¹². |
| t = log(M/C) ÷ log(1 + i) | **Logaritmos** (série própria) | Uso a fórmula como ferramenta pronta, com os logs dados no enunciado. As propriedades ficam para a série própria. |
| Montante como PG e como exponencial; duplicação; decaimento (0,8ᵗ) | **Função exponencial** e **Progressão geométrica** (séries próprias) | Só reconhecer "multiplica pelo mesmo fator = PG / exponencial" e a duplicação sucessiva (Q9). Meia-vida e gráfico da exponencial ficam para as séries próprias. |
| Lucro, desconto, margem sobre custo × venda | **Descontos, acréscimos, lucro e prejuízo** (próxima série) | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Juros sobre juros e a fórmula M = C · (1 + i)ᵗ** | 02, 03 | Q1, Q5 | 10–12 min |
| **2. Simples × compostos: reta e curva, PA e PG** | 04, 08 | Q4, Q8, Q9 | 10–12 min |
| **3. Potências sem calculadora e descobrir o tempo** | 05, 06 | Q6, Q7, Q2 | 10–12 min |
| **4. Trazendo valores para hoje** | 07 | Q3 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Vídeo 3, "dobrar o tempo":** 12 meses com 1,05⁶ ≈ 1,34 é **1,34² ≈ 1,80**, não 2 · 1,34 = 2,68 nem 1,68. A IA costuma escrever "o dobro do fator". O mesmo vale para o exercício: 1,22² = 1,4884.
- **Vídeo 3, logaritmo:** o denominador é **log(1 + i)** (log 1,2 ≈ 0,08), não a taxa (0,2). Com 0,30 ÷ 0,2 sairia 1,5 ano, que é absurdo. E para triplicar usa-se **log 3**, não log 2.
- **Vídeo 2, prazo menor que um período:** antes de t = 1, os juros **simples** rendem mais (meio período a 10%: 1,05 contra cerca de 1,0488). A IA tende a dizer que os compostos "sempre" rendem mais, que é o distrator A da Questão 4.
- **Vídeo 1, Questão 5:** 1,10 · 1,20 · 0,75 = **0,99** (perda de 1%), não ganho de 5% (soma) nem de 1% (sinal trocado).

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 4:** pronto sem voz · `ep4_valor_presente` · 1158 pal. ~7,7 min · voz: parte 2 da cena 14 · capa A · Q3 A
- **Vídeo 1:** pronto sem voz · `ep1_juros_sobre_juros` · 1701 pal. ~11,3 min · voz: parte 2 da cena 17 · capa B
- **Vídeo 2:** pronto sem voz · `ep2_simples_compostos` · 1752 pal. ~11,7 min · voz: parte 2 da cena 19 · capa A · Q4 C, Q8 E, Q9 D
- **Vídeo 3:** pronto sem voz · `ep3_potencias_tempo` · 1783 pal. ~11,9 min · voz: parte 2 da cena 18 · capa A · Q6 D, Q7 B, Q2 B
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1686 pal. ~11,2 min · voz: parte 2 da cena 18 · capa A · inéditas D, A, E, C, B
