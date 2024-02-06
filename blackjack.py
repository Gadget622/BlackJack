import numpy as np
# Black jack involves a deck of cards
# Each deck of cards has thirteen values and four suits.

class Card:
    def __init__(self, suit, value): 
        self.suit = suit
        self.value = value

class BlackJackGame:
    def __init__(self):
        self.deck = self.new_deck()
        self.cards_drawn = []
        self.total = 0

    def new_deck(self):
        deck = []
        suits = ['Spades','Clubs','Diamonds','Hearts']
        values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return deck

    def shuffle(self):
        current_deck = self.deck
        shuffle_deck = []
        while current_deck:
            shuffle_deck.append(current_deck.pop(np.random.randint(len(current_deck))))
        self.deck = shuffle_deck

    def update_total(self):
        new_total = 0
        for card in self.cards_drawn:
            if card.value == 'Ace': # Aces can be 1's or 11's. This will be updated soon.
                new_total += 1
            elif card.value == '2':
                new_total += 2
            elif card.value == '3':
                new_total += 3
            elif card.value == '4':
                new_total += 4
            elif card.value == '5':
                new_total += 5
            elif card.value == '6':
                new_total += 6
            elif card.value == '7':
                new_total += 7
            elif card.value == '8':
                new_total += 8
            elif card.value == '9':
                new_total += 9
            elif card.value in ['10','Jack','Queen','King']:
                new_total += 10
        self.total = new_total

    def draw_card(self):
        new_card = self.deck.pop()
        print(new_card.value, 'of ', new_card.suit)
        self.cards_drawn.append(new_card)

        new_total = self.total
        if new_card.value == 'Ace': # Aces can be 1's or 11's. This will be updated soon.
            if new_total + 11 <= 21:
                new_total += 11
            else:
                new_total += 1
        elif new_card.value == '2':
            new_total += 2
        elif new_card.value == '3':
            new_total += 3
        elif new_card.value == '4':
            new_total += 4
        elif new_card.value == '5':
            new_total += 5
        elif new_card.value == '6':
            new_total += 6
        elif new_card.value == '7':
            new_total += 7
        elif new_card.value == '8':
            new_total += 8
        elif new_card.value == '9':
            new_total += 9
        elif new_card.value in ['10','Jack','Queen','King']:
            new_total += 10
        self.total = new_total

        self.update_total()
        print('-----------------------')
        print(f'The total is {self.total}.')
        if self.total == 21:
            print('21!')
        elif self.total > 21:
            print('-----------------------')
            print('Bust.')