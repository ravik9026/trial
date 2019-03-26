bike=['trek', 'redline', 'giant']
print(bike[0])
print(bike[-1])
for bike in bike:
    print(bike, end=" ")
print()
print('\n')
#adding item to list

bikes=[]
bikes.append('hero')
bikes.append('yamaha')
print(bikes)

#marking numerical list

squares=[]
for x in range(1,10):
    squares.append(x**2)
print(squares)

#list comprehension
square=[x**2 for x in range(1,11)]
print(square)

#slicing of list
finishers=['sam', 'bob', 'ada', 'bea']
print(finishers[-2:])

#copy of list

bike_copy=bike[:]
print(bike_copy)



