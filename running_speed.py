distance = float(input("Введите дистанцию в км: "))
time = float(input("Введите время в минутах: "))

speed = (distance * 1000) / (time * 60)

print("Скорость бега: {:.2f} м/мин".format(speed))
