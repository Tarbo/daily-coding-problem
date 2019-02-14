"""
@author: Okwudili Ezeme
@date: 2019-02-13
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import numpy as np


def uniform_generator(k):
    return np.random.random_integers(1, k)


def shuffle():
    cards = np.linspace(1, 52, num=52, dtype=np.int).tolist()
    for read_in in range(len(cards)):
        write_in = uniform_generator(read_in + 1)
        if write_in != read_in:
            cards[read_in], cards[write_in] = cards[write_in], cards[read_in]
            print(f'>>> {cards[read_in]} ---> {cards[write_in]} <<<')


if __name__ == "__main__":
    shuffle()
