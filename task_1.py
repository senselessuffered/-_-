import csv ## импортируем нужные библиотеки
'''Начинаем перенос файла в переменную games'''
with open('/home/student/Рабочий стол/Предпроф/game.txt',encoding='utf-8') as file:
    games = list(csv.reader(file,delimiter='$',quotechar='"'))[1:]
    new_game=[] ## для новых данных
    for gamename,character,error,data in games:
        if '55' in error: ## проверяем наличие 55
            print(f'У персонажа\t{character}\tв игре\t{gamename}\tнашлась ошибка с кодом:\t {error}.\tДата фиксации:\t {data}')
            new_game.append([gamename,character,'Done','0000-00-00'])
        else:
            new_game.append([gamename,character,error,data])
            
'''Записываем новые данные в новый файл'''
with open('/home/student/Рабочий стол/Предпроф/game_new.csv','w',encoding='utf-8',newline='') as file:
    new=csv.writer(file,delimiter='$')
    new.writerow(['GameName','characters','nameError','date'])
    new.writerows(new_game)
    



