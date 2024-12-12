# Prime Game

This project implements a solution for the Prime Game, a game where two players take turns removing prime numbers and their multiples from a set of consecutive integers.

## How it Works

The `isWinner` function simulates the Prime Game between Maria and Ben. It takes the number of rounds (`x`) and a list of maximum numbers (`nums`) for each round as input. The function determines the winner of each round based on the number of prime numbers available. The player who starts the round (Maria) has an advantage if the number of primes is even.

The `get_primes` function uses the Sieve of Eratosthenes algorithm to efficiently calculate all prime numbers up to a given limit.

## Usage

The `isWinner` function can be used to determine the winner of the Prime Game for different sets of rounds and maximum numbers.

**Example:**

```python
>>> from prime_game import isWinner
>>> print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
Winner: Ben
