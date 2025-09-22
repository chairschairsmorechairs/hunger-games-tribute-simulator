#import js document
#ask for name and gender
import random
import core_engine
tributes = []
def log_event(message: str): 
    #output_div = document.getElementById("output")
    #output_div.innerHTML += f"<p>{message}</p>"
    pass  # placeholder until you add code


#def user_info(): 
    #name = input('What is your full name? ')
    #gender = input('What is your gender (m/f)? ')
    #input name and gender
    #return name, gender  # return so other functions can use it

district_industries = {
    1: "Luxury goods",
    2: "Masonry / Military",
    3: "Technology",
    4: "Fishing",
    5: "Power and Electricity",
    6: "Transportation",
    7: "Lumber",
    8: "Textiles",
    9: "Grain",
    10: "Livestock",
    11: "Agriculture",
    12: "Coal",
}

def create_user(): 
    #randomly generate name, gender, age, skills, district, family, personality
    name = input('What is your full name? ')
    gender = input('What is your gender (m/f)? ')
    #choose district
    district = random.randint(1,12)
    #choose age (12-18)
    age = random.randint(12, 18)
    #choose skills
    if district in [1, 2, 4]:
            skill = random.choice(['agility', 'target practice', 'strength', 'adaptability', 'observation', 'fencing', 'agility'])
    else:
        skill = random.choice(['foraging', 'hunting', 'none', 'charisma', 'strength', 'adaptability', 'observation'])
    #choose family 
    family = random.randint(0, 2)
    if family == 0: 
        family = 'orphan'
    elif family == 1:
        family = random.choice(['mother', 'father'])
    elif family == 2:
        family = random.choices(['mother', 'father', 'brother', 'sister'], weights=[2, 2, 1, 1], k=2)
    #choose personality
    popularity = random.randint(20, 60)
    if district == 12 and skill != 'charisma':
        popularity -= 5
    #add other factors ***************************************************
    #choose money
    money = random.randint(0, 10)
    if district == 12:
        money -= 2
    if money < 0:
        money = 0
    return name, gender, district, age, skill, family, popularity, money
    
def reaping(name, gender, district, age, skill, family, popularity, money, year): 
    industry = district_industries[district].lower()
    if district == 12:
        capitol_rep = "Effie Trinket"
    else:
        capitol_rep = "a pink haired woman with an atrociously yellow pinafore"
    print('It is the day of the reaping.')
    if age == 12:
        print(f'You, {name}, are 12 years old. This is the first year you have had the "opportunity" to participate in the reaping.')
    else:
        print(f'You, {name}, are {age} years old. You have participated in the reaping before, but have never been chosen.')
    print(f'You belong to district {district}, known for its {industry}.')
    if district not in [1, 2, 4]:
            print('You know that your chances of being chosen are quite low, but you can\'t help but feel a little nervous this year.')
            print('Another house was burnt down this morning. It feels like a bad omen , especially on this day.' \
            'The Capitol is sending us a message./')
            print("As you leave the house, you look back. You can't help but feel like this time will be your last.")
            if family != "orphan":
                print(f'"Are you ready to go yet?" {family[0]} asks.')
                print("'Yeah, I guess so,' you reply.")
                print("And with that, you head to the town square.")
    print("It's already packed when you arrive, with people squeezed in like sardines.")
    print(f"As {capitol_rep} steps onto the stage, the crowd falls silent. She announces the {year}the Hunger Games once again.")
    print(f'The audience holds their breath as she pulls a name from the glass bowl.')
    print(f'"{name}. You have been selected to participate in the {year}th Hunger Games."')
    if int(popularity) < 30:
        print("The capitol representative smiles at you, but it's not a nice one. " \
        "Your father had a scandalous reputation, and it only occurs to you now that she may have been one of the victims.")
    elif int(popularity) >= 45:
        print("A murmur rises in the crowd.")
        print("Everyone looks at you in pity")
    if age < 14 and family != "orphan" and district != [1, 2, 4]:
        print(f"You clutch your {family[0]}'s hand, trying not to think about the future ahead.")
    else:
        print('You ball your hands into fists.')
        print('Clearly, the Capitol has it in for you. First your father, and now you.')
        print('A cold clear resolve begins to rise to the surface in your mind.')
    if district in [1, 2, 4]:
        rando = random_name(gender)
        print(f'You share a glance with {rando}, whose face contorts with anger.')
        print(f"Clearly, {find_pronoun_only(gender)} wasn't expecting you to be chosen.")
        print(f"{rando} scoffs, swiping a finger across their neck as if to say, “Dead already.”")
        print(f"You simply smirk back, confident in your ability.")
    elif district not in [1, 2, 4]:
        if "mother" in family or "sister" in family:
            print(f'You look back at your {family[0]}, who is crying silently.') #match to mother
        print("The crowd parts as you make your way to the stage. They don't voice it, but they're all glad they didn't get chosen instead.")
    print("You will survive, no matter the cost. " \
    "And if you can take some Capitol scum down with you, so be it.")

