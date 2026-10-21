# Fonte — Claude Dashboards (Anthropic)

Consultado em 15/10/2026. Página oficial da Anthropic não acessada diretamente; fatos cruzados em coberturas do anúncio:
- https://www.unite.ai/anthropic-launches-claude-dashboards-and-motion-takes-docs-out-of-beta/
- https://www.eesel.ai/blog/claude-dashboards-review (resume a central de ajuda)
- https://www.digitaltrends.com/computing/claude-can-now-build-live-dashboards-and-animated-explainers-from-your-data/
- https://tabulareditor.com/blog/what-are-claude-dashboards
- https://thenewstack.io/claude-dashboards-data-motion/

## Fatos usados no roteiro
- Lançado em 08/10/2026, em beta, junto com o Claude Motion. Fica na aba Artifacts, ao lado de Docs, Slides e Design.
- Planos pagos. No Enterprise vem desligado; o admin liga em Configurações da organização > Artifacts.
  Requer "Cloud code execution and file creation" ligado (Team/Enterprise).
- Como funciona: conecta um data warehouse ou app → pergunta em linguagem natural → "Claude writes a SQL query
  for each chart and runs it against your data source" → painel continua atualizado quando os dados mudam.
- Warehouses: Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake. Apps conectados: Salesforce (exemplo oficial).
- Transparência: cada gráfico mostra a consulta SQL e o horário da última atualização; clicar num número mostra a
  consulta, ou pedir ao Claude para explicar.
- Começar: pedir num chat, ou "Output" > "Dashboards" na caixa de mensagem, ou template na aba Artifacts.
- Refinar: pedir filtros, mudar período, abrir a consulta e dizer o que contar. Dica oficial: diga a PERGUNTA,
  não o tipo de gráfico.
- Exemplos oficiais: cadastros desta semana × mês anterior; painel das oportunidades do Salesforce.
- Levar para outras ferramentas: Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog, Sigma
  (Looker, monday.com e Tableau "em breve").
- Compartilhar: quem vê usa as PRÓPRIAS conexões (sem acesso à fonte → o gráfico dá erro). Edição em equipe junto com o Claude.
  "Qualquer pessoa com o link" não vale para artifacts conectados a apps.
- Limites/cuidados: beta; sem camada semântica (cada SQL define a métrica → "cliente ativo" pode ter definições diferentes);
  uso conta no limite do plano e o processamento do warehouse é cobrado pelo provedor; HIPAA: não coberto pelo BAA.
