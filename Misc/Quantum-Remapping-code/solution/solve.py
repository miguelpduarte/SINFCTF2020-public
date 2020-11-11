from pwn import *
from collections import defaultdict

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

r = remote(remote_addr, remote_port)

r.recvlines(2)

data = []
max_x = 0
max_y = 0

while True:
    try:
        [x_raw, y_raw] = r.recvuntil('= ? ').strip().split(b'+')
        x = int(x_raw)
        # Removes the '= ?' from 'num = ?'
        y = int(y_raw[0:-3])

        r.sendline('0')
        reply = r.recvline().strip()
        # print(reply)

        if reply == b'yes':
            # print('put 0')
            data.append((x, y, 0))
        else:
             # print('put 1')
            data.append((x, y, 1))

        max_x = max(x, max_x)
        max_y = max(y, max_y)

        # print(data[-1])
    except EOFError:
        break

# Data is 0-indexed
width = max_x + 1
height = max_y + 1

print(f"Array has {len(data)} elems")
print(f"w:{width} h:{height}")

# Default dict to simplify creating nested dict
# https://stackoverflow.com/questions/16333296/how-do-you-create-nested-dict-in-python
coord_dict = defaultdict(dict)

for (x, y, is_white) in data:
    # print(f"{x},{y} -> {is_white}")
    coord_dict[x][y] = is_white

# print(coord_dict)

# This one is hacky but works for Google Lens at least (not QR Droid)
# It seems to be a little "skinny" tho, since the font isn't monospaced? it works fine for the generated txt tho...
for y in range(height):
    for x in range(width):
        if coord_dict[x][y] == 1:
            print('  ', end='')
        else:
            # print('██', end='')
            print('##', end='')
    print()



# Based on https://stackoverflow.com/questions/14831248/pil-selection-of-coordinates-to-make-an-image
# Using Pillow to generate an actual image from the coordinates
# This works much better than the other option (text)
from PIL import Image, ImageDraw

img = Image.new("RGB", (400,400), "white")
draw = ImageDraw.Draw(img)

dotSize = 2

for y in range(height):
    for x in range(width):
        if coord_dict[x][y] == 1:
            draw.rectangle([x,y,x+dotSize-1,y+dotSize-1], fill="black")
        else:
            draw.rectangle([x,y,x+dotSize-1,y+dotSize-1], fill="white")
    print()

img.show()

