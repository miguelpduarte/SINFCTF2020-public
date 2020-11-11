import itertools
import magic
from subprocess import call, DEVNULL

if __name__ == '__main__':
    data_parts = []
    for data_idx in range(6):
        with open(f"../public/{data_idx}.part", 'rb') as f:
            data_parts.append(f.read())

    # print(data_parts)
    print(len(data_parts))

    valid_zips = []

    for idx, perm in enumerate(itertools.permutations(data_parts, len(data_parts))):
        data_perm = b''.join(perm)
        filetype = magic.from_buffer(data_perm, mime=True)
        # print(filetype)

        if filetype == 'application/zip':
            valid_zips.append(data_perm)


    print(f"{len(valid_zips)} valid zips")


    for idx, valid_zip in enumerate(valid_zips):
        print(f"\rTrying {idx}", end='', flush=False)
        with open(f"temp.zip", 'wb') as f:
            f.write(valid_zip)
        return_code = call(['unzip', '-o', 'temp.zip'], stdout=DEVNULL, stderr=DEVNULL)

        if return_code == 0:
            print('\nFound flag!')
            break

