# Estilo comum a todos os canais

Vale para **todo** vídeo, de qualquer canal. O que muda de um canal para outro está em
`canais/<canal>/ESTILO.md`. **Antes de editar um vídeo, leia este arquivo e o ESTILO.md do canal.**

| Canal | Guia |
|---|---|
| Trading (ICT / Smart Money) | [canais/trading/ESTILO.md](canais/trading/ESTILO.md) |
| ENEM (Física) | [canais/enem/ESTILO.md](canais/enem/ESTILO.md) |
| Seguridade Social (INSS) | [canais/seguridade_social/ESTILO.md](canais/seguridade_social/ESTILO.md) |
| Tecnologia (IA, dev, ferramentas) | [canais/tecnologia/ESTILO.md](canais/tecnologia/ESTILO.md) — **visual próprio** (futurista, `tech.py`): a seção 2 abaixo não vale para ele |

---

## 1. Regras que nunca mudam
- **Português do Brasil** em tudo: narração, textos na tela, capa, título e descrição.
- **16:9, 1920x1080, 30 fps.** Capas em 1280x720.
- **Sem música de fundo.** Só a narração.
- **Ritmo didático, nunca frenético.** Pausas `[p=0.2]` a `[p=0.6]` entre as ideias.
- **Voz masculina, grave, imponente, que passa confiança.** A mesma voz do início ao fim do vídeo.
- **Ignorar propaganda do material original** (cartão final da marca do autor, links de curso etc.).
- **Um vídeo = uma pasta**, dentro do canal certo: `canais/<canal>/NNN_<slug>/`. Nunca misturar canais.
- **Fechamento com CTA**: like → inscreva-se → sininho → pergunta nos comentários → despedida.

## 2. Linguagem visual (motor.py, igual em trading, ENEM e seguridade; tecnologia usa `tech.py`)
- **Fonte:** Inter (pesos medium, bold, extrabold e black). Ícones: Segoe Icons.
- **Fundo:** gradiente radial suave + dois arcos decorativos (canto inferior esquerdo e superior direito).
- **Cartões:** retângulos arredondados (raio 28; 36 nas capas), brancos com sombra (ou cinza-escuro no tema escuro).
- **Título no topo (`title_chip` / `head`)**: pílula branca centralizada, 2 linhas em CAIXA ALTA extrabold;
  linha 1 escura, linha 2 colorida. Uma cor por tipo de conteúdo (ver o guia de cada canal).
- **Legenda palavra a palavra** na parte de baixo (y≈948): cada palavra aparece quando é dita;
  palavras marcadas com `*asterisco*` saem em extrabold e maiores.
- **Animação:** entrada suave (ease-out ~0,5 s, subindo alguns pixels). Nada de cortes secos ou zoom agressivo.
- **Semântica de cor fixa:** verde = certo / alta / alvo; vermelho = errado / baixa / pegadinha / stop;
  âmbar = atenção, dica, macete, nível marcado.
- **Tela de CTA** (`aula.cta`): três cartões (Curtir, Inscreva-se com o cursor clicando, Sininho balançando),
  um cartão com a pergunta para os comentários e a despedida em letra grande.

## 3. Roteiro (`roteiro/cenas.py`)
- Marcações: `{cue}` dispara animação · `*texto*` destaque na legenda · `[p=0.4]` pausa.
- `PRONUNCIA = {...}`: siglas soletradas (ex.: `"INSS": "I N S S"`), termos estrangeiros com grafia fonética.
  A legenda mantém o texto original.
- Números e fórmulas **por extenso** no texto narrado ("três vezes dez elevado a oito",
  "artigo cento e noventa e cinco"); na tela, aparecem em notação normal.
- Frases curtas, uma ideia por frase. Falar com o aluno em 2ª pessoa ("você").
- Estrutura base: **gancho → mapa da aula → blocos de conteúdo → erros/pegadinhas → resumo → CTA.**

## 4. Capas (`youtube/capa.py`)
- Sempre **3 variações** (A, B, C), arquivo `capa_<letra>_<ideia>.jpg`; a A é a recomendada.
- Layout: **texto enorme à esquerda** (2 linhas em preto black + 1 palavra-chave numa caixa colorida),
  **cartão ilustrativo à direita** (x=1120, 700x840), subtítulo menor embaixo em cinza.
- Ganchos de capa: curiosidade, dor/erro, macete. Poucas palavras.

## 5. Publicação (`youtube/publicacao.md`)
Mesma estrutura em todos os canais, nesta ordem:
1. Arquivo do vídeo (duração, resolução, tema) · canal · tipo de narração.
2. Tabela das 3 capas (recomendada em negrito) + dica do "Testar e comparar".
3. 4 opções de título (até 70 caracteres), a recomendada marcada, cada uma casada com uma capa.
4. Descrição pronta para colar: parágrafo de abertura → 📌 O que você vai aprender (✅) → ⏱️ Capítulos
   → 📋 Resumo → 👍 CTA → 💬 pergunta → 3 hashtags.
5. Tags · Hashtags · Comentário fixado (cola de revisão com emojis + pergunta).
6. Configurações do Studio (não é para crianças, Educação, PT-BR, voz sintética), tela final, cards,
   playlist e ideias de Shorts.

## 6. Fluxo técnico
Ver `LEIA-ME.md`. Resumo: `cenas.py` → `roteiro_para_gravar.txt` → voz gerada pelo usuário
(vozgen/Gemini TTS, em `Downloads\nova voz`) → `transcrever_palavras.py` + `voz_externa.py` → `visual.py` → `render.py --jobs 3/4`.
