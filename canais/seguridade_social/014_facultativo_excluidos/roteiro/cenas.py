# Roteiro — Seguridade Social 014: Facultativo, excluídos e o "quem é quem" (Módulo M10)
# Base: Estudos/Seguridade Social/modulos/M10-facultativo-excluidos-e-quem-e-quem.md — seções 1 a 4 e questões Q4, Q8 e quadro 1.7
#   Lei 8.213/1991, arts. 12 e 13 · Decreto 3.048/1999, art. 11 · CF, art. 201, §5º · EC 20/1998.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material avisa: alíquotas (plano simplificado, facultativo de baixa renda) mudam: "confira o valor atualizado" (cena 08).
# Gancho = o caso da Renata (Q8): a pergunta abre a aula e a resolução volta no fim.
# Fecha o bloco de segurados (Aulas 10 a 14). Próxima: Aula 15, dependentes.

TITULO = "Segurado facultativo, excluídos do RGPS e o quem é quem (Lei 8.213, arts. 12 e 13)"

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
        "{a}A Renata tem trinta anos, [p=0.2] é *dona de casa* e, em janeiro, [p=0.2] começou a contribuir para o INSS "
        "como segurada *facultativa.* [p=0.4] {b}Em julho, [p=0.2] foi contratada por uma empresa, [p=0.2] com *carteira "
        "assinada.* [p=0.5] {c}E agora? [p=0.3] Ela continua facultativa? [p=0.3] {d}Fica com as *duas* filiações ao "
        "mesmo tempo? [p=0.3] {e}Ou pode *escolher?* [p=0.5] {f}Guarde a sua resposta. [p=0.3] No fim da aula, [p=0.2] "
        "a gente resolve *juntos.*"),

    # ================= BASE LEGAL =================
    dict(id="02", block="base", text=
        "{t}Hoje a gente *fecha* o bloco de segurados. [p=0.4] {a}O *sexto* segurado, [p=0.2] o facultativo, [p=0.2] está "
        "no artigo *treze* da Lei oito mil, duzentos e treze, [p=0.2] e no artigo onze do Decreto três mil e quarenta e "
        "oito. [p=0.4] {b}E quem está *fora* do RGPS [p=0.2] está no artigo *doze* da mesma lei. [p=0.4] {c}E, no fim, "
        "[p=0.2] a tabela do *quem é quem.*"),

    # ================= CONCEITO =================
    dict(id="03", block="conceito", text=
        "{t}Primeiro, o conceito. [p=0.3] {a}Segurado facultativo é quem se filia ao RGPS *mediante contribuição,* "
        "[p=0.2] desde que *não* esteja incluído no artigo onze. [p=0.3] Ou seja, [p=0.2] desde que não seja segurado "
        "*obrigatório.* [p=0.4] {b}Daí saem os *três* requisitos. [p=0.3] {r1}Um: [p=0.2] *idade mínima.* [p=0.3] "
        "{r2}Dois: [p=0.2] *contribuição.* [p=0.3] {r3}E três: [p=0.2] *não* exercer atividade que o enquadre como "
        "obrigatório. [p=0.4] {c}Guarde esta frase: [p=0.2] facultativo é quem *pode não estar.* [p=0.3] {d}Obrigatório "
        "é quem *não pode escolher.*"),

    # ================= 14 x 16 =================
    dict(id="04", block="idade", text=
        "{t}E aqui está a pegadinha mais *sofisticada* do bloco: [p=0.2] a idade. [p=0.4] {a}O texto do artigo treze, "
        "[p=0.2] que é de mil novecentos e noventa e um, [p=0.2] ainda diz *maior de quatorze anos.* [p=0.3] {b}Ele "
        "*nunca* foi atualizado! [p=0.4] {c}Mas a Emenda Constitucional vinte, [p=0.2] de mil novecentos e noventa e "
        "oito, [p=0.2] elevou a idade mínima para o trabalho a *dezesseis* anos, [p=0.2] quatorze só como *aprendiz.* "
        "[p=0.4] {d}E o Decreto três mil e quarenta e oito [p=0.2] fixou o facultativo em *maior de dezesseis.* [p=0.4] "
        "{e}Então, como responder? [p=0.3] {f}Se a questão pedir a *literalidade* da lei, [p=0.2] é *quatorze.* [p=0.3] "
        "{g}Se falar no *Decreto,* [p=0.2] ou na idade *aplicável,* [p=0.2] é *dezesseis.* [p=0.3] {h}Sem especificação "
        "nenhuma? [p=0.3] *Dezesseis.* [p=0.3] {i}Isso cai."),

    # ================= QUEM PODE / QUEM NÃO =================
    dict(id="05", block="quem", text=
        "{t}E quem *pode* ser facultativo? [p=0.4] {a}A *dona de casa,* [p=0.2] {b}o *estudante* maior de dezesseis, "
        "[p=0.2] {c}o *desempregado* que perdeu a qualidade de segurado. [p=0.3] {d}E o *síndico não remunerado!* "
        "[p=0.3] Sem remuneração, [p=0.2] ele não é contribuinte individual, [p=0.2] então pode entrar como facultativo. "
        "[p=0.4] {e}E agora, [p=0.2] quem *não* pode? [p=0.3] {f}Quem já exerce atividade remunerada que gera filiação "
        "*obrigatória.* [p=0.3] {g}E o participante de *regime próprio.*"),
    dict(id="06", block="vedacao", text=
        "{t}Essa segunda vedação está na Constituição, [p=0.2] artigo duzentos e um, [p=0.2] parágrafo quinto: [p=0.3] "
        "{a}é *vedada* a filiação ao regime geral, [p=0.2] {b}na qualidade de segurado *facultativo,* [p=0.2] {c}de pessoa "
        "participante de *regime próprio.* [p=0.5] {d}Mas atenção à precisão: [p=0.2] a vedação é *só como facultativo.* "
        "[p=0.4] {e}O servidor com regime próprio que também trabalha na iniciativa privada [p=0.2] pode, sim, [p=0.2] "
        "ser segurado *obrigatório* do RGPS por essa atividade."),

    # ================= FILIAÇÃO =================
    dict(id="07", block="filiacao", text=
        "{t}E agora o ponto que *mais cai.* [p=0.3] E aqui está o ponto de ouro: [p=0.2] a *filiação.* [p=0.4] {a}Para os "
        "segurados obrigatórios, [p=0.2] a filiação é *automática:* [p=0.2] decorre do exercício da atividade remunerada, "
        "[p=0.2] independe de inscrição e de pagamento. [p=0.4] {b}Para o facultativo, [p=0.2] *não!* [p=0.3] Ele só se "
        "filia com a *inscrição* formalizada, [p=0.2] mais o *pagamento da primeira contribuição.* [p=0.4] {c}É a *única* "
        "categoria sem filiação automática. [p=0.4] {d}Guarde esta frase: [p=0.2] só o facultativo precisa *pagar para "
        "entrar.* [p=0.3] {e}Todos os outros entram *só por trabalhar.*"),

    # ================= CONTRIBUIÇÃO =================
    dict(id="08", block="contribuicao", text=
        "{t}E quem recolhe a contribuição do facultativo? [p=0.3] {a}*Ele mesmo.* [p=0.3] {b}Sobre um salário de "
        "contribuição que *ele escolhe,* [p=0.2] entre o *mínimo* e o *teto.* [p=0.4] {c}E o *risco* de não recolher "
        "[p=0.2] é todo dele. [p=0.4] {d}Sobre alíquotas, [p=0.2] como a do plano simplificado [p=0.2] e a do facultativo "
        "de baixa renda, [p=0.2] *confira sempre* o valor atualizado, [p=0.2] porque mudam por norma e pelo salário mínimo."),

    # ================= EXCLUÍDOS =================
    dict(id="09", block="excluidos", text=
        "{t}Agora, os *excluídos,* [p=0.2] no artigo doze. [p=0.4] {a}O servidor civil ocupante de *cargo efetivo,* "
        "[p=0.2] e o *militar,* [p=0.2] da União, [p=0.2] dos Estados, [p=0.2] do Distrito Federal e dos Municípios, "
        "[p=0.3] {b}são *excluídos* do RGPS, [p=0.3] {c}*desde que amparados por regime próprio.* [p=0.4] {d}Essa "
        "expressão é a *chave!* [p=0.3] A exclusão é *condicionada.* [p=0.4] {e}Município que não instituiu regime próprio? "
        "[p=0.3] {f}O servidor efetivo de lá [p=0.2] é segurado *obrigatório* do RGPS."),
    dict(id="10", block="servidor", text=
        "{t}E o parágrafo único resolve o caso clássico: [p=0.3] {a}se o servidor ou o militar exercer, [p=0.2] *ao "
        "mesmo tempo,* [p=0.2] atividade abrangida pelo RGPS, [p=0.2] vira segurado *obrigatório* em relação a essa "
        "atividade. [p=0.4] {b}E mais dois casos que a banca adora. [p=0.3] {c}Quem ocupa *exclusivamente* cargo em "
        "comissão [p=0.2] é segurado *empregado* do RGPS. [p=0.4] {d}E o empregado público *celetista,* [p=0.2] de empresa "
        "pública ou sociedade de economia mista, [p=0.2] também é empregado do RGPS. [p=0.3] {e}*Não* é excluído."),

    # ================= QUEM É QUEM =================
    dict(id="11", block="tabela", text=
        "{t}E agora, [p=0.2] a tabela do *quem é quem,* [p=0.2] nas três linhas que mais caem. [p=0.4] {a}Filiação: "
        "[p=0.2] automática para empregado, [p=0.2] doméstico, [p=0.2] contribuinte individual, [p=0.2] avulso e especial. "
        "[p=0.3] {a2}Só o facultativo entra por *inscrição mais primeira contribuição.* [p=0.4] {b}Quem recolhe: [p=0.2] "
        "empregado, [p=0.2] doméstico e avulso *não* recolhem para si. [p=0.3] {b2}O contribuinte individual e o "
        "facultativo, [p=0.2] *sim.* [p=0.4] {c}E o período de graça: [p=0.2] {c2}o facultativo tem *seis* meses. "
        "[p=0.3] {c3}Todos os demais, [p=0.2] *doze.*"),

    # ================= PEGADINHAS =================
    dict(id="12", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}É segurado facultativo o maior de *dezoito* anos que se filiar "
        "mediante contribuição. [p=0.4] {r1}*Errado:* [p=0.2] *dezesseis,* [p=0.2] pelo Decreto. [p=0.5] {p2}O "
        "participante de regime próprio pode se filiar ao RGPS como facultativo, [p=0.2] para ampliar sua proteção. "
        "[p=0.4] {r2}*Errado:* [p=0.2] é *vedado* pela Constituição. [p=0.5] {p3}A dona de casa é segurada *obrigatória.* "
        "[p=0.4] {r3}*Errado:* [p=0.2] ela é *facultativa,* [p=0.2] se quiser se filiar. [p=0.5] {p4}O síndico não "
        "remunerado pode ser facultativo. [p=0.4] {r4}*Certo!*"),
    dict(id="13", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}a filiação ao Regime Geral de Previdência Social é *sempre* automática, "
        "[p=0.2] decorrendo do exercício de atividade remunerada. [p=0.6] {r}*Errado!* [p=0.3] {x}Isso vale para os "
        "*obrigatórios.* [p=0.3] O facultativo se filia pela *inscrição,* [p=0.2] com o pagamento da primeira contribuição."),

    # ================= O CASO DA RENATA =================
    dict(id="14", block="caso", text=
        "{t}E agora, [p=0.2] a Renata! [p=0.4] {a}O artigo treze exige, [p=0.2] *o tempo todo,* [p=0.2] que o facultativo "
        "*não* esteja no artigo onze. [p=0.4] {b}Em julho, [p=0.2] ela virou *empregada:* [p=0.2] filiação obrigatória e "
        "automática. [p=0.4] {c}Então a condição de facultativa *acaba.* [p=0.4] {d}Não existe opção, [p=0.2] nem dupla "
        "filiação aqui: [p=0.2] o *obrigatório prevalece.* [p=0.4] {e}E nem precisa de nova inscrição: [p=0.2] quem "
        "inscreve o empregado [p=0.2] é o *empregador.*"),

    # ================= FECHAMENTO =================
    dict(id="15", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}facultativo, [p=0.2] artigo treze: [p=0.2] maior de *dezesseis,* [p=0.2] pelo Decreto, "
        "[p=0.2] e quatorze na literalidade da lei. [p=0.3] {b}Mediante contribuição, [p=0.2] e *sem* atividade "
        "obrigatória. [p=0.3] {c}Filiação por *inscrição mais primeira contribuição,* [p=0.2] a única não automática. "
        "[p=0.3] {d}Período de graça de *seis* meses. [p=0.3] {e}Regime próprio *não* pode ser facultativo. [p=0.3] "
        "{f}E os excluídos do artigo doze: [p=0.2] servidor efetivo e militar, [p=0.2] *só se amparados por regime "
        "próprio.*"),
    dict(id="16", block="cta", text=
        "Na próxima aula, [p=0.2] os *dependentes* [p=0.2] e as suas *três classes.* [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acertou o caso da Renata? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
