while True:
    iter = 0
    try:
        first_num = int(input("Please enter the first number: "))
        second_num = int(input("Please enter the second number: "))
    except ValueError:
        pass
    else:
        sum = first_num + second_num
        print(sum)
        iter += 1
        if iter != 0:
            break
