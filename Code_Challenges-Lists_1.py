"""
Challenge-1 : Append Size
For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

Define the function to accept one parameter for our list
Get the length of the list
Append the length of the list to the end of the list
Return the modified list
"""


def append_size(lst):
    length = len(lst)
    lst.append(length)
    return lst


print(append_size([23, 42, 108]))

"""
Challenge-2 : Append Sum
Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:

1-Define the function to accept one parameter for our list of numbers
2-Add the last and second to last elements from our list together
3-Append the calculated value to the end of our list.
4-Repeat steps 2 and 3 two more times
5-Return the modified list
"""


def append_sum(lst):
    count = 0
    while count < 3:
        lst.append(lst[-1] + lst[-2])
        count += 1
    return lst


print(append_sum([1, 1, 2]))

"""
Challenge-3 : Larger List
Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:

1-Define the function to accept two parameters for our two lists of numbers
2-Check if the length of the first list is greater than or equal to the length of the second list
3-If true, then return the last element from the first list. Otherwise, return the last element from the second list
"""


def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


"""
Challenge-4 : More Than N
Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:

1-Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
2-Count the number of occurrences of item (the second parameter) in lst (the first parameter)
3-If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False
"""


def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


"""
Challenge-5 : Combine Sort
Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

1-Define the function to accept two parameters, one for each list.
2-Combine the two lists together
3-Sort the result
4-Return the sorted and combined list
"""


def combine_sort(lst1, lst2):
    combine = lst1 + lst2
    combine.sort()
    return combine


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
