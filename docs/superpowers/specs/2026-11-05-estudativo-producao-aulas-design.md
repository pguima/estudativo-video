# Estudativo, Etapa 2: produção das aulas

Status: padrão aprovado pelo usuário em 2026-11-05, a partir do piloto `MAT-FRA-008`.

## Objetivo

Transformar qualquer aula do catálogo (`canais/estudativo/catalogo/aulas.csv`) em um vídeo pronto para publicar, pedindo só o id. A meta é cerca de 10 vídeos por semana.

## Decisões

| Tema | Decisão |
|---|---|
| Ordem de produção | Sob demanda: qualquer id, em qualquer ordem. Não há ondas. |
| Abordagem | Kit de aula: peças prontas e tema por matéria, com animação sob medida onde ela ensina. |
| Identidade | Conceito editorial dos vídeos de referência, com uma cor forte e uma forma-símbolo por matéria. |
| Legenda | Sem legenda embutida. As palavras-chave entram na tela no tempo da fala, e as legendas ficam com o YouTube. |
| Música | Sem música. |
| Voz | Gemini TTS local, Neno, sotaque neutro, tags `alegre`, `curiosa`, `amigavel`, com o tom de professor de cursinho aprovado em Redação. |
| CTA | Só "inscreva-se", junto da ponte para a próxima aula. |
| Formato | 16:9, 1920x1080, 30 fps, capas 1280x720. |

## Roteiro

Uma aula tem de 5 a 8 minutos. O piloto, com 678 palavras, deu 4:35 e foi aprovado, então uma aula pode ficar pouco abaixo de 5 minutos quando o conteúdo acabar: nunca se estica para atingir o tempo. Prática vai até 10 minutos.

Ordem: gancho de até 15 s, lembrete dos pré-requisitos de até 20 s, conteúdo (pergunta, exemplo, regra, exemplo resolvido), um erro comum, atalho em exatas, uma questão com pausa, resposta, fechamento de até 20 s com ponte para a próxima aula.

Fica fora: mapa da aula, recapitulação repetida e episódio de revisão. O limite do conteúdo é a ficha da aula: o que não estiver na cadeia de pré-requisitos só pode ser citado como assunto de outra aula.

Questão de prova real só entra com fonte citada e depois de checar o direito de uso. Questão inédita não pode ser apresentada como real.

## Peças

- `_ferramentas/editorial.py`: fundo, tipografia, formas, `MATERIAS` (cor e forma por matéria) e o kit (`fr`, `sinal`, `resultado`, `passo`, `corrida`, `palco`, `capa_modelo`). `usar()` ajusta a cor do texto para as matérias de cor clara.
- `canais/estudativo/catalogo/ficha_aula.py`: ficha da aula e situação da produção em `producao.csv` (`roteiro`, `voz`, `render`, `pronto`, `publicado`).
- `canais/estudativo/aulas/<id>/`: uma pasta por aula, com `roteiro/`, `audio/`, `trabalho/`, `final/` e `youtube/`.
- `canais/estudativo/ESTILO.md`: o guia do canal.
- `.claude/skills/estudativo-aula/`: o fluxo completo.

## Erros e verificação

- A voz pode improvisar ou repetir: comparar a transcrição com o roteiro antes do render. Palavra trocada que mude conta ou fato obriga a regerar.
- O servidor pode cair no modelo `lite`, com voz diferente: `gerar_voz_local.py` não salva e a aula espera a cota renovar, por volta de 04:00 de Brasília.
- Antes da voz, um revisor independente lê o roteiro como iniciante e confere fatos e contas.
- Depois do render, conferir duração, áudio e quadros das transições.

## Render

O grão foi removido, porque quase não aparecia e pesava no desenho e na compressão, e `render.py` deixou de copiar cada quadro. Um teste com um único processo caiu de 579 para 230 ms por quadro, mas o ganho não se repetiu no render real com 4 processos: as aulas seguintes levaram 27 min (3:26 de vídeo), 32 min (4:15) e cerca de 25 min (4:13), contra 34 min do piloto (4:35). Conte com cerca de 30 minutos por aula. As duas primeiras dividiram a máquina com outras tarefas em parte do tempo. A máquina tem 4 núcleos físicos.

## Pendências conhecidas

- Só a Matemática tem forma-símbolo desenhada. As outras saem como esfera até a primeira aula da matéria.
- O kit nasceu de uma aula de exatas. Matérias de texto vão precisar de peças próprias, como trecho marcado e mapa: criar na primeira aula que precisar, e não antes.
- Não há aula de Prática produzida nem Short no padrão novo.
- As ressalvas de conteúdo da Etapa 1 continuam valendo: Filosofia, Inglês e Espanhol têm pouco material de apoio, então os fatos pedem mais conferência.
