class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    print(self.name + " is now sitting")

  def roll_over(self):
    print(self.name + " rolled over!")


dog1 = Dog("Fidough", 4)
dog2 = Dog("Growlithe", 7)

dog1.sit()
dog2.roll_over()