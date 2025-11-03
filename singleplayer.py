#import js document
#ask for name and gender
import random
import sys
import core_engine
from pyscript import document
"""app = Flask(__name__)
@app.route('/')


if __name__ == '__main__': 
    app.run(debug=True)
    def hello():
        return 'hello'
    hello()
"""

tributes = []
death_messages = [ #fix grammar???
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
def log_event(message: str): 
    #output_div = document.getElementById("output")
    #output_div.innerHTML += f"<p>{message}</p>"
    pass  # placeholder until you add code

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
    12: "Coal Production",
}

def create_user(): 
    #randomly generate name, gender, age, skills, district, family, personality, determination
    while True:
        name = input('What is your full name? ')
        if len(name) >= 3:
            break
        print("Name must be at least 3 characters long.")

        # Get valid gender
    while True:
        gender = input('What is your gender (m/f)? ').lower()
        if gender in ['m', 'f']:
            break
        print("Please enter 'm' or 'f'.")

        print(f"User created: {name} ({'Male' if gender == 'm' else 'Female'})")
    determination = 0
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
        family = ["orphan"]
    elif family == 1:
        family = [random.choice(["mother", "father", "sibling"])]
    elif family == 2:
        family = random.choices(["mother", "father", "sibling"], k=2)
    #choose personality
    popularity = random.randint(20, 60)
    if district == 12 and skill != 'charisma':
        popularity -= 5
    determination = determination + 15
    if district in [1, 2, 4]:
        determination += 15 #career tributes are motivated
    elif district in [11, 12]:
        determination += 25 #poor districts are motivated but there's a chance they aren't
    #add other factors ***************************************************
    #choose money
    money = random.randint(0, 10)
    if district == 12:
        money -= 2
    if money < 0:
        money = 0
    return name, gender, district, age, skill, family, popularity, money, determination
    
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
    print(f'You belong to district {district}, known for its {industry.lower()}.')
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
    if age < 14 and family != "orphan" and district not in [1, 2, 4]:
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
    return

def find_pronoun_only(gender):
    if gender == "f":
        return "she"
    else:
        return "he"


def random_name(gender): #edit names
    #random first name
    if gender == "f":
        random_name = random.choice(['Alice', 'Beth', 'Cathy', 'Diana', 'Eva', 'Fiona', 'Grace', 'Hannah', 'Ivy', 'Jade', 'Kara', 'Luna', 'Mia', 'Nina', 'Olivia', 'Piper', 'Quinn', 'Riley', 'Sophie', 'Tina', 'Uma', 'Vera', 'Wendy', 'Xena', 'Yara', 'Zoe'])
    else:
        random_name = random.choice(['Alex', 'Ben', 'Chris', 'David', 'Evan', 'Frank', 'George', 'Harry', 'Ian', 'Jack', 'Kyle', 'Liam', 'Mike', 'Nate', 'Owen', 'Paul', 'Quinn', 'Ryan', 'Sam', 'Tom', 'Umar', 'Vince', 'Will', 'Xander', 'Yusuf', 'Zack'])
    return random_name

def create_tributes(number, district): #edit to make 2 for each district
    global tributes  # use the global list
    tributes.clear()  # optional: clear existing tributes if rerunning

    for i in range(number):
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

def ask_for_designer(popularity, determination):
    ask_true = input("Would you like to request for a designer (y/n): ")
    if district == 12:
        print("You are worried that you will get Magno Stift, who dresses the tributes in coal miner outfits every year.")
    if ask_true == "y":
        chance = randint(1, 3)
        if chance > 1:
            #yes
            designer = input("Which designer would you like to request for? Cinna, Portia, Prosperpina Trinket, Tigris Snow, or Magno Stift: ")
            designer = designer.lower()
            if designer not in ["cinna", "portia", "prosperpina trinket", "tigris nnow", "magno Stift"]:
                print("'That's not a designer I've heard of...' The lady looks at you in confusion. Very well...")
                print("You've failed to ask for a designer.")
                return False
            return designer
        else:
            #no
            print("You knock on the door of the office. Your feet wobble from the unsteady ground of the train.")
            print("The door is ajar. You swing it open slightly, and CRASH!")
            print("In comedic timing, a bucket of water tips over and lands on you.")
            print("'That was quite amusing...' The lady snickers. She won't listen to your request - you've humiliated yourself too much. Frustrated, you stomp away back to the common area to complain.")
            determination = determination + 5
            popularity = popularity - 5
            return False, popularity, determination


    

