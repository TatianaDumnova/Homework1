# ДЗ "Перегрузка операторов"
class Building:
    def __init__(self, number, type):
        self.numberOfFloors = []
        self.buildingType = []
        if number:
            self.numberOfFloors.append(number)
        if type:
            self.buildingType.append(type)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building(5, 'cottage')
another_building = Building(3, 'cottage')

if Building.__eq__(self=my_building, other=another_building):
    print('Мы одинаковые')
else:
    print('Мы разные')
