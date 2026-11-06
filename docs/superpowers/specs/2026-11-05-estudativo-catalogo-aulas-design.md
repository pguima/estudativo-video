# Estudativo: catálogo de aulas e playlists (Etapa 1)

Data: 2026-11-05 · Situação: concluída e aprovada pelo usuário em 2026-11-05

## Objetivo

Reiniciar o Estudativo como um curso pensado para o YouTube, e não como adaptação de um plano de estudos.
Esta spec cobre só a **Etapa 1: listar as aulas e as playlists**. A produção dos vídeos (Etapa 2) terá spec própria, depois que a lista for aprovada.

## Por que recomeçar

- O cronograma tem 559 assuntos. A 5 a 7 aulas por assunto, seriam de 2.795 a 3.913 aulas, ou 410 a 580 horas de vídeo na média atual (8,9 min), mais que as 377 horas do cronograma inteiro.
- O assunto do plano de estudos virou a unidade da aula. Como ele junta várias habilidades, a série herda conteúdo ainda não ensinado (caso de Conjuntos Numéricos com potenciação e frações).
- A coluna "Incidência" foi dada por matéria, não por assunto: todos os assuntos de uma matéria têm a mesma nota. Ela não serve para priorizar.

## Decisões tomadas

| Tema | Decisão |
|---|---|
| Provas | ENEM + grandes vestibulares: Fuvest, Unicamp, Unesp e UERJ |
| Ponto de partida | Nivelamento sob medida: só as bases do fundamental que alguma aula seguinte usa |
| Aulas ENEM existentes | Recomeço do zero: nenhuma entra no catálogo novo. `canais/enem/` fica intacta e os vídeos publicados não mudam |
| Método | Mapa de habilidades: 1 aula = 1 habilidade |
| Tamanho | Mapa aprovado: 1.169 vídeos. Catálogo montado: 1.502 vídeos, dentro do teto de 40% por trilha |

## Fontes

- **Assuntos a cobrir:** `Projetos/Estudos/Enem/cronograma-enem.csv` (os 559 assuntos servem de checklist de cobertura, não de estrutura).
- **O que cai em cada prova:** matriz de referência do Inep e editais oficiais de Fuvest, Unicamp, Unesp e UERJ.
- **Peso de cada tema:** rankings públicos de assuntos mais cobrados no ENEM. As fontes divergem bastante, então servem para ordenar temas, não como dado exato. Nos outros vestibulares, a etiqueta diz apenas se o tema cai ou não.

## Estrutura

Hierarquia: **Matéria → Trilha → Módulo → Aula**.
Exemplo: Matemática → Frações → Somar frações → "Somar frações com denominadores diferentes".

Tudo fica em `canais/estudativo/catalogo/`:

| Arquivo | Conteúdo |
|---|---|
| `aulas.csv` | Fonte única: uma linha por aula |
| `playlists.csv` | Definição de cada playlist (a ordem das aulas é derivada de `aulas.csv`) |
| `cobertura.csv` | Cada um dos 559 assuntos ligado às suas aulas, ou à justificativa de não ter aula |
| `validar_catalogo.py` | Validação automática |
| `gerar_planilha.py` | Gera a planilha de revisão e a ordem de cada playlist |

### Campos de cada aula

| Campo | Exemplo |
|---|---|
| `id` | `MAT-FRA-012` |
| `titulo` | Somar frações com denominadores diferentes |
| `materia`, `trilha`, `modulo` | Matemática, Frações, Somar frações |
| `ordem` | Posição dentro do módulo |
| `habilidade` | Ao final, você consegue somar 1/2 + 1/3 |
| `camada` | `nivelamento`, `nucleo` ou `extensao` |
| `tipo` | `aula` ou `pratica` |
| `prereqs` | Códigos das aulas necessárias, separados por `;` |
| `provas` | `enem;fuvest;unicamp;unesp;uerj` |
| `prioridade` | `1` (alta), `2` ou `3` |
| `termo_busca` | como somar frações com denominadores diferentes |

### Camadas

- **Nivelamento:** bases do fundamental que alguma aula do Núcleo usa. Quem já sabe pode pular.
- **Núcleo:** o que cai no ENEM e nos grandes vestibulares. Primeira onda de produção; o canal já funciona completo só com ela.
- **Extensão:** o que só cai em vestibulares tradicionais (ex.: números complexos, se a checagem nas fontes oficiais confirmar).

## Regras de cada aula

