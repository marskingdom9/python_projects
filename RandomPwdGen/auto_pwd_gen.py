# This file will generate a random password using python when run

import random
import string

total = string.ascii_letters + string.digits + string.punctuation

len = 16

""" A random password of len (16) with ASCII letters, digits, 
and special characters will be displayed to the console"""

password = "".join(random.sample(total, len))

print(password)