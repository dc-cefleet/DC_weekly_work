

class Character():

    def __init__(self,name, position, speed = 10, health=100, attack_power = 10):
        print("This is getting instantiated here as a character")
        self.speed = speed
        self.health = health
        self.name = name
        self.position = position
        self.attack_power = attack_power

    def move(self, direction, speed):
        if direction == 'right':
            self.position['x'] += speed
        elif direction == 'left':
            self.position['x'] -= speed
        elif direction == 'up':
            self.position['y'] -= speed
        elif direction == 'down':
            self.position['y'] += speed
        return self.position.values()

class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        print("This is getting instantiated as an enemy")
        self.health = 90
        self.speed = 100
        pass
class Player(Character):
    def __init__(self, name, position, speed, health):
        print("This is getting instantiated as an player")
        self.speed = 10
        pass

# player1 = Player({"x":0, "y":0})
# player1.move("left", 10)
# player2 = Player({"x":5, "y":10})
dp = {"x":5, "y":10}
player3 = Enemy("Clint", dp)
# player4 = Player("David", dp, 10, 100)
print(player3.attack_power)
# print(player4.speed)
# print(player1)