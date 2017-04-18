# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(list_of_numbers):
    odd_list = []
    for list_item in list_of_numbers:
        if list_item % 2 != 0:
            odd_list.append(list_item)
    sum_odd_numbers = 0
    for odd_list_item in odd_list:
        sum_odd_numbers += odd_list_item
    average = sum_odd_numbers / len(odd_list)
    return average

numbers = [1, 2, 3, 4, 5, 10, 1]
print(odd_average(numbers))
