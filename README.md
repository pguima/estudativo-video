# estudativo-video

Roteiros, animações e ferramentas dos vídeos do canal **Estudativo** (ENEM, concursos/Seguridade Social, trading e tecnologia).
Cada vídeo é gerado por código: roteiro com marcações → narração (Gemini TTS) → sincronização palavra a palavra → animação em
Python/skia → render com ffmpeg.

## Estrutura
```
_ferramentas/   motor visual (motor.py, aula.py, tech.py), render, voz, transcrição, fontes Inter (TTF)
canais/<canal>/NNN_<slug>/[epN_<tema>/]
    roteiro/    cenas.py (texto + marcações) · visual.py (animações) · roteiro_para_gravar.txt
    audio/      tempos.json (tempo de cada cena/palavra)
    youtube/    capa.py, capas .jpg, publicacao.md (título, descrição, capítulos)
```
Guias: [LEIA-ME.md](LEIA-ME.md) (fluxo de produção), [ESTILO_COMUM.md](ESTILO_COMUM.md) e `canais/<canal>/ESTILO.md`.
Registro de todos os vídeos: [REGISTRO_DE_VIDEOS.md](REGISTRO_DE_VIDEOS.md).

## Fora do repositório
Vídeos finais (.mp4), áudios (.wav/.mp3), segmentos de render (`trabalho/`), transcrições (`analise/`) e PDFs ficam no disco e no
backup (ver `.gitignore`). Para re-renderizar um vídeo é preciso a narração (`audio/narracao.wav`) do backup.
A chave da API de imagens fica em `~/.config/ia-imagens.env` (nunca no repositório).
