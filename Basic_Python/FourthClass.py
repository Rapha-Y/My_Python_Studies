# a = int(input("Entre com o número: "))
# div = 0
# for x in range(1, a + 1):
#     rest = a % x
#     print(a, rest)
#     if rest == 0:
#         div += 1
#
# if div == 2:
#     print("Número {} é primo".format(a))
# else:
#     print("Númer {} não é primo".format(a))

# a = int(input("Pucci, entre com um valor: "))
# for i in range(a+1):
#     div = 0
#     for x in range(1, i+1):
#         rest = i % x
#         if rest == 0:
#             div += 1
#     if div == 2:
#         print(i)

# nota = int(input("Entre com a nota: "))
# while nota > 10:
#     nota = int(input("Entre com a nota: "))

a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input("Nota inválida. Primeiro bimestre: "))
b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input("Nota inválida. Segundo bimestre: "))
c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input("Nota inválida. Terceiro bimestre: "))
d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input("Nota inválida. Quarto bimestre: "))
mean = (a + b + c + d) / 4
print("Média: {}".format(mean))