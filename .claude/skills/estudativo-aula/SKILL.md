---
name: estudativo-aula
description: Produz uma aula do curso Estudativo a partir do id do catálogo (como MAT-FRA-009): roteiro curto, voz, animação no visual editorial da matéria, capas e arquivo de publicação. Use sempre que o usuário pedir para fazer, gerar, gravar ou produzir uma aula, vídeo ou id do Estudativo, ou a próxima aula de uma trilha, mesmo sem citar a skill. Não use para Shorts, para os canais de Tecnologia, Seguridade e Survive the Headline, nem para as séries antigas de canais/enem.
---

# Produzir uma aula do Estudativo

Cada pedido vira um vídeo pronto para publicar. O padrão foi aprovado no piloto `canais/estudativo/aulas/MAT-FRA-008/`: leia o `roteiro/cenas.py` e o `roteiro/visual.py` dele antes de escrever os seus, porque são o melhor exemplo do nível esperado.

Leia também `canais/estudativo/ESTILO.md`.

O projeto antigo falhou por dois motivos: aulas prolixas e conteúdo usado antes de ser ensinado. Quase tudo abaixo existe para evitar esses dois erros.

## Preparação

Comandos a partir de `_ferramentas/`, com o Python que tem skia e faster_whisper:

```bash
export PYTHONUTF8=1
PY=/c/Users/Paulo/AppData/Local/Python/pythoncore-3.14-64/python.exe
A=../canais/estudativo/aulas/<id>
```

## Aula com material pronto, sem voz

Se a pasta já tiver `roteiro/visual.py` e `youtube/` e a ficha marcar `roteiro`, comece no passo 4. Depois da voz, olhe um quadro por cena, porque o `visual.py` foi testado com tempos provisórios (`tempos_sinteticos.py`). Renderize, troque `[DURAÇÃO]` e cada `[TEMPO]` do `publicacao.md` pelos valores de `audio/tempos.json` e siga para o passo 8.

## 1. Ficha

```bash
cd canais/estudativo/catalogo && py ficha_aula.py <id>
```

A ficha traz a habilidade, os pré-requisitos, a próxima aula e as playlists. Ela é o limite do roteiro: o que não estiver em "Já ensinado" só pode ser citado como assunto de outra aula.

Se o id não existir, mostre ao usuário as aulas de nome parecido em `aulas.csv` e pare.

## 2. Roteiro

Siga `references/roteiro.md` e grave `$A/roteiro/cenas.py`. Conteúdo de apoio: `C:\Users\Paulo\Documents\Claude\Projetos\Estudos\Enem\estudos\` (arquivos `.html`, não os `.src.html`), extraídos com `extrair_material.py`. É só consulta: não copie a divisão de seções. Não use `canais/enem/` como modelo.

Conte as palavras com `$PY roteiro_txt.py $A`.

## 3. Conferência antes da voz

A voz gasta cota, então os erros precisam morrer aqui.

1. Refaça cada conta do roteiro.
2. Chame um revisor independente (subagente) com a ficha e o roteiro. Peça que leia como quem está há anos sem estudar e aponte: termo usado sem explicar, conteúdo fora de "Já ensinado", fato duvidoso, frase longa ou repetida.
3. Em matérias com pouco material (Filosofia, Inglês, Espanhol), confira os fatos em fonte externa.

Corrija e só então siga.

## 4. Voz

```bash
curl -s -m 4 -o /dev/null -w "%{http_code}\n" http://localhost:3000
```

Se não responder 200, suba o servidor em segundo plano: `npm run dev` em `C:\Users\Paulo\Downloads\audio2-main\audio2-main`.

```bash
$PY gerar_voz_local.py $A zz 1
$PY transcrever_palavras.py $A/audio/nova_voz/palavras.json $A/audio/nova_voz/parte_1.wav
$PY voz_externa.py $A $A/audio/nova_voz/palavras.json $A/audio/nova_voz/parte_1.wav
```

A saída 3 de `gerar_voz_local.py` significa que a cota acabou. Ela renova por volta de 04:00 de Brasília: marque a aula como `roteiro`, avise o usuário e pare, porque o modelo `lite` tem outra voz.

Compare a transcrição com o roteiro. Sinônimo que não muda o sentido pode passar, mas avise. Número, conta ou fato trocado obriga a regerar. A transcrição costuma inventar um "e" em leituras como "sete doze avos": antes de regerar, transcreva o trecho isolado.

## 5. Visual

Siga `references/visual.md` e grave `$A/roteiro/visual.py`. Confira com quadros parados antes do vídeo, porque o render custa minutos e o quadro custa segundos:

```bash
$PY render.py $A --stills 5,20,45
```

Abra os PNGs de `$A/trabalho/stills/`. Procure: tela vazia por muitos segundos, texto pequeno para celular, sobreposição, elemento que aparece antes da fala. Quase todo defeito aparece aqui.

## 6. Render

```bash
rm -rf $A/trabalho/segmentos
$PY render.py $A --video --final --jobs 4
```

Rode em segundo plano. Máximo de 4 jobs, porque a máquina tem 7,9 GB de memória. Depois confira duração e áudio com `ffprobe` e extraia quadros do mp4 final, incluindo as transições.

## 7. Capas e publicação

- `$A/youtube/capa.py`: três capas no modelo do piloto, em 1280x720.
- `$A/youtube/publicacao.md`: copie a estrutura do piloto. Capítulos saem de `audio/tempos.json`; playlists saem da ficha. Títulos sem a palavra ENEM; a descrição cita as provas.
- Aula ainda não publicada entra como `[LINK <id>]`.

## 8. Fechar

```bash
cd canais/estudativo/catalogo && py ficha_aula.py <id> --marcar pronto
```

Marque também as etapas intermediárias (`roteiro`, `voz`, `render`), para que uma sessão futura saiba onde parou.

Relate ao usuário: o link do vídeo, a duração, as mudanças que a voz fez, o que não foi conferido e os `[LINK]` pendentes. Você não ouve o áudio, então a avaliação da voz é do usuário: diga isso. Não faça commit sem pedido.

Se pedirem várias aulas, a cota de voz manda: cerca de 2 por dia, às vezes 5. Faça roteiro e conferência de todas e gaste a voz na ordem que o usuário escolher.
