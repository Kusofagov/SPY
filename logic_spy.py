numberOfGamers = int(input("Введите число игроков: "))  # Пользователь вводит данные
numberOfAgents = int(input("Введите число шпионов: "))

a = numberOfGamers > numberOfAgents  # Проверим, чтобы шпионов не было больше, чем игроков
if a == True:
    import random  # Перемешаем и выберем случайную локацию
    listOfLocation = ["Библиотека", "Подвал", "Завод", "Супермаркет", "Стадион", "Спортивный зал", "Тюрьма", "ВУЗ", "Офис", "Рынок", "Вокзал", "Больница", "Ресторан", "Отель", "Метро", "Аэропорт"]
    random.shuffle(listOfLocation)
    location = random.choice(listOfLocation)
    gamers = []  # Создадим список игроков
    for i in range(numberOfGamers):
        gamers.append(i+1)
    agents = random.sample(gamers, k = numberOfAgents)  # Выбираем шпионов из числа игроков
    for i in range(numberOfAgents):  # Удалим шпионов из распространения слов
        gamers.insert(agents[i],0)
        gamers.pop(agents[i]-1)
    for i in range(numberOfGamers): # Распределим слова
        answer = int(input("Вы готовы узнать тайну? Введите \"1\": "))
        if answer == 1:
            if gamers[i] != 0:
                print(location, "\nПередай устройство следующему игроку")
            else:
                print("Ты шпион - удачи!\nПередай устройство следующему игроку")
        else:
            print("Не хочешь - как хочешь!")
else:
    print("Число игроков не может быть меньше, чем число шпионов\nНеобходим перезапуск игры")