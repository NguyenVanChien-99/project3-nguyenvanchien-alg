def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sort(input_list,0,len(input_list)-1)
    first_num=0
    second_num=0
    if len(input_list)%2==1:
        first_num=input_list[0]
        input_list=input_list[1:]
    start=0
    while start<len(input_list):
        first_num=first_num*10+input_list[start]
        start+=1
        second_num=second_num*10+input_list[start]
        start+=1
    return [first_num,second_num]

def sort(input,start_idx,end_idx):
    if len(input)<=1:
        return input
    if (start_idx < end_idx):
        pivot = input[end_idx]
        index=start_idx-1
        for j in range(start_idx, end_idx):
            if input[j] >= pivot:
                index = index + 1
                (input[index], input[j]) = (input[j], input[index])
        (input[index + 1], input[end_idx]) = (input[end_idx], input[index + 1])
        sort(input, start_idx, index)
        sort(input, index + 1, end_idx)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print('Fail , Expected: {}, output: {}'.format(solution,output))

#normal case
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
#emtpy or length <2
test_function([[], [0, 0]])
#same items
test_function([[0,0,0,0], [00, 00]])