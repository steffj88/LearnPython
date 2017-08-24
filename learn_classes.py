
import class_Person as cp

person1=cp.Person('Steffen',85)
child1=cp.Child("Lisa", 50, 15)

print(child1.name)

print(cp.Person.__doc__)

print(cp.Child.__doc__)

person1.health()


if person1.weight > 40:
    print (person1.weight)
    print('The name of the object in question is', person1.name)

else:
        print('The person is probably underweight')



