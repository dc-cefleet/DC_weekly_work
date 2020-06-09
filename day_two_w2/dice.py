import random
class Dice():
    def __init__(self,name, dice_type, history = []):
        print("This is getting instantiated here as a dice")
        self.name = name
        self.dice_type = dice_type
        self.history = history


    def roll(self):
        # make sure this rolls correctly
        result = random.randint(1, self.dice_type)
        self.history.append(result)
        return result
    
    def average_roll(self):
        # make sure this calculates correctly
        return sum(self.history) / len(self.history)
    
    def information_menu(self):
        answer = input("What information would you like to view about the dice? Options -> 'Show rolls', 'show average', 'reset roll count'")
        if answer == 'Show rolls':
            print(self.history)
        if answer == 'Show average':
            print(self.average_roll())
        if answer == 'reset roll count':
            self.history = []


class Dice_20(Dice):
    def __init__(self, name, dice_type, cheat = 10):
        super().__init__(name, dice_type)
        self.cheat = cheat

    def roll(self):
    # make sure this rolls correctly
        result = random.randint(1, self.dice_type)
        self.history.append(result)
        if self.cheat < 10:
            self.cheat +=1
        return result
    
    def average_roll(self):
        # make sure this calculates correctly
        return sum(self.history) / len(self.history)
    
    def information_menu(self):
        answer = input("What information would you like to view about the dice? Options -> 'Show rolls', 'show average', 'reset roll count'")
        if answer == 'Show rolls':
            print(self.history)
        if answer == 'Show average':
            print(self.average_roll())
        if answer == 'reset roll count':
            self.history = []
        
    def cheat_roll(self):
        ERROR = 2
        if self.cheat == 10:
            target = int(input("What number are you trying to roll?"))
            # make sure this rolls correctly
            result = random.randint(target-ERROR, target+ERROR)
            result = result % 20
            self.history.append(result)
            self.cheat = 1
            return result
        else:
            return ("Stop cheating so much, everyone else will catch on!")

dice_6 = Dice('My d6', 6)
dice_12 = Dice('My d12', 12)
dice_20 = Dice_20('My d20', 20)
# why does my history not save
# print(dice_6.roll())
# print(dice_6.roll())
# print(dice_6.roll())
dice_12.roll()
dice_12.information_menu()
# print(dice_6.history)
# print(dice_20.cheat_roll())
# print(dice_20.cheat)
# print(dice_20.cheat_roll())
    

        