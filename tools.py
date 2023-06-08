def list_composer(*arrs):
    try :
        lists = []

        for arr in arrs:
            lists += arr

        return lists
    except :
        return "Incorrect data"





def decompose_dict(obj: dict) -> dict:
    for key , value in obj.items():
        print(key, value)
    




def show_list_items(arr : list, cb=None):
    if type(arr) == list:

        for index, list_item in enumerate(arr):
            if cb:
                print("_______________")
                print(index)
                new_dict = cb(list_item)
            else:
                print(list_item)




def money_check(condition):
    if not condition:
        return False
    
    return True



def confirm(quest:str) -> bool:
    answer = input(quest)

    if answer.lower() == "n":
        return False

    return True