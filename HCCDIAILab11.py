# Ek simple tuple banate hain

#Mutable Data Types: List, Set, Dictionary
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# # Inka id() HAMESHA alag hoga
# print(id(list1)) 
# print(id(list2))

# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)  
# print(id(tuple1))
# print(id(tuple2))
# # Inka id() HAMESHA same hoga

# set1 = {1, 2, 3}
# set2 = {1, 2, 3}
# print(id(set1))
# print(id(set2))

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'a': 1, 'b': 2}
# print(id(dict1))
# print(id(dict2))

# dict1 = { }
# print(id(dict1)) # <class 'dict'>
# No matter empty brackets are used, 
# the id() will always gives the memory location. 

# boolean1 = True
# boolean2 = True
# print(id(boolean1)) # <class 'bool'>
# print(id(boolean2)) # <class 'bool'>
# Boolean Data Type is not immutable, 
# So the id() will not change memory location.

class Car: #Global
    def __init__(self,make,model): # __ Init__ is a constructor method that initializes the attributes of the class
        self.make = make #Self is keyword that refers to the current instance of the class. It is used to access the attributes and methods of the class.
        self.model = model

new_car = Car("Toyota", "Camry") #Global Printing the attributes of the new_car object.
print(new_car.make)  # Output: Toyota
print(new_car.model)  # Output: Camry