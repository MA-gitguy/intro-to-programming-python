## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x):
    diff_of_guess = 0.000001
    guess = x / 2.0

    if x== 0:
        return 0

    while True:
        new_guess = improve_guess(guess, x)
        if abs(new_guess-guess) < diff_of_guess:
            print(new_guess)
            return new_guess
        guess = new_guess

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(num1, num2):
    avg = float(num1 + num2) / 2
    return avg

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess_number, x):
    if guess_number == 0:
        return x
    avg_of_guess = average(guess_number, x/guess_number)
    return avg_of_guess

#### End OF MARKER




if __name__ == '__main__':
    print(sqrt(36))
