from showDataset import ShowDataset
from anxietyGenderAnalysis import AnxietyGenderAnalysis
from depressionGenderAnalysis import DepressionGenderAnalysis
from optionFour import OptionFour

class Menu:
    def __init__(menu): ## Contrutor da classe Menu
        menu.options = {
            "1": ShowDataset(),
            "2": AnxietyGenderAnalysis(),
            "3": DepressionGenderAnalysis(),
            "4": OptionFour(),
            "0": None
        }

    def displayTitle():
        print("Aqui vai o Nome do Projeto")
    
    def displayMenu(menu): ## Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Mostar Dataset")
        print("2 - Mostrar Ansiedade por Gênero")
        print("3 - Mostrar Depressão por Gênero")
        print("4 - Funcionalidade 4")
        print("0 - Sair")

