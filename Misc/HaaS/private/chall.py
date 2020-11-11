#!/usr/bin/python3
import signal
import os
import hashlib
import random

def interrupted():
    pass

POSSIBLE_ALGOS = ['md5', 'sha256', 'sha224', 'sha1', 'blake2b', 'sha512', 'whirlpool', 'ripemd160']

def generate_challenge():
    "Returns: (algorithm, data, solution), ex: ('md5', 'data', 'sol')"
    algo = random.choice(POSSIBLE_ALGOS)
    data = os.urandom(32).hex()
    h = hashlib.new(algo)
    h.update(data.encode())
    solution = h.hexdigest()
    return (algo, data, solution)

CHALLENGE_TIMEOUT = 5

def timed_input():
    signal.alarm(CHALLENGE_TIMEOUT)
    try:
        data = input()
        return data
    except:
        return None

# Method to simplify returning instead of sys/os.exit
def main_loop():
    for _ in range(100):
        (algorithm, data, solution) = generate_challenge()
        print(f"{algorithm}:{data}")

        response = timed_input()
        if not response:
            print('Too slow! Better luck next time!')
            return
        elif response != solution:
            print('Wrong! I thought I could count on you to hash things for me :(')
            return

    with open('flag.txt', 'r') as flag:
        print('Good job!')
        print(flag.read())

if __name__ == '__main__':
    print("You've arrived! Great! I need some hashing on this data, stat!")
    print(f"If you hash things really quickly for these algorithms ({', '.join(POSSIBLE_ALGOS)}) 100 times I'll give you a flag as reward!")

    # Setup signal handler
    signal.signal(signal.SIGALRM, interrupted)

    main_loop()
