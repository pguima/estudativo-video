# Série Razão, Proporção e Regra de Três (Matemática ENEM): 6 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/06-razao-proporcao-regra-de-tres.html` (texto extraído com
`_ferramentas/extrair_material.py` em `_material/material_razao.txt`) · modelo: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md)
· prompts por episódio enviados em 23/10/2026 (pedido: "faça sem os áudios ainda").

| Ep. | Pasta | Tema | Recorte do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_razao` | Razão: a ordem dos termos e as razões em todo lugar (passeio pela 03, sem km/h↔m/s nem escala) | 02, 03 + Q1, Q9 | 8–10 min | Proporção | pronto sem voz (1378 pal. ~9,2 min · voz: parte 2 da cena 16) |
| 2 | `ep2_proporcao_k` | Proporção, propriedade fundamental e o truque do k | 04, 05 + Q7 | 8–10 min | Direta ou inversa | pronto sem voz (1352 pal. ~9 min · voz: parte 2 da cena 16) |
| 3 | `ep3_direta_inversa` | Direta ou inversa (teste do dobro) e regra de três simples, com treino de 6 situações | 06, 07 + Q4, Q5 | 10–12 min | Composta | pronto sem voz (1694 pal. ~11,8 min · voz: parte 2 da cena 16) |
| 4 | `ep4_composta` | Regra de três composta e o atalho dos homens-hora | 08 + Q6 | 8–10 min | Quando não funciona | pronto sem voz (1214 pal. ~8,1 min · voz: parte 2 da cena 15) |
| 5 | `ep5_quando_nao_vale` | Quando a regra de três NÃO funciona e os 3 hábitos de prova | 09, 10 + Q8 | 8–10 min | Revisão | pronto sem voz (1320 pal. ~8,8 min · voz: parte 2 da cena 14) |
| 6 | `ep6_revisao` | Revisão, V/F dos erros (km/h e escala só citados) e 5 questões INÉDITAS | 01, 11, 13 (sem a seção 12) | 10–12 min | Grandezas proporcionais | pronto sem voz (1791 pal. ~11,9 min · voz: parte 2 da cena 19) |

**Gabaritos do material:** Q1 C (2/5) · Q2 C (28,8) · Q3 B (20 km) · Q4 C (600) · Q5 B (18 dias) · Q6 B (8 dias) · Q7 D (R$ 40 000) ·
Q8 B (2 min) · Q9 B (R$ 232). As Q2 (velocidade) e Q3 (escala) NÃO entram nesta série (têm séries próprias).

**Analogias âncora (a revisão retoma todas):** ep1 razão = comparar dividindo · "o que vem depois de 'para' vai embaixo" ·
taxa = razão com unidade (o R$/kg da etiqueta) · ep2 proporção = a mesma RECEITA em tamanhos diferentes · extremos = PONTAS,
meios = MIOLO · truque do k = PACOTINHOS · ep3 o TESTE DO DOBRO · ep4 colunas interrogadas uma de cada vez · o PACOTE de
pessoa-hora · ep5 a PERGUNTA DE OURO ("dobrar a causa dobra mesmo o efeito?").
Ícones da revisão: copos de suco · receita dupla · barras direta/inversa · pacote de trabalho · gatos.

**Peças comuns:** `comum.py` (nesta pasta) reexporta o `019/comum.py` (expr com frações e potências, fichas, atalho, selo_teste,
alternativas, erro_cards, pause_timer, pizza, barra). Cada `visual.py` importa como `K` e chama `K.usar_tempos(...)`.
Regras: uma cena verde de ATALHO por procedimento; toda fórmula explicada na hora; CTA com o aviso dos flashcards Anki
(cue {anki}, ver canais/enem/ESTILO.md). Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.
Voz: Gemini TTS Studio local (Neno), tags alegre/curiosa/amigavel.

Arquivos finais: `epN_<tema>/final/enem_matematica_razao_epN_<tema>.mp4`.


**Status 23/10/2026:** os 6 eps prontos SEM VOZ (roteiro, texto para gravar, visual com tempos sintéticos, prévias, 3 capas, aviso Anki).
Material sem erros. Exemplos dos prompts que eram as próprias questões foram trocados (ep1 turma → ônibus; ep2 3:5/64 → 2:3/10 000;
ep3 procedimento → tecido e jardineiros; ep4 muro dos blocos → calçada). Ep6: inéditas B, C, E, A, D.
Dica técnica: o expr do comum parte qualquer espaço ("24 000" vira 2 tokens); o ep2 tem `linha()` no visual.py para valores com milhar.