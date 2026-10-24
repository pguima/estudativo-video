# Função Afim: Gráfico, Coeficientes e Aplicações — série de videoaulas

Material de apoio (cópia em `_material/24-funcao-afim-grafico-coeficientes.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/24-funcao-afim-grafico-coeficientes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| y = kx (reta pela origem) × reta que não passa pela origem; táxi com bandeirada (6 + 2,5x) | **Grandezas proporcionais** (série 07) | Abordagem "você já viu isso disfarçado" no vídeo 1: a direta era o caso b = 0 e a "armadilha da parcela fixa" era uma afim. A Q2 daqui (celular, 100 → 200 min) tem a mesma armadilha da Q5 de Grandezas (táxi, 8 → 16 km), mas exige descobrir a taxa (90 − 40 = 50 em 100 min), por isso mantive. |
| M(t) = C + C·i·t, montante em reta (R$ 1.000,00 a 5% a.m. → M = 1 000 + 50t) | **Juros simples** (série 13) | Segundo "disfarce" no vídeo 1 e de novo na revisão (outras áreas). |
| Ponto de equilíbrio de planos, atalho da diferença, n > 800 → 801, F = 1,8C + 32 | **Equações e inequações do 1º grau** (série 20) | Revisão relâmpago no vídeo 4. O que é novo: ler o equilíbrio como cruzamento de retas e o lucro como estudo do sinal. |
| Máquina, f(x), caminho de volta, leitura de gráfico | **Conceito de função** (série 23) | Pré-requisito de 30 s. |
| Coeficiente angular como tangente, retas paralelas e perpendiculares, declividade em % | Série própria depois: **Coeficiente angular, paralelismo e perpendicularidade** (59) | Só cito no vídeo 3 ("isso tem série própria em Geometria Analítica"). Aqui o a é sempre "taxa de variação com unidade". |
| Montar a lei com sistema 2a + b = 11 e 5a + b = 20 | **Sistemas de equações lineares** (série 22) | Citado como caminho alternativo no vídeo 3. |
| PA como função afim nos naturais; MU e MUV | Séries próprias (Progressão aritmética; Física) | Só na revisão, seção 10. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Parte fixa + taxa: o que é função afim (e onde você já a viu disfarçada)** | 02, 08 ("Proporcional só quando b = 0" e a mola) | Q2, Q9 | 10–12 min |
| **2. O coeficiente angular (taxa), o linear (valor inicial) e o zero** | 03, 04 | Q3, Q8, Q1 | 10–12 min |
| **3. O gráfico e a lei a partir de dois pontos** | 05, 06 | Q6, Q5 | 8–10 min |
| **4. Estudo do sinal, lucro e comparação de planos** | 07, 08 ("Os três modelos de uma pequena empresa") | Q4, Q7 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Vela (vídeo 2, Q1):** a resposta é **95 min** contados desde que a vela foi acesa. A IA tende a fazer 17 ÷ 0,2 = 85 e parar. Confira também a explicação da alternativa A (47,5 = 19 ÷ 0,4): é a altura inicial certa com a taxa errada.
- **Taxa com x espaçado (vídeo 2, exercício):** na tabela de 2 em 2, a taxa é −4 ÷ 2 = **−2**, e o zero é x = 15. Se a IA usar −4, chega em 7,5. E 500/60 ≈ 8,3 h são **8 h 20 min**, não 8 h 30 min.
- **Sinal da taxa:** em grandezas que diminuem, a lei é escrita com menos (V = 2 000 − 80t; V = 60 000 − 6 000t). A IA às vezes escreve "a = 80" e subtrai "na cabeça". Isso confunde o estudo do sinal do vídeo 4.
- **Lucro mínimo (vídeo 4, Q4):** a resposta é **601**. A IA costuma dizer "a partir de 600", o que valida o distrator D.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 1:** pronto sem voz · `ep1_parte_fixa_taxa` · 1586 pal. ~10,6 min · voz: parte 2 da cena 16 · capa A · Q2 C, Q9 B · lei da mola só na resolução da Q9
- **Vídeo 2:** pronto sem voz · `ep2_taxa_valor_inicial_zero` · 1751 pal. ~11,7 min · voz: parte 2 da cena 20 · capa A · Q3 D, Q8 C, Q1 D · vela do prompt só na resolução da Q1
- **Vídeo 4:** pronto sem voz · `ep4_sinal_lucro_planos` · 1662 pal. ~11,1 min · voz: parte 2 da cena 16 · capa A · Q4 E, Q7 B
- **Vídeo 3:** pronto sem voz · `ep3_grafico_dois_pontos` · 1443 pal. ~9,6 min · voz: parte 2 da cena 16 · capa A · Q6 A, Q5 B · bloco f trocado (Celsius→Fahrenheit) para não entregar a Q5
- **Vídeo 5:** pronto sem voz · `ep5_revisao` · 1721 pal. ~11,5 min · voz: parte 2 da cena 21 · capa A · inéditas D, C, E, A, D
