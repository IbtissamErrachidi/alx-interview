#!/usr/bin/python3

def sieve(n):
    """Returns a list of booleans indicating whether numbers up to n are prime."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_primes_up_to(n, primes):
    """Counts the number of prime numbers up to n."""
    return sum(primes[:n + 1])

def isWinner(x, nums):
    """
    Determines who wins the most rounds.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)
    primes = sieve(max_num)  # Generate a list of prime numbers up to the maximum value in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, primes)
        # If the count of prime numbers is odd, Maria wins; otherwise, Ben wins
        if prime_count % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

