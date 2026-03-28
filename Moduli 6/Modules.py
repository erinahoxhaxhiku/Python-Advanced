from packages import module1 as m1
from packages import module2 as m2
from packages import module3 as m3
import emoji

import my_math

from my_math import sq

result =my_math.square(5)
print(result)


result2 = square(4)
print(result2)

print(m1.hello())
print(m2.greet())
print(m3.welcome())

print(emoji.emojize("Python is fun :snake:"))