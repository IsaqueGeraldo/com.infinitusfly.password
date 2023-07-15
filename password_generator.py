import string
import random

letters = string.ascii_letters
digits = string.digits
symbols =  '@#$%&*/\?'

alphabet = letters+digits+symbols
length = 15

password = "".join(random.sample(alphabet, length))

print(password)