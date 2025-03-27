from utils import Utils

class FindByColumn:
    def execute(self):
        print("Executando funcionalidade 5...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Solicita a coluna a ser pesquisada
        column = Utils.inputText('Digite o nome de uma coluna: ')
        # Solicita o valor a ser pesquisado
        value = Utils.inputText('Digite o valor a ser buscado: ')

        #Verifica se é um número e converte para um Float
        if value.isdigit():
            value = float(value)

        # Filtra os dados do dataFrame 
        result = (df.loc[df[column]==value])

        # Verifica se o dataFrame está vazio
        if result.empty:
            result = "Não há dados correspodente"
        
        return result