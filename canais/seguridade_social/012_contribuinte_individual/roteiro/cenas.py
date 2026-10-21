# Roteiro — Seguridade Social 012: Contribuinte individual (Módulo M09, parte 1 de 2)
# Base: Estudos/Seguridade Social/modulos/M09-contribuinte-individual-e-segurado-especial.md — seção 1, quadro 3 e questões Q3 e Q7
#   Lei 8.213/1991, art. 11, V · Lei 9.876/1999. O segurado especial (seção 2) fica para a Aula 13.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# O material pede para decorar o CONTEÚDO do rol do art. 11, V, e não as letras das alíneas: falado sem as letras.
# Motorista de aplicativo: o material marca "tema com discussão judicial — conferir"; dito com essa ressalva.
# Liga com a Aula 11: o macete "E-E-A não recolhem; C-F recolhem" ganha a exceção da retenção pela empresa.

TITULO = "Contribuinte individual: quem é e quem recolhe (Lei 8.213, art. 11, V)"

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
        "{a}A diarista. [p=0.3] {b}O pastor. [p=0.3] {c}O síndico do prédio. [p=0.3] {d}O médico com consultório próprio. "
        "[p=0.5] {e}O que eles têm em comum? [p=0.5] {f}No INSS, [p=0.2] todos podem ser a *mesma coisa:* [p=0.3] "
        "*contribuinte individual.* [p=0.5] {g}Hoje, a categoria que recebe *quem sobra.*"),

    # ================= A LÓGICA =================
    dict(id="02", block="logica", text=
        "{t}Ele está no artigo onze, [p=0.2] inciso *cinco,* [p=0.2] da Lei oito mil, duzentos e treze. [p=0.4] "
        "{a}É quem trabalha *por conta própria.* [p=0.3] {b}*Sem* subordinação. [p=0.3] {c}E *sem* intermediação. [p=0.5] "
        "{d}Por isso ele é a categoria *residual:* [p=0.2] quem não cabe em nenhum outro lugar, [p=0.2] *cai aqui.*"),
    dict(id="03", block="fluxo", text=
        "{t}E isso vira um método para *qualquer* questão de enquadramento. [p=0.4] {a}Tem *subordinação?* [p=0.2] "
        "Empregado, [p=0.2] ou doméstico. [p=0.4] {b}Tem *intermediação* do OGMO ou do sindicato? [p=0.2] Avulso. [p=0.4] "
        "{c}É rural, [p=0.2] em economia familiar, [p=0.2] até quatro módulos fiscais? [p=0.2] Segurado especial. [p=0.4] "
        "{d}Nenhum dos anteriores? [p=0.3] *Contribuinte individual.* [p=0.4] {e}Ele é sempre a *última* hipótese testada."),
    dict(id="04", block="historia", text=
        "{t}E por que o inciso é o *cinco?* [p=0.4] {a}Lembra da aula passada? [p=0.3] Os incisos *três* e *quatro* "
        "eram o *empresário* e o *autônomo.* [p=0.4] {b}Em mil novecentos e noventa e nove, [p=0.2] a Lei nove mil, oitocentos "
        "e setenta e seis [p=0.2] revogou os dois [p=0.3] {c}e *juntou* tudo no contribuinte individual. [p=0.5] "
        "{d}Empresário e autônomo como categorias separadas? [p=0.3] *Não existem mais!*"),

    # ================= QUEM É =================
    dict(id="05", block="rol1", text=
        "{t}Agora, quem a lei coloca aqui. [p=0.3] E o conselho do material é: [p=0.2] decore o *conteúdo,* [p=0.2] não a "
        "letra da alínea. [p=0.5] {a}O produtor rural em área *maior* que quatro módulos fiscais, [p=0.3] {b}ou em área "
        "menor, [p=0.2] mas *com empregados.* [p=0.4] {c}Quem explora *garimpo.* [p=0.4] {d}E o *ministro de confissão "
        "religiosa:* [p=0.2] o pastor, [p=0.2] o padre, [p=0.2] a freira."),
    dict(id="06", block="rol2", text=
        "{t}Depois, o pessoal da *empresa* que não é empregado. [p=0.4] {a}O titular de *firma individual.* [p=0.3] "
        "{b}O *diretor não empregado.* [p=0.3] {c}O membro de *conselho de administração* de sociedade anônima. [p=0.3] "
        "{d}O *sócio* que recebe remuneração pelo trabalho. [p=0.3] {e}E o *síndico* de condomínio, [p=0.2] desde que "
        "*remunerado.*"),
    dict(id="07", block="rol3", text=
        "{t}E, por fim, as duas portas mais largas. [p=0.4] {a}Quem presta serviço em caráter *eventual* a empresas, "
        "[p=0.2] sem relação de emprego. [p=0.4] {b}E quem exerce, *por conta própria,* [p=0.2] atividade econômica urbana, "
        "[p=0.3] {c}*com* fins lucrativos [p=0.2] *ou não.*"),

    # ================= CASOS PRÁTICOS =================
    dict(id="08", block="sindico", text=
        "{t}E agora o *campeão* de prova: [p=0.3] o *síndico!* [p=0.5] {a}Síndico *remunerado?* [p=0.2] Contribuinte "
        "individual. [p=0.4] {b}E se, em vez de salário, [p=0.2] ele ganha *isenção da taxa de condomínio?* [p=0.4] "
        "{c}Conta como remuneração! [p=0.2] Contribuinte individual também. [p=0.5] {d}Mas o síndico *não* remunerado [p=0.3] "
        "{e}*não* é segurado por essa atividade. [p=0.3] Falta a remuneração."),
    dict(id="09", block="casos", text=
        "{t}Mais casos que caem. [p=0.3] {a}A *diarista,* [p=0.2] até dois dias por semana: [p=0.2] contribuinte individual. "
        "[p=0.4] {b}O *médico* com consultório próprio. [p=0.3] {c}O *feirante,* [p=0.2] o *camelô,* [p=0.2] o "
        "*cabeleireiro* autônomo. [p=0.3] {d}O *MEI,* [p=0.2] o microempreendedor individual. [p=0.4] {e}Todos, "
        "*contribuintes individuais.* [p=0.4] {f}E o motorista de aplicativo? [p=0.2] O material enquadra como contribuinte "
        "individual, [p=0.2] mas avisa: [p=0.2] é tema com *discussão na Justiça.*"),
    dict(id="10", block="rural", text=
        "{t}E repare na fronteira com o *segurado especial.* [p=0.4] {a}Produtor rural com *mais* de quatro módulos fiscais? "
        "[p=0.3] Contribuinte individual. [p=0.4] {b}Com *até* quatro, [p=0.2] mas com *empregado permanente?* [p=0.3] "
        "Também! [p=0.5] {c}Passou de quatro módulos, [p=0.2] *ou* tem empregado permanente: [p=0.2] *vira contribuinte "
        "individual.*"),

    # ================= FILIAÇÃO E QUEM RECOLHE =================
    dict(id="11", block="filiacao", text=
        "{t}E como ele entra no RGPS? [p=0.4] {a}A *filiação* é *automática:* [p=0.2] começou a trabalhar com remuneração, "
        "[p=0.2] está filiado. [p=0.4] {b}E a *inscrição* é feita [p=0.2] *por ele mesmo.*"),
    dict(id="12", block="recolhe", text=
        "{t}Agora, lembra do macete da aula passada? [p=0.3] {m}*C, F recolhem.* [p=0.4] {a}Pois aqui tem um detalhe que a "
        "banca adora! [p=0.5] {b}Se o contribuinte individual presta serviço *a uma empresa,* [p=0.3] {c}é a *empresa* "
        "que desconta e recolhe. [p=0.2] O risco *não* é dele. [p=0.5] {d}Se ele presta serviço a *pessoa física,* "
        "[p=0.2] ou trabalha por conta própria, [p=0.3] {e}aí é *ele mesmo* que recolhe. [p=0.2] E o risco *é dele.*"),

    # ================= PEGADINHAS =================
    dict(id="13", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas! [p=0.4] {p1}O síndico de condomínio é *sempre* contribuinte individual. [p=0.4] "
        "{r1}*Errado:* [p=0.2] só se for *remunerado.* [p=0.5] {p2}O ministro de confissão religiosa é segurado "
        "*facultativo.* [p=0.4] {r2}*Errado:* [p=0.2] é contribuinte individual. [p=0.5] {p3}A filiação do contribuinte "
        "individual depende de *inscrição prévia.* [p=0.4] {r3}*Errado:* [p=0.2] a filiação é *automática.* [p=0.5] "
        "{p4}O diretor não empregado é contribuinte individual. [p=0.4] {r4}*Certo!*"),
    dict(id="14", block="q_ce", text=
        "{t}E uma questão de prova: [p=0.3] {e}o contribuinte individual que presta serviço a empresa é *sempre* "
        "responsável pelo recolhimento da própria contribuição. [p=0.6] {r}*Errado!* [p=0.3] {x}A *empresa* retém e recolhe."),
    dict(id="15", block="q_mult", text=
        "{t}E agora, uma de múltipla escolha. [p=0.3] É contribuinte individual: [p=0.4] {a}A: [p=0.2] o diretor *empregado* "
        "de sociedade anônima. [p=0.4] {b}B: [p=0.2] o síndico de condomínio remunerado. [p=0.4] {c}C: [p=0.2] o contratado "
        "por empresa de trabalho temporário. [p=0.4] {d}D: [p=0.2] o portuário intermediado pelo OGMO. [p=0.4] {e}E: [p=0.2] "
        "a faxineira que trabalha *quatro* dias por semana na mesma casa. [p=0.5] {p}*Pause e tente!* [p=2.0]"),
    dict(id="16", block="q_mult", text=
        "{t}Vamos usar o fluxograma. [p=0.3] {xa}O diretor *empregado* tem subordinação: [p=0.2] empregado. [p=0.4] "
        "{xc}O temporário: [p=0.2] empregado. [p=0.4] {xd}O portuário com OGMO: [p=0.2] avulso. [p=0.4] {xe}Quatro dias "
        "na mesma casa: [p=0.2] doméstica. [p=0.5] {ok}Sobra o síndico remunerado: [p=0.2] *letra B!*"),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}contribuinte individual: [p=0.2] por conta própria, [p=0.2] sem subordinação, [p=0.2] "
        "sem intermediação: [p=0.2] a categoria *residual.* [p=0.3] {b}Juntou o empresário e o autônomo, [p=0.2] em mil "
        "novecentos e noventa e nove. [p=0.3] {c}Síndico, [p=0.2] *só* se remunerado. [p=0.3] {d}Rural com mais de quatro "
        "módulos, [p=0.2] ou com empregado permanente. [p=0.3] {e}E quem recolhe? [p=0.2] Depende: [p=0.2] serviço a "
        "empresa, [p=0.2] a *empresa* recolhe."),
    dict(id="18", block="cta", text=
        "Na próxima aula, [p=0.2] o *segurado especial:* [p=0.2] o rural que *mais cai* na prova. [p=0.4] "
        "{pdf}E se você quer estudar tudo isso com calma, [p=0.2] deixei na *descrição* o link do *PDF completo* de "
        "Seguridade Social, [p=0.2] com todos os módulos, [p=0.2] pegadinhas e simulados. [p=0.5] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses casos você não sabia? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
