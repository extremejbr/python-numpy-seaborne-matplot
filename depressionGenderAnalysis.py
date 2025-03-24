import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class DepressionGenderAnalysis:
    def execute(self):
        print("Executando funcionalidade 2...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Choose your gender', 'Do you have Depression?']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Gender', 'Depression']

        # Contar respostas por gênero e ansiedade
        anxiety_counts = df.groupby(['Gender', 'Depression']).size().unstack()

        # Criar o gráfico de barras
        anxiety_counts.plot(kind='bar', figsize=(10, 6))

        # Personalizar o gráfico
        plt.title('Presença de Depressão por Gênero')
        plt.xlabel('Gênero')
        plt.ylabel('Número de Respostas')
        plt.xticks(rotation=0)
        plt.legend(title='Tem Depressão?')

        # Salvar o gráfico como imagem
        plt.savefig('graphics/depression_by_gender.png')
        plt.close()

        return "Gráfico gerado e salvo como 'depression_by_gender.png'."