#task 1

more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. x takes the value of 1 then 2 then 3 then 4
print("?")                               # What is the value of more at this point?[2,3,4,5] = more


def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. n starts as 1 and returns 1, then it is 2 adn returns 4, then it is 3 and returns 9, and then it is 4 and returns 16

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print(".")                                    # values recorded above? the value of squares is [1,4,9,16] it displays a list of each value in [1,2,3,4] squared


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. n =0 returns F, then n=1 returns F, then n=2 returns F, then n=3 and returns T, and then n=4 and returns T

answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print("?")


def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. m=3 and returns m=4, then m=4 and returns m=5

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. n=0 returns F, then n=1 returns F, then n=2 returns F, then n=3 and returns T, and then n=4 and returns T

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print(""".""")


#task 2

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. total =16 and the last num=1
    return total

result = tally([4, 9, 2, 1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. new_list=[4,9,2,1] and at the end idx=3
    return new_list                    # How does this loop differ from that above? this loop copies the original list and the previous loop adds the values of each entry

result = copy([4, 9, 2, 1])


def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. new_list[0]=5 and value=4, new_list[1]=10 and value=9, new_list[2]=3 and value=2, and new_list[3]=2 and value=1
    return new_list

result = increment_all([4, 9, 2, 1])