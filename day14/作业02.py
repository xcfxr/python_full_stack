def count(string):
    num_of_digit = 0
    num_of_space = 0
    num_of_others = 0
    num_of_char = 0
    for c in string:
        if c.isdigit():
            num_of_digit += 1
        elif c.isalpha():
            num_of_char += 1
        elif c.isspace():
            num_of_space += 1
        else:
            num_of_others += 1
    print('source string=======>', string)
    print('num_of_digit========>', num_of_digit)
    print('num_of_space========>', num_of_space)
    print('num_of_others=======>', num_of_others)
    print('num_of_char========>', num_of_char)
