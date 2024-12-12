class Emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"name:{self.name},salary:{self.salary}")

obj = Emp("David",2500)
obj.display()
