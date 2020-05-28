value_list = [1, 10]
file = open("teste.txt", "r")

try:
    smiley = ":)"
    text = file.read()
    # div = 10/0
    # num = value_list[3]
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero")
except ArithmeticError:
    print("Houve algum erro em alguma operação aritmética")
except IndexError:
    print("Tentou-se acessar um índice inválido na lista")
except BaseException as err:
    print(err)
else:
    print("Nada de errado, continue programando")
finally:
    print("Eu sempre ocorro")
    file.close()