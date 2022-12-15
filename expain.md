# Problem 1

> The idea is get the number in the middle(Start=0, end = number we put in. So middle = (Start+End)/2) then we will canculate squared of it
> if it equal to [number] , we return it.
> if less then [number], back to step 1 but Start= (Start of step 1), end = (middle)  (recurser).
> otherwise , we back to step 1 but Start= (middle), end = (end of step 1) (recurser).
> * note : if floored start number equal to floored end number, we return floored start.
> * =>>>> Big O: O(log(n))
> * At the begining, the length of input is [n]. After first step, we have [n/2] (row 27,28), After second step, we have [n/4] (row 27,28) and so on... . So big o is O(log(n))
> * Space complexity: for each step, we will have to create 4 variables ( row 20-23) and number of steps is log(n) , so : O(4*log(n))=> O(log(n))
> * * =>>>>Why choose:  Using binary search because after each step, we will a half list and reduce the time complexity (O(logn)) 
# Problem 2

> Using recurser
> I will get the middle of list and compare it with the number we need to search, if both are equal, just return the middle
> * if the middle item's value is more than [number]
> * we need to check the first item
> * if it more than [number], that's mean all the items from [first] to [middle] are more then [number], we need to check the rest (from [middle+1] to [end]) (Back to step 1)
> * else we need to check the items from [first] to [middle-1]) (Back to step 1)
> * else, we will do the same thing as above but in reverse
> * if first item more than [number], we to check the items from [first] to [middle-1]) (Back to step 1)
> * else  we to check the items from [middle+1] to [end]
> * =>>>> Big O: O(log(n))
> * At the begining, the length of input is [n]. After first step, we have [n/2] (row 26-33 : search from [first - middle] or from [middle - end]), After second step, we have [n/4] (row 26-33) and so on... . So big o is O(log(n))
> * Space complexity: for each step, we will have to create 3 variables ( row 14-2) and number of steps is log(n) , so : O(3*log(n))=> O(log(n))
> * * =>>>>Why choose:  Using binary search because after each step, we will a half list and reduce the time complexity (O(logn))

# Problem 3
> I will sort the list first (descending) and create 2 numbers [first_number] (0) and [second_number] (0)
> If total number of items is odd. we will remove the first item  from the list and put it to [first_number]
> Then get 2 first items of the list and put the first ont to [first_number], second one to [second_number]. We will continute until the list empty
> then we will return this 2 numbers
> * Big O: O(n*log(n))
> * We have : O(n*log(n)) (for sort function -row 10) + O(6) (row 11- 16) + O(n*4) (for while loop , row 17-21) => So summary: O(n*log(n))
> * * Space complexity: For the sort function (row 24):  for each step, we will have to create 3 lists ( row 28-30 to contain all the items of the original list => O(n)) + 2 variables (row 25,27) and number of steps is log(n) => so total will be : O((n+2)*log(n))=> O(n*log(n))
> * * Space complexity: rearrange_digits: O(n*log(n)) (for sort function ,row 24) + O(3) (row 11-16) => O(n*log(n)) 
> * * =>>>> Why choose: Choose QuickSort because it reduces the number of comparisons required and  it also doesn’t require any extra storage

# Problem 4
> Step 1:I will create 3 pointers: [first] , [last], [main]. The [first] and [main] will point to first element of the list, [last] will point to the last element of the list
> Step 2:[main] for interate . So while [main] is less than or equal [last], we will check it if:
> * [main] item equal to 2 => swap it with the [last] item and move the [last] item to previuos and back to step 2
> * [main] item equal to 0 => swap it with the [first] item, move the [first] and [main] to the next one ack to step 2
> * else => just move the [main] to next one
> * Big O : O(n)
> * We have : O(3) ( row 8-10) + O(n*7) (for while loop, row 11-24, worstest: list are already sorted )
> * Space complexity: O(3) ( row 8-10) + O(n) ( while loop, create variable row 12) => total : O(n)
> * * =>>>> Why choose: Just need a list because we don't need to change the size of it , and it's easy to get items at specific index

