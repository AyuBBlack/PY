class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'Возраст:', self.age, '. Кот счастлив?', self.isHappy)


cat_1 = Cat("Борис", 2, True)
cat_2 = Cat("Люпен", 1, False)
