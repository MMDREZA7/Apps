number_list = []
kollan = int(input('Chantaan kollan: '))
# number = int(input('insert a number: '))
# number_list.append(number)
majmoo = 0

# baghimandeh = len(number_list) - number
# majmoo += number
# print('majmoo = ',majmoo)
# print(number_list)

for i in range(kollan) :
    number = int(input('insert a number: '))

    while number < 0 or number > 20:
        print('!!! 0 < your number < 20 !!!')
        number = int(input('insert a number: '))

    number_list.append(number)
    majmoo += number

moadel = majmoo / kollan
print('Majmoo = ',majmoo)
print()
print(f'average: {moadel}')
   
print()
input()

