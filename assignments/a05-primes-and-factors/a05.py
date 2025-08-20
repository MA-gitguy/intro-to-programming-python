## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
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
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(num):
    for i in range(1, int(num+1)):
        if num % i == 0:
            print(i)
        else:
            continue
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(num):
    prime_num = []
    for i in range(1, int(num+1)):
        if is_prime(i) == True:
            prime_num.append(i)
        else:
            continue

    if not prime_num:
        return None
    else:
        return max(prime_num)
#### End OF MARKER



if __name__ == '__main__':
    print(is_prime(499))  # should return True

    print(get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
