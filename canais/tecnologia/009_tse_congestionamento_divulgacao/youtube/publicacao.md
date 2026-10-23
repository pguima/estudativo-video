# Publicação no YouTube — Tecnologia · vídeo 009: O que aconteceu com o sistema do TSE durante a divulgação dos votos?

**Arquivo do vídeo:** `final/tecnologia_009_tse_congestionamento_divulgacao.mp4` (3:18, 1920x1080, tema futurista escuro)
**Canal:** Tecnologia (IA, desenvolvimento, ferramentas) · formato **minidocumentário jornalístico**
**Narração:** Gemini TTS Studio local (voz Neno, sotaque neutro, tags confiante + formal, instrução "locutor de minidocumentário: grave, investigativo, sem alarmismo")
**Roteiro:** texto do usuário (cenas 01–06, literal) + frases curtas com fatos verificados (data, 19h/64% → 20h/84%, cerca de 1 hora, nome do ministro, citação, escopo segundo o TSE, ausência de relatório técnico público até 22/10/2026)
**Fonte:** `original/fonte_tse_congestionamento.md` (consulta em 22/10/2026)
**Imagens:** só motion graphics do canal. Tela de resultados congelada e boletim de urna = **reconstrução ilustrativa** (com selo na tela); gráfico de fluxo de dados = **ilustrativo, sem escala real**. Declarações reais em cartões com autor, data e veículo.
**Som:** trilha e efeitos sintetizados no próprio projeto (`som/gerar_som.py`), mix com `som/mixar.py`.

## Capa (escolha 1)
| Arquivo | Ideia |
|---|---|
| `capa_A_o_que_aconteceu.jpg` | **Recomendada.** "O que aconteceu com o sistema DO TSE?" + tela de totalização congelada em 64% (selo "reconstrução ilustrativa") |
| `capa_B_uma_hora.jpg` | O dado concreto: "Cerca de 1 hora sem atualizar: 64% → 84%" + painel 19h → 20h |
| `capa_C_contagem_parou.jpg` | A dúvida do público: "A contagem dos votos PAROU?" + apuração → totalização → divulgação |

Use o "Testar e comparar" com as três.

---

## Título (escolha 1; até 70 caracteres)
1. **O Que Aconteceu com o Sistema do TSE na Divulgação dos Votos?** ← recomendado (com capa A)
2. TSE Travou em 64%: o Que Explica a 1 Hora Sem Atualização? (com capa B)
3. A Contagem dos Votos Parou? Entenda o Congestionamento no TSE (com capa C)
4. Congestionamento no TSE: Falha Técnica, o Que Se Sabe e o Que Falta

---

## Descrição (copie e cole)

```
No domingo, 4 de outubro de 2026, primeiro turno das eleições, a divulgação dos resultados ficou parada: por volta das 19h, a totalização para presidente estava em 64% e só voltou a andar por volta das 20h, já em 84%. O TSE atribuiu o atraso de cerca de uma hora a um congestionamento no sistema de divulgação. Neste minidocumentário, a gente separa o que foi confirmado, o que é diferente entre apuração, totalização e divulgação, e as perguntas técnicas que ainda estão em aberto.

📌 O que você vai ver:
✅ A linha do tempo: 19h → 20h, de 64% para 84% (registros: 64,81% às 19h06 e 84,96% às 20h08)
✅ A explicação oficial: fluxo de dados acima do normal, protocolo de segurança e checagem dos sistemas em sequência
✅ Apuração, totalização e divulgação: três etapas diferentes, segundo o próprio TSE
✅ Por que uma falha de divulgação não é o mesmo que alteração de dados
✅ As declarações do presidente do TSE, com fonte e data
✅ O que ainda não foi explicado publicamente

⏱️ Capítulos
00:00 O que aconteceu?
00:18 O congestionamento
00:40 Linha do tempo: 64% → 84%
01:02 A contagem dos votos parou? Três etapas
01:23 Falha na tela não é voto perdido
01:37 Houve fraude? Separando os fatos
02:00 As perguntas em aberto
02:26 Transparência, segurança, informação
02:52 Até o próximo vídeo
03:08 Fontes

📋 Resumo rápido:
• Quando: 04/10/2026, 1º turno das Eleições 2026
• O quê: a totalização para presidente ficou parada em ~64% por volta das 19h e voltou por volta das 20h, em ~84% (atraso de cerca de 1 hora, segundo o presidente do TSE)
• Causa informada: congestionamento no sistema responsável pela divulgação, com fluxo de dados acima do normal; protocolo de segurança acionado
• Segundo o TSE: a dificuldade ficou restrita à divulgação e não afetou a totalização
• Em aberto: a origem do fluxo acima do normal; não encontramos relatório técnico público detalhando o incidente até 22/10/2026

🖼️ Sobre as imagens: tudo é motion graphics do canal. A tela de resultados congelada e o boletim de urna são reconstruções ilustrativas, e o gráfico de fluxo de dados é ilustrativo (sem escala real). A narração usa voz sintética (IA).

📰 Fontes (consultadas em 22/10/2026):
• TSE — Presidente do TSE conclui 1º turno das Eleições 2026 e projeta mesma tranquilidade para segunda fase do pleito (04/10/2026): https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/presidente-do-tse-conclui-1o-turno-das-eleicoes-2026-e-projeta-mesma-tranquilidade-para-segunda-fase-do-pleito
• TSE — Saiba como foi a totalização dos votos no 1º turno das Eleições 2026 (out/2026): https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/saiba-como-foi-a-totalizacao-dos-votos-no-1o-turno-das-eleicoes-2026
• TSE — Entenda a diferença entre apuração e totalização de votos (out/2026): https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/entenda-a-diferenca-entre-apuracao-e-totalizacao-de-votos
• Agência Brasil — Congestionamento no sistema de dados gerou atraso na apuração, diz TSE (04/10/2026): https://agenciabrasil.ebc.com.br/justica/noticia/2026-10/congestionamento-no-sistema-de-dados-gerou-atraso-na-apuracao-diz-tse
• Brasil 61 — Congestionamento de dados atrasa divulgação dos resultados das eleições, diz TSE (04/10/2026): https://brasil61.com/n/congestionamento-de-dados-atrasa-divulgacao-dos-resultados-das-eleicoes-diz-tse-bras2617219
• CNN Brasil — TSE registrou congestionamento no sistema de divulgação, diz Nunes Marques (04/10/2026): https://www.cnnbrasil.com.br/eleicoes/tse-registrou-congestionamento-no-sistema-de-divulgacao-diz-nunes-marques/
• Jornal do Brasil — Apuração do primeiro turno sofre atraso após problema no sistema do TSE (05/10/2026): https://www.jb.com.br/brasil/politica/2026/10/1061122-tse-confirma-atraso-na-totalizacao-dos-votos-e-explica-causa.html
• SBT News — TSE atribui atraso na apuração a congestionamento de dados (05/10/2026): https://sbtnews.sbt.com.br/noticia/eleicoes/tse-atribui-atraso-na-apuracao-a-congestionamento-de-dados
• Canaltech — Por que os resultados do 1º turno das eleições travaram por mais de 1 hora (05/10/2026): https://canaltech.com.br/mercado/por-que-os-resultados-do-1-turno-das-eleicoes-travaram-por-mais-de-1-hora/
• SpaceMoney — Falha no sistema de divulgação atrasa apuração do 1º turno (05/10/2026): https://www.spacemoney.com.br/politica/tse-congestionamento-atraso-divulgacao-primeiro-turno

👍 Se esse vídeo te ajudou a entender o caso, deixe seu like, inscreva-se e ative o sininho para não perder os próximos vídeos.
💬 Comente: qual dessas perguntas você gostaria de ver respondida?

#Tecnologia #Eleicoes2026 #TSE
```

