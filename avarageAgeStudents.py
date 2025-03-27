from utils import Utils


class AvarageAgeStudents:
    def execute(self):
        print("Executando funcionalidade 6...")

        # Carregar o dataset
        df = Utils.loadDataset('dataset/StudentMentalHealth.csv')

        # calcular a média
        average_age = df['Age'].mean()

        return f"A idade média dos estudantes é: {int(average_age)}"
