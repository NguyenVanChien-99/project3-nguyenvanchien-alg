
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <0:
        print('Invalid data')
        return
    if number <=1:
        return number
    current =0
    for i in range(1,number//2+1):
        pow = i*i
        if pow==number:
            return i
        if pow<number:
            current=i
        else:
            if (pow-number)>(number-current*current):
                return current
            return i
    return current



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")