---

## Tags
```
tse, eleições 2026, divulgação dos resultados, totalização dos votos, apuração, congestionamento de dados, atraso na apuração, sistema do tse, urna eletrônica, boletim de urna, kassio nunes marques, primeiro turno, segurança eleitoral, transparência, infraestrutura de ti, sobrecarga de sistema, tecnologia, minidocumentário
```

## Hashtags
`#Tecnologia #Eleicoes2026 #TSE` (o canal usa `#InteligenciaArtificial #Programacao`; aqui o tema não é IA nem programação, por isso foram trocadas)

---

## Comentário fixado
```
🗓️ 04/10/2026 · 1º turno
⏸️ ~19h: totalização para presidente parada em 64%
▶️ ~20h: retomada, já em 84% (cerca de 1 hora de atraso)
🧩 Apuração (urna) ≠ totalização (soma) ≠ divulgação (tela)
🔎 Segundo o TSE: problema na divulgação, sem afetar a totalização
❓ Em aberto: a origem do fluxo de dados acima do normal

📰 Todas as fontes, com links e datas, estão na descrição.
👇 Qual dessas perguntas você gostaria de ver respondida?
```

---

## Configurações no YouTube Studio
| Campo | Valor |
|---|---|
| Público | **Não, não é conteúdo para crianças** |
| Categoria | **Notícias e política** (ou Ciência e tecnologia) |
| Idioma do vídeo / título | Português (Brasil) |
| Legendas | Já estão na imagem; ative também as automáticas |
| Conteúdo alterado ou sintético | **Sim** — narração com voz sintética; reconstruções ilustrativas (sinalizadas na tela) |
| Data de publicação | 18h–21h em dia útil |
| Observação | Tema eleitoral: o YouTube pode exibir painel informativo; não há afirmações de fraude no vídeo |

## Playlist
Nova: **"Tecnologia explicada: casos reais"** (ou "Tecnologia e sociedade").

## Tela final (últimos 20 s, a partir de 02:58)
- **Inscrever-se** à esquerda
- **Vídeo**: o mais recente do canal (ex.: 008, bastidores)
- Atenção: a tela de **Fontes** (03:08–03:18) deve continuar legível — deixe os elementos da tela final no lado direito/superior

## Cards
- 01:02 (três etapas): link para a página do TSE "Entenda a diferença entre apuração e totalização" na descrição (cards só levam a vídeos/playlists; não usar card externo)

## Ideias de Shorts
- 00:40–01:02 · "64% → 84%: a hora em que a tela do TSE parou" (linha do tempo + citação)
- 01:02–01:37 · "A contagem dos votos parou? Apuração, totalização e divulgação"
- 02:00–02:26 · "As 4 perguntas técnicas que ainda faltam responder"
