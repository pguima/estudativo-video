# Roteiro — Seguridade Social 016: Filiação × inscrição (Módulo M12)
# Base: Estudos/Seguridade Social/modulos/M12-filiacao-e-inscricao.md — seções 1 a 9 e questões Q7, Q8, Q10 e Q12
#   Lei 8.213/1991, art. 17 (redação da Lei 13.846/2019) e art. 27, II · Decreto 3.048/1999, arts. 18 e 20.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material avisa: a numeração do Decreto 3.048 já mudou e o art. 17 foi alterado em 2019 — dito na base e no dependente.
# Gancho = o caso do Lucas (Q8): a pergunta abre a aula e a resolução volta no fim.
# A narração foi gravada fora (voz_completa.wav); o texto abaixo segue o que foi realmente falado.

TITULO = "Filiação × inscrição: o fato e a ficha (Lei 8.213, art. 17 · Decreto 3.048, arts. 18 e 20)"

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
    "OGMO": "Ógmo",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "{a}O Lucas trabalha há *três anos* como vendedor *autônomo,* [p=0.2] atendendo direto pessoas físicas. [p=0.4] "
        "{b}Nunca se *inscreveu* no INSS. [p=0.3] {c}Nunca *recolheu* um centavo. [p=0.4] {d}Pergunta: [p=0.2] o Lucas "
        "está *filiado* ao RGPS? [p=0.4] {e}Muita gente responde que *não,* [p=0.2] porque ele nunca se cadastrou nem "
        "pagou. [p=0.4] {f}Guarde a sua resposta. [p=0.3] No fim da aula, [p=0.2] a gente resolve *juntos.*"),

    # ================= BASE LEGAL =================
    dict(id="02", block="base", text=
        "{t}Hoje, [p=0.2] um par de conceitos que é o *campeão de pegadinhas* do bloco de segurados: [p=0.3] "
        "{a}*filiação* e *inscrição.* [p=0.4] {b}A banca *troca* uma palavra pela outra na afirmação [p=0.2] e derruba "
        "candidato bem preparado. [p=0.4] {c}A base está no artigo *dezessete* da Lei oito mil, duzentos e treze, "
        "[p=0.3] {d}e no Decreto três mil e quarenta e oito, [p=0.2] nos artigos *dezoito* e *vinte.* [p=0.4] {e}Os "
        "conceitos são *estáveis,* [p=0.2] mas a *numeração* do Decreto já mudou, [p=0.2] então confira no texto "
        "compilado."),

    # ================= ANALOGIA =================
    dict(id="03", block="academia", text=
        "{t}Pense numa *academia* de ginástica. [p=0.4] {a}A filiação é o *vínculo:* [p=0.2] você começou a treinar, "
        "[p=0.2] está dentro. [p=0.3] É o *fato* que cria direitos e obrigações. [p=0.4] {b}A inscrição é o *cadastro:* "
        "[p=0.2] preenche a ficha, [p=0.2] entrega documentos, [p=0.2] consta no sistema. [p=0.3] É um *ato formal.* "
        "[p=0.4] {c}E você pode estar *filiado* sem estar *inscrito.* [p=0.3] {d}É exatamente o que acontece com "
        "*milhões* de trabalhadores."),

    # ================= DEFINIÇÕES =================
    dict(id="04", block="definicoes", text=
        "{t}Agora, as definições do Decreto. [p=0.4] {a}Filiação é o *vínculo* que se estabelece entre pessoas que "
        "contribuem para a previdência social e esta, [p=0.2] {b}do qual decorrem *direitos e obrigações.* [p=0.4] "
        "{c}Inscrição é o *ato* pelo qual o segurado é *cadastrado* no RGPS, [p=0.2] {d}mediante comprovação dos dados "
        "pessoais e de outros elementos necessários à sua caracterização. [p=0.5] {e}Guarde essa frase: [p=0.2] a "
        "filiação é o *fato.* [p=0.2] A inscrição é a *ficha.* [p=0.4] {f}Filia-se *trabalhando.* [p=0.2] Inscreve-se "
        "*cadastrando.*"),

    # ================= QUANDO OCORRE =================
    dict(id="05", block="quando", text=
        "{t}E quando ocorre a filiação? [p=0.4] {a}Para os *cinco* segurados obrigatórios, [p=0.2] ela é *automática,* "
        "[p=0.2] pelo exercício da atividade remunerada. [p=0.4] {b}Independe de *inscrição,* [p=0.2] {c}independe de "
        "*pagamento,* [p=0.2] {d}e independe da *vontade* do segurado. [p=0.4] {e}Começou a trabalhar com remuneração? "
        "[p=0.2] *Está filiado.* [p=0.5] {f}Já o *facultativo,* [p=0.2] que não exerce atividade obrigatória, [p=0.2] "
        "{g}só se filia com a *inscrição* formalizada, [p=0.2] *mais* o pagamento da *primeira contribuição.*"),

    # ================= PONTO DE OURO =================
    dict(id="06", block="natureza", text=
        "{t}E aqui está o ponto de ouro: [p=0.3] a *natureza* da inscrição. [p=0.4] {a}Para o obrigatório, [p=0.2] ela é "
        "*declaratória:* [p=0.2] só *documenta* um vínculo que já existe. [p=0.4] {b}Para o facultativo, [p=0.2] ela é "
        "*constitutiva:* [p=0.2] sem ela, [p=0.2] não há vínculo nenhum. [p=0.5] {c}Por isso as duas frases que a banca "
        "adora são *falsas.* [p=0.4] {d}A filiação decorre *sempre* do exercício de atividade? [p=0.3] {e}*Errado,* "
        "[p=0.2] por causa do facultativo. [p=0.4] {f}A filiação depende de *prévia inscrição?* [p=0.3] {g}*Errado,* "
        "[p=0.2] para os obrigatórios."),

    # ================= QUEM INSCREVE =================
    dict(id="07", block="quem", text=
        "{t}E quem faz a inscrição? [p=0.4] {a}Do *empregado,* [p=0.2] o *empregador,* [p=0.2] na admissão. [p=0.3] "
        "{b}Do *doméstico,* [p=0.2] o empregador doméstico. [p=0.3] {c}Do *avulso,* [p=0.2] o *sindicato* ou o OGMO. "
        "[p=0.4] {d}E o contribuinte individual, [p=0.2] o segurado especial [p=0.2] e o facultativo [p=0.2] se "
        "inscrevem por *conta própria.* [p=0.4] {e}O segurado especial, [p=0.2] com uma sistemática *própria* de "
        "cadastro."),

    # ================= DEPENDENTE =================
    dict(id="08", block="dependente", text=
        "{t}E o *dependente?* [p=0.4] {a}Atenção: [p=0.2] só o *segurado* se filia. [p=0.3] {b}O dependente *não tem "
        "filiação!* [p=0.4] {c}A relação dele com o RGPS é *derivada.* [p=0.4] {d}Ele apenas *se inscreve,* [p=0.2] "
        "e em regra no momento do *requerimento do benefício,* [p=0.2] não antes. [p=0.5] {e}Então o dependente *não* "
        "precisa estar cadastrado em vida do segurado [p=0.2] para ter direito à *pensão.* [p=0.4] {f}Confira os detalhes "
        "no artigo dezessete da Lei, [p=0.2] que foi alterado em dois mil e dezenove."),

    # ================= PONTOS QUE DERRUBAM =================
    dict(id="09", block="derrubam", text=
        "{t}Mais pontos que derrubam candidato. [p=0.4] {a}A filiação do obrigatório *independe de recolhimento.* "
        "[p=0.4] {b}O empregado continua filiado [p=0.2] mesmo que a empresa *nunca* tenha recolhido. [p=0.4] {c}O "
        "recolhimento é obrigação *dela,* [p=0.2] e a omissão *não prejudica* o empregado. [p=0.5] {d}E inscrição *não "
        "cria* atividade: [p=0.3] {e}se inscrever sem trabalhar *não gera* filiação obrigatória."),

    # ================= TRÊS COISAS =================
    dict(id="10", block="tres", text=
        "{t}E não confunda *três* coisas. [p=0.4] {a}*Filiação* é o *ingresso* no sistema. [p=0.4] {b}*Qualidade de "
        "segurado* é a *manutenção* desse vínculo, [p=0.2] assunto da próxima aula. [p=0.4] {c}E *carência* é o número "
        "mínimo de contribuições, [p=0.2] assunto da aula seguinte. [p=0.5] {d}Isso cai: [p=0.2] a *perda* da qualidade "
        "de segurado [p=0.2] *não desfaz* a filiação anterior, [p=0.3] {e}e não apaga o tempo de contribuição já "
        "cumprido. [p=0.5] {f}Filiação, [p=0.2] qualidade, [p=0.2] carência, [p=0.2] benefício: [p=0.3] a *linha do "
        "tempo* do segurado."),

    # ================= RETROATIVO =================
    dict(id="11", block="retroativo", text=
        "{t}E o facultativo pode *comprar* período anterior à inscrição? [p=0.4] {a}Em regra, [p=0.2] *não.* [p=0.4] "
        "{b}Como o vínculo dele *nasce* com a inscrição e o primeiro pagamento, [p=0.2] {c}não há vínculo anterior "
        "[p=0.2] para amparar recolhimento *retroativo.* [p=0.5] {d}E, para carência, [p=0.2] o artigo vinte e sete, "
        "[p=0.2] inciso dois, [p=0.2] só conta as contribuições a partir do *primeiro pagamento sem atraso.* [p=0.4] "
        "{e}Há *exceções* no regulamento, [p=0.2] então confira antes de afirmar."),

    # ================= PEGADINHAS =================
    dict(id="12", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}*Inscrição* é o vínculo que se estabelece entre o segurado e a "
        "previdência social. [p=0.4] {r1}*Errado:* [p=0.2] esse é o conceito de *filiação.* [p=0.5] {p2}O dependente se "
        "*filia* ao RGPS na mesma data do segurado. [p=0.4] {r2}*Errado:* [p=0.2] dependente não se filia, [p=0.2] só se "
        "*inscreve.* [p=0.5] {p3}O dependente deve se inscrever *previamente,* [p=0.2] sob pena de perder a pensão. "
        "[p=0.4] {r3}*Errado:* [p=0.2] a inscrição ocorre, em regra, [p=0.2] no *requerimento do benefício.* [p=0.5] "
        "{p4}Para o facultativo, [p=0.2] a inscrição tem natureza *constitutiva.* [p=0.4] {r4}*Certo!*"),
    dict(id="13", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}o empregado cuja empresa deixa de recolher as contribuições "
        "previdenciárias [p=0.2] não se considera filiado ao RGPS naquele período. [p=0.6] {r}*Errado!* [p=0.3] "
        "{x}A filiação do obrigatório decorre do exercício da atividade, [p=0.2] e *independe* do recolhimento, [p=0.2] "
        "que é responsabilidade da *empresa.*"),

    # ================= O CASO DO LUCAS =================
    dict(id="14", block="caso", text=
        "{t}E agora, [p=0.2] o Lucas. [p=0.4] {a}Ele trabalha por *conta própria,* [p=0.2] com remuneração: [p=0.3] "
        "{b}é *contribuinte individual,* [p=0.2] segurado *obrigatório.* [p=0.4] {c}Então está *filiado* desde o primeiro "
        "dia da atividade, [p=0.3] mesmo sem inscrição [p=0.2] e sem nenhum recolhimento. [p=0.5] {d}Facultativo ele "
        "*não pode* ser, [p=0.2] porque exerce atividade obrigatória. [p=0.5] {e}Mas cuidado: [p=0.2] estar filiado "
        "*não é* ter direito imediato a benefício. [p=0.4] {f}Ele vai precisar *comprovar* a atividade, [p=0.2] "
        "*recolher* o que deve, [p=0.2] e cumprir *qualidade de segurado* e *carência.*"),

    # ================= FECHAMENTO =================
    dict(id="15", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}filiação é o *vínculo,* [p=0.2] do qual decorrem direitos e obrigações. [p=0.2] "
        "Inscrição é o *cadastro.* [p=0.3] {b}Obrigatórios: [p=0.2] filiação *automática,* [p=0.2] pelo exercício da "
        "atividade, [p=0.2] e inscrição *declaratória.* [p=0.3] {c}Facultativo: [p=0.2] filiação por inscrição *mais* "
        "primeira contribuição, [p=0.2] e inscrição *constitutiva.* [p=0.3] {d}Só o segurado se filia. [p=0.2] O "
        "dependente só se *inscreve,* [p=0.2] em regra no requerimento do benefício. [p=0.3] {e}A filiação é o *fato.* "
        "[p=0.2] A inscrição é a *ficha.*"),
    dict(id="16", block="cta", text=
        "Na próxima aula, [p=0.2] *qualidade de segurado* e *período de graça.* [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que o Lucas *não* estava filiado? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