1. **Um tipo de problema por aula.** Habilidade não é cada passo: casos parecidos ficam juntos em uma aula de 5 a 8 minutos (ex.: multiplicar e dividir potências de mesma base). Conteúdos diferentes ficam separados. Se a aula não cabe no tempo, ela é dividida.
2. **Nada ainda não ensinado.** Se a aula usa um conteúdo, ele é pré-requisito declarado. Citar de passagem só é permitido com um aviso curto de que aquilo vem depois.
3. **De 5 a 8 minutos.** Se passar disso, a aula deve ser dividida.
4. **Prática regular.** Vídeo de questões de até 10 minutos, no lugar do episódio de revisão. Módulo com 4 aulas ou mais termina na sua própria prática. Módulo com até 3 aulas pode dividir a prática com o módulo seguinte da mesma trilha, e essa prática cobre os dois.
5. **Aula independente.** Funciona sozinha para quem chega pela busca e em sequência na playlist.
6. **Título da matéria, não da prova.** Ex.: "Frações do zero | Matemática". ENEM e vestibulares vão na descrição e nas tags.

## Playlists

Um vídeo pode estar em mais de uma playlist. O catálogo terá quatro tipos fixos e playlists especiais:

| Tipo | Quantidade | Conteúdo | Exemplo |
|---|---|---|---|
| Trilha | 1 por trilha | Todas as aulas da trilha, na ordem do curso. É a playlist principal de cada aula | Frações do Zero |
| Matéria | 1 por matéria | Todas as aulas de Nivelamento e Núcleo da matéria, em ordem | Matemática do Zero |
| Comece Aqui | 1 por matéria que tenha Nivelamento | Só o Nivelamento | Comece Aqui: Bases de Matemática |
| Prova | 1 por prova e matéria, quando houver pelo menos 10 aulas | Aulas etiquetadas com aquela prova, em ordem | Matemática para a Fuvest |
| Especial | Sob demanda | Porta de entrada pela busca, definida por filtro | Tabuada e as Quatro Operações do Zero |

Cada linha de `playlists.csv` traz: `id`, `titulo`, `tipo`, `materia`, `regra` (qual filtro de aulas ela usa), `descricao` e `termo_busca`.

A lista de aulas de cada playlist **é gerada pelo filtro**, nunca digitada à mão. Assim, incluir uma aula atualiza todas as playlists em que ela entra.

As práticas entram nas playlists de Trilha, Matéria e Comece Aqui, mas não nas de Prova, que trazem só aulas. Uma playlist só de exercícios por matéria pode ser acrescentada depois, se fizer falta.

## Validação automática

`validar_catalogo.py` falha se encontrar:

- `id` repetido, campo obrigatório vazio ou valor fora da lista permitida;
- pré-requisito inexistente ou dependência em círculo;
- aula antes do seu pré-requisito na ordem do curso;
- aula do Núcleo que depende de aula da Extensão;
- aula do Nivelamento que não leve, direta ou indiretamente, a uma aula do Núcleo (práticas ficam de fora desta regra);
- módulo com 4 aulas ou mais sem prática própria; módulo menor sem prática que não divida com o seguinte; dois módulos seguidos sem prática; último módulo da trilha sem prática; prática conjunta de módulo do Núcleo ou Nivelamento que caia na Extensão;
- assunto do cronograma sem aula e sem justificativa em `cobertura.csv`;
- trilha com mais vídeos que 1,4 vez o previsto no mapa aprovado;
- playlist vazia, ou com aulas em ordem que quebre pré-requisitos;
- playlist que falte, sobre ou não traga exatamente as aulas previstas para o seu tipo na tabela acima;
- aula que não esteja em exatamente uma playlist de Trilha, ou aula de Nivelamento/Núcleo fora da playlist da sua Matéria.

A regra 1 (uma habilidade só) depende de julgamento, então o script só sinaliza títulos com " e " para revisão, sem falhar.

## Entregas, nesta ordem

1. **Mapa geral:** matérias, trilhas, módulos, lista de playlists de Matéria e Comece Aqui, e estimativa por camada.
2. **Matemática completa, aula por aula**, com as suas playlists. O usuário valida o modelo aqui.
3. **Demais matérias**, somente depois dessa aprovação.

Cada entrega traz uma planilha de revisão com abas de aulas, playlists e cobertura, além do resultado da validação.

## Fora do escopo

- Roteiros, modelo de aula, visual, voz e render (Etapa 2).
- Publicação, ou qualquer mudança nos vídeos e playlists que já estão no canal.
- Dados de desempenho do canal: a página do YouTube não carregou os números. Podem entrar na priorização se o usuário os fornecer.
- Provas além das cinco definidas. A lista pode crescer depois, acrescentando etiquetas.
