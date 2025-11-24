class Student:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
    def grade(self):
        if int(self.marks)>=90:
            print(self.name,"got an A grade")
        elif int(self.marks)>=75:
            print(self.name,"got B grade")
        else:
            print(self.name,"got a C grade")
    def eligible(self):
        if int(self.age)>=18:
            print(self.name,"is eligible to vote")
        else:
            print(self.name,"is NOT eligible to vote")
s1=Student("Moideen","34","17")
s2=Student("subaida","98","19")
s3=Student("sakeenah","77","18")
s1.grade()
s2.grade()
s3.grade()
s1.eligible()
s2.eligible()
s3.eligible()
