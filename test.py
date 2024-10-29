class Cat:
    def __init__(self,name,age):# __int__
        self.name = name #instance attribute
        self.age = age #instance attribute
        
    def __str__(self): #__str__
           return f"Cats name:{self.name} ,Age:{self.age}"
   
cat1 = Cat("tom",4)
print(cat1)

#Example of getters and setters

# class Person:
#     def __init__(self,name,location):
#         self.name= name
#         self._location = location
# #getter method
#     def get_location(self):
#          return self._location

# #setter method
#     def set_location(self,place):
#          self._location = place
         
# faith = Person("Faith","Kericho")
# faith.set_location("Nakuru")
# print(faith.get_location())