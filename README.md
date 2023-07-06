# Text Content Analyzer [en-us]

This project is a text content parser that performs operations on a dataset.
Developed from a Hash Table base structure, the purpose of this service is to evaluate a set of data in its completeness and categories, starting from a set of expected keys and classes in the composition of the data.
The text content analyzer is a useful tool to analyze data and extract valuable information about it.

## How it works

This project uses Google Cloud Natural Language API to make the analysis.

The data manipulated during the use of the tool is stored at runtime in three Hash Tables that can be exported or imported to .csv files, they are:
- `data_table`: Stores the raw data to be analyzed
- `category_table`: Stores the data related to the analysis of the categories related to the text content that are compatible with the provided content list
- `completeness_table`: Stores data related to the completeness analysis of the provided data, verifying the existence of all information from a provided list of keys.


### Functionalities
Based on user interaction, this tool provides the following features:

- Populate data table from configured remote database: Retrieves existing data in the database and fills the data table to be manipulated.

- Populate data table from CSV file: Reads data from a CSV file and populates the data table to be manipulated.

- Analyze Data Categories: Analyzes the data categories based on the content of the data description and populates the category table with the resulting information for each entry.

- Analyze the completeness of the data: analyzes the completeness of the data based on the structure of the data and the existence of the values of its fields.

- Export data table as CSV file: Exports the data table to a CSV file.

- Export Data Categories as CSV File: Exports the categories table to a CSV file.

- Export Data Completeness as CSV File: Exports the completeness table to a CSV file.


The purpose of this tool is to validate whether data meets standard requirements to belong to a given dataset.

---

## Running the project
To run the project, you need to follow these steps:

- Clone this project repository.
- Create the .env file based on sample.env and set the environment vars
- Em um ambiente com Python 3, install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
- Run the run.py file:
```
python run.py
```


---


# Analisador de conteúdo de texto [pt-br]

Este projeto é um analisador de conteúdo de texto que executa operações em um conjunto de dados.
Desenvolvido a partir de uma estrutura base Hash Table, o objetivo deste serviço é avaliar um conjunto de dados em sua completude e categorias, a partir de um conjunto de chaves e classes esperadas na composição dos dados.
O analisador de conteúdo de texto é uma ferramenta útil para analisar dados e extrair informações valiosas sobre eles.

## Como funciona

Este projeto usa a API Google Cloud Natural Language para fazer a análise.

Os dados manipulados durante o uso da ferramenta são armazenados em tempo de execução em três Tabelas Hash que podem ser exportadas ou importadas para arquivos .csv, são elas:
- `data_table`: Armazena os dados brutos a serem analisados
- `category_table`: Armazena os dados relacionados à análise das categorias relacionadas ao conteúdo do texto que são compatíveis com a lista de conteúdo fornecida
- `completeness_table`: Armazena dados referentes à análise de completude dos dados fornecidos, verificando a existência de todas as informações de uma lista de chaves fornecida.


### Funcionalidades
Com base na interação do usuário, esta ferramenta fornece os seguintes recursos:

- Preencher tabela de dados do banco de dados remoto configurado: Recupera os dados existentes no banco de dados e preenche a tabela de dados a ser manipulada.

- Preencher tabela de dados do arquivo CSV: Lê os dados de um arquivo CSV e preenche a tabela de dados a ser manipulada.

- Analisar categorias de dados: analisa as categorias de dados com base no conteúdo da descrição de dados e preenche a tabela de categorias com as informações resultantes para cada entrada.

- Analisar a completude dos dados: analisa a completude dos dados com base na estrutura dos dados e na existência dos valores de seus campos.

- Exportar tabela de dados como arquivo CSV: Exporta a tabela de dados para um arquivo CSV.

- Exportar categorias de dados como arquivo CSV: exporta a tabela de categorias para um arquivo CSV.

- Exportar completude de dados como arquivo CSV: exporta a tabela de completude para um arquivo CSV.


O objetivo desta ferramenta é validar se os dados atendem aos requisitos padrão para pertencer a um determinado conjunto de dados.

---

## Executando o projeto
Para executar o projeto, você precisa seguir estas etapas:

- Clone este repositório de projeto.
- Crie o arquivo .env com base em sample.env e defina as variáveis ​​de ambiente
- Em um ambiente com Python 3, instale as dependências necessárias executando o seguinte comando:
```
pip install -r requirements.txt
```
- Execute o arquivo run.py:
```
python run.py
```