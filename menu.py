from showDataset import ShowDataset
from anxietyGenderAnalysis import AnxietyGenderAnalysis
from depressionGenderAnalysis import DepressionGenderAnalysis
from avarageAgeStudents import AvarageAgeStudents
from findByColumn import FindByColumn
from findValue import FindValue
from depressionAnxietyPercentualAnalysis import DepressionAnxietyPercentualAnalysis
from studentesInterviewsByDay import StudentesInterviewsByDay
from anxietyByAge import AnxietyByAge
from depressionByAge import DepressionByAge
from percentualByGender import PercentualByGender
from anxietyByStudyYear import AnxietyByStudyYear
from depressionByStudyYear import DepressionByStudyYear
from depressionByCourse import DepressionByCourse


class Menu:
    def __init__(menu):  # Construtor da classe Menu
        menu.options = {
            "1": ShowDataset(),
            "2": AnxietyGenderAnalysis(),
            "3": DepressionGenderAnalysis(),
            "4": FindValue(),
            "5": FindByColumn(),
            "6": AvarageAgeStudents(),
            "7": DepressionAnxietyPercentualAnalysis(),
            "8": StudentesInterviewsByDay(),
            "9": AnxietyByAge(),
            "10": DepressionByAge(),
            "11": AnxietyByStudyYear(),
            "12": DepressionByStudyYear(),
            "14": PercentualByGender(),
            "16": DepressionByCourse(),
            "0": None
        }

    def displayTitle():
        print("Análises em Dataset de Transtornos de Humor")

    def displayMenu(menu):  # Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Apresentar o Dataset")
        print("2 - Ansiedade por Gênero")
        print("3 - Depressão por Gênero")
        print("4 - Buscar um valor no DataSet")
        print("5 - Buscar um valor em uma coluna no DataSet")
        print("6 - Média de idade dos estudantes")
        print("7 - Percentual de estudantes com Transtorno Mental")
        print("8 - Total de entrevistas por dia")
        print("9 - Ansiedade por Idade")
        print("10 - Depressão por Idade")
        print("11 - Ansiedade por Ano de Estudo")
        print("12 - Depressão por Ano de Estudo")
        print("14 - Percentual de estudantes por gênero")
        print("16 - Depressão por Curso")
        print("0 - Sair")
