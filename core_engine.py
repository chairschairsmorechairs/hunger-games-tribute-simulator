import random

print('Welcome to the Hunger Games Tribute Simulator!')
tributes = [] # do i need this?
death_messages = [
    ' slipped on wet moss while running and snapped pronoun neck.',
    ' somehow died. name_2 is spotted in the distance.',
    ' died mysteriously.',
    ' fell out of a tree trying to spy on name_2.',
    ' drank carelessly from a stream without checking, started flailing for a minute or so, and died.'
    ' burned pronoun_self to death while trying to start a campfire as the gasoline exploded in their face.',
    ' tried to climb a tree with a bow in their mouth and promptly choked to death.', #this too..
    ' got crushed under a parachute drop from District number they were too excited to catch.', #idk about thiss
    ' has a drink with name_2 and poisons the drink but forgets which one pronoun poisoned.',
    ' fell asleep in 6 7 foot tall grass and got trampled by mutts.',
    ' died after being too skibidi.',
    ' was killed by a convienient Lebron James holding an axe.',
    ' caused name_2 to lose all their aura, effectively killing pronoun. ', #idk bout this one
    ' died in shock after losing the huzz.', #alliance?
    ' tried to battle name_2 and failed miserably, only managing to splatter a single item on them before dying.', #replace item
    ' became allergic to the air and died.',
    ' literally just died.',
    ' died from looking at name_2, who was too chopped to look at.', # meaning?
    ' was killed when a coconut dropped on their head.',
    ' ate too much sand and perished.',
    ' was stung bay wasps', #finish this sentence
    ' was eaten alive by name_2',
    
    ]

#night messages etc
night_messages = [
    ' found a convenient log to sleep in decision', 
    ' kept watch all night. Paranoid much?',
    ' sees a campfire in the horizon decision', #add more options, not done
    ' sleeps in a tree.',
    ' hears a sound in the night decision', #not done
    ' found a square hole in the ground and decision', #not done' #group similar ones?
    ' hears voices in the night which tells them to action decision', #they are crazy. insert action
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
    #add falling out of a tree? or no?
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
    ' saw name_2 was following them and fired an arrow at them, verdict',
    ' jumped out of a bush and attacked name_2, verdict', # add more; not done
    ]

cornucopia_messages = [
	' decides to quickly run to the cornucopia and grab and item outside', # just do random chance of this??
	' decides to avoid the cornucopia and hides in the forest.',
	' decides to risk it and grab the weapon from the heart of the cornucopia, decision', #add decision and chance of death'
    ' fights name_2 over a machete in the cornucopia, verdict', #add more
]

USE_BROWSER = False  # change this to True when using PyScript

if USE_BROWSER:
    from js import document
    def log_event(message: str):
        output_div = document.getElementById("game-output")
        output_div.innerHTML += message + "<br>"
        output_div.scrollTop = output_div.scrollHeight
else:
    def log_event(message: str):
        print(message)


#find tribute from their name (no strings involved)
def find_tribute(name):
    for tribute in tributes:
        if tribute["name"] == name:
            return tribute
        
def add_kills_and_find(tribute):
    tribute["kills"] += 1
    return tribute["kills"]

# get the number of tributes at the beginning
def num_tributes(number):                                #tribute list
    for tribute in range(number):
        name = input('Tribute Name: ') #fix inputs

        tribute = {"name": name, "gender": "f", "weapons": ["none", "none"], "health": "full", "place": "n/a", "items": ["none", "none"], "status": "alive", "kills": 0,}
        
        tributes.append(tribute)
    return tributes

#randomly select death message (and variables)
def select_death_message(tribute):
    tribute_name = find_tribute(tribute)
    tribute_name["status"] = "dead"
    message = random.choice(death_messages)
    output = find_pronoun(tribute_name, message)
    log_event(output)
    return output

#finds pronoun and replaces variables
def find_pronoun(tribute, message):# resolve other inputs
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
        add_kills_and_find(name_2["name"])
        message = message.replace("name_2", name_2["name"]) #check this
    elif "number" in message:
        number = random.randint(1, 12)
        message = message.replace("number", str(number))
    elif "decision" in message:
        if message == night_messages[0]:
            decision = random.choice(['but decided it was too dangerous and ran away.', 'and slept peacefully until they realised they were stuck inside like Winnie the Pooh.'])
        elif message == near_death_messages[1]:
            decision = random.choice(['and decided to keep them for later', ''])
        elif message == night_messages[2]:
            chance = random.randint(1, 4)
            if chance >= 3:
                decision = 'but decided to ignore it and go back to sleep.'
            elif chance == 2:
                decision = 'and decided to investigate, but by the time they reached the site, it was nothing.'
            else:
                name_2 = random.choice(tributes)
                while name_2["name"] == tribute["name"]:
                    name_2 = random.choice(tributes)
                decision = 'and decided to investigate, finding' + name_2["name"] + 's camp.' #add alliance or death instantly
        message = message.replace("decision", decision)
    return tribute["name"] + message

