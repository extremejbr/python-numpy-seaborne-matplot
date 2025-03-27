from menu import Menu

class Main():

    def run(menu): ## Método de inínio da aplicação
            Menu.displayTitle()
            while True:
                Menu.displayMenu(menu)
                choice = input("Escolha uma opção: ")
                
                if choice == "0":
                    print("Saindo do programa...")
                    break
                
                option = menu.options.get(choice)
                if option:
                    result = option.execute()
                    print(result)
                else:
                    print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu = Menu()
    Main.run(menu)




