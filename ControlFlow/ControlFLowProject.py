def allPrimesUpTO(num):
    primes = [2]
    sqrt = num ** 0.5
    for number in range(3, num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                # not prime
                break
            if factor > sqrtNum:
                # prime
                primes.append(number)
                break
    return primes, f"SQRT of {num} is:", sqrt


print(allPrimesUpTO(8))