def choose_designer(district, designer_chosen): #unfinished
    while designer_chosen == False:
        #change for district 12 and change chance of getting district 12
        weights = [2, 1, 3, 2, 0]
        designers = ["Cinna", "Portia", "Prosperpina Trinket", "Tigris Snow", "Magno Stift"] # weight magno more, get some randoms.
        # Example weights to favor certain designers
        if district == 12:
            weights = [3, 2, 1, 1, 5]
        designer = random.choices(designers, weights=weights, k=1)[0]#what is [0] for
        print(f'Your stylist is {designer}.')
        if designer == "Cinna":
            print("You shake your head in confuseion - You've never heard of that name before.")
            print("You have a feeling that Cinna will create something you've never seen before. But he's a newbie, and that itself has its risks...")# not relief, confusion
            #rebellion
        elif designer == "Portia":
            print("Portia is known for her elegant and sophisticated designs.")
            print("She has a knack for making tributes look regal and poised.")
        elif designer == "Proserpina Trinket":
            print("Proserpina Trinket, a former capitol representative, is your stylist.")
            print("She is known for her flamboyant and extravagant fashion sense; a bit extreme a times.")
        elif designer == "Tigris Snow":
            print("Tigris is performative, and is attracted to the allure of the Capitol. Perhaps not the best stylist, but being related to the President, she may have some insider information...")
            print("You file this into your memory as information for later")
            #rebellion FIX THIS
        else: #magno
            print("Your heart sinks. Coal miner outfits it shall be, you suppose.")
        return designer
    if designer_chosen == "cinna":
        designer_chosen = "Cinna"
    elif designer_chosen == "portia":
        designer_chosen = "Portia"
    elif designer_chosen == "proserpina":
        designer_chosen = "Proserpina"
    elif designer_chosen == "tigris snow":
        designer_chosen = "Tigris Snow"
    else:
        designer_chosen =="Magno Stift"
    return designer_chosen

def randomise_designers(district, tributes_global_list, number_tributes): #unfinished
    designers = ["Cinna", "Portia", "Proserpina Trinket", "Tigris Snow", "Magno Stift"] #fix*****************
    if district == 12:
        weights = [1, 1, 1, 1, 5]  # Heavily favor Magno Stift for District 12
    else:
        weights = [5, 3, 2, 2, 2, 1, 1, 1]  # Example weights to favor certain designers
    for i in range(number): #tributes 
        designer = random.choices(designers, weights=weights, k=1)[0]

    return tributes_list #check


def dying_chance(tribute, chance):
    roll = random.randint(1, 100)
    if roll <= chance:
        return True  # Tribute dies
    else:
        return False  # Tribute survives
    #inter.called = False #the heck is inter.called?
def intermission():
    choice = input("There is a chance you can improve your stats before the games beging. Begin? (y/n): ") 
    #BUTTON_ one of skills or something completely different (dancing), ask for aim ***************************
    if choice.lower() == 'y':
        print("You chose to improve your stats. This feature is under development.")
        pass
    pass
    #inter.called = True
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
        10: ["idkk", "idf"], #remove
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
        else:
            return False, 0


