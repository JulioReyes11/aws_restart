""" Challenge Lab two: Python Scripting Exercise for the AWS reStart platform. 
The script displays the prime numbers between a range (1, 250) and 
stores the results at:  https://en.wikipedia.org/wiki/Prime_number"""

import sys

def is_prime(number):
  if number < 2:
    return False

  for i in range (2, number):
    if number % i == 0:
      return False
  return True

def main():
    print("""
    A prime number is a whole number greater than 1 whose 
    only factors are 1 and itself. A factor is a whole number that 
    can be divided evenly into another number. 
    The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
    """)
    
    while True:
        print('Enter a number')
        response = input('> ')
        if response.isdecimal():
            number = int(response)
            break
        
    with open('results.txt', 'w') as file:
        sys.stdout = file
        
        for number in range(1, number + 1):
            if is_prime(number):
                print(number, end=' ')
    
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    main()