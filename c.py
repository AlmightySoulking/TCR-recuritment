import random, math

def random_noise():
    random_characters = ['$', '!', 'p', '-_-', ':D', '~', '@', '#']
    random_index = [random_characters[random.randint(0, len(random_characters) - 1)] for i in range(4)]

    temp = ""
    for i in random_index:
        temp = temp + i

    return temp


def hypotenuse(x, b):
    return math.sqrt(x**2 + y**2)
# One way to do it.
if __name__=='__main__':
    print("TRY TO STOP THIS FROM BEING PRINTED IN FILE a.py WITHOUT DELETING THIS PRINT STATEMENT")
