from abc import ABCMeta, abstractstaticmethod

class IChair(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimentions():
        """ The chair interface """


class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumChair(IChair):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallChair(IChair):

    def __init__(self):
        self.height = 50
        self.width = 50
        self.depth = 50

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory():

    @staticmethod
    def get_Chair(chairtype):
        try:
            if chairtype == "BigChair":
                return BigChair()
            elif chairtype == "MediumChair":
                return MediumChair()
            elif chairtype == "SmallChair":
                return SmallChair()
        except AssertionError as err:
            print(err)

if __name__ == "__main__":
    CHAIR = ChairFactory.get_Chair("BigChair")
    print(f"{CHAIR.__class__} : {CHAIR.get_dimentions()}")
    CHAIR = ChairFactory.get_Chair("SmallChair")
    print(f"{CHAIR.__class__} : {CHAIR.get_dimentions()}")





