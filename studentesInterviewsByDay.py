import pandas as pd
import matplotlib.pyplot as plt
from utils import Utils


class StudentesInterviewsByDay:
    def execute(self):
        print("Executando funcionalidade 8...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # Filtrar as colunas relevantes e remover valores ausentes
        df = df[['Timestamp']].dropna()

        # Renomear colunas para facilitar o uso
        df.columns = ['Date']

        #Formatando e convetendo a columa da data de String para um tipo DateTime
        df['Date'] = df['Date'].str.split(' ').str[0]
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y").dt.strftime("%d/%m/%Y")

        # Contar o total de intrevistas por Data
        interviews = df.groupby(['Date']).size().reset_index(name='Total')
        print(f"\n{interviews}\n")

        #Atribui as colunas aos exios do gráfico de linha
        x=interviews["Date"]
        y=interviews["Total"]

        # Criar o gráfico de linha
        plt.plot(x, y, marker='o', linestyle='-', color='b')

        # Personalizar o gráfico
        plt.title('Período de coleta de dados')
        plt.xlabel('Data')
        plt.ylabel('Número de Entrevistas')
        plt.xticks(rotation=0)

        # Salvar o gráfico como imagem
        plt.savefig('graphics/students_interview_by_day.png')
        plt.close()

        return "Gráfico gerado e salvo como 'depression_by_gender.png'."