import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils

class DepressionByStudyYear:
    def execute(self):
        print("Executando funcionalidade - Depressão por Ano de Estudo...")

        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        df = df[['Your current year of Study', 'Do you have Depression?']].dropna()
        df.columns = ['study_year', 'depression']

        df['study_year'] = df['study_year'].str.strip().str.lower().str.capitalize()
        df['depression'] = df['depression'].str.strip().str.lower().str.capitalize()

        total_by_year = df.groupby('study_year').size()
        print("\nTotal de alunos por ano de estudo:")
        print(total_by_year)

        depression_yes = df[df['depression'] == 'Yes'].groupby('study_year').size()

        depression_percentage = (depression_yes / total_by_year * 100).round(2).reindex(['Year 1', 'Year 2', 'Year 3', 'Year 4'])

        depression_percentage.index = ['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4']

        depression_percentage.plot(kind='bar', figsize=(10, 6))

        plt.title('Percentual de Estudantes com Depressão por Ano de Estudo')
        plt.xlabel('Ano de Estudo')
        plt.ylabel('Percentual (%)')
        plt.xticks(rotation=0)

        for index, value in enumerate(depression_percentage):
            plt.text(index, value + 1, f'{value}%', ha='center')

        plt.savefig('graphics/depression_percent_by_study_year.png')
        plt.close()

        return "Gráfico salvo como 'depression_percent_by_study_year.png'."
