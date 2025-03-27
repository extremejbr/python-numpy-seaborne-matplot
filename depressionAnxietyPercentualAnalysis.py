import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class DepressionAnxietyPercentualAnalysis:
    def execute(self):
        print("Executando funcionalidade 7...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Do you have Anxiety?', 'Do you have Depression?']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Anxiety', 'Depression']

        # Contar respostas por ansiedade e depressão (Transtono de humor)
        mood_disorder_counts = df.groupby(['Anxiety', 'Depression']).size()

        print(f'\n{mood_disorder_counts}\n')

        # Criar o gráfico de pizza
        mood_disorder_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6))

        # Personalizar o gráfico
        plt.title('Presença de Ansiedade e/ou Depressão')
        plt.legend(title='Tem Ansiedade e/ou Depressão?',loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Salvar o gráfico como imagem
        plt.savefig('graphics/mood_disorder_percentual.png')
        plt.close()

        return "Gráfico gerado e salvo como 'mood_disorder_percentual.png'."