## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(marks):
    grade=""
    marks = round(marks)
    if marks>=90:
        grade = "A+"
    elif marks > 85:
        grade="A"
    elif marks>81:
        grade="A-"
    elif marks>77:
        grade="B+"
    elif marks>73:
        grade="B"
    elif marks>69:
        grade="B-"
    elif marks>65:
        grade="C+"
    elif marks>61:
        grade="C"
    elif marks>57:
        grade="C-"
    elif marks>53:
        grade="D+"
    elif marks>49:
        grade="D"
    elif marks<50:
        grade="F"

    else:
        print("Wrong input")

    return grade

#### End OF MARKER

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

    return points

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(grade1, grade2, grade3):
    total_marks = 0
    no_of_sub = 0
    if grade1!="nothing":
        no_of_sub+=1
        total_marks += points_calculate(grade1)

    if grade2!="nothing":
        no_of_sub+=1
        total_marks += points_calculate(grade2)

    if grade3!="nothing":
        no_of_sub+=1
        total_marks += points_calculate(grade3)

    sgpa = total_marks/no_of_sub
    return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print(get_grade(50))
    print(calculate_sgpa('A', 'B', 'nothing'))
