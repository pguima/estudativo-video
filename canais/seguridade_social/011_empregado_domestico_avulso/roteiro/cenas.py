# Roteiro — Seguridade Social 011: Empregado, empregado doméstico e avulso (Módulo M08)
# Base: Estudos/Seguridade Social/modulos/M08-segurados-empregado-domestico-avulso.md
#   Lei 8.213/1991, art. 11, I, II e VI · LC 150/2015, art. 1º · CF, art. 7º, XXXIV
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material pede para NÃO decorar as letras das alíneas finais do art. 11, I ("o que cai é o conteúdo"):
#   cargo em comissão e mandato eletivo são citados pelo conteúdo, sem a letra.
# Macetes: P-P-N-S-O (empregado) · C-P-R-S-2 (doméstico) · P-S-I (avulso) · "E-E-A não recolhem; C-F recolhem".

TITULO = "Empregado, empregado doméstico e avulso: como enquadrar (Lei 8.213, art. 11, I, II e VI)"

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
    "RPPS": "R P P S",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "{a}A banca do INSS quase nunca pergunta: [p=0.2] o gari é empregado? [p=0.5] {b}Ela *descreve uma situação,* "
        "[p=0.3] e *você* tem que enquadrar. [p=0.5] {c}Hoje você vai aprender a fazer isso com três categorias: [p=0.3] "
        "{d}o *empregado,* [p=0.2] o *doméstico* [p=0.2] e o *avulso.* [p=0.4] {e}E para cada um, [p=0.2] *uma pergunta* "
        "que resolve a questão."),
    dict(id="02", block="mapa", text=
        "{t}Todos estão no artigo *onze* da Lei oito mil, duzentos e treze. [p=0.4] {a}O empregado é o inciso *um.* [p=0.3] "
        "{b}O doméstico, [p=0.2] o inciso *dois.* [p=0.3] {c}E o avulso, [p=0.2] o inciso *seis.* [p=0.4] "
        "{d}E a regra de ouro do estudo: [p=0.2] *nunca* decore pelo nome. [p=0.3] Decore pelos *elementos.*"),

    # ================= EMPREGADO =================
    dict(id="03", block="emp_conceito", text=
        "{t}Começando pelo *empregado.* [p=0.3] {a}A lei diz: [p=0.2] é aquele que presta serviço de natureza urbana ou rural "
        "*à empresa,* [p=0.3] {b}em caráter *não eventual,* [p=0.3] {c}sob sua *subordinação* [p=0.3] {d}e mediante "
        "*remuneração,* [p=0.3] {e}inclusive como *diretor empregado.*"),
    dict(id="04", block="ppnso", text=
        "{t}Daí saem os *cinco elementos.* [p=0.4] {a}*Pessoa física:* [p=0.2] empresa nunca é empregado. [p=0.3] "
        "{b}*Pessoalidade:* [p=0.2] ele mesmo trabalha, [p=0.2] sem mandar outro no lugar. [p=0.3] {c}*Não eventualidade:* "
        "[p=0.2] é habitual. [p=0.3] {d}*Subordinação:* [p=0.2] recebe ordens. [p=0.3] {e}E *onerosidade:* [p=0.2] "
        "é pago. [p=0.5] {m}O macete: [p=0.2] *P, P, N, S, O.*"),
    dict(id="05", block="subordinacao", text=
        "{t}E agora, o ponto de ouro. [p=0.4] {a}Um desses elementos decide quase todas as questões: [p=0.3] "
        "{b}a *subordinação!* [p=0.5] {c}Tem subordinação? [p=0.2] *Empregado.* [p=0.4] {d}Não tem? [p=0.2] "
        "É *contribuinte individual,* [p=0.2] o autônomo."),
    dict(id="06", block="diretor", text=
        "{t}E a lei manda para o grupo do empregado algumas figuras que a banca adora. [p=0.4] {a}Primeira: [p=0.2] o *diretor.* "
        "[p=0.3] {b}Diretor *empregado* [p=0.2] é *empregado.* [p=0.4] {c}Mas o diretor *não* empregado [p=0.2] é "
        "*contribuinte individual.* [p=0.4] {d}Uma palavrinha muda tudo!"),
    dict(id="07", block="temporario", text=
        "{t}Segunda: [p=0.2] o *trabalhador temporário.* [p=0.4] {a}Contratado por *empresa de trabalho temporário,* "
        "[p=0.2] ele é *empregado.* [p=0.4] {b}E o vínculo dele é com a *empresa de trabalho temporário,* [p=0.3] "
        "{c}e não com a empresa onde ele presta o serviço. [p=0.4] {d}Temporário avulso? [p=0.2] *Errado!*"),
    dict(id="08", block="comissao", text=
        "{t}Terceira, [p=0.2] e essa é clássica: [p=0.2] o *servidor público.* [p=0.4] {a}Servidor efetivo, [p=0.2] "
        "com regime próprio? [p=0.3] Está *fora* do RGPS. [p=0.4] {b}Mas quem ocupa *exclusivamente cargo em comissão,* "
        "[p=0.2] *sem vínculo efetivo,* [p=0.3] {c}é *empregado* no RGPS! [p=0.5] {d}Então, [p=0.2] todo servidor público está "
        "excluído do RGPS? [p=0.3] *Errado!*"),
    dict(id="09", block="mandato", text=
        "{t}Quarta: [p=0.2] o *mandato eletivo.* [p=0.3] Vereador, [p=0.2] prefeito, [p=0.2] deputado, [p=0.2] senador. "
        "[p=0.4] {a}Se *não* estiver vinculado a regime próprio, [p=0.3] {b}ele é segurado *empregado.* [p=0.4] "
        "{c}Não é contribuinte individual. [p=0.3] {d}Parece estranho, [p=0.2] não parece? [p=0.3] É *por isso* que cai."),
    dict(id="10", block="emp_recolhe", text=
        "{t}E quem paga a contribuição do empregado? [p=0.4] {a}A *empresa:* [p=0.2] ela desconta do salário e recolhe. "
        "[p=0.4] {b}E se a empresa *não* recolher? [p=0.4] {c}O risco é *dela.* [p=0.3] O empregado *não* perde o tempo "
        "de contribuição."),

    # ================= DOMÉSTICO =================
    dict(id="11", block="dom_conceito", text=
        "{t}Agora, o *empregado doméstico.* [p=0.4] {a}Presta serviço de natureza *contínua,* [p=0.2] mediante remuneração, "
        "[p=0.3] {b}a *pessoa ou família,* [p=0.3] {c}no *âmbito residencial* destas, [p=0.3] {d}em atividades *sem fins "
        "lucrativos.*"),
    dict(id="12", block="cprs2", text=
        "{t}São *cinco filtros.* [p=0.4] {a}*Contínuo.* [p=0.3] {b}Para *pessoa ou família,* [p=0.2] e não para empresa. "
        "[p=0.3] {c}Na *residência.* [p=0.3] {d}*Sem lucro.* [p=0.3] {e}E *mais de dois dias* por semana. [p=0.5] "
        "{m}O macete: [p=0.2] *C, P, R, S, dois.*"),
    dict(id="13", block="dois_dias", text=
        "{t}E esse número é dos mais cobrados da matéria. [p=0.4] {a}Vem da Lei Complementar cento e cinquenta, [p=0.2] "
        "de dois mil e quinze. [p=0.4] {b}Até *dois* dias por semana? [p=0.2] É *diarista:* [p=0.2] contribuinte individual. "
        "[p=0.4] {c}*Mais* de dois dias? [p=0.2] É *empregada doméstica.* [p=0.5] {d}Três vezes por semana: [p=0.2] doméstica. "
        "[p=0.3] Duas vezes: [p=0.2] diarista."),
    dict(id="14", block="idade", text=
        "{t}E a idade? [p=0.3] {a}A mesma lei *proíbe* contratar menor de *dezoito* anos para o trabalho doméstico. [p=0.4] "
        "{b}Compare: [p=0.2] a regra geral é *dezesseis,* [p=0.2] {c}e o aprendiz, [p=0.2] *quatorze.* [p=0.5] "
        "{m}Guarde assim: [p=0.2] doméstico, *dezoito.* [p=0.2] Regra geral, *dezesseis.* [p=0.2] Aprendiz, *quatorze.*"),
    dict(id="15", block="lucro", text=
        "{t}E o filtro do *sem lucro* resolve os casos práticos. [p=0.4] {a}Cozinheira na casa da família? [p=0.2] *Doméstica.* "
        "[p=0.3] {b}Cozinheira no restaurante? [p=0.2] *Empregada:* [p=0.2] ali tem empresa, [p=0.2] e tem lucro. [p=0.5] "
        "{c}Caseiro do sítio de *lazer* da família? [p=0.2] *Doméstico.* [p=0.3] {d}Caseiro do sítio que *produz e vende?* "
        "[p=0.3] *Empregado rural.*"),

    # ================= AVULSO =================
    dict(id="16", block="avulso", text=
        "{t}Por último, [p=0.2] o *trabalhador avulso.* [p=0.4] {a}Ele presta serviço a *diversas* empresas, [p=0.3] "
        "{b}*sem vínculo empregatício.* [p=0.4] {c}Mas espera aí: [p=0.2] o autônomo também não faz isso? [p=0.5] "
        "{d}Faz! [p=0.3] {e}O que separa os dois é a *intermediação.*"),
    dict(id="17", block="psi", text=
        "{t}São três elementos. [p=0.4] {a}*Pluralidade* de tomadores. [p=0.3] {b}*Sem* vínculo. [p=0.3] {c}E "
        "*intermediação* obrigatória. [p=0.5] {m}O macete: [p=0.2] *P, S, I.* [p=0.4] {x}E a frase para levar: [p=0.2] "
        "*sem intermediação, [p=0.2] não há avulso.*"),
    dict(id="18", block="ogmo", text=
        "{t}E quem faz essa intermediação? [p=0.4] {a}Para o avulso *portuário,* [p=0.2] é o *OGMO,* [p=0.2] o Órgão Gestor "
        "de Mão de Obra. [p=0.4] {b}Para o avulso *não portuário,* [p=0.2] é o *sindicato.* [p=0.5] {c}Portuário pelo "
        "sindicato? [p=0.3] *Errado!*"),
    dict(id="19", block="cf7", text=
        "{t}E aqui está o ponto de ouro do avulso. [p=0.4] {a}O artigo sétimo da Constituição, [p=0.2] inciso trinta e quatro, "
        "[p=0.3] {b}garante *igualdade de direitos* entre o empregado permanente [p=0.2] e o trabalhador avulso. [p=0.5] "
        "{c}Por isso, [p=0.2] na previdência, [p=0.2] o avulso é tratado *como o empregado.*"),

    # ================= QUEM RECOLHE =================
    dict(id="20", block="recolhe", text=
        "{t}Agora, a linha mais importante deste módulo: [p=0.3] *quem recolhe?* [p=0.4] {a}Empregado, [p=0.2] doméstico "
        "e avulso [p=0.2] *não* recolhem para si mesmos. [p=0.3] Quem recolhe é um *terceiro:* [p=0.2] a empresa, [p=0.2] "
        "o empregador, [p=0.2] o OGMO. [p=0.4] {b}Já o contribuinte individual e o facultativo [p=0.2] recolhem *por conta "
        "própria.* [p=0.5] {m}O macete: [p=0.2] *E, E, A não recolhem; [p=0.2] C, F recolhem.*"),
    dict(id="21", block="perguntas", text=
        "{t}E lembra das três perguntas que eu prometi? [p=0.4] {a}Tem *subordinação?* [p=0.2] Empregado. [p=0.4] "
        "{b}Tem *residência sem lucro?* [p=0.2] Doméstico. [p=0.4] {c}Tem *intermediação?* [p=0.2] Avulso."),

    # ================= PEGADINHAS =================
    dict(id="22", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}A diarista que trabalha *dois* dias por semana é empregada "
        "doméstica. [p=0.4] {r1}*Errado:* [p=0.2] até dois dias, [p=0.2] é contribuinte individual. [p=0.5] "
        "{p2}O vereador não vinculado a regime próprio é contribuinte individual. [p=0.4] {r2}*Errado:* [p=0.2] é *empregado.* "
        "[p=0.5] {p3}A Constituição assegura igualdade de direitos entre o empregado permanente e o avulso. [p=0.4] "
        "{r3}*Certo!*"),
    dict(id="23", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}o empregado que tem a contribuição descontada do salário, [p=0.2] sem que a "
        "empresa faça o recolhimento, [p=0.2] *não* pode contar esse período como tempo de contribuição. [p=0.6] "
        "{r}*Errado!* [p=0.3] {x}A responsabilidade é da *empresa.* [p=0.2] O empregado não é prejudicado."),
    dict(id="24", block="q_caso", text=
        "{t}E um caso prático. [p=0.3] {a}Carlos é caseiro de uma chácara de uma família, [p=0.2] usada só para *lazer* "
        "nos fins de semana. [p=0.3] {b}Trabalha de segunda a sexta, [p=0.2] e mora no local. [p=0.4] {c}Carlos é: [p=0.2] "
        "empregado rural, [p=0.2] doméstico, [p=0.2] ou contribuinte individual? [p=1.5] {r}*Empregado doméstico!* [p=0.4] "
        "{x}Família, [p=0.2] residência, [p=0.2] sem lucro [p=0.2] e mais de dois dias. [p=0.3] Se a chácara fosse "
        "*comercial,* [p=0.2] seria empregado rural."),

    # ================= FECHAMENTO =================
    dict(id="25", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}Empregado: [p=0.2] *P, P, N, S, O,* [p=0.2] e a subordinação decide. [p=0.3] "
        "{b}Comissão sem vínculo efetivo e mandato sem regime próprio: [p=0.2] empregado. [p=0.3] {c}Doméstico: "
        "[p=0.2] *C, P, R, S, dois,* [p=0.2] e idade mínima de dezoito. [p=0.3] {d}Avulso: [p=0.2] *P, S, I,* [p=0.2] "
        "OGMO ou sindicato. [p=0.3] {e}E os três *não* recolhem para si."),
    dict(id="26", block="cta", text=
        "Na próxima aula, [p=0.2] o *contribuinte individual:* [p=0.2] o autônomo, [p=0.2] o diarista, [p=0.2] o diretor "
        "não empregado. [p=0.4] {pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do "
        "*PDF completo* de Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acertou o caso do Carlos? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
