from SeventhClass_Television import Television
from SeventhClass_Calculator_A import Calculator
from EighthClass_WordCounter import wordCounter

if __name__ == '__main__':

    television = Television()
    print(television.on)

    television.power()
    print(television.on)

    calculator = Calculator(5, 10)
    print(calculator.sum())

    animals = ["Hedgehog", "Cat", "Chinchilla"]
    print(wordCounter(animals))