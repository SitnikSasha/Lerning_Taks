def credit_numb(card_er:str)->str:
    card_er.replace(' ', '')
    change = []
    if card_er.isdigit() and len(card_er) == 16:
        for i in range(len(card_er)):
            if i > 11:
                change.append(card_er[i])
            else:
                change.insert(0, '*')
        return ''.join(change)
    else:
        return "Wrong Input Data"


def polyndrom(aim_word:str)-> bool:
    return aim_word[::-1] == aim_word


class Tomato:
    states = {1: "green",
              2: "yellow",
              3: "red"}

    def __init__(self)->None:
        self._index = 1
        self._state = Tomato.states[self._index]

    def grow(self)->None:
        if self._index < 3:
            self._index += 1
            self._state = Tomato.states[self._index]
        else:
            print(f"Tomato is {self._state}")

    def is_ripe(self):
        return True if self._index == 3 else False


class TomatoBush:
    def __init__(self, tomato_numb: int) -> None:
        self.tomatoes = [Tomato() for i in range(tomato_numb)]

    def grow_all(self) -> None:
        for i in range(len(self.tomatoes)):
            self.tomatoes[i].grow()

    def all_are_ripe(self) -> bool:
        for i in range(len(self.tomatoes)):
            if not self.tomatoes[i].is_ripe():
                return False
        else:
            return True

    def give_away_all(self)->None:
        if self.all_are_ripe():
            self.tomatoes.clear()
        else:
            print("Not all are ready for harvest")


class Gardener:

    def __init__(self, name: str) -> None:
        self.name = name
        self._plant = Tomato()

    def work(self) -> None:
        self._plant.grow()

    @staticmethod
    def knowledge_base(our_ricardo) -> bool:
        return our_ricardo._plant.is_ripe()
