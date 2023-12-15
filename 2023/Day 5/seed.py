"""
instructions were very long for this part so I will just write key information.

input: seeds

input:output through all the maps

find the lowest location number that corresponds to any of the initial seed numbers
"""
from functools import reduce

# get seeds into list
seeds, *mappings = open('seed_input.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

# a tuple with seed start and range pairs
# and the mappings are passed in
def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: yield (start, length); break

print(*[min(reduce(lookup, mappings, s))[0] for s in [
    
    #zip for part 1 seed number and range of 1
    zip(seeds, [1] * len(seeds)),

    #zip for part 2 start and end range of seed numbers
    zip(seeds[0::2], seeds[1::2])]])