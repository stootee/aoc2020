from day22.decks import *


class Game:

    def __init__(self, pl1, pl2, part2=False):
        self.player1 = Player(pl1[:])
        self.player2 = Player(pl2[:])
        self.part2 = part2

    def play(self):

        def cc(ls):
            return ':'.join(map(lambda x: str(x), ls))

        card_combos = []

        while self.player1.score() > 0 and self.player2.score() > 0:
            card_combo = cc(self.player1.cards) + '-' + cc(self.player2.cards)

            if card_combo in card_combos:
                return 1, 0

            card_combos.append(card_combo)

            p1_card = p1 = self.player1.draw()
            p2_card = p2 = self.player2.draw()

            if self.part2:
                if p1 <= len(self.player1.cards) and p2 <= len(self.player2.cards):
                    new_game = Game(self.player1.cards[:p1_card], self.player2.cards[:p2_card], True)
                    p1, p2 = new_game.play()

            if p1 > p2:
                self.player1.receive(p1_card, p2_card)
            elif p2 > p1:
                self.player2.receive(p2_card, p1_card)
            else:
                'A draw!!'

        return self.player1.score(), self.player2.score()


class Player:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        return self.cards.pop(0)

    def receive(self, card1, card2):
        self.cards.extend([card1, card2])

    def score(self):
        return sum([((n+1) * c) for n, c in enumerate(self.cards[::-1])])


# Part 1
print(Game(Player1, Player2).play())

# Part 2
print(Game(Player1, Player2, True).play())
