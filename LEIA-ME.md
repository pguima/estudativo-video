# Vídeos do canal — organização

> **Registro de todos os vídeos criados:** [REGISTRO_DE_VIDEOS.md](REGISTRO_DE_VIDEOS.md) (+ `registro_videos.csv`). Atualize com `python _ferramentas/registrar_videos.py`.

> **Guias de estilo (ler antes de editar qualquer vídeo):** [ESTILO_COMUM.md](ESTILO_COMUM.md) (regras de todos os canais)
> + `canais/<canal>/ESTILO.md` ([trading](canais/trading/ESTILO.md) · [enem](canais/enem/ESTILO.md) · [seguridade_social](canais/seguridade_social/ESTILO.md)).

```
videos_canal/
├── ESTILO_COMUM.md            regras de estilo comuns a todos os canais
├── _ferramentas/               ferramentas compartilhadas por todos os canais
│   ├── motor.py                estilo visual (temas claro/escuro, cartões, legenda animada, gráficos)
│   ├── aula.py                 componentes de aula (questão, resolução, frações, ondas, encerramento)
│   ├── tech.py                 visual futurista do canal tecnologia (fundo animado, HUD, painéis neon)
│   ├── render.py               renderiza 1920x1080 (prévias, segmentos e versão final)
│   ├── narracao.py             narração TTS provisória (edge-tts)
│   ├── transcrever_palavras.py transcreve a sua voz com o tempo de cada palavra (Whisper)
│   ├── voz_externa.py          sincroniza a sua voz (vozgen/Gemini) com o roteiro
│   ├── transcrever.py · musica.py · prever.sh
│   ├── fontes/                 fonte Inter
│   └── amostras_voz/           amostras de vozes testadas
└── canais/
    ├── trading/                canal de trading (ICT / smart money) · ESTILO.md
    ├── enem/                   canal de estudos para o ENEM (Física, Matemática, Química e Geografia) · ESTILO.md
    ├── seguridade_social/      canal de Seguridade Social (concurso INSS) · ESTILO.md
    └── tecnologia/             canal de tecnologia (IA, dev, ferramentas) · ESTILO.md
        └── PLANO_DE_VIDEOS.md      como o material foi dividido em vídeos
```

## Projetos por canal

