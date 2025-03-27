import pandas as pd
from utils import Utils

class ShowDataset:
    df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

    def execute(self):
        print("=" * 30)
        print("Executando Funcionalidade 1")
        print("=" * 30)
        print("\nPré-visualização dos Dados do DataFrame:")
        print(self.df.head())
        print("\n" + "=" * 30)
        return "Resultado da funcionalidade 1"