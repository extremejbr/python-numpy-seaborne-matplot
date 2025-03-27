from utils import Utils

class FindValue:
    def execute(self):
        print("Executando funcionalidade 4...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Solicita o valor a ser pesquisado
        value = Utils.inputText('Digite o valor a ser buscado: ')

        #Verifica se é um número e converte para um Float
        if value.isdigit():
            value = float(value)

        # Filtra os dados do dataFrame 
        result= df[df.isin([value]).any(axis=1)]

        # Verifica se o dataFrame está vazio
        if result.empty:
            result = "Não há dados correspodente"
        
        return result