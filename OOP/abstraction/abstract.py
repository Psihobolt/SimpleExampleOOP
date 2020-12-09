from abc import ABC, abstractmethod


class Cat(ABC):
    def __init__(self, name_cat):
        self._name_cat = name_cat

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def scream(self):
        pass


class YardCat(Cat):
    def eat(self):
        return f'My name is {self._name_cat} and I like to eat sausages'

    def scream(self):
        return f'My name is {self._name_cat} and I is yard cat and like sreaming. Meeeeeooooow'


class ScotlandCat(Cat):
    def eat(self):
        return f'My name is {self._name_cat} and I don\'t like to eat sausages, I like to eat only premium food'

    def scream(self):
        return f'My name is {self._name_cat} and I is scotland cat and and I\'m too lazy to scream'


def feed_the_cat(cat):
    print(cat.eat())
    print(cat.scream())


feed_the_cat(YardCat('Boris'))
feed_the_cat(ScotlandCat('Artur'))
