class Duck:
    def __init__(self, name_duck):
        self._name_duck = name_duck

    def scream(self):
        return f'Duck "{self._name_duck}" says: Quaaaack'

    def fly(self):
        return f'Duck "{self._name_duck}" takeoff and flying in sky'


class DuckFromGame(Duck):
    def scream(self):
        return f'Duck "{self._name_duck}" says: Ha-ha-ha, you missed shooter'


class StrangePerson:
    def __init__(self, name_person):
        self._name_person = name_person

    def scream(self):
        return f'Strange person "{self._name_person}" says: I\'m duck. Quack. Quack.'


# Применяем утиную типизацию
def watch_the_duck(duck):
    if hasattr(duck, 'fly'):
        print(duck.scream())
        print(duck.fly())
    else:
        print(f'Is\'t not duck. He {duck.scream()}. Maybe he crazy')


small_duck = Duck('Small duck')
duck_from_game = DuckFromGame('Duck from shooting game')
strange_person = StrangePerson('Alexandr')
# И юнат наблюдает за утками
watch_the_duck(small_duck)
watch_the_duck(duck_from_game)
watch_the_duck(strange_person)
