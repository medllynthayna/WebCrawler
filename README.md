# Análise de dados - Web Crawler

### Integrantes/Ra:
###### Guilherme Cardoso/318135325; Medllyn Thayna/318136828 ; Filipe Drumond/318127731; Victor Dutra/31811206; Breno Guimarães/31811209; Rafael Castro/318115768

## Estratégia utilizada: 
A estratégia utilizada para realizar a coleta de dados foi o método Web Crawler com o framework Scrapy sendo programado com linguagem Python.
Este método consiste em criar um coletor que é direcionado para um website de nosso interesse, onde  realizamos a coleta de dados por meio de um filtro. 
Este filtro é definido pelas tags do html da pagina do website,  selecionamos quais as informações da pagina queremos coletar.
Optamos por selecionar os nomes dos filmes mais populares e o seu ranking no ano de 2020 no site da IMDb. 

## Criação do coletor
Na criação do coletor utilizamos a seguinte estrutura.

![coletor](https://github.com/medllynthayna/WebCrawler/blob/master/coletor.PNG)

Nosso objetivo é coletar as seguintes informações do site IMDb: 

**titulo: nome dos filmes** 

**ranking: em qual posição o filme se econtra** 

![IMDB](https://github.com/medllynthayna/WebCrawler/blob/master/IBDM.PNG)

Atraves do seletor css **'td.titleColumn'** demos o primiero passo para coletar os dados do site. A coleta é feita usando os seguintes seletores:
#### titulo: td a::text

![nome Filme](https://github.com/medllynthayna/WebCrawler/blob/master/nomeFilme.PNG)

#### ranking : td div::text

![posicao Filme](https://github.com/medllynthayna/WebCrawler/blob/master/posicaoFilme.PNG)


Por fim temos como resultado um arquivo **.json** com as seguintes informações: 

![json](https://github.com/medllynthayna/WebCrawler/blob/master/json.PNG)
