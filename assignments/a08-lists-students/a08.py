## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(x):
    if x==None:
        return None

    new_list_data = []
    for i in x:
        roll_no_and_name = i[0:2]
        raw_marks = i[2:]

        raw_marks = tuple(0 if marks is None else marks for marks in raw_marks)
        marks = sum(raw_marks)
        # type conversion
        marks = (marks, )

        final_tuple_data = roll_no_and_name + marks

        new_list_data.append(final_tuple_data)

    return new_list_data


#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(x):
    largest_list = []
    marks = -1

    cumulative_marks_list = find_cumulative_marks(x)

    for i in cumulative_marks_list:
        if i[2] > marks:
            marks = i[2]
            largest_list = [i[0:2]]

        elif i[2] == marks:
            largest_list.append(i[0:2])

    if len(largest_list) == 1:
        return largest_list[0]

    return largest_list
#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]
    results2 = [
        ('p101111', 'Ali Khayam', 0),
        ('p101112', 'Mudasser Farooq', 0),
        ('p101113', 'Tamleek Ali', 0),
    ]

    print(find_cumulative_marks(results))
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print(find_top_student(results))
    print(find_top_student(results2))
    # output: ('p101111', 'Ali Khayam')
