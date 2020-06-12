import greet
import math
print(greet.hello1('김영진'))
print(math.sqrt(100))

import greet as gr
import math as m
print(gr.hello2('박소정'))
print(m.sqrt(100))

from greet import hello3
from math import sqrt
print(hello3('한은정'))
print(sqrt(100))

from greet import *
from math import *
print(hello2('한은정'))
print(sin(1))