def training(kill_mentor, chance, mentor, popularity, district):
    #select 3 skills to train, 
    skills_list = ["Target practice", "Archery", "Electricity generation", "Spear crafting", "Foraging", "Swordfighting", "Camouflage", "Water sourcing and sanitation", "Traps and tricks"]
    #randomly generate options
    if kill_mentor == True:
        print(f"How would you like to attempt to kill your mentor, {mentor}?")
        number = input("1. Poison; 2. Ambush Quietly; 3. Stage an Accident; 4. Strangle in the open. Enter the number of your choice: ")
        if number == 1:
            print(f'You decide to poison {mentor}\'s bean soup at dinner.')
            print("You sneak into the kitchen, and spy the pot of boiling soup. You know it will be for your mentor, as it is much too fancy for any tribute to consume.")
            if chance == 1: #chance from kill_mentor function
                print("As you push past, you subtly tip the clear vial of poison into the pot.")
                print("The poison seeps into the liquid, unnoticed...")
                print(f"Later that day, you are informed that {mentor} has fallen ill and died without cause.")
                print('Holidng in a smile, you feel a sense of pride at this accomplishment.')
                print("It's your way of rebelling against the Capitol.")
                print("Little do you know, the Gamemakers will be keeping an eye on you now...")
                #intelligence -= 5
                #rebellion
                popularity += 10
            else:
                print(f'You decide to poison {mentor}\'s water immediately.')
                print("You sneak into the common area, where your mentor is sitting alone, reading a book.")
                print("You silently slip the vial of poison into their water bottle.")
                print(f"Suddenly, {mentor} looks up, eyes narrowing in suspicion.")
                print("You've been caught red handed. Frozen, you can only watch as they pluck the waterbottle out of your hands.")
                print("The smell of poison is unmistakable, from their look of disgust.")
                print("They sigh. 'Cyanide', they mutter, before turning around. 'Peacekeepers!' they shout.")
                print("Game Over!")
                sys.exit() #ending
        elif number == 2:  
            print(f'You decide to ambush {mentor} quietly during training.')    
            if chance == 1: #success
                print("You wait until your mentor is alone, practicing archery.")
                print("Silently, you creep up behind them, a garrote in hand.")
                print("With a swift motion, you wrap the garrote around their neck and pull tight.")
                print(f"{mentor} gasps, eyes wide with shock, before going limp.")
                print("You release the garrote and step back, heart pounding.")
                print("You've done it. You've killed your mentor.")
                print("A sense of triumph washes over you, mixed with a hint of fear.")
                popularity += 10
            else:
                print("You wait until your mentor is alone, practicing archery.")
                print("Silently, you creep up behind them, a garrote in hand.")
                print("Just as you are about to strike, your mentor turns around suddenly.")
                print(f"'What are you doing, {mentor} asks, eyes narrowing suspiciously.'")
                print("You've been caught red handed.")
                print("'Peacekeepers!' they shout.")
                print("Game Over!")
                sys.exit() #ending
        elif number == 3:   
            print(f'You decide to stage an accident for {mentor}.')    
            if chance == 1: #success
                print("You wait until your mentor is alone, near the edge of a cliff.")
                print("With a swift motion, you push them over the edge.")
                print(f"{mentor} screams as they fall, before hitting the rocks below with a sickening thud.")
                print("You've done it. You've killed your mentor.")
                print("A sense of triumph washes over you, mixed with a hint of fear.")
                popularity += 10
            else:
                print("You wait until your mentor is alone, near the edge of a cliff.")
                print("With a swift motion, you push them over the edge.")
                print(f"{mentor} screams as they fall, but miraculously grab onto a ledge halfway down.")
                print("'You tried to kill me!' they shout angrily as they climb back up.")
                print("'Peacekeepers!' they shout.")
                print("Game Over!")
                sys.exit() #ending
        elif number == 4:
            print(f'You decide to strangle {mentor} in the open.')
            if chance == 1: #success
                print("You approach your mentor boldly during a training session.")
                print("Without warning, you wrap your hands around their neck and squeeze.")
                print(f"{mentor} gasps, eyes wide with shock, before going limp.")
                print("You've done it. You've killed your mentor.")
                print("A sense of triumph washes over you, mixed with a hint of fear.")
                popularity += 10
            else:
                print("You approach your mentor boldly during a training session.")
                print("Without warning, you wrap your hands around their neck and squeeze.")
                print(f"{mentor} gasps, eyes wide with shock, before breaking free and shouting angrily, 'Peacekeepers!'")
                print("Game Over!")
                sys.exit() #ending
        else:
            print("Invalid choice. You hesitate too long, and your mentor grows suspicious.")
            print("You've missed your chance; back to training for you...")
    print("Here is a list of skills you can choose from:")
    #select 3 with i think this is done?
    player_skills = []
    skills = ['foraging', 'hunting', 'fire-starting', 'shelter-building', 'camouflage', 'tricks and traps', 'first-aid', 'archery', 'hand-to-hand combat', 'stealth', 'swimming', 'rope and mountain climbing'] #add more later
    
    for i in range (3):
        print("It is Day", i+1, "of training.")
        for skill in skills:
            print(f'- {skills}')
        skill_1 = input(f'Choose a skill to train from the list above: ') #check formatting
        #if not in skills
        if skill_1 not in skills:
            print("Invalid skill. Please choose a valid skill.")
            continue  # Skip the rest of the loop and prompt again
        skills.remove(skill_1)
        print(f'You have chosen {skill_1}.')
        if skill_1 in ['archery', 'hand-to-hand combat', 'hunting'] and district in [1, 2, 4]:
            print(f'As a career tribute, you excel at {skill_1}. {mentor} is impressed.')
            popularity += 5
        elif skill_1 in ['archery', 'hand-to-hand combat', 'hunting'] and district not in [1, 2, 4]:
            print(f'You struggle to keep up with the rigorous training in {skill_1}. {mentor} looks disappointed.') 
            print("You don't know if you will succeed...")
            if popularity < 50:
                probability = random.randint(1, 5)
            else:
                probability = random.randint(1, 4)
            if probability >= 3:
                #success
                print(f"With much pressure, you successfully obtain the skill of {skill_1}.")
                print(f"You feel more confident about {skill_1} in the arena.")
                player_skills.append(skill_1)
                popularity += 2
                determination += 5
            else:
                print(f"You failed to obtain the skill of {skill_1}.")
                popularity -= 2
                if i != 2:
                    print("Try again tomorrow.")
                determination -= 5
                #fail
        elif skill_1 in ['foraging', 'fire-starting', 'shelter-building', 'camouflage', 'tricks and traps', 'first-aid', 'stealth', 'swimming', 'rope and mountain climbing']:
            print(f'You focus intently on mastering {skill_1}. {mentor} nods in approval.') #elaborate
            popularity += 3
            probability = random.randint(1, 3)
            print(f"'This skill is quite easy to pick up,' you think to yourself.")
            determination -= 2
            print(f"{mentor} seems pleased with your progress.")
            if probability > 1:
                print(f"You successfully obtain the skill of {skill_1}.")
                print(f"You feel more confident about {skill_1} in the arena.")
                player_skills.append(skill_1)
                determination += 5
            else:
                print(f"You failed to obtain the skill of {skill_1}.")
                popularity -= 2
                if i != 2:
                    print("Try again tomorrow.")
                
                if district in [1, 2, 4]:
                    popularity -= 5
                    determination += 5
                else:
                    determination -= 5
        else: 
            pass #no option to kill mentor
            print("You decide to skip training for today. A questionable decision...")
            instead = input("What would you like to do instead? (explore/socialise/rest): ")
            if instead.lower() == "explore":
                print("You spend the day exploring the training center.")
                determination += 3
            elif instead.lower() == "socialise":
                print("You spend the day socialising with other tributes.")
                popularity += 3
            elif instead.lower() == "rest":
                print("You spend the day resting and recuperating.")
                skills.append("Resting") #immunity to paranoia and hallucinations. PLEASE I ACTUALLY WANT THIS FUNCTION!!!!!!
            
        #option 1 for day 1.
    return kill_mentor, popularity, player_skills, determination


