import pandas as pd

class Utils:
    @staticmethod
    def loadDataset(file_path):
        df = pd.read_csv(file_path)
        return df

