# if we want to members of module in our program, then we should import that module. our module name was 'abt'
# now we can access the members using module name
'''import abt
print(abt.x)
abt.add(10,20)
abt.product(20,30)'''

# now 'aliasing' (rename) the module name. once we defined as alias name, then shuld be use alias name only
'''import abt as a
print(a.x)
a.add(5,6)
a.product(10,20)'''

# now import with using module name
'''from abt import x,add
print(x)
add(30,40)'''
#or import all members of module using '*'
'''from abt import *
print(x)
add(40,50)
product(90,90)'''

'''import time
from imp import reload
import abt
time.sleep(5)
reload(abt)
time.sleep(5)
reload(abt)
time.sleep(5)
reload(abt)'''
# if we are import the module multiple times it gives an output only once. But we want multiply times updated output
#then we should use the above program using 'reload', which was import => 'from imp import reload'
'''import abt
import abt
import abt
print("This is test.py module")'''

# we want to know all the members of module then use 'print(dir(module-name))' and for current module use 'print(dir())'
'''import abt
print(dir(abt)) # it will show all the members of 'abt.py' module
a="akash"
def division(a,b):
    print("Division=>\t",a%2)
print(dir()) # it will show the members of current 'test.py' modules
print(__builtins__ )
print(__cached__ )
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)
print(__spec__)'''

'''from abt import *
print(__name__)
print()
def f1():
    print("This is test.py module")
    print(__name__)
f1()'''

import random
help(random)
