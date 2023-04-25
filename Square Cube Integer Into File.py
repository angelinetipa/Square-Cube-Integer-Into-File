# define function that create double and triple text
def create_double_triple_txt():
    # open integers.txt [read], double.txt [append], triple.txt [append]
    with open("integers.txt") as file_int, open("double.txt", "a") as file_sqr, open("triple.txt", "a") as file_cube:
# for each line in integers.txt
# if integer is even, # write to double.txt the square of integer
# if integer is odd, #write to triple.txt the cube of integer
# call the function/output
create_double_triple_txt()