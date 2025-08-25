import random
print('Welcome to the Hunger Games Tribute Simulator!')
tributes = []
death_messages = [
    ' slipped on wet moss while running and snapped pronoun neck.',
    ' somehow died.',
    ' died mysteriously.',
    ' fell out of a tree trying to spy on person.',
    ' drank carelessly from a stream without checking, started flailing for a minute or so, and died.'
    ' burned pronoun_self to death while trying to start a campfire as the gasoline exploded in their face.',
    ' tried to climb a tree with a bow in their mouth and promptly choked to death.',
    ' got crushed under a parachute drop from District number they were too excited to catch.',
    ' has a drink with name_2 and poisons the drink but forgets which one pronoun poisoned.',
    ' fell asleep in 6 7 foot tall grass and got trampled by mutts.',
    ' died after being too skibidi.'
    ' was killed by a convienient Lebron James holding an axe.'
    ' lost all pronoun aura. '
    ]
#find tribute from their name (no strings involved)
def find_tribute(name):
    for tribute in tributes:
        if tribute["name"] == name:
            return tribute
        return None

# get the number of tributes at the beginning
def num_tributes(number):                                #tribute list
    for tribute in range(number):
        name = input('Tribute Name: ')
        tribute = {"name": "Kaitlyn", "gender": "f", "weapons": ["none", "none"], "health": "full", "place": "n/a", "items": ["none", "none"], "status": "alive",}
        
        tributes.append(tribute)
    return tributes

#randomly select death message (and variables)
def select_death_message(tribute):
    tribute_name = find_tribute(tribute)
    tribute_name["status"] = "dead"
    if tribute_name["gender"] == "f":
        pronoun = "her"
    else:
        pronoun = "him"
    message = random.choice(death_messages)
    if "pronoun" in message:
        message = message.replace("pronoun", pronoun)
    elif "pronoun_self" in message:
        pronoun = pronoun + "self"
        message= message.replace("pronoun_self", pronoun)
    elif "name_2" in message:
        name_2 = random.choice(tributes)
        while name_2["name"] == tribute_name["name"]:
            name_2 = random.choice(tributes)
        message = message.replace("name_2", name_2["name"]) #check this
    elif "number" in message:
        number = random.randint(1, 12)
        message = message.replace("number", str(number))
    return tribute_name["name"] + message

#selects close to death message
def select_close_to_death_message(tribute):
    if tribute["name"] == tribute:
        None

#opening function bloodbath: how many should die?
def bloodbath():    
    for tribute in tributes:
        chance = random.randint(1, 4)
        if chance >= 3:
            tribute = tribute[tribute]["health"] = "none"
            tribute = tribute[tribute]["status"] = "dead"
            tributes.append(tribute)
            find_name = tribute[tribute]["name"]
            output_ = select_death_message(find_name) + output_ #here
                

#randomiser core engine, place all code in here later
def game_one():
    None

#first user input** check pyscript
number_of_tributes = int(input('Enter the number of tributes: ')) 

#decides if the tribute goes to cornucopia or runs away
for tribute in tributes:
    None #here do stuff wher i left off

#checks if the tribute is alive and location.
for tribute in tributes:
    if tribute["status"] == "alive":
        if tribute["place"] == "cornucopia":
            None#bloodbath code         ***blood bath effect/background screen***
        elif tribute["place"] == "volcano":
            None# find weapons code different directions or no? different volcano stuff??
    else:
        None # how to remove from dict? 
    
