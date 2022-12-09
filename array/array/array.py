
print("Mason Hall")

cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']

print(cars)

x = len(cars)
print(x)

cars.append('Buick')

print(cars[3])

cars.insert(2, 'Toyota')

print(cars)

cars.pop(4)

print(cars)

cars.sort()

print(cars)

cars.sort(reverse=True)
print(cars)

my_array_length = len(cars)

array_string = 'The length of my array is: '

print(array_string, my_array_length)