## IMPORTS GO HERE
import math
## END OF IMPORTS

def is_prime(num):
    if num < 0:
        return None
    if num == 2:
        return True
    if num != int(num) or num%2==0 or num < 2:
        return False

    for i in range(3, int(num), 2):
        if num % i == 0:
            return False

    return True


### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(num):
    num = int(round(num))
    if num < 1:
        return None

    while num % 2 == 0:
        print(2)
        num /= 2

    for i in range(3, int(math.sqrt(num)), 2):
        while num%i == 0:
            print(int(i))
            num /= i

    if num>2:
        print(int(num))

#### End OF MARKER

### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):

    if n<0 or n!=int(n):
        return None

    count = 0
    prime_num = 1

    while count < n:
        prime_num += 1
        if is_prime(prime_num):
            count += 1

    return prime_num

#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print(get_nth_prime(4))
