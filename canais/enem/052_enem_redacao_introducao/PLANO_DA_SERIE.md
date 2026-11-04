# Série Introdução (Redação ENEM): 7 episódios para iniciantes

Material: `Estudos/Enem/estudos/06-redacao/02-introducao.html` (cópia em `_material/`, texto em `_material/material_introducao.txt`)
Prompts do usuário (Drive, 26/10/2026): `_material/prompts_02-introducao.md` · modelo de aula: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md)
Títulos: `<gancho> | Introdução da Redação Ep. N` · Playlist da série: **"Redação: Introdução"** (+ playlist geral "Redação ENEM do Zero").

| Ep. | Pasta | Tema | Seções | Questões | Situação |
|---|---|---|---|---|---|
| 1 | `ep1_tres_movimentos` | Da tese ao primeiro parágrafo: os três movimentos | 01, 02 | Q6 | pronto |
| 2 | `ep2_quatro_caminhos` | Contextualizar: quatro caminhos | 03 | Q2, Q8 | pronto |
| 3 | `ep3_ponte_teste_retirada` | A ponte e o teste da retirada | 04 | Q7, Q3 | pronto |
| 4 | `ep4_tese_antecipacao` | A tese e a antecipação dos eixos | 05, 06 | INÉDITA (2017, gabarito B) no lugar da Q4, Q5 | pronto |
| 5 | `ep5_fracas_boas_armadilhas` | Introduções fracas × boas e as armadilhas | 07, 08 | Q1 | pronto |
| 6 | `ep6_oficina_seis_passos` | Oficina: montando uma introdução do zero | 09, 10 | Q9 | pronto |
| 7 | `ep7_revisao_desafio` | Revisão: V ou F dos 10 erros, 5 inéditas, desafio | 01, 11, 13 | 5 inéditas | pronto |

**Analogia âncora:** a introdução é a **ETIQUETA COMPLETA DA ENCOMENDA** (continua o "endereço de entrega" da série 014):
**MAPA** = contextualização ("de onde parte a discussão?") · **RUA DE ACESSO** = ponte (entra no ep. 3) ·
**ENDEREÇO + ENTREGA** = tese ("o que o autor defende?") · **LISTA DA CAIXA** = antecipação ("por quais caminhos?").
Apoios: quatro portas (ep. 2), cartão-postal genérico = repertório de bolso e TESTE DA RETIRADA (ep. 3),
"promessa feita é promessa cobrada" (ep. 4), "arrume a caixa antes de escrever a etiqueta" (ep. 6).
Fio entre as séries de Redação: a tese do estigma (2020) aparece no ep. 4 e será terminada nas séries Desenvolvimento e Conclusão.

Desenho compartilhado: `introducao_visual.py` (etiqueta de 4 faixas `etiqueta_intro`, `mini_etiqueta`, ícones das peças,
`recap`, `erros`, `cta_intro` com Anki) + reaproveita a série 014 (rascunho com caligrafia, alternativas, peças, placar).
Cores das peças: mapa azul · rua verde · tese laranja-telha · lista azul-petróleo. Cores com função: azul = definição ·
verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).
Fidelidade (risco nº 1 da série): só números e leis do material — 55,5% (Censo 2022), 1888, Lei nº 10.639/2003, art. 216,
art. 231, art. 68 do ADCT, Lei nº 9.534/1997, Estatuto da Pessoa Idosa (Lei nº 10.741/2003). Trechos didáticos com aviso na tela.
Voz: Gemini TTS local, Neno, `VOZ = dict(tags=["alegre", "curiosa", "amigavel"], prompt=...)`.
Arquivos finais: `epN_<tema>/final/enem_redacao_introducao_epN_<tema>.mp4`.

## Situação (27/10/2026): os 7 episódios estão renderizados
- **Ep. 2:** a voz da parte 2 foi refeita no modelo completo. A versão lite antiga está em `parte_2_lite.wav.bak`.
- **Ep. 4:** a parte 1 também foi refeita (cena 9 sem improviso).
- **Sem tema religioso (pedido do usuário, 27/10/2026):** parte do público é de diversas religiões, então a série **não usa
  "racismo religioso"** nem "tradições de matriz africana". O 2º eixo da tese-modelo (tema de 2024) passou a ser a **mídia**:
  "…da aplicação irregular da lei nas escolas e da pouca visibilidade da cultura afro-brasileira nos meios de comunicação";
  eixos curtos "a escola e a mídia". Mudou nos eps. 1 (cenas 14, 18), 4 (11, 15, 19), 5 (10, 11) e 6 (30), no
  `introducao_visual.py` (V3_BOA) e no material. Só essas cenas foram regravadas e emendadas no áudio
  (`trocar_cenas.py` na pasta da série); backups em `audio/nova_voz/*.antes_midia.bak` e `analise/voz_antes_midia.json.bak`.
  A 15.a do ep. 4 voltou a dizer "da lei". Ep. 6, cena 30: corrigido "Lei 10.630" → 10.639.
  **Em temas futuros, evitar exemplos que envolvam religião.**
- Os capítulos dos publicacao.md (eps. 1, 2, 4, 5, 6) foram recalculados com os tempos novos (`analise/capitulos_cenas.json` = capítulo → cena).
- Letra manuscrita: fonte **Caveat** (`_ferramentas/fontes/`, HAND_K = 1,3).
- Página da série: https://claude.ai/artifact/6U3JjmVPf296C56g9SdRpp (gerada por `scratchpad/introducao/gerar.py`). Cada versão
  de artifact guarda no máximo **256 MiB**, e os 7 vídeos somam cerca de 272 MB. Por isso o **ep. 4 fica numa página própria**:
  https://claude.ai/artifact/HGNA5bJqMHnjQgajK2pbFD (`gerar.py 4`; o link fica em `externos.json`).
- Títulos ⬅️/➡️ dos 7 publicacao.md já sincronizados com o TITULO de cada cenas.py.
