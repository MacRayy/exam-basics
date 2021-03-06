# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(list_of_numbers):
    odd_list = []
    try:
        for list_item in list_of_numbers:
            if list_item % 2 != 0:
                odd_list.append(list_item)
    except ValueError:
        print("These are not numbers")
        return 0
    except TypeError:
        print("These are not numbers")
        return 0
    sum_odd_numbers = 0
    for odd_list_item in odd_list:
        sum_odd_numbers += odd_list_item
    try:
        average = sum_odd_numbers / len(odd_list)
        return average
    except ZeroDivisionError:
        print("If you devide with zero the world will collapse")
        return 0
