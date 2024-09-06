#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        N
    """
    # Step 1: Precompute primes using Sieve of Eratosthenes up to the maximum value in nums.
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Step 2: Initialize win counts for Maria and Ben.
    maria_wins = 0
    ben_wins = 0
    
    # Step 3: Simulate the game for each round.
    for n in nums:
        winner = simulate_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    # Step 4: Determine the overall winner.
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    # Create a list to mark prime numbers.
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers.
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    # Collect all prime numbers.
    return [i for i in range(2, n+1) if sieve[i]]

def simulate_game(n, primes):
    # Initialize a set to represent the current game state (all numbers from 1 to n).
    game_set = set(range(1, n+1))
    
    turn_count = 0
    
    for prime in primes:
        if prime > n:
            break
        if prime in game_set:
            # Remove the prime and all its multiples.
            for multiple in range(prime, n+1, prime):
                game_set.discard(multiple)
            turn_count += 1
    
    # Maria wins if turn_count is odd, Ben wins if turn_count is even.
    return "Maria" if turn_count % 2 != 0 else "Ben"
