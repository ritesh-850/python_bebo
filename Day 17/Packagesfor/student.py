class Stu:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(f"name:{self.name},id:{self.id}")

obj1 = Stu("David",101)
obj1.display()