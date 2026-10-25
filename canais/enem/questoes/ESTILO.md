# Estudativo · Questões resolvidas (Matemática): guia de estilo

Vídeos de **uma questão resolvida, explicada como aula**, publicados no **Estudativo** (PT) e no **Estudativo English** (EN).
Ficam aqui em `canais/enem/questoes/`, **separados das aulas** (`canais/enem/NNN_enem_<matéria>_<assunto>/`).
Pasta: `NNN_<matéria>_<assunto>/` com numeração própria das questões (ex.: `001_matematica_triangulo_cateto_5`).
Desde 2026-10-25. Modelo: `001_matematica_triangulo_cateto_5`.

Formato padrão: **aula horizontal 1920x1080 (4–6 min)**. Nada de "direto ao ponto": cada conceito usado é dito pelo nome
e explicado antes de ser aplicado (o 001 nasceu como Short de 1 min e foi refeito por isso).

## Estrutura
1. **Enunciado no primeiro quadro** (`ENTRADA_SECA = True`, `RITMO pad_inicio=0`) + o que a aula vai usar (ex.: Pitágoras + produto notável).
2. **Vocabulário**: os nomes (hipotenusa, catetos...) antes de qualquer conta.
3. **Cada ferramenta pelo nome e explicada** antes de usar: fórmula, de onde vem (ex.: distributiva, prova geométrica) e um
   exemplo numérico. Nunca usar um truque sem dizer qual é.
4. **Por que o dado-chave importa** (ex.: sem "lados inteiros" haveria infinitas respostas) e por que chutar não basta.
5. **Resolução em passos numerados** (PASSO 1 · ISOLAR...), uma ideia por tela; cada conta aparece quando é falada.
6. **Conferência**, **generalização** (o mesmo método em outro caso) e um **desafio** para os comentários.
7. **Resumo** dos passos.
8. **Convite para as aulas (obrigatório em toda questão)**: cena final `aulas` com um cartão "AULA" para cada assunto
   usado na questão, falando o nome de cada um, "procure essas aulas aqui no canal" + CTA de inscrição.
   Vale **mesmo que as aulas ainda não estejam prontas** (o convite fica; a lista de aulas não precisa existir ainda).
   Em PT, os nomes seguem as séries do canal (ex.: 034 Produtos notáveis, 037 Sistemas lineares); em EN, os nomes dos
   assuntos em inglês ("the Pythagorean theorem", "special products").

Regras: o enunciado tem que ter resposta única (ex.: "lados inteiros"); números por extenso no roteiro (a voz lê melhor),
em algarismos na legenda (feito pelo design system).

## Visual: design system de matemática
`_ferramentas/matematica.py` — **padrão para todo vídeo de matemática do Estudativo** (questões e, daqui em diante, aulas).
`from matematica import *` no visual.py dá a paleta, o layout, os componentes (`pill`, `popill`, `label`, `eq`, `board`,
`header`, `check`, `cross`, `strike`, `cartao`, `selo`), as figuras (`tri`, `quadrados`), o fundo e a legenda karaokê.
- Fundo azul-noite com papel quadriculado ciano e símbolos flutuando bem de leve; selo âmbar no canto (`selo(c, L["selo"], t)`).
- Cores com função: **âmbar** = dado do problema, **ciano** = incógnita principal / fórmula, **menta** = segunda incógnita / certo,
  **coral** = erro / descartado. Caixa com contorno colorido = resultado de um passo.
- Tela de aula: figura à esquerda (x≈520), quadro com as contas à direita (x 930–1830, y 175–905), título do passo no topo,
  legenda numa faixa escura em y=1000.

## Duas línguas, um projeto (Estudativo English = --lang en)
Nem toda questão ganha versão em inglês: só as de matemática que façam sentido fora do ENEM (o SAT é um projeto futuro).
- PT: `roteiro/cenas.py`, `audio/`, `youtube/`, `final/estudativo_questao_NNN_<...>.mp4`
- EN: `roteiro/cenas_en.py` (mesmos ids, blocks e cues), `audio_en/`, `youtube_en/`, `final/..._en.mp4`
- Textos da tela no dicionário `T` do visual.py, em pares (inglês, português); `IDIOMAS_NO_CODIGO = True` (sem textos_en.py).
- `youtube/capa.py` gera as capas dos dois idiomas.

## Produção
```bash
F=_ferramentas; Q=canais/enem/questoes/NNN_x
python $F/narracao.py $Q [--lang en]                  # voz provisória (prévia)
# voz final, 2 partes (corte = cena do meio): roteiro/roteiro_para_gravar[_en].txt
python $F/gerar_voz_local.py $Q <corte> 1 [--lang en]
python $F/gerar_voz_local.py $Q <corte> 2 [--lang en]
python $F/transcrever_palavras.py $Q/analise/voz.json <parte_1.wav> <parte_2.wav> [--lang en]
python $F/voz_externa.py $Q $Q/analise/voz.json <parte_1.wav> <parte_2.wav> [--lang en]
python $F/render.py $Q --video --final --jobs 4 [--lang en]
python $Q/youtube/capa.py
```
Som: `SOM = dict(intro=False, ganho_trilha=0.20, lufs=-14, ...)`; poucos efeitos, só nos resultados (dicionário `sfx`).
