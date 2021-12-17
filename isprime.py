def is_prime(n):
    k = n//2
    while k != 1:
        if n % k == 0 :
            return(str(n) + " is not prime")
        k -= 1
    return(str(n) + " is prime")


print(is_prime(int(input())))