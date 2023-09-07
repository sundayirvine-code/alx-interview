#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def calculate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def isWinner(x, nums):
    prime_numbers = calculate_primes(max(nums))
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        if n in prime_numbers:
            prime_numbers.remove(n)
        if len(prime_numbers) % 2 == 0:
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None