def performance(): #rebellion input
    print("Your performance at the training sessions has finally concluded.")
    print("Which skill would you like to showcase to the Gamemakers? (This feature is under development.)")
    #list skills
    #impact popularity
    #add options later . if skills not in player_skills, return an error. If they continue, they will score a 1. Or something special/rebellious.
    pass

def ranking():
    print("The Gamemakers will rank the tributes based on their performances tomorrow.")
    #note based on performance
    print("You gaze up anxiously at the scoreboard. (This feature is still under development.)")
    #randomly generate ranking, if skill showcased is in player_skills, +2 to ranking. If kill mentor and chance = 1, -3 to ranking.
    pass

def run_away_option(): #terrain
    choice = input('Would you like to run away from the cornucopia? (y/n): ')
    if choice.lower() == "y":
        print("You have chosen to run away from the cornucopia.")
        print("A stray pack lies on the ground, maybe fifty metres off the cornucopia.")
        print("Do you to attempt to collect it?")
        chance = random.randint(1, 4)
        if chance != 1:
            print("You successfully collect the pack and run away.")
            print("Inside it lies a huge pack of dried meat. You wonder how long it will last.")
            if chance == 4:
                print("It's a shame you're vegetarian. You could use this as barter or an alliance though.")
                print("Tucking that thought into the back of your mind, you slink off into the forest.") #land!!
            print("You feel more prepared for the games now.")
        else:
            print("As you run towards the pack, a tribute from another district spots you. Luckily, they don't want to fight.")
            print("You quickly grab the pack and run away into the trees.")
            #chance of winning, alliance. *choose. 
                #find person to ally or fight
    elif choice.lower() == "n":
        fight_chance = random.randint(1, 4)
        if fight_chance > 1:
            #there will be one fight. 
            pass
        else:
            print("You have chosen to stay to fight for the resources at the cornucopia.")
            print("It towers above you, in its cone-shaped glory. You can't see the inside, but you know it's filled with everything you need to survive.")
            print("And win.")
            determination = determination + 5


