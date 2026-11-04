# Série "Top 10 projetos do GitHub" (canal Tecnologia)

Uma lista por episódio com os 10 repositórios que **mais ganharam estrelas no mês** (GitHub Trending, filtro *monthly*),
em contagem regressiva do 10º ao 1º. Pasta de cada episódio: `canais/tecnologia/NNN_top10_github_epXX/`.

## Registro (não repetir)
Todo projeto que entra num episódio vai para [`top10_github_registro.csv`](top10_github_registro.csv)
(episódio, data, posição, repositório, **versão no dia**, estrelas, ganho no mês, licença).

**Regra:** um repositório já registrado **só volta** se tiver uma **versão nova importante** desde o episódio em que
apareceu: mudou o número principal (ex.: `v2.2.3` → `v3.0`), ou, em projetos versionados por data/sem release, saiu
um lançamento anunciado como grande. Nesse caso ele entra como **"atualizado"**, e o roteiro fala só do que mudou.

## Como montar o próximo episódio
```bash
python3 canais/tecnologia/top10_github.py            # baixa o Trending mensal e filtra pelo registro
python3 canais/tecnologia/top10_github.py --registrar 02 013_top10_github_ep01   # depois de fechar o roteiro
```
O script lista os candidatos em ordem de ganho de estrelas e marca `NOVO`, `ATUALIZADO (vX → vY)` ou `REPETIDO` (fica de fora).
Pegue os 10 primeiros que não são `REPETIDO`, leia o README de cada um e guarde em `original/` (dados da API + data da consulta).

## Roteiro (padrão da série)
- Gancho com o número do 1º lugar sem dizer o nome → critério (estrelas ganhas no mês, data da consulta) → 10 a 1 →
  resumo em uma tela com os 10 → CTA com a pergunta "qual você vai testar primeiro?".
- Cada projeto ~30 s: **o que é** em uma frase, **um número ou exemplo concreto do README**, **comando de instalação**
  na tela exatamente como se digita, **licença**. Cuidados quando houver (clonagem de voz, segurança, pacotes falsos).
- Estrelas: na fala, arredondadas por extenso ("cinquenta e três mil"); na tela, o número exato.

## Visual (padrão desde 2026-10-28): tema `tech` sem roxo + 3D onde carrega informação
Modelo: `013_top10_github_ep01/roteiro/visual.py`. Mantém o visual HUD do canal (`tech.py`), com dois ajustes:
- **Sem degradê roxo** (o usuário vê como "padrão de IA"): no `visual.py`, `tech.ACENTO2 = "#34D399"` (esmeralda),
  `tech.BASE = ("#0A1A26", "#040A10", "#010305")` (fundo mais escuro, mais contraste) e `tech.ORB_A = 0.16`.
  Projetos e painéis usam ciano, laranja `#FB923C`, magenta, verde, âmbar, rosa — **nunca `VIOLET`**.
- **3D com `_ferramentas/tech3d.py`** só onde ajuda: a posição do ranking extrudada girando com reflexo
  (`extrude` + `spin_in`), a estrela do gancho (`star3d`), o "10 → 1". O #1 vem em dourado.
- **Não usar** piso de quadradinhos em perspectiva nem fundo preto chapado: o usuário achou "serrilhado" e "simples"
  (tentativa rejeitada em 28/10/2026).

## Episódios
| Ep | Data | Pasta | Roteiro (doc) |
|---|---|---|---|
| 01 | 2026-10-27 | `013_top10_github_ep01` | https://claude.ai/artifact/NRfn1JsKKyQNxE83KH427u (copiar) · vídeo: https://claude.ai/artifact/KYs7wpSFckxtCtg7kU2vci |
