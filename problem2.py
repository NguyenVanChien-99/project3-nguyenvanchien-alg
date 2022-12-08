def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    output =   search(0,input_list,number)
    print(output)
    return output

def search(start,input_list, number):
    if len(input_list)==0:
        return -1

    if len(input_list)==1:
        if input_list[0]==number:
            return start
        return -1

    middle = len(input_list)//2
    if input_list[middle]==number:
        return start+middle
    ##########
    if input_list[middle]>number:
        if input_list[0]> number:
            return search(start+middle+1,input_list[middle+1:],number)
        return search(start,input_list[:middle],number)
    else:
        if input_list[len(input_list)-1]< number:
            return search(start,input_list[:middle],number)
        return search(start+middle+1,input_list[middle+1:],number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 3, 4], 10])