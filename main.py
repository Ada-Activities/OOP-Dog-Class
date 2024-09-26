class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    print(self.name + " is now sitting")

  def roll_over(self):
    print(self.name + " rolled over!")


dog_1 = Dog("Fidough", 4)
dog_2 = Dog("Growlithe", 7)

dog_1.sit()
dog_2.roll_over()
