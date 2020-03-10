#!/usr/bin/python3.8

nums = []
# max
nums.append(10 ** 12)
# max prime
nums.append(999999999989)
# square - 1
nums.append(10 ** 12 - 1)
# prime^2
nums.append(999983**2)

for i, N in enumerate(nums):
    fname = f'05_hand_{i:02}.in'
    with open(fname, 'w') as f:
        f.write(f'{N}\n')
