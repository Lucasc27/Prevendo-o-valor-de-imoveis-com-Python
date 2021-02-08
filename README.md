# Análisando e prevendo os preços de aluguéis de imóveis

### Entendimento do problema de negócio

Esse projeto tem como objetivo oferecer uma solução rápida, eficaz e em tempo real para fazer a previsão de valores dos aluguéis de imóveis do tipo apartamento de uma maneira diferenciada.
A escolha dos imóveis do tipo apartamento se deve ao volume de dados disponíveis para a construção do modelo capaz de retornar o valor dos aluguéis mais próximo da realidade possível sem deixar de considerar suas diversas características.

Por meio de análise das características vamos tentar justificar os respectivos valores que compõe o preço dos aluguéis, além de fazer previsões para atualizar os preços por meio de um modelo de machine learning.

### Coleta dos dados 
[Link para o script 1](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/blob/main/page_collector.py) - 
Script para coletar as listas de link's dos imóveis.

[Link para o script 2](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/blob/main/data_extract.ipynb) - 
Script para coletar os dados e características dos imóveis.

Para podermos simular o problema de negócio com o maior grau possível de realidade vamos coletar dados reais de imóveis de um dos maiores portais de imóveis do Brasil, o ZAP Imóvel(https://www.zapimoveis.com.br/).

Vamos usar um método em Python conhecido como Webscraping e vamos criar um Webcrawler que nada mais é do que um programa de computador que navega de forma automática pela rede em busca de dados.

### Pré-processamento [[Link para o script](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/blob/main/pr%C3%A9%20processamento.ipynb)]

Para que seja possível entender, analisar e manipular os dados teremos que fazer alguns pré-processamentos, nessa etapa vamos limpar e transformar os dados para que possamos usa-lós em uma análise exploratória e no modelo de machine learning.

### EDA - Análise exploratória de dados [[Link para o script](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/blob/main/An%C3%A1lise_explorat%C3%B3ria.ipynb)]

A fim de descobrirmos padrões consistentes e relações entre as variáveis que influenciam o preço do aluguel, vamos fazer uma análise exploratória nos dados que até aqui já estão bem tratados.

### Prediction - Machine Learning [[Link para a pasta dos scripts](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/tree/main/Modelos)]

Essa etapa consiste na criação do modelo de machine learning com objetivo de encontrar o melhor algoritmo que busque a formulação matemática para explicar a relação entre as variáveis que envolvem o preço dos aluguéis. Nesse processo de machine learning podemos criar vários e vários modelos usando técnicas e métodos diferentes afim de chegarmos em um resultado desejado, podemos criar a modelagem preditiva e se precisar voltarmos na etapa de pré-processamento para modificar algo ou até mesmo voltar na etapa de coleta de dados se acharmos que nossos dados não são suficiente para a modelagem.

### Desenvolvimento de um simulador de App

Por final e não menos importante, para poder simular um deploy de machine learning, vamos criar um App que faz as coletas de novos dados do usuário e usa o modelo treinado para fazer as novas previsões.
