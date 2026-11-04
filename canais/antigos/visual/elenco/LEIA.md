# Elenco do canal "Nós, os Antigos"

Personagens e objetos reutilizáveis, todos no padrão de acabamento da Lume. O código fica em
`_ferramentas/antigos_elenco.py`, e a Lume em `_ferramentas/antigos.py`.

Para usar num episódio, coloque no `visual.py` do episódio:

```python
from antigos import *
from antigos_elenco import *
```

Para gerar as folhas de catálogo (`elenco_*.png`), rode `python elenco.py`.

## Referências de estilo (02/11/2026)

Os dois vídeos que o usuário mandou estão em `/root/work/ref_antigos/`: um no estilo Kurzgesagt e um do The Infographics Show.
Deles vem a anatomia, mas não as cores:
- **Pessoa:** cabeça com cerca de 1/5 da altura e pescoço visível. O tronco é uma forma única, com ombros caídos e cintura.
- **Braços e pernas:** longos, afinando, com cotovelo.
- **Mãos e pés:** a mão é uma "luva" simples, e os pés são pequenos.
- **Rosto:** olhos são ovais escuros com um pontinho de brilho, a bochecha é rosada, o nariz é uma bolinha de pele
  mais escura e a boca é pequena.
- **Mão em close:** uma luva gorda, com dedos grossos encostados, sem unha e sem ruga, e um único tom de sombra.
- **Paleta:** continua a do canal (`antigos.py`), sem mudanças.

## O padrão da Lume (regra para todo elemento novo)

1. Formas arredondadas, sem contorno preto.
2. Sombreamento plano: a cor base, mais uma mancha de sombra recortada dentro da peça (embaixo ou à direita)
   e um brilho claro (em cima ou à esquerda). Use `volume(c, path, cor, sh=..., hl=...)`.
3. A sombra mantém o matiz e escurece com `sombra(cor)`. O amarelo escurece para âmbar, nunca para
   verde-oliva nem para preto.
4. Sombra de contato no chão, desfocada.
5. Rosto com vida: olho com reflexo branco, sobrancelha, boca que abre na fala e bochecha.
6. Vida em repouso: respiração, piscadas e balanço, sempre em função do tempo t (`antigo_vivo`, `piscadas`).
7. Antes de usar no vídeo, renderize uma folha (catálogo ou quadros), olhe a imagem e corrija os três piores
   problemas. Repita até ficar no nível da Lume.

## Peças

| Peça | Função | Observações |
|---|---|---|
| Pessoa (os Antigos) | `antigo(c, x, y, s, antigo_vivo(t, seed, ...))` | `s=1` ≈ 172 px. Estilos de cabelo: `ESTILOS`. Expressões: `expressao("feliz" \| "surpreso" \| "preocupado" \| "hipnotizado" \| "cansado" \| "dormindo")`. Com `celular="d"`, ganha o celular na mão e a luz da tela no rosto. |
| Troca direta da `pessoa` antiga | `pessoa2(...)` | Mesmos argumentos da `pessoa` antiga, mais `t=`, `seed=`, `estilo=` e a expressão. |
| Mão em close | `mao(...)` / `mao_na_ponta(c, px, py, s, "toque", ang, manga=..., aperta=...)` | Gestos: `aponta`, `toque` e `aberta`. `mao_na_ponta` põe a ponta do indicador exatamente em (px, py), para tocar ou arrastar na tela. `toque_onda` desenha a onda do toque. |
| Celular (peça 002) | `celular_aceso(c, cx, cy, s, t, tela, badge, feed, ang)` | Tela com apps ou com feed rolando. |
| Rato | `rato(c, x, y, s, t, aperta, dorme)` | Rato de laboratório de perfil; pisca sozinho. |
| Cérebro | `cerebro(c, cx, cy, s, flash)` | `flash` acende o ponto de dopamina. |
| Móveis | `mesa(c, x0, x1, ytopo, ychao)`, `caixa_madeira(c, x, y, w, h, tampa_h, aberta=)` | Madeira com veios e sombra. |
| Objetos | `olho`, `sino` (`riscado=True` = silenciado), `moeda`, `coracao`, `ampulheta`, `caca_niquel`, `estrela`, `raio`, `simbolo` | |

## O que não fazer (para não virar "AI slop")

- Peças chapadas, como uma cápsula bege no lugar de uma mão ou um retângulo marrom no lugar de uma mesa.
- Texto centralizado sobre um degradê, com tudo entrando em fade ao mesmo tempo.
- Uma pessoa sem rosto, ou com o rosto parado.
- Qualquer elemento novo que não passe pela regra 7.
- Roxo neon e pássaros (regra do canal).
