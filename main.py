n=int(input('количество билетов'))
stoimost=0

for i in range(n):
    age=int(input('возраст'))
    if 0<age<18:
        print('Бесплатный вход')
        stoimost += 0
    if 18 <=age< 25:
        print('Стоимость одного билета: 990 руб.')
        stoimost += 990
    elif 25 <=age<= 100:
        print('Стоимость одного билета: 1390 руб.')
        stoimost += 1390
    elif age > 100 or age <= 0:
        raise ValueError("Вам не может быть столько лет")

if n > 3 and stoimost >= 3960:
    stoimost = (stoimost)-(stoimost*10/100)
else:
    stoimost = stoimost
print ("Цена с учетом скидки:"f'{stoimost} руб.')





