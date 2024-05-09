# Exercise 1
# Your solution comes here
five_digit = int(input("Please enter a five digit number:"))
ones = five_digit%10
tenths = (five_digit//10)%10
hundreths = (five_digit//100)%10
thousenths = (five_digit//1000)%10
ten_thousenths = (five_digit//10000)%10
first_section = str(ones+hundreths+ten_thousenths)
second_section = str(tenths+thousenths)
print(first_section+second_section)