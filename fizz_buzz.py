#  Title: FizzBuzz
#
#  Description: A program that takes a number.
#               If the number is divisible by 3, it will print “Fizz”.
#               If it is divisible by 5, it will print “Buzz”.
#               If it is divisible by both 3 and 5, it will print “FizzBuzz”.
#               Otherwise, it will print the same number.
#
#  Author: Kefas Kingsley (KC)
#
#  Date: 13/05/2020


# Take the input from the user
num = int(input("Input a number:\n>>"))

# We use floor division to see if it can be perfectly divided by 3 or 5 or both

# for both
if num % 3 == 0 and num % 5 == 0:
  print("FizzBuzz")
  
# for 3
elif num % 3 == 0:
  print("Fizz")  

# for 5
elif num % 5 == 0:
  print("Buzz")


# if the number cannot be perfectly divided by 3 or 5
else:
  print(num)