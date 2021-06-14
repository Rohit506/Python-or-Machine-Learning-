# want to import module1 0f package module
import module.module1
module.module1.show()
print(module.module1.mul(10,5))
print("-"*30)

import module.module1 as d
d.show()
print(d.mul(3,6))
print("-"*30)

from module.module1 import show
module.module1.show()
print("-"*30)

from module.module1 import *
module.module1.show()
print(module.module1.mul(10,20))
print("-"*30)

from module import module1
module1.show()
print(module1.mul(5,4))
print("-"*30)

from module import module1 as r
r.show()
print(r.mul(6,5))