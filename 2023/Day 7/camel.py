"""

i've been lagging a bit in doing AoC so I am just looking through and understanding python submissions until Day 14
reference:
https://github.com/fuglede/adventofcode/blob/master/2023/day07/solutions.py

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. 
Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, 
the second-weakest hand gets rank 2, and so on up to the strongest hand. 
Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger 
(K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying 
each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). 
So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
"""
from collections import Counter

with open('camel_input.txt') as f:
    data = f.read().strip()

def hand_type(hand):
    c = Counter(hand)
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
    counts[-1] += jokers
    match counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1


def solve(data):
    ws = [l.split() for l in data.split("\n")]
    return sum(
        rank * bid
        for rank, (*_, bid) in enumerate(
            sorted(
                (hand_type(hand), *map("*23456789TJQKA".index, hand), int(bid))
                for hand, bid in ws
            ),
            1,
        )
    )


# Part 1
print(solve(data))

# Part 2
print(solve(data.replace("J", "*")))