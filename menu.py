from showDataset import ShowDataset
from anxietyGenderAnalysis import AnxietyGenderAnalysis
from depressionGenderAnalysis import DepressionGenderAnalysis
from avarageAgeStudents import AvarageAgeStudents
from findByColumn import FindByColumn
from findValue import FindValue
from depressionAnxietyPercentualAnalysis import DepressionAnxietyPercentualAnalysis
from studentesInterviewsByDay import StudentesInterviewsByDay
from percentualByGender import PercentualByGender

class Menu:
    def __init__(menu): ## Construtor da classe Menu
        menu.options = {
            "1": ShowDataset(),
            "2": AnxietyGenderAnalysis(),
            "3": DepressionGenderAnalysis(),
            "4": FindValue(),
            "5": FindByColumn(),
            "6": AvarageAgeStudents(),
            "7": DepressionAnxietyPercentualAnalysis(),
            "8": StudentesInterviewsByDay(),
            "14": PercentualByGender(),
            "0": None
        }

    def displayTitle():
        print("Análises em Dataset de Transtornos de Humor")
        
    def displayMenu(menu): ## Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Mostar Dataset")
        print("2 - Mostrar Ansiedade por Gênero")
        print("3 - Mostrar Depressão por Gênero")
        print("4 - Buscar um valor no DataSet")
        print("5 - Buscar um valor em uma coluna no DataSet")
        print("6 - Média de idade dos estudantes")
        print("7 - Percentual de estudantes com Transtorno Mental")
        print("8 - Total de entrevistas por dia")
        print("14 - Percentual de estudantes por gênero")
        print("0 - Sair")
