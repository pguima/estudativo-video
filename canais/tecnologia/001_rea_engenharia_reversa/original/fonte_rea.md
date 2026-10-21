# Fonte — REA (Reverse Engineer Anything)

Consultado em 15/10/2026.
- Repositório: https://github.com/morluto/rea (licença MIT; README marca 250 mil estrelas; ~259 mil estrelas, ~65 mil forks)
- Site/documentação: https://rea.tools · pacote npm: `rea-agents`

## O que é
"One MCP for reverse engineering across binaries, applications, and runtime behavior."
"See a feature you like. Understand how it works, down to the binary level."
Servidor MCP que dá a agentes de IA (Claude Code, Codex, Cursor, Gemini CLI, Grok Build, qualquer agente com MCP local)
ferramentas para inspecionar binários nativos, apps JavaScript/Electron, assemblies .NET, sites e mais. Também tem CLI (`rea`).

## Como funciona
1. O agente chama o REA via MCP para inspecionar o alvo e rastrear o código relevante.
2. O REA devolve descobertas com evidências (código, referências, desconhecidos).
3. O agente explica o comportamento ou escreve e testa uma implementação. A CLI roda os mesmos fluxos.
Cada conclusão vem com evidência e limitações. Separa dados retornados pelo REA da interpretação do agente.

## Alvos (~25 tipos)
Binários nativos (Hopper, Ghidra, IDA, Kuna) · Go e Rust (estático, sem toolchain) · WASM · bytecode EVM · ELF ·
crashes Linux · JavaScript/Electron (módulos, IPC, add-ons nativos, ASAR) · APK Android (JADX) · dispositivos Android (adb) ·
.NET · Flutter · bundles Apple · sites (navegador Chrome-family) · HAR/SAZ/mitmdump · pacotes (TShark) · SQLite ·
firmware (Binwalk/Unblob) · analisador lógico (sigrok) · comportamento de processo (PTY, Linux/macOS).

## Privacidade
Análise local. Estática de JS e .NET lê arquivos sem executar. Captura em tempo de execução roda o alvo com as permissões do usuário.
O provedor do modelo do agente aplica sua própria política aos resultados.

## Instalação
Node.js 22.x (≥22.19), 24.x (≥24.11) ou 26+, e npm. `npx rea-agents setup` → escolhe agentes, revisa mudanças, aprova
(faz backup da config) → reinicia o agente. CLI global: `npm install --global rea-agents` → `rea --help`; `rea update`.
Exemplo de prompt: "Understand how search works in the Notes app, show me the evidence, and build a similar feature."
CLI: `npx -y rea-agents@latest analyze-javascript-application <path> --json`

## Exemplos (rea.tools / README)
- Calculadora do Windows 11.2508.4.0 x64 (REA 4.1.0): % depois de + → porcentagem do 1º número (200 + 10% = 220);
  depois de × ou ÷ → 10% vira 0,1 (200 × 10% = 20). IDs de operador 0x5b/0x5c = ÷ e ×.
- Dinossauro (edição de navegador, derivado do Chromium, BSD): velocidade começa em 6, +0,001 por atualização, teto 13
  (10,0 após 4.000 atualizações; 13,0 após 10.000). Minijogo com controle de velocidade.
- DX-Ball (Windows, 1996): posição da bola → panorâmica do som (esquerda/direita); reconstruído em C, passa 3.205 casos
  do x86 original e reproduz os 63 bytes da função compilada.
- Notion (Electron): API de clipboard via preload e IPC até o processo principal.
- Aegis (Android): como o código de 6 dígitos é gerado e muda a cada 30 s. TH04 (PC-98): ângulos dos anéis de balas.

## Legal
Para pesquisa lícita, educação, interoperabilidade, preservação de software e análise de software próprio ou autorizado.
Código do REA: MIT. Ferramentas comerciais (IDA Pro, Hex-Rays, Hopper, JEB) precisam ser obtidas legalmente; o REA não dá
licença nem chave; cópias crackeadas, chaves roubadas/compartilhadas e burla de licença não são autorizadas.
Aviso do README: nome parecido ou README copiado não prova que um download é oficial (fontes oficiais: repo, rea.tools, npm).
