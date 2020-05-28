class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10: "))
        if x > 10:
            raise InputError("Valor inválido, notas devem ser menores ou iguais a 10")
        elif x < 0:
            raise InputError("Valor inválido, notas devem ser maiores ou iguais a 0")
        break
    except ValueError:
        print("Valor inválido, apenas números são aceitos")
    except InputError as err:
        print(err)