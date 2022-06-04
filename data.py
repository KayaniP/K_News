from News import News
from States import States
states = [
    States(0, 'AC', 'Acre', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Acre.png'),
    States(1, 'AL', 'Alagoas', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Alagoas-300x200.png'),
    States(2, 'AP', 'Amapá', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amapa-300x210.png'),
    States(3, 'AM', 'Amazonas', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amazonas-300x214.png'),
    States(4, 'BH', 'Bahia', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Bahia-300x200.png'),
    States(5, 'CE', 'Ceará', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Ceara-300x210.png'),
    States(6,'DF', 'Distrito Federal', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Distrito_Federal_Brasil-300x210.png'),
    States(7, 'ES', 'Espírito Santo', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Espirito_Santo-300x210.png'),
    States(8, 'GO', 'Goiás', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Goias-300x210.png'),
    States(9, 'MA', 'Maranhão', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Maranhao-300x200.png'),
    States(10, 'MT', 'Mato Grosso', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso-300x210.png'),
    States(11, 'MS', 'Mato Grosso do Sul', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso_do_Sul-300x210.png'),
    States(12, 'MG', 'Minas Gerais', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Minas_Gerais-300x210.png'),
    States(13, 'PA', 'Pará', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Para-300x200.png'),
    States(14, 'PB', 'Paraíba', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Paraiba-300x210.png'),
    States(15, 'PR', 'Paraná', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Parana-300x210.png'),
    States(16, 'PE', 'Pernambuco', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Pernambuco-300x210.png'),
    States(17, 'PI', 'Piauí', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Piaui-300x200.png'),
    States(18, 'RJ', 'Rio de Janeiro', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Rio_de_Janeiro-300x210.png'),
    States(19, 'RN', 'Rio Grande do Norte', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Norte-300x200.png'),
    States(20, 'RS', 'Rio Grande do Sul', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Sul-300x210.png'),
    States(21, 'RO', 'Rondônia', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Rondonia-300x210.png'),
    States(22, 'RR', 'Roraima', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Roraima-300x200.png'),
    States(23, 'SC', 'Santa Catarina', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Santa_Catarina-300x218.png'),
    States(24, 'SP', 'São Paulo', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Sao_Paulo-300x200.png'),
    States(25, 'SG', 'Sergipe', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Sergipe-300x210.png'),
    States(26, 'TO', 'Tocantins', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Tocantins-300x210.png')
]


acNews = [
      News(0, 'Veja onde se vacinar contra a Covid-19 nesta segunda-feira (4), em Rio Branco', 'A Saúde de Rio Branco volta com a aplicação das doses da vacina contra a Covid-19, nesta segunda-feira (4), após suspender a imunização nesse domingo (3). A vacinação ocorre das 8h às 16h, em unidades de saúde da capital. (Veja pontos abaixo). / O público infantil é atendido exclusivamente em seis unidades de saúde da família no período de 8h às 11h e de 14h às 16h. Crianças de 5 a 11 anos deve estar acompanhadas com os pais ou responsáveis na hora da imunização. Assim como os adolescentes de 12 anos ou mais.', 'https://s2.glbimg.com/KK0PIDfJ2Mg_IBEzZm4ykHQE-Hc=/0x0:1280x853/1000x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/J/o/jkojWgSgWpNANSsRY4CA/vacina-5.jpg', False, 'AC'),
]

alNews = [
    News(1, 'Alagoas tem mais um domingo sem morte por Covid-19, aponta boletim', 'O Boletim Epidemiológico da Secretaria de Estado da Saúde (Sesau) deste domingo (3) mostra que não foi registrada nenhuma morte por Covid-19 nas últimas 24h em Alagoas, onde foram confirmados quatro novos casos. A última vez que o Estado teve um dia sem registro de morte foi no domingo passado (27), data em que também não foi registrado nenhum caso de Covid-19. /  Com esses dados, o Estado tem agora o total de 296.252 casos confirmados do novo coronavírus até o momento, dos quais 152 estão em isolamento domiciliar. Outros 288.958 pacientes já finalizaram o período de isolamento, não apresentam mais sintomas e estão recuperados da doença. Há 1.364 casos em investigação epidemiológica. Alagoas segue, assim, com 6.888 óbitos por Covid-19.', 'https://gwebs3.redacms.com/images/hospital_de_campanha_covid-19_com.2e16d0ba.fill-1120x700.jpg', False, 'AL'),
]

apNews = [
    News(2, 'Crianças, adolescentes e adultos: saiba onde Macapá vacina contra a Covid-19 em 4 de abril', 'Nesta segunda-feira (4), Macapá oferta vacinas contra a Covid-19 para todos os públicos a partir dos 5 anos de idade, inclusive a segunda dose de reforço para o público de 60 anos ou mais. / Para quem está dentro do prazo previsto, são ofertadas doses de AstraZeneca, Janssen, CoronaVac e Pfizer.', 'https://s2.glbimg.com/J4jrF2T7-pIwK_wnxFV_J6_92F8=/0x0:800x450/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/6/U/fu0M2cSXiAEyUFVWyWyg/51484138715-cc97233bfc-c.jpg', False, 'AP'),
]

amNews = [
    News(3, 'Apesar de 8 novos casos, Amazonas não registra mortes por Covid-19', 'O Amazonas não registrou mortes por Covid-19 neste domingo (3), segundo dados do boletim da Fundação de Vigilância em Saúde do Amazonas (FVS-AM). O total de vidas perdidas para a doença desde o início da pandemia permanece em 14.157 vítimas. / Entre as vítimas em Manaus, há o registro de 9.697 óbitos confirmados em decorrência do novo coronavírus. No interior, são 61 municípios com óbitos confirmados até o momento, totalizando 4.460.', 'https://s2.glbimg.com/zJrekm3v1XvQJXP8aDVSJo9Qkps=/0x0:1280x853/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/C/A/fVoBAxSXOPJGdj4xmBNQ/whatsapp-image-2022-02-19-at-17.17.38.jpeg', True, 'AM'),
]

bhNews = [
    News(4, 'Bahia registra 1.342 casos ativos de covid-19 e mais 5 mortes', 'O boletim epidemiológico deste sábado (2) registra 1.342 casos ativos de covid-19 na Bahia. Nas últimas 24 horas, foram registrados 616 casos de covid-19 e mais 5 mortes. Dos 1.533.984 casos confirmados desde o início da pandemia, 1.502.919 já são considerados recuperados e 29.723 tiveram óbito confirmado. / O boletim epidemiológico contabiliza ainda 1.816.597 casos descartados e 327.700 em investigação.', 'https://i0.wp.com/www.conass.org.br/wp-content/uploads/2021/04/Bahia-passa-a-ter-capacidade-para-realizar-mil-testes-dia%CC%81rios-da-Covid-19-5-555x369-1.jpg?fit=555%2C369&ssl=1', False, 'BH')
]

ceNews = [
    News(5, 'Ceará soma 26.777 mortes e 1.241.271 casos de Covid-19', 'Desde o início da pandemia no Ceará, há quase dois anos, o Estado já confirmou 1.241.271 casos de Covid-19 e 26.777 mortes em decorrência da infecção. Os dados são da última atualização da plataforma IntegraSUS, da Secretaria da Saúde do Estado do Ceará (Sesa), às 7h13min desta segunda-feira, 4.', 'https://www.opovo.com.br/_midias/jpg/2022/04/01/818x460/1_pzzb8946-18453965.jpeg', False, 'CE')
]

dfNews = [
    News(6, 'Covid-19: DF tem 237 novos casos e mais 5 mortes', 'O Distrito Federal registrou 237 novos casos conhecidos de Covid-19 e mais 5 mortes pela doença, nesta segunda-feira (4). Os números são referentes ao acumulado entre sábado (2) e esta segunda, uma vez que, nos fins de semana e nos feriados, não há divulgação do boletim, por parte da Secretaria de Saúde.', 'https://s2.glbimg.com/JrLtt0r7DNAl2RnMWOz1rbhRgG0=/0x0:976x549/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/C/g/GQZsJqSRA2qwqAhcCAqQ/imagem1.jpg', False, 'DF')
]

esNews = [
    News(7, 'ES chega a 14.342 mortes e 1.040.089 casos confirmados de Covid-19', 'O Espírito Santo registrou, até esta segunda-feira (4), 14.342 mortes por Covid-19. O número de casos confirmados chegou a 1.040.089. O índice de letalidade da doença no estado é de 1,38%. Os dados foram divulgados na plataforma Painel Covid-19, do governo do estado.', 'https://www.paho.org/sites/default/files/styles/max_1500x1500/public/2021-05/covid-19-variants.jpg?itok=szJH1mCw', False, 'ES')
]

goNews = [
    News(8, 'Atualização sobre a Covid-19 em Goiás e doses da vacina já aplicadas', 'A Secretaria de Estado da Saúde de Goiás (SES-GO) informa que há 1.286.311 casos de doença pelo coronavírus 2019 (Covid-19) no território goiano. No Estado, há 771.094 casos suspeitos em investigação e 318.324 casos já foram descartados. Há 26.294 óbitos confirmados de Covid-19 em Goiás até o momento, o que significa uma taxa de letalidade de 2,05%. Há 326 óbitos suspeitos que estão em investigação.', 'https://www.saude.go.gov.br/images/2022/noticias/marco/2803-Vacinacao-Britto.jpeg', True, 'GO')
]

maNews = [
    News(9, 'Maranhão completa uma semana sem registro de mortes por Covid-19', 'O Maranhão completou neste domingo (3) uma semana sem registro de mortes por Covid-19, segundo a Secretaria de Estado da Saúde (SES). Os registros são de 28 de março a 3 de abril e foram obtidos a partir do boletim epidemiológico que é divulgado diariamente pela pasta. Na mesma semana, foram 2.093 casos registrados da doença e está em tendência de queda. Neste domingo (3), 18 foram registrados na Ilha de São Luís e 4 nas remais regiões do estado.', 'https://s2.glbimg.com/7TzGzN6c5oC1ZD6SM9-a96iEdNg=/0x0:1024x683/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/g/Y/BPnsgKSKOARN0lCiLyuw/whatsapp-image-2021-12-27-at-14.26.13.jpeg', False, 'MA')
]

mtNews = [
    News(10, 'Sexta-feira (01): Mato Grosso registra 727.094 casos e 14.869 óbitos por Covid-19', 'A Secretaria de Estado de Saúde (SES-MT) notificou, até a tarde desta sexta-feira (01.04), 727.094 casos confirmados da Covid-19 em Mato Grosso, sendo registrados 14.869 óbitos em decorrência do coronavírus no Estado. Foram notificadas 434 novas confirmações de casos de coronavírus no Estado. Dos 727.094 casos confirmados da Covid-19 em Mato Grosso, 449 estão em isolamento domiciliar e 711.206 estão recuperados.', 'http://www.mt.gov.br/documents/21013/11469654/_TCH5376.jpg/6de9de1b-993e-07bb-9089-a480e06b2462?t=1557930779523+&imageThumbnail=3', False, 'mt')
]

msNews = [
    News(11, 'MS confirma 159 casos novos e mais 3 mortes por Covid-19 neste sábado', 'A Secretaria de Estado de Saúde (SES) de Mato Grosso do Sul confirmou, neste sábado (2), 159 novos casos de Covid-19 e 3 óbitos pela doença. O estado atingiu 524.755 infectados desde o início da pandemia e 10.507 óbitos, segundo dados do boletim epidemiológico. A média móvel dos últimos 7 dias é de 195,3 registros a cada 24 horas. Os novos casos de hoje trazem Campo Grande à frente, com 49 novos casos, seguida por Paranaíba (43) e Rio Verde do Mato Grosso (15).', 'https://s2.glbimg.com/KV_3IqrAQiDNur-QZnXvy1YX8qw=/0x0:1024x682/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/n/B/ozWjB9QCi7pZsjAt464w/image1024x768.jpg', False, 'MS')
]

mgNews = [
    News(12, 'Minas Gerais registra 42 óbitos por Covid-19 em 24 horas', 'Minas Gerais registrou 1.324 novos casos conhecidos de Covid-19 e 42 mortes foram confirmadas decorrentes da doença nas últimas 24 horas. Desde o início da pandemia, 3.333.724 pessoas testaram positivo para o coronavírus no estado. Destas, 3.221.184 se recuperaram da doença. Outros 51.589 pacientes estão em acompanhamento.', 'https://s2.glbimg.com/K0e3y7yvKIrshkBXs0vlViYEPj4=/0x0:1024x768/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/H/M/Bye25GSwiXBuIzeBEAXg/whatsapp-image-2022-04-01-at-17.41.10.jpeg', False, 'MG')
]

paNews = [
    News(13, 'Pará registra 756.124 casos e 18.121 mortes por Covid-19', 'O Pará contabilizou mais 176 casos de Covid-19 e 3 mortes causadas pela doença, segundo o boletim divulgado pela Secretaria de Saúde Pública do Pará (Sespa) neste domingo (3). Agora são 756.124 pessoas diagnosticadas com a doença desde março de 2020, sendo que 18.121 morreram.', 'https://s2.glbimg.com/MW0_5yUtU0LuveAxpAzrvnFlJz4=/0x0:1920x960/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/Q/x/B8DlKjT12NHuoC9jAmYQ/virus-molecula-covid-19-coronavirus-cred-peter-linforth-pixabay.jpg', False, 'PA')
]

pbNews = [
    News(14, 'Paraíba vacina 38,6 mil pessoas em dois dias de mobilização contra a Covid-19', 'A Paraíba somou um total de 38.671 pessoas vacinadas nos dias D contra a Covid-19, realizados na última sexta-feira (1º) e nesse sábado (2). A iniciativa, mobilizada pela Secretaria de Estado da Saúde (SES), teve o intuito de atualizar o cartão de vacinas de mais de 1,5 milhão de paraibanos que estão com doses contra o coronavírus em atraso', 'https://portalcorreio.com.br/portalcorreio/wp-content/uploads/2022/04/eeb34ed14b34bc322638aa6b12d63154.jpg', False, 'PB')
]

prNews = [
    News(15, 'Covid: Confira cronograma de vacinação de segunda (4) a sexta-feira (8), em Curitiba', 'A Secretaria Municipal da Saúde (SMS) de Curitiba divulgou o cronograma de vacinação contra a Covid para a próxima semana. O atendimento será de segunda (4) a sexta-feira (8), das 8h às 17h, em 11 unidades de saúde. Conforme a prefeitura, cerca de 28.500 pessoas são esperadas para receber a segunda dose e as doses de reforço da vacina anticovid, além das repescagens.', 'https://s2.glbimg.com/3v3A1sgrNJ0Kf10lM-h6fxdUznQ=/0x0:800x533/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/i/B/7kkeABRvOmOHACMtQlmg/vacina.jpg', False, 'PR')
]

peNews = [
    News(16, 'Pernambuco confirma mais 232 casos e oito mortes por Covid e recebe mais doses de vacinas', 'O governo de Pernambuco confirmou, nesta segunda (4), mais 232 casos do novo coronavírus. A Secretaria Estadual de Saúde (SES-PE) também registrou oficialmente outras oito mortes provocadas pela Covid. O estado recebeu nova remessa de vacinas. Segundo o boletim de acompanhamento da pandemia, desde o início da crise sanitária, em março de 2020, o estado totalizou 900.990 casos confirmados da doença, sendo 58.366 graves e 842.624 leves.', 'https://s2.glbimg.com/ZQgPgAoWAJMYguv9P9FQAakVDTE=/0x0:1280x853/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/W/q/BzbFXoSfWZZAXPN6wA9A/whatsapp-image-2022-01-29-at-16.43.42-1-.jpeg', False, 'PE')
]

piNews = [
    News(17, 'Piauí entra no 3º dia seguido sem registrar óbitos por covid-19, diz Sesapi', 'O Piauí entrou no 3º dia seguido sem registrar óbitos por covid-19. A informação é da Secretaria de Saúde do Estado (Sesapi). O último registro aconteceu na sexta-feira, dia 1º. No domingo, de acordo com a Sesapi, não foram registrados casos e nem  óbitos por Covid-19. O mesmo aconteceu no sábado, dia 2. Nesta segunda-feira (4), a Sesapi notificou 45 casos confirmados de covid-19. Destes, 28 são de mulheres e 17 de homens, com idades entre 03 a 69 anos.', 'https://cidadeverde.com/assets/uploads/posts/UaifotoFolhapress-covid-coronavirus-exames-testes.jpg', False, 'PI')
]

rjNews = [  
    News(18, 'Covid-19: intervalo entre as doses da vacina da Pfizer para crianças é reduzido para 21 dias', 'A partir desta quinta-feira (31/3), o intervalo entre a primeira e a segunda dose da vacina Pfizer pediátrica passa a ser de 21 dias no município do Rio de Janeiro. As crianças que tomaram a primeira dose neste período ou mais podem ir aos postos para completar o esquema vacinal. / O município atingiu a marca de 60% da população carioca vacinada com a dose de reforço. Todas as pessoas com 18 anos ou mais que tomaram a segunda dose há quatro meses ou mais devem tomar a dose de reforço, que pode ser antecipada até o intervalo mínimo de três meses em casos de viagem, problemas de saúde e outras questões pessoais.', 'https://prefeitura.rio/wp-content/uploads/2022/03/51844525588_afd1513866_w.jpg', True, 'RJ'),
]

rnNews = [
    News(19, 'Decreto torna uso de máscara facultativo em locais abertos e fechados de Parnamirim, na Grande Natal', 'Um decreto da Prefeitura de Parnamirim, publicado no último sábado (2), tornou o uso de máscara de proteção contra a Covid-19 facultativo em locais abertos e fechados do município. Os moradores do município já não eram obrigados a usar a proteção em locais abertos desde o dia 10 de março, mas a obrigação seguia vigente para locais fechados.', 'https://s2.glbimg.com/0nS8Lpqcsn68JiZ1kz8M8NNqzNM=/0x0:1700x1065/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/v/M/mlhBzjQFaOsR66P8edOQ/msc.jpg', False, 'RN')
]

rsNews = [
    News(20, 'RS tem 117 internados com Covid em UTI, menor número desde maio de 2020', 'O Rio Grande do Sul tinha, no começo da tarde desta segunda-feira (4), 117 pacientes internados em leitos de UTI com diagnóstico positivo para Covid-19. É o menor número desde 21 de maio de 2020, no começo da pandemia, quando 114 pessoas estavam hospitalizadas com coronavírus.', 'https://www.gov.br/saude/pt-br/assuntos/noticias/2021-1/dezembro/ministerio-da-saude-recomenda-vacinacao-de-criancas-contra-a-covid-19/ministerio-da-saude-recomenda-vacinacao-de-criancas-contra-a-covid-19.png', False, 'RS')
]

roNews = [
    News(21, 'Rondônia registra mais de 3 mil novos casos de Covid e 9 mortes em uma semana', 'Rondônia registrou 3.179 novos casos conhecidos de Covid-19 nos últimos sete dias. Chegando no sábado (2) com o total de 394.966 testes positivos desde o início da pandemia. Já entre as mortes confirmadas, em uma semana o estado registrou 9. Chegando ao total de 7.181 vidas perdidas desde começo da crise sanitária.', 'https://s2.glbimg.com/UKi2Zs8_azCokWpqfL3mVWNgZjw=/0x0:1280x960/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/h/B/qZyWTFQ3SDx0EGksisPQ/photo-2022-02-16-13-50-52.jpg', False, 'RO')
]

rrNews = [
    News(22, 'Roraima completa três dias sem internados com Covid-19 na UTI', 'Roraima chegou ao terceiro dia sem registrar pacientes gravemente internados com Covid-19 na Unidade de Terapia Intensiva (UTI) do Hospital Geral de Roraima (HGR). A informação é do boletim epidemiológico divulgado pela Secretaria Estadual de Saúde. Na unidade, existem oito leitos de UTI e 15 de enfermaria (clínicos) - estes responsáveis por receber os casos mais estáveis da doença.', 'https://cdn.folhabv.com.br/images/noti-1648813937.webp', False, 'RR')
]

scNews = [
    News(23, 'Matriz de risco: SC tem 17 regiões no menor nível de risco para a Covid-19', 'Todas as regiões de Santa Catarina estão no menor nível de risco para a Covid-19. Segundo a matriz de risco que monitora a situação da pandemia no estado, divulgada neste sábado (2), as 17 áreas do estado foram classificadas como situação moderada (cor azul) para a doença.', 'https://s2.glbimg.com/9AzFL8NLplTdvO33eFu02H2nlYE=/0x74:620x520/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/H/Z/ILuGmwQgAbNmS26GOz2Q/matriz-02-04-22-20220402-1257021147.png', False, 'SC')
]

spNews = [
    News(24, 'Cidade de SP aplica 4ª dose da vacina contra a Covid-19 em maiores de 60 anos a partir desta segunda', 'A cidade de São Paulo começa a aplicar nesta segunda-feira (4) a quarta dose da vacina contra a Covid-19 em idosos acima de 60 anos. A capital também inicia a aplicação da vacina contra o vírus influenza, causador da gripe, em idosos maiores de 60 anos e em profissionais da saúde.', 'https://s2.glbimg.com/qRMZlMHG-OPcN5kgUmD2FCTP4SU=/0x0:1620x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/I/x/i8zeXVTHGyy9ADaBcl2A/fup20210421050.jpg', True, 'SP'),
]

sgNews = [
    News(25, 'Sergipe registra 122 novos casos conhecidos de Covid-19 e nenhuma morte', 'Desde o início da pandemia, 326.314 pessoas testaram positivo para a doença e 6.321 morreram. A taxa de letalidade no estado é de 1,9%, a de mortalidade de 275 e a de incidência de 14.195,6. Em virtude da continuidade da contaminação pela Covid-19 e por acreditarem que muitas pessoas não realizam o teste para a identificação da doença, mesmo sendo necessário, especialistas recomendam a manutenção do uso de máscara, álcool em gel, distanciamento social e isolamento das pessoas com sintomas.', 'https://s2.glbimg.com/C0GekVmkfRJpOa4AZnUOF7uH7d4=/0x0:1280x916/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/l/l/WhkK9kQuGfNCxA0aONyw/whatsapp-image-2022-03-04-at-11.16.37.jpeg', False, 'SG')
]

toNews = [
    News(26, 'Araguaína zera número de casos de Covid-19 pela primeira vez desde o início da pandemia', 'O número de casos ativos de Covid-19 foi zerado em Araguaína, nesta segunda-feira (4), pela primeira vez desde o início da pandemia. Segundo a Secretaria Municipal de Saúde, não há nenhum novo diagnóstico da doença desde sexta-feira (1º). O primeiro diagnóstico da doença na cidade aconteceu há pouco mais de dois anos, no dia 27 de março de 2020, pouco depois da capital. Araguaína ficou aproximadamente cinco meses liderando os números de Covid-19 até ser ultrapassada por Palmas em agosto daquele ano. Atualmente são 43.404 casos confirmados e 604 mortes.', 'https://s2.glbimg.com/1sDnYSF3UTQQRIDSPw4XaHYz_cY=/0x0:1280x720/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/m/k/0uBZFTSxGAfYDXOj9FXQ/araguaina.jpg', False, 'TO')
]

news = [states[0].set_news(acNews), states[1].set_news(alNews), states[2].set_news(apNews),  states[3].set_news(amNews), states[4].set_news(bhNews),  states[5].set_news(ceNews), states[6].set_news(dfNews), states[7].set_news(esNews), states[8].set_news(goNews), states[9].set_news(maNews), states[10].set_news(mtNews), states[11].set_news(msNews), states[12].set_news(mgNews), states[13].set_news(paNews), states[14].set_news(pbNews), states[15].set_news(prNews), states[16].set_news(peNews), states[17].set_news(piNews), states[18].set_news(rjNews), states[19].set_news(rnNews), states[20].set_news(rsNews), states[21].set_news(roNews), states[22].set_news(rrNews), states[23].set_news(scNews), states[24].set_news(spNews), states[25].set_news(sgNews), states[26].set_news(toNews)]

