# Série Notação Científica e Ordem de Grandeza (Matemática ENEM): 6 episódios para iniciantes

Material: `Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html` (texto extraído com
`_ferramentas/extrair_material.py` em `_material/material_notacao.txt`: expoentes "^(−3)", raízes "√(10)", frações "(a/b)")
· modelo: [../PROMPT_AULA_INICIANTE.md](../PROMPT_AULA_INICIANTE.md) · prompts por episódio enviados em 23/10/2026
(pedido: "faça sem gerar os áudios" → roteiro, roteiro_para_gravar.txt, animação com tempos SINTÉTICOS, prévias e capas).

| Ep. | Pasta | Tema | Recorte do material | Duração | Ponte para | Situação |
|---|---|---|---|---|---|---|
| 1 | `ep1_forma_exata` | Forma exata, converter qualquer número, algarismos significativos | 02, 03, 09 + Q1 | 10–12 min | Operações | pronto sem voz (1624 pal. ~10,8 min · voz: parte 2 da cena 18) |
| 2 | `ep2_operacoes` | Multiplicar, dividir, elevar e tirar raiz (renormalizar; raiz com expoente par) | 04 + Q2, Q3, Q8 + extra das bactérias | 10–12 min | Somar | pronto sem voz (1771 pal. ~11,8 min · voz: parte 2 da cena 16) |
| 3 | `ep3_somar_comparar` | Somar (a que derruba) e comparar grandezas | 05, 08 + Q4, Q7 | 8–10 min | Ordem de grandeza | pronto sem voz (1555 pal. ~10,4 min · voz: parte 2 da cena 20) |
| 4 | `ep4_ordem_de_grandeza` | Ordem de grandeza (critério 3,16) e a conta de guardanapo | 06, 10 + Q5, Q9 | 10–12 min | Prefixos | pronto sem voz (1738 pal. ~11,6 min · voz: parte 2 da cena 16) |
| 5 | `ep5_prefixos_area_volume` | Prefixos de tera a pico e a armadilha de área e volume | 07 + Q6 | 8–10 min | Revisão | pronto sem voz (1389 pal. ~9,3 min · voz: parte 2 da cena 16) |
| 6 | `ep6_revisao` | Revisão, V/F dos 9 erros e 5 questões INÉDITAS (uma por área) | 01, 11, 13 (sem Q1–9) | 10–12 min | Razão, proporção e regra de três | pronto sem voz (1762 pal. ~11,7 min · voz: parte 2 da cena 19) |

**Gabaritos do material:** Q1 C (5,97·10²⁴) · Q2 C (4·10⁷) · Q3 D (400) · Q4 C (4·10⁵) · Q5 C (10⁶) · Q6 C (2,5·10⁷) ·
Q7 B (80 vezes) · Q8 A (4·10⁻³) · Q9 B (1,8·10⁸) · extra das bactérias (ep2) B (6·10⁻⁴).

**Analogias âncora (a revisão retoma todas, com os mesmos ícones):** ep1 forma exata = PLACA DE CARRO (um só jeito certo) ·
expoente = contador de casas que a vírgula andou (liga ao "contador de zeros" da série 019) · zeros à esquerda = cadeiras vazias ·
ep2 duas PISTAS (coeficientes / expoentes) · a GANGORRA (coeficiente ×10, expoente −1, mesmo valor) · ep3 NOTAS de valores
diferentes · "quantas vezes" = quantas Luas cabem na Terra · ep4 casa de potência de 10 mais próxima · régua de multiplicar com
3,16 no meio · conta de GUARDANAPO · ep5 prefixo = potência de 10 com apelido · área = GRADE de quadradinhos, volume = cubo de cubinhos.
Ícones da revisão: placa de carro · gangorra · notas de dinheiro · régua do 3,16 · grade de quadradinhos.

**Atenção (material e prompts):** o material diz que o assunto "cai nas quatro áreas" e lista Matemática, Física, Química,
Biologia e Humanas. Isso dá TRÊS das quatro áreas do ENEM (Matemática, Ciências da Natureza e Ciências Humanas); Linguagens fica
de fora. Nos ganchos dos eps 1 e 6 a fala deve ser precisa: "Matemática, Ciências da Natureza (Física, Química e Biologia) e até Humanas".

**Peças comuns:** `comum.py` (nesta pasta) reexporta o `019/comum.py` (expr com potências "7,2·10^{-3}", raízes "√{10}", frações,
fichas, escada, atalho, selo_teste, alternativas, erro_cards, pause_timer). Cada `visual.py` importa como `K` e chama `K.usar_tempos(...)`.
Regras: em exatas, uma cena verde de ATALHO por procedimento e toda fórmula explicada na hora; CTA com o aviso dos flashcards
Anki (cue {anki}, ver canais/enem/ESTILO.md). Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho · vermelho = erro.
Voz: Gemini TTS Studio local (Neno), tags alegre/curiosa/amigavel.

Arquivos finais: `epN_<tema>/final/enem_matematica_notacao_epN_<tema>.mp4`.


**Status 23/10/2026:** os 6 eps prontos SEM VOZ (roteiro, texto para gravar, visual com tempos sintéticos, prévias, 3 capas, aviso Anki).
Erros do material: Q3 (errar o sinal NÃO leva à A = 25; −2 − 5 = −7 dá 0,4·10⁻⁷) · Q4 (a A = 1,3·10⁴ não sai só de somar
coeficientes: 13·10⁴ = 1,3·10⁵) · seção 01 ("quatro áreas" lista três). Exemplos trocados para não entregar questões: ep2 blocos c/e,
ep3 Terra ÷ Lua, ep4 gancho 720 000 → 850 000 (aguardando o usuário). Ep6: inéditas B, D, C, E, A.