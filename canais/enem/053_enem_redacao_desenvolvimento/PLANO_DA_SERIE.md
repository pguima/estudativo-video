# Série Desenvolvimento (Redação ENEM): 7 episódios para iniciantes

Material: `Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html`. Cópia em `_material/`, texto em `_material/material_desenvolvimento.txt`.
Prompts do usuário (Drive, pasta "redacao", 27/10/2026): `_material/prompts_03-desenvolvimento.md`. Modelo de aula: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md).
Títulos: `<gancho> | Desenvolvimento da Redação Ep. N`. Playlist da série: **"Redação: Desenvolvimento"** (e a playlist geral "Redação ENEM do Zero").

| Ep. | Pasta | Tema | Seções | Questões | Situação |
|---|---|---|---|---|---|
| 1 | `ep1_anatomia_paragrafo` | Onde a tese é provada: as cinco partes do parágrafo | 01, 02 | Q6 | pronto (final + publicacao) |
| 2 | `ep2_topico_frasal` | O tópico frasal | 03 | Q1, Q3 | pronto (final + publicacao) |
| 3 | `ep3_argumento_repertorio` | Argumento e repertório: explicar e comprovar | 04, 05 | Q8, Q4 | pronto (final + publicacao) |
| 4 | `ep4_analise_fechamento` | Análise e fechamento: o "e daí?" | 06, 07 | Q2, Q5 | pronto (final + publicacao) |
| 5 | `ep5_paragrafo_modelo` | O parágrafo-modelo e do fraco ao bom | 08, 09 | Q7 | pronto (final + publicacao) |
| 6 | `ep6_oficina_cinco_linhas` | Oficina: o segundo parágrafo em cinco linhas | 10 | Q9 | pronto (final + publicacao) |
| 7 | `ep7_revisao_desafio` | Revisão: V ou F dos 10 erros, 5 inéditas e desafio | 01, 11, 13 | 5 inéditas | pronto (final + publicacao) |

**Analogia âncora:** a série continua a Introdução. Lá, a introdução colou na caixa a lista "contém 2 itens: A e B". Aqui, **cada parágrafo de desenvolvimento ENTREGA UM ITEM**, em cinco etapas:
- **ETIQUETA DO ITEM** = tópico frasal;
- **POR QUE ESTÁ NA CAIXA** = argumento;
- **NOTA FISCAL** = repertório;
- **PRODUTO FUNCIONANDO** (na casa do cliente) = análise;
- **RECIBO ASSINADO** = fechamento, que liga o item à tese.

A pergunta do cliente é **"E DAÍ?"**. O rascunho de cinco linhas é a **lista de compras** (ep. 6). A ponte com Linguagens é "a tese é o tampo, os argumentos são as pernas": aqui o aluno aprende a construir cada perna.

**Fio da série:** a redação do estigma (ENEM 2020), com a tese guardada no ep. 4 da Introdução. Eixos: desinformação (D1, parágrafo-modelo da seção 08) e mídia (D2, construído ao vivo no ep. 6). A série Conclusão fecha a redação.

**Desenho compartilhado:** `desenvolvimento_visual.py`.
- **Componentes:** ícones das 5 etapas (`icone_etapa`), ficha da entrega (`ficha_entrega`, checklist), `mini_entrega`, barras de peso típico (`barras_peso`), parágrafo com faixas por função (`faixas_paragrafo`), `tese_card`.
- **Textos exatos do material:** `MODELO`, `TOPICOS`, `FECHAMENTOS`, `RASCUNHO`, `V1_OPINIAO`, `V2_SOLTO`, `APRESENTAR`, `DEGRAUS`…
- **Herança:** importa tudo de `../052_enem_redacao_introducao/introducao_visual.py` (rascunho com caligrafia, caixa, alternativas, recap, erros, CTA com Anki).
- **Cores das etapas:**
  - tópico: azul `#2F6FED`;
  - argumento: azul-petróleo `#0E8C9A`;
  - repertório: ocre `#B7791F`;
  - análise: laranja-telha `#D9480F`;
  - fechamento: magenta `#C2255C`.
- **Cores com função:** azul = definição · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

**Fidelidade (risco nº 1):**
- **Referências:** só as do material. São elas: O Alienista (Machado de Assis, Simão Bacamarte, Casa Verde, Itaguaí), Lei nº 10.216/2001, Lei nº 10.436/2002, Constituição de 1988, Estatuto da Pessoa Idosa e Cinema Paradiso (Giuseppe Tornatore).
- **Métodos:** "cinco partes" e "mini-conclusão" são método, não termo oficial.
- **Níveis:** nenhum nível ou nota da C3 (isso é da série Competência 3).
- **Ep. 6:** a linha "Repertório" fica **em aberto**, sem filme ou notícia inventada.
- **Trechos didáticos:** levam aviso na tela.
- **Religião:** nada de exemplos religiosos (memória do usuário).

**Voz:** Gemini TTS local, Neno, com o mesmo VOZ da série Introdução.
**Arquivos finais:** `epN_<tema>/final/enem_redacao_desenvolvimento_epN_<tema>.mp4`.

## Notas de produção (28/10/2026)

- Voz: Gemini com gerador estrito (rejeita o modelo lite; tenta até sair a voz certa). Transcrição conferida contra o roteiro em todos os episódios.
- ep1: improviso da voz aparado. ep2: trecho improvisado (~1min20) e frase repetida cortados da parte 1 (backup `parte_1.wav.improviso.bak`).
- ep5: cena 32 reescrita.
- Durações finais: ep1 10:39 · ep2 10:00 · ep3 12:21 · ep4 11:25 · ep5 12:10 · ep6 10:22 · ep7 12:25.
- Pendentes nos textos de publicação: `[LINK DOS FLASHCARDS]` e `[LINK DA PLAYLIST]`.
