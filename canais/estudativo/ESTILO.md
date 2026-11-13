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

## Shorts

- **Sempre com trilha e efeitos sonoros.** As aulas não têm música, mas todo Short tem. Use `SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={...})` no `visual.py`. O `render.py --final` chama o `som_tech`, que faz a trilha eletrônica, os efeitos e o volume de −14 LUFS. Acerte cada efeito com uma animação: contagem com `tick`, resposta com `confirm`, erro com `deny`, peças entrando com `pop`, digitação com `typing`, clique com `click` e `notif`.
- **Modelo:** `divulgacao/MAT-NUM_short/`, o convite de uma trilha publicada. É vertical, 1080x1920, com cerca de 35 s. Ordem: desafio no 1º quadro, macete no palco escuro, virada, mural com as capas reais e busca "Estudativo" com a playlist. A legenda queimada fica em y≈1560.
- **O `publicacao.md` do Short sempre tem `### Tags`** logo depois do vídeo relacionado. São de 12 a 15 termos separados por vírgula: o macete do vídeo, os assuntos da trilha, "matemática do zero", "estudativo" e "shorts".
- **Capa vertical 1080x1920** em `youtube/capa_short_*.jpg`, gerada pelo `divulgacao/capa_shorts.py` (acrescente uma função por Short). Use o fundo da cor da matéria (`capa_base`) com o desafio em letra grande e branca, a pergunta em amarelo e a bola "3s". Não mostre a resposta, deixe a pergunta em aberto. Mantenha o texto entre y 250 e 1600.

## Questões resolvidas

Ficam em `questoes/<PROVA>-<nº>/` (resolução horizontal) e `questoes/<PROVA>-<nº>_short/` (Short). Modelo: `questoes/ENEM2025-153`, que segue a estrutura das questões antigas (`canais/enem/questoes`, no histórico do git).

- **Print da questão no 1º quadro.** Recorte a questão do PDF da prova para `enunciado/questao.png` (PyMuPDF, 300 dpi). Use `ENTRADA_SECA = True` e passe marca-texto amarelo sobre o print, no tempo da fala.
- **Estrutura da horizontal (3 a 4 min):**
  1. a questão;
  2. as ideias, cada uma pelo nome e explicada;
  3. os passos numerados;
  4. a resposta;
  5. por que cada alternativa errada engana;
  6. o atalho, no palco escuro;
  7. um desafio para os comentários;
  8. o resumo;
  9. os cartões "AULA" com as aulas do catálogo usadas na questão.
- **Som da horizontal:** efeitos sonoros, sem trilha: `SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, sfx={...})`.
- **Short com no mínimo 1 minuto:**
  1. o print com marca-texto;
  2. as alternativas, "comenta antes de ver" e a contagem para pausar;
  3. a resolução;
  4. a resposta em destaque;
  5. a armadilha;
  6. o atalho;
  7. "você acertou?" e o cartão da resolução completa.
- **Destaque o objeto da resposta.** Se a resposta é um código ou número, monte-o em casas grandes, uma cor por pedaço, e repita-o em letra enorme numa faixa. Uma resposta só falada fica confusa.
- **Títulos** podem levar "ENEM 2025", porque é assim que o aluno procura a questão.
