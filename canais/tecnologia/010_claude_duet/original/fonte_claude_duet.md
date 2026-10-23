# Fonte — Claude Duet (Tecnologia 010)

Consulta: **22/10/2026** (anúncio foi em 21/10/2026). Produto em *research preview*: tudo pode mudar.
Regra do vídeo: só entra o que está na **fonte oficial**; o que vem de uma única fonte não oficial aparece com "segundo X" ou fica de fora.

## 1. OFICIAL — Anthropic, "Introducing Claude Duet"
URL: https://claude.com/resources/articles/claude-duet (anthropic.com/news/claude-duet devolveu 404; o anúncio está no claude.com, que o CNBC também linka como "blog post" da Anthropic). Lido na íntegra via Apify web-fetch em 22/10/2026.

Trechos (tradução livre; original em inglês):
- "research preview of Claude Duet, a new app where Claude works as a proactive agent. It comes to you with what needs your attention, completes tasks you ask of it, keeps working even when you step away, and checks with you before it acts on your behalf."
- Público: "professionals and small business owners".
- Plataformas: "standalone app on iOS and Android, and on claude.ai". **(Android: confirmado na oficial.)**
- "included in Pro and Max plans and uses the same usage limits as the rest of Claude"; acesso por **lista de espera** (claude.com/product/claude-duet).
- "We designed it around **Claude Opus 5.5**" **(modelo confirmado na oficial.)**
- "Each morning, it sends you a short brief on the most important items across your connected apps. Throughout the day, it keeps tabs on those apps and messages you only when something needs your attention."
- Tarefas: "from simple administrative tasks of scheduling meetings to more complex ones, such as building dashboards with dozens of tools, creating financial or sales forecasts, prototyping, and building web apps."
- Segurança: framework de agentes confiáveis (o mesmo de Claude Code e Claude in Chrome); credenciais como no Claude Managed Agents → "never directly sees your passwords or sign-in tokens"; ações aprovadas pelo classificador do auto mode; defesas contra prompt injection; red team + pentest externo + bug bounty público.
- Informação sensível: novo classificador + system prompt de segurança que checa cada mensagem; rejeita compartilhar o nível mais restrito (número de cartão de crédito, documento de identidade); saúde e finanças pessoais só com instrução explícita. "will share more details ... in the coming days".
- Testers internos (Boris Cherny, Chelsea Larsson, Karan Ahuja) e pequenos empresários (Jess Provencher: Duet apontou visita a imóvel marcada no dia errado; Amin Ebrahimi, Shahs of Kabob, ~110 funcionários: contabilidade, atendimento, marketing, faturas loja a loja, "I don't need to open up 100 tabs"; Mya Dalton: preparou brief de reunião e notou que era logo antes do voo, ofereceu remarcar).
- Como funciona: herda **memória, skills e apps conectados** da conta Claude; conversa por **texto ou voz** num **único fio contínuo**.
- "Claude Duet has a **virtual machine with its own browser**, so it doesn't require your laptop or phone to be on." Notifica quando termina ou precisa de revisão.
- "Claude Duet checks your connected accounts **every few hours**, because checking nonstop would use up your plan's limits much faster." Dá para dizer o que quer ouvir e com que frequência.
- "before it **sends a message, makes a payment, signs a document, or deletes anything**, it shows you exactly what it's about to do and waits for your approval. A few things are **off-limits even with your approval, like trading securities or moving money between accounts**." Pode desconectar qualquer app.
- "**over 6,000 connectors and plugins** in the Claude Marketplace" **(número confirmado na oficial.)** Exemplos: Gmail e Slack (mensagens perdidas + respostas), Intuit QuickBooks ou Stripe (faturas em aberto + lembretes), Gusto (folha), LinkedIn (vaga, após edição e aprovação), Docusign, HubSpot, Canva, Shopify (editor visual "coming soon").
- Compras com **Link (carteira da Stripe)**: confirma o item, Link pede aprovação do gasto, paga com **cartão virtual**; também **Shop Pay** (Shopify). "Coming soon": login com 1Password.
- Limites: "might misread a thread or miscalibrate what's urgent"; tarefas pessoais (ex.: comprar ingressos) "aren't quite as strong"; "can't yet show you its browser"; app separado do app principal do Claude.
- Uso: checagens em segundo plano contam no limite; tarefas grandes (modelo financeiro, deck) gastam mais.
- "We're starting today with **Pro and Max users in the US**."
- **Preço:** nenhum preço próprio; incluído no Pro/Max durante a prévia. Nenhuma data de lançamento geral.

## 2. OFICIAL — posts da conta @claudeai no X (via resultado de busca, 22/10/2026)
- https://x.com/claudeai/status/2112984664256241837 — mesmo texto de abertura do anúncio.
- https://x.com/claudeai/status/2112984669943968099 — "early research preview, available through a waitlist on Pro and Max plans in the US. It can still misjudge what's urgent".

