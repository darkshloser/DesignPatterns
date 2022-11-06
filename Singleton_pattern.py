
# First Way to creat SINGLETON implementation 
# in that case user is enforced to use 'getInstance' method instead of just 'Singleton()'

# class Singleton:

#     __instance = None

#     @staticmethod
#     def getInstance()
#         if Singleton.__instance == None:
#             Singleton()
#         return Singleton.__instance

#     def __init__(self):
#         if Singleton.__instance != None:
#             raise Exception("Singleton exists already!")
#         else:
#             Singleton.__instance = self


# s1 = Singleton.getInstance()
# print(s1)

# s2 = Singleton.getInstance()
# print(s2)



# Second way to create SINGLETON implementation and in that case 
# we'll be able to use 'Singleton()' to have the instance, which is more intuitive


class Singleton:

    __instance = None

    def __new__(cls):

        if (cls.__instance is None):
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance

s1 = Singleton()
print(s1)

s2 = Singleton()
print(s2)
