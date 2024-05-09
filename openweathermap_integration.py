import requests  # Importa o módulo 'requests' para fazer solicitações HTTP

def obter_informacoes_clima(api_key, city):
    try:
        # Faz a solicitação GET para a API OpenWeatherMap
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric"
        resposta = requests.get(url)  # Faz a solicitação GET para a URL especificada

        resposta.raise_for_status()  # Verifica se houve algum erro na solicitação

        # Analisa os dados JSON retornados pela API
        dados_clima = resposta.json()
    
        # Extrai as informações necessárias
        descricao_clima = dados_clima['weather'][0]['description']  # Extrai a descrição do clima do JSON

        cidade = dados_clima['name']  # Extrai o nome da cidade do JSON
        temperatura_atual = dados_clima['main']['temp']  # Extrai a temperatura atual do JSON

        print(f'Cidade: {cidade}')  # Imprime o nome da cidade

        # Imprime a descrição do clima 
        print(f"Clima: {descricao_clima}")

        print(f"Temperatura atual: {temperatura_atual}°C")  # Imprime a temperatura atual em graus Celsius

    except Exception as e:
        # Trata adequadamente qualquer erro ou exceção que possa ocorrer
        print(f'Erro ao obter informações do clima da cidade de "{city.upper()}"! Causa do erro: {e.response.status_code if hasattr(e, "response") else "Erro desconhecido"}')
        return None, None


# executa o código quando o script é executado como um programa principal
if __name__ == "__main__":

    # Chave de API para autenticar as solicitações (substitua pela sua chave)
    api_key = "9b7fa3207f0925d9bea8b69f6c0378d5"

    # Solicita ao usuário o nome da cidade como entrada
    cidade = input("Digite o nome da cidade para verificar o clima: ").strip()
    print('\n')

    # Obtém e exibe as informações meteorológicas da cidade
    obter_informacoes_clima(api_key, cidade)
