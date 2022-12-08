def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    before_index=0
    after_index=len(input_list)-1
    temp_index=0
    while temp_index <= after_index:
        current= input_list[temp_index]
        if current==0:
            temp=input_list[before_index]
            input_list[before_index]=current
            input_list[temp_index]=temp
            before_index+=1
        elif current==2:
            temp=input_list[after_index]
            input_list[after_index]=current
            input_list[temp_index]=temp
            after_index-=1
            continue
        temp_index+=1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])