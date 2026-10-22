# Roteiro — Seguridade Social 017: Qualidade de segurado e período de graça (Módulo M13)
# Base: Estudos/Seguridade Social/modulos/M13-qualidade-de-segurado-e-periodo-de-graca.md — seções 1 a 8, pegadinhas e questões Q4, Q8
#   Lei 8.213/1991, art. 15, I a VI e §§ 1º a 4º · art. 27-A · Lei 10.666/2003, art. 3º e §1º.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material avisa: a ressalva do auxílio-acidente (inciso I) veio por alteração posterior — "confira o texto compilado" (dito na cena 06);
#   o dia exato da perda depende do prazo de recolhimento — "guarde a mecânica, não o dia" (cena 09);
#   a aposentadoria por tempo de contribuição foi extinta pela EC 103/2019 (transição e direito adquirido) — cena 11.
# Gancho = o caso do Carlos (Q8): a pergunta abre a aula e a resolução volta no fim, degrau por degrau.

TITULO = "Período de graça: 12, 24 ou 36 meses? Qualidade de segurado (Lei 8.213, art. 15)"

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
        "{a}O Carlos foi empregado por *quinze* anos, [p=0.2] {b}com *cento e oitenta* contribuições sem interrupção. "
        "[p=0.4] {c}Foi demitido, [p=0.2] e se registrou como *desempregado* no órgão próprio do Ministério do Trabalho. "
        "[p=0.5] {d}Por quanto tempo ele continua *protegido* pelo INSS? [p=0.4] {e}Doze meses? [p=0.2] Vinte e quatro? "
        "[p=0.4] {f}Guarde a sua resposta. [p=0.3] No fim da aula, [p=0.2] a gente resolve *juntos.*"),

    # ================= BASE LEGAL =================
    dict(id="02", block="base", text=
        "{t}Hoje é aula de *números.* [p=0.4] {a}Qualidade de segurado e período de graça, [p=0.2] no artigo *quinze* da "
        "Lei oito mil, duzentos e treze. [p=0.5] {b}A banca cobra o *prazo,* [p=0.2] {c}as *prorrogações* [p=0.2] {d}e até "
        "a *data exata* da perda."),

    # ================= CONCEITO =================
    dict(id="03", block="conceito", text=
        "{t}Primeiro, o conceito. [p=0.3] Qualidade de segurado é a condição de quem está *coberto* pela previdência. "
        "[p=0.3] É a *vigência* do seguro. [p=0.4] {a}A filiação é o *ingresso.* [p=0.3] {b}A qualidade é a *manutenção* "
        "da cobertura. [p=0.3] {c}E a carência é o *tempo mínimo* de contribuição. [p=0.4] {d}E, em regra, [p=0.2] sem "
        "qualidade de segurado *não há benefício.* [p=0.5] {e}E o período de graça é o intervalo em que o segurado continua "
        "protegido *mesmo sem contribuir.* [p=0.4] {f}O caput do artigo quinze diz: [p=0.2] {g}mantém a qualidade de "
        "segurado, [p=0.2] *independentemente de contribuições.* [p=0.4] {h}E, durante esses prazos, [p=0.2] diz o "
        "parágrafo terceiro, [p=0.2] o segurado conserva *todos os seus direitos* perante a previdência."),

    # ================= OS SEIS INCISOS =================
    dict(id="04", block="incisos", text=
        "{t}Agora, os *seis* incisos. [p=0.4] {a}Um: [p=0.2] quem está em gozo de benefício, [p=0.2] *sem limite de "
        "prazo.* [p=0.4] {b}Dois: [p=0.2] quem deixou de exercer atividade remunerada, [p=0.2] ou está suspenso ou "
        "licenciado sem remuneração, [p=0.2] *doze meses.* [p=0.4] {c}Três: [p=0.2] doença de segregação compulsória, "
        "[p=0.2] *doze meses* após cessar a segregação. [p=0.4] {d}Quatro: [p=0.2] o preso, [p=0.2] *doze meses* após o "
        "livramento. [p=0.4] {e}Cinco: [p=0.2] o serviço militar, [p=0.2] *três meses* após o licenciamento. [p=0.4] "
        "{f}E seis: [p=0.2] o facultativo, [p=0.2] *seis meses.*"),
    dict(id="05", block="frase", text=
        "{t}Guarde essa frase: [p=0.3] {a}*três* é o militar, [p=0.2] o mais curto. [p=0.3] {b}*Seis* é o facultativo. "
        "[p=0.3] {c}*Doze* é todo o resto. [p=0.3] {d}E *infinito* é quem já está recebendo. [p=0.5] {e}E repare nos "
        "termos iniciais, [p=0.2] que a banca adora trocar. [p=0.4] {f}O preso: [p=0.2] doze meses depois de *solto,* "
        "[p=0.2] {g}não da prisão. [p=0.4] {h}O militar: [p=0.2] três meses depois do *licenciamento,* [p=0.2] {i}não da "
        "incorporação."),
    dict(id="06", block="acidente", text=
        "{t}E a exceção do inciso um: [p=0.3] {a}quem recebe benefício mantém a qualidade sem limite, [p=0.2] {b}*exceto* "
        "no *auxílio-acidente.* [p=0.4] {c}Por quê? [p=0.3] {d}Ele é *indenizatório* [p=0.2] {e}e pago *junto com o "
        "salário:* [p=0.2] quem recebe *continua trabalhando.* [p=0.5] {f}Essa ressalva entrou depois, [p=0.2] por "
        "alteração da lei, [p=0.2] então confira o texto compilado."),

    # ================= PRORROGAÇÕES =================
    dict(id="07", block="prorrog", text=
        "{t}Agora, as *duas* prorrogações. [p=0.4] {a}Parágrafo primeiro: [p=0.2] os doze meses do inciso dois passam "
        "para *vinte e quatro,* [p=0.2] {b}se o segurado já pagou *mais de cento e vinte* contribuições mensais, [p=0.2] "
        "sem interrupção que acarrete a perda da qualidade. [p=0.4] {c}Atenção: [p=0.2] *mais de* cento e vinte! [p=0.3] "
        "Cento e vinte exatas *não bastam.* [p=0.5] {d}Parágrafo segundo: [p=0.2] *mais doze meses* para o desempregado, "
        "[p=0.2] {e}comprovado pelo *registro* no órgão próprio do Ministério do Trabalho. [p=0.4] {f}Se a questão pedir "
        "a lei, [p=0.2] é o *registro.*"),
    dict(id="08", block="escada", text=
        "{t}E aqui está o ponto de ouro: [p=0.2] a *escada.* [p=0.3] {a}Doze, [p=0.2] vinte e quatro, [p=0.2] trinta e "
        "seis. [p=0.4] {b}Doze é a regra. [p=0.3] {c}Vinte e quatro, [p=0.2] com mais de cento e vinte contribuições, "
        "[p=0.2] *ou* com o desemprego. [p=0.3] {d}Trinta e seis, [p=0.2] com as *duas coisas juntas.* [p=0.4] {e}Então o "
        "período de graça pode chegar a *trinta e seis meses.* [p=0.4] {f}E as prorrogações *só* alcançam o inciso dois. "
        "[p=0.3] {g}Militar e facultativo *não sobem a escada.*"),

    # ================= A DATA DA PERDA =================
    dict(id="09", block="perda", text=
        "{t}E quando, *exatamente,* ele perde a qualidade? [p=0.3] {a}Não é no dia seguinte ao fim do prazo! [p=0.4] "
        "{b}Parágrafo quarto: [p=0.2] a perda ocorre no dia seguinte ao término do prazo para recolher a contribuição "
        "referente ao *mês imediatamente posterior* ao fim do período de graça. [p=0.5] {c}Ou seja: [p=0.2] acabou o prazo, "
        "[p=0.2] {d}vá ao *mês seguinte,* [p=0.2] {e}veja o *vencimento* da contribuição dele, [p=0.2] {f}e a perda é no "
        "*dia seguinte.* [p=0.4] {g}O dia exato depende da categoria, [p=0.2] então guarde a *mecânica,* [p=0.2] não o dia."),

    # ================= RECUPERAÇÃO =================
    dict(id="10", block="art27a", text=
        "{t}E se ele perdeu, [p=0.2] e depois voltou? [p=0.3] {a}Artigo vinte e sete A: [p=0.2] precisa cumprir *metade* "
        "da carência, [p=0.2] a partir da nova filiação. [p=0.4] {b}Auxílio por incapacidade temporária e aposentadoria "
        "por incapacidade permanente: [p=0.2] *seis* contribuições, [p=0.2] em vez de doze. [p=0.3] {c}Salário-maternidade: "
        "[p=0.2] *cinco,* [p=0.2] em vez de dez. [p=0.3] {d}Auxílio-reclusão: [p=0.2] *doze,* [p=0.2] em vez de vinte e "
        "quatro. [p=0.4] {e}Mas a aposentadoria *por idade* fica de fora! [p=0.4] {f}E a perda *não apaga* o tempo de "
        "contribuição já cumprido."),
    dict(id="11", block="lei10666", text=
        "{t}E há casos em que a perda *nem importa.* [p=0.3] {a}Lei dez mil, seiscentos e sessenta e seis, [p=0.2] artigo "
        "terceiro: [p=0.2] a perda da qualidade *não é considerada* [p=0.2] {b}para a aposentadoria por *tempo de "
        "contribuição* [p=0.2] {c}e para a *especial.* [p=0.4] {d}E, na aposentadoria *por idade,* [p=0.2] também não, "
        "[p=0.2] desde que o segurado já tenha a *carência* exigida. [p=0.4] {e}E lembre: [p=0.2] a aposentadoria por "
        "tempo de contribuição foi extinta pela Emenda cento e três, [p=0.2] e sobrevive na *transição* e no *direito "
        "adquirido.*"),

    # ================= PEGADINHAS =================
    dict(id="12", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}O facultativo mantém a qualidade por *doze* meses após cessar as "
        "contribuições. [p=0.4] {r1}*Errado:* [p=0.2] *seis* meses. [p=0.5] {p2}O período de graça é de, [p=0.2] no "
        "máximo, [p=0.2] *vinte e quatro* meses. [p=0.4] {r2}*Errado:* [p=0.2] pode chegar a *trinta e seis.* [p=0.5] "
        "{p3}Quem recebe *qualquer* benefício mantém a qualidade sem limite de prazo. [p=0.4] {r3}*Errado:* [p=0.2] exceto "
        "o *auxílio-acidente.* [p=0.5] {p4}A perda da qualidade não é considerada para a aposentadoria especial. [p=0.4] "
        "{r4}*Certo!*"),
    dict(id="13", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}o prazo do inciso dois será prorrogado para até vinte e quatro meses [p=0.2] "
        "se o segurado já tiver pago cento e vinte contribuições mensais, [p=0.2] sem interrupção que acarrete a perda da "
        "qualidade. [p=0.6] {r}*Errado!* [p=0.3] {x}A lei exige *mais de* cento e vinte. [p=0.3] No mínimo, [p=0.2] *cento "
        "e vinte e uma.*"),

    # ================= O CASO DO CARLOS =================
    dict(id="14", block="caso", text=
        "{t}E agora, [p=0.2] o Carlos. [p=0.4] {a}Prazo básico do inciso dois: [p=0.2] *doze meses.* [p=0.4] {b}Ele tem "
        "cento e oitenta contribuições sem interrupção, [p=0.2] mais de cento e vinte: [p=0.2] sobe para *vinte e quatro.* "
        "[p=0.4] {c}E está registrado como desempregado: [p=0.2] *mais doze.* [p=0.4] {d}Total: [p=0.2] *trinta e seis "
        "meses!* [p=0.5] {e}Com só *cem* contribuições, [p=0.2] seriam vinte e quatro."),

    # ================= FECHAMENTO =================
    dict(id="15", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}período de graça, [p=0.2] artigo quinze: [p=0.2] infinito, [p=0.2] doze, [p=0.2] doze, "
        "[p=0.2] doze, [p=0.2] três e seis. [p=0.3] {b}Exceto o auxílio-acidente no inciso um. [p=0.3] {c}Preso, [p=0.2] "
        "após o livramento. [p=0.2] Militar, [p=0.2] após o licenciamento. [p=0.2] Facultativo, [p=0.2] seis meses. "
        "[p=0.3] {d}A escada: [p=0.2] doze, [p=0.2] vinte e quatro, [p=0.2] trinta e seis, [p=0.2] só no inciso dois. "
        "[p=0.3] {e}A perda é no dia seguinte ao vencimento da contribuição do mês seguinte. [p=0.3] {f}E, se perdeu e "
        "voltou: [p=0.2] *metade* da carência, [p=0.2] menos na aposentadoria por idade."),
    dict(id="16", block="cta", text=
        "Na próxima aula, [p=0.2] a *carência:* [p=0.2] quantas contribuições cada benefício exige. [p=0.3] Ela *fecha* a "
        "Temporada dois. [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você chegou aos *trinta e seis meses* do Carlos? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
