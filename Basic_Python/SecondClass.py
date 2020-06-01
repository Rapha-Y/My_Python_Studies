a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
sum = a + b
sub = a - b
mul = a * b
div = a / b
res = a % b
print("Soma: " + str(sum))
print("Subtração: {minus}\nMultiplicação: {ex}".format(minus=sub, ex=mul))
print("Divisão truncada:", int(div))
print("Resto:", res)