def find_pronoun_only(gender):
    if gender == "f":
        return "she"
    else:
        return "he"


def random_name(gender):
    #random first name
    if gender == "f":
        random_name = random.choice(['Alice', 'Beth', 'Cathy', 'Diana', 'Eva', 'Fiona', 'Grace', 'Hannah', 'Ivy', 'Jade', 'Kara', 'Luna', 'Mia', 'Nina', 'Olivia', 'Piper', 'Quinn', 'Riley', 'Sophie', 'Tina', 'Uma', 'Vera', 'Wendy', 'Xena', 'Yara', 'Zoe'])
    else:
        random_name = random.choice(['Alex', 'Ben', 'Chris', 'David', 'Evan', 'Frank', 'George', 'Harry', 'Ian', 'Jack', 'Kyle', 'Liam', 'Mike', 'Nate', 'Owen', 'Paul', 'Quinn', 'Ryan', 'Sam', 'Tom', 'Umar', 'Vince', 'Will', 'Xander', 'Yusuf', 'Zack'])
    return random_name

def create_tributes(): 
    global tributes  # use the global list
    tributes.clear()  # optional: clear existing tributes if rerunning

    for i in range(23):
        # generate a random name & gender
        gender = random.choice(['m', 'f'])
        name = random_name(gender)

        # district (1–12)
        district = random.randint(1, 12)

        # age (12–18)
        age = random.randint(12, 18)

        # skills
        if district in [1, 2, 4]:
            skill = random.choice(['agility', 'target practice', 'strength', 'adaptability', 'observation', 'fencing']) #k = 2
        else:
            skill = random.choice(['foraging', 'hunting', 'none', 'charisma', 'strength', 'adaptability', 'observation'])
        # family
        family = random.randint(0, 2)
        if family == 0:
            family = 'orphan'
        elif family == 1:
            family = random.choice(['mother', 'father'])
        elif family == 2:
            family = random.choices(['mother', 'father', 'brother', 'sister'], weights=[2, 2, 1, 1], k=2)

        # popularity
        popularity = random.randint(20, 60)
        if district == 12 and skill != 'charisma':
            popularity -= 5

        # money
        money = random.randint(0, 10)
        if district == 12:
            money -= 2
        if money < 0:
            money = 0

        # add tribute to global list
        tributes.append({
            "name": name,
            "gender": gender,
            "district": district,
            "age": age,
            "skill": skill,
            "family": family,
            "popularity": popularity,
            "money": money
        })

def train(district): #forcibly taken parameter
    if district in [1, 2, 4]:
        #print("luxurious train station")
        if district not in [1, 2, 4]:
            #print("You wake to the sound of the television blaring.") (only if forcibly taken)
            print("Your fellow tribute and you sit in silence for quite some time, watching the scenery, perhaps pondering your imminent doom...")
            print("You decide to break the silence. As if on cue, the television lights up, a gadget you have never seen before. At least, not at this size")
            print("The sound is too small and tinny for you to make out, but you turn to your district partner")
            print(f"In a fair impression of the weater presenter, you say 'Uhhh it's gonna be a little overcast in District 5 today, with some sunshine on the east side in District {district}.")
            print("A great day to do some starving or maybe catch up on your 'prepping to send your child to die' time!'")
            #
        #calculate rivlry chance 
        #attempt to ally query
        #chance of alliance
        alliance = random.randint(1, 4)
        return alliance
    else:
        #career alliance

        pass

def choose_designer():
    #change for district 12 and change chance of getting district 12
    designers = ["Cinna", "Portia", "Effie Trinket", "Tigris Snow", "Magno Stift"] # weight magno more, get some randoms.
    weights = [3, 2, 1, 1, 5]  # Example weights to favor certain designers
    designer = random.choices(designers, weights=weights, k=1)[0]#what is [0] for
    print(f'Your stylist is {designer}.')
    if designer == "Cinna":
        print("You feel a wave of relief wash over you. Cinna is known for his subtle defiance of the Capitol.")
        print("With him by your side, you might just have a chance.")# not relief, confusion
    elif designer == "Portia":
        print("Portia is known for her elegant and sophisticated designs.")
        print("She has a knack for making tributes look regal and poised.")
    elif designer == "Effie Trinket":
        print()

def randomise_designers():
    designers = ["Cinna", "Portia", "Proserpina Trinket", "Tigris Snow", "Magno Stift"] #fix*****************
    weights = [5, 3, 2, 2, 2, 1, 1, 1]  # Example weights to favor certain designers
    designer = random.choices(designers, weights=weights, k=1)[0]
    #tributes 
    return designer


def dying_chance(tribute, chance):
    roll = random.randint(1, 100)
    if roll <= chance:
        return True  # Tribute dies
    else:
        return False  # Tribute survives
