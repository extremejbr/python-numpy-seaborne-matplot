import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class DepressionByAge:
    def execute(self):
        print("Executando funcionalidade 10...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Age', 'Do you have Depression?']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Age', 'Depression']

        # Contar respostas por idade e ansiedade
        anxiety_counts = df.groupby(['Age', 'Depression']).size().unstack()

        # Criar o gráfico de barras
        anxiety_counts.plot(kind='bar', figsize=(10, 6))

        # Personalizar o gráfico
        plt.title('Presença de Depressão por Idade')
        plt.xlabel('Idade')
        plt.ylabel('Número de Respostas')
        plt.xticks(rotation=0)
        plt.legend(title='Tem Depressão?')

        # Salvar o gráfico como imagem
        plt.savefig('graphics/depression_by_age.png')
        plt.close()

        return "Gráfico gerado e salvo como 'depression_by_age.png'."
