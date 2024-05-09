# Exercise 2
# Your solution comes here
three_digit = int(input("Please enter a three digit number:"))
ones = three_digit%10
tenths = (three_digit//10)%10
hundreths = (three_digit//100)%10
sum = (ones+tenths+hundreths)
print(sum)