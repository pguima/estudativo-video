# Pesos de assuntos no ENEM: rankings publicos e prioridades 1/2/3

Acesso a todas as fontes: 2026-11-05. Classificacao feita por **tema** (grupos de assuntos do `cronograma-enem.csv`), usando as colunas Area, Materia e Assunto; a coluna Incidencia foi ignorada.
Prioridade 1 = faixa alta, 2 = media, 3 = baixa. Onde nenhuma fonte tem dado, vale 2 e o tema vem marcado **sem dado**.

## 1. Fontes (rankings publicos usados)

| Sigla | Fonte | Periodo | Cobertura | Metodologia declarada |
|---|---|---|---|---|
| **AT** | Aprova Total, paginas "<materia> no Enem: assuntos que mais caem" (https://aprovatotal.com.br/matematica-no-enem/ e equivalentes `fisica-`, `quimica-`, `biologia-`, `historia-`, `geografia-`, `sociologia-`, `filosofia-`, `portugues-`, `literatura-`; Matematica datada 20/08/2026, demais "atualizado em set/2026") | Provas do Enem **2016 a 2025** | Matematica, Fisica, Quimica, Biologia, Historia, Geografia, Sociologia, Filosofia, Portugues; Literatura so qualitativo | "Levantamento de incidencia do Aprova Total, com base na analise das provas do Enem de 2016 a 2025". Nao informa numero de questoes nem criterio de classificacao; o relatorio completo e para assinantes. Tabelas mostram so as maiores categorias (Matematica soma 90,6%). Na pagina de Filosofia a tabela renderizada e a de Sociologia (erro da pagina); usei o texto: Antiga 28,1%, Moderna 18,8%, Areas da Filosofia 14,1%, Mal e justica 12,5%, Politica 6,3%. |
| **VW*** | Vestibulando Web, "Enem: saiba o que estudar primeiro..." (https://www.vestibulandoweb.com.br/enem/assuntos-que-mais-caem-no-enem-por-disciplina/, 25/09/2026) | Provas regulares 2016-2025, "levantamento atualizado em agosto de 2026" | Todas, so o topo de cada materia | Nao nomeia a fonte; numeros coincidem com a AT em Matematica, Fisica, Quimica, Biologia, Historia, Geografia, Filosofia, Sociologia e Portugues, entao trato como **derivado da AT, nao independente**. Unica fonte para Literatura (contemporanea 30,8%, depois artes e Modernismo), Ingles (gramatica e interpretacao 93,6%, depois vocabulario) e Espanhol (gramatica 90%, depois vocabulario). Esses tres itens sao tratados como AT* (indiretos). |
| **EST** | Estrategia Vestibulares, "Assuntos que mais caem no Enem" (https://vestibulares.estrategia.com/portal/enem/assuntos-que-mais-caem-no-enem/, atualizado em 06/11/2025 segundo a pagina) | **1998 a 2020**, incluindo reaplicacoes ("ultimos 22 anos") | Todas as materias de todas as areas, com percentuais | Banco de Questoes do Estrategia; "mais de 88% de todas as questoes da historia do Enem" classificadas por professores. "Outros" = nao classificadas (Matematica 26,43%, Portugues 24,44%). **Dados param em 2020**; taxonomia propria e ampla (ex.: Matematica "Aritmetica" 26,36%, Quimica em 4 blocos, Portugues "Gramatica" 58,79%). |
| **SAS** | SAS Educacao "mapeamento" via CNN Brasil: (a) https://www.cnnbrasil.com.br/educacao/enem-veja-ranking-dos-temas-mais-cobrados-entre-2009-e-2024/ (22/05/2025); (b) https://www.cnnbrasil.com.br/educacao/a-3-meses-do-enem-confira-lista-com-assuntos-mais-cobrados-das-disciplinas/ (09/08/2025) | Provas do Enem **2009 a 2024** | Todas as disciplinas; (b) traz lista de temas por disciplina com total de questoes | A CNN **nao descreve metodologia** (nem como as questoes foram classificadas). Totais por disciplina 2009-2024: Matematica 1.462, Portugues 1.281, Quimica 584, Biologia 536, Historia 502, Geografia 486, Fisica 467, Sociologia 228, Filosofia 179, Ingles 132, Espanhol 115, Arte 22. A lista de (b) esta **provavelmente em ordem decrescente** (os 1os itens conferem com o ranking (a): competencia leitora 563, proporcionalidade 213, estatistica 187, geometria plana 110); a ordem nao e declarada. So aparecem 9 a 15 temas por disciplina; o restante nao tem dado. |

Tentativa nao concluida: o PDF "Raio X ENEM 2023" do SAS (https://enem.saseducacao.com.br/wp-content/uploads/2023/10/Raio_X_ENEM_2023.pdf) devolve uma pagina HTML "Pagina nao encontrada" (nao e PDF); nao foi usado. Buscas retornaram a Aprova Total em 403 via WebFetch (baixei pelo navegador de linha de comando sem problema) e a pagina da CNN (a) via WebFetch confirma os mesmos numeros de (a).

### Regras de faixa (aplicadas por fonte, dentro de cada materia)

- Fontes com percentual (AT, EST): faixas por **quebras naturais** da distribuicao da materia. Limites usados: Matematica AT alta >=10%, media 4-10%, baixa <4%; EST alta >=6%, media 2-6%, baixa <2%. Quimica AT alta >=6,5%, media 5-6,5%, baixa <5% (distribuicao plana); EST alta >=25%, media 10-25%, baixa <10%. Fisica AT alta >=11%, media 4-11%, baixa <4%; EST alta >=13%, media 4-13%, baixa <4%. Biologia AT alta >=10% (so Ecologia), media 5-10%, baixa <5%; EST alta >=8%, media 4-8%, baixa <4%. Geografia AT alta >=10%, media 4-10%, baixa <4%; EST alta >=12%, media 4-12%, baixa <4%. Historia AT alta >=9%, media 5-9%, baixa <5%. Sociologia AT alta >=13%, media 6-13%, baixa <6%; EST alta >=15%, media 5-15%, baixa <5%. Filosofia AT alta >=14%, media 6-14%, baixa <6%; EST alta >=20%, media 5-20%, baixa <5%.
- SAS (lista ordenada, N temas): terco superior = alta, terco medio = media, terco inferior = baixa.
- Tema que nao e categoria propria da tabela de uma fonte (subtopico de categoria maior) = **sem dado nessa fonte**; nao herdo a faixa da categoria-mae. Excecao: Matrizes, Polinomios, Numeros complexos, Geometria analitica/conicas contam como **B\*** na AT (ausentes das 8 categorias que somam 90,6%, logo <3,7%).
- Prioridade final = faixa mais frequente entre as fontes com dado. **Empate: vale a fonte mais recente na ordem AT (2016-2025), SAS (2009-2024), EST (1998-2020).** So uma fonte com dado: vale ela. Nenhuma: prioridade 2, "sem dado".
- Legenda das tabelas: A/M/B = faixa alta/media/baixa; `-` = sem dado na fonte. Numeros entre parenteses = percentual ou posicao na lista SAS.

### Divergencias importantes entre fontes (registro)

- **Generos textuais**: AT 44,1% (alta) x EST 0,23% (taxonomia diferente, tudo cai em "Gramatica 58,79%") x SAS posicao 8/14 (media). Empate resolvido pela AT: prioridade 1.
- **Cinematica**: AT 11,4% (A), EST 8,4% (M), SAS lancamentos/MU nas posicoes 10-11 (B). Empate, AT: prioridade 1.
- **Bioquimica e DNA/sintese proteica**: AT e EST colocam em B (3,6-3,7%); SAS coloca "Bioquimica" na posicao 5 e "DNA" na 3 (A). Maioria B: prioridade 3, mas **divergente**.
- **Funcoes organicas**: SAS no 1o lugar; AT 6,6% (A para propriedades dos compostos organicos); EST Organica 16,8% (M). Prioridade 1.
- **Zoologia/Fisiologia humana/Botanica**: AT M, EST B/A. Resolvidas pela AT (prioridade 2).
- **Espanhol/Ingles "gramatica"**: VW 90% e 93,6% x EST (interpretacao 73% e 81%). Taxonomias incompativeis; ver observacoes nas tabelas.
- **Matematica basica 37,3% (AT)** e **Aritmetica 26,4% (EST)** incluem varios itens do cronograma (porcentagem, razao, regra de tres, unidades, equacoes). A AT lista nominalmente: inteiros, fracoes, decimais, potenciacao, radiciacao, unidades, equacoes do 1o e 2o graus, porcentagem, razao e proporcao, regra de tres.

---

## 2. Classificacao por materia (nomes de Materia como no `cronograma-enem.csv`)

### Matematica

#### Matematica, Matematica Basica e Proporcionalidade
| Tema (assuntos agrupados) | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Razao, proporcao, regra de tres, grandezas direta/inversamente proporcionais, divisao proporcional, escalas, velocidade/densidade/vazao como razao | A (37,3 Mat. basica) | A (26,4 Aritmetica) | A (1o proporcionalidade; 7o razao) | **1** | Unanime |
| Porcentagem: aumentos, descontos, variacoes sucessivas | A | A | - | **1** | AT lista porcentagem |
| Operacoes e conjuntos numericos, fracoes/decimais/dizimas, potenciacao e radiciacao | A | A | B (racionais, 14o) | **1** | |
| Unidades de medida e conversoes | A | - | B (11o) | **1** | Empate A/B, AT decide |
| Divisibilidade, primos, MMC e MDC | - | - | - | **2** | sem dado (AT nao cita nominalmente) |
| Notacao cientifica e ordem de grandeza | - | - | - | **2** | sem dado |

#### Matematica, Algebra e Funcoes
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Expressoes algebricas e produtos notaveis; equacoes e inequacoes do 1o e 2o graus (Bhaskara) | A (equacoes na Mat. basica) | M (Equacoes 3,39; Inequacoes 0,49) | B (Equacoes, 12o) | **1** | Tres faixas distintas; AT decide |
| Sistemas de equacoes lineares | - | B (0,71) | - | **3** | uma fonte |
| Conceito de funcao, funcao afim, funcao quadratica (vertice, max/min) | A (10,2) | A (10,11) | M (6o) | **1** | |
| Funcao exponencial; logaritmos e funcao logaritmica (pH, Richter, decibeis) | - | - | - | **2** | sem dado (so ha a categoria Funcoes) |
| Funcao modular e funcoes definidas por partes | - | - | - | **2** | sem dado; fora da matriz do Inep (ver provas.md) |
| Funcao composta e funcao inversa | - | - | - | **2** | sem dado; fora da matriz do Inep |
| Progressao aritmetica (PA) e geometrica (PG) | - | M (2,47) | - | **2** | uma fonte |
| Matrizes e operacoes; determinantes e sistemas lineares | B\* | B (0,21) | - | **3** | AT nao lista; EST 0,21% |
| Polinomios e equacoes polinomiais | B\* | B (0,07) | - | **3** | |
| Numeros complexos | B\* | - (nenhuma categoria) | - | **3** | Nenhum ranking cita; fora da matriz do Inep. Nao e "sem dado" puro (AT/EST listam categorias minimas, como Polinomios 0,07%, e omitem complexos), mas o dado e indireto |

#### Matematica, Geometria Plana
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Angulos, triangulos, Tales e semelhanca, Pitagoras, quadrilateros, poligonos, circunferencia, areas, perimetros, razao entre areas | M (7,7) | A (6,71; Circulo e circunferencia a parte 1,13) | A (3o; areas de figuras planas 15o) | **1** | AT considera top 5 |

#### Matematica, Geometria Espacial
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Poliedros, prismas, piramides, cilindros, cones, esfera, solidos compostos, razao entre volumes, vistas | A (11,2) | A (7,07) | A (4o; volume 8o) | **1** | |

#### Matematica, Estatistica e Probabilidade
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Populacao e amostra, tabelas, leitura de graficos, media, mediana, moda, analise critica de graficos | A (11,2) | M (Estatistica 2,47; Medias 2,05) | A (2o) | **1** | |
| Desvio medio, variancia, desvio padrao | B (texto da AT: "as medidas de dispersao, no geral, nao caem no Enem") | - | - | **3** | dado qualitativo |
| Quartis, boxplot, amplitude, interpretacao de dispersao | - | - | - | **2** | sem dado |
| Principio fundamental da contagem, fatorial, arranjos, permutacoes, combinacoes | M (4,1) | M (2,05) | M (9o) | **2** | |
| Probabilidade (espaco amostral, uniao/intersecao, condicional) | M (5,2) | M (4,10) | A (5o) | **2** | |
| Distribuicao binomial | - | - | - | **2** | sem dado |

#### Matematica, Trigonometria
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Razoes no triangulo retangulo, angulos notaveis, leis dos senos e cossenos, ciclo, radianos, identidades, funcoes trigonometricas | B (3,7) | B (Trig. 0,42; Func. trig. 0,64; Arcos 0,42) | - | **3** | |

#### Matematica, Matematica Financeira
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Juros simples e compostos, descontos, taxas equivalentes, inflacao, financiamento, comparacao de propostas | - | B (0,85) | M (10o) | **2** | Empate B/M sem AT; SAS decide. Descontos/acrescimos/lucro tambem estao em Porcentagem (prio 1) |

#### Matematica, Geometria Analitica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Plano cartesiano, distancia, ponto medio, reta, circunferencia, area por determinante | B\* | B (0,92) | B (13o) | **3** | |
| Nocoes de conicas | - | - | - | **3** | sem dado proprio; herda B da categoria; fora da matriz do Inep (so circunferencia) |

#### Matematica, Raciocinio Logico e Leitura Matematica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Leitura de tabelas, mapas e infograficos | A (parte de Estatistica: interpretacao de graficos e tabelas) | - | - | **1** | |
| Interpretacao de problemas contextualizados; estimativas e aproximacoes; otimizacao e tomada de decisao | - | - | - | **2** | sem dado (habilidade transversal) |
| Sequencias e padroes | - | M (Progressoes 2,47) | - | **2** | |
| Logica proposicional basica | - | B (0,49) | - | **3** | |

### Ciencias da Natureza

#### Natureza, Fisica - Mecanica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Grandezas, unidades, notacao cientifica, vetores | - | B (Introducao 3,02) | - | **3** | |
| Cinematica: MU, MUV, graficos, queda livre, lancamentos, circular | A (11,4) | M (8,42) | B (lancamentos 10o, MU 11o) | **1** | Empate, AT decide |
| Leis de Newton, atrito, plano inclinado, centripeta | M (Dinamica 6,3) | - | A (Forcas e movimento, 4o) | **2** | Empate, AT decide |
| Trabalho, potencia, energia e conservacao | M (4,6) | - | M (7o) | **2** | |
| Impulso, quantidade de movimento, colisoes | - | - | - | **2** | sem dado |
| Estatica, torque, alavancas | B (2,9) | - | - | **3** | |
| Gravitacao universal e Kepler | - | - | - | **2** | sem dado (EST: Astronomia 0,22 e outra coisa) |
| Hidrostatica; hidrodinamica | M (Fluidos 4,0) | - | - | **2** | |

#### Natureza, Fisica - Eletricidade e Fisica Moderna
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Corrente, resistores, Ohm, circuitos, potencia e consumo, geradores | A (Eletrodinamica 21,1) | A (Eletricidade 19,44) | A (circuitos 2o; consumo 5o) | **1** | |
| Eletrostatica: carga, Coulomb, campo, potencial, capacitores | B (3,4) | - | - | **3** | |
| Magnetismo, forca magnetica, inducao, transformadores | M (5,1) | B (Eletromagnetismo 2,81) | - | **2** | Empate, AT decide |
| Efeito fotoeletrico, espectros, radioatividade, relatividade | B\* | B (Fisica Moderna 1,73) | - | **3** | |
| Fisica e sociedade: usinas, matriz energetica | - | - | - | **2** | sem dado |

#### Natureza, Fisica - Termologia, Optica e Ondas
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Termometria, dilatacao, calorimetria, mudancas de estado, propagacao de calor | A (Termologia 16,0) | A (13,17) | A (Calorimetria 1o) | **1** | |
| Gases ideais, termodinamica, maquinas termicas | A | A | A (Termodinamica 3o) | **1** | |
| Optica geometrica, refracao, lentes, olho humano | M (9,1) | M (6,05) | M (Reflexao e refracao, 6o) | **2** | |
| Ondas, acustica, Doppler, espectro eletromagnetico | A (13,7) | A (14,69) | M (som 8o, 9o, 12o, 13o) | **1** | |

#### Natureza, Quimica Geral e Inorganica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Materia, substancias, misturas, separacao, estados fisicos | A (Separacao 6,6) | A (Q. geral 32,9) | M (5o) | **1** | |
| Modelos atomicos, distribuicao eletronica, tabela periodica | M (Atomos 5,9) | - | B (Estrutura atomica 11o) | **2** | Empate, AT decide |
| Ligacoes, geometria molecular, polaridade, forcas intermoleculares | A (Moleculas e propriedades 8,6) | - | - | **1** | |
| Funcoes inorganicas | A (6,6) | - | - | **1** | |
| Reacoes inorganicas e balanceamento | M (5,3) | - | B (Tipos de reacoes 10o) | **2** | Empate, AT decide |
| Mol, massa molar, estequiometria (rendimento, pureza, limitante) | A (7,9) | - | - | **1** | |
| Estudo dos gases | - | - | - | **2** | sem dado |
| Solucoes: concentracao, diluicao, mistura; coligativas; titulacao | M (5,3) | - | M (Concentracao 6o) | **2** | Coligativas e titulacao sem dado proprio |

#### Natureza, Quimica - Fisico-Quimica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Termoquimica, Lei de Hess, energia de ligacao | B (3,3) | - | B (Entalpia 12o, Termoquimica 13o) | **3** | |
| Cinetica quimica, catalisadores | M (5,3) | - | A (3o) | **2** | Empate, AT decide |
| Equilibrio quimico, Le Chatelier, pH/pOH, hidrolise, tampao, Kps | B (4,6) | - | - | **3** | uma fonte; EST (Fisico-quimica 30,19%) e categoria ampla |
| Eletroquimica: pilhas, eletrolise, corrosao | A (6,6) | - | A (Pilhas 4o) | **1** | |
| Radioatividade (meia-vida, fissao, fusao) | - | - | - | **2** | sem dado |

#### Natureza, Quimica Organica e Ambiental
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Cadeias, hidrocarbonetos, nomenclatura, funcoes organicas, propriedades fisicas | A (Prop. dos C.O. 6,6; Hidrocarbonetos 5,9) | M (Organica 16,77) | A (Funcoes organicas 1o) | **1** | |
| Isomeria plana e espacial | B (3,3) | - | - | **3** | |
| Reacoes organicas: adicao, substituicao, oxidacao, esterificacao, saponificacao | M (5,3) | - | A (2o) | **2** | Empate, AT decide |
| Polimeros naturais e sinteticos, plasticos | - | - | - | **2** | sem dado |
| Bioquimica (carboidratos, lipidios, proteinas) | - | B (1,89) | - | **3** | |
| Combustiveis, poluicao atmosferica, chuva acida, tratamento de agua e esgoto, quimica verde | B (Quimica ambiental 3,9) | M (14,68) | M (poluicao 7o-9o) | **2** | |

#### Natureza, Biologia - Citologia e Bioquimica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Agua, sais, carboidratos, lipidios, proteinas, enzimas | B (Bioquimica 3,6) | B (3,73) | A (Bioquimica 5o) | **3** | Divergente: SAS alta |
| Acidos nucleicos DNA/RNA | B (Genetica 3,6) | B (Genetica 3,57) | A (DNA 3o) | **3** | Divergente: SAS alta |
| Membrana, citoplasma, organelas, nucleo, procarioticas/eucarioticas, mitose e meiose | M (Citologia 5,3; Citogenetica 3,6) | A (Citologia 9,32) | M (Biologia celular 6o) | **2** | |
| Respiracao celular, fermentacao, fotossintese, quimiossintese | M (Bioenergetica 7,1) | - | B (Fotossintese 13o) | **2** | Empate, AT decide |

#### Natureza, Biologia - Ecologia e Meio Ambiente
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Niveis de organizacao, nicho, cadeias e teias, piramides, ciclos biogeoquimicos, relacoes ecologicas, populacoes, sucessao, biomas, poluicao, eutrofizacao, biodiversidade, impactos | A (Ecologia 26,0) | A (37,42) | A (Desequilibrio 1o, ciclos 4o) / M (cadeias 8o) | **1** | Unanime: tema mais forte do ENEM em Biologia |

#### Natureza, Biologia - Genetica e Evolucao
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Mendel, heredogramas, grupos sanguineos, heranca ligada ao sexo, ligacao genica | B (3,6) | B (3,57) | - | **3** | |
| Mutacoes, sintese proteica e codigo genetico | B (3,6) | B | A (DNA 3o) | **3** | Divergente (SAS alta) |
| Biotecnologia: transgenicos, clonagem, CRISPR, celulas-tronco, bioetica | B (4,7) | M (5,43) | B (DNA recombinante 14o) | **3** | |
| Origem da vida, Lamarck, Darwin, teoria sintetica, selecao natural, especiacao | M (Evolucao 6,5) | M (7,45) | - | **2** | |
| Hardy-Weinberg | - | - | - | **2** | sem dado |

#### Natureza, Biologia - Seres Vivos e Fisiologia
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Taxonomia e classificacao | - | B (0,62) | - | **3** | |
| Virus, bacterias, protistas, fungos, doencas | M (Microbiologia 6,5) | M (Doencas humanas 5,59) | A (Viroses 2o; protozooses 9o, bacterioses 10o: M) | **2** | |
| Botanica | M (7,1) | B (Biologia vegetal 3,57) | - | **2** | Empate, AT decide |
| Zoologia | M (8,3) | B (Biologia animal 2,8) | - | **2** | Empate, AT decide |
| Histologia animal | M (5,3) | B (1,24) | - | **2** | Empate, AT decide |
| Sistemas digestorio, respiratorio, circulatorio, excretor, nervoso, endocrino, locomotor | M (Fisiologia 7,7) | A (8,54) | - | **2** | Empate, AT decide |
| Sistema imunologico, vacinas, doencas, vetores, ISTs, saneamento, epidemiologia | M (Microbiologia) | M (Doencas 5,59) | B (Saude 12o) | **2** | |
| Reproducao humana e embriologia | - | B (0,93; 0,47) | - | **3** | |

### Ciencias Humanas

#### Humanas, Geografia Fisica e Ambiental
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Cartografia: escala, projecoes, coordenadas, curvas, fusos, sensoriamento, GPS | B (3,5) | M (4,02) | M (Interpretacao de mapas 8o) | **2** | |
| Estrutura da Terra, tectonica, relevo, rochas, minerais, solos, erosao | M (Geologia 6,5; Solos 3,5) | M (4,33) | M (Geomorfologia 6o; Geologia 10o) | **2** | |
| Clima, tipos climaticos, massas de ar, El Nino e La Nina | M (4,7) | B (3,87) | M (9o) | **2** | |
| Hidrografia, aquiferos, oceanos, recursos hidricos | - | B (2,79) | B (12o) | **3** | |
| Biomas brasileiros e mundiais, dominios morfoclimaticos | M (4,7) | B (1,55) | - | **2** | Empate, AT decide |
| Impactos ambientais, aquecimento global, ozonio, chuva acida, residuos, acordos, ODS | M (Questoes ambientais 4,1) | A (Meio ambiente 13,16) | B (13o, 14o) | **2** | Tres faixas; AT decide |
| Fontes de energia e matriz energetica | B (3,5) | - | - | **3** | EST "Infraestrutura 8,98" e ambigua e nao foi usada |

#### Humanas, Geografia Humana, Economica e Politica
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Urbanizacao, metropolizacao, problemas urbanos, rede urbana | A (11,8) | M (6,04) | A (1o) | **1** | |
| Estrutura fundiaria, agronegocio, agricultura familiar, Revolucao Verde, producao de alimentos | A (12,4) | A (13,47) | A (2o, 4o) | **1** | |
| Geopolitica, blocos, organismos internacionais, conflitos, regionalizacao do mundo | A (11,2) | M (6,19) | A (5o) | **1** | |
| Globalizacao, divisao internacional do trabalho, transportes, comercio exterior | M (Transportes 4,7) | M (Globalizacao 9,29; Infra 8,98) | B (11o) | **2** | |
| Industrializacao mundial e brasileira | - | M (4,95) | - | **2** | |
| Populacao, transicao demografica, migracoes, indicadores sociais | M (Migracoes 4,1) | A (Populacao 15,48) | M (Migracoes 7o; Populacao 15o: B) | **2** | |
| Regionalizacao do Brasil (IBGE, complexos regionais) | - | B (Regional 2,01) | - | **3** | uma fonte |

#### Humanas, Historia do Brasil
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Povos indigenas, periodo colonial, capitanias, acucar, escravidao, bandeirantes, mineracao, Inconfidencias | A (Colonia 11,8) | - | A (Colonial 1o; Trabalho escravo 12o: B) | **1** | |
| Joanina, Independencia, Primeiro Reinado, Regencia, Segundo Reinado, Paraguai, abolicao | M (Monarquico 6,6) | - | M (Segundo Reinado 6o; Abolicao 9o: B) | **2** | |
| Proclamacao, Republica Velha, revoltas, tenentismo, Semana de Arte Moderna | M (7,4) | - | A (Primeira Republica 2o) | **2** | Empate, AT decide |
| Revolucao de 1930, Era Vargas, Estado Novo, Republica de 1946 a 1964 | A (Estado Novo e Populismo 10,3) | - | A (Era Vargas 3o; Republica Nova 11o: B) | **1** | |
| Golpe de 1964, Ditadura, abertura, Nova Republica, CF/88, governos recentes | - | - | M (Ditadura 5o) | **2** | AT "Tempo Presente 9,6" pode incluir; nao uso |
| Historia e cultura afro-brasileira e indigena; movimentos sociais | - | - | - | **2** | sem dado direto (EST: Hist. da Africa 0,84) |

#### Humanas, Historia Geral
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Pre-historia, civilizacoes antigas, Grecia, Roma | M (Antiga 5,9) | - | M (Antiguidade Classica 7o) | **2** | |
| Idade Media, feudalismo, Igreja, mundo islamico, Cruzadas, crise do seculo XIV | A (10,3) | - | - | **1** | uma fonte |
| Renascimento, Reforma, Absolutismo, Mercantilismo, Grandes Navegacoes, Iluminismo | A (Moderna 9,6) | - | B (Absolutismo 10o) | **1** | Empate, AT decide |
| Revolucao Industrial, revolucoes Inglesa e Francesa, Napoleao, imperialismo, socialismo | - | - | M (Rev. Industrial 8o) | **2** | |
| Independencias latino-americanas, unificacoes | - | M (Hist. da America 4,2) | - | **2** | |
| Seculo XX: Guerras Mundiais, Revolucao Russa, crise de 1929, totalitarismos, Guerra Fria | M (Seculo 20 6,6; Conflitos 5,1) | - | - | **2** | |
| Descolonizacao, Revolucao Cubana, queda do Muro, nova ordem mundial | A (Tempo Presente 9,6) | - | - | **1** | uma fonte |

#### Humanas, Sociologia
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Contexto, positivismo, Durkheim, Weber, Marx | B (Teoria sociologica 5,7) | B (Classica 3,32; Introducao 4,27) | B (Teoricos classicos 12o) | **3** | Unanime |
| Cultura, identidade, diversidade, etnocentrismo, socializacao, instituicoes | A (19,0) | A (Cultura 18,48) | A (Cultura 2o; Identidade 3o) | **1** | |
| Estratificacao, desigualdade, relacoes raciais, cotas, genero | - | B (Estratificacao 0,95) | M (Desigualdade 7o; Estrutura social 9o) | **2** | Empate, SAS decide |
| Trabalho: taylorismo, fordismo, toyotismo, uberizacao | M (6,7) | B (2,84) | A (5o) | **2** | Tres faixas; AT decide |
| Movimentos sociais, cidadania, Estado, democracia, partidos, direitos humanos | A (Mov. sociais 18,1; Estado e cidadania 15,2) | A (Ciencia politica 21,8) | A (1o, 4o) | **1** | |
| Violencia, criminalidade, sistema prisional | - | - | B (11o) | **3** | uma fonte |
| Industria cultural, midia, consumo, globalizacao e sociedade em rede | B (Meio ambiente, sociedade e comunicacao 5,7) | A (Temas contemporaneos 17,06) | M (Meios de comunicacao 6o) | **3** | Tres faixas; AT decide |
| Questao ambiental e sociedade de risco | B (5,7) | - | - | **3** | |
| Pensadores brasileiros (Freyre, Buarque, Caio Prado, Florestan, Darcy, Milton Santos) | A (Sociologia brasileira 13,3) | M (Sociologia no Brasil 6,16) | - | **1** | Empate, AT decide |

#### Humanas, Filosofia
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Mito a filosofia, pre-socraticos, sofistas e Socrates, Platao, Aristoteles | A (Antiga 28,1) | M (Grega 10,83) | M (Aristoteles 3o: A; Naturalistas 7o: M; Antiga 10o: M; Platao 15o: B) | **2** | Divergente: AT alta |
| Helenisticas | - | - | B (14o) | **3** | |
| Patristica e Escolastica | - | B (Medieval 1,27) | M (Medieval 6o) | **2** | Empate, SAS decide |
| Renascimento e Maquiavel, racionalismo, empirismo, contratualismo, Iluminismo, Kant | A (Moderna 18,8) | M (12,74) | A (Origens da modernidade 4o; Descartes 5o; Kant 12o: B) | **1** | |
| Hegel, Marx, utilitarismo, Nietzsche, existencialismo, Frankfurt, Foucault, Arendt, Habermas, Bauman, Rawls | M (Mal e justica 12,5) | B (Contemporanea 1,91) | B (Contemporanea 11o; Frankfurt 13o) | **3** | |
| Etica e moral, liberdade e determinismo, filosofia politica | A (Areas da Filosofia 14,1) | A (Politica 24,84; Etica 24,84) | A (Politica 1o; Moral e etica 2o) | **1** | |
| Teoria do conhecimento e logica | - | B (Logica 0,64) | M (Epistemologia 9o) | **2** | Empate, SAS decide |
| Estetica e filosofia da arte | - | B (2,55) | - | **3** | |
| Bioetica; filosofia africana (Ubuntu) e pensamento latino-americano | - | - | - | **2** | sem dado |

### Linguagens

#### Linguagens, Interpretacao e Analise de Texto
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Compreensao global, tese, informacoes explicitas/implicitas, inferencia, finalidade, publico-alvo, ponto de vista | B (Estrategias de interpretacao 2,9) | A (Interpretacao 15,65) | A (Competencia leitora 1o; Apreensao de sentido 2o; Habilidades de leitura 7o: M) | **1** | AT classifica diferente |
| Generos textuais (noticia, reportagem, opiniao, cronica, generos digitais), tipologia, relacao texto e imagem | A (44,1) | B (0,23) | M (8o) | **1** | Divergente; AT decide |
| Funcoes da linguagem | M (5,9) | - | - | **2** | |
| Intertextualidade, ironia, humor, ambiguidade, multimodalidade | - | - | M (Estrategias de convencimento 6o; Anuncio 12o: B) | **2** | |
| Estrutura argumentativa, falacias, persuasao | - | - | M (Estrategias de convencimento 6o) | **2** | |

#### Linguagens, Gramatica e Norma-Padrao
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Variacao linguistica, norma-padrao x variedades, registro formal e informal | M (Linguagem culta x coloquial 10,7) | - | - | **2** | |
| Coesao e coerencia, progressao textual, conectivos | B (Tempos verbais e progressao tematica 4,4) | - | B (Coesao 13o) | **3** | |
| Semantica, denotacao e conotacao, figuras de linguagem | - | - | - | **2** | sem dado |
| Classes de palavras, sintaxe, concordancia, regencia, crase, colocacao, pontuacao, vozes verbais, ortografia | - | - (Gramatica 58,79 e categoria ampla, sem desdobramento) | - | **2** | sem dado especifico |
| Formacao de palavras, estrangeirismo | - | - | - | **2** | sem dado |

#### Linguagens, Literatura
| Tema | AT/VW | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Generos literarios, versificacao | - | A (Teoria literaria 48,08) | - | **1** | uma fonte |
| Quinhentismo, Barroco, Arcadismo | B (AT: "as esteticas anteriores ao periodo romantico nao sao cobradas", qualitativo) | - | - | **3** | |
| Romantismo (poesia e prosa), Realismo e Naturalismo | A (AT: Romantismo, Realismo e Modernismo "mais recorrentes", qualitativo) | B (Romantismo 0,38) | - | **1** | Empate, AT decide |
| Parnasianismo, Simbolismo | B (fora das mais recorrentes, AT qualitativo) | - | - | **3** | |
| Pre-Modernismo, vanguardas, Modernismo (1a a 3a fases, romance de 30, poesia) | A (Modernismo) | - | - | **1** | |
| Literatura contemporanea (Adelia, Evaristo, Carolina, Hatoum), concretismo, poesia marginal, literatura indigena e periferica | A (VW*: contemporanea 30,8%, 1a) | - | B (Literatura contemporanea 14o) | **1** | Empate, AT decide |
| Literaturas africanas em lingua portuguesa | - | B (0,38) | - | **3** | |
| Dialogo literatura-musica-artes, canone | M (VW*: "artes" em 2o) | - | - | **2** | |

#### Linguagens, Lingua Estrangeira - Ingles
| Tema | AT/VW | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Estrategias de leitura, cognatos, generos (charges, noticias, letras, anuncios), temas sociais | A (VW*: gramatica e interpretacao 93,6%) | A (Interpretacao 80,95) | A (Estruturas e aspectos discursivos 1o; Habilidades de leitura 2o; Apreensao 3o) | **1** | |
| Vocabulario, campo semantico, phrasal verbs, expressoes | M (VW*: vocabulario, 2o) | M (10,88) | M (Vocabulario 6o; Expressoes 9o: B) | **2** | |
| Gramatica aplicada (tempos verbais, modais, passiva, condicionais, pronomes, comparativos) | - | B (Contracoes 0,68) | - | **2** | sem dado separado: VW junta gramatica e interpretacao |
| Conectivos e marcadores discursivos; preposicoes e adverbios | - | - | B (Marcadores 8o; Adverbios 7o) | **3** | uma fonte |

#### Linguagens, Lingua Estrangeira - Espanhol
| Tema | AT/VW | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Estrategias de leitura e inferencia | - | A (Interpretacao 73,28) | A (Apreensao de sentido 1o; Habilidades 3o; Pontos de vista 4o) | **1** | |
| Heterosemanticos (falsos amigos), vocabulario | M (VW*: vocabulario) | M (Semantica 10,69) | B (Equivalencia de vocabulos 9o) | **2** | |
| Gramatica: artigos, pronomes, verbos, muy/mucho, apocope, acentuacao | A (VW*: gramatica 90%) | B (Classes gramaticais 2,29) | M (Verbos 8o) | **1** | Tres faixas; VW* decide, **baixa confianca** (taxonomia de gramatica nao comparavel; EST e SAS indicam leitura) |
| Variedades do espanhol; cultura e questoes sociais da America Hispanica | - | M (Historia da hispanidade 12,98) | M (Variedades 5o) | **2** | |
| Generos: noticias, tirinhas, publicidade, literatura hispano-americana | - | - | M (Publicidade 7o; Poesia 11o: B) | **2** | |

#### Linguagens, Artes
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Elementos da linguagem visual | - | M (Conceitos basicos 10,45) | - | **2** | |
| Arte pre-historica, egipcia, grega, romana, medieval, Renascimento, Barroco, Neoclassicismo, Romantismo, Realismo, Impressionismo | - | B (Pre-historia 2,24; Neoclassico 0,75; Impressionismo 0,75) | - | **3** | |
| Vanguardas: Expressionismo, Cubismo, Futurismo, Dadaismo, Surrealismo, Abstracionismo | - | M (soma 13,4: Cubismo 6,72) | - | **2** | |
| Pop Art, Op Art, Minimalismo | - | B (Pop Art 0,75) | - | **3** | |
| Arte contemporanea: performance, instalacao, land art, digital, street art | - | A (14,18) | A (Idade contemporanea 1o) | **1** | |
| Barroco brasileiro, Missao Francesa, Modernismo brasileiro, Neoconcretismo, arte indigena, afro-brasileira e popular | - | A (Arte brasileira 17,16) | A (Culturas em tempos variados 2o) | **1** | |
| Musica; Teatro; Danca | - | M (8,21; 6,72; 4,48) | - | **2** | |
| Cinema e fotografia | - | - | - | **2** | sem dado |
| Patrimonio cultural material e imaterial | - | A (Patrimonio e museu 16,42) | - | **1** | |

#### Linguagens, Educacao Fisica
Amostra muito pequena: SAS aponta apenas 3 questoes no tema de topo em 2009-2024; EST nao tem categoria de Educacao Fisica.
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Cultura corporal, esporte (historia, regras), jogos e brincadeiras | - | - | A (Conceituacao de jogos, brincadeiras e esporte 1o; Corpo e cultura de movimento 2o) | **1** | |
| Saude, qualidade de vida, sedentarismo, nutricao e obesidade | - | - | M (3o saude e atividade fisica: A; 4o a 6o: M) | **2** | |
| Esporte-espetaculo, mitos, doping | - | - | M (7o) / B (8o) | **2** | |
| Lutas, ginasticas, dancas; corpo, padroes de beleza e midia | - | - | B (Luta 9o; Padroes de beleza 10o) | **3** | |
| Capacidades fisicas, inclusao e paralimpico, lazer, Jogos Olimpicos | - | - | - | **2** | sem dado |

#### Linguagens, Tecnologias da Informacao e Comunicacao
| Tema | AT | EST | SAS | Prio | Obs |
|---|---|---|---|---|---|
| Impacto e funcao das TIC, cibercultura, redes sociais, inclusao digital, trabalho e educacao | - | - | M (Impacto e funcao das TIC 9o na lista de Portugues) | **2** | |
| Linguagem da internet, desinformacao, bolhas e algoritmos, privacidade e LGPD, cyberbullying, IA | - | - | - | **2** | sem dado |

#### Redacao
Os rankings tratam de questoes objetivas; nenhum ranqueia temas de redacao. **Redacao, Estrutura e Tecnica** e **Redacao, Competencias da Correcao**: todos os temas **prioridade 2, sem dado** (regra do pedido). Observacao para quem consome: a redacao e obrigatoria e vale uma das cinco notas do Enem, entao a prioridade editorial pode ser tratada a parte (decisao sua, nao baseada nos rankings).

---

## 3. Notas finais

- Materias do CSV cobertas: todas as 35 (Matematica 9, Natureza 10, Humanas 6, Linguagens 8, Redacao 2).
- Maior risco de erro: temas de Linguagens (taxonomias muito diferentes entre AT, EST e SAS), Espanhol/Ingles (VW* unico a trazer percentual do periodo recente) e Educacao Fisica/Artes (amostras pequenas).
- A AT e o unico ranking recente completo (2016-2025) e pesa nos desempates; a EST e antiga (ate 2020) e a SAS nao descreve metodologia nem mostra percentuais por tema.
- Numeros complexos, matrizes, polinomios, funcao modular, composta/inversa e conicas: ver linhas acima e `provas.md` secao 6.
