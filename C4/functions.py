def maxof2(a, b):
# Check if a is greater than b
    if a > b:
# If a is greater, return the value of a
        return a
    else:
# If b is greater or equal, return the value of b
        return b
def maxof3(a, b, c):
# frst it finds the maximum value between b and c using maxof2
# Then, compare the maximum value between a and the result from the previous step
    return maxof2(a, maxof2(b, c))
# Call the maxof3 function with arguments 3, 6, and 23
print(maxof3(3, 6, 23))