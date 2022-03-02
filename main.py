import random

high_range = input("type a number:")

if high_range.isdigit():
    high_range = int(high_range)

    if high-range <= 0 :
        print("please type valid  number range ")
        quit()

else:
    print("please type a number next time:")
    quit()