inter.called = False
def intermission():
    choice = input("There is a chance you can improve your stats before the games beging. Begin? (y/n): ") 
    #BUTTON_ one of skills or something completely different (dancing), ask for aim ***************************
    if choice.lower() == 'y':
        if inter.called == False: #this means it can 
            inter.called = True

        print("You chose to improve your stats. This feature is under development.")
        pass
    pass
    inter.called = True
############################################
def choose_mentor(district): #find names for mentors
    mentors = { 
        1: ["Gloss", "Cashmere", "Augustus Braun"],
        2: ["Brutus", "Lyme", "Enobaria"],
        3: ["Beetee", "Wiress"],
        4: ["Mags Flanagan", "Finnick Odair", "Annie Cresta"],
        5: ["Porter Millicent Trip", "James Logan", "Nyra"], #james = alcoholic , nolan n Nyra = made up (nothing)
        6: ["n", "idk"], #morphlings
        7: ["Blight", "Johanna Mason"],
        8: ["Woof", "Cecelia"],  # cecelia is semi canon
        9: ["Nolan", "Sylva Mayleaf"], #unnamed male
        10: ["idkk", "idf"],
        11: ["Seeder", "Chaff"],
        # 12 handled separately
    }

    # Full victor pool
    all_victors = [
        "Haymitch Abernathy",
        "Beetee",
        "Wiress",
        "Mags Flanagan",
        "Chaff",
        "Seeder",
        "Cecelia",
        "Annie Cresta",
        "James Logan",
        "Nyra",
        "Porter Millicent Trip",
        "Augustus Braun",
        "Blight",
        "Woof",
        "Sylva Mayleaf",
        "Nolan", #unnamed district 9 victor
    ]

    # Matching weights (higher = more likely)
    weights = [
        10 if name == "Haymitch Abernathy" else 1  # Haymitch boosted
        for name in all_victors
    ]

    if district == 12:
        mentor = random.choices(all_victors, weights=weights, k=1)[0]
    elif district in mentors:
        mentor = random.choice(mentors[district])
    else:
        mentor = "nonexistent"  # fallback
    
    print(f"District {district}, your mentor is {mentor}.")
    
    return mentor

def kill_mentor(district):
    if district in [1, 2, 4]:
        return False, 0
    else:
        answer = input('Would you like to hatch a plot to secretly kill your mentor? (y/n): ')
        if answer.lower() == "y":
            chance = random.randint(1, 4)
            if chance == 1:
                return True, 1
            return True, 0


def training(kill_mentor, chance, mentor, popularity):
    #select 3 skills to train, 
    #randomly generate options
    #if kill_mentor = true
    #
    if kill_mentor == True:
        print(f"How would you like to attempt to kill your mentor, {mentor}?")
        #add options
    if popularity < 50:
        chance = random.randint(1, 3)
        if chance > 1:
            #success
            pass
        else:
            pass #fail
    #option 1 for day 1.



def first_game(): 
    year = random.randint(2000, 4000)
    name, gender, district, age, skill, family, popularity, money = create_user()
    reaping(name, gender, district, age, skill, family, popularity, money, year)
    create_tributes()
    #print(tributes) debug
    train(district)  #unfinished
    #print(train(district))
    #intermission
    #ask for designer? You are worried that you will get Magno Stift, who dresses the tributes in coal miner outfits every year.
    designer = choose_designer(gender) #unfinished
    randomise_designers() #unfinished
    #parade()
    mentor = choose_mentor(district) #use mentor
    rebellion_bool, success_chance = kill_mentor(district)

    #chance to kill mentor (you die) if not in 124. 75%
    training(rebellion_bool, success_chance, mentor, popularity) #in training, if popularity is low, chance of planting bombs 50% success rate; if success attempt to escape, 33% chance. intermission called in training too.
    performance() #
    ranking() #out of 24
    intermission() # call in
    #interviews!
    interview_choice() #choose image
    live_interview() #increase popularity, ask why they should be supported
    #final intermission (dinner) #poision someone else, 25% success rate. unlock secret path , rebel, lucy gray baird?**
    morning_chance() #breakfast, alliance last chance with district
    #start game
    #chance of type of arena
    #generate and describe location
    generate_arena()
    #choose run away or no, or grab item (choose which one), add clue (cornucopia)
    #bloodbath , work on FIGHT CODE, how much chance of fighting/alliance 
    #first night
    #chance of sponsor
    #day 2 (forage? chance of bumpong into someone, make fire? where shelter? chance of madness if kills > 3)
    #night 2 and feast, make something enticing for thing #if madness, see things. 75% chance of hallucination (new function later?)
    #sponsor definite
    # day 3 (while player = alive) if kills >3, hasn't followed hallucination, 50% chance of hallucination, else no more.
    #die function
    #win function and announce winner
    #play again? and stats

    #random events 
    #core_engine.select_death_message(), night msg, etc.
    #win = mentor
    #victoryparade()


#covey mode, backstory add way later; healer; escort(capitol)

#district 13 mode, survival or backstory









def main():
    first_game()