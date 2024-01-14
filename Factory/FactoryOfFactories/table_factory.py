from abc import ABCMeta, abstractstaticmethod

class ITable(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_dimentions():
        """ The table interface """


class BigTable(ITable):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class MediumTable(ITable):

    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class SmallTable(ITable):

    def __init__(self):
        self.height = 50
        self.width = 50
        self.depth = 50

    def get_dimentions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class TableFactory():

    @staticmethod
    def get_Table(chairtype):
        try:
            if chairtype == "BigTable":
                return BigChair()
            elif chairtype == "MediumTable":
                return MediumChair()
            elif chairtype == "SmallTable":
                return SmallChair()
        except AssertionError as err:
            print(err)

if __name__ == "__main__":
    TABLE = TableFactory.get_Table("BigTable")
    print(f"{TABLE.__class__} : {TABLE.get_dimentions()}")
    TABLE = TableFactory.get_Table("SmallTable")
    print(f"{TABLE.__class__} : {TABLE.get_dimentions()}")





