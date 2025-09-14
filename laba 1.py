age=6
name='Dima'
surrender=5.6
choice=True
list=[1,6,2,"Heloo",5]
set={1,6,7,"Dima", 12}
tuple=(1,7,9,40,734,98,367)
dictionary={1: "Lutsk"}

age+=1#додавання до вже присвоєного
surrender-=3#віднімання від вже присвоєного
name*=3#домноження на вже присвоєне
surrender/=1#ділення на вже присвоєне
age**=1#до піднесення до степеня

print(age+surrender)#додавання
print(surrender-age)#віднімання
print(age*name)#множення
print(age/surrender)#ділення
print(age%surrender)#повертає остачу після ділення
print(age**surrender)#зведення в степінь
print(age//surrender)#ділення без остачі

print('age', type(age), age)
print('name', type(name), name)
print('surrender', type(surrender), surrender)
print('choice', type(choice), choice)
print('list', type(list), list)
print('set', type(set), set)
print('tuple', type(tuple), tuple)
print('dictionary', type(dictionary), dictionary)
