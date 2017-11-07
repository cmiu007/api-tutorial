lottery_player = {
    'name': 'Rolf',
    'numbers': (8, 0, 88, 82, 11)
}

class LotteryPlayer:
    # def __init__(self, name):
    #     self.name = name
    #     self.numbers = (8, 0, 88, 82, 11)
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)
    def average(self):
        return sum(self.numbers) / len(self.numbers)


# player = LotteryPlayer()
# print(player.name)
# print(player.numbers)
# print(player.total())
# print(player.average())

player_one = LotteryPlayer('Rolf', (8, 0, 88, 82, 11))
player_one.numbers = (8, 0, 88, 99, 99)
player_two = LotteryPlayer('John', (8, 4, 22, 81, 1))

print(player_one.name == player_two.name)
print(player_one.numbers)