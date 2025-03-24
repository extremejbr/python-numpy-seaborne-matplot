import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class AnxietyGenderAnalysis:
    def execute(self):
        print("Executando funcionalidade 2...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Choose your gender', 'Do you have Anxiety?']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Gender', 'Anxiety']

        # Contar respostas por gênero e ansiedade
        anxiety_counts = df.groupby(['Gender', 'Anxiety']).size().unstack()

        # Criar o gráfico de barras
        anxiety_counts.plot(kind='bar', figsize=(10, 6))

        # Personalizar o gráfico
        plt.title('Presença de Ansiedade por Gênero')
        plt.xlabel('Gênero')
        plt.ylabel('Número de Respostas')
        plt.xticks(rotation=0)
        plt.legend(title='Tem Ansiedade?')

        # Salvar o gráfico como imagem
        plt.savefig('graphics/anxiety_by_gender.png')
        plt.close()

        return "Gráfico gerado e salvo como 'anxiety_by_gender.png'."