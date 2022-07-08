# HW#7 - Classes
######################

# importing Abstract Base Classes library and abstractmethod from it
from abc import ABC, abstractmethod


# defining class Figure with self attrs - name, coordinate, team
class Figure(ABC):
    def __init__(self, name: str, coordinate: tuple, team: str):
        self.name = name
        self.coordinate = coordinate
        self.team = team

# adding empty abstract method check_cell which should be redefined in class descendants
    @abstractmethod
    def check_cell(self):
        pass

# adding property method to return a string with current info about a figure
    @property
    def display_name(self):
        return f"{self.name} ({self.team}) {str(self.coordinate)}"

# adding a class method for creating a new instance for child classes of Figure class
# with attributes received from values of imported dict
    @classmethod
    def create_from_dict(cls, figure_dict):
        print("Creating new figure from dict:\n", figure_dict)
        return cls(name=figure_dict.get("FNAME"),
                   coordinate=figure_dict.get("FCOORDINATE"),
                   team=figure_dict.get("FTEAM"))


# creating Horse - a child class to Figures and redefining (overriding) method check_cell
# from abstract class, which "moves" a figure to new position by assigning a new coordinate
class Horse(Figure):
    def check_cell(self, new_coordinate):
        self.coordinate = new_coordinate
        print("Moved Horse to new coordinate:", self.display_name)
        pass


# creating Pawn - a child class to Figures and redefining method check_cell
# for moving instances of this class to new coordinate
class Pawn(Figure):
    def check_cell(self, new_coordinate):
        self.coordinate = new_coordinate
        print("Moved Pawn to new coordinate:", self.display_name)
        pass


figure_dict = {
    "FNAME": "Horse 1",
    "FCOORDINATE": (2, 2),
    "FTEAM": "black"
}

print("Implementation of abstract class Figure with abc method for changing coordinates.\n")

# creating new figure by class method which takes attributes from values of figure_dict
horse_1 = Horse.create_from_dict(figure_dict)
print(horse_1.display_name)

print("\nCreating new figures in ordinary way:")
horse_2 = Horse("Horse 2", (1, 1), "black")
print(horse_2.display_name)
pawn_1 = Pawn("Pawn 1", (5, 5), "white")
print(pawn_1.display_name)

# moving created figures by changing their coordinates
print("\nMoving figures by defining new coordinates:")
horse_1.check_cell((4, 5))
pawn_1.check_cell((7, 7))
