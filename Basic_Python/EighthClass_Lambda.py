word_counter = lambda item_list: [len(i) for i in item_list]

fruits = ["Caju", "Morango", "Melão", "Pêssego", "Pitaya"]
print(word_counter(fruits))

sum = lambda a, b: a + b
print(sum(5, 10))

calculator = {
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b
}
print(calculator['div'](10, 2))

soma = calculator['sum']
print(soma(5, 5))