def interview_choice(popularity, stylist): #add stylist
    if popularity > 30:
        print("Your interview with Caesar Flickerman approaches.")
        print("Your mentor sits you down.")
        print("How would you like to present yourself?")
        print("1. The innocent victim")
        print("2. The fierce competitor")
        print("3. The strategic thinker")
        print("4. The rebel")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print("You decide to present yourself as the innocent victim, hoping to garner sympathy from the audience.")
            popularity += 5
        elif choice == "2":
            print("You decide to present yourself as a fierce competitor, showing your confidence and strength.")
            print("You want to show the audience that you are not to be underestimated.")
            print("But the Capitol has seen many others like you...")
            popularity += 3
        elif choice == "3":
            print("You decide to present yourself as a strategic thinker, emphasizing your intelligence and planning skills.")
            popularity += 4
        elif choice == "4":
            print("You decide to present yourself as a rebel, challenging the norms, without angering the Capitol.")
            print("This is a risky move, but it could pay off if the audience resonates with your message.")
            popularity += 6
        else:
            print("Invalid choice. You will miss the opportunity to improve your image.")
    return popularity, choice

def live_interview(popularity, choice, name, money):
    print("The night of the interviews arrive.")
    print("As you walk onto the stage, Caesar Flickerman greets you with his signature smile.")
    print(f"'So, {name}, tell us, why should the audience root for *you* in the games?'")
    print("You take a deep breath and begin to tell the audience your story.")
    if choice == "1":
        print("You share your struggles and hardships, hoping to evoke sympathy from the audience.")
        print("You talk about your family, your dreams, and how you never wanted to be here.")
        print("One person from your district is crying in the audience.")
        print("The audience seems to connect with your story, and you feel a surge of support.")
        print("But one person in the crowd yells out 'Get over yourself!' They scoff 'You're nothing new. Just another sob story nobody cares about.'")
        chance = random.randint(1, 4)
        if chance == 1 and money < 5:
            print("The audience seems to agree with them")
            print("'Get off the stage!' they yell.")
            print("One of them even throws a rotten tomato at you.")
            print("You clench your fists in humiliation and resentment.")
            print("But you vow to show them all in the arena - You will survive, and come out on top.") 
            determination = determination + 20
            popularity -= 3
        else:
            print("The crowd starts to boo the person, and you feel a wave of relief wash over you.")
            print("'It's nice for someone to have your back for once', you think to yourself.")
            popularity += 5
            determination = determination + 5
    elif choice == "2":
        print("You confidently talk about your skills and strengths, showing that you are a force to be reckoned with.")
        print("You want the audience to see you as a fierce competitor who will stop at nothing to win.")
        print("Some people in the audience look intimidated, but others seem intrigued.")
        print("Others just look bored.")
        popularity += 3
    elif choice == "3":
        print("You discuss your strategic approach to the games, emphasizing your intelligence and planning skills.")
        print("You want the audience to see you as a smart and capable tribute who can outwit the competition, just like Wiress, who won without lifting a finger.")
        print("Some people in the audience nod in approval, but others seem skeptical.")
        popularity += 4

