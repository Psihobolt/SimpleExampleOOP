class YardCat:
    def __init__(self, name_cat):
        self.__name_cat = name_cat

    def eat(self):
        return f'My name is {self.__name_cat} and I like to eat sausages'

    def scream(self):
        return f'My name is {self.__name_cat} and I is yard cat and like sreaming. Meeeeeooooow'


class ScotlandCat:
    def __init__(self, name_cat):
        self.__name_cat = name_cat

    def eat(self):
        return f'My name is {self.__name_cat} and I don\'t like to eat sausages, I like to eat only premium food'

    def scream(self):
        return f'My name is {self.__name_cat} and I is scotland cat and and I\'m too lazy to scream'


def feed_the_yard_cat(yard_cat):
    print(yard_cat.eat())
    print(yard_cat.scream())

def feed_the_scotland_cat(scotland_cat):
    print(scotland_cat.eat())
    print(scotland_cat.scream())


feed_the_yard_cat(YardCat('Boris'))
feed_the_scotland_cat(ScotlandCat('Artur'))
