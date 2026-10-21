# Publicação no YouTube — Tecnologia · vídeo 008: Bastidores (como eu faço estes vídeos com IA)

**Arquivo do vídeo:** `final/tecnologia_008_bastidores_videos_com_ia.mp4` (5:29, 1920x1080, tema futurista escuro)
**Canal:** Tecnologia (IA, desenvolvimento, ferramentas)
**Narração:** Gemini TTS Studio local (voz Neno, sotaque neutro, tags alegre + curiosa + amigável, instrução de estilo "criador apaixonado mostrando os bastidores")
**Fonte:** o próprio projeto `videos_canal/` — números contados por script em 19/10/2026; ver `original/fonte_bastidores.md`
**Observação de produção:** a voz da parte 1 improvisou ~90 s de texto que não estava no roteiro (e falso: "biblioteca Manim", "trilha licenciada", "60 fps"). O trecho foi cortado (original guardado em `audio/nova_voz/parte_1_original.wav`). Bom exemplo para um Short sobre os cuidados com voz de IA.

## Capa (escolha 1)
| Arquivo | Ideia |
|---|---|
| `capa_A_sem_camera.jpg` | **Recomendada.** "Sem câmera, sem microfone: SÓ IA" (com quadros reais dos três canais) |
| `capa_B_53_videos.jpg` | Resultado concreto: "53 vídeos feitos com CÓDIGO" |
| `capa_C_pipeline.jpg` | O pipeline: "Meu pipeline de vídeo COM IA" (Claude · Gemini · Whisper · Skia · ffmpeg) |

Use o "Testar e comparar" com as três.

---

## Título (escolha 1; até 70 caracteres)
1. **Sem Câmera, Sem Microfone: Como Eu Faço Vídeos Só com IA** ← recomendado (com capa A)
2. 53 Vídeos Feitos com Código e IA: os Bastidores do Meu Pipeline (com capa B)
3. Meu Pipeline de Vídeo com IA: Claude, Gemini, Whisper e Python (com capa C)
4. Como Automatizar Vídeos com IA e Python (Bastidores Reais)

---

## Descrição (copie e cole)

```
Este vídeo não teve câmera, microfone nem editor de vídeo: a voz, as animações e as legendas saíram de código e de IA. E ele não está sozinho: já são 53 vídeos, quase 7 horas de aula, em quatro canais. Neste vídeo eu abro os bastidores do pipeline completo, com os arquivos reais, e conto também o que deu errado pelo caminho.

📌 O que você vai ver:
✅ O roteiro: o Claude Code lê o material e escreve um arquivo Python (cenas.py) com gatilhos de animação, destaques e pausas
✅ A regra de ouro: a IA não inventa conteúdo (e um script confere as citações)
✅ A voz: Gemini TTS rodando num app local, com voz, emoção e instrução de estilo
✅ Os erros da voz de IA: trecho lido duas vezes, frase inventada, troca de modelo
✅ A transcrição com faster-whisper e o tempo exato de cada palavra
✅ Como o roteiro e a voz são alinhados para a animação cair bem na palavra
✅ A animação: cada quadro é uma função do tempo, desenhada com Skia
✅ O render: 30 quadros por segundo, pedaços de 20 s em paralelo e ffmpeg
✅ A vida real: 8 GB de memória, MemoryError e a folha de prévia
✅ Capas e descrição geradas automaticamente, e o que continua sendo decisão minha

⏱️ Capítulos
00:00 Sem câmera, sem microfone, sem editor
00:18 As cinco etapas
00:30 O roteiro: do material ao cenas.py
00:46 As marcações do roteiro
01:03 A regra de ouro: a IA não inventa
01:17 A voz: Gemini TTS no meu computador
01:37 A voz de IA apronta
01:53 Transcrição com faster-whisper
02:04 Roteiro × transcrição
02:22 O pulo do gato: cada gatilho vira um instante
02:37 A animação: o quadro é função do tempo
03:00 Cada canal, um estilo
03:20 A legenda palavra por palavra
03:29 O render: dezoito mil quadros
03:48 A vida real: oito gigas de memória
04:03 A folha de prévia
04:17 Capas e descrição
04:30 Então a IA faz tudo?
04:42 Três cuidados
04:56 Resumo
05:12 Até o próximo vídeo

📋 Resumo rápido:
• Roteiro: Claude Code → cenas.py (gatilhos, destaques e pausas)
• Voz: Gemini TTS (voz Neno), conferida sempre
• Transcrição: faster-whisper (modelo small, CPU), tempo de cada palavra
• Animação: Skia (Python), o quadro é função do tempo
• Render: ffmpeg, 30 fps, em pedaços paralelos
• 1 vídeo = 1 pasta

👍 Se esse vídeo te mostrou algo novo, deixe seu like, inscreva-se e ative o sininho para não perder as próximas ferramentas.
💬 Comente: qual etapa você quer ver em detalhe num próximo vídeo?

#Tecnologia #InteligenciaArtificial #Programacao #Python
```

---

## Tags
```
inteligência artificial, ia, criar vídeos com ia, automação de vídeo, vídeo com python, pipeline de vídeo, claude code, gemini tts, texto para fala, faster whisper, whisper, skia, ffmpeg, legenda automática, narração com ia, youtube com ia, bastidores, programação, python, tecnologia
```

## Hashtags
`#Tecnologia #InteligenciaArtificial #Programacao #Python`

---

## Comentário fixado
```
🛠️ O pipeline deste vídeo:
1️⃣ Roteiro → Claude Code (cenas.py)
2️⃣ Voz → Gemini TTS (voz Neno)
3️⃣ Transcrição → faster-whisper (tempo de cada palavra)
4️⃣ Animação → Skia (Python)
5️⃣ Render → ffmpeg

😅 Curiosidade: na primeira versão da voz, a IA improvisou 90 segundos falando de uma biblioteca que eu nem uso. Foi cortado — por isso eu sempre confiro.
👇 Qual etapa você quer ver em detalhe?
```

---

## Configurações no YouTube Studio
| Campo | Valor |
|---|---|
| Público | **Não, não é conteúdo para crianças** |
| Categoria | **Ciência e tecnologia** |
| Idioma do vídeo / título | Português (Brasil) |
| Legendas | Já estão na imagem; ative também as automáticas |
| Conteúdo alterado ou sintético | **Sim** — narração com voz sintética (o próprio vídeo fala disso) |
| Data de publicação | 18h–21h em dia útil |

## Playlist
**"Ferramentas de IA para devs"** (ou nova: **"Criar conteúdo com IA"**, se for virar série com os vídeos de TTS e Whisper).

## Tela final (últimos 20 s, a partir de 05:09)
- **Inscrever-se** à esquerda
- **Vídeo**: 007 (Remotion — vídeos com código), que conversa direto com este

## Cards
- 00:30 (roteiro): card para o **004 (Claude Code)**
- 02:37 (animação com código): card para o **007 (Remotion)**

## Ideias de Shorts
- 01:37–01:53 · "A voz de IA apronta" (+ a história real dos 90 s improvisados)
- 02:22–02:37 · "Como a animação cai bem na palavra"
- 03:48–04:03 · "MemoryError: a vida real com 8 GB"