## 3. CNBC — 21/10/2026
https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html (WebFetch 403; lido via Apify)
- Duet deve competir com o **Dots, da OpenAI** ("always-on agents", apresentado no DevDay, semanas depois do Muse) e o **Muse, da Meta** ("personal AI agent", lançado no mês anterior, chegou ao topo da App Store).
- Meta mira mais consumidores; o produto da OpenAI fica entre empresas e consumidores; Duet é focado em trabalho.
- Zuckerberg: mais de 10 milhões de pessoas nos EUA e Canadá configuraram agentes Muse em um mês e meio (não usado no vídeo).

## 4. TechCrunch — 22/10/2026
https://techcrunch.com/2026/10/22/claude-duet-app-is-anthropics-bet-on-agents/
- iOS, Android e web; Pro e Max; lista de espera; Opus 5.5; 6.000+ conectores; VM própria; Link e Shop Pay.
- Não faz compras de "errands"/ingressos tão bem; não mostra o navegador.
- Concorrentes citados: Meta Muse, OpenAI Dots, Hark, Instinct, Grok Bot, Fo.
- Não negocia valores mobiliários nem transfere dinheiro entre contas; classificador contra vazamento.

## 5. 9to5Mac — 21/10/2026
https://9to5mac.com/2026/10/21/anthropic-takes-on-chatgpt-dots-and-meta-muse-with-claude-duet/
- "Claude Duet isn't available on Team or Enterprise plans yet"; sem custo extra, uso conta no limite.
- Abas **Tasks** (só o usuário marca como concluída) e **Make** (entregas maiores editáveis: brief de pesquisa, modelo financeiro, slides, dashboards).
- Navegador na nuvem para sites sem conector; pode buscar conversas antigas.

## 6. MacRumors — 21/10/2026
https://www.macrumors.com/2026/10/21/anthropic-claude-duet/
- Web + app iOS (não menciona Android); EUA; Pro/Max; checa "every few hours"; VM com navegador; Opus 5.5; aprovação antes de mensagem/pagamento/assinatura/apagar.

## 7. 9to5Google — 21/10/2026
https://9to5google.com/2026/10/21/claude-duet-anthropic-ai-agent-waitlist/
- Pro/Max, lista de espera, brief matinal, monitoramento, tarefas (dashboards, previsões, web apps). Dots "lançado poucas semanas antes".

## 8. Flavio Copes (blog, não testou o produto) — 22/10/2026
https://flaviocopes.com/claude-duet/
- Cita o guia de ajuda: "**Microsoft 365 isn't available in Duet yet**"; alguns conectores, como **Slack**, têm limites (não detalha).
- Precisa de conta Pro/Max nos EUA + convite; Team/Enterprise fora; entrar na lista não garante data.
- Não acessa arquivos locais, não faz ligações nem envia SMS (segundo ele).
- **Não consegui achar o artigo da central de ajuda** (support.claude.com) citado por ele → no vídeo, Microsoft 365 aparece só como "segundo o desenvolvedor Flavio Copes, citando a central de ajuda". Slack com limites: deixado de fora (vago demais).

## 9. Every (Vibe Check) — 22/10/2026
https://every.to/vibe-check/vibe-check-duet-anthropic-s-always-on-agent
- Teste com acesso antecipado: "first personal agent" que o autor chamaria de ferramenta profissional; canais por tema; lista do que está fazendo e do que precisa do usuário.
- Fraquezas: rascunhos de e-mail piores que os do Dot (OpenAI); execuções agendadas não alcançam conectores personalizados; sem modo de voz real (só transcrição). Não usado no vídeo (opinião, parcialmente atrás de paywall).

## 10. AIN.ua — 22/10/2026
https://en.ain.ua/2026/10/22/anthropic-introduced-claude-duet-an-agent-that-autonomously-tracks-work-tasks-and-executes-them/
- Repete os dados oficiais; diz que OpenAI apresentou o Dots em setembro de 2026.

## Divergências e decisões
- **Android**: MacRumors só cita iOS; a página oficial diz iOS **e Android** → vale a oficial.
- **Opus 5.5** e **6.000+ conectores**: confirmados na oficial.
- **"Dots" x "Dot"**: CNBC/TechCrunch/9to5Mac escrevem "Dots"; Every escreve "Dot". Vídeo usa "Dots, da OpenAI" citando a imprensa, sem afirmar recursos.
- **Preço próprio / lançamento geral**: não existem nas fontes → não citados (só "incluído no Pro e Max durante a prévia").
- **Microsoft 365**: só uma fonte não oficial → citado com atribuição. **Slack com limites**: deixado de fora.
