# Author: JD 01/14/2022

def sum_nums(num1, num2):
    if num1 > num2:
       smaller = num2
       greater = num1
    elif num2 > num1:
        smaller = num1
        greater = num2
    else:
        smaller = num1
        greater = num2

    counter = smaller
    sum = 0

    if smaller != greater:
        while counter <= greater:
            sum += counter
            counter += 1
    else:
        sum = smaller

    print("The sum is {0}.".format(sum))


sum_nums(1,4)
sum_nums(3,13)
sum_nums(5,5)
