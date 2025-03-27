import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils

class AnxietyByStudyYear:
    def execute(self):
        print("Executando funcionalidade - Ansiedade por Ano de Estudo...")

        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        df = df[['Your current year of Study', 'Do you have Anxiety?']].dropna()
        df.columns = ['study_year', 'anxiety']

        df['study_year'] = df['study_year'].str.strip().str.lower().str.capitalize()
        df['anxiety'] = df['anxiety'].str.strip().str.lower().str.capitalize()

        total_by_year = df.groupby('study_year').size()
        anxiety_yes = df[df['anxiety'] == 'Yes'].groupby('study_year').size()

        anxiety_percentage = (anxiety_yes / total_by_year * 100).round(2).reindex(['Year 1', 'Year 2', 'Year 3', 'Year 4'])

        anxiety_percentage.index = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4']

        anxiety_percentage.plot(kind='bar', figsize=(10, 6))

        plt.title('Percentual de Estudantes com Ansiedade por Ano de Estudo')
        plt.xlabel('Ano de Estudo')
        plt.ylabel('Percentual (%)')
        plt.xticks(rotation=0)

        for index, value in enumerate(anxiety_percentage):
            plt.text(index, value + 1, f'{value}%', ha='center')

        plt.savefig('graphics/anxiety_percent_by_study_year.png')
        plt.close()

        return "Gráfico salvo como 'anxiety_percent_by_study_year.png'."
