## IMPORTS GO HERE

## END OF IMPORTS


## START OF get_diag_sum FUNCTION
def get_diag_sum(n):
    if n<2 or n%2==0:
        return None

    diag_sum = 1
    diag_num_add = 2
    diag_num = 1

    num = n // 2

    for _ in range(num):
        for _ in range(4):
            diag_num += diag_num_add
            diag_sum += diag_num
        diag_num_add += 2

    return diag_sum
if __name__ == '__main__':
    print(get_diag_sum(11))
