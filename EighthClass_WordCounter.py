def wordCounter(word_list):
    counter = []
    for i in word_list:
        quantity = len(i)
        counter.append(quantity)
    return counter

if __name__ == '__main__':
    animals = ["Kitty", "Catty"]
    print(wordCounter(animals))