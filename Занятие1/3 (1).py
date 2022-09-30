print("Имя: ")
name=input()
if name=="Иван":
    print("Тебе здесь не рады")
else:



    print("Возраст: ")
    age=int(input())
    if age>0 and age<75:
        if age >= 16:
            print("Поздравляем вы поступили в ВГУИТ")
        else:
            print("Сначала нужно окончить школу!")
    else:
        print("Иди на пенсию!")
    