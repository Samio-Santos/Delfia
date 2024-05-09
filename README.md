# Delfia

## Descrição do Projeto

### ETAPA 1: Automatização de Processamento de Dados CSV

Este projeto foca na automatização do processamento de dados em um arquivo CSV contendo informações sobre transações financeiras. O objetivo é desenvolver um script Python que leia o arquivo CSV, identifique as transações que estão acima de um determinado valor (por exemplo, $1000) e as salve em um novo arquivo CSV.

**Requisitos:**
- O script deve ser capaz de ler um arquivo CSV chamado `transacoes.csv`.
- Identificar transações com valor superior a $1000.
- Salvar as transações identificadas em um novo arquivo chamado `transacoes_altas.csv`.

**Critérios de Avaliação:**
- Funcionalidade correta e precisa.
- Boa prática de código (Clean Code).
- Tratamento adequado de erros, a aplicação não pode quebrar caso tenha algum erro na planilha.
- Logs em txt para registro de erros.
- Eficiência e desempenho do código.

**Observações:**
- Comente seu código para explicar decisões ou abordagens específicas.

**Exemplo de Estrutura do Arquivo CSV que será utilizado para teste (`transacoes.csv`):**

Nome do Cliente,Valor da Transação,Data da Transação
Cliente A,1200,2023-01-15
Cliente B,800,2023-02-02
Cliente C,1500,2023-03-10
Cliente D,900,2023-04-05


### ETAPA 2: API Rest e Python

Este projeto envolve a integração com uma API REST para obter informações meteorológicas de uma cidade específica.

**Tarefas:**
- Conexão com a API OpenWeatherMap:
  - Faça uma solicitação GET para a API OpenWeatherMap ([OpenWeatherMap API](https://openweathermap.org/current)) para obter informações meteorológicas de uma cidade de sua escolha.
  - Crie uma chave de API para autenticar suas solicitações.
  - Extraia e exiba os seguintes detalhes sobre o clima atual da cidade:
    - Descrição do clima (por exemplo, "ensolarado", "chuvoso", etc.).
    - Temperatura atual em graus Celsius.
- Manipulação de Dados JSON:
  - Analise os dados JSON retornados pela API e extraia as informações necessárias para exibição.
  - Certifique-se de lidar adequadamente com qualquer erro ou exceção que possa ocorrer durante o processo de solicitação e análise dos dados.
- Exibição de Resultados:
  - Exiba as informações meteorológicas de forma clara e legível no console.
- Melhorias Opcionais:
  - Permita que o usuário insira o nome da cidade como entrada, em vez de codificar a cidade diretamente no código.
  - Implemente outras funcionalidades adicionais que você considerar relevantes ou interessantes.
  
**Observações:**
- Você pode usar qualquer IDE ou editor de texto de sua preferência para escrever o código.
- Certifique-se de incluir comentários adequados em seu código para explicar sua lógica e fornecer contexto quando necessário.

## Instruções de Uso

### Passo 1: Crie um Ambiente Virtual

No diretório principal do projeto, abra o terminal e execute o seguinte comando para criar um ambiente virtual:


COMANDO: python -m venv .venv


Em seguida, ative o ambiente virtual com base no seu sistema operacional:

**Windows:**

COMANDO:.venv\Scripts\activate.bat

**Linux/Mac:**

COMANDO: source .venv/bin/activate



### Passo 2: Instale as Dependências do Projeto

No diretório principal do projeto, onde se encontra o arquivo "requirements.txt", abra o terminal e execute o seguinte comando para instalar as dependências:

COMANDO: pip install -r requiriments.txt


### Passo 3: Execute os Arquivos Python

#### Executar o Arquivo "processar_dados_csv.py"

No diretório principal do projeto, onde se encontra o arquivo "processar_dados_csv.py", abra o terminal e execute o seguinte comando para executar a automatização do processamento de um arquivo CSV:


COMANDO: python3 processar_dados_csv.py


*Observação*: A Etapa 1 deste projeto se concentra na automatização do processamento de dados em um arquivo CSV contendo informações sobre transações financeiras. O objetivo é escrever um script Python que leia o arquivo CSV, identifique as transações que estão acima de um determinado valor (por exemplo, $1000) e as salve em um novo arquivo CSV.


#### Executar o Arquivo "openweathermap_integration.py"

No diretório principal do projeto, onde se encontra o arquivo "openweathermap_integration.py", abra o terminal e execute o seguinte comando para executar openweathermap_integration:

COMANDO: python3 openweathermap_integration.py


*Observação*: A Etapa 2 deste projeto envolve a integração com uma API REST para obter informações meteorológicas de uma cidade específica.


