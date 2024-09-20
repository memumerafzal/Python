import math
import os
import random
import re
import sys


# Taking 4 comma-separated integers
comma_separated_numbers = list(map(int, input("Please enter 4 comma-separated numbers: ").split(',')))

# Processing each of the comma-separated numbers
for number in comma_separated_numbers:
    if number % 2 != 0:  # If the number is odd
        print(f"{number}: Weird")
    elif number % 2 == 0:  # If the number is even
        if 2 <= number <= 5:  # Inclusive range of 2 to 5
            print(f"{number}: Not Weird")
        elif 6 <= number <= 20:  # Inclusive range of 6 to 20
            print(f"{number}: Weird")
        elif number > 20:  # Greater than 20
            print(f"{number}: Not Weird")
