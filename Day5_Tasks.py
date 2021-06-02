# Class Example
class myclass:
    def function(self):
        print('Hello')

    def function2(self, name):
        print('Name Is : ' + name)


myc = myclass()
myc.function()
myc.function2('Harsh Parmar')


# sum of 2 numbers Using Class

class Sum:
    def fun1(self, n1, n2):
        ans = n1 + n2
        print('Ans Is :', ans)


s1 = Sum()
s1.fun1(10, 20)


# Constructor Example

class construct:
    def __init__(self):
        print("Hello World.")


m1 = construct()


# Parameterized Construct Example

class para:
    def __init__(self, name):
        print("Value is :", name)


m2 = para("Harsh Parmar.")


# Assign String Value to Class Variable Using Method

class string:
    name = ""

    def funct1(self):
        print("Hello Function1")

    def funct2(self, name):
        self.name = name

    def funct3(self):
        print("Value Is ", self.name)


f1 = string()
f1.funct1()
f1.funct2("IMHP")
f1.funct3()


# Assign String Value to Class Variable Using Constructor
#Task
class str:
    nam = ""

    def __init__(self,nam):
        self.nam= nam

    def funct1(self):
        print("Name is :",self.nam)
my = str("Kakaroth")
my.funct1()

#Task2
class myclas:
    a1 = 0
    a2 = 0

    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2

    def fun2(self):
        ans = self.a1 + self.a2
        print("Ans is : ",ans)

clas = myclas(10,20)
clas.fun2()

#Single level inheritance

class parent:
    #Define Parent Class
    def __init__(self):
        print("Calling Parent Constructor")

    def parentmethod(self):
        print("Calling Parent Method")

#Define Child Class

class child(parent):
    def __init__(self):
        print("Calling Child Constructor")

    def childmethod(self):
        print("Calling Child Method")

c = child()                 #object of Child
c.childmethod()             #Child Class method
c.parentmethod()            #Parent Class method

#multi level inheritence

class parent2:

# Define parent class
    def __init__(self):
        print("Calling Parent Constructor(MLI)")

    def parentmethod2(self):
        print("Calling Parent Method(MLI)")

#Define child class

class child2(parent2):

    def __init__(self):
        print("Calling child constructor(MLI)")

    def childmethod2(self):
        print("Calling child method(MLI)")

#Define subchild class

class subchild(child2):

    def __init__(self):
        print("Calling subchild constructor(MLI)")

    def subchildmethod(self):
        print("Calling subchild method(MLI)")

sc = subchild()
sc.subchildmethod()
sc.childmethod2()
sc.parentmethod2()

#Multiple Inheritance

class myparentclass():

    def method_parent1(self):
        print("Parent1 method called")

#define parent class2

class myparentclass1():

    def method_parent2(self):
        print("Parent2 Method Called ")

#define child class

class childclass(myparentclass, myparentclass1):

    def child_method(self):
        print("Child Method")

c = childclass()
c.method_parent1()
c.method_parent2()
c.child_method()

#Hirearchical Inheritance

class parent3:

    def __init__(self):
        print("Calling parent3 constructor")

    def parentmethod3(self):
        print("Calling parent3 method")

#define child class

class child3(parent3):

    def __init__(self):
        print("Calling child3 constructor")

    def childmethod3(self):
        print("Calling child3 method")

#Define subchild class

class child3(parent3):

    def __init__(self):
        print("Calling child3 constructor")

    def childmethod3(self):
        print("Calling child3 method")

sc1 =  child3()
sc1.childmethod3()
sc1.parentmethod3()

#hybrid Inheritance

class mpc1:

    def method_pr1(self):
        print("Parent method called")

#Define parent class2

class mpc2:

    def method_pr2(self):
        print("parent2 method called")

#define child class

class cc3(mpc1, mpc2):
    def child_method(self):
        print("Child Method")

#define child class2

class cc4(mpc1):

    def c_method2(self):
        print("Child Method2")

c2 = cc3()
c2.method_pr1()
c2.method_pr2()
c2.child_method()

c2= cc4()
c2.c_method2()
c2.method_pr1()


#Overriding method

class parent_class():

    def function6(self):
        print("Parent method called")

#define child class

class child_class5(parent_class):

        def funt1(self):
            print("child method called")

c5 = child_class5()
c5.funt1()

#Overloading method

class my_class:

    def sum3(self,x,y):
        ans = x+y
        print("Ans is :",ans)

    def sum3(self,x,y,z):
        ans = x+y+z
        print("Ans is :",ans)

p=my_class()
#p.sum3(10,20)
p.sum3(10,20,30)

