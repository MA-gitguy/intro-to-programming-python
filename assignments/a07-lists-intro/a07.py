## IMPORTS GO HERE

## END OF IMPORTS

# Another fxn for ease
def points_calculate(grade):
    points=0.00
    if grade=="A+":
        points=4.00
    elif grade=="A":
        points=4.00
    elif grade=="A-":
        points=3.67
    elif grade=="B+":
        points=3.33
    elif grade=="B":
        points=3.00
    elif grade=="B-":
        points=2.67
    elif grade=="C+":
        points=2.33
    elif grade=="C":
        points=2.00
    elif grade=="C-":
        points=1.67
    elif grade=="D+":
        points=1.33
    elif grade=="D":
        points=1.00
    elif grade=="F":
        points=0.00
    else:
        return None

    return points

### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def calculate_sgpa(x):
    if type(x) != list:
        sgpa = points_calculate(x)
        return sgpa

    else:
        total_marks = []
        no_of_sub = len(x)
        for i in x:
            sgpa = points_calculate(i)
            total_marks.append(sgpa)

        if None in total_marks:
            return None
        elif no_of_sub == 0:
            return 0

        else:
            total_sgpa = sum(total_marks) / no_of_sub
            return total_sgpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(x, y):

    if type(x) != list:
        sgpa = points_calculate(x)
        return sgpa

    else:
        if len(x) != len(y):
            return None
        points_list = []
        for i in x:
            sgpa = points_calculate(i)
            points_list.append(sgpa)

        if None in points_list:
            return None

        else:
            final_sgpa = sum([a * b for a, b in zip(points_list, y)]) / sum(y)
            return final_sgpa
#### End OF MARKER


if __name__ == '__main__':
    print(calculate_sgpa(['A+']))
    print(calculate_sgpa_weighted(['A+'], [4]))
