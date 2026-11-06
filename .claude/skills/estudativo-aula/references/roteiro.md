# Roteiro de uma aula

## Tamanho

De 650 a 1.250 palavras, ou cerca de 5 a 8 minutos. Prática vai até 10 minutos. Pare quando o conteúdo acabar: ficar pouco abaixo de 5 minutos é melhor que esticar, e a prolixidade foi o defeito do projeto antigo.

## Ordem

| Parte | Tempo | O que faz |
|---|---|---|
| Gancho | até 15 s | Um erro, pergunta ou resultado que surpreende, e a promessa da aula |
| Lembrete | até 20 s | O que a pessoa precisa saber, tirado dos pré-requisitos diretos |
| Conteúdo | o resto | Pergunta → exemplo do dia a dia → regra → exemplo resolvido |
| Erro comum | curto | Um só, mostrando por que está errado |
| Atalho | curto | Em Matemática, Física e Química: macete de prova, com o motivo de funcionar e quando não compensa |
| Questão | curto | Uma questão, com "pause o vídeo" e pausa de 3 s |
| Resposta | curto | Resolvida passo a passo |
| Fechamento | até 20 s | Resumo em uma frase, ponte para a próxima aula, "inscreva-se" |

Não entram: mapa da aula, "nesta aula vamos ver", recapitulação repetida, curtir, sininho, pergunta para comentários. Prática: de 3 a 5 questões inéditas no lugar do conteúdo, cobrindo o módulo.

## Regras de texto

- Todo conteúdo usado precisa estar na ficha, em "Já ensinado". Precisa citar algo fora dela? Diga que é assunto de outra aula.
- Termo novo: explique na hora, com exemplo.
- Toda fórmula tem seu significado explicado. Exemplo: o que é perímetro antes de calcular.
- Frases curtas, uma ideia por frase, em "você".
- Números e fórmulas por extenso no texto narrado: "três quartos", "cinco doze avos". Na tela, em notação normal.
- Evite "os dois" perto de números, porque soa como o número 2: diga "seis e oito são pares".
- Não comece várias cenas com "Agora".
- Fração nova é lida como será ouvida: "sete doze avos", nunca "sete sobre doze".
- A ponte para a próxima aula precisa bater com a ficha: confira o que aquela aula ensina, não só o título.
- Só prometa o que existe. Se o pré-requisito não estiver publicado (veja a situação na ficha), não diga que a aula está na descrição: diga "se faltar alguma, procure no canal".
- Questão real de prova só com fonte citada e direito de uso checado. Questão inédita nunca é apresentada como real.
- Títulos e textos sem a palavra ENEM; o curso serve a vários vestibulares.

## O que a revisão mais pega

Nas revisões de 42 aulas, nenhuma conta saiu errada: os defeitos são de ensino. Procure estes antes do revisor:

- Regra que falha em caso que a própria aula mostra ou que o aluno verá logo depois. Teste a frase contra os exemplos. "Só em vezes e dividido" contradizia 3 − (−5) = 8; "dez, cem ou mil" falha com 1/16; "multiplicar faz crescer" falha com 0,3.
- Palavra tratada como regra. "Sobrou" pode pedir soma: a história decide, a palavra é pista.
- Exemplo em que o erro comum dá a resposta certa, ou em que parar na primeira etapa já acerta.
- Enunciado que admite outra leitura ("um terço à tarde" depois de uma aula de fração do restante) ou que não faz a pergunta.
- Desfecho do erro comum que não reproduz o erro: refaça a conta errada e veja se ela dá o número citado.
- Fato do mundo real desatualizado, como preço de combustível com três casas.
- Termo ou método diferente do usado nas aulas seguintes. Antes de escrever, leia como elas usam aquilo.
- Fala que soa mal no áudio: "o de vira vezes" (diga "a palavra de"), "menos menos cinco" (diga "abre parênteses"), vírgula de pontuação entre dois números.

## Formato do cenas.py

```python
# Estudativo · <id> — <título> (<matéria> · <trilha>).
# Habilidade: <habilidade>
# Pré-requisitos: <ids>. Próxima: <id>.

TITULO = "<título>"

VOZ = <copie do piloto>

SCENES = [
    dict(id="s01", block="gancho", text="{a}Um meio {b}mais um terço. [p=0.3] ..."),
]
```

- `{a}` dispara animação no instante da palavra seguinte e vira `C["s01.a"]` no visual.
- `[p=0.3]` é pausa; `[p=3.0]` no fim da cena da questão.
- `block` agrupa cenas de uma mesma tela. Ids em ordem: `s01`, `s02`...
- Coloque um cue em cada coisa que deve aparecer. Sem cue, a animação não sincroniza com a fala.
