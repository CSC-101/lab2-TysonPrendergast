#My email is typrende@calpoly.edu I am Tyson Prendergast

#Task 3
def smallest(n: float, m: float) -> float:
    if n < m:
        return n  # For which calls below is this statement evaluated? n<m is True
    else:
        return m


first = smallest(3, 2)  # What is the value of first? 2
second = smallest(2, 2)  # What is the value of second? 2
#Is this a reasonable result? Why or why not? Yes, 2 is the only value and therefore the smallest
print(second)




def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # In general, when will a call to this function evaluate this statement? when a>b and a>c
   elif b > c:
      return b + c  # In general, when will a call to this function evaluate this statement? when b>=a and b>c
   else:
      return 2 * c  # In general, when will a call to this function evaluate this statement? when c>=a and c>=b


answer1 = function2(3, 2, 1)  # What is the value of answer1?1
answer2 = function2(2, 3, 1)  # What is the value of answer2?4
answer3 = function2(2, 1, 3)  # What is the value of answer3?6
print(answer3)

#Task 4
from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? True on first and second
    if test:                            # What is this check preventing? negative indexes and indexes that are too big
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? none
second = checked_access([1, 0, 1], 2)    # What is the value of second? 1
print(second)



def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
    elif len(L) > 1:                                  #   and what are the values being added? first and 4+2+3
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated
    elif len(L) > 0:                                  #   and what are the values being added? third and 7+4
        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added? second and 6
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(third)


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? ["this", "is", "confusing", "code."]
         # What are the values of first and second at this point? ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
         # What happened? "Avoid" and "such" were made uppercase and appended to words
print(second)