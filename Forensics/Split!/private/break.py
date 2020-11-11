import random

def randomly(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)

if __name__ == '__main__':
    with open('data_orig.zip', 'rb') as f:
        data = f.read()

    assert len(data) == 618

    N_PARTS = 6
    size_per_part_float = len(data) / N_PARTS
    size_per_part = len(data) // N_PARTS

    assert size_per_part_float == 103.0
    assert size_per_part == 103

    data_parts = [data[i*size_per_part:(i+1)*size_per_part] for i in range(N_PARTS)]

    for idx, data_part in enumerate(randomly(data_parts)):
    # for idx, data_part in enumerate(data_parts): # Sequential for initial testing
        with open(f"{idx}.part", 'wb') as f:
            f.write(data_part)

    print(f"Files shuffled! {N_PARTS} parts created!")
