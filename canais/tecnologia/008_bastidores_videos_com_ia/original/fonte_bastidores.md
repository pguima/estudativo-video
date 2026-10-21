# Fonte — Tecnologia 008: bastidores (como os vídeos dos canais são feitos com IA)

Consulta em 19/10/2026, direto no projeto `videos_canal/` (não é fonte externa: é o próprio pipeline).

## Números (contados por script)
- Vídeos finais prontos: **53** (`canais/*/.../final/*.mp4`, sem os antigos) — ENEM 30 · Seguridade Social 12 · Tecnologia 7 · Trading 2.
- Duração somada: **~6,96 h** (ffprobe).
- `visual.py` de todos os vídeos somados: **~32 mil linhas**.
- Ferramentas compartilhadas (`_ferramentas/`): motor.py 504 · tech.py 410 · aula.py 220 · voz_externa.py 192 · render.py 169 ·
  gerar_voz_local.py 42 · transcrever_palavras.py 12 linhas.

## Etapas e ferramentas (como estão no código)
1. **Roteiro**: o Claude Code lê o material de estudo (HTML/MD) e escreve `roteiro/cenas.py` — lista de cenas com
   `{cue}` (gatilho de animação), `*texto*` (destaque na legenda) e `[p=0.4]` (pausa). Citações conferidas por script contra o original.
2. **Voz**: Gemini TTS Studio (app local do usuário, `http://localhost:3000`, Express + Vite, chave do Gemini no `.env`).
   `gerar_voz_local.py` manda o texto em 2 partes: voz **Neno**, sotaque neutro, tags de emoção + instrução de estilo (`VOZ` no cenas.py).
   Modelo principal `gemini-3.8-flash-tts`; se o servidor cair para o `...-lite-tts` (voz diferente), o script pede de novo.
   Problemas reais já vistos: trecho lido duas vezes, frases improvisadas, recusa de um trecho (erro 502), cota diária gratuita.
3. **Transcrição**: `faster-whisper`, modelo **small**, CPU, int8, `word_timestamps=True` → tempo de cada palavra.
   Diff roteiro × transcrição (difflib) acha repetição/improviso. O Whisper às vezes pula alguns segundos de fala
   (caso real na Aula 11 de Seguridade: 7 s) → retranscrever só o trecho.
4. **Alinhamento**: `voz_externa.py` casa as palavras do roteiro com os tempos falados, insere silêncios e gera
   `audio/narracao.wav` + `audio/tempos.json` (início de cada cena, cada cue e cada palavra).
5. **Animação**: `roteiro/visual.py` — uma função por bloco, `(canvas, t, cues)` → desenha o quadro com **Skia** (skia-python).
   Componentes: `motor.py` (temas, cartões, legenda palavra a palavra), `aula.py` (questão, CTA), `tech.py` (visual futurista).
6. **Render**: `render.py` — 30 fps, 1920x1080; segmentos de 20 s em processos paralelos; cada processo envia os quadros
   crus para o **ffmpeg** (libx264); no fim junta os segmentos e a narração. Máquina com 7,9 GB de RAM: `--jobs 3`
   (com 7 processos deu MemoryError em 06/10).
7. **Prévia**: quadros de cada cena (`--stills`) montados numa folha de contato com ffmpeg `tile` para revisão.
8. **Capas e publicação**: `youtube/capa.py` (3 capas 1280x720) e `publicacao.md` (títulos, descrição, capítulos a partir do tempos.json).
- Guias de estilo por canal: `ESTILO_COMUM.md` + `canais/<canal>/ESTILO.md`. Sem música; voz sintética declarada no YouTube Studio.
