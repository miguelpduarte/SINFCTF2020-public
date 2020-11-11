#!/usr/bin/python3
import random
import sys

# https://stackoverflow.com/questions/9252373/random-iteration-in-python
def randomly(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)


qr_data = [
'                                                                          ',
'                                                                          ',
'                                                                          ',
'                                                                          ',
'        ##############  ########      ####    ####  ##############        ',
'        ##          ##  ##    ##  ##    ##  ##  ##  ##          ##        ',
'        ##  ######  ##    ##      ########  ######  ##  ######  ##        ',
'        ##  ######  ##        ####  ######    ####  ##  ######  ##        ',
'        ##  ######  ##  ##    ####    ####  ####    ##  ######  ##        ',
'        ##          ##  ######  ####        ######  ##          ##        ',
'        ##############  ##  ##  ##  ##  ##  ##  ##  ##############        ',
'                        ####      ####  ##    ####                        ',
'        ######    ####  ####  ########  ####  ##  ########    ####        ',
'              ##        ##      ######  ######  ##        ####            ',
'            ##  ######  ######  ######  ####  ##      ######  ##          ',
'        ########      ####  ##########    ####        ######              ',
'        ##  ##  ##  ##  ######    ##      ####    ########  ##  ##        ',
'          ##    ##    ########    ##      ####    ##  ######  ####        ',
'          ####  ##  ####      ##  ####    ######      ####  ######        ',
'                ##    ####            ##    ##  ##      ##                ',
'          ####  ########      ######      ##      ##    ####  ##          ',
'          ##    ####      ##    ######  ######  ####  ####  ##  ##        ',
'        ####  ##  ######  ##    ##    ##    ########  ##  ####            ',
'            ####      ######  ####  ##    ####    ##  ####    ####        ',
'        ######  ##  ##    ##      ##      ####  ##############            ',
'                        ##  ##          ##  ######      ##                ',
'        ##############    ##  ##    ##        ####  ##  ####              ',
'        ##          ##  ####      ##  ########  ##      ##    ##          ',
'        ##  ######  ##    ##  ##########  ##    ##############  ##        ',
'        ##  ######  ##    ####  ##          ######    ##                  ',
'        ##  ######  ##  ####    ######  ####  ##    ##  ##  ######        ',
'        ##          ##  ##  ######      ##    ##    ##          ##        ',
'        ##############  ####    ########  ##    ####  ##  ########        ',
'                                                                          ',
'                                                                          ',
'                                                                          ',
'                                                                          ',
]


def handle_input(x, y):
    sys.stdout.write(f"{x} + {y} = ? ")
    sys.stdout.flush()
    raw_answer = sys.stdin.readline().strip()
    if qr_data[x][y] == '#':
        # 1
        if raw_answer == '1':
            print('yes')
        else:
            print('no')
    else:
        # 0
        if raw_answer == '0':
            print('yes')
        else:
            print('no')


height = len(qr_data)
width = len(qr_data[0])

print("I've created a Quantum Reffobler that broke my math!")
print("Can you find out the secret behind this data?")

for i in randomly(range(height)):
    for j in randomly(range(width)):
        handle_input(i, j)
