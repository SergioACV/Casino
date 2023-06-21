def create_list(list_dictionaries):
    new_list = [set(dictionary.values()) for dictionary in list_dictionaries]
    return new_list

def check_set(new_list, balls_list):
    for i in range(len(new_list)):
        if new_list[i].issubset(balls_list):
            return i
    return None