| Canal | Pasta | Vídeo | Tema visual |
|---|---|---|---|
| Trading | `canais/trading/001_2tVWDa3uXQw` | Fair Value Gap (refeito do YouTube) | claro |
| Trading | `canais/trading/002_videoplayback1` | Candle Range Theory (roteiro novo) | escuro |
| ENEM | `canais/enem/003_enem_fisica_grandezas` | Física: grandezas, unidades e notação científica | claro |
| ENEM | `canais/enem/004_enem_fisica_ondas` | Física: ondas, características e classificação | claro |
| ENEM | `canais/enem/005_enem_fisica_fenomenos_ondulatorios` | Física: fenômenos ondulatórios | claro |
| ENEM | `canais/enem/006_enem_fisica_acustica` | Física: acústica | claro |
| ENEM | `canais/enem/007_enem_fisica_doppler` | Física: efeito Doppler | claro |
| ENEM | `canais/enem/008_enem_fisica_espectro` | Física: espectro eletromagnético | claro |
| ENEM | `canais/enem/009_enem_fisica_vetores` | Física: vetores e operações vetoriais | claro |
| ENEM | `canais/enem/010_enem_matematica_conjuntos` | Matemática: operações e conjuntos numéricos | claro |
| ENEM | `canais/enem/011_enem_quimica_materia` | Química: matéria, substâncias e misturas — **série de 6 episódios** (ver `PLANO_DA_SERIE.md`; o vídeo único antigo está em `_antigo_video_unico/`) | claro |
| ENEM | `canais/enem/012_enem_geografia_cartografia` | Geografia: cartografia — **série de 6 episódios** (ver `PLANO_DA_SERIE.md`; o vídeo único antigo está em `_antigo_video_unico/`) | claro |
| ENEM | `canais/enem/013_enem_linguagens_compreensao` | Linguagens: compreensão global e tese — **série de 7 episódios** (ver `PLANO_DA_SERIE.md`) | claro |
| ENEM | `canais/enem/014_enem_redacao_leitura_proposta` | Redação: leitura da proposta — **série de 6 episódios** (ver `PLANO_DA_SERIE.md`) | claro |
| Seguridade Social | `canais/seguridade_social/001_conceito_e_tripe` | 001: conceito e tripé (M01) — plano em `PLANO_DE_VIDEOS.md` | claro verde-petróleo (`set_theme("seguridade")`) |
| Seguridade Social | `canais/seguridade_social/002_principios_parte1` | 002: princípios parte 1 — incisos I a III (M02) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/003_principios_parte2` | 003: princípios parte 2 — incisos IV a VII (M02) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/004_financiamento_fontes` | 004: financiamento — fontes do art. 195 (M03) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/005_contrapartida_orcamento` | 005: contrapartida, noventena, imunidade e orçamento — §§ do art. 195 (M03) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/006_saude_sus` | 006: saúde e SUS na Constituição — arts. 196 a 200 (M04) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/007_assistencia_loas` | 007: assistência social e LOAS — arts. 203 e 204 + Lei 8.742 (M05 §1–3) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/008_bpc_auxilio_inclusao` | 008: BPC e auxílio-inclusão — LOAS arts. 20, 21, 21-A e 26-A (M05 §4–6) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/009_previdencia_rgps_art201` | 009: previdência social e RGPS — CF, art. 201 (M06) · fim da temporada 1 | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/010_estrutura_rgps` | 010: a estrutura do RGPS — segurados, dependentes e prestações (M07) · abre a temporada 2 · PDF no CTA | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/011_empregado_domestico_avulso` | 011: empregado, empregado doméstico e avulso — art. 11, I, II e VI (M08) | claro verde-petróleo |
| Seguridade Social | `canais/seguridade_social/012_contribuinte_individual` | 012: contribuinte individual — art. 11, V (M09, parte 1) | claro verde-petróleo |
| Tecnologia | `canais/tecnologia/001_rea_engenharia_reversa` | 001: REA — engenharia reversa com agentes de IA (github.com/morluto/rea) | **futurista escuro** (`import tech`) |
| Tecnologia | `canais/tecnologia/008_bastidores_videos_com_ia` | 008: bastidores — como os vídeos dos canais são feitos com IA | futurista escuro |

## Dentro de cada projeto (vídeo)
```
<projeto>/
├── original/      material de origem (vídeo ou HTML/MD do estudo)
├── roteiro/       cenas.py (roteiro com marcações) · visual.py (animações) · roteiro_para_gravar.txt
├── audio/         narração final, tempos e a voz enviada (nova_voz/)
├── trabalho/      segmentos intermediários (pode apagar depois de pronto)
├── final/         ★ VÍDEO PRONTO PARA O YOUTUBE
└── youtube/       capas (capa_*.jpg), capa.py e publicacao.md (título, descrição, capítulos, tags)
```

## Fluxo de produção
```bash
# 1) roteiro pronto → texto para gerar a voz:   <projeto>/roteiro/roteiro_para_gravar.txt
# 2) com os áudios da voz:
python _ferramentas/transcrever_palavras.py <projeto>/analise/nova_voz_palavras.json parte_1.wav parte_2.wav
python _ferramentas/voz_externa.py <projeto> <projeto>/analise/nova_voz_palavras.json parte_1.wav parte_2.wav
# 3) renderizar (máquina com 8 GB de RAM: no máximo 4 processos)
python _ferramentas/render.py <projeto> --video --final --jobs 4
#    se der falta de memória: refaz só o que faltou
python _ferramentas/render.py <projeto> --video --final --jobs 3 --retomar
# 4) capas
python <projeto>/youtube/capa.py
```
Tema escuro/claro: `motor.set_theme("escuro")` no topo do `roteiro/visual.py`.