# Problem 5
> Using Trie to store the words , each word's charater will be a Trie Node. and the node of previous character will contains the node of next .
> suffixes function:
>> Create list to contains possible suffixes.
>> if current node is a word, then add [suffix] to the list and find the suffixes of its childrens and put it to the list also. 
>> finally, we return this list

> * TrieNode.insert (row 12): O(1) (row 14)
> * Space complexity: O(1) (row 14, just create 1 variable)
> * ========================================================================================================
> * TrieNode.suffixes (row 19): O(3) (row 23-25) + O(n*n) (for loop, row 26,27. Each item will get call to the suffixes funtion again and so on. So it will be n*n) => O(n*n)
> * Space complexity: O(n) (row 23,25 . FOr the worst case each character is a word)
> * ========================================================================================================
> * Trie.insert (row 36): O(1) (row 38)+ O(3*n) (for loop ,row 40-43) + O(1) (row 44) => O(n)
> * Space complexity: O(1) (row 38) + O(n) ( row 42, insert function inside for loop, for worst case) => O(n)
> * ========================================================================================================
> * Trie.find (row 46) :  O(1) (row 48)+ O(2*n) (for loop ,row 50-52) => O(n)
> * Space complexity: O(1) (row 48, just create 1 variable)
> * ========================================================================================================
> * Note : assume that [not in] function have Big O = O(1)
> * * =>>>> Why choose: Choose Trie because it's easy to add and search element. It's also save memories

# Pronlem 6
> Create [min] and [max] with the value equal to the first element of input list
> interate the list:
> * if current item more than [max] ,then [max]= current item
> * if current item less than [min] ,then [min]= less item
> * Big O : O(3) (row 8-11)+ O(3*n) (For loop , row 12-17) => O(n)
> * Space complexity: O(3) (row 8,10,11) => O(1)
> * * =>>>> Why choose: Just need a list because we don't need to change the size of it , and it's easy to get items at specific index

# Problem 7
> Using Trie to store the routes and its handler fucntion.
> Each part of path will be a TrieNode
> Router class: there are 3 atrributes : routes (Trie), default handler, root path
> * add_handler: if the path is the root path, we do nothing, else we add the path and its handler to the routes (Trie)
> * lookup: use routes (Trie) to find the handler of the path, if it return None, then we return default handler .

> * RouteTrieNode.insert (row 38): O(1)
> * Space complexity: O(1) (row 38, just create 1 variable)
> * ========================================================================================================
> * Trie.insert (row 8): O(1) (row 11)+ O(3*n) (for loop ,row 13-16) + O(1) (row 17) => O(n)
> * Space complexity: O(1) (row 11) + O(n) ( row 35, insert function inside for loop, for worst case) => O(n)
> * ========================================================================================================
> * Trie.find (row 19) :  O(1) (row 22)+ O(2*n) (for loop ,row 24-27) => O(n)
> * Space complexity: O(1) (row 22, just create 1 variable)
> * ========================================================================================================
> * Router.split_path (row 72): O(3) (row 76-79)=> O(1)
> * Space complexity: O(n) (row 80, need to create a list to store parts of path)
> * ========================================================================================================
> * Router.add_handler (row 50): O(1) (row 54)+ O(1) (row 56, split_path function)+ O(n) (row 56,Trie.insert function ) => O(n)
> * Space complexity: O(n) (row 54, a list to store parts of path) +O(n) (row 56, insert function) => O(n)
> * ========================================================================================================
> * Router.lookup (row 58) :  O(3) (row 64-66)+ O(n) (row 67,Trie.find function ) +O(2) (row 68,69) => O(n)
> * Space complexity: O(n) (row 66, a list to store parts of path) +O(1) (row 67) => O(n)
> * ========================================================================================================
> * Note : assume that [not in] function have Big O = O(1)
> * * =>>>> Why choose: Choose Trie because it's easy to add and search element. It's also save memories
