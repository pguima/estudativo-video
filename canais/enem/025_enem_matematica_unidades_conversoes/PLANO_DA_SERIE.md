# Série Unidades de Medida e Conversões (Matemática ENEM): 5 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html` (texto extraído com
`_ferramentas/extrair_material.py` em `_material/material_unidades.txt`) · modelo: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md)
· prompts por episódio enviados em 23/10/2026 (pedido: "faça sem os áudios").

| Ep. | Pasta | Tema | Recorte do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_escada_metrica` | A escada de 7 degraus: comprimento e massa | 02, 03, 06 (sem "1 L de água = 1 kg") + Q7 | 8–10 min | Área e volume | pronto sem voz (1296 pal. ~8,6 min · voz: parte 2 da cena 14) |
| 2 | `ep2_area_volume` | Área (×100), volume (×1 000), litro = dm³ e 1 L de água = 1 kg | 04, 05, parte da 06 + Q1 (eu), Q2 (nós), Q9 (você) | 10–12 min | Tempo | pronto sem voz (1714 pal. ~11,4 min · voz: parte 2 da cena 18) |
| 3 | `ep3_tempo_compostas` | O tempo não é decimal e a conversão de velocidade, densidade e vazão | 07, 08 + Q3 (eu), Q4 (nós), Q6 (você) | 10–12 min | Análise dimensional | pronto sem voz (1700 pal. ~11,3 min · voz: parte 2 da cena 18) |
| 4 | `ep4_analise_dimensional` | Análise dimensional e unidades de fora do sistema métrico (kWh) | 09, 10 + Q5, Q8 | 8–10 min | Revisão | pronto sem voz (1545 pal. ~10,3 min · voz: parte 2 da cena 16) |
| 5 | `ep5_revisao` | Revisão, V/F dos 9 erros e 5 questões INÉDITAS | 01, 11, 13 (sem Q1–9) | 10–12 min | Escalas, plantas e mapas | pronto sem voz (1560 pal. ~10,4 min · voz: parte 2 da cena 19) |

**Gabaritos do material:** Q1 C (25 000 m²) · Q2 D (1 200 L) · Q3 A (3 h 15) · Q4 B (20 m/s) · Q5 D (800 kg/m³) · Q6 B (1,8 m³) ·
Q7 C (3 500 kg) · Q8 C (127 cm) · Q9 D (60 000 L).
**Imprecisão do material (Q6):** "1 800 m³ seria o volume de uma piscina olímpica inteira" — uma olímpica tem ≈ 2 500 m³ (50 × 25 × 2).
No vídeo: "quase uma piscina olímpica".

**Exemplos:** ganchos do usuário ficam (o do ep3 já cita 3 h 15 e 20 m/s). Blocos podem repetir questões "eu faço"; troca números só
quando o bloco entregaria uma "você faz" (ep2 Q9 piscina 8 × 5 × 1,5; ep3 Q6 torneira de 15 L/min por 2 h).

**Analogias âncora (a revisão retoma todas):** ep1 a ESCADA de 7 degraus (Kátia Hoje Dançou Muito, Dançou Com Marcos) · unidade menor,
número maior · ep2 área = GRADE 10 × 10; volume = CUBO 10 × 10 × 10 · a CAIXA DE LEITE de 1 L ≈ 1 dm³ · 1 L de água = 1 kg ·
ep3 o RELÓGIO de 60 em 60 · unidade composta = fração de DOIS ANDARES · em m/s o número é o menor · ep4 frações que valem 1
(trocar uma nota de 100 por dez de 10) · unidades RISCADAS · kWh = potência × tempo.
Ícones da revisão: escada · caixa de leite · relógio · fração com unidades riscadas.

**Peças comuns:** `comum.py` (nesta pasta) reexporta o `019/comum.py`. Valores com milhar ("10 000"): o expr parte no espaço; use uma
`linha()` própria (modelo em 021/ep2_proporcao_k/roteiro/visual.py). Regras: cena verde de ATALHO por procedimento; fórmula explicada
na hora; CTA com o aviso dos flashcards Anki (cue {anki}). Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho ·
vermelho = erro. Voz: Gemini TTS Studio local (Neno), tags alegre/curiosa/amigavel.

Arquivos finais: `epN_<tema>/final/enem_matematica_unidades_epN_<tema>.mp4`.


**Status 23/10/2026:** os 5 eps prontos SEM VOZ (roteiro, texto para gravar, visual com tempos sintéticos, prévias, 3 capas, aviso Anki). Ep5: inéditas D, E, C, B, A.
Imprecisões do material: Q6 (piscina olímpica ≈ 2 500 m³) e Q2 ("menores que um balde" não vale para 120 L). Prompt do ep2 corrigido: a caixa de leite real (≈ 6 × 9 × 17 cm) não é quase um cubo; o vídeo diz que o leite dela ENCHE um cubo de 10 cm.