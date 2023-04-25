# open integers.txt [read], double.txt [append], triple.txt [append]
with open("integers.txt", "r") as file_int, open("double.txt", "w") as file_sqr, open("triple.txt", "w") as file_cube:
    # for each line in integers.txt
    for line in file_int:
        integer = int(line)
        # if integer is even, write to double.txt the square of integer
        if integer % 2 == 0:
            square = integer ** 2
            file_sqr.write(str(integer) + " ^ 2 = " + str(square) + "\n")
        # if integer is odd, write to triple.txt the cube of integer
        else:
            cube = integer ** 3
            file_cube.write(str(integer) + " ^ 3 = " + str(cube) + "\n")
