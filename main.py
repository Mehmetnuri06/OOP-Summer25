class Person:
  def __init__(self, name, age, adress):
    self.name = name
    self.age = age
    self.adress = adress

p1 = Person("mehmet", 22, "wilcza")

print(p1.name)
print(p1.age)
print(p1.adress)

class student:
   def __init__(self , name , index_number,last_name,nationality):
    self.name = name
    self.index_number = index_number
    self.last_name = last_name
    self.nationality = nationality
p2 = student("frank" ,347, "speed", "America")

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)
 

p2 = student("nuri" ,245, "killer", "brasil")

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)


p2 = student("michael" ,212, "reyhold", "Italy")

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)