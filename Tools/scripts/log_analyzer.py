NSMALLPOSINTS = 1001
NSMALLNEGINTS = 1000

frequency = [0] * (NSMALLNEGINTS + NSMALLPOSINTS)

with open('log.log') as log:
    for line in log:
        try:
            i, f = line.split()
        except ValueError:
            continue
        if i.isnumeric():
            frequency[int(i) + NSMALLNEGINTS] += int(f)

print('\n'.join([f'{idx - NSMALLNEGINTS} {freq}' for idx, freq in enumerate(frequency)]))