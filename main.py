Prog_Cont = True  # Program loop variable
while Prog_Cont:  # loop beginning
    first_num = input("Please enter the first number \n> ")
    try:  # exception handling.
        first_num == int(first_num)
    except print("please entry valid entry"):
        continue
    sec_num = input("Please enter the second number \n> ")
    try:  # exception handling.
        sec_num == int(sec_num)
    except print("please entry valid entry"):
        continue
    operation = input(" please enter an operation \n 'x,-,/,+'>")
    # Code to allow for operations such as addition subtraction multiplication etc.
    if operation == "-":
        answer = float(first_num) - float(sec_num)
        Prog_Cont = False  # breaking the loop for the whole program
    elif operation == "+":
        answer = float(first_num) + float(sec_num)
        Prog_Cont = False

    elif operation == "/":
        answer = float(first_num) / float(sec_num)
        Prog_Cont = False
    elif operation == "x":
        answer = float(first_num) * float(sec_num)
        Prog_Cont = False

new_text_file = input("Please enter a name for the file\n> ")
if new_text_file == new_text_file:
    file_obj = open(new_text_file, "w+", "r+")  # creation of new file and input sequence
    file_obj.write("\n")
    file_obj.write("The answer to your inputs are " + str(answer))
else:
    file_obj = open(new_text_file, "w+")  # creation of new file and input sequence
    file_obj.write("The answer to your inputs are " + str(answer))
    print(file_obj)