def morning_chance(district, popularity): #unfinished
    print("You toss and turn in bed, struggling to sleep.")
    print("It haunts you, the blood, the bodies, the screams.")
    print("You wake up with a jolt. It's still dark outside.")
    decision = input("Do you get up, or do you go back to sleep? (get up/sleep): ")
    if decision == "get up":
        print("You decide to get up and start your day early.")
        print("The time is 4:30 AM.")
        morning_activity = input("Do you want to (1) train, (2) journal, or (3) eat an early morning snack? Enter 1, 2, or 3: ")
        if morning_activity == "1":
            print("You head to the training area to practice your skills.")
            #choose a skill to train. pop don't matter, you get it anyway, but determination goes up, tiredness/energy ********* add factor
            print("The sun begins to rise, casting a golden glow over the training center.")
            print("You feel more prepared for the games now.")
            #if you find someone else popularity += 2
        elif morning_activity == "2":   
            print("You sit down with your journal and pen, reflecting on your journey so far.")
            print("You write about your hopes, fears, and strategies for the games.")
            print("The act of writing helps you clear your mind and focus.")
            #determination + 10
        elif morning_activity == "3":
            print("You sneak into the kitchen and grab a quick snack.")
            print("You find some bread and cheese, and eat it quietly.")
            print("The food gives you a bit of energy; you know you'll need more before the games begin.")
            #chance of being caught. charisma.
            #energy + 10
    else:
        print("There's a bird cawing outside, an omen of misfortune.")
        print("As you drift into a restless sleep, the darkness rises to meet you.")
        print("There's a whispering, and you know the voices will torment you again.") 
        # chance of hallucination.

def sponsor_chance(popularity, district): #add skills too
    base_chance = 10  # Base 10% chance
    popularity_bonus = (popularity - 20) // 5  # Every 5 points above 20 adds 1%
    district_bonus = 0
    if district in [1, 2, 4]:
        district_bonus = 5  # Career tributes get a bonus
    total_chance = base_chance + popularity_bonus + district_bonus
    roll = random.randint(1, 100)
    if roll <= total_chance:
        print("You have received a sponsor gift!")
        #generate gift
    else:
        print("No sponsor gifts this time.")

