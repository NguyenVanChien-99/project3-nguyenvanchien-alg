# Problem 1

> The idea is get the number in the middle(Start=0, end = number we put in. So middle = (Start+End)/2) then we will canculate squared of it
> if it equal to [number] , we return it.
> if less then [number], back to step 1 but Start= (Start of step 1), end = (middle)  (recurser).
> otherwise , we back to step 1 but Start= (middle), end = (end of step 1) (recurser).
> * note : if floored start number equal to floored end number, we return floored start.

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


# Problem 3
> I will sort the list first (descending) and create 2 numbers [first_number] (0) and [second_number] (0)
> If total number of items is odd. we will remove the first item  from the list and put it to [first_number]
> Then get 2 first items of the list and put the first ont to [first_number], second one to [second_number]. We will continute until the list empty
> then we will return this 2 numbers

# Problem 4
> Step 1:I will create 3 pointers: [first] , [last], [main]. The [first] and [main] will point to first element of the list, [last] will point to the last element of the list
> Step 2:[main] for interate . So while [main] is less than or equal [last], we will check it if:
> * [main] item equal to 2 => swap it with the [last] item and move the [last] item to previuos and back to step 2
> * [main] item equal to 0 => swap it with the [first] item, move the [first] and [main] to the next one ack to step 2
> * else => just move the [main] to next one



# Problem 5
> Using Trie to store the words , each word's charater will be a Trie Node. and the node of previous character will contains the node of next .
> suffixes function:
>> Create list to contains possible suffixes.
>> if current node is a word, then add [suffix] to the list and find the suffixes of its childrens and put it to the list also. 
>> finally, we return this list

# Pronlem 6
> Create [min] and [max] with the value equal to the first element of input list
> interate the list:
> * if current item more than [max] ,then [max]= current item
> * if current item less than [min] ,then [min]= less item

# Problem 7
> Using Trie to store the routes and its handler fucntion.
> Each part of path will be a TrieNode
> Router class: there are 3 atrributes : routes (Trie), default handler, root path
> * add_handler: if the path is the root path, we do nothing, else we add the path and its handler to the routes (Trie)
> * lookup: use routes (Trie) to find the handler of the path, if it return None, then we return default handler .