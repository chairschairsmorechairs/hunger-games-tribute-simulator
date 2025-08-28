import random
from pyscript import Element #investigate why this isnt working and how to actually output to html

print('Welcome to the Hunger Games Tribute Simulator!')
tributes = [] # do i need this?
death_messages = [
    ' slipped on wet moss while running and snapped pronoun neck.',
    ' somehow died. name_2 is spotted in the distance.',
    ' died mysteriously.',
    ' fell out of a tree trying to spy on name_2.',
    ' drank carelessly from a stream without checking, started flailing for a minute or so, and died.'
    ' burned pronoun_self to death while trying to start a campfire as the gasoline exploded in their face.',
    ' tried to climb a tree with a bow in their mouth and promptly choked to death.',
    ' got crushed under a parachute drop from District number they were too excited to catch.',
    ' has a drink with name_2 and poisons the drink but forgets which one pronoun poisoned.',
    ' fell asleep in 6 7 foot tall grass and got trampled by mutts.',
    ' died after being too skibidi.',
    ' was killed by a convienient Lebron James holding an axe.',
    ' lost all pronoun aura. ', #idk bout this one
    ' died in shock after losing the huzz.',
    ' tried to battle name_2 and failed miserably, only managing to splatter a single item on them before dying.', #replace item
    ' became allergic to the air and died.',
    ' literally just died.',
    ' died from looking at name_2, who was chopped.' # meaning?

    ]

#night messages etc
night_messages = [
    ' found a convenient log to sleep in decision', 
    ' kept watch all night. Paranoid much?',
    ' sees a campfire in the horizon decision', #add more options, not done
    ' sleeps in a tree.',
    ' hears a sound in the night decision', #not done
    ' found a square hole in the ground and decision', #not done' #group similar ones?
]

#alliance messages, add more, run chance, what is the chance they get an alliance
alliance_messages = [
	' formed an alliance with name_2.',
	' asked to form an alliance with name_2, but was declined and lost aura.',
	' agreed to ally with name_2, even though pronoun_2 was crazy.', #add pronoun 2, add 2 decisions.
]

#do i need this?
near_death_messages = [
    ' was almost run over by a stray Pinnochio but escaped by a hair.',
    ' found poisonous berries, decision.'
]

#not even half done
it_was_coming_death_messages = [ #can i add this to death messages?
    ' was killed by poisonous berries.',
    ' impaled pronoun on weapon' #in their possession
    ' was betrayed by name_2 and killed under the cover of darkness.',
    ' , out of desperation, took a bite out of name_2, and ran away.', #only if they had an alliance
]

#chances they fight etc
fight_messages = [
    ' started beefing with name_2 over a cob of corn verdict',
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
        tribute = {"name": "Kaitlyn", "gender": "f", "weapons": ["none", "none"], "health": "full", "place": "n/a", "items": ["none", "none"], "status": "alive", "kills": "0",}
        
        tributes.append(tribute)
    return tributes

#randomly select death message (and variables)
def select_death_message(tribute):
    tribute_name = find_tribute(tribute)
    tribute_name["status"] = "dead"
    message = random.choice(death_messages)
    output = find_pronoun(tribute_name, message)
    return output

#finds pronoun and replaces variables
def find_pronoun(tribute, message):
    if tribute["gender"] == "f":                       
        pronoun = "her"
    else:
        pronoun = "him"
    if "pronoun" in message:
        message = message.replace("pronoun", pronoun)
    elif "pronoun_self" in message:
        pronoun = pronoun + "self"
        message= message.replace("pronoun_self", pronoun)
    elif "name_2" in message:
        name_2 = random.choice(tributes)
        while name_2["name"] == tribute["name"]:
            name_2 = random.choice(tributes)
        message = message.replace("name_2", name_2["name"]) #check this
    elif "number" in message:
        number = random.randint(1, 12)
        message = message.replace("number", str(number))
    elif "decision" in message:
        if message == night_messages[0]:
            decision = random.choice(['but decided it was too dangerous and ran away.', 'and slept peacefully until they realised they were stuck inside like Winnie the Pooh.'])
        elif message == near_death_messages[1]:
            decision = random.choice(['and decided to keep them for later', ''])
        message = message.replace("decision", decision)
    return tribute["name"] + message

#chooses a night message randomly
def select_night_message(tribute):
    tribute_name = find_tribute(tribute)
    tribute_name["status"] = "injured"
    message = random.choice(night_messages)
    output = find_pronoun(tribute_name, message)
    

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
            tributes.append(tribute) # not sure about this
            find_name = tribute[tribute]["name"]
            output_ = select_death_message(find_name) + output_ #here
# remove from dict
                



#first user input** check pyscript
number_of_tributes = int(input('Enter the number of tributes: ')) #change input

#decides if the tribute goes to cornucopia or runs away
def choose_location():
    for tribute in tributes:
        None #here do stuff where i left off
        chance = random.randint(2, 6)
        if chance >= 4:
            tribute["place"] = "cornucopia" 
        else:
            tribute["place"] = "volcano" #add more places??

#checks if the tribute is alive and location.
def bloodbath():                            #call after choose location !!!! very important!!! 
    for tribute in tributes:
        if tribute["status"] == "alive":
            if tribute["place"] == "cornucopia":
                None#bloodbath code         ***blood bath effect/background screen***
            elif tribute["place"] == "volcano":
                None# find weapons code different directions or no? different volcano stuff??
        else:
            None # how to remove from dict? 

def day_one():
    None #yet
    choose_location() #reverse cornucopia, make them find items as well
    bloodbath()
    #food? 



def day_miscellaneous():
    choose_location() #not cornucopia

    None #yet

def night():
    None #yet
    #night messages
    winner_yet_query = one_left()   
    if winner_yet_query == True:
        for tribute in tributes:
            if tribute["status"] == "alive":
                return tribute["name"]  + "is the champion of the 2025 Hunger Games!" #display this!!1
    else:
        return False #input "click to proceed", fix
        #find winner
    #use this -> number_of_shots can be heard in the distance. The following tributes have fallen:
    #cannon shots fired DO THIS
    #list dead tributes

def one_left():
    for tribute in tributes:
        if tribute["status"] == "alive":
            return False 
        else:
            return True

def find_winner():
    for tribute in tributes:
        if tribute["status"] == "alive":
            print(tribute["name"] + " is the winner of the Hunger Games!")
            return tribute["name"]

#randomiser core engine, place all code in here later
def one_game():
    day_one()
    while one_left() == False: #can i put brackets here? check this please
        None #day/night cycle
        night()
        day_miscellaneous()
        one_left()
    print('Would you like to play again?') # make a button
    #fix this and complete cycle
    
    

#one_game()

output_div = Element.querySelector('#test_output') #check if this works
output_div.innerHTML = "Testing testing 123" #check if this works
