# Fonte — Tecnologia 014: API oficial do WhatsApp (Meta): custo, configuração e multiatendimento
Consulta: 29/10/2026. Tudo o que aparece no vídeo sai daqui.

## Preços (oficial: developers.facebook.com/docs/whatsapp/pricing + rate cards de 01/10/2026)
- Cobrança **por mensagem entregue** desde 01/07/2025; valor depende da **categoria** e do **país do destinatário**.
- "Meta does not charge for messages from users to businesses" → mensagens do cliente para a empresa: grátis.
- Categorias de modelo (template): **Marketing, Utilidade (Utility), Autenticação (Authentication)**. Sem modelo: **Serviço**
  (inclui mensagens de atendentes humanos ou de IA de terceiros), só dentro da **janela de atendimento de 24 horas**
  ("a 24-hour timer called a customer service window starts" quando o usuário manda mensagem).
- **Desde 01/10/2026:** mensagens de serviço e de utilidade dentro da janela, antes grátis, passam a ser cobradas.
  Cada número comercial tem **1.000 mensagens de serviço grátis por mês** (não acumulam).
  Sem forma de pagamento cadastrada até 30/09/2026: risco de interrupção na entrega das mensagens de serviço.
- **Free entry point:** conversa iniciada por anúncio "Click to WhatsApp" (ou botão de CTA da página do Facebook) → respostas grátis na janela;
  "The FEP window may remain open for up to 7 days."
- **Cobrança em reais (BRL)** disponível para clientes elegíveis no Brasil desde 01/07/2026; contas não-BRL migram até 30/06/2027.
- Meta só muda preços em 1º/jan, 1º/abr, 1º/jul ou 1º/out.

### Tabela oficial BRL, vigência 01/10/2026 (arquivo `meta_rate_card_BRL_2026-10-01.xlsx`), linha Brazil
| Marketing | Utility | Authentication | Service |
|---|---|---|---|
| R$ 0,3217 | R$ 0,035 | R$ 0,035 | R$ 0,035 |
USD (arquivo `meta_rate_card_USD_2026-10-01.xlsx`): 0,0625 · 0,0068 · 0,0068 · 0,0068.

### Faixas de volume BRL (`meta_volume_tiers_BRL_2026-10-01.xlsx`), Brazil — só utilidade e autenticação, por mês
- Utilidade: 0–250.000 = 0,035 (lista) · 250.001–2 mi = 0,0333 (−5%) · 2 mi–17 mi = 0,0315 (−10%) · 17–35 mi = 0,0298 (−15%) ·
  35–70 mi = 0,028 (−20%) · acima de 70 mi = 0,0263 (−25%).
- Autenticação: 0–500.000 = 0,035 · 500.001–3 mi = 0,0333 · … · acima de 20 mi = 0,0263.
- Marketing: sem desconto por volume.

## Limites de envio (developers.facebook.com/docs/whatsapp/messaging-limits)
- Por **portfólio empresarial**: começa em **250**; **2.000** após caminho de escala (verificar a empresa, ou 2.000 mensagens
  de qualidade fora da janela em 30 dias); depois **10.000, 100.000 e ilimitado** automaticamente (alta qualidade e uso de
  metade do limite nos últimos 7 dias). Limite = destinatários únicos em 24 h fora da janela de atendimento.

## Configuração (developers.facebook.com/docs/whatsapp/cloud-api/get-started e /phone-numbers)
1. Conta no Meta for Developers; App Dashboard → **Create App** → caso de uso **"Connect with customers through WhatsApp"** →
   escolher/criar **portfólio empresarial**.
2. **API Setup:** conta do WhatsApp (WABA), **número de teste** e **token temporário**; enviar mensagem de teste.
3. Número real: um número registrado "cannot be used with WhatsApp Messenger"; se já estiver no WhatsApp, precisa ser
   **apagado antes** (ou usar a **coexistência**). Exige **nome de exibição** e **PIN de verificação em duas etapas**.
4. **Token permanente:** Configurações do negócio → **Usuários do sistema** → atribuir o app e a conta do WhatsApp (controle
   total) → Gerar token com `business_management`, `whatsapp_business_messaging`, `whatsapp_business_management`.
5. **Webhook:** URL HTTPS + token de verificação; assinar o campo **messages** (status de entrega e mensagens recebidas).
6. Enviar: `POST https://graph.facebook.com/<versão>/<PHONE_NUMBER_ID>/messages`, header `Authorization: Bearer <TOKEN>`,
   corpo com `messaging_product: "whatsapp"`, `to`, `type: "text"`. Mensagem livre só dentro da janela de 24 h.
   Versão mais recente da Graph API: **v26.0** (29/07/2026, changelog).
7. Webhooks são assinados com o cabeçalho `X-Hub-Signature-256` (HMAC-SHA256 com o app secret): validar no servidor.

## Coexistência (developers.facebook.com/docs/whatsapp/embedded-signup/custom-flows/onboarding-business-app-users)
- App WhatsApp Business **e** Cloud API no **mesmo número**; via **Embedded Signup** de um parceiro (Solution Partner/Tech Provider).
- Sincroniza conversas 1:1 dos últimos **180 dias** e os contatos; mensagens do app continuam grátis; vazão fixa de 20 msg/s.
- Grupos, chamadas, catálogo e listas de transmissão não passam pela API.

## Multiatendimento — exemplo Chatwoot (chatwoot.com/hc/user-guide · "How to setup a WhatsApp channel (Manual flow)")
- Chatwoot: código aberto (licença MIT, exceto a pasta `enterprise/`), github.com/chatwoot/chatwoot (~38,5 mil estrelas em 29/10/2026).
- Settings › Inboxes › Add Inbox › WhatsApp › **WhatsApp Cloud** → "manual setup flow".
- Pede **Phone Number ID**, **WhatsApp Business Account ID** e o **token permanente** (expiração "Never",
  `whatsapp_business_management` + `whatsapp_business_messaging`).
- Chatwoot confere Number access, Template access, Webhook callback e Webhook subscription e configura o webhook na Meta;
  depois "Continue to add agents". Sem `whatsapp_business_management`, os modelos não sincronizam.
- Alternativa: **Quick setup** (Embedded Signup). Coexistência não funciona no fluxo manual.

## Política (WhatsApp Business Messaging Policy)
- É preciso ter **consentimento (opt-in)** da pessoa antes de mandar mensagens iniciadas pela empresa.
