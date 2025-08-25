import random
tributes = []
death_messages = [
    ' slipped on wet moss while running and snapped pronoun neck.',
    ' somehow died.'
    
    ]
def find_tribute(name):
    for tribute in tributes:
        if tribute["name"] == name:
            return tribute
        return None

def num_tributes(number):                                #tribute list
    for tribute in range(number):
        name = input('Tribute Name: ')
        tribute = {"name": "Kaitlyn", "gender": "f", "weapons": ["none", "none"], "health": "full", "place": "n/a", "items": ["none", "none"], "status": "alive",}
        
        tributes.append(tribute)
    return tributes

def select_death_message(tribute):
    tribute_name = find_tribute(tribute)
    tribute_name["status"] = "dead"
    if tribute_name["gender"] == "f":
        pronoun = "her"
    else:
        pronoun = "him"
    message = random.choice(death_messages)
    message = message.replace("their", pronoun)
    return tribute_name["name"] + message

def select_close_to_death_message(tribute):
    if tribute["name"] == tribute:
        None

def bloodbath():    
    for tribute in tributes:
        chance = random.randint(1, 4)
        if chance >= 3:
            tribute = tribute[tribute]["health"] = "none"
            tribute = tribute[tribute]["status"] = "dead"
            tributes.append(tribute)
            find_name = tribute[tribute]["name"]
            output_ = select_death_message(find_name) + output_ #here
                


  

#randomiser core engine
def game_one():
    None

number_of_tributes = int(input('Enter the number of tributes: ')) 

for tribute in tributes:
    if tribute["status"] == "alive":
        if tribute["place"] == "cornucopia":
            None#bloodbath code         ***blood bath effect/background screen***
        elif tribute["place"] == "volcano":
            None#find weapons code  different directions or no? different volcano stuff??
    else:
        None #remove from dict?
    
