# Roteiro — Seguridade Social 013: Segurado especial (Módulo M09, parte 2 de 2)
# Base: Estudos/Seguridade Social/modulos/M09-contribuinte-individual-e-segurado-especial.md — seção 2, quadro 3 e questões Q2, Q5, Q6, Q8, Q11 e Q12
#   Lei 8.213/1991, art. 11, VII e §§ 1º, 7º, 8º, 9º e 10 · art. 39 · CF, art. 195, §8º. O contribuinte individual foi a Aula 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material avisa: os §§ 8º a 10 do art. 11 "já sofreram alterações — conferir no texto compilado". Dito na cena dos números.
# Gancho = o caso do João (Q8): a pergunta abre a aula e a resolução volta no fim, item a item.
# Liga com a Aula 12: a fronteira "mais de 4 módulos OU empregado permanente → contribuinte individual".

TITULO = "Segurado especial: 4 módulos, 16 anos e três vezes 120 (Lei 8.213, art. 11, VII)"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho apaixonado pela matéria, conversando de perto com o aluno que vai fazer "
            "o concurso do INSS: voz calorosa, envolvente e MUITO expressiva, com bastante variação de entonação e emoção "
            "verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara uma revelação; mostre "
            "surpresa e suspense nas pegadinhas; responda com firmeza e energia ('Errado!', 'Certo!'); dê ênfase forte às "
            "palavras-chave e aos macetes. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. "
            "Leia apenas o texto, sem acrescentar nem repetir nada."),
)

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "{a}O João planta com a esposa e o filho [p=0.2] num sítio de *três* módulos fiscais. [p=0.4] {b}Na safra, "
        "[p=0.2] contratou *cinco* trabalhadores. [p=0.3] {c}Recebe *Bolsa Família.* [p=0.3] {d}E ainda é *vereador!* "
        "[p=0.5] {e}Ele continua sendo *segurado especial?* [p=0.5] {f}Guarde a sua resposta. [p=0.3] No fim da aula, "
        "[p=0.2] a gente resolve *juntos.*"),

    # ================= BASE LEGAL =================
    dict(id="02", block="base", text=
        "{t}O segurado especial está no artigo onze, [p=0.2] inciso *sete,* [p=0.2] da Lei oito mil, duzentos e treze. "
        "[p=0.4] {a}E ele tem uma coisa que nenhum outro segurado tem: [p=0.3] {b}base *própria* na Constituição, "
        "[p=0.2] no artigo cento e noventa e cinco, [p=0.2] parágrafo oitavo. [p=0.5] {c}É a categoria *mais detalhada* "
        "do RGPS. [p=0.3] {d}E, por isso, [p=0.2] uma das que *mais caem.*"),

    # ================= CONCEITO =================
    dict(id="03", block="elementos", text=
        "{t}O conceito tem *quatro* elementos. [p=0.4] {a}Primeiro: [p=0.2] *pessoa física.* [p=0.4] {b}Segundo: "
        "[p=0.2] que *mora* no imóvel rural, [p=0.2] ou num aglomerado *próximo* a ele. [p=0.4] {c}Terceiro: [p=0.2] "
        "que trabalha *individualmente,* [p=0.2] *ou* em regime de economia familiar. [p=0.4] {d}E quarto: [p=0.2] "
        "que se encaixe numa das condições da lei."),
    dict(id="04", block="quem", text=
        "{t}E que condições são essas? [p=0.4] {a}O *produtor* [p=0.2] em atividade agropecuária de até *quatro módulos "
        "fiscais.* [p=0.3] Pode ser proprietário, [p=0.2] parceiro, [p=0.2] meeiro, [p=0.2] arrendatário. [p=0.4] "
        "{b}O *seringueiro* e o *extrativista vegetal,* [p=0.2] como principal meio de vida. [p=0.4] {c}O *pescador "
        "artesanal.* [p=0.4] {d}E a família: [p=0.2] o *cônjuge,* [p=0.2] o companheiro [p=0.2] e o *filho maior de "
        "dezesseis anos* [p=0.2] que trabalhe com o grupo."),
    dict(id="05", block="sozinho", text=
        "{t}E repare numa palavrinha: [p=0.3] *individualmente,* [p=0.2] *ou* em economia familiar. [p=0.5] {a}Então, "
        "[p=0.2] o produtor que trabalha *sozinho,* [p=0.2] sem família nenhuma, [p=0.4] {b}*pode* ser segurado especial! "
        "[p=0.5] {c}A família *não* é obrigatória. [p=0.3] E a banca adora dizer que é."),

    # ================= ECONOMIA FAMILIAR =================
    dict(id="06", block="economia", text=
        "{t}Mas o que é regime de economia familiar? [p=0.4] {a}É quando o trabalho da família é *indispensável* à "
        "subsistência, [p=0.3] {b}e ao desenvolvimento do *núcleo familiar.* [p=0.3] {c}Com *mútua dependência* e "
        "colaboração. [p=0.4] {d}E, aqui está o ponto de ouro: [p=0.3] *sem empregados permanentes.* [p=0.5] {e}Empregado "
        "*permanente* descaracteriza. [p=0.3] Ajuda *eventual* de terceiros, [p=0.2] *não.*"),
    dict(id="07", block="modulo", text=
        "{t}E o que é módulo fiscal? [p=0.4] {a}É uma medida agrária fixada *por município.* [p=0.3] {b}Vai de *cinco* "
        "a *cento e dez* hectares, [p=0.2] conforme a região. [p=0.5] {c}Então, [p=0.2] se a questão disser [p=0.2] "
        "*quatro hectares,* [p=0.3] {d}*Errado!* [p=0.3] São quatro *módulos fiscais.*"),

    # ================= OS NÚMEROS =================
    dict(id="08", block="numeros", text=
        "{t}Agora, os números do segurado especial. [p=0.3] Decore como um *bloco.* [p=0.5] {a}*Quatro:* [p=0.2] módulos "
        "fiscais. [p=0.4] {b}*Dezesseis:* [p=0.2] a idade mínima do filho. [p=0.4] {c}*Cento e vinte* pessoas por dia, "
        "[p=0.2] na safra. [p=0.4] {d}*Cento e vinte* dias de atividade remunerada fora. [p=0.4] {e}*Cento e vinte* dias "
        "de turismo rural. [p=0.4] {f}E *cinquenta* por cento: [p=0.2] o limite para ceder o imóvel a terceiros. [p=0.5] "
        "{g}Quatro, [p=0.2] dezesseis, [p=0.2] e *três vezes cento e vinte!* [p=0.3] {h}E confira esses limites no texto "
        "atualizado da lei, [p=0.2] porque eles *já mudaram.*"),
    dict(id="09", block="safra", text=
        "{t}E a conta da safra, [p=0.2] que a banca adora. [p=0.4] {a}Cento e vinte pessoas por dia é o *produto:* [p=0.2] "
        "pessoas *vezes* dias, [p=0.2] no ano civil. [p=0.5] {b}Uma pessoa por cento e vinte dias. [p=0.3] {c}Quatro "
        "pessoas por trinta dias. [p=0.3] {d}Dez pessoas por doze dias. [p=0.4] {e}Tudo dentro do limite. [p=0.5] "
        "{f}Mas seis pessoas por vinte e cinco dias? [p=0.3] Dá *cento e cinquenta.* [p=0.3] {g}*Passou!*"),

    # ================= NÃO DESCARACTERIZA =================
    dict(id="10", block="nao_desc", text=
        "{t}Agora, o que *não* tira a condição de segurado especial. [p=0.4] {a}Ceder a terceiros até *metade* do imóvel. "
        "[p=0.3] {b}Fazer *turismo rural,* [p=0.2] com hospedagem, [p=0.2] até cento e vinte dias no ano. [p=0.3] "
        "{c}Participar de *cooperativa.* [p=0.3] {d}Beneficiar a produção de forma *artesanal.* [p=0.4] {e}E receber "
        "*Bolsa Família,* [p=0.2] ou outro programa assistencial. [p=0.4] {f}Isso *cai muito:* [p=0.2] programa "
        "assistencial *não* descaracteriza!"),
    dict(id="11", block="outras_rendas", text=
        "{t}E as outras fontes de renda. [p=0.4] {a}Trabalhar fora, [p=0.2] com remuneração, [p=0.2] por até *cento e "
        "vinte dias* no ano: [p=0.2] pode. [p=0.4] {b}Ser *dirigente sindical* dos trabalhadores rurais: [p=0.2] pode. "
        "[p=0.4] {c}E ser *vereador* do município onde trabalha na roça? [p=0.3] Também pode! [p=0.5] {d}Mas *prefeito?* "
        "[p=0.3] {e}*Não!* [p=0.3] Nem deputado, [p=0.2] nem senador. [p=0.4] {f}Guarde esta frase: [p=0.2] *vereador "
        "sim,* [p=0.2] *prefeito não.*"),

    # ================= DESCARACTERIZA =================
    dict(id="12", block="exclusao", text=
        "{t}E quando ele *perde* a condição? [p=0.3] Aqui a banca cobra até a *data.* [p=0.5] {a}Se ele deixa de cumprir "
        "os requisitos, [p=0.2] vira outro tipo de segurado, [p=0.2] ou entra numa *sociedade empresária,* [p=0.4] {b}a "
        "exclusão vale desde o *primeiro dia do mês* do fato. [p=0.5] {c}Mas, se ele só *estourou um limite,* [p=0.2] "
        "os cento e vinte, [p=0.4] {d}a exclusão vale do primeiro dia do mês *seguinte.* [p=0.5] {e}Condição própria: "
        "[p=0.2] mês *do fato.* [p=0.3] Excesso de limite: [p=0.2] mês *seguinte.*"),

    # ================= CONTRIBUIÇÃO E BENEFÍCIOS =================
    dict(id="13", block="contribuicao", text=
        "{t}E como ele contribui? [p=0.4] {a}*Não* é sobre salário. [p=0.3] {b}É uma alíquota sobre o *resultado da "
        "comercialização da produção.* [p=0.3] Vendeu, [p=0.2] contribui. [p=0.5] {c}Com isso, [p=0.2] os benefícios "
        "saem no valor de *um salário mínimo.* [p=0.4] {d}Mas ele *pode* contribuir também, [p=0.2] facultativamente, "
        "[p=0.2] como contribuinte individual. [p=0.3] {e}E aí, [p=0.2] receber *acima* do mínimo."),
    dict(id="14", block="comprova", text=
        "{t}E o detalhe que muda tudo: [p=0.4] {a}o segurado especial *não* conta contribuições. [p=0.3] {b}Ele *comprova "
        "atividade rural.* [p=0.4] {c}Ainda que de forma *descontínua,* [p=0.2] no período imediatamente anterior ao "
        "pedido, [p=0.2] igual à carência do benefício. [p=0.5] {d}É um regime de *comprovação,* [p=0.2] não de "
        "recolhimento mensal."),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}O filho *menor* de dezesseis anos que trabalha com o grupo é "
        "segurado especial. [p=0.4] {r1}*Errado:* [p=0.2] tem que ser *maior* de dezesseis. [p=0.5] {p2}Usar empregado "
        "permanente *não* descaracteriza a economia familiar. [p=0.4] {r2}*Errado:* [p=0.2] *descaracteriza.* [p=0.5] "
        "{p3}O segurado especial *nunca* recebe mais que um salário mínimo. [p=0.4] {r3}*Errado:* [p=0.2] pode, se "
        "contribuir facultativamente. [p=0.5] {p4}O pescador artesanal pode ser segurado especial. [p=0.4] {r4}*Certo!*"),
    dict(id="16", block="q_ce", text=
        "{t}E uma questão de prova, [p=0.2] nível avançado: [p=0.3] {e}o segurado especial que exerce atividade "
        "remunerada por cento e cinquenta dias no ano civil [p=0.2] é excluído a contar do primeiro dia do mês da "
        "ocorrência. [p=0.6] {r}*Errado!* [p=0.3] {x}Passou dos cento e vinte, [p=0.2] então é excluído, [p=0.2] sim. "
        "[p=0.3] Mas é excesso de limite: [p=0.2] vale o mês *seguinte.*"),

    # ================= O CASO DO JOÃO =================
    dict(id="17", block="caso", text=
        "{t}E agora, [p=0.2] o João! [p=0.4] Vamos testar item por item. [p=0.5] {a}Área de três módulos fiscais? "
        "[p=0.2] Até quatro: [p=0.2] *ok.* [p=0.4] {b}Cinco trabalhadores por vinte dias? [p=0.2] Cem pessoas por dia, "
        "[p=0.2] abaixo de cento e vinte: [p=0.2] *ok.* [p=0.4] {c}Bolsa Família? [p=0.2] Não descaracteriza: [p=0.2] "
        "*ok.* [p=0.4] {d}Vereador do município? [p=0.2] Está na ressalva: [p=0.2] *ok.* [p=0.4] {e}E o filho de "
        "dezessete anos? [p=0.2] Maior de dezesseis: [p=0.2] *ok.* [p=0.5] {f}Resposta: [p=0.2] o João, [p=0.2] a "
        "esposa e o filho [p=0.2] *continuam* segurados especiais! [p=0.5] {g}Agora, [p=0.2] se fossem *sete* "
        "trabalhadores por vinte dias? [p=0.3] Cento e quarenta. [p=0.2] *Aí perdia.*"),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}segurado especial: [p=0.2] artigo onze, [p=0.2] inciso sete, [p=0.2] com base na "
        "Constituição. [p=0.3] {b}Individualmente *ou* em família, [p=0.2] e *sem empregados permanentes.* [p=0.3] "
        "{c}Os números: [p=0.2] quatro, [p=0.2] dezesseis, [p=0.2] e três vezes cento e vinte, [p=0.2] mais cinquenta "
        "por cento. [p=0.3] {d}Vereador sim, [p=0.2] prefeito não. [p=0.3] {e}E ele contribui sobre a *venda da "
        "produção,* [p=0.2] com benefício de um salário mínimo."),
    dict(id="19", block="cta", text=
        "Na próxima aula, [p=0.2] o *segurado facultativo,* [p=0.2] quem está *fora* do RGPS, [p=0.2] e o *quem é quem* "
        "de todos os segurados. [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acertou o caso do João? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
