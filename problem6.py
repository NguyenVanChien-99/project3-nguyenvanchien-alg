def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return 0,0
    min = ints[0]
    max=ints[0]
    for item in ints:
        if item>max:
            max=item
            continue
        if item < min:
            min= item
    return min,max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

#Normal case
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((1, 9) == get_min_max([9,8,7,5,4,3,1])) else "Fail")
#same number
print ("Pass" if ((1,1) == get_min_max([1,1,1,1,1,1])) else "Fail")
#only have 1 number
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
#empty
print ("Pass" if ((0, 0) == get_min_max([])) else "Fail")