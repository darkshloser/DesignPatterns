



class Old:
    def get(self):
        return "123"


class New:
    def get(self):
        return 123


class Adapter:
    def __init__(self, cls):
        self.cls = cls

    def get(self):
        return str(self.cls.get())


def main(obj):
    print("The result is: " + obj.get())


if __name__ == "__main__":
    # obj = Old() # str and it works 
    # obj = New()   # when we switch to New it trows an error
    obj = Adapter(New())
    main(obj)

