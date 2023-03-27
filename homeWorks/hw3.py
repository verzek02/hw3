class Bank:

    def __init__(self, name, balanse):

        self._name = name

        self._balanse = balanse

    def moneyX(self):

        ad = input(f'сколько добавишь к своим {self._balanse} введи сумму: ')

        print(self._balanse + int(ad))

    def _kill(self):

        if self._balanse > 0:

            print('теперь у тебя все наличкой')

            return self._balanse - self._balanse

        else:

            print('ты и так бомж, на счету нету денег')

            return self._balanse

    def __jackpot(self):
        return self._balanse * 10

    def _copyy(self, other):

        print(f'ваш сложенный баланс {self._balanse + other._balanse}\n'

              f'было{self._balanse}')


bank = Bank('mbank', 20)

load = Bank('g', 233)

bank.moneyX()

print(bank._kill())

bank._copyy(load)


class Just(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    def name(self):
        return self._name

    def name_set(self, new_name):
        self._name = new_name

    def balance(self):
        return self._balanse

    def balance_set(self, new_balance):
        self._balanse = new_balance


class Just2(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    @property
    def nam(self):
        return self._name

    @nam.setter
    def nam(self, value):
        self._name = value

    @property
    def balanc(self):
        return self._balanse

    @balanc.setter
    def balanc(self, value):
        self._balanse = value


pro = Just('max', 200)
pro2 = Just2('lida', 300)

print(pro.name())
pro.name_set('john')
print(pro.name())
print(pro2.nam)
pro2.nam = 'john'
print(pro2.nam)
pro.balance_set(100)
print(pro.balance())
pro2.balanc = 122
print(pro2.balanc)
# beka\scripts\activate