#approach 1
import a
import b
obj = a.Animal()
obj.display()

obj = b.Bird()
obj.display()

#approach 2
from a import *
from b import *
obj = Animal()
obj.display()

obj = Bird()
obj.display()
