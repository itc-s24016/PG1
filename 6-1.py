class Car:
    weight = 4000
    num_wheels = 4

    def __init__(self, car_name = "NoName"):
        self.name = car_name

    def calc_weight_per_wheel(self):
        return selt.weight /  self.num_wheels

default_car = Car()

print(default_car.name)

my_car = Car("DeLorean")
print(my_car.name)


#問題１
class Cat:
    cry = "ニャー"
    legs = 4
    is_animal = True

tama = Cat()
print("鳴き声:{}, 足の数:{}, 動物:{}".format(tama.cry, tama.legs, tama.is_animal))


#問題２
class Person:
    def __init__(self, name = "", nationality = "", birth = "", address = ""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいる所:", self.address)

heroine = Person("かぐや姫", "日本", "685", "静岡県富士市")
print(heroine.show_attributes())

hero = Person("金太郎", "日本", "956", "静岡県駿東郡小山町")
print(hero.show_attributes())
