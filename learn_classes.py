
import class_Person as cp

person1=cp.Person('Steffen',50)

print(cp.Person.__doc__)

if person1.weight > 40:
    print (person1.weight)
    print('The name of the object in question is', person1.name)

else:
        print('The person is probably underweight')



