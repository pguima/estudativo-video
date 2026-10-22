# Roteiro — Seguridade Social 015: Dependentes, as 3 classes (Módulo M11)
# Base: Estudos/Seguridade Social/modulos/M11-dependentes.md — seções 1 a 6, pegadinhas 1, 3, 8 e 14, questões Q4 e Q7
#   Lei 8.213/1991, art. 16, I a III e §§ 1º, 2º, 4º e 5º · Decreto 3.048/1999, art. 17 (perda da condição).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material avisa: a exceção da colação de grau "CONFERIR NA FONTE OFICIAL — art. 17 do Decreto 3.048/1999". Dito na cena 11.
# Menor sob guarda: só "texto da lei × tribunais", sem citar precedente (o material pede para não citar número sem conferir).
# Gancho = o caso do Antônio (Q7): a pergunta abre a aula e a resolução volta no fim, pelo método das 3 etapas.

TITULO = "Dependentes do INSS: as 3 classes e a regra da exclusão (Lei 8.213, art. 16)"

# Estilo da voz (a narração foi gravada externamente: audio/nova_voz/usuario/voz_completa.wav)
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
        "{a}O Antônio era segurado do INSS [p=0.2] e *faleceu.* [p=0.4] {b}Deixou a *esposa,* [p=0.2] {c}um filho de "
        "*vinte e três* anos, [p=0.2] saudável, [p=0.2] {d}um filho de *dezesseis* anos, [p=0.2] {e}e a *mãe,* [p=0.2] "
        "que dependia dele economicamente. [p=0.4] {f}Quem recebe a *pensão por morte?* [p=0.3] Todo mundo dividindo? "
        "[p=0.3] Só a esposa? [p=0.4] {g}Guarde a sua resposta. [p=0.3] No fim da aula, [p=0.2] a gente resolve *juntos.*"),

    # ================= BASE LEGAL =================
    dict(id="02", block="base", text=
        "{t}Hoje é dia de *dependentes.* [p=0.3] {a}E aqui a banca *não* pergunta a lista: [p=0.2] {b}ela monta um *caso* "
        "[p=0.2] e pergunta *quem recebe.* [p=0.4] {c}A base está no artigo *dezesseis* da Lei oito mil, duzentos e "
        "treze, [p=0.3] {d}e no artigo *dezessete* do Decreto três mil e quarenta e oito, [p=0.2] que trata da *perda* "
        "da condição."),

    # ================= CONCEITO =================
    dict(id="03", block="conceito", text=
        "{t}Primeiro, [p=0.2] o conceito. [p=0.3] {a}Dependente é quem, [p=0.2] pela relação com o segurado, [p=0.2] "
        "recebe prestações em *nome próprio* [p=0.2] quando o segurado *morre* [p=0.2] ou é *preso.* [p=0.4] {b}Os "
        "benefícios exclusivos dele são *dois:* [p=0.2] {c}*pensão por morte* [p=0.2] {d}e *auxílio-reclusão.* [p=0.4] "
        "{e}E o dependente *não contribui.* [p=0.3] O vínculo dele é *derivado* do segurado. [p=0.3] {f}Sem segurado, "
        "[p=0.2] não há dependente."),

    # ================= AS TRÊS CLASSES =================
    dict(id="04", block="classes", text=
        "{t}Agora, [p=0.2] as *três classes.* [p=0.3] {a}Classe *um:* [p=0.2] o cônjuge, [p=0.2] a companheira, "
        "[p=0.2] o companheiro [p=0.2] e o filho não emancipado, [p=0.2] de qualquer condição, [p=0.2] menor de vinte e "
        "um anos, [p=0.2] ou inválido, [p=0.2] ou com deficiência intelectual ou mental, [p=0.2] ou deficiência grave. "
        "[p=0.4] {b}Classe *dois:* [p=0.2] os *pais.* [p=0.4] {c}Classe *três:* [p=0.2] o *irmão,* [p=0.2] com os "
        "mesmos requisitos do filho. [p=0.4] {d}Guarde esta frase: [p=0.2] *família nuclear,* [p=0.2] depois *pais,* "
        "[p=0.2] depois *irmãos.*"),
    dict(id="05", block="exclusao", text=
        "{t}E aqui está o ponto de ouro, [p=0.2] o parágrafo primeiro: [p=0.3] {a}a existência de dependente de "
        "*qualquer* classe [p=0.2] *exclui* do direito às prestações [p=0.2] os das classes *seguintes.* [p=0.4] "
        "{b}*Exclui!* [p=0.3] {c}Não é preferência, [p=0.2] não é prioridade no pagamento. [p=0.3] {d}É *exclusão "
        "total.* [p=0.3] {e}Basta *um* dependente da classe de cima [p=0.2] para *zerar* as de baixo. [p=0.4] {f}E, "
        "dentro da *mesma* classe, [p=0.2] todos concorrem em igualdade, [p=0.2] em *partes iguais.* [p=0.3] {g}O "
        "cônjuge *não* tem preferência sobre o filho."),

    # ================= PRESUMIDA × COMPROVADA =================
    dict(id="06", block="presuncao", text=
        "{t}E a dependência econômica? [p=0.3] Parágrafo quarto: [p=0.2] {a}na classe um, [p=0.2] ela é *presumida.* "
        "[p=0.3] {b}Nas classes dois e três, [p=0.2] os pais e o irmão, [p=0.2] ela precisa ser *comprovada.* [p=0.4] "
        "{c}Classe um *não prova.* [p=0.2] Classes dois e três *provam.* [p=0.4] {d}E a presunção é *relativa:* "
        "[p=0.2] admite prova em contrário. [p=0.3] {e}Por isso, [p=0.2] o filho de dezenove anos que começa a "
        "trabalhar, [p=0.2] ou o cônjuge que passa a ter renda própria, [p=0.2] {f}*não* perdem a condição."),

    # ================= O FILHO =================
    dict(id="07", block="filho", text=
        "{t}Agora, [p=0.2] os requisitos do filho, [p=0.2] que valem também pro *irmão.* [p=0.3] {a}*Não "
        "emancipado,* [p=0.2] {b}mais *uma* destas condições: [p=0.2] menor de vinte e um, [p=0.2] ou inválido, "
        "[p=0.2] ou com deficiência intelectual, mental ou grave. [p=0.4] {c}De qualquer condição quer dizer: [p=0.2] "
        "*biológico,* [p=0.2] *adotivo,* [p=0.2] havido ou não do casamento. [p=0.4] {d}E o filho *inválido* não tem "
        "limite de idade. [p=0.3] {e}Inválido aos *quarenta e cinco* anos? [p=0.3] Continua dependente."),

    # ================= EQUIPARADOS =================
    dict(id="08", block="equiparados", text=
        "{t}E os equiparados a filho, [p=0.2] no parágrafo segundo: [p=0.2] {a}o *enteado* [p=0.2] e o *menor "
        "tutelado.* [p=0.3] {b}Mas com *dois* requisitos juntos: [p=0.2] {c}*declaração* do segurado, [p=0.2] {d}e "
        "*comprovação* da dependência econômica. [p=0.4] {e}A banca adora isso: [p=0.2] eles estão na classe um, "
        "[p=0.2] mas a dependência deles *não* é presumida! [p=0.4] {f}E o menor sob *guarda?* [p=0.3] {g}Foi retirado "
        "do texto da lei em mil novecentos e noventa e sete, [p=0.2] {h}mas os tribunais já reconheceram o direito dele. "
        "[p=0.3] {i}Então leia o comando: [p=0.2] *texto da lei* [p=0.2] ou *entendimento dos tribunais.*"),

    # ================= A PROVA (§5º) =================
    dict(id="09", block="prova", text=
        "{t}E a prova da união estável [p=0.2] e da dependência econômica, [p=0.2] no parágrafo quinto. [p=0.3] "
        "{a}Exige início de *prova material* contemporânea dos fatos, [p=0.2] {b}produzida em até *vinte e quatro "
        "meses* [p=0.2] antes do óbito ou da prisão. [p=0.4] {c}E não se admite a prova *exclusivamente* testemunhal, "
        "[p=0.2] {d}salvo força maior [p=0.2] ou caso fortuito. [p=0.4] {e}Repare: [p=0.2] testemunha *pode.* "
        "[p=0.2] O que não pode é *só* testemunha."),

    # ================= PERDA DA CONDIÇÃO =================
    dict(id="10", block="perda", text=
        "{t}Agora, [p=0.2] a *perda* da condição. [p=0.3] {a}O filho e o irmão perdem aos *vinte e um* anos, [p=0.2] "
        "salvo se inválidos ou com deficiência. [p=0.4] {b}E *não* existe prorrogação por faculdade! [p=0.3] {c}Isso é "
        "regra do *Imposto de Renda,* [p=0.2] não do INSS. [p=0.4] {d}O cônjuge perde com a *separação* ou o "
        "*divórcio,* [p=0.2] {e}salvo se recebia *pensão alimentícia.* [p=0.4] {f}E todos perdem pela cessação da "
        "invalidez, [p=0.2] ou pelo falecimento."),
    dict(id="11", block="emancipacao", text=
        "{t}E a emancipação, [p=0.2] que é pegadinha de ouro. [p=0.3] {a}Emancipou? [p=0.2] *Perde* a condição, "
        "[p=0.2] {b}*ainda que seja inválido.* [p=0.4] {c}O *casamento* emancipa: [p=0.2] filho de vinte anos que "
        "casou, [p=0.2] *perdeu.* [p=0.4] {d}Mas há uma *exceção* no Decreto: [p=0.2] {e}a emancipação por *colação de "
        "grau* em curso de ensino superior [p=0.2] *não* faz perder. [p=0.4] {f}Confira essa exceção no texto "
        "atualizado do artigo dezessete do Decreto, [p=0.2] mas saiba que ela *cai.*"),

    # ================= PEGADINHAS =================
    dict(id="12", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}Havendo cônjuge e pais, [p=0.2] o benefício é *rateado* entre "
        "todos. [p=0.4] {r1}*Errado:* [p=0.2] as classes são excludentes, [p=0.2] os pais não recebem nada. [p=0.5] "
        "{p2}A dependência econômica dos pais é *presumida.* [p=0.4] {r2}*Errado:* [p=0.2] é *comprovada.* [p=0.5] "
        "{p3}O filho universitário mantém a condição até os *vinte e quatro* anos. [p=0.4] {r3}*Errado:* [p=0.2] não há "
        "prorrogação por estudo. [p=0.5] {p4}O ex-cônjuge que recebia pensão alimentícia [p=0.2] mantém a condição de "
        "dependente. [p=0.4] {r4}*Certo!*"),
    dict(id="13", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}o enteado e o menor tutelado equiparam-se a filho mediante declaração do "
        "segurado, [p=0.2] sendo sua dependência econômica presumida [p=0.2] por integrarem a primeira classe. [p=0.6] "
        "{r}*Errado!* [p=0.3] {x}A equiparação exige declaração [p=0.2] e também *comprovação* da dependência "
        "econômica. [p=0.3] A presunção *não* alcança os dois."),

    # ================= O CASO DO ANTÔNIO =================
    dict(id="14", block="caso", text=
        "{t}E agora, [p=0.2] o Antônio! [p=0.3] {m}Vamos pelo método: [p=0.2] identifique a *classe* de cada um, "
        "[p=0.2] aplique a *exclusão,* [p=0.2] e divida em *partes iguais.* [p=0.4] {a}O filho de vinte e três anos, "
        "[p=0.2] capaz, [p=0.2] perdeu a condição aos vinte e um. [p=0.2] {a2}*Fora.* [p=0.4] {b}A mãe é classe *dois,* "
        "[p=0.2] e há dependentes na classe um. [p=0.2] {b2}Mesmo comprovando a dependência, [p=0.2] está *excluída.* "
        "[p=0.4] {c}Sobram a esposa e o filho de dezesseis: [p=0.2] {c2}*cinquenta por cento* para cada. [p=0.5] {d}E se "
        "o filho de vinte e três fosse *inválido?* [p=0.3] {d2}Aí entraria, [p=0.2] e seriam *três* partes iguais."),

    # ================= FECHAMENTO =================
    dict(id="15", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}três classes, [p=0.2] *excludentes.* [p=0.3] {b}Classe um: [p=0.2] cônjuge, "
        "companheiro e filho, [p=0.2] com dependência *presumida.* [p=0.3] {c}Classe dois: [p=0.2] pais. [p=0.2] "
        "Classe três: [p=0.2] irmão. [p=0.2] Essas duas, [p=0.2] *comprovada.* [p=0.3] {d}Dentro da classe, [p=0.2] "
        "partes iguais. [p=0.3] {e}Enteado e tutelado: [p=0.2] declaração *mais* comprovação. [p=0.3] {f}Prova material "
        "de até vinte e quatro meses, [p=0.2] nunca só testemunhal. [p=0.3] {g}Vinte e um anos, [p=0.2] sem "
        "prorrogação por faculdade. [p=0.3] {h}E a emancipação faz perder, [p=0.2] ainda que inválido."),
    dict(id="16", block="cta", text=
        "Na próxima aula, [p=0.2] *filiação* e *inscrição:* [p=0.2] a diferença que a banca adora cobrar. [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acertou quem recebe a pensão do Antônio? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
