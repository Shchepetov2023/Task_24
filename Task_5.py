

from typing import Literal


class Animal:
    def __int__(
            self,
            animal_type: str,
            feeds: Literal['травоядное', 'хищное'],
            animal_makes_a_sound: str,
    ):
        self.animal_type = animal_type
        self.feeds = feeds
        self.animal_makes_a_sound = animal_makes_a_sound

    def __str__(self) -> str:
        return f'Это {self.feeds} животное {self.animal_type}!'

    def sound(self) -> str:
        return f'{self.animal_type} издает звуки {self.animal_makes_a_sound}!'

    def feeds(self) -> str:
        return f'{self.animal_type} кушает {self.feeds}!'


cat = Animal('кот', 'мяукает', 'хищное', 'кушает', 'мясо')

print(cat, cat.sound())
print(cat, cat.feeds())

elephant = Animal('слон', 'трубит', 'травоядное', 'кушает', 'бананы')

print(elephant, elephant.sound())
print(elephant, elephant.feeds())