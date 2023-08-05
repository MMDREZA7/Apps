per_hour = int(input('please enter your per_hour: ' ))
hour = int(input('please enter your hour: '))
Name = input('please enter your name: ')

def work(a, b) :
    kol = a * b
    return kol

print('Hi',Name)

print(f'name: {Name}')
print(Name)

kol = int(work(hour,per_hour))
print(f'daryafty: {kol}')
print(work(hour,per_hour))


if kol > 20 :
    print('ziad kaar kardi')
    print('very Thanks')

elif kol < 5 :
    print('az farda digeh nemikhad biaie')

else:
    print('babete kaar kardanet barayeh ma Thanks')

print('bye',Name)
# print('bye ' + Name)
print()
print()

input('plaese press enter')


























