# Estilo do Estudativo

Vale para as aulas do curso novo, em `canais/estudativo/aulas/<id>/`. Onde este guia diverge de `ESTILO_COMUM.md`, vale este guia. Para produzir uma aula, use a skill `estudativo-aula`.

## O que muda em relação ao estilo comum

- **Sem legenda embutida:** as palavras-chave entram na tela no tempo da fala.
- **Visual próprio:** `_ferramentas/editorial.py`, não o `motor.py` claro nem o `matematica.py`.
- **Roteiro curto:** sem mapa da aula, sem resumo longo.
- **CTA curto:** só "inscreva-se", com ponte para a próxima aula.

## Conceito visual

Tipografia editorial em movimento, inspirada nos vídeos de `C:\Users\Paulo\Documents\Claude\videos-referencias`:

- papel claro com grade fina e arco cinza à deriva;
- muito espaço vazio;
- grotesca pesada (Inter Black) misturada com serifada itálica (Instrument Serif);
- palavras que entram desfocadas e ganham foco, no tempo da fala;
- uma única cor forte por tela, a da matéria;
- esferas com volume para respostas e números de passo;
- caixas pontilhadas com cursor;
- cortina na cor da matéria entre as partes grandes da aula;
- palco escuro com brilho da cor da matéria para atalhos e macetes.

Vermelho é erro e verde é certo, em qualquer matéria.

## Cor de cada matéria

| Matéria | Cor | Forma |
|---|---|---|
| Matemática | `#2B14D9` índigo | + (desenhada) |
| Português | `#E3212F` vermelho | aspas |
| Redação | `#FFC400` amarelo | traço |
| Literatura | `#8A1C4A` vinho | livro |
| Inglês | `#C6E800` lima | balão |
| Espanhol | `#FFA8BC` rosa | balão |
| Artes | `#E0009C` magenta | estrela |
| Física | `#FF5A1F` laranja | órbita |
| Química | `#00B8A0` turquesa | hexágono |
| Biologia | `#2FA84F` verde | folha |
| História | `#B5742A` ocre | arco |
| Geografia | `#0A93E0` azul | relevo |
| Filosofia | `#7B3FE4` roxo | olho |
| Sociologia | `#0B5D6B` petróleo | pessoas |

Fonte da verdade: `MATERIAS` em `editorial.py`. A folha `identidade/folha_materias.jpg` mostra todas lado a lado. As formas ainda não desenhadas saem como esfera.

Em Português e Biologia, vermelho e verde coincidem com a cor da matéria. Nessas matérias, marque erro e acerto também com risco ou sinal, não só com a cor.

## Capas

A cor da matéria em tela cheia, com a tira da matéria no canto: é o que identifica a matéria na lista de vídeos. São três variações: o erro ou gancho, o modelo padrão (`capa_modelo`) e o macete. Títulos sem a palavra ENEM; a descrição cita as provas.
