import numpy as np
from utils import Utils

class CGP:
   def execute(self):
        print("Executando funcionalidade 16...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Função para converter os valores da coluna para float, tratando intervalos
        def parse_cgpa(value):
            if '-' in value:
                low, high = value.split('-')
                return (float(low.strip()) + float(high.strip())) / 2
            else:
                return float(value)

        # Aplicar a função na coluna e converter para numpy array
        cgpa = df['What is your CGPA?'].apply(parse_cgpa).to_numpy()
        
        # Calcular a mediana
        average_cgpa = np.median(cgpa)

        return f"A Media do CGPA é: {float(average_cgpa)}"