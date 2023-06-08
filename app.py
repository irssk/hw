# HW

# Our restaurant also has a menu and staff

# It's (programm) should start with greeting from staff ("Julia , Aida , Sam (not manualy) ... glad to see you here .") , then it's send a request to =>
# John.

# After -> John may ask about menu , or go away
# if "go away"  ->  then programm send msg -> Are you sure about this ? if y/n -> y -> game over
# n -> turn back to : John may ask about menu , or go away
# if "stay here" -> John should get a menu and then if he has money he might to buy something . (search by name)
# if John hasn't any money he should "go away" but before he must to pay his bill (bill + comission)
# John might order so much food as he want (money!)

from tools import confirm , list_composer , decompose_dict , show_list_items , money_check

CONFIRM_MESSAGE = "Are you sure about this ? y/n"

menu = {
    "dishes": [
        {"name": "Karbonara", "price": 240},
        {"name": "Pizza", "price": 300},
        {"name": "Pasta", "price": 200},
        {"name": "Salamy white", "price": 500},
    ],

    "drinks": [
        {"name": "Wine", "price": 40},
        {"name": "Cola", "price": 30},
        {"name": "7up", "price": 45},
        {"name": "Fanta", "price": 50},
    ],
}

waitress = [
    {
        "name": "Julia",
        "tips": "10%"
    },

    {
        "name": "Aida",
        "tips": "12%"
    },

    {
        "name": "transSam",
        "tips": "14%"
    },

    {
        "name": "Gaga",
        "tips": "24%"
    },
]

john = {
    "name": "John",
    "money": 500
}

def sum_with_comission(sum:int , persent:int) -> float:
    return sum + (sum / 100 * persent)


def greeting(arr: list):
    print("Hi , there ! FROM : ")
    show_list_items(arr , decompose_dict)
    print("--------------------")

def refreshed_walled(obj:dict , dish:int):
    return obj["money"] - dish


def pick(choose : str, food:list):

    match(input(choose)):
        case "1":
            
            show_list_items(food, decompose_dict)

            chosen_food = int(input(
                "Enter number of dish that you wanna order : \n"))
            
            if type(chosen_food) != int:
                raise ValueError("Incorrect data")
            
            return food[chosen_food]
            
        case "2":
            is_stay = confirm(CONFIRM_MESSAGE)

            if is_stay == False : 
                return "Goodbye"
            
        case _ :
            print("Something went wrong")
        
def main():
    greeting(waitress)

    food = list_composer(
        menu["dishes"] , menu["drinks"])

    picked_dish = pick("1) Menu 2) Quit \n" , food)

    whole_sum = (sum_with_comission(picked_dish['price'], 15))

    is_available = money_check(john['money'] >= whole_sum)

    print(is_available)
    if not is_available : 
        return "Something went wrong"
    print(john)

    john["money"] = refreshed_walled(john, whole_sum)

    print(john)


if __name__ == "__main__" :
    main()