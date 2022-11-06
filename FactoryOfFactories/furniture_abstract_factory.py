from abc import ABCMeta, abstractstaticmethod
from chair_factory import ChairFactory
from table_factory import TableFactory

class IFurnitureFactory(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_furniture():
        """ The static function factory interface method """


class FurnitureFactory(IFurnitureFactory):

    @staticmethod
    def get_furniture(furniture_type):
        try:
            if furniture_type in ["BigChair", "MediumChair", "SmallChair"]:
                return ChairFactory.get_Chair(furniture_type)
            elif furniture_type in ["BigTable", "MediumTable", "SmallTable"]:
                return TableFactory.get_Table(furniture_type)
        except AssertionError as err:
            print(err)
        return None


if __name__ == "__main__":
    FURNITURE = FurnitureFactory.get_furniture("SmallChair")
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimentions()}")

