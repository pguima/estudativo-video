# Série Escalas, Plantas e Mapas (Matemática ENEM): 4 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/11-escalas-plantas-mapas.html` (texto extraído com
`_ferramentas/extrair_material.py` em `_material/material_escalas.txt`) · modelo: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md)
· prompts por episódio enviados em 23/10/2026 (pedido: "faça sem os áudios").

| Ep. | Pasta | Tema | Recorte do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_tres_calculos` | O que é escala, os três cálculos e a cadeia até o km | 02, 05 + Q1 (eu), Q2 (nós), Q3 (você) | 10–12 min | Gráfica × numérica | pronto sem voz (1755 pal. ~11,7 min · voz: parte 2 da cena 19) |
| 2 | `ep2_grafica_grande_pequena` | Escala gráfica × numérica e grande × pequena | 03, 04 + Q8, Q4 | 6–8 min | Plantas e maquetes | pronto sem voz (1294 pal. ~8,6 min · voz: parte 2 da cena 15) |
| 3 | `ep3_plantas_maquetes` | Plantas e maquetes: área usa n², volume usa n³ | 06, 07, 08 + Q9, Q5 (eu), Q6 (nós), Q7 (você) | 10–12 min | Revisão | pronto sem voz (1789 pal. ~11,9 min · voz: parte 2 da cena 18) |
| 4 | `ep4_revisao` | Revisão, V/F dos 8 erros e 5 questões INÉDITAS (Mat + Geo) | 01, 09, 10, 11, 13 (sem Q1–9) | 10–12 min | Velocidade, densidade e vazão | pronto sem voz (1552 pal. ~10,3 min · voz: parte 2 da cena 19) |

**Gabaritos do material:** Q1 B (30 km) · Q2 B (3 cm) · Q3 C (1 : 300 000) · Q4 A (1 : 10 000) · Q5 C (20 m²) · Q6 C (4 m²) ·
Q7 D (40 000 L) · Q8 C (1 : 250 000) · Q9 B (3,5 m).

**Imprecisões do material (o vídeo diz só a parte verdadeira):**
- Q1: "C, D e E são de quem parou em cada degrau" — só E (30 000) é parar num degrau (nos metros). D (3 000) = pulou o degrau
  cm → m (só ÷ 1 000); C (300) = cortou zeros demais (÷ 10 000). Os 3 000 000 cm (parar no primeiro degrau) nem estão nas alternativas.
- Q3: "a alternativa B é de quem usou 12 000" — 4 / 12 000 dá 1 : 3 000, que é a A (12 km parado em metros). B (1 : 30 000) = 4 / 120 000 (um zero a menos).
- Q6: "a alternativa B (2 m²) aplicou o fator 200 uma vez só" — 1 cm² × 200 = 200 cm² = 0,02 m², que é a A (o vídeo atribui o erro do fator linear à A;
  a B, 2 m², é de quem trocou 200 cm² por 2 m², esquecendo que 1 m² = 10 000 cm²).

**Analogias âncora (a revisão retoma todas):** ep1 o mapa como FOTO ENCOLHIDA (cada 1 cm guarda n cm) · do mapa para o mundo CRESCE
(multiplica), do mundo para o mapa ENCOLHE (divide) · ATALHO DOS 5 ZEROS (tesoura) · ep2 o ZOOM DO CELULAR (mesma da Cartografia 012 ep1:
aproximado = escala grande, afastado = escala pequena) · a BARRA GRÁFICA que viaja com o mapa · escala como fração (1/2 > 1/20) ·
ep3 o QUADRADINHO de 1 cm² que vira 4 m² · a MAQUETE que encolhe em três direções (20 × 20 × 20 = 8 000) · 1 : 100 = 1 cm é 1 m.
Ícones da revisão: mapa com tesoura nos 5 zeros · celular com zoom · maquete.

**Peças comuns:** `comum.py` (nesta pasta) reexporta o `019/comum.py`. Valores com milhar ("250 000"): o expr parte no espaço; use uma
`linha()` própria (modelo em 021/ep2_proporcao_k/roteiro/visual.py). Regras: cena verde de ATALHO por procedimento; fórmula explicada
na hora; CTA com o aviso dos flashcards Anki (cue {anki}). Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho ·
vermelho = erro. Voz: Gemini TTS Studio local (Neno), tags alegre/curiosa/amigavel.

Arquivos finais: `epN_<tema>/final/enem_matematica_escalas_epN_<tema>.mp4`.
