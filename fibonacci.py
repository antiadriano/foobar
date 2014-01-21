#!/usr/bin/env python

# Print Fibonacci sequence to n number
# @antiadriano 2014

def getFibonacci(number):
   a, b = 0, 1
   for i in range(number):
      print str(b),
      a, b = b, a+b


def main():
   inputNumber = raw_input("Type the limit for your fibonacci sequence: ");
   try:
      inputNumber = int(float(inputNumber))
      if inputNumber > 0:
         getFibonacci(inputNumber)
      else:
         print "Enter a positive number"
   except ValueError:
      print "Enter a valid integer"

if __name__ == "__main__":
   main()

