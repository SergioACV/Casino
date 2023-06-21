import random

def create_tables():
    dictionaries = []

    for _ in range(2):
        dictionary = {}       

        values = random.sample(range(71), 25)

        for key, value in enumerate(values):
            dictionary[key] = value

        dictionaries.append(dictionary)

    values = random.sample(range(71), 71)

    return dictionaries, values

def add_tables():
    dictionary = {}       

    values = random.sample(range(71), 25)

    for key, value in enumerate(values):
        dictionary[key] = value
    
    return dictionary