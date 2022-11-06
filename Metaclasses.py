# Changing the way how the objects (also classes in that case) are modified 
# during their construction 

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        # this magic method is called before __init__
        # so here we can modify the object during the creation
        print(attrs)
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name]=val
            else:
                a[name.upper()]=val
        
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
#print(d.hello())  # !! Error because Dog object has no attribute 'hello'
print(d.HELLO())   # Successfully print 'hi' because we've modified the method during the creation of the object
