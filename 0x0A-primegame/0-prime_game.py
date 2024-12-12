#!/usr/bin/python3
"""Todo: add module info"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n, where n is the maximum number in the
        set for each round.

    Returns:
        str: Name of the player that won the most rounds, or None if the
        winner cannot be determined.
    """
    if not x or not nums:
        return None
    if x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)  # Get all prime numbers up to n
        num_primes = len(primes)

        # If the number of primes is even, Maria (first player) wins
        if num_primes % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def get_primes(n):
    """
    Calculates all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for finding primes.

    Returns:
        list: A list of prime numbers up to n.
    """
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]
