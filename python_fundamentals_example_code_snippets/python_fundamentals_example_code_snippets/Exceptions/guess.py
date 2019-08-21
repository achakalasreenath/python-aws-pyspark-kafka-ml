from random import randrange


def guess():
    """hffuy"""
    r = randrange(100)
    while (True):
        try:
            guess = int(input("?"))
        # always sp[pecigy the particular exception to be caught
        except ValueError:
            continue
        if guess == r:
            print("you win")
            break


if __name__ == '__main__':
    guess()
