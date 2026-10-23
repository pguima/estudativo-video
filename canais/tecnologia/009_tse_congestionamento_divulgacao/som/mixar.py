"""Mix final (sem mexer em _ferramentas): vídeo mudo do render + narração + trilha (com ducking pela voz) + efeitos.

Uso: python3 som/mixar.py
Pré-requisitos: render.py <proj> --video --final (gera trabalho/video_mudo.mp4) e som/gerar_som.py.
Sobrescreve final/tecnologia_009_tse_congestionamento_divulgacao.mp4 com o áudio mixado e mede os níveis.
"""
import subprocess
from pathlib import Path

EP = Path(__file__).resolve().parents[1]
OUT = EP / "final" / "tecnologia_009_tse_congestionamento_divulgacao.mp4"
G_TRILHA = 0.42   # trilha v3 (-18.4 LUFS) → ~ -26 LUFS antes do ducking (voz -16.5); abaixa mais quando a voz entra
G_SFX = 0.6

F = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
fc = (f"[1:a]{F},asplit=2[v][vk];"
      f"[2:a]{F},volume={G_TRILHA}[m];"
      f"[m][vk]sidechaincompress=threshold=0.02:ratio=5:attack=40:release=700:makeup=1[md];"
      f"[3:a]{F},volume={G_SFX}[sx];"
      f"[v][md][sx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.93:level=false[a]")
cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(EP / "trabalho" / "video_mudo.mp4"), "-i", str(EP / "audio" / "narracao.wav"),
       "-i", str(EP / "som" / "trilha.wav"), "-i", str(EP / "som" / "sfx.wav"), "-filter_complex", fc,
       "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest",
       "-movflags", "+faststart", str(OUT)]
subprocess.run(cmd, check=True)
print("FINAL:", OUT)
