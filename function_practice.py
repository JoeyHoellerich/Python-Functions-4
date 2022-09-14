# Write a Python function called max_num()to find the maximum of three numbers.
from audioop import mul


def max_num(num1, num2, num3):
    return max(num1, num2, num3)


print(max_num(4, 2, 3))

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(num_list):
    if (len(num_list) <= 1):
        return num_list[0]
    else:
        return num_list[0] * mult_list(num_list[1:])


m_list = [2, 5, 6, 4, 1]
print(mult_list(m_list))

# Write a Python function called rev_string() to reverse a string.


def rev_string(string_input):
    return string_input[::-1]


print(rev_string("joey"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.


def num_within(num_check, num_start, num_finish):
    return (num_check >= num_start and num_check <= num_finish)


print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.


def pascal(n):
    # starting value
    prev_row = [1]
    # iterate though n times
    for i in range(0, n):
        print(prev_row)
        # add 1 to existing row
        prev_row.append(1)
        # create blank slate for next row [1,1,1,1,1,1,1,1,...]
        next_row = [1]*(len(prev_row))
        # iterate through the length of the new row size
        for i2 in range(1, len(prev_row) - 1):
            # calculate value for the new row based on the values from previous row
            # don't include 1st or last value (these will be 1)
            next_row[i2] = prev_row[i2 - 1] + prev_row[i2]
        # once for loop is complete assign the newly created row to the previous row vairable so it will be printed next iteration
        prev_row = next_row


pascal(6)
