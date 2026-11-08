# Prompts do Suno: trilha do EP 01 (v2, thriller financeiro)

Direção definida pelo usuário em 07/11/2026: piano misterioso e pulsos no começo, suspense crescendo, piano e cello melancólicos na fase difícil da família, esperança frágil perto do fim e final em tensão sem resolução. Nada de música corporativa nem efeitos de trailer de ação. Substitui a versão de 10 blocos com cara de trailer de herói.

Episódio com 12min16s, dividido em 3 fases pelos tempos de `output/planos.json`. Cada prompt pede um pouco mais que o trecho, para sobrar margem no corte.

## Como gerar

- Ligue **Instrumental** e deixe o campo de letra vazio.
- Cole o texto de **Style** no campo de estilo e use o **Título** para achar a faixa depois.
- Faixa mais longa que a fase não é problema: eu corto. Faixa mais curta precisa ser estendida no Suno até passar da duração.
- Baixe em WAV, se o plano permitir. Se não, MP3 serve.
- Salve em `som/suno/` com o nome indicado em cada fase (`p1.wav`, `p2.wav`, `p3.wav`).

Sting, batidas, sino, tique-taque e pratos pontuais continuam vindo de `som/efeitos.wav`.

## P1. A queda (0:00 a 4:37, 277 s): `p1.wav`

Da abertura ao pânico do cancelamento (4:11). Precisa de pelo menos 4min40s.

**Título:** STH01 P1 The Fall

**Style:**
```
Cinematic financial thriller score, instrumental, no vocals, D minor, mysterious solo piano, dark ambient synths, subtle electronic pulses, slowly building suspense, deep sub bass, ticking rhythms, tense staccato strings, restrained cinematic percussion, dark peak near the end, premium film score, sophisticated sound design, subtle beneath narration, no corporate music, no trailer effects
```

## P2. A luta da família (4:37 a 9:54, 317 s): `p2.wav`

Da conta na mesa à briga do dia 24. Precisa de pelo menos 5min20s.

**Título:** STH01 P2 Family Struggle

**Style:**
```
Cinematic financial thriller score, instrumental, no vocals, D minor, melancholic felt piano, expressive solo cello, soft sustained strings, low anxious pulse, faint ticking rhythm, dark ambient texture, emotional depth and quiet anxiety, restrained tension swells, premium film score, subtle beneath narration, no corporate music, no trailer effects, no big drums
```

## P3. Esperança frágil e novo perigo (9:54 a 12:16, 142 s): `p3.wav`

Do alívio no banco ao cartão do próximo episódio. Precisa de pelo menos 2min30s. A virada para o escuro deve vir perto de 1min50s (o "next" começa em 11:56).

**Título:** STH01 P3 Fragile Hope

**Style:**
```
Cinematic financial thriller score, instrumental, no vocals, warm piano and subtle orchestral strings, fragile hope and resilience, then turns dark near the end, low pulsing bass, ticking rhythm, rising tense strings, finishes on dark unresolved suspended chord, foreshadowing another crisis, premium film score, subtle beneath narration, no corporate music, no trailer effects, no happy resolution
```

Se o Suno resolver o acorde ou fizer fade no final, eu corto no ponto de maior tensão.
