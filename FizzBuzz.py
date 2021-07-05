#Write your code below this row 👇
''' You are going to write a program that automatically prints the solution to the FizzBuzz game. 

>`Your program should print each number from 1 to 100 in turn.` 

>`When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

>`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"` '''


for number in range(1,101):
  a = number % 3
  b = number % 5
  if a==0 and b==0:
    print("FizzBuzz")
  elif a==0:
    print("Fizz")
  elif b==0:
    print("Buzz")
  else:
    print(number)
