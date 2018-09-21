import numpy as np

def pla():
    # TODO: start coding here...
    # the first thing is to read `pla.dat`
    f  = open('./pla.dat', 'r')
    x = [[float(num) for num in line.split(' ')] for line in f ]  # l is a 400*5 list

    y = []
    for one in x:
        one.insert(0, 1)
        y.append(one.pop())

    w = [1, 0.97681, 0.10723, 0.64385, 0.29556]

    num_of_try = 1
    while True:
        count = 0
        for i, j in zip(x, y):
            if np.dot(w, i)>0:
                sign = 1
            else:
                sign = -1

            if sign != j:
                w = w + np.dot(j, i)
                num_of_try += 1
            else:
                count += 1
        if count == len(x):
            #print("#" + str(num_of_try), end = " ")
            print("my answer:")
            print(w)
            break



if True: # TODO: change `False` to `True` once you finish `pla()`
    pla()
