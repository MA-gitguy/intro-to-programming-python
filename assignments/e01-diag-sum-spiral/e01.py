## IMPORTS GO HERE

## END OF IMPORTS


## START OF get_diag_sum FUNCTION
def get_diag_sum(n):
    if n<2 or n%2==0:
        return None

    diag_sum = 1 # final solution will be in this variable
    diag_num_add = 2 # each rotation has specific value (3, 5, 7, 9) or (13, 17, 21, 25) diff of 2 and 4 respectively
    diag_num = # this is to track the number value and add it to final solution within loop

    num = n // 2

    for _ in range(num):
        for _ in range(4):
            diag_num += diag_num_add
            diag_sum += diag_num
        diag_num_add += 2 # as one rotation complete the values get double

    return diag_sum
if __name__ == '__main__':
    print(get_diag_sum(11))
