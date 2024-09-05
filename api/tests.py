import csv
from django.core.exceptions import ValidationError

class CSVFactory:
    @staticmethod
    def create(arquivo, encoding='ISO-8859-1', delimiter=';'):
        return CSVLeitor(arquivo, encoding, delimiter)

class CSVLeitor:
    def __init__(self, arquivo, encoding='ISO-8859-1', delimiter=';'):
        self.arquivo = arquivo
        self.encoding = encoding
        self.delimiter = delimiter

    def coluna(self, nome_coluna):
        datas = []
        try:
            with open(self.arquivo, mode='r', encoding=self.encoding) as file:
                next(file)  # Pula a primeira linha (cabeçalho)
                reader = csv.DictReader(file, delimiter=self.delimiter)
                for row in reader:
                    if nome_coluna not in row:
                        raise ValidationError(f"A coluna '{nome_coluna}' não localiza")
                    datas.append(row[nome_coluna])
        except FileNotFoundError:
            raise ValidationError(f"O arquivo '{self.arquivo}' não encontrado.")
        except ValidationError as e:
            raise e  
        except Exception as e:
            raise ValidationError(f"Ocorreu um erro inesperado: {e}")
        return datas
