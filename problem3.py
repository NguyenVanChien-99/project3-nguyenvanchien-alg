def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input= sort(input_list)
    first_num=0
    second_num=0
    if len(input_list)%2==1:
        first_num=sorted_input[0]
        sorted_input=sorted_input[1:]
    start=0
    while start<len(sorted_input):
        first_num=first_num*10+sorted_input[start]
        start+=1
        second_num=second_num*10+sorted_input[start]
        start+=1
    return [first_num,second_num]

def sort(input):
    if len(input)<=1:
        return input
    p = input[len(input)//2]
    left=[]
    right=[]
    for i in input:
        if i>p:
            left.append(i)
        elif i<p:
            right.append(i)
    return sort(left)+[p]+sort(right)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])