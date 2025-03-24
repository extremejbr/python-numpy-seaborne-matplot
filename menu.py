from showDataset import ShowDataset
from anxietyGenderAnalysis import AnxietyGenderAnalysis
from optionThree import OptionThree

class Menu:
    def __init__(menu): ## Contrutor da classe Menu
        menu.options = {
            "1": ShowDataset(),
            "2": AnxietyGenderAnalysis(),
            "3": OptionThree(),
            "0": None
        }

    def displayTitle():
        print("Aqui vai o Nome do Projeto")
    
    def displayMenu(menu): ## Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Mostar Dataset")
        print("2 - Mostrar Ansiedade por Gênero")
        print("3 - Executar funcionalidade 3")
        print("0 - Sair")

