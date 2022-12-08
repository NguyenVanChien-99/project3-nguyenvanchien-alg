
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
    return find_sqrt(0,number,number)


def find_sqrt(start_num,end_num,number):
    if round(start_num)==round(end_num):
        return round(start_num)
    middle = (start_num+end_num)/2
    pow = middle*middle
    if pow==number:
        return round(middle)
    if pow < number:
        return find_sqrt(middle,end_num,number)
    return find_sqrt(start_num,middle,number)

def get_abs(num):
    if num<0:
        return num*-1
    return num

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

sqrt(-1) #expected : invalid data