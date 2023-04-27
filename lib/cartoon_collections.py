def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        num = dwarves.index(dwarf) + 1
        print(f"{num}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    # formatted_calls = []
    # for call in planeteer_calls:
    #     formatted_call = call.capitalize() + "!"
    #     formatted_calls.append(formatted_call)
    # return formatted_calls
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    for food in foods:
        if food == "cheddar":
            return food
        elif food == "gouda":
            return food
        elif food == "camembert":
            return food
    return None