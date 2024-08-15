class Person:
    num = 20

    def __init__(self, name):
        self.name = name

    def run(self, num):
        print("run" * num)

    def say_something(self):
        print(f"こんにちは、私は{self.name}です")
        run(10)

person = Person("Miyagi")
print(person.say_something())

class Athlete(Person):
    def run(self, num):
        print("run" * num, "Jump")

athlete = Athlete("Ryoichi")
print(athlete.say_something())
