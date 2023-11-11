class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = int(balance)

    def moneyx(self, sum=0):
        self.sum = sum
        if self.sum == False:
            self.sum = int(input('Какую сумму денег Вы хотите добавить: '))
        self._balance += int(self.sum)

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10
        return f'Джекпот! Баланс: {self._balance}!'

    def plus_balance(self, obj):
        self._balance += obj._balance

    def __str__(self):
        return f'Имя владельца счета: {self._name}. Счет: {self._balance}.'

Beka = Bank('Beka', 100)
Bakai = Bank('Bakai', 100)
# Beka.moneyx()
# Beka._kill()
# Beka._Bank__jackpot()
# Beka.plus_balance(Bakai)
print(Beka)
print(Bakai)