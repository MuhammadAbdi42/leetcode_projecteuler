number = 600851475143

primes = [2]
while True:
    # Dividing the number by the prime until it is not divisible anymore
    while number % primes[-1] == 0:
        number /= primes[-1]

    # If the number reaches 1, then we the last prime we chose is the answer
    if number == 1:
        print(primes[-1])
        break

    # Finding the next prime for the next cycle of division
    i = primes[-1] + 1
    while True:
        is_prime = True

        for prime in primes:
            if prime > i ** 1/2:
                break

            if i % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
            break
        else:
            i += 1
