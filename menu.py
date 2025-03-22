from optionOne import OptionOne
from optionTwo import OptionTwo
from optionThree import OptionThree

class Menu:
    def __init__(menu): ## Contrutor da classe Menu
        menu.options = {
            "1": OptionOne(),
            "2": OptionTwo(),
            "3": OptionThree(),
            "0": None
        }

    def displayMenu(menu): ## Método para visualização do menu
        print("\nMenu de Opções:")
        print("1 - Executar funcionalidade 1")
        print("2 - Executar funcionalidade 2")
        print("3 - Executar funcionalidade 3")
        print("0 - Sair")

