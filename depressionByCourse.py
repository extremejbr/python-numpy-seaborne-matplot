import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import Utils

class DepressionByCourse:
    def execute(self):
        print("Executando funcionalidade - Gráfico e Estatísticas de Depressão por Curso...\n")

        sns.set_theme(style="whitegrid")

        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')
        df = df[['What is your course?', 'Do you have Depression?']].dropna()
        df.columns = ['course', 'depression']
        df['course'] = df['course'].str.strip().str.title()
        df['depression'] = df['depression'].str.strip().str.lower().str.capitalize()

        total_by_course = df.groupby('course').size()

        depression_yes = df[df['depression'] == 'Yes'].groupby('course').size()
        depression_yes = depression_yes[depression_yes > 0]

        total_filtered = total_by_course[depression_yes.index]

        data = pd.DataFrame({
            'Total': total_filtered,
            'Yes': depression_yes
        })
        data['Percentual'] = (data['Yes'] / data['Total'] * 100).round(2)
        data = data.sort_values(by='Yes', ascending=False)

        print("Resumo por curso:")
        for curso, row in data.iterrows():
            print(f"- {curso}: {row['Yes']} com depressão / {row['Total']} total ({row['Percentual']}%)")

     
        plt.figure(figsize=(14, 7))
        ax = sns.barplot(x=data.index, y=data['Yes'], palette='coolwarm', edgecolor='black')

        ax.set_title('Quantidade de Estudantes com Depressão por Curso')
        ax.set_xlabel('Curso')
        ax.set_ylabel('Qtd. com Depressão')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig('graphics/depression_yes_only_by_course_final.png')
        plt.close()

        return "Gráfico salvo como 'depression_yes_only_by_course_final.png'."
