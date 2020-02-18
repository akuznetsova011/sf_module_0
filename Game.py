import numpy as np

def game():
    count = 0
    a=0
    b=99
    number = np.random.randint(1,100)

    l = [*range(a+1,b+1)]
    
    while a <= b:
        count += 1
        c = (a+b)//2

        if number > l[c]:
            a = c + 1

        elif number < l[c]:
            b = c - 1
        else:
            break
    return (count)

def score_game(game):
    ls_count = []
    for i in range(1,100):
        c = game()
        ls_count.append(c)
    score = int(np.mean(ls_count))

    print('Ваш алгоритм угадывает значение в среднем за {} попыток'.format(score))

    return score

score_game(game)
