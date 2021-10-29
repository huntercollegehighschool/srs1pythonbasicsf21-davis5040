"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""
import math
from math import sqrt
from math import floor

def isprime(number):
  for i in range(2,floor(sqrt(number))):
    if number % i == 0:
      return False
  return True