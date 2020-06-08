import random

noun_dict = {}
nouns = ["house", "water", "wolf", "brick", "mortar", "red", "coffee"]
verb_dict = {}
verbs = ["Blow", "Sneak", "Drink", "Lay", "Bake", "Sit"]

def random_sentence():
    noun1 = nouns[random.randint(0, len(nouns)-1)]
    verb1 = verbs[random.randint(0, len(verbs)-1)]
    noun2 = nouns[random.randint(0, len(nouns)-1)]
    print(f"The {noun1} {verb1} the {noun2}")
    cont = input("Would you like to continue? (Type 'True' to continue)")
    if cont == "True":
        random_sentence()
    elif (cont == "quit" or cont == "q"):
        return
    elif cont == "exit":
        return
# random_sentence()



def word_jumbler(c_score, user_score, words):
    all_words = words
    word = words[random.randint(0, len(words)-1)]
    times = int(input("How many times do you want to shuffle the word?\n"))
    shuffled_word = shuffler(word, times)
    guess = grab_input(shuffled_word)
    if guess == word:
        user_score+=1
        print("awesome job\n")
    else:
        c_score+=1
        print(f"The computer wins this round. The word was {word}")
    print(scoreboard(c_score, user_score))
    replay = input("If you want to exit the game loop, type in q\n")
    if replay == "q":
        print("The final score is:")
        print(scoreboard(c_score, user_score))
        exit()
    else:
        word_jumbler(c_score, user_score, all_words)

def shuffler(word, times):
    for i in range(0, times):
        ls = list(word)
        random.shuffle(ls)
        word = ''.join(ls)
    return word

def printer(word):
    print(f"The word is {word}\n")

def grab_input(shuffled):
    return input(f"what is your guess?, the shuffled word is {shuffled}\n")

def scoreboard(c_score, user_score):
    return f"Computer score: {c_score}\n User score: {user_score}"

word_jumbler(0,0, nouns+verbs)
# print(shuffler("pupil", 1))
# ls = list("123456789")
# random.shuffle(ls)
# word = ''.join(ls)
# print(word)