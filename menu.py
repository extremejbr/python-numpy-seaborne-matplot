from showDataset import ShowDataset
from anxietyGenderAnalysis import AnxietyGenderAnalysis
from depressionGenderAnalysis import DepressionGenderAnalysis
from findByColumn import FindByColumn
from findValue import FindValue
from depressionAnxietyPercentualAnalysis import DepressionAnxietyPercentualAnalysis

class Menu:
    def __init__(menu): ## Contrutor da classe Menu
        menu.options = {
            "1": ShowDataset(),
            "2": AnxietyGenderAnalysis(),
            "3": DepressionGenderAnalysis(),
            "4": FindValue(),
            "5": FindByColumn(),
            "7": DepressionAnxietyPercentualAnalysis(),
            "0": None
        }

    def displayTitle():
        print("Aqui vai o Nome do Projeto")
    
    def displayMenu(menu): ## Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Mostar Dataset")
        print("2 - Mostrar Ansiedade por Gênero")
        print("3 - Mostrar Depressão por Gênero")
        print("4 - Buscar um valor no DataSet")
        print("5 - Buscar um valor em uma coluna no DataSet")
        print("7 - Percentual de estudantes com Transtorno Mental")
        print("0 - Sair")