def select_cornucopia_msg(tribute):
    tribute_name = find_tribute(tribute)
    message = random.choice(cornucopia_messages)
    output = find_pronoun(tribute, message)
    log_event(output)
    return output

#chooses a night message randomly
def select_night_message(tribute):
    tribute_name = find_tribute(tribute)
    message = random.choice(night_messages)
    output = find_pronoun(tribute_name, message)
    log_event(output)
    #return output



#selects close to death message
def select_close_to_death_message(tribute):
    if tribute["name"] == tribute:
         #add more code
        message = random.choice(near_death_messages)
        output = find_pronoun(tribute, message)
        log_event(output)

#opening function bloodbath: how many should die?
def bloodbath():
    #trigger bloodbath effect + screen
    for tribute in tributes:
        if tribute["status"] == "alive" and tribute["place"] == "cornucopia": # or tribute running away
            chance = random.randint(1, 4)
            if chance >= 3:
                tribute["health"] = "none"
                tribute["status"] = "dead"
                message = select_death_message(tribute["name"])
                
            else:
                tribute = find_tribute(tribute["name"])
                message = select_cornucopia_msg(tribute) # add func, could find weapons
                # TODO: output to HTML instead of print
                log_event(message)
                #print(message)

# remove from dict
def remove_tribute_and_cannons(tribute):
    dead_names = []
    for tribute in dead_names:
        tributes = [t for t in tributes if t["name"] != tribute["name"]] #do i need this

#first user input** check pyscript
number_of_tributes = int(input('Enter the number of tributes: ')) #change input, move to bottom !!!!!!!!!!!

#decides if the tribute goes to cornucopia or runs away
def choose_location():
    for tribute in tributes:
        None #here do stuff where i left off
        chance = random.randint(2, 6)
        if chance >= 4:
            tribute["place"] = "the cornucopia" 
        elif chance == 3:
            tribute["place"] = "higher ground" #tribute is leaving to go to high ground. "the forest but plans to go to higher ground"
        elif chance == 2:
            tribute["place"] = "the rock face to scale the mountain"
            #chance of falling off and dying
        else:
            tribute["place"] = "the forest" #add more places??
            #print the messages - all of them - have i?
        log_event(f"{tribute['name']} decides to head to {tribute['place']}.")

#checks if the tribute is alive and location.



def action():
    for tribute in tributes:
        if tribute["status"] == "alive":
            chance = random.randint(1, 10)
            if chance >= 8:
                alive_ness = random.randint(1, 2)
                if alive_ness == 2: 
                    tribute["status"] = "dead"
                    tribute["health"] = "none"
                    message = select_death_message(tribute["name"])
                    log_event(message)
                #fight code/die
                #link to death_messages
                #add kills
                #add

            elif chance >= 6:
                None #find item code

            elif chance == 5:
                pass #food ?
            elif chance == 2:
                None #find weapon code
            else:
                None #do nothing code
        else:
            None #remove from dict? unless done previously


#first day function (bloodbath,)
def day_one():
    None #yet
    choose_location() #reverse cornucopia, make them find items as well
    bloodbath()
    action()
    #food? 



def day_miscellaneous():
    choose_location() #not cornucopia
    action()

    None #yet

def night():
    None #yet
    #call night messages
    for tribute in tributes:
        if tribute["status"] == "alive":
            message = select_night_message(tribute["name"])
            #output message to html
    #input "click to proceed", fix
        #find winner
    #use this -> number_of_shots can be heard in the distance. The following tributes have fallen:
    #cannon shots fired DO THIS
    #list dead tributes

def one_left():
    alive_count = sum(1 for tribute in tributes if tribute["status"] == "alive")
    return alive_count <= 1

def find_winner():
    for tribute in tributes:
        if tribute["status"] == "alive":
            winner_message = f"{tribute['name']} is the winner of the Hunger Games!"
            
            # put message into a <div> with id="game-output"
            output_div = document.getElementById("game-output")
            output_div.innerText = winner_message
            log_event(winner_message)
            return tribute["name"]
        
#randomiser core engine, place all code in here later
def one_game():
    day_one()
    while not one_left():
        night()
        day_miscellaneous()
    winner = find_winner()
    log_event(f"{winner} is the winner of the Hunger Games!")
    
    

#one_game()
#option to repeat()

output_div = document.getElementById("test_output")
output_div.innerText = "Testing testing 123"
