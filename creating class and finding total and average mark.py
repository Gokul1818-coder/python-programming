class student_mark:
     def __init__(self,a,b,c,m1,m2,m3):
          self.sno=a
          self.name=b
          self.age=c
          self.tamil=m1
          self.english=m2
          self.maths=m3
     def calculate(self):
        self.total=self.tamil+self.english+self.maths
        self.average=self.total/3
        if(m1>=40 and m2>=40 and m3>=40):
            self.result="pass"
        else:
            self.result="fail"

     def disp(self):
          print("student sno:",self.sno)
          print("student name:",self.name)
          print("student age:",self.age)
          print("tamil mark is:",self.tamil)
          print("english mark is:",self.english)
          print("maths mark is:",self.maths)
          print("total mark is:",self.total)
          print("average mark is:",self.average)
          print("result is:",self.result)

a=int(input("enter the number"))
b=input("enter the name")
c=int(input("enter the age"))
m1=int(input("enter the mark of tamil"))
m2=int(input("enter the mark of english"))
m3=int(input("enter the mark of maths"))

ob=student_mark(a,b,c,m1,m2,m3)
ob.calculate()
ob.disp()
