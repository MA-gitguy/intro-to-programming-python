## IMPORTS GO HERE
import os
## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory, f_name, skip_white_space=False):
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # full_path = os.path.join(script_dir, f_name)

    full_path = os.path.join(directory, f_name)

    with open(full_path, "r") as file:
        count = 0

        if skip_white_space:
            for line in file:
                if not line.isspace():
                    count+=1
        else:
            for line in file:
                count+=1

        return count



#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory, f_name, count_white_space=False):

    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # full_path = os.path.join(script_dir, f_name)

    full_path = os.path.join(directory, f_name)


    with open(full_path, "r") as file:
        content = file.read()
        if count_white_space==True:
            non_ws_char = "".join(char for char in content if not char.isspace())
            return len(non_ws_char)
        else:
            character_count = len(content)
            return character_count
#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(rel_path1, rel_path2, no_of_lines):
    input_full_path = rel_path1
    output_full_path = rel_path2

    with open(input_full_path, "r") as file1, open(output_full_path, "w") as file2:

        lines_to_move = [file1.readline() for _ in range(no_of_lines)] #actual value of the iteration counter is not needed

        for line in lines_to_move[:-1]:
            file2.write(line)
        file2.write(lines_to_move[-1].rstrip("\n"))

#### End OF MARKER



if __name__ == '__main__':
    print(line_count('.', 'essay.txt'))
    print(line_count('.', 'essay.txt', True))
    print(character_count('.', 'essay.txt'))
    print(character_count('.', 'essay.txt', True))

    move_lines('essay.txt', 'out.txt', 3)
    pass
