import random


class Character:
    class_dice = 0
    class_name = "Character"

    def __init__(self):
        self.name = Character.class_name

        self.power = random.randint(1, 20)
        self.dex = random.randint(1, 20)
        self.body = random.randint(1, 20)
        self.know = random.randint(1, 20)
        self.wisdom = random.randint(1, 20)
        self.charm = random.randint(1, 20)

        self.max_hp = int((self.body-10)/2) + Character.class_dice + 10
        self.hp = self.max_hp

        self.class_dice = Character.class_dice

        self.armor = int((self.dex+10)/2) + 11

    def get_info(self):
        return self.max_hp, self.hp, self.armor, self.power, self.dex, self.body, self.know, self.wisdom, self.charm

    def attack(self, armor=11):
        touch = random.randint(1, 20) + int((self.power-10)/2)
        if touch < armor:
            return 0
        elif touch == 1:
            self.hp -= 2
            return 0
        elif touch == 20:
            return 4
        else:
            return 2

    def tacking_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f'{self.name} is dead')

    def rest(self):
        if self.hp + self.class_dice <= self.max_hp:
            self.hp += self.class_dice
        else:
            self.hp = self.max_hp


class NPC(Character):
    class_dice = random.randint(10,  100)
    class_name = "Monster"

    def __init__(self):
        super().__init__()
        self.danger = random.randint(0, 100)
        self.name = NPC.class_name
        self.class_dice = NPC.class_dice

    @staticmethod
    def multi_attack(armor):
        damage = 0
        for i in range(2):
            damage += NPC.attack(armor)
        return damage

    def get_info(self):
        return super().get_info(), self.danger


class PCWarrior(Character):
    class_dice = 10
    class_name = "Warrior"

    def __init__(self):
        super().__init__()
        self.name = PCWarrior.class_name
        self.class_dice = PCWarrior.class_dice
        self.lvl = 1
        self.exp = 0

    def exp_up(self, exp=0):
        self.exp += exp
        while self.exp >= 100:
            self.lvl += 1
            self.exp -= 100
            self.max_hp += random.randint(1, self.class_dice) + int((self.body-10)//2)

    def get_info(self):
        return super().get_info(), self.lvl, self.exp

