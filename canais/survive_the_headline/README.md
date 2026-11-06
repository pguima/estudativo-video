# Survive the Headline: motor de personagens

Biblioteca de personagens 2D em SVG e JavaScript puro, sem dependências. Abra `studio.html` no navegador para testar tudo sem escrever código.

## Uso

```html
<div id="palco" style="width:600px;height:600px"></div>
<script src="engine/SVGRenderer.js"></script>
<script src="engine/ExpressionEngine.js"></script>
<script src="engine/PoseController.js"></script>
<script src="engine/AnimationEngine.js"></script>
<script src="engine/LipSyncEngine.js"></script>
<script src="engine/CharacterEngine.js"></script>
<script src="engine/rigs/HumanRig.js"></script>
<script src="engine/rigs/QuadrupedRig.js"></script>
<script>
(async () => {
  const dan = await CharacterEngine.load('dan', { container: '#palco' });
  dan.setExpression('worried');
  dan.setPose('standing');
  dan.play('talking');
  dan.setDirection('left');
  dan.setVisible(true);
})();
</script>
```

`container` é opcional. Sem ele, o personagem nasce em um `<div class="sth-character">` no fim do `<body>`.

A mesma interface vale para `dan`, `mia`, `leo`, `bea` e `biscuit`.

| Método | Função |
|---|---|
| `setExpression(nome)`, `setPose(nome)`, `play(nome)` | Expressão, pose e animação, com transição suave |
| `setDirection('front' \| 'left' \| 'right' \| 'three-quarter-left' \| 'three-quarter-right')` | Direção |
| `setVisible(bool)`, `setAccessory(nome, true \| false \| 'auto')` | Visibilidade e acessórios |
| `setOutfit(nome)`, `setHair(nome)` | Figurino e penteado, quando existem |
| `setArm('right', { shoulder, elbow, wrist, hand })`, `setArm('right', null)` | Braço independente da pose |
| `setViseme('A')`, `speak(linha)`, `speak('texto', segundos)` | Lábios: por boca, por linha do tempo ou por rascunho de texto |
| `lookAt(x, y)`, `setHeadTilt(graus)`, `blink()` | Olhar e cabeça |
| `expressions`, `poses`, `animations`, `getState()` | O que o personagem aceita e seu estado atual |
| `tick(ms)`, `toSVG()` | Avança um quadro e exporta o SVG |

## Cenas

```js
const cena = CharacterEngine.createScene('#tela', { background: 'kitchen' });
const dan = await cena.add('dan', { x: 500, direction: 'three-quarter-right' });
const bea = await cena.add('bea', { x: 1100 });
dan.moveTo(620);
cena.setBackground('street');
```

A tela tem 1920 x 1080. `x` é o centro do personagem, e todos pisam na mesma linha de chão. Cenários: `house_exterior`, `living_room`, `kitchen`, `bedroom_kids`, `bedroom_parents`, `garage`, `hospital`, `school`, `office`, `street`.

## Vídeo quadro a quadro

```js
const cena = CharacterEngine.createScene(el, { autoStart: false, background: 'kitchen' });
const mia = await cena.add('mia', { x: 960, seed: 42 });
for (let quadro = 0; quadro < 90; quadro++) {
  cena.tick(1000 / 30);
  salvarQuadro(cena.toSVG());   // sua função
}
```

Com a mesma semente, os quadros saem idênticos a cada renderização.

`scenes/family-scene.js` é um modelo de roteiro: uma lista de batidas com tempo e comandos.

## Estrutura

```
engine/CharacterEngine.js    API, relógio único, cenas
engine/SVGRenderer.js        curvas, nós SVG, cores
engine/ExpressionEngine.js   mistura de expressões, piscadas, olhar, bocas de fala
engine/PoseController.js     poses por ângulo, apoio no chão, ciclos de andar e correr
engine/AnimationEngine.js    animações em camadas
engine/LipSyncEngine.js      linha do tempo de lábios
engine/rigs/HumanRig.js      corpo e rosto comuns aos quatro humanos
engine/rigs/QuadrupedRig.js  esqueleto de quatro patas
characters/<nome>/config.js  dados e partes próprias do personagem
characters/<nome>/model.svg  exportação editável do modelo
scenes/backdrops.js          cenários
scenes/family-scene.js       cena de teste
tools/engine-test.html       testes automáticos
```

## Como estender

- **Nova expressão ou pose:** acrescente nas tabelas de `characters/<nome>/config.js`.
- **Novo personagem humano:** copie um `config.js`, troque medidas (`M`, `D`), formas (`SHAPE`) e partes próprias.
- **Novo cenário:** acrescente uma entrada em `SCENES`, em `scenes/backdrops.js`. `draw(k)` desenha atrás do elenco e `front(k)`, opcional, à frente dele. O kit `k` traz sala em perspectiva, portas e quadros nas paredes laterais, janelas, livros, plantas, fachos de luz e sombras.
- **Nova animação comum:** acrescente em `AnimationEngine.js`. Para um personagem só, em `ANIMATE` do `config.js`.

`model.svg` serve para abrir no Illustrator, Figma ou Inkscape. A animação vem do rig, então editar esse arquivo não muda o personagem no motor.

`tools/build-characters.js` foi usado uma vez, para migrar os personagens aprovados. A fonte oficial agora é `characters/<nome>/config.js`: não rode o script de novo, ou as edições feitas nesses arquivos serão sobrescritas.
