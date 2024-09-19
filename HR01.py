import math
import os
import random
import re
import sys


n = int(input().strip())

if n % 2 != 0:  # If n is odd
    print("Weird")
elif n % 2 == 0:  # If n is even
    if 2 <= n <= 5:  # Inclusive range of 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:  # Inclusive range of 6 to 20
        print("Weird")
    elif n > 20:  # Greater than 20
        print("Not Weird")
