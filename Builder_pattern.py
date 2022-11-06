
# class Address:

#     def __init__(self, zip, street):
#         self.zip = zip
#         self.street = street

    
# class User:

#     def __init__(self, name, age, phone, address):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.address = address


# # This is really dificult to understand and it's not a good way. That's why the builder comes in.
# address1 = Address('1', 'Main')
# user = User('Bob', None, None, address1)

# print(user)


# ---------------------
#  WITH Builder pattern
# ---------------------

class User:

    def __init__(self, name):
        self.name = name


class UserBuilder:

    def __init__(self, name):
        self.user = User(name)

    def setAge(self, age):
        self.user.age = age
        return self

    def setPhone(self, phone):
        self.user.phone = phone
        return self

    def setAddress(self, address):
        self.user.address = address
        return self

    def build(self):
        return self.user


user = UserBuilder('Bob').setAge(30).build()
print(user.name)
print(user.age)


