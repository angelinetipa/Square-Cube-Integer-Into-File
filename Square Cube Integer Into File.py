# define function that create double and triple text
def create_double_triple_txt():
    # open integers.txt [read], double.txt [append], triple.txt [append]
    with open("integers.txt") as file_int, open("double.txt", "a") as file_sqr, open("triple.txt", "a") as file_cube:
        # for each line in integers.txt
        for line in file_int:
            integer = int(line)
            # if integer is even, # write to double.txt the square of integer
            if integer % 2 == 0:
                square = integer ** 2
                file_sqr.write(str(square) + "\n")
# if integer is odd, #write to triple.txt the cube of integer
# call the function/output
create_double_triple_txt()