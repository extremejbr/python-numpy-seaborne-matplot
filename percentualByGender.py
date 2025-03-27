import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class PercentualByGender:
    def execute(self):
        print("Executando funcionalidade 13...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Choose your gender']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Gender']

        # Contar respostas por ansiedade e depressão (Transtono de humor)
        gender_counts = df.groupby(['Gender']).size()

        print(f'\n{gender_counts}\n')

        # Criar o gráfico de pizza
        gender_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6))

        # Personalizar o gráfico
        plt.title('Percentual por Gênero')
        plt.legend(title='Gênero',loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Salvar o gráfico como imagem
        plt.savefig('graphics/gender_percentual.png')
        plt.close()

        return "Gráfico gerado e salvo como 'gender_percentual.png'."