# Velocidade, Densidade e Vazão — série de videoaulas

Material de apoio (cópia em `_material/12-velocidade-densidade-vazao.html`, texto em `_material/material.txt`, prompts em `_material/roteiros.md`): `01-matematica/12-velocidade-densidade-vazao.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| **Questão 2 de Razão** (atleta: 100 m em 12,5 s → 8 m/s → 28,8 km/h), que estava guardada | Material `06-razao-proporcao-regra-de-tres.html`, reservada para esta série | **Uso no vídeo 2** ("você faz"). Como a IA de vídeo só vê o material 12, o texto completo da questão (enunciado, alternativas, gabarito e distratores) está dentro do prompt. |
| km/h ↔ m/s (fator 3,6), g/cm³ ↔ kg/m³ (×1 000), 1 m³ = 1 000 L, tempo não decimal (2,5 h = 2 h 30 min) | **Unidades, vídeos de unidades compostas e de tempo** (Q4: 72 km/h → 20 m/s; Q5: óleo 0,8 g/cm³ → 800 kg/m³; Q6: torneira de 15 L/min) | Só revisão relâmpago, sem reensinar. Não repito as questões de Unidades: as contas novas aqui são velocidade média, densidade e vazão. |
| Densidade como propriedade específica; gelo (0,92) e óleo (0,8) flutuando na água | **Química 01 (Matéria, substâncias e misturas)** | Cito como "propriedade que identifica a substância, que você viu em Química". O foco aqui é a conta (d = m ÷ V, m = d · V) e o critério da flutuação como comparação de números. |
| Velocidade e tempo inversamente proporcionais; torneiras e tempo de enchimento como exemplo de grandeza inversa | **Razão** (tabela de razões usuais) e **Grandezas Proporcionais** | Revisão de uma frase. O novo é a média harmônica e o método das frações do tanque. |
| Densidade demográfica | **Geografia** (sem série própria ainda) | Só citada como "a mesma razão com outra roupa". |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A estrutura comum: toda taxa é "quanto por unidade"** | 02, 07, 08 | Q8 | 7–9 min |
| **2. Velocidade média: distância total ÷ tempo total** | 03 | Q1, Q2 do material 06 (atleta) | 8–10 min |
| **3. A armadilha da média: ida a 60, volta a 40, média 48** | 04 | Q2 | 8–10 min |
| **4. Densidade: identificar o material e decidir se flutua** | 05 | Q3, Q4 | 8–10 min |
| **5. Vazão e o método das frações do tanque** | 06 | Q5, Q9, Q6, Q7 | 10–12 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Cuidados ao revisar os roteiros

- **Vídeo 2, Questão 1:** o material diz que a alternativa B (66) é de quem usou 2,3 h, mas 180 ÷ 2,3 ≈ 78,3. O prompt já corrige; confira se a IA não "reaproveitou" a explicação errada que está no material.
- **Vídeo 3, média harmônica:** a IA tende a aplicar 2·v₁·v₂/(v₁ + v₂) a qualquer situação. Ela só vale para **distâncias iguais**; com **tempos iguais** (1 h a 80 e 1 h a 60) a média simples (70 km/h) é a certa.
- **Vídeo 5, ralo:** confira o sinal e a conferência: 1/4 − 1/6 = 1/12 → 12 h (maior que 4 h). Se aparecer 1/4 + 1/6 = 5/12 (≈ 2,4 h) como resposta, o roteiro somou a vazão de saída.
- **Vídeo 2, fator 3,6:** m/s → km/h **multiplica** (8 m/s = 28,8 km/h). Se a tela mostrar 8 ÷ 3,6 ≈ 2,2 km/h, o sentido foi invertido; o número em m/s é sempre o menor.

## Erros encontrados no material

- **Questão 1, explicação da alternativa B:** o material afirma que 66 km/h "é de quem usou 2,3 em vez de 2,5". Está errado: 180 ÷ 2,3 ≈ 78,3 km/h, valor que não está entre as alternativas. Correção usada no prompt: E (90) vem de usar só 2 h e A (60) de usar 3 h; B (66) e D (75) são valores vizinhos sem erro associado; o erro "30 min = 0,30 h" é citado como alerta geral.
- **Questão 9, explicação da alternativa E:** o material diz que 1 080 000 "é o total em litros por dia, sem nenhuma conversão". O total em litros por dia é 45 000 000. O valor 1 080 000 é 45 000 m³ · 24, ou seja, multiplicar pelas 24 horas em vez de dividir. O prompt do vídeo 5 usa essa explicação.

**Peças comuns:** `comum.py` reexporta o `019/comum.py` (tipografia matemática, frações, escada, atalho, selo_teste). Regras: cena verde de ATALHO por procedimento; fórmula explicada na hora; CTA com o aviso dos flashcards Anki (cue {anki}); cores azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.

## Situação dos episódios

- **Vídeo 3:** pronto sem voz · `ep3_armadilha_media` · 1476 pal. ~9,8 min · voz: parte 2 da cena 17 · capa A · Q2 C
- **Vídeo 2:** pronto sem voz · `ep2_velocidade_media` · 1485 pal. ~9,9 min · voz: parte 2 da cena 16 · capa A · Q1 corrigida (B não é 2,3 h) · atleta C
- **Vídeo 1:** pronto sem voz · `ep1_estrutura_comum` · 1361 pal. ~9,1 min · voz: parte 2 da cena 18 · capa A · Q8: só a A fica fora da faixa plausível; B, D, E caem multiplicando de volta
- **Vídeo 4:** pronto sem voz · `ep4_densidade` · 1542 pal. ~10,3 min · voz: parte 2 da cena 20 · capa A
- **Vídeo 6:** pronto sem voz · `ep6_revisao` · 1677 pal. ~11,2 min · voz: parte 2 da cena 18 · capa A · inéditas B, D, A, E, C
- **Vídeo 5:** pronto sem voz · `ep5_vazao_torneiras` · 1837 pal. ~12,2 min · voz: parte 2 da cena 21 · capa A · Q9 E corrigida (45 000 × 24)
