class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'Возраст:', self.age, '. Кот счастлив?', self.isHappy)


cat_1 = Cat()
cat_1.set_data("Борис", 2, True)

cat_2 = Cat()
cat_2.set_data("Люпен", 1, False)

cat_1.get_data()
cat_2.get_data()

