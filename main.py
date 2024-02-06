import blackjack
from blackjack import BlackJackGame
import numpy.random as npr

def main1():
    # Just learned you can make an instance of a class without instantiating it!
    blackjack = BlackJackGame
    # I may have already learned this, but I can't recall. It's admittedly been awhile.
    # You can instantiate it once again using this:
    game = blackjack()
    # I'd like to be able to take notes while I program.
    # I'll have to find a way to keep comments in and automate their removal when I commit code to my GitHub.
    print(game.shuffle())

def main():
    # My game
    bust = False
    my_game = BlackJackGame()
    my_game.shuffle()
    my_game.draw_card()
    my_game.draw_card()
    while True:
        response = input('Hit? (y/n): ')
        if response == 'y':
            my_game.draw_card()
            if my_game.total >= 21:
                print('House wins.')
                bust = True
                break
        elif response == 'n':
            break
        else:
            print('Please respond with a `y` or `n`')

    # House game
    if not bust:
        house_game = BlackJackGame()
        house_game.shuffle()
        while True:
            house_game.draw_card()
            if house_game.total > 21:
                print('The house busted. You win!')
                break

            # If the house's score isn't larger and not equal to 21, it'll always draw.
            # The house could choose to draw, but in the long run it's not worth it for them.
            if house_game.total > my_game.total:
                print('House wins.')
                break
            elif house_game.total == 21 and my_game.total == 21:
                print('Draw')


def test():
    return npr.randint(10)

if __name__ == '__main__':
    main()
