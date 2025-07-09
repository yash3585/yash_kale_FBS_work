class Student:
    def __init__(self,id=None,name=None,age=None,persentage=None):
        self.id = id
        self.nm = name
        self.age = age
        self.per = persentage

    def display(self):
        print("Student id:",self.id) 
        print("Student name:",self.nm)
        print("Student age:",self.age)
        print("Student persentage",self.per) 
        print("################")

    def Accept(self):
        self.id = int(input("Enter The Student Id:"))
        self.nm = input("Enter The Student Name:")
        self.age = int(input("Enter the Student Age:"))
        self.per = float(input("Enter The Student Percentage:"))      
        
    
    def Rank(self):
        if self.per > 90:
            print("Rank A")
        elif self.per > 60:
            print("Rank B") 
        elif self.per > 30:   
            print("Rank C")
        else:
            print("Rank D") 

    def __str__(self):
        return f'Id: {self.id}\nName: {self.nm}\nAge: {self.age}\nPersentage {self.per}'

class Medical(Student):
    def __init__(self, id=None, name=None, age=None, persentage=None, specilization=None,intership_m=None):
        super().__init__(id, name, age, persentage)
        self.bra = specilization
        self.inte = intership_m

    def display(self):
         super().display() 
         print("Branch :",self.bra)
         print("Internal Marks :",self.inte)

    def Accept(self):
         super().Accept()
         self.bra = input("Enter A Branch:") 
         self.inte = int(input("Enter The Internal Marks:"))


    def Rank(self):  
        if self.per > 20:
            print("Rank A")
        elif self.per > 15:
            print("Rank B") 
        elif self.per > 10:   
            print("Rank C")
        else:
            print("Rank D") 

s1 = Medical()
s1.Accept()
s1.display()
s1.Rank()
print(s1)