def choose_gift(health, kills, popularity, mentor):
    gift_list = [
        "sage healing salve", "a full jug of water", "a pack of jujubes", "a ration of dried meat", "iron axe", "a spool of leather cord", "flint and steel", "a basket of apples, bread and cheese.", "a hunting knife", "poison antidote", "a tablespoon of sleep syrup"]
    if health <= 50:
        weights = [5 if gift in ["sage healing salve", "a full jug of water", "poison antidote"] else 1 for gift in gift_list]
    pass
    #kill mentor/number of kills/popularity

def generate_arena():
    arenas = [
        "scorching desert", "beach with dense jungle", "snowy mountain range",
        "swampy marshland", "dense forest with rivers", "rocky canyon",
        "volcanic terrain", "abandoned urban area", "floating islands",
        "underground cave system", "toxic wasteland",
        "underwater city", "ancient ruins", "mystical forest"]
    arena = random.choice(arenas)
    print(f"The gamemakers have chosen an arena of {arena} this year.")
    return arena

def start_location(arena, determination): #alliances. 
    locations = [
        "at the edge of a dense forest", "near a sparkling river",
        "on a rocky hillside", "in an open field", "beside a steep cliff",
        "within a dark cave", "on a sandy beach", "in a ruined building"]
    location = random.choice(locations)
    print("You are ushered into underground tunnels, through hallways and up staircases.")
    print("The end is near.")
    determination = determination + 10
    print(f"You are immersed into a new world {location}.")
    return location, determination,

def select_death_message(tribute_name): #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    output = random.choice(core_engine.death_messages)
    return output

def bloodbath(alliance_name):
    #2/3 chance you die immediately if no alliance. else 1/3 chance
    #run away choice
    chance = random.randint(1, 3)
    if chance == 1 or chance == 2 and alliance_name == "":
        print("The whistle blows. You step off the block, and begin to run.")
        core_engine.death_messages("You")
        sys.exit()
    elif chance >= 2 and alliance_name != "":
        print(f"The whistle blows. You and {alliance_name} step off the block, and begin to run.")
    elif chance == 3 and alliance_name == "":
        pass #definite survival
    #generate respective death messages
    #calculate for each tribute.



def first_game(): #determination variable, tiredness/energy variable, add later
    year = random.randint(2000, 4000)
    name, gender, district, age, skill, family, popularity, money, determination = create_user()
    reaping(name, gender, district, age, skill, family, popularity, money, year)
    create_tributes(23, district)
    #print(tributes) debug
    train(district)  #unfinished
    #print(train(district))
    #intermission
    #ask for designer? You are worried that you will get Magno Stift, who dresses the tributes in coal miner outfits every year.
    designer_chosen, popularity, determination = ask_for_designer()
    designer = choose_designer(district, designer_chosen) #unfinished
    randomise_designers(district, 23) #unfinished ADD TRIBUTES_GLOBAL_LIST (global list of tributes made in create tributes)
    #parade() # chance of dying like loella
    mentor = choose_mentor(district) #use mentor
    rebellion_bool, success_chance = kill_mentor(district)

    #chance to kill mentor (you die) if not in 124. 75%
    kill_mentor, chance, popularity, player_skills, determination = training(rebellion_bool, success_chance, mentor, popularity, district) #in training, if popularity is low, chance of planting bombs 50% success rate; if success attempt to escape, 33% chance. intermission called in training too.
    performance() #popularity +/-
    ranking() #out of 24
    intermission() # call in
    interview_choice(popularity, designer) #choose image
    live_interview() #increase popularity, ask why they should be supported
    #final intermission (dinner) #poision someone else, 25% success rate. unlock secret path , rebel, lucy gray baird?**
    sponsor_chance() #based on popularity and district
    morning_chance() #breakfast, alliance last chance with district
    #start game
    #chance of type of arena
    arena = generate_arena() #generate and describe location
    start_location(arena, determination)
    run_away_option()#choose run away or no, or grab item (choose which one), add clue (cornucopia)
    bloodbath() #work on FIGHT CODE, how much chance of fighting/alliance
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
   