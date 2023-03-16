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
        return self.balanse * 10
    @property
    def jackpot(self):
        return self.__jackpot()

    @property
    def name(self):

        return f'{self.__name}'

    @name.setter
    def name(self, a):

        self.__name = a

    @property
    def balanse(self):

        return f'{self._balanse}'

    @balanse.setter
    def balanse(self, b):

        self.balanse = b



    def _copyy(self, other):

        print(f'ваш сложенный баланс {self._balanse + other._balanse}\n'

              f'было{self._balanse}')


bank = Bank('mbank', 20)

load = Bank('g', 233)

bank.moneyX()

print(bank._kill())

bank._copyy(load)

load.jackpot