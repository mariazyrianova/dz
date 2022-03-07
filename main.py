#1,2
name1='Мария'
age1='18'
print('Меня зову', name1, 'мне', age1, 'лет')

#3
name3='Мария'*5
print(name3)

#4
name4=input('Как вас зовут?')
age4=input('Сколько вам лет?')
print('Привет,', name4 , '!', 'Какой прекрасный возраст!')

z=int(input('Сколько вам лет?'))
if 18<=z<=25:
    print('хаххаха')
if 26<=z<=45:
    print('хехехеххе')
if z>=46:
    print('Вы слишком старый!')

#6
name6=input('Введите свое имя:')
text1=name6[2:-2:]
text2=name6[::-1]
text3=name6[-4:]
text4=name6[:6]
print(text1, text2, text3, text4)


#7
name7=input('Введите имя:')
age7=int(input('Введите возраст:'))
pr=1
q1=age7//100
q2=age7//10%10
q3=age7%10
while age7>0:
    digit=age7%10
    pr*=digit
    age7//=10
print(q1+q2+q3, pr, len(name7))

#8
name8=input('Введите имя:')
print(name8.title(),  name8.capitalize())

#9!!!!!!!!!!!!1
age9=int(input('Введите возраст:'))
if age9>150 or age9<0:
    print('Ошибка!')
else:
    print('Все верно')

#10
r=int(input('Вычислите 8/2(2+2)='))
if r==16:
    print('Все верно')
else:
    print('Ошибка!')
