class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def short_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Місто: {self.city}")


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def full_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}, Колір: {self.color}")

    def change_color(self, new_color):
        print(f"Зміна кольору автомобіля з {self.color} на {new_color}")
        self.color = new_color


class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено на {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума поповнення має бути більшою за 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття має бути більшою за 0.")
            return
        if amount > self.balance:
            print(f"Недостатньо коштів для зняття {amount}. Баланс: {self.balance}")
        else:
            self.balance -= amount
            print(f"Знято {amount}. Залишок: {self.balance}")

    def check_balance(self):
        print(f"Баланс рахунку {self.account_number}: {self.balance}")


# Приклад використання

if __name__ == "__main__":
    # Person
    p = Person("Олена", 28, "Київ")
    p.short_info()

    # Car
    car = Car("Toyota", "Camry", 2018, "червоний")
    car.full_info()
    car.change_color("синій")
    car.full_info()

    # BankAccount
    account = BankAccount("Іван", "UA1234567890", 1000)
    account.check_balance()
    account.deposit(500)
    account.withdraw(2000)
    account.withdraw(300)
    account.check_balance()
