

from typing import Literal


class Animal:
    def __int__(
            self,
            animal_type: str,
            eat: Literal['травоядное', 'хищное'],
            animal_makes_a_sound: str,
    ):
        self.animal_type = animal_type
        self.eat = eat
        self.animal_makes_a_sound = animal_makes_a_sound

    def __str__(self) -> str:
        return f'Это {self.eat} животное {self.animal_type}!'

    def sound(self) -> str:
        return f'{self.animal_type} издает звуки {self.animal_makes_a_sound}!'


cat = Animal('кот', 'мяукает', 'хищное')
elephant = Animal('слон', 'трубит', 'травоядное')

print(cat, cat.sound())
print(elephant, elephant.sound())
