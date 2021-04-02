from Company import Company
from math import cos,sin,tan
import numpy as np

class Person:

  def __init__(self):
    self._name = "Tom"
    self._age = 5
    self.company = Company()

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, newName):
    self._name = newName

  @property
  def age(self):
    return str(self._age)

  @age.setter
  def age(self, newAge):
    self._age = newAge

  def displayPerson(self):
    arr1 = np.array([-3.7, -1.2, 0.5, 4.5])
    return "name: " + self.name + ", age: " + self.age + "," + self.company.displayEmployer() + "," + "{0}".format(cos(1)) + "," + str(arr1[0])


