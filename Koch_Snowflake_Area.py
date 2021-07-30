#Solving the Koch Snowflake area of a given side
import math
def initial_area(side):
    return math.sqrt(3) / 4 * (side**2)

def get_area(times, side):
    init = initial_area(side)
    total=0
    for n in range(0,times):
        total += (4/9)**n
    return init*(1+(1/3)*total)


if __name__ == '__main__':
    side = int(input("Enter size of side: "))
    iteration = int(input("Enter how much iterations: "))
    print(f"The area of the Koch snowflake iterated {iteration} time(s) with a side length of {side} is {get_area(iteration,side)}")