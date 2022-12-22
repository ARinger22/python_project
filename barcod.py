from barcode import EAN13
from barcode.writer import ImageWriter 
import random

number1 = random.randint(1000000000000,9999999999999)
number = str(number1)
my_code = EAN13(number,writer=ImageWriter())
print(my_code.save("new_code2"))