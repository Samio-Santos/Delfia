import csv  # Importa o módulo 'csv' para manipulação de arquivos CSV
import traceback  # Importa o módulo 'traceback' para rastreamento de exceções

def processar_transacoes(valor_limite, arquivo_entrada, arquivo_saida, arquivo_log):
    transacoes_altas = []  # Inicializa uma lista para armazenar as transações com valor acima do limite
    
    try:
        with open(arquivo_entrada, 'r') as arquivo_csv:  # Abre o arquivo de entrada para leitura
            leitor_csv = csv.DictReader(arquivo_csv)  # Cria um leitor de CSV usando 'DictReader'

            for linha in leitor_csv:  # Itera sobre as linhas do arquivo CSV
                if float(linha['Valor da Transação']) > valor_limite:  # Verifica se o valor da transação é superior ao limite
                    transacoes_altas.append(linha)  # Adiciona a linha à lista de transações altas

        if transacoes_altas:  # Verifica se existem transações altas
            with open(arquivo_saida, 'w', newline='') as arquivo_saida_csv:  # Abre o arquivo de saída para escrita
                escritor_csv = csv.DictWriter(arquivo_saida_csv, fieldnames=transacoes_altas[0].keys())  # Cria um escritor de CSV usando 'DictWriter'
                escritor_csv.writeheader()  # Escreve o cabeçalho no arquivo de saída
                escritor_csv.writerows(transacoes_altas)  # Escreve as transações identificadas no arquivo de saída
        else:
            print(f"Nenhuma transação encontrada com valor superior a R${valor_limite}.")  # Imprime uma mensagem se não houver transações altas
    
    except Exception as e:
        # Em caso de exceção, registra o erro no arquivo de log
        with open(arquivo_log, 'a') as arquivo_log_txt:
            arquivo_log_txt.write(f"Erro durante o processamento das transações:\n{traceback.format_exc()}\n")
        print("Ocorreu um erro durante o processamento das transações. Consulte o arquivo de log para mais informações.")

# Executa o código quando o script é executado como um programa principal
if __name__ == "__main__":
    # Define os nomes dos arquivos e o valor limite
    valor_limite = 1000
    arquivo_entrada = 'transacoe'
    arquivo_saida = 'transacoes_altas.csv'
    arquivo_log = 'log_erros.txt'

    # Chama a função 'processar_transacoes' com os parâmetros especificados
    processar_transacoes(valor_limite, arquivo_entrada, arquivo_saida, arquivo_log)
