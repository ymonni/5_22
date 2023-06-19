#Ymonni Simms 2106646

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
ser1 = input("Select first service:\n")
ser2 = input("Select second service:\n")
print()
print("Davy's auto shop invoice")
print()

sum = 0

if ser1 == 'Oil change':
  sum += 35
  print('Service 1: Oil change, $35')
elif ser1 == 'Car wax':
  sum += 12
  print('Service 1: Car wax, $12')
elif ser1 == 'Car wash':
  sum += 7
  print('Service 1: Car wash, $7')
elif ser1 == 'Tire rotation':
  sum += 19
  print('Service 1: Tire rotation, $19')
else:
  print('Service 1: No service')

if ser2 == 'Oil change':
  sum += 35
  print('Service 2: Oil change, $35')
elif ser2 == 'Car wax':
  sum += 12
  print('Service 2: Car wax, $12')
elif ser2 == 'Car wash':
  sum += 7
  print('Service 2: Car wash, $7')
elif ser2 == 'Tire rotation':
  sum += 19
  print('Service 2: Tire rotation, $19')
else:
  print("Service 2: No service")

print()
print("Total: $", end='')
print(sum)
