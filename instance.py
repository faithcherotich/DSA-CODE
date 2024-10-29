# class Person:
#     # __int___ method the constructor
#   def __init__(self,name,location):
#       self.name = name #instance attribute
#       self._location = location # instance attribute
      
#   def say_hi(self):
#       return f"Hello,my name is:{self.name} , My location is:{self._location}"
#   #getter
#   def get_location(self):
#       return self._location
  
#   #setter
#   def set_location(self,place):
#       self._location = place
      
      
# #invoke by creating a new class name
# person1 = Person("Faith","Kericho")
# person1.set_location("JERICHO")
# print(person1.set_location())
# print(person1.say_hi())
# class Car:
#     def __init__(self,color,year,owner):
#         self.color = color
#         self.year = year
#         self._owner = owner
        
#     def make_is(self):
#         return f"My car color is:{self.color} , Year is {self.year}, Owner: {self._owner}"
#     def get_owner(self):
#         return self._owner
#     def set_owner(self,person):
#         self._owner = person
       
# car1 = Car("blue",2020,"Faith")
# car1.set_owner("mutai")
# # print(car1.make_is())    
# print(car1.get_owner())
#setters and getters
class Cat:
    def __init__(self,age =0):
        self._age = age
     
    #getter method
    def get_age(self):
        return self._age
    #setter method
    def set_age(self,new_age):
        self._age = new_age
tom = Cat()  
    
#set age using setter
tom.set_age(12)
print(tom.get_age())
# print(tom._age)
