def even_number_of_evens(numbers):
    """
    Should raise TypeError if a list is not passed into the function
    error message: "A list was not passed into the function
    If numbers is empty return False
    If the numbers of even numbers is odd, return False
    If the numbers of even numbers is zero, return False
    If the numbers of even numbers is even, return True
    """
    if isinstance(numbers, list):

        evens = sum([1 for n in numbers if n % 2 == 0])
        # line 12 same as lines 14 to 23
        # if numbers == []:
        #     return False
        # else:
        # evens = 0

        # print(sum([1 for n in numbers if n % 2 == 0]))

        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1
        
        return True if evens and evens % 2 == 0 else False
        # line 23 same as lines 25 to 28
        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed into the function.")

if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 4]))
    